#!/usr/bin/env python3
"""Local Pipeline Hub / 本地 AIGC 电影项目总控台."""

from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import gzip
import json
import mimetypes
import os
import re
import shutil
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, quote, unquote, urlparse


APP_ROOT = Path(__file__).resolve().parent
REPO_ROOT = APP_ROOT.parents[1]
PROJECTS_ROOT = REPO_ROOT / "projects"
SCRIPTS_ROOT = REPO_ROOT / "scripts"
STATIC_ROOT = APP_ROOT / "static"

sys.path.insert(0, str(SCRIPTS_ROOT))

from analyze_aigc_project import analyze_stages, category_for, count_files_by_category, list_files, shot_list_stats  # noqa: E402
from create_aigc_project import STAGES, TEXT_TEMPLATES, render_template  # noqa: E402
from validate_aigc_project import validate_project  # noqa: E402

try:
    import yaml
except Exception:  # pragma: no cover - server can still run read-only without YAML.
    yaml = None


SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")
TEXT_PREVIEW_EXTENSIONS = {".md", ".txt", ".csv", ".json", ".yaml", ".yml", ".srt"}
IMAGE_PREVIEW_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".gif"}
MEDIA_PREVIEW_EXTENSIONS = IMAGE_PREVIEW_EXTENSIONS | {".mp4", ".webm", ".mp3", ".wav", ".ogg"}
LFS_POINTER_PREFIX = b"version https://git-lfs.github.com/spec/v1\n"
LEGACY_COIN_SLOT_AIGC_ROOT = REPO_ROOT.parent / "投币口" / "01_AIGC"
STAGE_IDS = tuple(stage_id for stage_id, _description in STAGES)
ANNOTATION_STATUSES = {"", "use", "reject"}
IMPACT_ACTIONS = {"create", "modify", "check"}
SCENE_STATUSES = {
    "draft",
    "in_progress",
    "needs_changes",
    "impact_ready",
    "generation_queued",
    "generation_failed",
    "review_ready",
    "approved",
}
RESOURCE_KIND_LABELS = {
    "script": "剧本/文档",
    "shot_prompt": "分镜提示词",
    "video_prompt": "视频提示词",
    "whitebox": "白模/预演",
    "storyboard_keyframe": "分镜关键帧",
    "scene_lock": "场景锁",
    "character_ref": "角色参考",
    "scene_ref": "场景参考",
    "lookdev": "风格/Lookdev",
    "audio": "音频",
    "video": "视频",
    "three_d": "3D",
    "image": "图片",
    "document": "文档",
    "other": "其他",
}
PREVIEW_DOC_LIMIT = 16
PREVIEW_IMAGE_LIMIT = 24
PREVIEW_VIDEO_LIMIT = 12
PREVIEW_AUDIO_LIMIT = 12
PREVIEW_THREE_D_LIMIT = 18
PREVIEW_SCENE_LOCK_LIMIT = 12
AUTH_TOKEN_ENV = "PIPELINE_HUB_TOKEN"
AUTH_COOKIE_NAME = "pipeline_hub_token"


def read_text(path: Path) -> str:
    return read_text_fallback(path) if path.exists() else ""


def read_text_fallback(path: Path) -> str:
    raw = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "gb18030", "big5"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def sanitize_text_for_display(text: str) -> str:
    text = text.replace("\ufffd", "【编码损坏 / Encoding damaged】")
    text = re.sub(r"\?{3,}", "【原文损坏，需从源文件重建 / Original text corrupted; rebuild from source】", text)
    return text


def read_json_body(handler: BaseHTTPRequestHandler) -> dict[str, object]:
    length = int(handler.headers.get("Content-Length", "0") or 0)
    if length <= 0:
        return {}
    raw = handler.rfile.read(length).decode("utf-8")
    return json.loads(raw) if raw.strip() else {}


def configured_auth_token() -> str:
    return os.environ.get(AUTH_TOKEN_ENV, "").strip()


def auth_cookie_token(handler: BaseHTTPRequestHandler) -> str:
    cookie_header = handler.headers.get("Cookie", "")
    for item in cookie_header.split(";"):
        name, separator, value = item.strip().partition("=")
        if separator and name == AUTH_COOKIE_NAME:
            return unquote(value.strip())
    return ""


def request_is_authorized(handler: BaseHTTPRequestHandler, parsed) -> bool:
    token = configured_auth_token()
    if not token:
        return True
    query_token = parse_qs(parsed.query).get("token", [""])[0].strip()
    if query_token == token:
        setattr(handler, "_pipeline_hub_auth_cookie", token)
        return True
    header_token = handler.headers.get("X-Pipeline-Hub-Token", "").strip()
    return header_token == token or auth_cookie_token(handler) == token


def add_auth_cookie_header(handler: BaseHTTPRequestHandler) -> None:
    token = getattr(handler, "_pipeline_hub_auth_cookie", "")
    if token:
        cookie = f"{AUTH_COOKIE_NAME}={quote(token)}; Path=/; HttpOnly; SameSite=Lax"
        handler.send_header("Set-Cookie", cookie)


def send_unauthorized(handler: BaseHTTPRequestHandler) -> None:
    send_text(
        handler,
        "需要访问令牌 / Access token required. Open the authorized URL with ?token=...",
        status=401,
    )


def maybe_compress_body(handler: BaseHTTPRequestHandler, body: bytes) -> tuple[bytes, bool]:
    accepted = handler.headers.get("Accept-Encoding", "").lower()
    if "gzip" not in accepted or len(body) < 1024:
        return body, False
    return gzip.compress(body), True


def send_json(handler: BaseHTTPRequestHandler, payload: object, status: int = 200) -> None:
    body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
    response_body, is_gzipped = maybe_compress_body(handler, body)
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(response_body)))
    handler.send_header("Vary", "Accept-Encoding")
    if is_gzipped:
        handler.send_header("Content-Encoding", "gzip")
    add_auth_cookie_header(handler)
    handler.end_headers()
    handler.wfile.write(response_body)


def send_text(handler: BaseHTTPRequestHandler, text: str, status: int = 200, content_type: str = "text/plain") -> None:
    body = text.encode("utf-8")
    response_body, is_gzipped = maybe_compress_body(handler, body)
    handler.send_response(status)
    handler.send_header("Content-Type", f"{content_type}; charset=utf-8")
    handler.send_header("Content-Length", str(len(response_body)))
    handler.send_header("Vary", "Accept-Encoding")
    if is_gzipped:
        handler.send_header("Content-Encoding", "gzip")
    add_auth_cookie_header(handler)
    handler.end_headers()
    handler.wfile.write(response_body)


def parse_json_output(stdout: str) -> object:
    text = stdout.strip()
    if not text:
        return {}
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start >= 0 and end > start:
            return json.loads(text[start : end + 1])
    return {"raw": stdout}


def run_repo_script(args: list[str]) -> dict[str, object]:
    env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    completed = subprocess.run(
        [sys.executable, *args],
        cwd=REPO_ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        env=env,
        check=False,
    )
    return {
        "ok": completed.returncode == 0,
        "returncode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "json": parse_json_output(completed.stdout),
    }


def validate_slug(slug: str) -> None:
    if not SLUG_RE.fullmatch(slug):
        raise ValueError("项目 slug 无效 / Invalid project slug.")


def project_path(slug: str) -> Path:
    validate_slug(slug)
    path = (PROJECTS_ROOT / slug).resolve()
    if PROJECTS_ROOT.resolve() not in path.parents and path != PROJECTS_ROOT.resolve():
        raise ValueError("项目路径越界 / Project path escaped projects root.")
    return path


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def annotation_path(path: Path) -> Path:
    return path / "00_admin" / "resource_annotations.json"


def empty_annotations(slug: str) -> dict[str, object]:
    return {
        "schema_version": 1,
        "project_slug": slug,
        "updated_at": "",
        "assets": {},
    }


def load_resource_annotations(path: Path) -> dict[str, object]:
    data = empty_annotations(path.name)
    target = annotation_path(path)
    if not target.exists():
        return data
    try:
        loaded = json.loads(target.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return data
    if isinstance(loaded, dict):
        assets = loaded.get("assets", {})
        data.update({key: value for key, value in loaded.items() if key != "assets"})
        data["assets"] = assets if isinstance(assets, dict) else {}
    return data


def write_resource_annotations(path: Path, data: dict[str, object]) -> None:
    target = annotation_path(path)
    assets = data.get("assets", {})
    if not assets and target.exists():
        target.unlink()
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def load_manifest(path: Path) -> dict[str, object]:
    manifest = path / "project.yaml"
    if not manifest.exists():
        return {}
    text = read_text_fallback(manifest)
    if yaml is None:
        return parse_manifest_fallback(text)
    data = yaml.safe_load(text)
    return data if isinstance(data, dict) else {}


def load_yaml_file(path: Path) -> dict[str, object]:
    if not path.exists():
        return {}
    text = read_text_fallback(path)
    try:
        data = json.loads(text)
        return data if isinstance(data, dict) else {}
    except json.JSONDecodeError:
        pass
    if yaml is None:
        return {}
    try:
        data = yaml.safe_load(text)
    except Exception:
        return {}
    return data if isinstance(data, dict) else {}


def write_yaml_file(path: Path, data: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parse_manifest_fallback(text: str) -> dict[str, object]:
    data: dict[str, object] = {"raw": text}
    current_section = ""
    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if not raw_line.startswith((" ", "\t")) and raw_line.rstrip().endswith(":"):
            current_section = raw_line.strip()[:-1]
            data.setdefault(current_section, {})
            continue
        if current_section != "project" or not raw_line.startswith("  "):
            continue
        key, sep, value = raw_line.strip().partition(":")
        if not sep:
            continue
        scalar = value.strip()
        if len(scalar) >= 2 and scalar[0] == scalar[-1] and scalar[0] in {"'", '"'}:
            scalar = scalar[1:-1]
        project = data.setdefault("project", {})
        if isinstance(project, dict):
            project[key] = scalar
    return data


def write_manifest(path: Path, manifest: dict[str, object]) -> None:
    if yaml is None:
        raise RuntimeError("更新项目链接需要 PyYAML / PyYAML is required to update project links.")
    (path / "project.yaml").write_text(
        yaml.safe_dump(manifest, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )


def manifest_project_value(manifest: dict[str, object], key: str) -> str:
    project = manifest.get("project")
    if isinstance(project, dict):
        value = project.get(key, "")
        return "" if value is None else str(value)
    return ""


def resolve_link_root(value: str, path: Path) -> Path | None:
    if not value or value.startswith("{{"):
        return None
    raw = Path(value)
    candidates = [raw] if raw.is_absolute() else [REPO_ROOT / raw, path / raw, PROJECTS_ROOT / raw]
    for candidate in candidates:
        if candidate.exists():
            return candidate.resolve()
    return None


def preview_roots(path: Path, manifest: dict[str, object]) -> list[tuple[str, Path]]:
    roots: list[tuple[str, Path]] = [("project", path.resolve())]
    resource_root = resolve_link_root(manifest_project_value(manifest, "resource_root"), path)
    if resource_root and resource_root.exists():
        roots.append(("resource", resource_root))
    return roots


def safe_asset_path(slug: str, origin: str, rel_path: str) -> Path:
    path = project_path(slug)
    manifest = load_manifest(path)
    roots = dict(preview_roots(path, manifest))
    root = roots.get(origin)
    if root is None:
        raise ValueError("未知资源来源 / Unknown asset origin.")
    target = (root / rel_path).resolve()
    if root not in target.parents and target != root:
        raise ValueError("资源路径越界 / Asset path escaped its root.")
    if not target.exists() or not target.is_file():
        raise FileNotFoundError("资源不存在 / Asset not found.")
    return target


def asset_url(slug: str, origin: str, rel_path: str) -> str:
    return f"/api/projects/{slug}/asset?origin={quote(origin)}&path={quote(rel_path)}"


def asset_ref(origin: str, rel_path: str) -> str:
    return f"{origin}:{rel_path}"


def asset_stage(origin: str, rel_path: str) -> str:
    first = rel_path.split("/", 1)[0]
    if first in STAGE_IDS:
        return first
    text = rel_path.lower()
    if "prompt" in text or "storyboard" in text or "keyframe" in text or "micro_storyboard" in text:
        return "07_shots"
    if "whitebox" in text or "previs" in text or "blender" in text or "camera_" in text:
        return "06_previs"
    if "character" in text or "scene_ref" in text or "continuity" in text or "asset" in text:
        return "05_asset_bible"
    if "lookdev" in text or "style" in text or "reference" in text:
        return "04_lookdev"
    if "script" in text or "beat" in text or "outline" in text or "/story" in text:
        return "03_story"
    if "audio" in text or "edit" in text or "animatic" in text or "subtitle" in text:
        return "09_edit"
    if "qa" in text or "reject" in text or "report" in text:
        return "10_qa"
    if "delivery" in text or "export" in text:
        return "11_delivery"
    return "resources" if origin == "resource" else "other"


def resource_kind(rel_path: str, category: str) -> str:
    text = rel_path.lower()
    if "video_prompts" in text or "video_prompt" in text:
        return "video_prompt"
    if "prompt" in text:
        return "shot_prompt"
    if "scene_lock" in text:
        return "scene_lock"
    if "whitebox" in text or "previs" in text or "blender" in text or "camera_whitebox" in text:
        return "whitebox"
    if "final_storyboard" in text or "storyboard_panel" in text or "storyboard_panels" in text or "keyframe" in text or "micro_storyboard" in text:
        return "storyboard_keyframe"
    if "script" in text or "beat" in text or "outline" in text or rel_path.startswith("03_story/"):
        return "script"
    if "character" in text:
        return "character_ref"
    if "scene_ref" in text or "location" in text or "environment" in text:
        return "scene_ref"
    if "lookdev" in text or "style" in text or "palette" in text:
        return "lookdev"
    if category == "audio":
        return "audio"
    if category == "video":
        return "video"
    if category == "3d":
        return "three_d"
    if category == "text":
        return "document"
    if category == "image":
        return "image"
    return "other"


def is_lfs_pointer(path: Path) -> bool:
    try:
        with path.open("rb") as handle:
            return handle.read(len(LFS_POINTER_PREFIX)) == LFS_POINTER_PREFIX
    except OSError:
        return False


_LEGACY_NAME_INDEX: dict[str, Path] | None = None


def legacy_name_index() -> dict[str, Path]:
    """Index every real (non-LFS) file under the local 投币口 backup by basename.

    Used as a name-based fallback so any local original can stand in for an
    undownloaded LFS object, even when the relative path no longer matches.
    """
    global _LEGACY_NAME_INDEX
    if _LEGACY_NAME_INDEX is not None:
        return _LEGACY_NAME_INDEX
    index: dict[str, Path] = {}
    root = LEGACY_COIN_SLOT_AIGC_ROOT.parent  # 投币口/
    if root.exists():
        for candidate in root.rglob("*"):
            if not candidate.is_file():
                continue
            if candidate.name in index:
                continue  # keep first match; exact-path lookup handles collisions
            if is_lfs_pointer(candidate):
                continue
            index[candidate.name] = candidate.resolve()
    _LEGACY_NAME_INDEX = index
    return index


def legacy_coin_slot_asset_path(origin: str, rel_path: str) -> Path | None:
    if not rel_path or not LEGACY_COIN_SLOT_AIGC_ROOT.exists():
        return None
    # 1) Precise path mapping for media/01_AIGC/<suffix> -> 投币口/01_AIGC/<suffix>.
    if origin == "resource" and rel_path.startswith("media/01_AIGC/"):
        suffix = rel_path.removeprefix("media/01_AIGC/")
        root = LEGACY_COIN_SLOT_AIGC_ROOT.resolve()
        candidate = (root / suffix).resolve()
        if (root in candidate.parents or candidate == root) and candidate.is_file() and not is_lfs_pointer(candidate):
            return candidate
    # 2) Name-based fallback across the whole 投币口 backup (covers project-origin
    #    scene locks, renamed paths, and assets stored outside media/01_AIGC).
    return legacy_name_index().get(Path(rel_path).name)


def asset_item(slug: str, origin: str, rel_path: str, file_path: Path, category: str | None = None) -> dict[str, object]:
    extension = file_path.suffix.lower()
    lfs_pointer = is_lfs_pointer(file_path)
    fallback = legacy_coin_slot_asset_path(origin, rel_path)
    asset_category = category or category_for(file_path)
    kind = resource_kind(rel_path, asset_category)
    return {
        "ref": asset_ref(origin, rel_path),
        "origin": origin,
        "path": rel_path,
        "name": file_path.name,
        "category": asset_category,
        "stage": asset_stage(origin, rel_path),
        "kind": kind,
        "kind_label": RESOURCE_KIND_LABELS.get(kind, kind),
        "size_kb": round(file_path.stat().st_size / 1024, 1),
        "extension": extension,
        "previewable": extension in MEDIA_PREVIEW_EXTENSIONS and (not lfs_pointer or fallback is not None),
        "url": asset_url(slug, origin, rel_path),
        "lfs_pointer": lfs_pointer,
        "lfs_missing": lfs_pointer and fallback is None,
        "fallback": "legacy_local" if fallback else "",
    }


def asset_priority(path: Path) -> tuple[int, str]:
    text = str(path).lower()
    score = 50
    for keyword in (
        "contact",
        "scene_lock",
        "first-act",
        "first_act",
        "styleframe",
        "keyframe",
        "storyboard",
        "character",
        "whitebox",
        "look",
        "reference",
        "prompt",
        "script",
        "beat",
        "audio",
    ):
        if keyword in text:
            score -= 5
    if "rejected" in text or "reject" in text:
        score += 10
    return score, text


def doc_kind(rel_path: str) -> str:
    if rel_path.startswith("03_story/"):
        return "story"
    if rel_path.startswith("02_direction/"):
        return "direction"
    if rel_path.startswith("04_lookdev/"):
        return "lookdev"
    if rel_path.startswith("05_asset_bible/"):
        return "asset bible"
    if rel_path.startswith("06_previs/"):
        if rel_path.startswith("06_previs/scene_locks/"):
            return "scene lock"
        return "previs"
    if rel_path.startswith("09_edit/"):
        return "edit/audio"
    if rel_path.startswith("10_qa/"):
        return "qa"
    return "document"


def read_preview_text(path: Path, limit: int = 12000) -> str:
    text = sanitize_text_for_display(read_text_fallback(path))
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + "\n\n[预览已截断 / preview truncated]"


def collect_preview_assets(slug: str, path: Path, manifest: dict[str, object]) -> dict[str, object]:
    assets: list[dict[str, object]] = []
    docs: list[dict[str, object]] = []
    images: list[dict[str, object]] = []
    videos: list[dict[str, object]] = []
    audio: list[dict[str, object]] = []
    three_d: list[dict[str, object]] = []
    counts: dict[str, int] = {}

    important_doc_prefixes = (
        "00_admin/director_brief",
        "02_direction/",
        "03_story/",
        "04_lookdev/",
        "05_asset_bible/",
        "06_previs/scene_locks/",
        "06_previs/qa/",
        "07_shots/prompts/",
        "07_shots/video_prompts/",
        "09_edit/",
        "10_qa/autofill_runs/autofill_latest",
    )

    for origin, root in preview_roots(path, manifest):
        files = list_files(root)
        for file_path in files:
            rel_path = str(file_path.relative_to(root)).replace("\\", "/")
            if origin == "project" and rel_path == "00_admin/resource_annotations.json":
                continue
            category = category_for(file_path)
            counts[category] = counts.get(category, 0) + 1
            item = asset_item(slug, origin, rel_path, file_path, category=category)
            assets.append(item)
            if category == "image":
                images.append(item)
            elif category == "video":
                videos.append(item)
            elif category == "audio":
                audio.append(item)
            elif category == "3d":
                three_d.append(item)
            elif (
                origin == "project"
                and file_path.suffix.lower() in TEXT_PREVIEW_EXTENSIONS
                and rel_path.startswith(important_doc_prefixes)
            ):
                docs.append(
                    {
                        **item,
                        "kind": doc_kind(rel_path),
                        "text": read_preview_text(file_path),
                    }
                )

    assets = sorted(assets, key=lambda item: (str(item["stage"]), str(item["kind"]), asset_priority(Path(str(item["path"])))))
    docs = sorted(docs, key=lambda item: asset_priority(Path(str(item["path"]))))[:PREVIEW_DOC_LIMIT]
    images = sorted(images, key=lambda item: asset_priority(Path(str(item["path"]))))[:PREVIEW_IMAGE_LIMIT]
    videos = sorted(videos, key=lambda item: asset_priority(Path(str(item["path"]))))[:PREVIEW_VIDEO_LIMIT]
    audio = sorted(audio, key=lambda item: asset_priority(Path(str(item["path"]))))[:PREVIEW_AUDIO_LIMIT]
    three_d = sorted(three_d, key=lambda item: asset_priority(Path(str(item["path"]))))[:PREVIEW_THREE_D_LIMIT]
    return {
        "counts": counts,
        "assets": assets,
        "docs": docs,
        "images": images,
        "videos": videos,
        "audio": audio,
        "three_d": three_d,
    }


def url_from_asset_ref(slug: str, ref: str) -> str:
    origin, sep, rel_path = ref.partition(":")
    if sep and origin in {"project", "resource"} and rel_path:
        return asset_url(slug, origin, rel_path)
    return ""


def image_item_from_project_path(slug: str, root: Path, path: Path) -> dict[str, object]:
    rel_path = str(path.relative_to(root)).replace("\\", "/")
    return asset_item(slug, "project", rel_path, path)


def asset_item_from_ref(slug: str, ref: str) -> dict[str, object]:
    origin, sep, rel_path = ref.partition(":")
    if not sep or origin not in {"project", "resource"} or not rel_path:
        return {}
    try:
        target = safe_asset_path(slug, origin, rel_path)
    except (ValueError, FileNotFoundError):
        return {
            "origin": origin,
            "path": rel_path,
            "url": asset_url(slug, origin, rel_path),
            "previewable": False,
            "missing": True,
        }
    return asset_item(slug, origin, rel_path, target)


def collect_scene_locks(slug: str, path: Path) -> dict[str, object]:
    root = path / "06_previs" / "scene_locks"
    if not root.exists():
        return {"exists": False, "items": [], "overview_images": [], "index": {}}

    overview_images = [
        image_item_from_project_path(slug, path, image)
        for image in sorted(root.glob("*scene_lock_overview.*"), key=lambda item: item.stat().st_mtime, reverse=True)
        if image.is_file() and category_for(image) == "image"
    ][:PREVIEW_SCENE_LOCK_LIMIT]

    index_path = root / "index.md"
    index = {}
    if index_path.exists():
        index = {
            "path": "06_previs/scene_locks/index.md",
            "url": asset_url(slug, "project", "06_previs/scene_locks/index.md"),
            "text": read_preview_text(index_path, limit=10000),
        }

    items: list[dict[str, object]] = []
    for scene_dir in sorted([item for item in root.iterdir() if item.is_dir()]):
        lock_yaml = scene_dir / "scene_lock.yaml"
        lock_md = scene_dir / "scene_lock.md"
        data: dict[str, object] = {}
        if lock_yaml.exists() and yaml is not None:
            loaded = yaml.safe_load(read_text_fallback(lock_yaml))
            data = loaded if isinstance(loaded, dict) else {}
        preview = next(iter(sorted(scene_dir.glob("*_preview.*"))), None)
        master_asset = asset_item_from_ref(slug, str(data.get("master_reference", "")))
        item = {
            "scene_id": str(data.get("scene_id", scene_dir.name)),
            "folder": str(scene_dir.relative_to(root)).replace("\\", "/"),
            "shot_count": data.get("shot_count", 0),
            "batch": data.get("batch", ""),
            "master_reference": data.get("master_reference", ""),
            "master_url": master_asset.get("url", ""),
            "master_asset": master_asset,
            "preview": image_item_from_project_path(slug, path, preview) if preview and preview.exists() else {},
            "lock_path": str(lock_yaml.relative_to(path)).replace("\\", "/") if lock_yaml.exists() else "",
            "doc_path": str(lock_md.relative_to(path)).replace("\\", "/") if lock_md.exists() else "",
            "doc_text": read_preview_text(lock_md, limit=9000) if lock_md.exists() else "",
        }
        items.append(item)

    return {
        "exists": bool(items or overview_images or index),
        "items": items,
        "overview_images": overview_images,
        "index": index,
    }


def report_info(path: Path) -> dict[str, object]:
    report = path / "10_qa" / "reports" / "project_audit_latest.md"
    if not report.exists():
        return {"exists": False, "path": str(report)}
    text = sanitize_text_for_display(read_text_fallback(report))
    readiness_match = re.search(r"Readiness score:\s+\*\*(\d+)%\*\*", text)
    status_match = re.search(r"Audit status:\s+\*\*([^*]+)\*\*", text)
    generated_match = re.search(r"Generated at:\s+(.+)", text)
    p0_count = len(re.findall(r"\|\s+P0\s+\|", text))
    p1_count = len(re.findall(r"\|\s+P1\s+\|", text))
    return {
        "exists": True,
        "path": str(report),
        "status": status_match.group(1).strip() if status_match else "",
        "readiness": int(readiness_match.group(1)) if readiness_match else None,
        "generated_at": generated_match.group(1).strip() if generated_match else "",
        "p0_count": p0_count,
        "p1_count": p1_count,
        "text": text,
    }


def autofill_info(path: Path) -> dict[str, object]:
    report = path / "10_qa" / "autofill_runs" / "autofill_latest.md"
    if not report.exists():
        return {"exists": False, "path": str(report)}
    text = sanitize_text_for_display(read_text_fallback(report))
    status_match = re.search(r"Completion status:\s+\*\*([^*]+)\*\*", text)
    generated_match = re.search(r"Generated at:\s+(.+)", text)
    pending_match = re.search(r"Pending external tasks:\s+(\d+)", text)
    return {
        "exists": True,
        "path": str(report),
        "status": status_match.group(1).strip() if status_match else "",
        "generated_at": generated_match.group(1).strip() if generated_match else "",
        "pending_external": int(pending_match.group(1)) if pending_match else None,
        "text": text,
    }


def stage_summary(path: Path) -> list[dict[str, object]]:
    rows = analyze_stages(path)
    by_id = {row["stage"]: row for row in rows}
    summary = []
    for stage_id, description in STAGES:
        stage_root = path / stage_id
        files = list_files(stage_root)
        row = by_id.get(stage_id, {})
        summary.append(
            {
                "id": stage_id,
                "description": description,
                "status": row.get("status", "missing"),
                "file_count": len(files),
                "category_counts": dict(count_files_by_category(files)),
                "missing": row.get("missing", []),
                "weak": row.get("weak", []),
            }
        )
    return summary


def read_shots(path: Path, limit: int = 100) -> dict[str, object]:
    import csv

    shot_list = path / "07_shots" / "shot_list.csv"
    if not shot_list.exists():
        return {"exists": False, "rows": [], "columns": []}
    with shot_list.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
    return {"exists": True, "columns": reader.fieldnames or [], "rows": rows[:limit], "row_count": len(rows)}


def load_change_requests(path: Path, scene_id: str) -> list[dict[str, object]]:
    root = path / "10_qa" / "change_requests"
    if not root.exists():
        return []
    requests: list[dict[str, object]] = []
    for request_path in sorted(root.glob("*.yaml")):
        data = load_yaml_file(request_path)
        if not data or data.get("scene_id") != scene_id:
            continue
        impacts = data.get("impact_table", [])
        if isinstance(impacts, list):
            for index, impact in enumerate(impacts, start=1):
                if isinstance(impact, dict) and not impact.get("impact_id"):
                    impact["impact_id"] = f"I{index:03d}"
        queue = data.get("generation_queue", [])
        if isinstance(queue, list):
            for item in queue:
                if isinstance(item, dict):
                    item.setdefault("change_request_id", data.get("change_request_id", ""))
        data["path"] = str(request_path.relative_to(path))
        requests.append(data)
    return sorted(requests, key=lambda item: str(item.get("created_at", "")), reverse=True)


def load_scene_review_log(path: Path, scene_id: str) -> dict[str, object]:
    review_path = path / "10_qa" / "scene_reviews" / f"{scene_id}.yaml"
    data = load_yaml_file(review_path)
    if data:
        return data
    return {
        "schema_version": 1,
        "scene_id": scene_id,
        "reviews": [],
    }


def load_scene_snapshots(path: Path, scene_id: str) -> list[dict[str, object]]:
    root = path / "10_qa" / "scene_snapshots"
    if not root.exists():
        return []
    snapshots: list[dict[str, object]] = []
    for snapshot_path in sorted(root.glob(f"{scene_id}_*.yaml")):
        data = load_yaml_file(snapshot_path)
        if not data or data.get("scene_id") != scene_id:
            continue
        data["path"] = str(snapshot_path.relative_to(path))
        snapshots.append(data)
    return sorted(snapshots, key=lambda item: str(item.get("created_at", "")), reverse=True)


def scene_generation_queue(change_requests: list[dict[str, object]]) -> list[dict[str, object]]:
    queue: list[dict[str, object]] = []
    for request in change_requests:
        if str(request.get("status", "")).endswith("_example"):
            continue
        items = request.get("generation_queue", [])
        if not isinstance(items, list):
            continue
        for item in items:
            if not isinstance(item, dict):
                continue
            queue.append(
                {
                    **item,
                    "change_request_id": item.get("change_request_id") or request.get("change_request_id", ""),
                    "trigger_step": request.get("trigger_step", ""),
                    "creative_direction": request.get("creative_direction", ""),
                }
            )
    return queue


def annotate_scene_resource_assets(slug: str, resource_manifest: dict[str, object]) -> None:
    stage_assets = resource_manifest.get("stage_assets", {})
    if not isinstance(stage_assets, dict):
        return
    for assets in stage_assets.values():
        if not isinstance(assets, list):
            continue
        for asset in assets:
            if not isinstance(asset, dict):
                continue
            rel_path = str(asset.get("path", "") or "")
            if not rel_path:
                continue
            origin = "resource" if asset.get("origin") == "resource" else "project"
            extension = Path(rel_path).suffix.lower()
            asset["previewable"] = extension in MEDIA_PREVIEW_EXTENSIONS
            asset["category"] = category_for(Path(rel_path)) if extension else "other"
            try:
                target = safe_asset_path(slug, origin, rel_path)
            except Exception:
                asset["exists"] = False
                asset["lfs_pointer"] = False
                asset["lfs_missing"] = False
                continue
            pointer = is_lfs_pointer(target)
            fallback = legacy_coin_slot_asset_path(origin, rel_path) if pointer else None
            asset["exists"] = target.exists()
            asset["lfs_pointer"] = pointer
            asset["lfs_missing"] = pointer and fallback is None
            if fallback is not None:
                asset["fallback"] = "legacy_local"


def load_scene_workbench(path: Path) -> dict[str, object]:
    scene_manifest = load_yaml_file(path / "00_admin" / "scene_manifest.yaml")
    slug = str(scene_manifest.get("project_slug", path.name) or path.name) if isinstance(scene_manifest, dict) else path.name
    acts = scene_manifest.get("acts", []) if isinstance(scene_manifest, dict) else []
    scenes: list[dict[str, object]] = []
    if isinstance(acts, list):
        for act in acts:
            if not isinstance(act, dict):
                continue
            for scene in act.get("scenes", []) or []:
                if not isinstance(scene, dict):
                    continue
                scene_id = str(scene.get("scene_id") or "")
                scene_slug = str(scene.get("scene_slug") or scene_id.lower().replace("_", "-"))
                resource_manifest = load_yaml_file(path / "06_previs" / "scene_locks" / scene_slug / "scene_resource_manifest.yaml")
                annotate_scene_resource_assets(slug, resource_manifest)
                version_registry = load_yaml_file(path / "10_qa" / "version_registry" / f"{scene_id}.yaml")
                change_requests = load_change_requests(path, scene_id)
                scenes.append(
                    {
                        **scene,
                        "act_id": act.get("act_id", ""),
                        "act_title": act.get("title", ""),
                        "resource_manifest": resource_manifest,
                        "version_registry": version_registry,
                        "change_requests": change_requests,
                        "generation_queue": scene_generation_queue(change_requests),
                        "review_log": load_scene_review_log(path, scene_id),
                        "snapshots": load_scene_snapshots(path, scene_id),
                    }
                )
    return {
        "manifest": scene_manifest,
        "scenes": scenes,
    }


def scene_by_id(path: Path, scene_id: str) -> dict[str, object]:
    for scene in load_scene_workbench(path).get("scenes", []):
        if isinstance(scene, dict) and scene.get("scene_id") == scene_id:
            return scene
    raise ValueError("未知场戏 / Unknown scene.")


def change_request_path(path: Path, change_request_id: str) -> Path:
    if not re.fullmatch(r"[A-Za-z0-9_.-]+", change_request_id):
        raise ValueError("变更请求 ID 无效 / Invalid change request id.")
    return path / "10_qa" / "change_requests" / f"{change_request_id}.yaml"


def next_change_request_id(scene_id: str) -> str:
    stamp = datetime.now(timezone.utc).astimezone().strftime("%Y%m%d_%H%M%S")
    return f"CR_{scene_id}_{stamp}"


def impact_reason(trigger_step: str, target_step: str, scope: str) -> str:
    if scope == "direct":
        return "直接修改的步骤资源 / Directly edited step asset."
    reasons = {
        "03_story": "故事变化会影响后续所有制作资源 / Story changes affect downstream production assets.",
        "04_lookdev": "风格变化会影响场景锁、提示词、生成和调色 / Look changes affect scene locks, prompts, generation, and color.",
        "05_asset_bible": "角色/场景/道具锁变化会影响引用它的场戏资源 / Bible changes affect scene assets that reference it.",
        "06_previs": "白模、机位或场景锁变化会影响提示词、关键帧、视频和剪辑 / Previs, camera, or scene-lock changes affect prompts, keyframes, video, and edit.",
        "07_shots": "镜头提示词变化会影响生成输出、剪辑和 QA / Shot prompt changes affect generated outputs, edit, and QA.",
        "08_generation": "生成输出变化会影响剪辑、QA 和交付 / Generated-output changes affect edit, QA, and delivery.",
        "09_edit": "剪辑/声音变化会影响 QA 和交付验证 / Edit or sound changes affect QA and delivery validation.",
        "10_qa": "QA 变化会影响修复队列和交付判断 / QA changes affect fix queues and delivery decisions.",
        "11_delivery": "交付变化通常只影响交付包 / Delivery changes usually affect delivery packages only.",
    }
    return reasons.get(trigger_step) or f"{trigger_step} 会影响 {target_step} / {trigger_step} affects {target_step}."


def build_impact_table(scene: dict[str, object], trigger_step: str, trigger_asset_id: str = "") -> list[dict[str, object]]:
    stage_assets = scene.get("resource_manifest", {}).get("stage_assets", {})
    if not isinstance(stage_assets, dict):
        stage_assets = {}
    steps = [str(step) for step in scene.get("primary_steps", []) or stage_assets.keys()]
    if trigger_step not in steps:
        raise ValueError("再创作步骤不属于当前场戏 / Re-create step is not part of this scene.")
    trigger_index = steps.index(trigger_step)
    table: list[dict[str, object]] = []
    for step_index, step in enumerate(steps):
        assets = stage_assets.get(step, [])
        if not isinstance(assets, list):
            continue
        if step_index < trigger_index and step not in {"05_asset_bible"}:
            continue
        if step_index == trigger_index:
            scope = "direct"
        elif step == "05_asset_bible":
            scope = "shared"
        else:
            scope = "downstream"
        for asset in assets:
            if not isinstance(asset, dict):
                continue
            asset_id = str(asset.get("asset_id") or asset.get("role") or "")
            if trigger_asset_id and step_index == trigger_index and asset_id != trigger_asset_id:
                continue
            action = "check" if scope == "shared" and step_index < trigger_index else "modify"
            if step == "08_generation" and step_index > trigger_index:
                action = "create"
            selected = scope == "direct" or (step_index == trigger_index + 1)
            table.append(
                {
                    "impact_id": f"I{len(table) + 1:03d}",
                    "action": action,
                    "impact_scope": scope,
                    "asset_id": asset_id,
                    "stage_id": step,
                    "role": asset.get("role", ""),
                    "path": asset.get("path", ""),
                    "why": impact_reason(trigger_step, step, scope),
                    "selected": selected,
                }
            )
    return table


def create_scene_change_request(slug: str, payload: dict[str, object]) -> dict[str, object]:
    path = project_path(slug)
    scene_id = str(payload.get("scene_id", "") or "").strip()
    trigger_step = str(payload.get("trigger_step", "") or "").strip()
    trigger_asset_id = str(payload.get("trigger_asset_id", "") or "").strip()
    creative_direction = str(payload.get("creative_direction", "") or "").strip()
    if not scene_id or not trigger_step or not creative_direction:
        raise ValueError("需要场戏、步骤和创作方向 / Scene, step, and creative direction are required.")
    scene = scene_by_id(path, scene_id)
    change_request_id = next_change_request_id(scene_id)
    request = {
        "schema_version": 1,
        "change_request_id": change_request_id,
        "project_slug": slug,
        "scene_id": scene_id,
        "trigger_step": trigger_step,
        "trigger_asset_id": trigger_asset_id,
        "creative_direction": creative_direction,
        "status": "impact_ready",
        "created_at": now_iso(),
        "impact_table": build_impact_table(scene, trigger_step, trigger_asset_id),
        "generation_queue": [],
        "approval": {
            "user_confirmed": False,
            "confirmed_at": "",
            "notes": "",
        },
    }
    write_yaml_file(change_request_path(path, change_request_id), request)
    set_scene_manifest_status(path, scene_id, "impact_ready", creative_direction)
    return {"ok": True, "change_request": request, "project": project_detail(slug)}


def set_scene_manifest_status(path: Path, scene_id: str, status: str, notes: str = "") -> str:
    manifest_path = path / "00_admin" / "scene_manifest.yaml"
    manifest = load_yaml_file(manifest_path)
    acts = manifest.get("acts", [])
    if not isinstance(acts, list):
        raise ValueError("场戏清单无效 / Scene manifest is invalid.")
    updated_at = now_iso()
    found = False
    for act in acts:
        if not isinstance(act, dict):
            continue
        scenes = act.get("scenes", [])
        if not isinstance(scenes, list):
            continue
        for scene in scenes:
            if not isinstance(scene, dict) or scene.get("scene_id") != scene_id:
                continue
            scene["status"] = status
            scene["last_reviewed_at"] = updated_at
            if notes:
                scene["last_review_note"] = notes
            found = True
    if not found:
        raise ValueError("未知场戏 / Unknown scene.")
    manifest["updated_at"] = updated_at
    write_yaml_file(manifest_path, manifest)
    return updated_at


def update_scene_status(slug: str, payload: dict[str, object]) -> dict[str, object]:
    path = project_path(slug)
    scene_id = str(payload.get("scene_id", "") or "").strip()
    status = str(payload.get("status", "") or "").strip()
    notes = str(payload.get("notes", "") or "").strip()
    change_request_id = str(payload.get("change_request_id", "") or "").strip()
    if not scene_id or status not in SCENE_STATUSES:
        raise ValueError("需要有效场戏和状态 / A valid scene and status are required.")
    updated_at = set_scene_manifest_status(path, scene_id, status, notes)

    review_path = path / "10_qa" / "scene_reviews" / f"{scene_id}.yaml"
    review_log = load_scene_review_log(path, scene_id)
    reviews = review_log.setdefault("reviews", [])
    if not isinstance(reviews, list):
        reviews = []
        review_log["reviews"] = reviews
    reviews.append(
        {
            "review_id": f"RV_{scene_id}_{datetime.now(timezone.utc).astimezone().strftime('%Y%m%d_%H%M%S')}",
            "scene_id": scene_id,
            "status": status,
            "notes": notes,
            "change_request_id": change_request_id,
            "created_at": updated_at,
        }
    )
    write_yaml_file(review_path, review_log)
    snapshot = save_scene_snapshot(path, slug, scene_id, status, notes, change_request_id) if status == "approved" else {}
    return {"ok": True, "project": project_detail(slug), "review_log": review_log, "snapshot": snapshot}


def save_scene_snapshot(
    path: Path,
    slug: str,
    scene_id: str,
    status: str,
    notes: str = "",
    change_request_id: str = "",
) -> dict[str, object]:
    scene = scene_by_id(path, scene_id)
    registry = scene.get("version_registry", {})
    versions = registry.get("versions", []) if isinstance(registry, dict) else []
    if not isinstance(versions, list):
        versions = []
    change_requests = scene.get("change_requests", [])
    if not isinstance(change_requests, list):
        change_requests = []
    review_log = load_scene_review_log(path, scene_id)
    reviews = review_log.get("reviews", [])
    if not isinstance(reviews, list):
        reviews = []
    stamp = datetime.now(timezone.utc).astimezone().strftime("%Y%m%d_%H%M%S")
    snapshot_id = f"SNAP_{scene_id}_{stamp}"
    snapshot = {
        "schema_version": 1,
        "snapshot_id": snapshot_id,
        "project_slug": slug,
        "scene_id": scene_id,
        "scene_title": scene.get("title", ""),
        "status": status,
        "notes": notes,
        "change_request_id": change_request_id,
        "created_at": now_iso(),
        "shot_ids": scene.get("shot_ids", []),
        "primary_steps": scene.get("primary_steps", []),
        "current_versions": [record for record in versions if isinstance(record, dict) and record.get("status") == "current"],
        "candidate_versions": [record for record in versions if isinstance(record, dict) and record.get("status") == "candidate"],
        "change_requests": [
            {
                "change_request_id": request.get("change_request_id", ""),
                "status": request.get("status", ""),
                "trigger_step": request.get("trigger_step", ""),
                "creative_direction": request.get("creative_direction", ""),
            }
            for request in change_requests
            if isinstance(request, dict) and not str(request.get("status", "")).endswith("_example")
        ],
        "review_tail": reviews[-5:],
        "resource_manifest": scene.get("resource_manifest", {}),
    }
    snapshot_path = path / "10_qa" / "scene_snapshots" / f"{scene_id}_{stamp}.yaml"
    write_yaml_file(snapshot_path, snapshot)
    snapshot["path"] = str(snapshot_path.relative_to(path))
    return snapshot


def next_asset_version(versions: list[dict[str, object]], asset_id: str) -> tuple[str, str]:
    latest_number = 0
    latest_version = ""
    for version in versions:
        if not isinstance(version, dict) or version.get("asset_id") != asset_id:
            continue
        match = re.fullmatch(r"v(\d+)", str(version.get("version", "")))
        if match and int(match.group(1)) >= latest_number:
            latest_number = int(match.group(1))
            latest_version = str(version.get("version", ""))
    return f"v{latest_number + 1:03d}", latest_version


def version_registry_path(path: Path, scene_id: str) -> Path:
    if not re.fullmatch(r"[A-Za-z0-9_.-]+", scene_id):
        raise ValueError("场戏 ID 无效 / Invalid scene id.")
    return path / "10_qa" / "version_registry" / f"{scene_id}.yaml"


def load_version_registry(path: Path, slug: str, scene_id: str) -> dict[str, object]:
    return load_yaml_file(version_registry_path(path, scene_id)) or {
        "schema_version": 1,
        "project_slug": slug,
        "scene_id": scene_id,
        "current_scene_iteration": "scene_iter_001",
        "versions": [],
    }


def load_generation_adapters(path: Path) -> dict[str, object]:
    config = load_yaml_file(path / "00_admin" / "generation_adapters.yaml")
    adapters = config.get("adapters", []) if isinstance(config, dict) else []
    if not isinstance(adapters, list):
        adapters = []
    manual = {
        "adapter_id": "manual_packet",
        "label": "任务包 / Manual packet",
        "type": "manual_packet",
        "enabled": True,
        "description": "只生成可交给外部工具的任务包 / Create handoff packets only.",
    }
    by_id = {"manual_packet": manual}
    for adapter in adapters:
        if not isinstance(adapter, dict):
            continue
        adapter_id = str(adapter.get("adapter_id", "") or "").strip()
        if not re.fullmatch(r"[A-Za-z0-9_.-]+", adapter_id):
            continue
        by_id[adapter_id] = adapter
    return {
        "schema_version": 1,
        "adapters": list(by_id.values()),
    }


def safe_file_stem(value: object) -> str:
    stem = re.sub(r"[^A-Za-z0-9_.-]+", "_", str(value or "")).strip("._")
    return stem or "asset"


def normalize_project_rel_path(rel_path: str) -> str:
    value = rel_path.strip().replace("\\", "/")
    if not value:
        raise ValueError("需要输出路径 / Output path is required.")
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", value) or value.startswith("/"):
        raise ValueError("输出路径必须是项目内相对路径 / Output path must be project-relative.")
    normalized = Path(value)
    if any(part in {"", ".", ".."} for part in normalized.parts):
        raise ValueError("输出路径无效 / Invalid output path.")
    return "/".join(normalized.parts)


def find_version_record(versions: list[dict[str, object]], asset_id: str, version: str) -> dict[str, object] | None:
    for record in versions:
        if not isinstance(record, dict):
            continue
        if record.get("asset_id") == asset_id and record.get("version") == version:
            return record
    return None


def queue_scene_generation(slug: str, payload: dict[str, object]) -> dict[str, object]:
    path = project_path(slug)
    change_request_id = str(payload.get("change_request_id", "") or "").strip()
    request_path = change_request_path(path, change_request_id)
    request = load_yaml_file(request_path)
    if not request:
        raise ValueError("找不到变更请求 / Change request not found.")
    if str(request.get("status", "")).endswith("_example"):
        raise ValueError("样板变更请求不能写入生成队列 / Example change requests cannot be queued.")
    existing_queue = request.get("generation_queue", [])
    if request.get("status") == "generation_queued" and isinstance(existing_queue, list) and existing_queue:
        return {
            "ok": True,
            "already_queued": True,
            "change_request": request,
            "generation_queue": existing_queue,
            "project": project_detail(slug),
        }
    selected_ids = {str(item) for item in payload.get("selected_impact_ids", []) if str(item).strip()}
    if not selected_ids:
        raise ValueError("请选择要新增或修改的资产 / Select assets to create or modify.")
    raw_action_overrides = payload.get("action_overrides", {})
    action_overrides: dict[str, str] = {}
    if isinstance(raw_action_overrides, dict):
        for impact_id, action in raw_action_overrides.items():
            normalized_action = str(action or "").strip()
            if normalized_action in IMPACT_ACTIONS:
                action_overrides[str(impact_id)] = normalized_action
    impacts = request.get("impact_table", [])
    if not isinstance(impacts, list):
        impacts = []
    selected_impacts = []
    for impact in impacts:
        if not isinstance(impact, dict):
            continue
        impact_id = str(impact.get("impact_id", ""))
        if impact_id in action_overrides:
            impact["action"] = action_overrides[impact_id]
            impact["action_overridden"] = True
        is_selected = impact_id in selected_ids
        impact["selected"] = is_selected
        if is_selected and impact.get("action") in {"create", "modify"}:
            selected_impacts.append(impact)
    if not selected_impacts:
        raise ValueError("所选项仅需检查，不会进入生成队列 / Selected items only require review and will not enter the generation queue.")
    scene_id = str(request.get("scene_id", ""))
    registry_path = version_registry_path(path, scene_id)
    registry = load_version_registry(path, slug, scene_id)
    versions = registry.setdefault("versions", [])
    if not isinstance(versions, list):
        versions = []
        registry["versions"] = versions
    queue = []
    for impact in selected_impacts:
        asset_id = str(impact.get("asset_id", ""))
        target_version, parent_version = next_asset_version(versions, asset_id)
        output_path = str(impact.get("path", ""))
        versions.append(
            {
                "asset_id": asset_id,
                "scene_id": scene_id,
                "stage_id": impact.get("stage_id", ""),
                "version": target_version,
                "status": "queued",
                "created_at": now_iso(),
                "change_request_id": change_request_id,
                "trigger_step": request.get("trigger_step", ""),
                "trigger_asset_id": request.get("trigger_asset_id", ""),
                "action": impact.get("action", ""),
                "parent_version": parent_version,
                "target_path": output_path,
                "output_path": "",
                "notes": request.get("creative_direction", ""),
            }
        )
        queue.append(
            {
                "queue_id": f"GEN_{change_request_id}_{len(queue) + 1:03d}",
                "asset_id": asset_id,
                "stage_id": impact.get("stage_id", ""),
                "target_version": target_version,
                "action": impact.get("action", ""),
                "path": output_path,
                "result_path": "",
                "status": "queued",
            }
        )
    request["generation_queue"] = queue
    request["status"] = "generation_queued"
    request["approval"] = {
        "user_confirmed": True,
        "confirmed_at": now_iso(),
        "notes": str(payload.get("notes", "") or ""),
    }
    write_yaml_file(request_path, request)
    write_yaml_file(registry_path, registry)
    set_scene_manifest_status(path, scene_id, "generation_queued", str(request.get("creative_direction", "")))
    job_dir = path / "08_generation" / "jobs" / change_request_id
    write_yaml_file(job_dir / "generation_queue.yaml", {"change_request_id": change_request_id, "queue": queue})
    return {"ok": True, "change_request": request, "generation_queue": queue, "project": project_detail(slug)}


def generation_brief_text(request: dict[str, object], item: dict[str, object], version_record: dict[str, object]) -> str:
    return "\n".join(
        [
            f"# Generation Task / 生成任务: {item.get('queue_id', '')}",
            "",
            f"- Scene / 场戏: {request.get('scene_id', '')}",
            f"- Change request / 变更请求: {request.get('change_request_id', '')}",
            f"- Trigger step / 触发步骤: {request.get('trigger_step', '')}",
            f"- Asset / 资产: {item.get('asset_id', '')}",
            f"- Stage / 步骤: {item.get('stage_id', '')}",
            f"- Target version / 目标版本: {item.get('target_version', '')}",
            f"- Action / 动作: {item.get('action', '')}",
            f"- Source or target path / 原路径或目标路径: {item.get('path', '')}",
            f"- Parent version / 父版本: {version_record.get('parent_version', '')}",
            "",
            "## Creative Direction / 创作方向",
            "",
            str(request.get("creative_direction", "")),
            "",
            "## Operator Notes / 操作说明",
            "",
            "- Use this brief as the handoff packet for the image, video, text, edit, or QA tool that will produce the real asset.",
            "- 使用这份 brief 作为外部图片、视频、文本、剪辑或 QA 工具的任务交接包。",
            "- After real output is produced, replace or link the final asset path in the version record, then promote the version if it passes review.",
            "- 真实输出完成后，把最终资产路径回填到版本记录；审片通过后再晋级为 current。",
            "",
        ]
    )


def generation_task_payload(
    request: dict[str, object],
    item: dict[str, object],
    version_record: dict[str, object],
    packet_path: str,
) -> dict[str, object]:
    return {
        "schema_version": 1,
        "project_slug": request.get("project_slug", ""),
        "scene_id": request.get("scene_id", ""),
        "change_request_id": request.get("change_request_id", ""),
        "trigger_step": request.get("trigger_step", ""),
        "trigger_asset_id": request.get("trigger_asset_id", ""),
        "creative_direction": request.get("creative_direction", ""),
        "queue_id": item.get("queue_id", ""),
        "asset_id": item.get("asset_id", ""),
        "stage_id": item.get("stage_id", ""),
        "target_version": item.get("target_version", ""),
        "action": item.get("action", ""),
        "target_path": item.get("path", ""),
        "parent_version": version_record.get("parent_version", ""),
        "packet_path": packet_path,
    }


def write_generation_packet(
    path: Path,
    change_request_id: str,
    request: dict[str, object],
    item: dict[str, object],
    version_record: dict[str, object],
) -> tuple[str, str, dict[str, object]]:
    asset_id = str(item.get("asset_id", ""))
    target_version = str(item.get("target_version", ""))
    packet_rel_path = str(
        Path("08_generation")
        / "jobs"
        / change_request_id
        / "outputs"
        / f"{safe_file_stem(item.get('queue_id'))}_{safe_file_stem(asset_id)}_{safe_file_stem(target_version)}.md"
    )
    task_rel_path = str(
        Path("08_generation")
        / "jobs"
        / change_request_id
        / "tasks"
        / f"{safe_file_stem(item.get('queue_id'))}_{safe_file_stem(asset_id)}_{safe_file_stem(target_version)}.json"
    )
    task_payload = generation_task_payload(request, item, version_record, packet_rel_path)
    (path / packet_rel_path).parent.mkdir(parents=True, exist_ok=True)
    (path / task_rel_path).parent.mkdir(parents=True, exist_ok=True)
    (path / packet_rel_path).write_text(generation_brief_text(request, item, version_record), encoding="utf-8")
    (path / task_rel_path).write_text(json.dumps(task_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return packet_rel_path, task_rel_path, task_payload


def format_adapter_template(template: object, task: dict[str, object]) -> str:
    raw = str(template or "")
    values = {key: safe_file_stem(value) for key, value in task.items()}
    values.update({f"raw_{key}": str(value or "") for key, value in task.items()})
    try:
        return raw.format(**values)
    except Exception:
        return raw


def command_adapter_result(
    path: Path,
    adapter: dict[str, object],
    task: dict[str, object],
    task_rel_path: str,
    packet_rel_path: str,
) -> dict[str, object]:
    command = adapter.get("command", [])
    if not isinstance(command, list) or not command or not all(isinstance(part, str) and part for part in command):
        raise ValueError("命令适配器缺少 command 数组 / Command adapter requires a command array.")
    if not adapter.get("enabled"):
        raise ValueError("生成适配器未启用 / Generation adapter is not enabled.")
    if adapter.get("requires_confirmation", True):
        raise ValueError("生成适配器仍需确认，未执行 / Generation adapter still requires confirmation and was not run.")
    timeout = int(adapter.get("timeout_seconds", 300) or 300)
    env = {
        **os.environ,
        "PIPELINE_PROJECT_ROOT": str(path),
        "PIPELINE_TASK_JSON": str(path / task_rel_path),
        "PIPELINE_TASK_PACKET": str(path / packet_rel_path),
        "PIPELINE_QUEUE_ID": str(task.get("queue_id", "")),
        "PIPELINE_ASSET_ID": str(task.get("asset_id", "")),
        "PIPELINE_TARGET_VERSION": str(task.get("target_version", "")),
    }
    started_at = now_iso()
    completed = subprocess.run(
        command,
        cwd=path,
        input=json.dumps(task, ensure_ascii=False),
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        env=env,
        timeout=timeout,
        check=False,
    )
    finished_at = now_iso()
    logs_dir = path / "08_generation" / "jobs" / str(task.get("change_request_id", "")) / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    stdout_rel = str(Path("08_generation") / "jobs" / str(task.get("change_request_id", "")) / "logs" / f"{safe_file_stem(task.get('queue_id'))}_stdout.txt")
    stderr_rel = str(Path("08_generation") / "jobs" / str(task.get("change_request_id", "")) / "logs" / f"{safe_file_stem(task.get('queue_id'))}_stderr.txt")
    (path / stdout_rel).write_text(completed.stdout, encoding="utf-8")
    (path / stderr_rel).write_text(completed.stderr, encoding="utf-8")
    result: dict[str, object] = {
        "adapter": adapter.get("adapter_id", "command"),
        "returncode": completed.returncode,
        "started_at": started_at,
        "completed_at": finished_at,
        "stdout_path": stdout_rel,
        "stderr_path": stderr_rel,
    }
    parsed: dict[str, object] = {}
    try:
        raw = completed.stdout.strip()
        parsed = json.loads(raw) if raw else {}
    except json.JSONDecodeError:
        parsed = {}
    if isinstance(parsed, dict):
        result.update({key: value for key, value in parsed.items() if key in {"final_output_path", "output_path", "notes"}})
    if completed.returncode == 0 and not (result.get("final_output_path") or result.get("output_path")):
        output_template = adapter.get("output_path_template", "")
        if output_template:
            result["final_output_path"] = format_adapter_template(output_template, task)
    return result


def run_scene_generation(slug: str, payload: dict[str, object]) -> dict[str, object]:
    path = project_path(slug)
    change_request_id = str(payload.get("change_request_id", "") or "").strip()
    adapter_id = str(payload.get("adapter_id", "manual_packet") or "manual_packet").strip()
    request_path = change_request_path(path, change_request_id)
    request = load_yaml_file(request_path)
    if not request:
        raise ValueError("找不到变更请求 / Change request not found.")
    if str(request.get("status", "")).endswith("_example"):
        raise ValueError("样板变更请求不能执行 / Example change requests cannot be run.")
    queue = request.get("generation_queue", [])
    if not isinstance(queue, list) or not queue:
        raise ValueError("还没有生成队列 / No generation queue yet.")
    scene_id = str(request.get("scene_id", ""))
    registry_path = version_registry_path(path, scene_id)
    registry = load_version_registry(path, slug, scene_id)
    versions = registry.setdefault("versions", [])
    if not isinstance(versions, list):
        versions = []
        registry["versions"] = versions
    adapters = load_generation_adapters(path).get("adapters", [])
    adapter = next((item for item in adapters if isinstance(item, dict) and item.get("adapter_id") == adapter_id), None)
    if adapter is None:
        raise ValueError("找不到生成适配器 / Generation adapter not found.")
    adapter_type = str(adapter.get("type", "manual_packet") or "manual_packet")
    if adapter_type == "command":
        command = adapter.get("command", [])
        if not adapter.get("enabled"):
            raise ValueError("生成适配器未启用 / Generation adapter is not enabled.")
        if adapter.get("requires_confirmation", True):
            raise ValueError("生成适配器仍需确认，未执行 / Generation adapter still requires confirmation and was not run.")
        if not isinstance(command, list) or not command or not all(isinstance(part, str) and part for part in command):
            raise ValueError("命令适配器缺少 command 数组 / Command adapter requires a command array.")
    elif adapter_type != "manual_packet":
        raise ValueError("生成适配器类型无效 / Invalid generation adapter type.")

    now = now_iso()
    job_dir = path / "08_generation" / "jobs" / change_request_id
    outputs_dir = job_dir / "outputs"
    outputs_dir.mkdir(parents=True, exist_ok=True)
    run_items: list[dict[str, object]] = []
    failed_count = 0
    for item in queue:
        if not isinstance(item, dict):
            continue
        if item.get("status") in {"review_ready", "current", "superseded"} and adapter_type == "manual_packet":
            run_items.append(item)
            continue
        asset_id = str(item.get("asset_id", ""))
        target_version = str(item.get("target_version", ""))
        version_record = find_version_record(versions, asset_id, target_version)
        if version_record is None:
            version_record = {
                "asset_id": asset_id,
                "scene_id": scene_id,
                "stage_id": item.get("stage_id", ""),
                "version": target_version,
                "status": "queued",
                "change_request_id": change_request_id,
                "trigger_step": request.get("trigger_step", ""),
                "trigger_asset_id": request.get("trigger_asset_id", ""),
                "parent_version": "",
                "target_path": item.get("path", ""),
                "output_path": "",
                "notes": request.get("creative_direction", ""),
            }
            versions.append(version_record)
        packet_rel_path, task_rel_path, task_payload = write_generation_packet(path, change_request_id, request, item, version_record)
        item["started_at"] = item.get("started_at") or now
        item["result_path"] = packet_rel_path
        item["packet_path"] = packet_rel_path
        item["task_path"] = task_rel_path
        version_record["packet_path"] = packet_rel_path
        version_record["target_path"] = version_record.get("target_path") or item.get("path", "")
        if adapter_type == "manual_packet":
            item["status"] = "review_ready"
            item["adapter"] = "manual_packet"
            item["completed_at"] = now
            version_record["status"] = "candidate"
            version_record["adapter"] = "manual_packet"
            version_record["generated_at"] = now
            version_record["output_path"] = packet_rel_path
            version_record["result_kind"] = "generation_brief"
        elif adapter_type == "command":
            item["adapter"] = adapter_id
            task_payload["change_request_id"] = change_request_id
            try:
                command_result = command_adapter_result(path, adapter, task_payload, task_rel_path, packet_rel_path)
            except Exception as exc:  # noqa: BLE001
                command_result = {
                    "adapter": adapter_id,
                    "returncode": -1,
                    "completed_at": now_iso(),
                    "error": str(exc),
                }
            item["adapter_result"] = command_result
            item["completed_at"] = str(command_result.get("completed_at", now_iso()))
            if command_result.get("returncode") == 0:
                final_output = str(command_result.get("final_output_path") or command_result.get("output_path") or "").strip()
                item["status"] = "review_ready"
                version_record["status"] = "candidate"
                version_record["adapter"] = adapter_id
                version_record["generated_at"] = item["completed_at"]
                version_record["result_kind"] = "final_asset" if final_output else "generation_brief"
                if final_output:
                    try:
                        final_output = normalize_project_rel_path(final_output)
                    except ValueError as exc:
                        failed_count += 1
                        item["status"] = "failed"
                        version_record["status"] = "failed"
                        version_record["error"] = str(exc)
                    else:
                        item["final_output_path"] = final_output
                        item["output_exists"] = (path / final_output).exists()
                        version_record["output_path"] = final_output
                        version_record["final_output_path"] = final_output
                        version_record["output_exists"] = item["output_exists"]
                else:
                    version_record["output_path"] = packet_rel_path
            else:
                failed_count += 1
                item["status"] = "failed"
                version_record["status"] = "failed"
                version_record["adapter"] = adapter_id
                version_record["error"] = str(command_result.get("error") or command_result.get("stderr_path") or "adapter failed")
        else:
            raise ValueError("生成适配器类型无效 / Invalid generation adapter type.")
        run_items.append(item)

    request["generation_queue"] = queue
    request["status"] = "generation_failed" if failed_count and failed_count == len(run_items) else "review_ready"
    request["generation_run"] = {
        "adapter": adapter_id,
        "adapter_type": adapter_type,
        "status": request["status"],
        "started_at": now,
        "completed_at": now,
        "item_count": len(run_items),
        "failed_count": failed_count,
        "notes": str(payload.get("notes", "") or ""),
    }
    write_yaml_file(request_path, request)
    write_yaml_file(registry_path, registry)
    write_yaml_file(job_dir / "generation_queue.yaml", {"change_request_id": change_request_id, "queue": queue})
    write_yaml_file(job_dir / "generation_run.yaml", request["generation_run"])
    set_scene_manifest_status(path, scene_id, "needs_changes" if request["status"] == "generation_failed" else "review_ready", str(request.get("creative_direction", "")))
    return {"ok": True, "change_request": request, "generation_queue": queue, "project": project_detail(slug)}


def update_scene_output(slug: str, payload: dict[str, object]) -> dict[str, object]:
    path = project_path(slug)
    change_request_id = str(payload.get("change_request_id", "") or "").strip()
    queue_id = str(payload.get("queue_id", "") or "").strip()
    output_path = normalize_project_rel_path(str(payload.get("output_path", "") or ""))
    notes = str(payload.get("notes", "") or "").strip()
    request_path = change_request_path(path, change_request_id)
    request = load_yaml_file(request_path)
    if not request:
        raise ValueError("找不到变更请求 / Change request not found.")
    if str(request.get("status", "")).endswith("_example"):
        raise ValueError("样板变更请求不能回填输出 / Example change requests cannot receive outputs.")
    queue = request.get("generation_queue", [])
    if not isinstance(queue, list):
        raise ValueError("生成队列无效 / Generation queue is invalid.")
    item = next((entry for entry in queue if isinstance(entry, dict) and entry.get("queue_id") == queue_id), None)
    if item is None:
        raise ValueError("找不到队列项 / Queue item not found.")
    scene_id = str(request.get("scene_id", ""))
    asset_id = str(item.get("asset_id", ""))
    version = str(item.get("target_version", ""))
    registry_path = version_registry_path(path, scene_id)
    registry = load_version_registry(path, slug, scene_id)
    versions = registry.setdefault("versions", [])
    if not isinstance(versions, list):
        versions = []
        registry["versions"] = versions
    version_record = find_version_record(versions, asset_id, version)
    if version_record is None:
        raise ValueError("找不到版本记录 / Version record not found.")
    now = now_iso()
    output_exists = (path / output_path).exists()

    packet_path = str(item.get("result_path", "") or version_record.get("packet_path", "") or "")
    if not packet_path and version_record.get("result_kind") == "generation_brief":
        packet_path = str(version_record.get("output_path", "") or "")
    if packet_path:
        item["packet_path"] = packet_path
        version_record["packet_path"] = packet_path

    item["final_output_path"] = output_path
    item["status"] = "review_ready"
    item["output_attached_at"] = now
    item["output_exists"] = output_exists
    if notes:
        item["output_notes"] = notes

    version_record["status"] = "candidate"
    version_record["output_path"] = output_path
    version_record["final_output_path"] = output_path
    version_record["result_kind"] = "final_asset"
    version_record["output_attached_at"] = now
    version_record["output_exists"] = output_exists
    if notes:
        version_record["output_notes"] = notes
    registry["updated_at"] = now

    request["generation_queue"] = queue
    request["status"] = "review_ready"
    request["last_output_attached_at"] = now
    write_yaml_file(request_path, request)
    write_yaml_file(registry_path, registry)
    job_dir = path / "08_generation" / "jobs" / change_request_id
    write_yaml_file(job_dir / "generation_queue.yaml", {"change_request_id": change_request_id, "queue": queue})
    set_scene_manifest_status(path, scene_id, "review_ready", str(request.get("creative_direction", "")))
    return {"ok": True, "change_request": request, "version": version_record, "project": project_detail(slug)}


def update_scene_version(slug: str, payload: dict[str, object]) -> dict[str, object]:
    path = project_path(slug)
    scene_id = str(payload.get("scene_id", "") or "").strip()
    asset_id = str(payload.get("asset_id", "") or "").strip()
    version = str(payload.get("version", "") or "").strip()
    action = str(payload.get("action", "promote") or "promote").strip()
    notes = str(payload.get("notes", "") or "").strip()
    if action not in {"promote", "rollback", "set_current"}:
        raise ValueError("版本动作无效 / Invalid version action.")
    if not scene_id or not asset_id or not version:
        raise ValueError("需要场戏、资产和版本 / Scene, asset, and version are required.")
    registry_path = version_registry_path(path, scene_id)
    registry = load_version_registry(path, slug, scene_id)
    versions = registry.setdefault("versions", [])
    if not isinstance(versions, list):
        versions = []
        registry["versions"] = versions
    target = find_version_record(versions, asset_id, version)
    if target is None:
        raise ValueError("找不到版本记录 / Version record not found.")
    now = now_iso()
    previous_current = ""
    for record in versions:
        if not isinstance(record, dict) or record.get("asset_id") != asset_id:
            continue
        if record.get("status") == "current" and record.get("version") != version:
            previous_current = str(record.get("version", ""))
            record["status"] = "superseded"
            record["superseded_at"] = now
            record["superseded_by"] = version
    target["status"] = "current"
    target["current_at"] = now
    target["version_action"] = action
    target["previous_current"] = previous_current
    if notes:
        target["review_notes"] = notes
    registry["updated_at"] = now
    write_yaml_file(registry_path, registry)
    return {"ok": True, "version": target, "project": project_detail(slug)}


def apply_annotations_to_item(item: dict[str, object], annotations: dict[str, object]) -> None:
    assets = annotations.get("assets", {})
    if not isinstance(assets, dict):
        item["annotation"] = {}
        return
    ref = str(item.get("ref", ""))
    annotation = assets.get(ref, {})
    item["annotation"] = annotation if isinstance(annotation, dict) else {}


def apply_annotations_to_previews(previews: dict[str, object], annotations: dict[str, object]) -> None:
    for key in ("assets", "docs", "images", "videos", "audio", "three_d"):
        items = previews.get(key, [])
        if isinstance(items, list):
            for item in items:
                if isinstance(item, dict):
                    apply_annotations_to_item(item, annotations)


def apply_annotations_to_scene_locks(scene_locks: dict[str, object], annotations: dict[str, object]) -> None:
    for item in scene_locks.get("overview_images", []):
        if isinstance(item, dict):
            apply_annotations_to_item(item, annotations)
    for lock in scene_locks.get("items", []):
        if not isinstance(lock, dict):
            continue
        for key in ("preview", "master_asset"):
            item = lock.get(key, {})
            if isinstance(item, dict):
                apply_annotations_to_item(item, annotations)


def split_asset_ref(value: str) -> tuple[str, str]:
    origin, sep, rel_path = value.partition(":")
    if not sep or origin not in {"project", "resource"} or not rel_path:
        raise ValueError("资源引用无效 / Invalid asset reference.")
    return origin, rel_path


def update_resource_annotation(slug: str, payload: dict[str, object]) -> dict[str, object]:
    path = project_path(slug)
    raw_ref = str(payload.get("asset_ref", "")).strip()
    origin, rel_path = split_asset_ref(raw_ref)
    safe_asset_path(slug, origin, rel_path)

    status = str(payload.get("status", "")).strip()
    if status not in ANNOTATION_STATUSES:
        raise ValueError("标注状态无效 / Invalid annotation status.")
    note = str(payload.get("note", "")).replace("\r\n", "\n").replace("\r", "\n").strip()
    if len(note) > 5000:
        note = note[:5000]

    annotations = load_resource_annotations(path)
    assets = annotations.setdefault("assets", {})
    if not isinstance(assets, dict):
        assets = {}
        annotations["assets"] = assets

    ref = asset_ref(origin, rel_path)
    if status or note:
        assets[ref] = {
            "status": status,
            "note": note,
            "updated_at": now_iso(),
        }
    else:
        assets.pop(ref, None)
    annotations["schema_version"] = 1
    annotations["project_slug"] = slug
    annotations["updated_at"] = now_iso()
    write_resource_annotations(path, annotations)
    return {"ok": True, "annotations": load_resource_annotations(path)}


def project_detail(slug: str, include_report_text: bool = True, include_previews: bool = True) -> dict[str, object]:
    path = project_path(slug)
    manifest = load_manifest(path)
    report = report_info(path)
    if not include_report_text:
        report.pop("text", None)
    validation = validate_project(path)
    annotations = load_resource_annotations(path)
    previews = collect_preview_assets(slug, path, manifest) if include_previews else {}
    scene_locks = collect_scene_locks(slug, path) if include_previews else {}
    if include_previews:
        apply_annotations_to_previews(previews, annotations)
        apply_annotations_to_scene_locks(scene_locks, annotations)
    return {
        "slug": slug,
        "path": str(path),
        "manifest": manifest,
        "name": manifest_project_value(manifest, "name") or slug,
        "status": manifest_project_value(manifest, "status") or "unknown",
        "source_root": manifest_project_value(manifest, "source_root"),
        "resource_root": manifest_project_value(manifest, "resource_root"),
        "stages": stage_summary(path),
        "shot_stats": shot_list_stats(path),
        "shots": read_shots(path),
        "validation": validation,
        "report": report,
        "autofill": autofill_info(path),
        "idea_board": load_idea_board(path, slug),
        "annotations": annotations,
        "previews": previews,
        "scene_locks": scene_locks,
        "scene_workbench": load_scene_workbench(path),
        "whitebox_lab": load_whitebox_lab(path),
        "generation_adapters": load_generation_adapters(path),
    }


def list_projects() -> list[dict[str, object]]:
    if not PROJECTS_ROOT.exists():
        return []
    projects = []
    for path in sorted(PROJECTS_ROOT.iterdir()):
        if not path.is_dir() or path.name == "_template":
            continue
        if not (path / "project.yaml").exists():
            continue
        detail = project_detail(path.name, include_report_text=False, include_previews=False)
        stage_statuses = [stage["status"] for stage in detail["stages"]]
        projects.append(
            {
                "slug": path.name,
                "name": detail["name"],
                "path": detail["path"],
                "status": detail["status"],
                "readiness": detail["report"].get("readiness"),
                "p0_count": detail["report"].get("p0_count", 0),
                "stage_pass": stage_statuses.count("pass"),
                "stage_warn": stage_statuses.count("warn"),
                "stage_fail": stage_statuses.count("fail"),
                "shot_rows": detail["shot_stats"].get("rows", 0),
            }
        )
    return projects


def create_project(payload: dict[str, object]) -> dict[str, object]:
    name = str(payload.get("name", "")).strip()
    slug = str(payload.get("slug", "")).strip()
    source_root = str(payload.get("source_root", "")).strip()
    resource_root = str(payload.get("resource_root", "")).strip()
    if not name:
        raise ValueError("项目名必填 / Project name is required.")
    args = ["scripts/create_aigc_project.py", "--name", name, "--root", "projects", "--print-json"]
    if slug:
        validate_slug(slug)
        args.extend(["--slug", slug])
    if source_root:
        args.extend(["--source-root", source_root])
    if resource_root:
        args.extend(["--resource-root", resource_root])
    result = run_repo_script(args)
    return result


def update_project_links(slug: str, payload: dict[str, object]) -> dict[str, object]:
    path = project_path(slug)
    manifest = load_manifest(path)
    project = manifest.setdefault("project", {})
    if not isinstance(project, dict):
        raise ValueError("project.yaml 缺少 project 对象 / project.yaml does not contain a project object.")

    source_root = str(payload.get("source_root", "")).strip()
    resource_root = str(payload.get("resource_root", "")).strip()
    project["source_root"] = source_root
    project["resource_root"] = resource_root
    write_manifest(path, manifest)

    values = {
        "PROJECT_NAME": str(project.get("name", slug)),
        "PROJECT_SLUG": str(project.get("slug", slug)),
        "SOURCE_ROOT_TEXT": source_root if source_root else "(尚未链接 / not linked yet)",
        "RESOURCE_ROOT_TEXT": resource_root if resource_root else "(尚未链接 / not linked yet)",
    }
    (path / "assets_link_map.md").write_text(
        render_template(TEXT_TEMPLATES["assets_link_map.md"], values),
        encoding="utf-8",
    )
    return project_detail(slug)


def idea_board_path(path: Path) -> Path:
    return path / "03_story" / "idea_board" / "idea_board.json"


def idea_board_markdown_path(path: Path) -> Path:
    return path / "03_story" / "idea_board" / "idea_board.md"


def idea_board_csv_path(path: Path) -> Path:
    return path / "07_shots" / "idea_board_prompts.csv"


def whitebox_lab_dir(path: Path) -> Path:
    return path / "06_previs" / "whitebox_lab"


def whitebox_lab_index_path(path: Path) -> Path:
    return whitebox_lab_dir(path) / "whitebox_lab.json"


def bool_from_payload(value: object, default: bool = True) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return default
    text = str(value).strip().lower()
    if text in {"false", "0", "no", "off", "不用", "否"}:
        return False
    if text in {"true", "1", "yes", "on", "用", "是"}:
        return True
    return default


def normalize_idea_reference(ref: dict[str, object], index: int) -> dict[str, object]:
    asset_ref = str(ref.get("asset_ref") or ref.get("ref") or "").strip()
    raw_id = str(ref.get("ref_id") or ref.get("asset_id") or asset_ref or "").strip()
    normalized = {
        "ref_id": safe_file_stem(raw_id) if raw_id else f"REF_{index:03d}",
        "asset_ref": asset_ref,
        "asset_id": str(ref.get("asset_id", "") or "").strip(),
        "path": str(ref.get("path", "") or "").strip(),
        "origin": str(ref.get("origin", "") or "").strip(),
        "kind": str(ref.get("kind", "") or "").strip(),
        "role": str(ref.get("role", "") or "").strip(),
        "note": str(ref.get("note", "") or "").strip(),
        "version_id": str(ref.get("version_id", "") or "").strip(),
        "version_status": str(ref.get("version_status", "") or "").strip(),
        "card_type": str(ref.get("card_type", "") or "").strip(),
        "card_id": str(ref.get("card_id", "") or "").strip(),
        "card_title": str(ref.get("card_title", "") or "").strip(),
    }
    for key in ("usage_note", "generation_guidance"):
        value = str(ref.get(key, "") or "").strip()
        if value:
            normalized[key] = value
    interpretation = ref.get("whitebox_interpretation")
    if isinstance(interpretation, dict):
        normalized["whitebox_interpretation"] = interpretation
    return normalized


def normalize_idea_references(value: object) -> list[dict[str, object]]:
    refs: list[dict[str, object]] = []
    if isinstance(value, list):
        for index, ref in enumerate(value, start=1):
            if isinstance(ref, dict):
                refs.append(normalize_idea_reference(ref, index))
    return refs


def normalize_concept_card_versions(value: object) -> list[dict[str, object]]:
    allowed_statuses = {"candidate", "current", "reference", "rejected"}
    versions: list[dict[str, object]] = []
    if isinstance(value, list):
        for index, version in enumerate(value, start=1):
            if not isinstance(version, dict):
                continue
            raw_output_path = str(version.get("output_path", "") or "").strip()
            if not raw_output_path:
                continue
            output_path = normalize_project_rel_path(raw_output_path)
            status = str(version.get("status", "candidate") or "candidate").strip()
            if status not in allowed_statuses:
                status = "candidate"
            versions.append(
                {
                    "version_id": safe_file_stem(version.get("version_id") or f"v{index:03d}"),
                    "output_path": output_path,
                    "notes": str(version.get("notes", "") or "").strip(),
                    "created_at": str(version.get("created_at", "") or "").strip(),
                    "status": status,
                }
            )
    return versions


def append_current_card_version(
    versions: list[dict[str, object]],
    version_id: str,
    output_path: str,
    notes: str,
) -> list[dict[str, object]]:
    next_versions: list[dict[str, object]] = []
    for version in versions:
        if not isinstance(version, dict):
            continue
        next_version = dict(version)
        if next_version.get("status") == "current":
            next_version["status"] = "candidate"
        next_versions.append(next_version)
    next_versions.append(
        {
            "version_id": version_id,
            "output_path": output_path,
            "notes": notes,
            "created_at": now_iso(),
            "status": "current",
        }
    )
    return next_versions


def normalize_idea_act(act: dict[str, object], index: int) -> dict[str, object]:
    raw_id = str(act.get("act_id") or act.get("id") or "").strip()
    return {
        "act_id": safe_file_stem(raw_id) if raw_id else f"ACT{index:02d}",
        "title": str(act.get("title", "") or "").strip(),
        "summary": str(act.get("summary", "") or "").strip(),
        "dramatic_purpose": str(act.get("dramatic_purpose") or act.get("purpose") or "").strip(),
        "key_beats": str(act.get("key_beats", "") or "").strip(),
        "status": str(act.get("status", "draft") or "draft").strip(),
    }


def normalize_idea_acts(value: object) -> list[dict[str, object]]:
    acts: list[dict[str, object]] = []
    if isinstance(value, list):
        for index, act in enumerate(value, start=1):
            if isinstance(act, dict):
                acts.append(normalize_idea_act(act, index))
    return acts


def normalize_project_bible_card(card: dict[str, object], index: int) -> dict[str, object]:
    raw_id = str(card.get("card_id") or card.get("id") or "").strip()
    raw_act_id = str(card.get("act_id", "") or "").strip()
    versions = normalize_concept_card_versions(card.get("versions", []))
    raw_preview_path = str(card.get("preview_path", "") or "").strip()
    preview_path = normalize_project_rel_path(raw_preview_path) if raw_preview_path else ""
    if not preview_path and versions:
        preview_path = str(versions[-1].get("output_path", "") or "")
    return {
        "card_id": safe_file_stem(raw_id) if raw_id else f"BIBLE_{index:03d}",
        "scope": str(card.get("scope", "project") or "project").strip(),
        "act_id": safe_file_stem(raw_act_id) if raw_act_id else "",
        "category": str(card.get("category", "lookdev") or "lookdev").strip(),
        "title": str(card.get("title", "") or "").strip(),
        "summary": str(card.get("summary", "") or "").strip(),
        "visual_direction": str(card.get("visual_direction", "") or "").strip(),
        "prompt_notes": str(card.get("prompt_notes", "") or "").strip(),
        "revision_note": str(card.get("revision_note", "") or "").strip(),
        "negative_prompt": str(card.get("negative_prompt", "") or "").strip(),
        "selected": bool_from_payload(card.get("selected"), True),
        "image_selected": bool_from_payload(card.get("image_selected"), True),
        "status": str(card.get("status", "draft") or "draft").strip(),
        "references": normalize_idea_references(card.get("references", [])),
        "preview_path": preview_path,
        "versions": versions,
    }


def normalize_project_bible(value: object) -> list[dict[str, object]]:
    cards: list[dict[str, object]] = []
    if isinstance(value, list):
        for index, card in enumerate(value, start=1):
            if isinstance(card, dict):
                cards.append(normalize_project_bible_card(card, index))
    return cards


def enabled_project_bible_cards(board: dict[str, object]) -> list[dict[str, object]]:
    cards = board.get("project_bible", [])
    if not isinstance(cards, list):
        return []
    return [
        card
        for card in cards
        if isinstance(card, dict) and bool_from_payload(card.get("selected"), True)
    ]


def project_bible_references(cards: list[dict[str, object]]) -> list[dict[str, object]]:
    references: list[dict[str, object]] = []
    for card in cards:
        refs = card.get("references", [])
        if isinstance(refs, list):
            references.extend(ref for ref in refs if isinstance(ref, dict))
    return references


def normalize_idea_row(row: dict[str, object], index: int) -> dict[str, object]:
    raw_id = str(row.get("item_id") or row.get("shot_id") or "").strip()
    item_id = safe_file_stem(raw_id) if raw_id else f"IDEA_SHOT_{index:03d}"
    versions = normalize_concept_card_versions(row.get("versions", []))
    return {
        "item_id": item_id,
        "scene_id": str(row.get("scene_id", "") or "").strip(),
        "beat": str(row.get("beat", "") or "").strip(),
        "shot_type": str(row.get("shot_type", "") or "").strip(),
        "frame_description": str(row.get("frame_description", "") or "").strip(),
        "image_prompt": str(row.get("image_prompt", "") or "").strip(),
        "video_prompt": str(row.get("video_prompt", "") or "").strip(),
        "notes": str(row.get("notes", "") or "").strip(),
        "revision_note": str(row.get("revision_note", "") or "").strip(),
        "selected": bool_from_payload(row.get("selected"), True),
        "status": str(row.get("status", "draft") or "draft").strip(),
        "output_path": str(row.get("output_path", "") or "").strip(),
        "output_notes": str(row.get("output_notes", "") or "").strip(),
        "output_attached_at": str(row.get("output_attached_at", "") or "").strip(),
        "versions": versions,
        "references": normalize_idea_references(row.get("references", [])),
    }


def normalize_idea_board(slug: str, payload: dict[str, object]) -> dict[str, object]:
    rows_payload = payload.get("rows", [])
    rows = []
    if isinstance(rows_payload, list):
        for index, row in enumerate(rows_payload, start=1):
            if isinstance(row, dict):
                rows.append(normalize_idea_row(row, index))
    return {
        "schema_version": 1,
        "project_slug": slug,
        "updated_at": now_iso(),
        "idea": str(payload.get("idea", "") or "").strip(),
        "story_title": str(payload.get("story_title", "") or "").strip(),
        "logline": str(payload.get("logline", "") or "").strip(),
        "story_outline": str(payload.get("story_outline", "") or "").strip(),
        "style_notes": str(payload.get("style_notes", "") or "").strip(),
        "acts": normalize_idea_acts(payload.get("acts", [])),
        "project_bible": normalize_project_bible(payload.get("project_bible", [])),
        "global_references": normalize_idea_references(payload.get("global_references", [])),
        "rows": rows,
    }


def idea_board_to_markdown(board: dict[str, object]) -> str:
    lines = [
        "# Idea Board / 创意分镜板",
        "",
        f"- Project / 项目: {board.get('project_slug', '')}",
        f"- Updated / 更新时间: {board.get('updated_at', '')}",
        f"- Story title / 片名: {board.get('story_title', '')}",
        f"- Logline / 一句话: {board.get('logline', '')}",
        "",
        "## Idea / 创意",
        str(board.get("idea", "") or ""),
        "",
        "## Story Outline / 剧本大纲",
        str(board.get("story_outline", "") or ""),
        "",
        "## Style Notes / 风格备注",
        str(board.get("style_notes", "") or ""),
        "",
        "## Acts / 幕结构",
    ]
    acts = board.get("acts", [])
    if isinstance(acts, list) and acts:
        for index, act in enumerate(acts, start=1):
            if not isinstance(act, dict):
                continue
            lines.extend(
                [
                    "",
                    f"### {index:02d}. {act.get('act_id', '')} {act.get('title', '')}",
                    f"- Status / 状态: {act.get('status', '')}",
                    f"- Dramatic purpose / 戏剧功能: {act.get('dramatic_purpose', '')}",
                    f"- Key beats / 关键节拍: {act.get('key_beats', '')}",
                    "",
                    str(act.get("summary", "") or ""),
                ]
            )
    else:
        lines.append("- None")
    lines.extend(
        [
            "",
            "## Project Bible / 总概念",
        ]
    )
    project_bible = board.get("project_bible", [])
    if isinstance(project_bible, list) and project_bible:
        for index, card in enumerate(project_bible, start=1):
            if not isinstance(card, dict):
                continue
            refs = card.get("references", [])
            ref_count = len(refs) if isinstance(refs, list) else 0
            lines.extend(
                [
                    "",
                    f"### {index:02d}. {card.get('card_id', '')} {card.get('title', '')}",
                    f"- Category / 分类: {card.get('category', '')}",
                    f"- Status / 状态: {card.get('status', '')}",
                    f"- Selected / 启用: {card.get('selected', True)}",
                    f"- References / 参考: {ref_count}",
                    "",
                    "Summary / 概念说明:",
                    str(card.get("summary", "") or ""),
                    "",
                    "Visual direction / 视觉方向:",
                    str(card.get("visual_direction", "") or ""),
                    "",
                    "Prompt notes / 提示词要点:",
                    str(card.get("prompt_notes", "") or ""),
                    "",
                    "Revision note / 本次修图意见:",
                    str(card.get("revision_note", "") or ""),
                    "",
                    "Negative prompt / 负面约束:",
                    str(card.get("negative_prompt", "") or ""),
                ]
            )
    else:
        lines.append("- None")
    lines.extend(
        [
        "",
        "## Global References / 全局参考",
        ]
    )
    global_refs = board.get("global_references", [])
    if isinstance(global_refs, list) and global_refs:
        for ref in global_refs:
            if isinstance(ref, dict):
                lines.append(f"- {ref.get('asset_id') or ref.get('path')}: {ref.get('note', '')}")
    else:
        lines.append("- None")
    lines.extend(
        [
        "",
        "## Keyframes / 关键分镜",
        ]
    )
    rows = board.get("rows", [])
    if isinstance(rows, list) and rows:
        for index, row in enumerate(rows, start=1):
            if not isinstance(row, dict):
                continue
            lines.extend(
                [
                    "",
                    f"### {index:03d}. {row.get('item_id', '')}",
                    f"- Scene / 场戏: {row.get('scene_id', '')}",
                    f"- Beat / 剧情点: {row.get('beat', '')}",
                    f"- Shot type / 镜头: {row.get('shot_type', '')}",
                    f"- Selected / 选中: {row.get('selected', True)}",
                    f"- Status / 状态: {row.get('status', '')}",
                    "",
                    "Frame description / 画面描述:",
                    str(row.get("frame_description", "") or ""),
                    "",
                    "Image prompt / 图片提示词:",
                    str(row.get("image_prompt", "") or ""),
                    "",
                    "Video prompt / 视频提示词:",
                    str(row.get("video_prompt", "") or ""),
                    "",
                    "Notes / 备注:",
                    str(row.get("notes", "") or ""),
                    "",
                    "Revision note / 本次修图意见:",
                    str(row.get("revision_note", "") or ""),
                    "",
                    "Shot references / 单条参考:",
                    json.dumps(row.get("references", []), ensure_ascii=False),
                ]
            )
    else:
        lines.append("\n暂无分镜条目 / No storyboard rows yet.")
    return "\n".join(lines).rstrip() + "\n"


def write_idea_board_files(path: Path, board: dict[str, object]) -> None:
    write_yaml_file(idea_board_path(path), board)
    md_path = idea_board_markdown_path(path)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(idea_board_to_markdown(board), encoding="utf-8")
    csv_path = idea_board_csv_path(path)
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "item_id",
        "scene_id",
        "beat",
        "shot_type",
        "frame_description",
        "image_prompt",
        "video_prompt",
        "notes",
        "revision_note",
        "selected",
        "status",
        "output_path",
        "references",
    ]
    rows = board.get("rows", [])
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        if isinstance(rows, list):
            for row in rows:
                if isinstance(row, dict):
                    record = {key: row.get(key, "") for key in fieldnames}
                    record["references"] = json.dumps(row.get("references", []), ensure_ascii=False)
                    writer.writerow(record)


def load_idea_board(path: Path, slug: str) -> dict[str, object]:
    data = load_yaml_file(idea_board_path(path))
    if not data:
        return {
            "schema_version": 1,
            "project_slug": slug,
            "updated_at": "",
            "idea": "",
            "story_title": "",
            "logline": "",
            "story_outline": "",
            "style_notes": "",
            "acts": [],
            "project_bible": [],
            "global_references": [],
            "rows": [],
        }
    board = normalize_idea_board(slug, data)
    board["updated_at"] = str(data.get("updated_at", board.get("updated_at", "")) or "")
    return board


def update_idea_board(slug: str, payload: dict[str, object]) -> dict[str, object]:
    path = project_path(slug)
    existing = load_idea_board(path, slug)
    merged = {**existing, **payload}
    for key in ("acts", "project_bible", "global_references", "rows"):
        if key not in payload:
            merged[key] = existing.get(key, [])
    board = normalize_idea_board(slug, merged)
    write_idea_board_files(path, board)
    return {"ok": True, "idea_board": load_idea_board(path, slug), "project": project_detail(slug)}


def build_idea_image_packet_text(
    slug: str,
    path: Path,
    board: dict[str, object],
    packet_id: str,
    packet_rel_path: str,
    tasks: list[dict[str, object]],
) -> str:
    project_bible = enabled_project_bible_cards(board)
    return "\n".join(
        [
            "# Codex Storyboard Image Batch Handoff / Codex 分镜图片批量生图包",
            "",
            "请解析这个资料包，调用当前聊天里的真实生图能力批量生成分镜图。生成完成后，将每张图片保存到 Suggested output path，并调用回填接口更新网页列表。",
            "",
            "## Codex Run Mode / Codex 执行模式",
            "- 快速出图：不要逐步汇报读取、复制、写入等执行细节；除非缺文件或路径错误，直接生成图片并展示结果。",
            "- 生成前优化：每条提示词先做电影级优化，强化构图、光影、角色连续性、负面约束，再生成图片。",
            "- 如果任务里有 revision_note，它是本轮修改的最高优先级；保留长期设定，只改 revision_note 指定的问题。",
            "- 输出保持短：给关键优化原则、图片预览、保存路径、回填状态。",
            "",
            "## Whitebox Reading Rules / 白模读取规则",
            "- 白模只用于控制空间、机位、构图、人物站位、遮挡关系、动作、景深层次和主要光照方向。",
            "- 不要复制白模的灰色材质、方块/球体/圆柱形状、低模人偶、干净测试渲染质感。",
            "- 最终图必须按分镜提示词、角色参考、场景参考、年代、材质和电影美术方向重建。",
            "- 如果任务里有 whitebox_guidance，以该说明为准；它是白模到最终图之间的解释层。",
            "",
            "## Project / 项目",
            f"- Project slug: {slug}",
            f"- Project root: {path}",
            f"- Packet id: {packet_id}",
            f"- Packet path: {packet_rel_path}",
            "",
            "## Story / 故事",
            f"- Title: {board.get('story_title', '')}",
            f"- Logline: {board.get('logline', '')}",
            "",
            "## Acts / 幕结构",
            "```json",
            json.dumps(board.get("acts", []), ensure_ascii=False, indent=2),
            "```",
            "",
            "## Project Bible / 总概念",
            "这些卡片是项目级视觉圣经，作用于所有任务；分镜备注可以局部覆盖它们。",
            "```json",
            json.dumps(project_bible, ensure_ascii=False, indent=2),
            "```",
            "",
            "## Global References / 全局参考",
            "这些参考作用于所有任务，不要在每条任务里重复理解；仅按 note 使用指定元素。",
            "```json",
            json.dumps(board.get("global_references", []), ensure_ascii=False, indent=2),
            "```",
            "",
            "## Callback / 回填接口",
            f"- POST: http://127.0.0.1:8787/api/projects/{slug}/idea-image-output",
            "- Body: {\"outputs\":[{\"item_id\":\"...\",\"output_path\":\"...\",\"notes\":\"...\"}]}",
            "",
            "## Tasks / 任务",
            "```json",
            json.dumps({"packet_id": packet_id, "project_bible": project_bible, "global_references": board.get("global_references", []), "tasks": tasks}, ensure_ascii=False, indent=2),
            "```",
        ]
    )


def create_idea_image_packet(slug: str, payload: dict[str, object]) -> dict[str, object]:
    path = project_path(slug)
    board = normalize_idea_board(slug, payload) if payload.get("rows") is not None else load_idea_board(path, slug)
    board = enrich_idea_board_whitebox_references(path, board)
    if payload.get("rows") is not None:
        write_idea_board_files(path, board)
    rows = [row for row in board.get("rows", []) if isinstance(row, dict) and row.get("selected", True)]
    if not rows:
        raise ValueError("没有选中的分镜条目 / No selected storyboard rows.")
    project_bible = enabled_project_bible_cards(board)
    bible_references = project_bible_references(project_bible)
    packet_id = f"IDEA_IMG_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    job_dir = path / "08_generation" / "jobs" / packet_id
    outputs_dir = job_dir / "outputs"
    tasks_dir = job_dir / "tasks"
    outputs_dir.mkdir(parents=True, exist_ok=True)
    tasks_dir.mkdir(parents=True, exist_ok=True)
    tasks: list[dict[str, object]] = []
    global_references = board.get("global_references", [])
    if not isinstance(global_references, list):
        global_references = []
    for index, row in enumerate(rows, start=1):
        item_id = safe_file_stem(row.get("item_id") or f"IDEA_SHOT_{index:03d}")
        output_rel_path = str(Path("08_generation") / "jobs" / packet_id / "outputs" / f"{index:03d}_{item_id}.png")
        shot_references = row.get("references", [])
        if not isinstance(shot_references, list):
            shot_references = []
        whitebox_guidance = [
            str(ref.get("generation_guidance", "") or "").strip()
            for ref in [*global_references, *bible_references, *shot_references]
            if isinstance(ref, dict) and is_whitebox_reference(ref) and str(ref.get("generation_guidance", "") or "").strip()
        ]
        task = {
            "task_id": f"{packet_id}_{index:03d}",
            "item_id": item_id,
            "scene_id": row.get("scene_id", ""),
            "beat": row.get("beat", ""),
            "shot_type": row.get("shot_type", ""),
            "frame_description": row.get("frame_description", ""),
            "image_prompt": row.get("image_prompt", ""),
            "video_prompt": row.get("video_prompt", ""),
            "notes": row.get("notes", ""),
            "revision_note": row.get("revision_note", ""),
            "shot_references": shot_references,
            "whitebox_guidance": whitebox_guidance,
            "suggested_output_path": output_rel_path,
            "suggested_output_absolute_path": str(path / output_rel_path),
        }
        tasks.append(task)
        (tasks_dir / f"{index:03d}_{item_id}.json").write_text(json.dumps(task, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    packet_rel_path = str(Path("08_generation") / "jobs" / packet_id / "outputs" / f"{packet_id}_handoff.md")
    packet_text = build_idea_image_packet_text(slug, path, board, packet_id, packet_rel_path, tasks)
    (path / packet_rel_path).write_text(packet_text, encoding="utf-8")
    write_yaml_file(
        job_dir / "storyboard_image_tasks.json",
        {"packet_id": packet_id, "project_bible": project_bible, "global_references": global_references, "tasks": tasks},
    )
    return {
        "ok": True,
        "packet_id": packet_id,
        "packet_path": packet_rel_path,
        "packet_absolute_path": str(path / packet_rel_path),
        "task_count": len(tasks),
        "tasks": tasks,
        "handoff_text": packet_text,
        "project": project_detail(slug),
    }


def update_idea_image_output(slug: str, payload: dict[str, object]) -> dict[str, object]:
    path = project_path(slug)
    board = load_idea_board(path, slug)
    outputs = payload.get("outputs", [])
    if not isinstance(outputs, list):
        outputs = []
    by_id: dict[str, dict[str, object]] = {}
    for item in outputs:
        if not isinstance(item, dict):
            continue
        item_id = safe_file_stem(item.get("item_id", ""))
        if item_id:
            by_id[item_id] = item
    rows = board.get("rows", [])
    updated = 0
    if isinstance(rows, list):
        for row in rows:
            if not isinstance(row, dict):
                continue
            item_id = safe_file_stem(row.get("item_id", ""))
            output = by_id.get(item_id)
            if not output:
                continue
            output_path = normalize_project_rel_path(str(output.get("output_path", "") or ""))
            versions = normalize_concept_card_versions(row.get("versions", []))
            version_id = safe_file_stem(output.get("version_id") or f"v{len(versions) + 1:03d}")
            notes = str(output.get("notes", "") or "")
            versions = append_current_card_version(versions, version_id, output_path, notes)
            row["output_path"] = output_path
            row["output_notes"] = notes
            row["output_attached_at"] = now_iso()
            row["versions"] = versions
            row["status"] = "image_ready"
            updated += 1
    board["updated_at"] = now_iso()
    write_idea_board_files(path, board)
    return {"ok": True, "updated": updated, "idea_board": load_idea_board(path, slug), "project": project_detail(slug)}


def scene_context_for_row(path: Path, board: dict[str, object], row: dict[str, object]) -> dict[str, object]:
    scene_id = str(row.get("scene_id", "") or "")
    scene_data = load_scene_workbench(path)
    scenes = [scene for scene in scene_data.get("scenes", []) if isinstance(scene, dict)]
    scene = next((item for item in scenes if item.get("scene_id") == scene_id), {})
    act_id = str(scene.get("act_id", "") or "")
    scene_ids = {
        str(item.get("scene_id", "") or "")
        for item in scenes
        if act_id and str(item.get("act_id", "") or "") == act_id
    }
    rows = board.get("rows", [])
    if not isinstance(rows, list):
        rows = []
    sibling_rows = [
        item
        for item in rows
        if isinstance(item, dict)
        and (
            str(item.get("scene_id", "") or "") == scene_id
            or (scene_ids and str(item.get("scene_id", "") or "") in scene_ids)
        )
    ]
    related_assets: list[dict[str, object]] = []
    for item in scenes:
        if scene_ids and str(item.get("scene_id", "") or "") not in scene_ids:
            continue
        if not scene_ids and str(item.get("scene_id", "") or "") != scene_id:
            continue
        stage_assets = item.get("resource_manifest", {}).get("stage_assets", {})
        if not isinstance(stage_assets, dict):
            continue
        for step, assets in stage_assets.items():
            if not isinstance(assets, list):
                continue
            for asset in assets:
                if not isinstance(asset, dict):
                    continue
                related_assets.append(
                    {
                        "scene_id": item.get("scene_id", ""),
                        "scene_title": item.get("title", ""),
                        "step": step,
                        "asset_id": asset.get("asset_id", ""),
                        "kind": asset.get("kind", ""),
                        "role": asset.get("role", ""),
                        "path": asset.get("path", ""),
                    }
                )
    return {
        "scene": {
            "scene_id": scene.get("scene_id", scene_id),
            "title": scene.get("title", ""),
            "act_id": act_id,
            "act_title": scene.get("act_title", ""),
        },
        "nearby_storyboard_cards": [
            {
                "item_id": item.get("item_id", ""),
                "scene_id": item.get("scene_id", ""),
                "beat": item.get("beat", ""),
                "shot_type": item.get("shot_type", ""),
                "frame_description": item.get("frame_description", ""),
                "image_prompt": item.get("image_prompt", ""),
                "notes": item.get("notes", ""),
                "revision_note": item.get("revision_note", ""),
                "output_path": item.get("output_path", ""),
                "versions": item.get("versions", []),
            }
            for item in sibling_rows[:40]
        ],
        "related_assets": related_assets[:80],
    }


def build_card_image_packet_text(
    slug: str,
    path: Path,
    board: dict[str, object],
    packet_id: str,
    packet_rel_path: str,
    tasks: list[dict[str, object]],
) -> str:
    context_cards = enabled_project_bible_cards(board)
    return "\n".join(
        [
            "# Codex Card Image Handoff / Codex 卡片图片生成包",
            "",
            "请解析这个资料包，调用当前聊天里的真实生图能力，只为 Tasks 中列出的目标卡片生成图片。不要因为上下文里有其他卡片，就自动生成它们。",
            "",
            "## Codex Run Mode / 执行模式",
            "- 目标是卡片级生成：如果 Tasks 里只有 1 张卡，就只生成 1 张；有多张才批量生成。",
            "- 生成前可做电影级提示词优化，强化构图、光影、材质、角色连续性和负面约束。",
            "- revision_note 是本轮精修意见，优先级高于长期 notes/prompt_notes；不要把一次性修改写死成永久设定。",
            "- Context cards、global references、nearby storyboard cards、related assets 只用于风格和连续性参考，不是生成目标。",
            "- 每个任务保存到 Suggested output path；完成后调用回填接口追加到对应卡片 versions，并更新当前预览。",
            "- 输出保持短：图片预览、保存路径、回填状态。",
            "",
            "## Project / 项目",
            f"- Project slug: {slug}",
            f"- Project root: {path}",
            f"- Packet id: {packet_id}",
            f"- Packet path: {packet_rel_path}",
            "",
            "## Story / 故事",
            f"- Title: {board.get('story_title', '')}",
            f"- Logline: {board.get('logline', '')}",
            "",
            "## Context Cards / 上下文概念卡",
            "这些卡片用于统一人物、场景、道具、美术、年代和负面约束；不要自动生成它们，除非它们也出现在 Tasks 里。",
            "```json",
            json.dumps(context_cards, ensure_ascii=False, indent=2),
            "```",
            "",
            "## Global References / 全局参考",
            "```json",
            json.dumps(board.get("global_references", []), ensure_ascii=False, indent=2),
            "```",
            "",
            "## Callback / 回填接口",
            f"- POST: http://127.0.0.1:8787/api/projects/{slug}/card-image-output",
            "- Body: {\"outputs\":[{\"card_type\":\"storyboard|concept\",\"item_id\":\"...\",\"card_id\":\"...\",\"output_path\":\"...\",\"notes\":\"...\"}]}",
            "",
            "## Tasks / 目标卡片任务",
            "```json",
            json.dumps({"packet_id": packet_id, "tasks": tasks}, ensure_ascii=False, indent=2),
            "```",
        ]
    )


def create_card_image_packet(slug: str, payload: dict[str, object]) -> dict[str, object]:
    path = project_path(slug)
    board = normalize_idea_board(slug, payload) if payload.get("rows") is not None or payload.get("project_bible") is not None else load_idea_board(path, slug)
    board = enrich_idea_board_whitebox_references(path, board)
    if payload.get("rows") is not None or payload.get("project_bible") is not None:
        write_idea_board_files(path, board)
    targets_payload = payload.get("targets", [])
    if not isinstance(targets_payload, list):
        targets_payload = []
    target_keys = []
    for target in targets_payload:
        if not isinstance(target, dict):
            continue
        card_type = str(target.get("card_type") or target.get("type") or "").strip()
        card_id = safe_file_stem(target.get("card_id") or target.get("item_id") or target.get("id") or "")
        if card_type and card_id:
            target_keys.append((card_type, card_id))
    if not target_keys:
        raise ValueError("没有勾选的目标卡片 / No selected target cards.")
    rows = board.get("rows", [])
    cards = board.get("project_bible", [])
    row_by_id = {
        safe_file_stem(row.get("item_id", "")): row
        for row in rows
        if isinstance(row, dict)
    } if isinstance(rows, list) else {}
    card_by_id = {
        safe_file_stem(card.get("card_id", "")): card
        for card in cards
        if isinstance(card, dict)
    } if isinstance(cards, list) else {}
    packet_id = f"CARD_IMG_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    job_dir = path / "08_generation" / "jobs" / packet_id
    outputs_dir = job_dir / "outputs"
    tasks_dir = job_dir / "tasks"
    outputs_dir.mkdir(parents=True, exist_ok=True)
    tasks_dir.mkdir(parents=True, exist_ok=True)
    global_references = board.get("global_references", [])
    if not isinstance(global_references, list):
        global_references = []
    context_cards = enabled_project_bible_cards(board)
    context_references = project_bible_references(context_cards)
    tasks: list[dict[str, object]] = []
    seen: set[tuple[str, str]] = set()
    for card_type, card_id in target_keys:
        key = (card_type, card_id)
        if key in seen:
            continue
        seen.add(key)
        index = len(tasks) + 1
        if card_type == "concept":
            card = card_by_id.get(card_id)
            if not card:
                continue
            versions = card.get("versions", []) if isinstance(card.get("versions", []), list) else []
            output_rel_path = str(Path("08_generation") / "jobs" / packet_id / "outputs" / f"{index:03d}_{card_id}_v{len(versions) + 1:03d}.png")
            card_refs = card.get("references", [])
            if not isinstance(card_refs, list):
                card_refs = []
            whitebox_guidance = [
                str(ref.get("generation_guidance", "") or "").strip()
                for ref in [*global_references, *context_references, *card_refs]
                if isinstance(ref, dict) and is_whitebox_reference(ref) and str(ref.get("generation_guidance", "") or "").strip()
            ]
            task = {
                "task_id": f"{packet_id}_{index:03d}",
                "card_type": "concept",
                "card_id": card_id,
                "category": card.get("category", ""),
                "title": card.get("title", ""),
                "summary": card.get("summary", ""),
                "visual_direction": card.get("visual_direction", ""),
                "prompt_notes": card.get("prompt_notes", ""),
                "revision_note": card.get("revision_note", ""),
                "negative_prompt": card.get("negative_prompt", ""),
                "target_references": card_refs,
                "existing_versions": versions,
                "whitebox_guidance": whitebox_guidance,
                "suggested_output_path": output_rel_path,
                "suggested_output_absolute_path": str(path / output_rel_path),
            }
        elif card_type == "storyboard":
            row = row_by_id.get(card_id)
            if not row:
                continue
            versions = row.get("versions", []) if isinstance(row.get("versions", []), list) else []
            output_rel_path = str(Path("08_generation") / "jobs" / packet_id / "outputs" / f"{index:03d}_{card_id}_v{len(versions) + 1:03d}.png")
            row_refs = row.get("references", [])
            if not isinstance(row_refs, list):
                row_refs = []
            whitebox_guidance = [
                str(ref.get("generation_guidance", "") or "").strip()
                for ref in [*global_references, *context_references, *row_refs]
                if isinstance(ref, dict) and is_whitebox_reference(ref) and str(ref.get("generation_guidance", "") or "").strip()
            ]
            task = {
                "task_id": f"{packet_id}_{index:03d}",
                "card_type": "storyboard",
                "item_id": card_id,
                "scene_id": row.get("scene_id", ""),
                "beat": row.get("beat", ""),
                "shot_type": row.get("shot_type", ""),
                "frame_description": row.get("frame_description", ""),
                "image_prompt": row.get("image_prompt", ""),
                "video_prompt": row.get("video_prompt", ""),
                "notes": row.get("notes", ""),
                "revision_note": row.get("revision_note", ""),
                "target_references": row_refs,
                "existing_output_path": row.get("output_path", ""),
                "existing_versions": versions,
                "nearby_context": scene_context_for_row(path, board, row),
                "whitebox_guidance": whitebox_guidance,
                "suggested_output_path": output_rel_path,
                "suggested_output_absolute_path": str(path / output_rel_path),
            }
        else:
            continue
        tasks.append(task)
        (tasks_dir / f"{index:03d}_{card_type}_{card_id}.json").write_text(json.dumps(task, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if not tasks:
        raise ValueError("没有可生成的目标卡片 / No valid target cards.")
    packet_rel_path = str(Path("08_generation") / "jobs" / packet_id / "outputs" / f"{packet_id}_card_handoff.md")
    packet_text = build_card_image_packet_text(slug, path, board, packet_id, packet_rel_path, tasks)
    (path / packet_rel_path).write_text(packet_text, encoding="utf-8")
    write_yaml_file(job_dir / "card_image_tasks.json", {"packet_id": packet_id, "tasks": tasks})
    return {
        "ok": True,
        "packet_id": packet_id,
        "packet_path": packet_rel_path,
        "packet_absolute_path": str(path / packet_rel_path),
        "task_count": len(tasks),
        "tasks": tasks,
        "handoff_text": packet_text,
        "project": project_detail(slug),
    }


def update_card_image_output(slug: str, payload: dict[str, object]) -> dict[str, object]:
    path = project_path(slug)
    board = load_idea_board(path, slug)
    outputs = payload.get("outputs", [])
    if not isinstance(outputs, list):
        outputs = []
    rows = board.get("rows", [])
    cards = board.get("project_bible", [])
    row_by_id = {
        safe_file_stem(row.get("item_id", "")): row
        for row in rows
        if isinstance(row, dict)
    } if isinstance(rows, list) else {}
    card_by_id = {
        safe_file_stem(card.get("card_id", "")): card
        for card in cards
        if isinstance(card, dict)
    } if isinstance(cards, list) else {}
    updated = 0
    for output in outputs:
        if not isinstance(output, dict):
            continue
        card_type = str(output.get("card_type") or output.get("type") or "").strip()
        output_path = normalize_project_rel_path(str(output.get("output_path", "") or ""))
        notes = str(output.get("notes", "") or "")
        if card_type == "concept":
            card_id = safe_file_stem(output.get("card_id", "") or output.get("item_id", ""))
            card = card_by_id.get(card_id)
            if not card:
                continue
            versions = normalize_concept_card_versions(card.get("versions", []))
            version_id = safe_file_stem(output.get("version_id") or f"v{len(versions) + 1:03d}")
            versions = append_current_card_version(versions, version_id, output_path, notes)
            card["versions"] = versions
            card["preview_path"] = output_path
            card["status"] = "image_ready"
            updated += 1
        elif card_type == "storyboard":
            item_id = safe_file_stem(output.get("item_id", "") or output.get("card_id", ""))
            row = row_by_id.get(item_id)
            if not row:
                continue
            versions = normalize_concept_card_versions(row.get("versions", []))
            version_id = safe_file_stem(output.get("version_id") or f"v{len(versions) + 1:03d}")
            versions = append_current_card_version(versions, version_id, output_path, notes)
            row["versions"] = versions
            row["output_path"] = output_path
            row["output_notes"] = notes
            row["output_attached_at"] = now_iso()
            row["status"] = "image_ready"
            updated += 1
    board["updated_at"] = now_iso()
    write_idea_board_files(path, board)
    return {"ok": True, "updated": updated, "idea_board": load_idea_board(path, slug), "project": project_detail(slug)}


def project_bible_card_kind(card: dict[str, object]) -> str:
    category = str(card.get("category", "") or "").strip()
    if category == "character":
        return "character_ref"
    if category == "location":
        return "scene_ref"
    if category == "prop":
        return "prop_ref"
    if category in {"lookdev", "mood", "period", "constraint"}:
        return "lookdev"
    return "image"


def version_entries_for_output(record: dict[str, object], current_path_key: str) -> list[dict[str, object]]:
    versions = normalize_concept_card_versions(record.get("versions", []))
    current_path = normalize_project_rel_path(str(record.get(current_path_key, "") or "").strip()) if record.get(current_path_key) else ""
    has_current = any(version.get("status") == "current" for version in versions)
    matched_current_path = False
    if current_path:
        for version in versions:
            if version.get("output_path") == current_path:
                matched_current_path = True
                if not has_current and version.get("status") == "candidate":
                    version["status"] = "current"
                    has_current = True
        if not matched_current_path:
            versions.append(
                {
                    "version_id": "current",
                    "output_path": current_path,
                    "notes": str(record.get("output_notes", "") or "").strip(),
                    "created_at": str(record.get("output_attached_at", "") or "").strip(),
                    "status": "current",
                }
            )
    return versions


def package_scope_matches(entry: dict[str, object], scope: str, scene_id: str, act_id: str) -> bool:
    value = str(scope or "all").strip()
    entry_scene = str(entry.get("scene_id", "") or "")
    entry_act = str(entry.get("act_id", "") or "")
    if value == "all":
        return True
    if value == "global":
        return not entry_scene and not entry_act
    if value == "current_scene":
        return bool(scene_id) and entry_scene == scene_id
    if value == "current_act":
        return bool(act_id) and entry_act == act_id
    if value.startswith("scene:"):
        return entry_scene == value.split(":", 1)[1]
    if value.startswith("act:"):
        return entry_act == value.split(":", 1)[1]
    return True


def video_reference_scope_label(scope: str, scene_id: str, act_id: str, scenes: list[dict[str, object]]) -> str:
    if scope == "current_scene" and scene_id:
        scene = next((item for item in scenes if item.get("scene_id") == scene_id), {})
        return f"当前场戏 / Current scene: {scene_id} {scene.get('title', '')}"
    if scope == "current_act" and act_id:
        scene = next((item for item in scenes if item.get("act_id") == act_id), {})
        return f"当前幕 / Current act: {act_id} {scene.get('act_title', '')}"
    if scope.startswith("scene:"):
        return f"场戏 / Scene: {scope.split(':', 1)[1]}"
    if scope.startswith("act:"):
        return f"幕 / Act: {scope.split(':', 1)[1]}"
    if scope == "global":
        return "全局资料库 / Global library"
    return "全部项目 / Whole project"


def collect_video_reference_entries(slug: str, path: Path, board: dict[str, object]) -> list[dict[str, object]]:
    scenes = [scene for scene in load_scene_workbench(path).get("scenes", []) if isinstance(scene, dict)]
    scene_by_id = {str(scene.get("scene_id", "") or ""): scene for scene in scenes}
    entries: list[dict[str, object]] = []
    for card in board.get("project_bible", []):
        if not isinstance(card, dict) or not bool_from_payload(card.get("selected"), True):
            continue
        for version in version_entries_for_output(card, "preview_path"):
            if version.get("status") not in {"current", "reference"}:
                continue
            output_path = str(version.get("output_path", "") or "")
            if not output_path:
                continue
            entries.append(
                {
                    "card_type": "concept",
                    "card_id": card.get("card_id", ""),
                    "title": card.get("title", ""),
                    "category": card.get("category", ""),
                    "kind": project_bible_card_kind(card),
                    "scene_id": "",
                    "act_id": card.get("act_id", ""),
                    "act_title": card.get("act_id", ""),
                    "version_id": version.get("version_id", ""),
                    "version_status": version.get("status", ""),
                    "output_path": output_path,
                    "absolute_path": str(path / output_path),
                    "browser_url": asset_url(slug, "project", output_path),
                    "notes": version.get("notes", ""),
                    "prompt_context": " ".join(
                        str(card.get(key, "") or "").strip()
                        for key in ("summary", "visual_direction", "prompt_notes", "negative_prompt")
                        if str(card.get(key, "") or "").strip()
                    ),
                }
            )
    for row in board.get("rows", []):
        if not isinstance(row, dict):
            continue
        scene = scene_by_id.get(str(row.get("scene_id", "") or ""), {})
        for version in version_entries_for_output(row, "output_path"):
            if version.get("status") not in {"current", "reference"}:
                continue
            output_path = str(version.get("output_path", "") or "")
            if not output_path:
                continue
            entries.append(
                {
                    "card_type": "storyboard",
                    "card_id": row.get("item_id", ""),
                    "title": row.get("beat", "") or row.get("item_id", ""),
                    "category": "storyboard",
                    "kind": "storyboard_keyframe",
                    "scene_id": row.get("scene_id", ""),
                    "scene_title": scene.get("title", ""),
                    "act_id": scene.get("act_id", ""),
                    "act_title": scene.get("act_title", ""),
                    "version_id": version.get("version_id", ""),
                    "version_status": version.get("status", ""),
                    "output_path": output_path,
                    "absolute_path": str(path / output_path),
                    "browser_url": asset_url(slug, "project", output_path),
                    "notes": version.get("notes", ""),
                    "prompt_context": " ".join(
                        str(row.get(key, "") or "").strip()
                        for key in ("frame_description", "image_prompt", "video_prompt", "notes")
                        if str(row.get(key, "") or "").strip()
                    ),
                }
            )
    return entries


def build_video_reference_package_text(package: dict[str, object]) -> str:
    current_assets = package.get("current_assets", [])
    reference_assets = package.get("reference_assets", [])
    lines = [
        "# Video Reference Package / 视频参考图包",
        "",
        "这个包汇总文字界面中已标记为采用或参考的图片版本，用于交给视频模型或后续 Codex 生成视频任务。",
        "This package collects current/reference image versions for video-model handoff.",
        "",
        "## Project / 项目",
        f"- Project slug: {package.get('project_slug', '')}",
        f"- Project root: {package.get('project_root', '')}",
        f"- Package id: {package.get('package_id', '')}",
        f"- Scope: {package.get('scope_label', '')}",
        f"- Created at: {package.get('created_at', '')}",
        "",
        "## Use Rules / 使用规则",
        "- Current assets 是主参考图；优先作为视频模型的画面/角色/场景参考。",
        "- Reference assets 是辅助参考；只按 notes 或 prompt_context 借用元素。",
        "- 不要使用 rejected/candidate 图，除非导演另行指定。",
        "- 保持角色身份、场景空间、年代质感、构图和光线连续性。",
        "",
        f"## Current Assets / 采用图 ({len(current_assets)})",
    ]
    if current_assets:
        for index, item in enumerate(current_assets, start=1):
            lines.extend(
                [
                    "",
                    f"### {index:03d}. {item.get('card_id', '')} {item.get('title', '')}",
                    f"- Type / 类型: {item.get('card_type', '')} · {item.get('kind', '')}",
                    f"- Scene / 场戏: {item.get('scene_id', '')} {item.get('scene_title', '')}",
                    f"- Version / 版本: {item.get('version_id', '')} · {item.get('version_status', '')}",
                    f"- Path / 路径: {item.get('output_path', '')}",
                    f"- Absolute / 绝对路径: {item.get('absolute_path', '')}",
                    f"- Browser URL: {item.get('browser_url', '')}",
                    f"- Notes / 备注: {item.get('notes', '')}",
                    f"- Prompt context / 提示词上下文: {item.get('prompt_context', '')}",
                ]
            )
    else:
        lines.append("- None")
    lines.extend(["", f"## Reference Assets / 辅助参考图 ({len(reference_assets)})"])
    if reference_assets:
        for index, item in enumerate(reference_assets, start=1):
            lines.extend(
                [
                    "",
                    f"### R{index:03d}. {item.get('card_id', '')} {item.get('title', '')}",
                    f"- Type / 类型: {item.get('card_type', '')} · {item.get('kind', '')}",
                    f"- Version / 版本: {item.get('version_id', '')} · {item.get('version_status', '')}",
                    f"- Path / 路径: {item.get('output_path', '')}",
                    f"- Notes / 备注: {item.get('notes', '')}",
                ]
            )
    else:
        lines.append("- None")
    return "\n".join(lines).rstrip() + "\n"


def create_current_version_package(slug: str, payload: dict[str, object]) -> dict[str, object]:
    path = project_path(slug)
    board = load_idea_board(path, slug)
    scope = str(payload.get("scope", "all") or "all").strip()
    scene_id = str(payload.get("scene_id", "") or "").strip()
    act_id = str(payload.get("act_id", "") or "").strip()
    scenes = [scene for scene in load_scene_workbench(path).get("scenes", []) if isinstance(scene, dict)]
    entries = collect_video_reference_entries(slug, path, board)
    scoped_entries = [entry for entry in entries if package_scope_matches(entry, scope, scene_id, act_id)]
    global_context = [
        entry
        for entry in entries
        if entry.get("card_type") == "concept"
        and not entry.get("act_id")
        and entry not in scoped_entries
        and entry.get("version_status") in {"current", "reference"}
    ]
    current_assets = [entry for entry in scoped_entries if entry.get("version_status") == "current"]
    reference_assets = [entry for entry in scoped_entries if entry.get("version_status") == "reference"]
    if scope not in {"all", "global"}:
        reference_assets.extend(global_context)
    if not current_assets and not reference_assets:
        raise ValueError("当前范围没有采用或参考版本图 / No current or reference image versions in this scope.")
    package_id = f"VRP_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    package_dir = path / "11_delivery" / "video_reference_packages" / package_id
    package_dir.mkdir(parents=True, exist_ok=True)
    package: dict[str, object] = {
        "schema_version": 1,
        "project_slug": slug,
        "project_root": str(path),
        "package_id": package_id,
        "scope": scope,
        "scope_label": video_reference_scope_label(scope, scene_id, act_id, scenes),
        "scene_id": scene_id,
        "act_id": act_id,
        "created_at": now_iso(),
        "current_assets": current_assets,
        "reference_assets": reference_assets,
    }
    json_rel_path = Path("11_delivery") / "video_reference_packages" / package_id / f"{package_id}.json"
    md_rel_path = Path("11_delivery") / "video_reference_packages" / package_id / f"{package_id}.md"
    handoff_text = build_video_reference_package_text(package)
    (path / json_rel_path).write_text(json.dumps(package, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (path / md_rel_path).write_text(handoff_text, encoding="utf-8")
    return {
        "ok": True,
        "package_id": package_id,
        "package_path": str(md_rel_path),
        "package_absolute_path": str(path / md_rel_path),
        "json_path": str(json_rel_path),
        "current_count": len(current_assets),
        "reference_count": len(reference_assets),
        "handoff_text": handoff_text,
        "project": project_detail(slug),
    }


def blender_executable() -> str:
    candidate = shutil.which("blender")
    if candidate:
        return candidate
    app_binary = Path("/Applications/Blender.app/Contents/MacOS/Blender")
    if app_binary.exists():
        return str(app_binary)
    return ""


def load_whitebox_lab(path: Path) -> dict[str, object]:
    data = load_yaml_file(whitebox_lab_index_path(path))
    if not isinstance(data, dict):
        data = {}
    jobs = data.get("jobs", [])
    if not isinstance(jobs, list):
        jobs = []
    return {
        "schema_version": 1,
        "updated_at": str(data.get("updated_at", "") or ""),
        "blender_available": bool(blender_executable()),
        "blender_executable": blender_executable(),
        "jobs": jobs[-24:],
    }


def write_whitebox_lab(path: Path, lab: dict[str, object]) -> None:
    lab_dir = whitebox_lab_dir(path)
    lab_dir.mkdir(parents=True, exist_ok=True)
    lab["schema_version"] = 1
    lab["updated_at"] = now_iso()
    write_yaml_file(whitebox_lab_index_path(path), lab)


def is_whitebox_reference(ref: dict[str, object]) -> bool:
    text = " ".join(
        str(ref.get(key, "") or "").lower()
        for key in ("kind", "role", "asset_id", "ref_id", "asset_ref", "path")
    )
    return "whitebox" in text or "白模" in text or "previs" in text or "blender" in text


def whitebox_interpretation_for_job(job: dict[str, object]) -> dict[str, object]:
    source = job.get("source_asset", {})
    if not isinstance(source, dict):
        source = {}
    tags = job.get("tags", [])
    if not isinstance(tags, list):
        tags = []
    return {
        "mode": "spatial_control_only",
        "source_asset_id": str(source.get("asset_id", "") or ""),
        "source_path": str(source.get("path", "") or ""),
        "replica_note": str(job.get("replica_note", "") or ""),
        "tags": [str(item) for item in tags if str(item).strip()],
        "use_for": [
            "camera framing and lens/composition",
            "subject scale, blocking, pose, sightline, and depth order",
            "major set anchors such as doors, windows, corridors, walls, props, and openings",
            "main light direction, shadow rhythm, and scene readability",
        ],
        "preserve": [
            "overall aspect ratio and camera angle",
            "relative positions between characters and key set pieces",
            "door/window/opening height and screen position when present",
            "foreground/midground/background separation",
        ],
        "ignore": [
            "gray clay material",
            "primitive cube/sphere/cylinder shapes",
            "mannequin or toy-like character appearance",
            "unfinished low-poly geometry",
            "plain studio-white lighting unless the shot explicitly asks for it",
        ],
        "prompt_bridge": (
            "把白模只当作空间、机位、构图、人物站位、遮挡关系、动作和光照方向参考；"
            "不要复制灰色材质、积木形状、低模人偶或 3D 测试渲染质感。"
            "最终图必须按分镜提示词、角色参考和美术风格重建为电影级真实画面。"
        ),
    }


def whitebox_generation_guidance(job_or_ref: dict[str, object]) -> str:
    interpretation = job_or_ref.get("whitebox_interpretation")
    if not isinstance(interpretation, dict):
        interpretation = whitebox_interpretation_for_job(job_or_ref)
    replica_note = str(interpretation.get("replica_note", "") or "").strip()
    source_asset_id = str(interpretation.get("source_asset_id", "") or "").strip()
    source_path = str(interpretation.get("source_path", "") or "").strip()
    header = "Whitebox guidance / 白模读取说明"
    lines = [
        f"{header}:",
        "- Use the whitebox image only for camera, composition, scale, blocking, pose, sightline, depth order, and main lighting direction.",
        "- Preserve the relative positions of characters and key set pieces; preserve major anchors such as door/window/opening height, wall edges, corridors, and foreground/background separation.",
        "- Do not copy gray clay materials, primitive cube/sphere/cylinder shapes, mannequin appearance, low-poly geometry, or clean 3D test-render look.",
        "- Convert the whitebox into the shot's requested cinematic world using the storyboard prompt, character references, scene references, era, materials, atmosphere, and art direction.",
        "- Negative constraint: no toy-like figures, no unfinished previs look, no blank gray surfaces unless explicitly requested, no random text, no watermark.",
    ]
    if source_asset_id or source_path:
        lines.append(f"- Source whitebox replica seed: {source_asset_id or source_path}.")
    if replica_note:
        lines.append(f"- Replica intent / 复刻意图: {replica_note}")
    return "\n".join(lines)


def whitebox_job_lookup(path: Path) -> dict[str, dict[str, object]]:
    lookup: dict[str, dict[str, object]] = {}
    lab = load_whitebox_lab(path)
    jobs = lab.get("jobs", [])
    if not isinstance(jobs, list):
        return lookup
    for job in jobs:
        if not isinstance(job, dict):
            continue
        keys = {
            str(job.get("job_id", "") or ""),
            str(job.get("suggested_render_path", "") or ""),
            f"project:{job.get('suggested_render_path', '')}",
        }
        for key in keys:
            if key:
                lookup[key] = job
    return lookup


def enrich_whitebox_reference_for_generation(ref: dict[str, object], lookup: dict[str, dict[str, object]]) -> dict[str, object]:
    normalized = dict(ref)
    if not is_whitebox_reference(normalized):
        return normalized
    job = (
        lookup.get(str(normalized.get("asset_id", "") or ""))
        or lookup.get(str(normalized.get("ref_id", "") or ""))
        or lookup.get(str(normalized.get("asset_ref", "") or ""))
        or lookup.get(str(normalized.get("path", "") or ""))
        or {}
    )
    source = job if job else normalized
    interpretation = normalized.get("whitebox_interpretation")
    if not isinstance(interpretation, dict):
        interpretation = whitebox_interpretation_for_job(source)
    normalized["whitebox_interpretation"] = interpretation
    normalized.setdefault("usage_note", interpretation.get("prompt_bridge", ""))
    normalized.setdefault("generation_guidance", whitebox_generation_guidance({**source, "whitebox_interpretation": interpretation}))
    return normalized


def enrich_idea_references_for_generation(
    refs: object,
    lookup: dict[str, dict[str, object]],
) -> list[dict[str, object]]:
    enriched: list[dict[str, object]] = []
    if not isinstance(refs, list):
        return enriched
    for index, ref in enumerate(refs, start=1):
        if isinstance(ref, dict):
            enriched.append(enrich_whitebox_reference_for_generation(normalize_idea_reference(ref, index), lookup))
    return enriched


def enrich_idea_board_whitebox_references(path: Path, board: dict[str, object]) -> dict[str, object]:
    lookup = whitebox_job_lookup(path)
    enriched = dict(board)
    enriched["global_references"] = enrich_idea_references_for_generation(board.get("global_references", []), lookup)
    project_bible = []
    for card in board.get("project_bible", []):
        if not isinstance(card, dict):
            continue
        next_card = dict(card)
        next_card["references"] = enrich_idea_references_for_generation(card.get("references", []), lookup)
        project_bible.append(next_card)
    enriched["project_bible"] = project_bible
    rows = []
    for row in board.get("rows", []):
        if not isinstance(row, dict):
            continue
        next_row = dict(row)
        next_row["references"] = enrich_idea_references_for_generation(row.get("references", []), lookup)
        rows.append(next_row)
    enriched["rows"] = rows
    return enriched


def whitebox_reference_for_job(job: dict[str, object]) -> dict[str, object]:
    interpretation = whitebox_interpretation_for_job(job)
    return {
        "ref_id": safe_file_stem(str(job.get("job_id", "") or "whitebox")),
        "asset_ref": f"project:{job.get('suggested_render_path', '')}",
        "asset_id": str(job.get("job_id", "") or "whitebox"),
        "path": str(job.get("suggested_render_path", "") or ""),
        "origin": "project",
        "kind": "whitebox",
        "role": "replica_whitebox",
        "note": str(job.get("default_reference_note", "") or "白模复刻参考 / replica whitebox reference"),
        "usage_note": str(interpretation.get("prompt_bridge", "") or ""),
        "generation_guidance": whitebox_generation_guidance({**job, "whitebox_interpretation": interpretation}),
        "whitebox_interpretation": interpretation,
    }


def attach_whitebox_to_idea_rows(path: Path, slug: str, job: dict[str, object], target_item_ids: list[str]) -> int:
    board = load_idea_board(path, slug)
    rows = board.get("rows", [])
    if not isinstance(rows, list):
        return 0
    target_ids = {safe_file_stem(item) for item in target_item_ids if str(item).strip()}
    ref = whitebox_reference_for_job(job)
    updated = 0
    for row in rows:
        if not isinstance(row, dict):
            continue
        item_id = safe_file_stem(row.get("item_id", ""))
        if item_id not in target_ids:
            continue
        refs = row.get("references", [])
        if not isinstance(refs, list):
            refs = []
        ref_key = ref["asset_ref"]
        if not any(isinstance(item, dict) and item.get("asset_ref") == ref_key for item in refs):
            refs.append(ref)
            row["references"] = refs
            updated += 1
    if updated:
        board["updated_at"] = now_iso()
        write_idea_board_files(path, board)
    return updated


def build_whitebox_blender_script() -> str:
    return r'''import json
import math
import sys
from pathlib import Path

import bpy


def arg_after(flag, default=""):
    if flag in sys.argv:
        index = sys.argv.index(flag)
        if index + 1 < len(sys.argv):
            return sys.argv[index + 1]
    return default


spec_path = Path(arg_after("--spec")).resolve()
spec = json.loads(spec_path.read_text(encoding="utf-8"))
project_root = Path(spec["project_root"]).resolve()
render_path = project_root / spec["suggested_render_path"]
blend_path = project_root / spec["suggested_blend_path"]
render_path.parent.mkdir(parents=True, exist_ok=True)
blend_path.parent.mkdir(parents=True, exist_ok=True)

bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete()

scene = bpy.context.scene
scene.render.engine = "BLENDER_EEVEE_NEXT" if "BLENDER_EEVEE_NEXT" in {item.identifier for item in bpy.types.RenderSettings.bl_rna.properties["engine"].enum_items} else "BLENDER_EEVEE"
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.view_settings.view_transform = "Standard"
scene.view_settings.look = "Medium High Contrast"

mat_white = bpy.data.materials.new("WBX_matte_white")
mat_white.diffuse_color = (0.82, 0.82, 0.78, 1)
mat_dark = bpy.data.materials.new("WBX_dark_openings")
mat_dark.diffuse_color = (0.18, 0.19, 0.18, 1)
mat_light = bpy.data.materials.new("WBX_light_source")
mat_light.diffuse_color = (1.0, 0.92, 0.62, 1)


def cube(name, loc, scale, material):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(material)
    return obj


cube("floor_plane_match_source_perspective", (0, 0, -0.05), (9, 7, 0.1), mat_white)
cube("back_wall_major_plane", (0, 2.7, 1.7), (9, 0.16, 3.4), mat_white)
cube("left_depth_wall", (-4.2, 0.3, 1.6), (0.16, 5.2, 3.2), mat_white)
cube("right_depth_wall", (4.2, 0.3, 1.6), (0.16, 5.2, 3.2), mat_white)

scene_id = (spec.get("scene_id") or "").upper()
if "ARCADE" in scene_id:
    for i, x in enumerate([-2.6, -1.3, 0.0, 1.3, 2.6]):
        cube(f"arcade_cabinet_row_A_{i}", (x, 1.35, 0.72), (0.72, 0.72, 1.45), mat_dark)
    cube("entrance_door_plane", (3.15, 2.58, 1.05), (1.25, 0.18, 2.1), mat_dark)
elif "COMPOUND" in scene_id:
    cube("hidden_arcade_metal_door_with_peephole", (2.7, 2.56, 1.05), (1.35, 0.18, 2.1), mat_dark)
    cube("old_pipe_left_wall", (-3.6, 2.43, 1.55), (0.12, 0.18, 2.4), mat_dark)
else:
    cube("primary_scene_anchor_block", (0, 1.6, 0.9), (2.2, 0.45, 1.8), mat_dark)

for i, x in enumerate([-0.65, 0.0, 0.65]):
    body = cube(f"proxy_character_{i+1}_body", (x, -1.0 - 0.12 * i, 0.75), (0.28, 0.18, 0.9), mat_white)
    head = cube(f"proxy_character_{i+1}_head", (x, -1.0 - 0.12 * i, 1.35), (0.3, 0.24, 0.3), mat_white)
    body.rotation_euler[2] = math.radians((i - 1) * 5)
    head.rotation_euler[2] = math.radians((i - 1) * 5)

bpy.ops.object.light_add(type="AREA", location=(0, -2.7, 4.2))
light = bpy.context.object
light.name = "large_soft_whitebox_key_light"
light.data.energy = 520
light.data.size = 5.0

if "ARCADE" in scene_id:
    bpy.ops.object.light_add(type="POINT", location=(1.8, 1.6, 1.4))
    glow = bpy.context.object
    glow.name = "crt_glow_proxy"
    glow.data.energy = 180
    glow.data.color = (0.45, 0.9, 1.0)

bpy.ops.object.camera_add(location=(0, -5.6, 1.55), rotation=(math.radians(78), 0, 0))
camera = bpy.context.object
camera.name = "CAM_source_replica_1to1"
camera.data.lens = 28
scene.camera = camera

empty = None
bpy.ops.object.empty_add(type="PLAIN_AXES", location=(0, 0.8, 1.0))
empty = bpy.context.object
empty.name = "source_composition_center"
constraint = camera.constraints.new(type="TRACK_TO")
constraint.track_axis = "TRACK_NEGATIVE_Z"
constraint.up_axis = "UP_Y"
constraint.target = empty

for note_index, target in enumerate(spec.get("targets", []), start=1):
    empty = bpy.data.objects.new(f"target_{note_index:02d}_{target.get('item_id', 'shot')}", None)
    empty.empty_display_type = "CUBE"
    empty.empty_display_size = 0.25
    empty.location = (0.35 * (note_index % 5), -0.6 + 0.15 * note_index, 1.2)
    bpy.context.collection.objects.link(empty)

scene.render.filepath = str(render_path)
bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
bpy.ops.render.render(write_still=True)
'''


def build_whitebox_handoff_text(slug: str, path: Path, job: dict[str, object], spec: dict[str, object]) -> str:
    return "\n".join(
        [
            "# Codex Blender Whitebox Handoff / Codex Blender 白模复刻交接包",
            "",
            "请解析这个资料包，调用 Blender 制作源图 1:1 白模复刻，并按目标分镜生成可作为图生图参考的高清白模图。",
            "",
            "## Project / 项目",
            f"- Project slug: {slug}",
            f"- Project root: {path}",
            f"- Job id: {job.get('job_id', '')}",
            f"- Source asset: {job.get('source_asset', {}).get('asset_id', '')}",
            f"- Source path: {job.get('source_asset', {}).get('path', '')}",
            "",
            "## Output / 输出",
            f"- Suggested render path: {job.get('suggested_render_path', '')}",
            f"- Suggested blend path: {job.get('suggested_blend_path', '')}",
            f"- Blender script: {job.get('script_path', '')}",
            f"- Spec path: {job.get('spec_path', '')}",
            "",
            "## Requirements / 要求",
            "- 先复刻源图构图：画幅、主透视线、前中后景层次、门/墙/柜体/道具/人物位置必须一一对应。",
            "- 白模只解决空间、机位、光照、人物形状与动作，不追求材质贴图。",
            "- 对每条目标分镜，根据 frame_description、image_prompt、notes 调整机位、镜头焦段、人物动作和光照。",
            "- 输出 PNG 要能直接作为该分镜的 whitebox reference。",
            "- 完成后保留 suggested_render_path，网页已经把这个 pending whitebox 引用插入目标分镜。",
            "",
            "## Final Image Usage / 最终图使用说明",
            str(job.get("generation_guidance") or whitebox_generation_guidance(job)),
            "",
            "## Spec JSON / 任务规格",
            "```json",
            json.dumps(spec, ensure_ascii=False, indent=2),
            "```",
        ]
    )


def build_precise_whitebox_blender_script() -> str:
    return r'''import json
import math
import sys
from pathlib import Path

import bpy
from mathutils import Vector


def arg_after(flag, default=""):
    if flag in sys.argv:
        index = sys.argv.index(flag)
        if index + 1 < len(sys.argv):
            return sys.argv[index + 1]
    return default


spec_path = Path(arg_after("--spec")).resolve()
spec = json.loads(spec_path.read_text(encoding="utf-8"))
project_root = Path(spec["project_root"]).resolve()
render_path = project_root / spec["suggested_render_path"]
blend_path = project_root / spec["suggested_blend_path"]
source_asset = spec.get("source_asset", {})
source_path = project_root / source_asset.get("path", "")
render_path.parent.mkdir(parents=True, exist_ok=True)
blend_path.parent.mkdir(parents=True, exist_ok=True)

bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete()

scene = bpy.context.scene
try:
    scene.render.engine = "BLENDER_EEVEE_NEXT"
except Exception:
    scene.render.engine = "BLENDER_EEVEE"
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.eevee.taa_render_samples = 64 if hasattr(scene, "eevee") else 16
scene.view_settings.view_transform = "Standard"
scene.view_settings.look = "Medium High Contrast"
scene.world = bpy.data.worlds.new("WBX_gray_world") if not scene.world else scene.world
scene.world.color = (0.78, 0.80, 0.78)


def material(name, color, roughness=0.82):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = color
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = roughness
    return mat


mat_wall = material("WBX_plaster_wall_mid_gray", (0.62, 0.63, 0.60, 1))
mat_wall_dark = material("WBX_recess_shadow_gray", (0.31, 0.33, 0.32, 1))
mat_door = material("WBX_dark_metal_door", (0.23, 0.22, 0.19, 1))
mat_edge = material("WBX_chipped_edge_light", (0.78, 0.78, 0.72, 1))
mat_floor = material("WBX_old_concrete_floor", (0.45, 0.47, 0.45, 1))
mat_proxy = material("WBX_character_proxy_warm_white", (0.82, 0.80, 0.74, 1))
mat_proxy_mid = material("WBX_character_proxy_mid_gray", (0.68, 0.69, 0.64, 1))
mat_proxy_vest = material("WBX_character_proxy_front_vest", (0.58, 0.52, 0.40, 1))
mat_proxy_dark = material("WBX_character_proxy_dark", (0.40, 0.43, 0.42, 1))
mat_black = material("WBX_black_detail", (0.08, 0.08, 0.075, 1))
mat_mark = material("WBX_camera_match_markers", (0.95, 0.86, 0.55, 1))


def cube(name, loc, scale, mat, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc, rotation=rot)
    obj = bpy.context.object
    obj.name = name
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    return obj


def cyl(name, loc, radius, depth, mat, rot=(0, 0, 0), vertices=48):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=loc, rotation=rot)
    obj = bpy.context.object
    obj.name = name
    obj.data.materials.append(mat)
    return obj


def sphere(name, loc, radius, mat, scale=(1, 1, 1)):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, radius=radius, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    obj.data.materials.append(mat)
    return obj


def look_at(obj, target):
    direction = Vector(target) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def add_crack(name, x, z, length=0.55, angle=0.0):
    return cube(name, (x, 0.018, z), (0.018, 0.018, length), mat_black, rot=(0, 0, angle))


def add_child_proxy(name, x, zbase, height, depth_offset, head_turn=0.0, backpack=False, glasses=False, width=0.34, body_mat=None):
    y = depth_offset
    body_mat = body_mat or mat_proxy
    torso_h = height * 0.44
    leg_h = height * 0.34
    head_r = height * 0.095
    cube(f"{name}_torso", (x, y, zbase + leg_h + torso_h * 0.5), (width, 0.18, torso_h), body_mat)
    cube(f"{name}_left_leg", (x - width * 0.18, y, zbase + leg_h * 0.5), (width * 0.22, 0.15, leg_h), mat_proxy_dark)
    cube(f"{name}_right_leg", (x + width * 0.18, y, zbase + leg_h * 0.5), (width * 0.22, 0.15, leg_h), mat_proxy_dark)
    cube(f"{name}_neck", (x, y, zbase + leg_h + torso_h + 0.035), (width * 0.16, 0.12, 0.07), mat_proxy)
    head = sphere(f"{name}_head_turned_to_door", (x + math.sin(head_turn) * 0.04, y, zbase + leg_h + torso_h + head_r + 0.08), head_r, mat_proxy, scale=(0.92, 0.78, 1.08))
    head.rotation_euler[2] = head_turn
    cube(f"{name}_nose_direction_marker", (x + 0.04 + math.sin(head_turn) * 0.05, y - 0.08, zbase + leg_h + torso_h + head_r + 0.08), (0.05, 0.04, 0.025), mat_black)
    cube(f"{name}_left_arm", (x - width * 0.56, y, zbase + leg_h + torso_h * 0.48), (width * 0.16, 0.13, torso_h * 0.72), mat_proxy_dark, rot=(0.0, math.radians(0), math.radians(-8)))
    cube(f"{name}_right_arm", (x + width * 0.56, y, zbase + leg_h + torso_h * 0.48), (width * 0.16, 0.13, torso_h * 0.72), mat_proxy_dark, rot=(0.0, math.radians(0), math.radians(8)))
    if backpack:
        cube(f"{name}_backpack_block", (x - width * 0.42, y + 0.12, zbase + leg_h + torso_h * 0.52), (width * 0.28, 0.18, torso_h * 0.62), mat_wall_dark)
        cube(f"{name}_backpack_strap", (x - width * 0.18, y - 0.095, zbase + leg_h + torso_h * 0.58), (0.035, 0.03, torso_h * 0.78), mat_black)
    if glasses:
        cyl(f"{name}_glasses_left_ring", (x + 0.025, y - 0.087, zbase + leg_h + torso_h + head_r + 0.09), head_r * 0.35, 0.012, mat_black, rot=(math.radians(90), 0, 0), vertices=24)
        cyl(f"{name}_glasses_right_ring", (x + 0.092, y - 0.087, zbase + leg_h + torso_h + head_r + 0.09), head_r * 0.35, 0.012, mat_black, rot=(math.radians(90), 0, 0), vertices=24)
        cube(f"{name}_glasses_bridge", (x + 0.058, y - 0.095, zbase + leg_h + torso_h + head_r + 0.09), (0.045, 0.012, 0.01), mat_black)


# 16:9 camera-matched stage. The source image is kept as a non-rendering camera
# background in the .blend so the whitebox can be refined against it by hand.
cube("source_frame_floor_slab_left_to_door", (-0.1, -0.12, -0.04), (7.7, 4.7, 0.08), mat_floor, rot=(0, 0, math.radians(-1.2)))
cube("rear_plaster_wall_full_width", (0.45, 0.06, 1.55), (7.8, 0.12, 3.1), mat_wall)
cube("deep_black_passage_left_behind_boys", (-1.78, -0.02, 1.45), (0.48, 0.16, 2.9), mat_wall_dark)
cube("left_wall_plane_fading_to_edge", (-2.35, 0.0, 1.35), (0.45, 0.13, 2.7), mat_wall_dark)
cube("door_recess_vertical_light_pillar_left", (0.28, -0.035, 1.53), (0.21, 0.18, 3.05), mat_edge)
cube("right_cracked_plaster_plane", (1.86, 0.02, 1.52), (0.62, 0.14, 3.04), mat_wall)
door = cube("large_closed_dark_metal_door_matches_right_half", (0.92, -0.07, 1.48), (1.22, 0.18, 2.96), mat_door)
cube("thin_shadow_gap_between_wall_and_door", (0.46, -0.18, 1.48), (0.055, 0.08, 2.96), mat_black)
cube("door_bottom_darker_wear_band", (0.92, -0.175, 0.21), (1.22, 0.045, 0.34), mat_black)
cube("door_right_jamb_chipped_vertical", (1.56, -0.16, 1.42), (0.09, 0.18, 2.84), mat_edge)
cube("door_lock_plate", (1.42, -0.19, 0.98), (0.10, 0.035, 0.52), mat_black)
cyl("round_peephole_exact_upper_door_position", (0.84, -0.205, 1.97), 0.055, 0.028, mat_black, rot=(math.radians(90), 0, 0), vertices=48)
cyl("peephole_outer_ring", (0.84, -0.214, 1.97), 0.085, 0.014, mat_mark, rot=(math.radians(90), 0, 0), vertices=48)
cyl("door_handle_curved_proxy", (1.45, -0.225, 0.82), 0.035, 0.42, mat_black, rot=(math.radians(90), 0, math.radians(78)), vertices=24)
cube("small_lock_below_handle", (1.42, -0.22, 0.72), (0.08, 0.04, 0.1), mat_black)
cube("small_wall_hole_left_of_door", (-0.15, -0.07, 1.35), (0.13, 0.035, 0.09), mat_black)

add_crack("right_wall_primary_crack_vertical", 2.08, 2.05, 0.72, math.radians(-11))
add_crack("right_wall_secondary_crack", 1.9, 1.68, 0.45, math.radians(21))
add_crack("rear_wall_center_stain_line", -0.08, 2.02, 0.8, math.radians(-3))
add_crack("door_surface_vertical_stain_01", 0.72, 1.52, 0.9, math.radians(0))
add_crack("door_surface_vertical_stain_02", 1.18, 1.15, 0.7, math.radians(2))

add_child_proxy("older_brother_left_glasses_tall", -1.23, 0.0, 1.78, -0.55, head_turn=math.radians(-8), backpack=False, glasses=True, width=0.42, body_mat=mat_proxy)
add_child_proxy("middle_brother_center_backpack", -0.58, 0.0, 1.52, -0.57, head_turn=math.radians(-13), backpack=True, glasses=False, width=0.36, body_mat=mat_proxy_mid)
add_child_proxy("younger_brother_front_short_near_door", -0.08, 0.0, 1.24, -0.59, head_turn=math.radians(-17), backpack=False, glasses=False, width=0.34, body_mat=mat_proxy_vest)

# Camera and light match the source: eye-height, slight telephoto compression,
# boys occupy left third; door dominates right half.
bpy.ops.object.camera_add(location=(0.05, -6.35, 1.48))
camera = bpy.context.object
camera.name = "CAM_1to1_source_match_ACT1_SHOT_003"
camera.data.type = "ORTHO"
camera.data.ortho_scale = 3.28
camera.data.shift_x = 0.0
camera.data.shift_y = -0.005
look_at(camera, (0.03, -0.06, 1.34))
scene.camera = camera

if source_path.exists():
    try:
        image = bpy.data.images.load(str(source_path))
        bg = camera.data.background_images.new()
        bg.image = image
        bg.alpha = 0.22
        bg.display_depth = "BACK"
        bg.frame_method = "FIT"
    except Exception as exc:
        print(f"Could not load camera background: {exc}")

bpy.ops.object.empty_add(type="PLAIN_AXES", location=(0.35, -0.06, 1.34))
center = bpy.context.object
center.name = "source_image_composition_center"
for label, loc in {
    "source_left_boy_eye_line": (-1.23, -0.22, 1.55),
    "source_middle_boy_eye_line": (-0.58, -0.25, 1.38),
    "source_younger_boy_eye_line": (-0.08, -0.32, 1.14),
    "source_peephole_anchor": (0.84, -0.24, 1.97),
    "source_handle_anchor": (1.45, -0.24, 0.82),
}.items():
    sphere(f"match_marker_{label}", loc, 0.035, mat_mark)

bpy.ops.object.light_add(type="AREA", location=(-2.7, -3.4, 3.2))
key = bpy.context.object
key.name = "soft_overcast_left_key_from_source"
key.data.energy = 360
key.data.size = 4.8
bpy.ops.object.light_add(type="AREA", location=(1.6, -2.3, 2.2))
fill = bpy.context.object
fill.name = "very_soft_door_fill"
fill.data.energy = 45
fill.data.size = 3.2

for obj in bpy.context.scene.objects:
    obj["whitebox_tag"] = "replica_from_source_image"
    obj["source_asset"] = source_asset.get("asset_id", source_asset.get("path", ""))

scene.render.filepath = str(render_path)
bpy.ops.wm.save_as_mainfile(filepath=str(blend_path))
bpy.ops.render.render(write_still=True)
'''


def create_whitebox_job(slug: str, payload: dict[str, object]) -> dict[str, object]:
    path = project_path(slug)
    source = payload.get("source_asset", {})
    if not isinstance(source, dict) or not source.get("path"):
        raise ValueError("缺少源图 / Missing source image.")
    targets_payload = payload.get("targets", [])
    targets = [item for item in targets_payload if isinstance(item, dict)]
    if not targets:
        raise ValueError("请至少选择一个目标分镜 / Select at least one target storyboard row.")
    job_id = f"WBX_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    job_rel_dir = Path("06_previs") / "whitebox_lab" / "jobs" / job_id
    spec_rel_path = job_rel_dir / "blender" / f"{job_id}_spec.json"
    script_rel_path = job_rel_dir / "blender" / f"{job_id}_generate_whitebox.py"
    blend_rel_path = job_rel_dir / "blender" / f"{job_id}.blend"
    render_rel_path = job_rel_dir / "renders" / f"{job_id}_replica_whitebox.png"
    handoff_rel_path = job_rel_dir / "outputs" / f"{job_id}_codex_blender_handoff.md"
    for rel in (spec_rel_path, script_rel_path, blend_rel_path, render_rel_path, handoff_rel_path):
        (path / rel).parent.mkdir(parents=True, exist_ok=True)
    source_norm = {
        "asset_ref": str(source.get("asset_ref") or source.get("ref") or "").strip(),
        "asset_id": str(source.get("asset_id") or source.get("role") or Path(str(source.get("path"))).name).strip(),
        "path": normalize_project_rel_path(str(source.get("path", "") or "")),
        "origin": str(source.get("origin", "project") or "project").strip(),
        "kind": str(source.get("kind", "image") or "image").strip(),
        "scene_id": str(source.get("scene_id", "") or "").strip(),
        "scene_title": str(source.get("scene_title", "") or "").strip(),
        "act_id": str(source.get("act_id", "") or "").strip(),
        "act_title": str(source.get("act_title", "") or "").strip(),
    }
    job = {
        "job_id": job_id,
        "created_at": now_iso(),
        "status": "packet_ready",
        "source_asset": source_norm,
        "tags": [str(item).strip() for item in payload.get("tags", []) if str(item).strip()] if isinstance(payload.get("tags", []), list) else [],
        "replica_note": str(payload.get("replica_note", "") or "").strip(),
        "target_item_ids": [safe_file_stem(item.get("item_id", "")) for item in targets],
        "suggested_render_path": str(render_rel_path),
        "suggested_blend_path": str(blend_rel_path),
        "spec_path": str(spec_rel_path),
        "script_path": str(script_rel_path),
        "handoff_path": str(handoff_rel_path),
        "default_reference_note": "高精度白模复刻：默认作为该分镜空间、机位、光照和人物动作参考 / high-fidelity replica whitebox for blocking, camera, lighting, and pose.",
    }
    job["whitebox_interpretation"] = whitebox_interpretation_for_job(job)
    job["generation_guidance"] = whitebox_generation_guidance(job)
    spec = {
        "schema_version": 1,
        "project_slug": slug,
        "project_root": str(path),
        **job,
        "targets": targets,
        "blender_available": bool(blender_executable()),
        "blender_executable": blender_executable(),
        "workflow": [
            "replicate_source_image_composition_1_to_1",
            "tag_scene_objects_and_whitebox_relationships",
            "derive_camera_lighting_pose_variants_for_targets",
            "render_high_resolution_whitebox_references",
            "keep_suggested_render_path_stable_for_idea_board_references",
        ],
    }
    (path / spec_rel_path).write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (path / script_rel_path).write_text(build_precise_whitebox_blender_script(), encoding="utf-8")
    handoff_text = build_whitebox_handoff_text(slug, path, job, spec)
    (path / handoff_rel_path).write_text(handoff_text, encoding="utf-8")
    lab = load_whitebox_lab(path)
    jobs = lab.get("jobs", [])
    if not isinstance(jobs, list):
        jobs = []
    jobs.append(job)
    lab["jobs"] = jobs[-48:]
    write_whitebox_lab(path, lab)
    attach_count = attach_whitebox_to_idea_rows(path, slug, job, job["target_item_ids"]) if bool_from_payload(payload.get("attach_to_rows"), True) else 0
    return {
        "ok": True,
        "job": job,
        "spec": spec,
        "handoff_text": handoff_text,
        "attached_rows": attach_count,
        "whitebox_lab": load_whitebox_lab(path),
        "project": project_detail(slug),
    }


def send_static(handler: BaseHTTPRequestHandler, path: str) -> None:
    if path in {"", "/"}:
        target = STATIC_ROOT / "index.html"
    else:
        target = (STATIC_ROOT / unquote(path.lstrip("/"))).resolve()
        if STATIC_ROOT.resolve() not in target.parents and target != STATIC_ROOT.resolve():
            send_text(handler, "禁止访问 / Forbidden", status=403)
            return
    if not target.exists() or not target.is_file():
        send_text(handler, "未找到 / Not found", status=404)
        return
    content_type = mimetypes.guess_type(str(target))[0] or "application/octet-stream"
    body = target.read_bytes()
    handler.send_response(200)
    handler.send_header("Content-Type", content_type)
    handler.send_header("Content-Length", str(len(body)))
    add_auth_cookie_header(handler)
    handler.end_headers()
    handler.wfile.write(body)


def send_asset(handler: BaseHTTPRequestHandler, slug: str, query: str) -> None:
    params = parse_qs(query)
    origin = params.get("origin", [""])[0]
    rel_path = params.get("path", [""])[0]
    target = safe_asset_path(slug, origin, rel_path)
    if is_lfs_pointer(target):
        fallback = legacy_coin_slot_asset_path(origin, rel_path)
        if fallback is None:
            send_text(handler, "这张图的原始文件在 Git LFS 上还没下载，本地也没有备份。请联网后运行 git lfs pull 获取。/ This image lives in Git LFS and is not downloaded, with no local backup. Run git lfs pull (online) to fetch it.", status=409)
            return
        target = fallback
    content_type = mimetypes.guess_type(str(target))[0] or "application/octet-stream"
    body = target.read_bytes()
    handler.send_response(200)
    handler.send_header("Content-Type", content_type)
    handler.send_header("Content-Length", str(len(body)))
    handler.send_header("Cache-Control", "no-store")
    add_auth_cookie_header(handler)
    handler.end_headers()
    handler.wfile.write(body)


class PipelineHubHandler(BaseHTTPRequestHandler):
    server_version = "PipelineHub/1.0"

    def log_message(self, fmt: str, *args: object) -> None:
        print(f"[pipeline-hub] {self.address_string()} - {fmt % args}")

    def do_GET(self) -> None:  # noqa: N802
        try:
            self.route_get()
        except (BrokenPipeError, ConnectionResetError):
            return
        except Exception as exc:  # noqa: BLE001
            send_json(self, {"error": str(exc)}, status=500)

    def do_POST(self) -> None:  # noqa: N802
        try:
            self.route_post()
        except (BrokenPipeError, ConnectionResetError):
            return
        except Exception as exc:  # noqa: BLE001
            send_json(self, {"error": str(exc)}, status=500)

    def route_get(self) -> None:
        parsed = urlparse(self.path)
        if not request_is_authorized(self, parsed):
            send_unauthorized(self)
            return
        parts = [part for part in parsed.path.split("/") if part]
        if not parts:
            send_static(self, "/")
            return
        if parts[0] == "static":
            send_static(self, "/".join(parts[1:]))
            return
        if parts == ["api", "projects"]:
            send_json(self, {"projects": list_projects()})
            return
        if len(parts) == 3 and parts[:2] == ["api", "projects"]:
            send_json(self, project_detail(parts[2]))
            return
        if len(parts) == 4 and parts[:2] == ["api", "projects"] and parts[3] == "asset":
            send_asset(self, parts[2], parsed.query)
            return
        if len(parts) == 4 and parts[:2] == ["api", "projects"] and parts[3] == "report":
            detail = project_detail(parts[2])
            send_text(self, detail["report"].get("text", ""))
            return
        send_text(self, "未找到 / Not found", status=404)

    def route_post(self) -> None:
        parsed = urlparse(self.path)
        if not request_is_authorized(self, parsed):
            send_unauthorized(self)
            return
        parts = [part for part in parsed.path.split("/") if part]
        payload = read_json_body(self)
        if parts == ["api", "projects"]:
            send_json(self, create_project(payload))
            return
        if len(parts) == 4 and parts[:2] == ["api", "projects"]:
            slug = parts[2]
            action = parts[3]
            if action == "validate":
                result = run_repo_script(["scripts/validate_aigc_project.py", f"projects/{slug}", "--print-json"])
                send_json(self, result)
                return
            if action == "analyze":
                sample_size = int(payload.get("sample_size", 24) or 24)
                args = ["scripts/analyze_aigc_project.py", f"projects/{slug}", "--sample-size", str(sample_size), "--print-json"]
                if payload.get("include_source_root"):
                    args.append("--include-source-root")
                result = run_repo_script(args)
                result["project"] = project_detail(slug)
                send_json(self, result)
                return
            if action == "autofill":
                sample_size = int(payload.get("sample_size", 24) or 24)
                max_rounds = int(payload.get("max_rounds", 3) or 3)
                args = [
                    "scripts/autofill_aigc_project.py",
                    f"projects/{slug}",
                    "--max-rounds",
                    str(max_rounds),
                    "--sample-size",
                    str(sample_size),
                    "--print-json",
                ]
                if payload.get("include_source_root"):
                    args.append("--include-source-root")
                if payload.get("allow_external"):
                    args.append("--allow-external")
                if payload.get("allow_plugin_install"):
                    args.append("--allow-plugin-install")
                if payload.get("require_external_complete"):
                    args.append("--require-external-complete")
                result = run_repo_script(args)
                result["project"] = project_detail(slug)
                send_json(self, result)
                return
            if action == "scene-locks":
                batch = str(payload.get("batch", "B01") or "B01").strip()
                sequence = str(payload.get("sequence", "") or "").strip()
                label = str(payload.get("label", "first_act") or "first_act").strip()
                args = [
                    "scripts/build_scene_lock_pack.py",
                    f"projects/{slug}",
                    "--batch",
                    batch,
                    "--label",
                    label,
                    "--print-json",
                ]
                if sequence:
                    args.extend(["--sequence", sequence])
                result = run_repo_script(args)
                result["project"] = project_detail(slug)
                send_json(self, result)
                return
            if action == "links":
                send_json(self, update_project_links(slug, payload))
                return
            if action == "annotations":
                send_json(self, update_resource_annotation(slug, payload))
                return
            if action == "idea-board":
                send_json(self, update_idea_board(slug, payload))
                return
            if action == "idea-image-packet":
                send_json(self, create_idea_image_packet(slug, payload))
                return
            if action == "idea-image-output":
                send_json(self, update_idea_image_output(slug, payload))
                return
            if action == "card-image-packet":
                send_json(self, create_card_image_packet(slug, payload))
                return
            if action == "card-image-output":
                send_json(self, update_card_image_output(slug, payload))
                return
            if action == "current-version-package":
                send_json(self, create_current_version_package(slug, payload))
                return
            if action == "whitebox-job":
                send_json(self, create_whitebox_job(slug, payload))
                return
            if action == "scene-change-request":
                send_json(self, create_scene_change_request(slug, payload))
                return
            if action == "scene-generate":
                send_json(self, queue_scene_generation(slug, payload))
                return
            if action == "scene-run-generation":
                send_json(self, run_scene_generation(slug, payload))
                return
            if action == "scene-output":
                send_json(self, update_scene_output(slug, payload))
                return
            if action == "scene-version":
                send_json(self, update_scene_version(slug, payload))
                return
            if action == "scene-status":
                send_json(self, update_scene_status(slug, payload))
                return
        send_text(self, "未找到 / Not found", status=404)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the local AIGC Pipeline Hub.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8787)
    args = parser.parse_args(argv)

    PROJECTS_ROOT.mkdir(parents=True, exist_ok=True)
    httpd = ThreadingHTTPServer((args.host, args.port), PipelineHubHandler)
    print(f"Pipeline Hub running at http://{args.host}:{args.port}")
    if configured_auth_token():
        print(f"Remote access token auth is enabled via {AUTH_TOKEN_ENV}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Stopping Pipeline Hub")
    finally:
        httpd.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
