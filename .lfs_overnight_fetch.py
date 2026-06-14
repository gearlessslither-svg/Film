#!/usr/bin/env python3
"""Bypass the hanging git-lfs client: fetch all LFS objects directly.

Reads pointer files in the working tree, gets a fresh auth token via
`ssh ... git-lfs-authenticate`, calls the batch API (no proxy), and downloads
each object straight from its presigned href into .git/lfs/objects.
"""
import json, os, subprocess, sys, urllib.request, hashlib, time, threading
from pathlib import Path

REPO = Path("/Users/jaychoupp/Desktop/Story/Film")
LFS_OBJ = REPO / ".git/lfs/objects"

# --- Git Progress Float 浮窗对接：按其 schema 写状态，浮窗即可显示本下载进度 ---
GP_RESULTS = Path.home() / "Library/Application Support/GitProgressFloat/results"
GP_TASKS = GP_RESULTS / "tasks"
GP_STATUS = GP_RESULTS / "git_progress_status.json"
GP_TASK_ID = f"{int(time.time()*1000)}-{os.getpid()}"

class Progress:
    """线程安全地把下载进度写成 Git Progress Float 的 task JSON。"""
    def __init__(self):
        self.lock = threading.Lock()
        self.total = 0          # 全部 LFS 指针数
        self.present0 = 0       # 起始已存在数
        self.done = 0           # 本次新下成功数
        self.bytes = 0          # 本次累计字节
        self.win_bytes = 0      # 速度窗口字节
        self.win_t = time.time()
        self.speed = ""
        self.started = time.time()

    def add(self, nbytes):
        with self.lock:
            self.done += 1
            self.bytes += nbytes
            self.win_bytes += nbytes
            now = time.time()
            dt = now - self.win_t
            if dt >= 2.0:
                bps = self.win_bytes / dt
                self.speed = f"{bps/1024:.0f} KiB/s" if bps < 1024*1024 else f"{bps/1048576:.2f} MiB/s"
                self.win_bytes = 0; self.win_t = now

    def publish(self, phase, detail, active=True, state="running"):
        present = self.present0 + self.done
        pct = round(present / self.total * 100, 1) if self.total else None
        payload = {
            "schema": 2, "id": GP_TASK_ID, "pid": os.getpid(),
            "active": active, "state": state,
            "command": "lfs-fetch", "repo": "Film (LFS images)",
            "phase": phase, "detail": detail,
            "percent": pct, "speed": self.speed,
            "updated_at": time.time(), "started_at": self.started,
            "started_at_text": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.started)),
        }
        if not active:
            payload["finished_at"] = time.time()
            payload["returncode"] = 0 if state == "done" else 1
        try:
            GP_TASKS.mkdir(parents=True, exist_ok=True)
            for p in (GP_TASKS / f"{GP_TASK_ID}.json", GP_STATUS):
                tmp = p.with_name(f".{p.name}.tmp")
                tmp.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
                tmp.replace(p)
        except OSError:
            pass

PROG = Progress()
# Auto Guard 控制锁路径（源 + 运行时副本都写，覆盖两处）
LOCK_PATHS = [
    Path("/Users/jaychoupp/Desktop/Story/mullvad-speed-guard/results/auto_guard_control.lock"),
    Path.home() / "Library/Application Support/MullvadSpeedGuard/results/auto_guard_control.lock",
]
TARGET_RELAY = ("de", "fra")  # 探测出的对 GitHub 最快节点
BATCH_URL = "https://lfs.github.com/gearlessslither-svg/Film/objects/batch"
SSH_HOST = "git@github-gearlessslither"
SSH_PATH = "gearlessslither-svg/Film.git"
POINTER_V1 = b"version https://git-lfs.github.com/spec/v1\n"

# urllib opener that ignores ALL proxies
opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

def parse_pointer(p: Path):
    try:
        with p.open("rb") as h:
            head = h.read(200)
    except OSError:
        return None
    if not head.startswith(POINTER_V1):
        return None
    txt = head.decode("utf-8", "ignore")
    oid = size = None
    for line in txt.splitlines():
        if line.startswith("oid sha256:"):
            oid = line.split("sha256:", 1)[1].strip()
        elif line.startswith("size "):
            try: size = int(line.split(" ", 1)[1].strip())
            except ValueError: pass
    if oid and size is not None:
        return {"oid": oid, "size": size, "path": p}
    return None

def obj_store_path(oid: str) -> Path:
    return LFS_OBJ / oid[0:2] / oid[2:4] / oid

def get_token() -> str:
    import time as _t
    last = None
    for attempt in range(6):
        try:
            out = subprocess.check_output(
                ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=20", SSH_HOST,
                 "git-lfs-authenticate", SSH_PATH, "download"],
                text=True, timeout=60, stderr=subprocess.DEVNULL)
            return json.loads(out)["header"]["Authorization"]
        except Exception as e:
            last = e
            _t.sleep(8)  # 连接抖动/DNS 失败时退避重试，由 Auto Guard 在后台恢复链路
    raise last

def batch(objs, token):
    body = json.dumps({"operation": "download", "transfers": ["basic"],
                       "objects": [{"oid": o["oid"], "size": o["size"]} for o in objs]}).encode()
    req = urllib.request.Request(BATCH_URL, data=body, method="POST", headers={
        "Accept": "application/vnd.git-lfs+json",
        "Content-Type": "application/vnd.git-lfs+json",
        "Authorization": token})
    with opener.open(req, timeout=60) as r:
        return json.loads(r.read())

def download(href, headers, dest: Path, size: int):
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(".tmp")
    req = urllib.request.Request(href, headers=headers or {})
    with opener.open(req, timeout=120) as r, tmp.open("wb") as f:
        while True:
            chunk = r.read(1 << 20)
            if not chunk: break
            f.write(chunk)
    if tmp.stat().st_size != size:
        tmp.unlink(missing_ok=True)
        raise IOError(f"size mismatch {tmp.stat().st_size}!={size}")
    tmp.rename(dest)

from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

def write_lock(ttl=10800):
    import time as _t
    payload = json.dumps({
        "reason": "github lfs bulk download (claude)",
        "pid": os.getpid(),
        "created_at": _t.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "expires_at_epoch": _t.time() + ttl,
    }, ensure_ascii=False)
    for p in LOCK_PATHS:
        try:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(payload, encoding="utf-8")
        except OSError:
            pass

def clear_lock():
    for p in LOCK_PATHS:
        try: p.unlink(missing_ok=True)
        except OSError: pass

def ensure_relay():
    import time as _t
    c, city = TARGET_RELAY
    subprocess.run(["mullvad", "relay", "set", "location", c, city],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["mullvad", "connect"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(20):
        st = subprocess.run(["mullvad", "status"], capture_output=True, text=True).stdout
        if st.startswith("Connected"):
            print("relay:", st.splitlines()[1].strip() if len(st.splitlines())>1 else st[:40], flush=True)
            return
        _t.sleep(1)
    print("relay connect timeout", flush=True)

def enumerate_todo():
    by_oid = {}
    for f in REPO.rglob("*"):
        if ".git/" in str(f): continue
        if f.is_file():
            info = parse_pointer(f)
            if info: by_oid.setdefault(info["oid"], info)
    return [o for o in by_oid.values() if not obj_store_path(o["oid"]).exists()]

def run_pass(todo):
    lock = threading.Lock()
    counters = {"ok": 0, "fail": 0}
    def fetch_one(obj, act, meta):
        try:
            download(act["href"], act.get("header", {}), obj_store_path(obj["oid"]), meta["size"])
            with lock: counters["ok"] += 1
            PROG.add(meta["size"])
            PROG.publish("Downloading", f"{PROG.present0+PROG.done}/{PROG.total} objects")
        except Exception:
            with lock: counters["fail"] += 1
    CHUNK, WORKERS = 100, 8
    for i in range(0, len(todo), CHUNK):
        group = todo[i:i+CHUNK]
        try:
            token = get_token(); resp = batch(group, token)
        except Exception:
            try:
                token = get_token(); resp = batch(group, token)
            except Exception as e:
                print(f"  batch failed: {e}", flush=True)
                PROG.publish("Reconnecting", "link busy, retrying"); continue
        oid2obj = {o["oid"]: o for o in group}
        with ThreadPoolExecutor(max_workers=WORKERS) as ex:
            tasks = []
            for obj in resp.get("objects", []):
                act = obj.get("actions", {}).get("download")
                meta = oid2obj.get(obj["oid"])
                if not act or not meta: continue
                tasks.append(ex.submit(fetch_one, obj, act, meta))
            for _ in as_completed(tasks): pass
        print(f"  ...{min(i+CHUNK,len(todo))}/{len(todo)} ok={counters['ok']} fail={counters['fail']}", flush=True)
    return counters

def checkout():
    # 把已下好的对象增量落到工作区（纯本地，不联网）
    subprocess.run(["git", "-c", "http.proxy=", "-c", "https.proxy=", "lfs", "checkout"],
                   cwd=str(REPO), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def count_all_pointers():
    n = 0
    for f in REPO.rglob("*"):
        if ".git/" in str(f): continue
        if f.is_file() and parse_pointer(f): n += 1
    return n

def main():
    import time as _t
    clear_lock()  # 不再钉节点/上锁：让 Auto Guard 维持连接健康
    PROG.total = count_all_pointers()
    PROG.present0 = PROG.total - len(enumerate_todo())
    PROG.publish("Starting", f"{PROG.present0}/{PROG.total} objects")
    MAX_PASSES = 500
    try:
        for p in range(1, MAX_PASSES + 1):
            todo = enumerate_todo()
            # 每轮以文件系统真实值校准已完成数
            PROG.present0 = PROG.total - len(todo); PROG.done = 0
            print(f"[pass {p}] remaining={len(todo)} @ {_t.strftime('%m-%d %H:%M:%S')}", flush=True)
            if not todo:
                print("ALL OBJECTS PRESENT", flush=True); break
            try:
                run_pass(todo)
            except Exception as e:
                print(f"  pass error: {e}", flush=True)
            checkout()  # 每轮增量签出，进度即时可见
            if enumerate_todo():
                PROG.publish("Waiting", "backoff before retry")
                _t.sleep(30)  # 链路抖动/限速时退避，由 Auto Guard 后台恢复
        checkout()
        left = len(enumerate_todo())
        PROG.present0 = PROG.total - left; PROG.done = 0
        PROG.publish("Done" if left == 0 else "Stopped",
                     f"{PROG.total-left}/{PROG.total} objects",
                     active=False, state="done" if left == 0 else "failed")
        print(f"FINISHED remaining={left} @ {_t.strftime('%m-%d %H:%M:%S')}", flush=True)
    except BaseException:
        PROG.publish("Interrupted", "downloader stopped", active=False, state="failed")
        raise

if __name__ == "__main__":
    main()
