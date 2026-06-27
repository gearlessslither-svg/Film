#!/usr/bin/env python3
"""film-session-relay helper.

Two jobs, no third-party deps, safe to run from either Codex or Claude:

  relay.py status
      Report the size + danger band of the live Codex session (the rollout
      JSONL that is growing right now) and any other oversized sessions.
      This is the "memory meter" the agent checks at session start and at
      danger nodes. Codex is the tool that OOM-crashes, so the meter reads
      ~/.codex/sessions even when invoked from Claude.

  relay.py handoff <project-slug-or-path> [--note "free text"]
      Create/refresh a handoff packet under
      <project>/00_admin/handoff/HANDOFF_<date>.md and update HANDOFF_LATEST.md.
      Auto-summarizes idea_board.json if present. The agent fills the
      narrative sections; this guarantees the file exists and is discoverable.
"""
from __future__ import annotations
import argparse, datetime as dt, json, sys
from pathlib import Path
from collections import Counter

HOME = Path.home()
CODEX_SESSIONS = HOME / ".codex" / "sessions"
FILM_PROJECTS = HOME / "Story" / "Film" / "projects"   # /Users/.../Story is the real dir; Desktop/Story symlinks here
MB = 1024 * 1024

# size -> (band, advice)
BANDS = [
    (2400 * MB, "FATAL",   "必崩。立刻写交接 → 隔离该会话 → 重启 Codex。"),
    (800 * MB,  "HIGH",    "高危。马上写交接并开新窗口；考虑隔离。"),
    (300 * MB,  "DANGER",  "危险。收尾当前批次，写交接，开新窗口。"),
    (150 * MB,  "WARN",    "注意。准备收尾，更新交接。"),
    (0,         "OK",      "安全，正常使用。"),
]

def human(b: int) -> str:
    f = float(b)
    for u in ("B", "KB", "MB", "GB"):
        if f < 1024:
            return f"{f:.1f}{u}"
        f /= 1024
    return f"{f:.1f}TB"

def band(size: int):
    for threshold, name, advice in BANDS:
        if size >= threshold:
            return name, advice
    return "OK", BANDS[-1][2]

def newest_sessions(limit=8):
    files = []
    if CODEX_SESSIONS.exists():
        for p in CODEX_SESSIONS.rglob("*.jsonl"):
            try:
                files.append((p.stat().st_mtime, p.stat().st_size, p))
            except OSError:
                pass
    files.sort(reverse=True)
    return files[:limit]

def cmd_status(_args):
    files = newest_sessions()
    if not files:
        print("没有找到 Codex 会话文件（~/.codex/sessions）。")
        return 0
    mtime, size, path = files[0]
    name, advice = band(size)
    when = dt.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M")
    print("== 活动 Codex 会话（最近写入）/ live session ==")
    print(f"  大小: {human(size)}   状态: [{name}]   最后写入: {when}")
    print(f"  建议: {advice}")
    print(f"  文件: {path}")
    over = [(s, p) for (_m, s, p) in files[1:] if s >= 150 * MB]
    if over:
        print("\n== 其它 >=150MB 的会话 / other large sessions ==")
        for s, p in over:
            n, _ = band(s)
            print(f"  {human(s):>9}  [{n}]  {p}")
    print("\n阈值参考: 150MB 注意 / 300MB 危险(开新窗) / 800MB 高危 / 2.4GB 必崩")
    return 0

def resolve_project(arg: str) -> Path:
    p = Path(arg).expanduser()
    if p.exists() and p.is_dir():
        return p
    cand = FILM_PROJECTS / arg
    if cand.exists():
        return cand
    return cand  # may not exist yet; caller handles

def board_summary(project: Path) -> str:
    bp = project / "03_story" / "idea_board" / "idea_board.json"
    if not bp.exists():
        return "_(no idea_board.json found)_"
    try:
        with bp.open(encoding="utf-8") as f:
            b = json.load(f)
    except Exception as e:
        return f"_(idea_board.json unreadable: {e})_"
    rows = b.get("rows", []) if isinstance(b, dict) else []
    pre = Counter("".join(ch for ch in str(r.get("item_id", ""))[:5] if not ch.isdigit()).strip("_")
                  for r in rows)
    st = Counter(r.get("status", "?") for r in rows)
    lines = [f"- 总卡数 / rows: **{len(rows)}**",
             f"- 按前缀 / by prefix: {dict(pre)}",
             f"- 按状态 / by status: {dict(st)}"]
    return "\n".join(lines)

HANDOFF_TEMPLATE = """# 项目交接包 / Handoff — {slug}

> 新窗口先读这份 + `03_story/idea_board/idea_board.json`，不要重新分析整个项目。

- 项目根: `{root}`
- 工具: AIGC Film Pipeline（Pipeline Hub `http://127.0.0.1:8787`），skill `aigc-film-pipeline`
- 生成时间: {now}
- 备注: {note}

## 当前 board 状态 / Current board
{board}

## 创意主线 / Creative spine
_(填：一句话故事 + 风格关键词)_

## 已锁定设定 / Locked bible rules（务必延续）
_(填：角色/服装/道具/安全红线，例如肖像与 logo 禁区)_

## 已完成 / Done
_(填：本窗口产出的卡、批次、输出目录)_

## 下一批 / NEXT
_(填：下一步要做的卡 + 前缀；越具体越好)_

## 怎么继续 / Resume
1. 启动 Pipeline Hub：`/Users/jaychoupp/Story/Film_Tool_Launcher.command`
2. 校验：`python3 Film/scripts/validate_pipeline_state.py {root}`
3. 加卡 → 生成 → 回填 `card-image-output`（只回路径，禁回 base64）→ 核验
4. 每完成一批回来更新本交接 + HANDOFF_LATEST.md
"""

def cmd_handoff(args):
    project = resolve_project(args.project)
    if not project.exists():
        print(f"项目不存在: {project}", file=sys.stderr)
        return 2
    hdir = project / "00_admin" / "handoff"
    hdir.mkdir(parents=True, exist_ok=True)
    today = dt.date.today().isoformat()
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    target = hdir / f"HANDOFF_{today}.md"
    if target.exists() and not args.force:
        print(f"今天已存在交接文件，未覆盖（用 --force 覆盖）:\n  {target}")
    else:
        target.write_text(HANDOFF_TEMPLATE.format(
            slug=project.name, root=project, now=now,
            note=args.note or "—", board=board_summary(project)),
            encoding="utf-8")
        print(f"已写入交接脚手架:\n  {target}\n请把 _(填...)_ 段落补全。")
    latest = hdir / "HANDOFF_LATEST.md"
    latest.write_text(target.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"已更新最新交接副本:\n  {latest}")
    return 0

def main(argv=None):
    ap = argparse.ArgumentParser(prog="relay.py")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status", help="会话体积预警 / session size meter")
    hp = sub.add_parser("handoff", help="生成/刷新项目交接包")
    hp.add_argument("project", help="项目 slug 或绝对路径")
    hp.add_argument("--note", default="", help="一句话备注")
    hp.add_argument("--force", action="store_true", help="覆盖今天已存在的交接文件")
    args = ap.parse_args(argv)
    if args.cmd == "status":
        return cmd_status(args)
    if args.cmd == "handoff":
        return cmd_handoff(args)
    ap.print_help()
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
