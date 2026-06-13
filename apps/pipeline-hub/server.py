#!/usr/bin/env python3
"""Local Pipeline Hub for standardized AIGC film projects."""

from __future__ import annotations

import argparse
import json
import mimetypes
import os
import re
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
PREVIEW_DOC_LIMIT = 16
PREVIEW_IMAGE_LIMIT = 24
PREVIEW_VIDEO_LIMIT = 12
PREVIEW_AUDIO_LIMIT = 12
PREVIEW_THREE_D_LIMIT = 18


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def read_json_body(handler: BaseHTTPRequestHandler) -> dict[str, object]:
    length = int(handler.headers.get("Content-Length", "0") or 0)
    if length <= 0:
        return {}
    raw = handler.rfile.read(length).decode("utf-8")
    return json.loads(raw) if raw.strip() else {}


def send_json(handler: BaseHTTPRequestHandler, payload: object, status: int = 200) -> None:
    body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


def send_text(handler: BaseHTTPRequestHandler, text: str, status: int = 200, content_type: str = "text/plain") -> None:
    body = text.encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", f"{content_type}; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


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
        raise ValueError("Invalid project slug.")


def project_path(slug: str) -> Path:
    validate_slug(slug)
    path = (PROJECTS_ROOT / slug).resolve()
    if PROJECTS_ROOT.resolve() not in path.parents and path != PROJECTS_ROOT.resolve():
        raise ValueError("Project path escaped projects root.")
    return path


def load_manifest(path: Path) -> dict[str, object]:
    manifest = path / "project.yaml"
    if not manifest.exists():
        return {}
    text = manifest.read_text(encoding="utf-8")
    if yaml is None:
        return {"raw": text}
    data = yaml.safe_load(text)
    return data if isinstance(data, dict) else {}


def write_manifest(path: Path, manifest: dict[str, object]) -> None:
    if yaml is None:
        raise RuntimeError("PyYAML is required to update project links.")
    (path / "project.yaml").write_text(
        yaml.safe_dump(manifest, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
        newline="\n",
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
        raise ValueError("Unknown asset origin.")
    target = (root / rel_path).resolve()
    if root not in target.parents and target != root:
        raise ValueError("Asset path escaped its root.")
    if not target.exists() or not target.is_file():
        raise FileNotFoundError("Asset not found.")
    return target


def asset_url(slug: str, origin: str, rel_path: str) -> str:
    return f"/api/projects/{slug}/asset?origin={quote(origin)}&path={quote(rel_path)}"


def asset_priority(path: Path) -> tuple[int, str]:
    text = str(path).lower()
    score = 50
    for keyword in (
        "contact",
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
        return "previs"
    if rel_path.startswith("09_edit/"):
        return "edit/audio"
    if rel_path.startswith("10_qa/"):
        return "qa"
    return "document"


def read_preview_text(path: Path, limit: int = 12000) -> str:
    text = path.read_text(encoding="utf-8-sig", errors="ignore")
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + "\n\n[preview truncated]"


def collect_preview_assets(slug: str, path: Path, manifest: dict[str, object]) -> dict[str, object]:
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
        "06_previs/qa/",
        "07_shots/prompts/",
        "07_shots/video_prompts/",
        "09_edit/",
        "10_qa/autofill_runs/autofill_latest",
    )

    for origin, root in preview_roots(path, manifest):
        files = list_files(root)
        for file_path in files:
            category = category_for(file_path)
            counts[category] = counts.get(category, 0) + 1
            rel_path = str(file_path.relative_to(root)).replace("\\", "/")
            item = {
                "origin": origin,
                "path": rel_path,
                "name": file_path.name,
                "category": category,
                "size_kb": round(file_path.stat().st_size / 1024, 1),
                "extension": file_path.suffix.lower(),
                "previewable": file_path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".gif", ".mp4", ".webm", ".mp3", ".wav", ".ogg"},
                "url": asset_url(slug, origin, rel_path),
            }
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

    docs = sorted(docs, key=lambda item: asset_priority(Path(str(item["path"]))))[:PREVIEW_DOC_LIMIT]
    images = sorted(images, key=lambda item: asset_priority(Path(str(item["path"]))))[:PREVIEW_IMAGE_LIMIT]
    videos = sorted(videos, key=lambda item: asset_priority(Path(str(item["path"]))))[:PREVIEW_VIDEO_LIMIT]
    audio = sorted(audio, key=lambda item: asset_priority(Path(str(item["path"]))))[:PREVIEW_AUDIO_LIMIT]
    three_d = sorted(three_d, key=lambda item: asset_priority(Path(str(item["path"]))))[:PREVIEW_THREE_D_LIMIT]
    return {
        "counts": counts,
        "docs": docs,
        "images": images,
        "videos": videos,
        "audio": audio,
        "three_d": three_d,
    }


def report_info(path: Path) -> dict[str, object]:
    report = path / "10_qa" / "reports" / "project_audit_latest.md"
    if not report.exists():
        return {"exists": False, "path": str(report)}
    text = report.read_text(encoding="utf-8", errors="ignore")
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
    text = report.read_text(encoding="utf-8", errors="ignore")
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


def project_detail(slug: str, include_report_text: bool = True, include_previews: bool = True) -> dict[str, object]:
    path = project_path(slug)
    manifest = load_manifest(path)
    report = report_info(path)
    if not include_report_text:
        report.pop("text", None)
    validation = validate_project(path)
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
        "previews": collect_preview_assets(slug, path, manifest) if include_previews else {},
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
        raise ValueError("Project name is required.")
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
        raise ValueError("project.yaml does not contain a project object.")

    source_root = str(payload.get("source_root", "")).strip()
    resource_root = str(payload.get("resource_root", "")).strip()
    project["source_root"] = source_root
    project["resource_root"] = resource_root
    write_manifest(path, manifest)

    values = {
        "PROJECT_NAME": str(project.get("name", slug)),
        "PROJECT_SLUG": str(project.get("slug", slug)),
        "SOURCE_ROOT_TEXT": source_root if source_root else "(not linked yet)",
        "RESOURCE_ROOT_TEXT": resource_root if resource_root else "(not linked yet)",
    }
    (path / "assets_link_map.md").write_text(
        render_template(TEXT_TEMPLATES["assets_link_map.md"], values),
        encoding="utf-8",
        newline="\n",
    )
    return project_detail(slug)


def send_static(handler: BaseHTTPRequestHandler, path: str) -> None:
    if path in {"", "/"}:
        target = STATIC_ROOT / "index.html"
    else:
        target = (STATIC_ROOT / unquote(path.lstrip("/"))).resolve()
        if STATIC_ROOT.resolve() not in target.parents and target != STATIC_ROOT.resolve():
            send_text(handler, "Forbidden", status=403)
            return
    if not target.exists() or not target.is_file():
        send_text(handler, "Not found", status=404)
        return
    content_type = mimetypes.guess_type(str(target))[0] or "application/octet-stream"
    body = target.read_bytes()
    handler.send_response(200)
    handler.send_header("Content-Type", content_type)
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


def send_asset(handler: BaseHTTPRequestHandler, slug: str, query: str) -> None:
    params = parse_qs(query)
    origin = params.get("origin", [""])[0]
    rel_path = params.get("path", [""])[0]
    target = safe_asset_path(slug, origin, rel_path)
    content_type = mimetypes.guess_type(str(target))[0] or "application/octet-stream"
    body = target.read_bytes()
    handler.send_response(200)
    handler.send_header("Content-Type", content_type)
    handler.send_header("Content-Length", str(len(body)))
    handler.send_header("Cache-Control", "no-store")
    handler.end_headers()
    handler.wfile.write(body)


class PipelineHubHandler(BaseHTTPRequestHandler):
    server_version = "PipelineHub/1.0"

    def log_message(self, fmt: str, *args: object) -> None:
        print(f"[pipeline-hub] {self.address_string()} - {fmt % args}")

    def do_GET(self) -> None:  # noqa: N802
        try:
            self.route_get()
        except Exception as exc:  # noqa: BLE001
            send_json(self, {"error": str(exc)}, status=500)

    def do_POST(self) -> None:  # noqa: N802
        try:
            self.route_post()
        except Exception as exc:  # noqa: BLE001
            send_json(self, {"error": str(exc)}, status=500)

    def route_get(self) -> None:
        parsed = urlparse(self.path)
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
        send_text(self, "Not found", status=404)

    def route_post(self) -> None:
        parsed = urlparse(self.path)
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
            if action == "links":
                send_json(self, update_project_links(slug, payload))
                return
        send_text(self, "Not found", status=404)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the local AIGC Pipeline Hub.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8787)
    args = parser.parse_args(argv)

    PROJECTS_ROOT.mkdir(parents=True, exist_ok=True)
    httpd = ThreadingHTTPServer((args.host, args.port), PipelineHubHandler)
    print(f"Pipeline Hub running at http://{args.host}:{args.port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Stopping Pipeline Hub")
    finally:
        httpd.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
