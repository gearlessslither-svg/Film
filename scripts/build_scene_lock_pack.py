#!/usr/bin/env python3
"""Build reusable Scene Lock Packs from a project shot list.

Scene locks are the handoff layer between previs and image/video generation:
they collect the approved master reference, whitebox/camera evidence, prompt
anchors, allowed variation range, and reject rules for each location.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

try:
    import yaml
except Exception:  # pragma: no cover - JSON fallback is still readable.
    yaml = None

try:
    from PIL import Image, ImageDraw, ImageFont, ImageOps
except Exception:  # pragma: no cover - contact sheet is optional.
    Image = None
    ImageDraw = None
    ImageFont = None
    ImageOps = None


SCENE_REFERENCE_HINTS = {
    "SCN_COMPOUND": "media/01_AIGC/scene_refs/SC_01_compound_corner_v001.png",
    "SCN_ARCADE": "media/01_AIGC/scene_refs/SC_02_arcade_interior_v001.png",
    "SCN_ARCADE_EXIT": "media/01_AIGC/scene_refs/SC_03_arcade_exit_v001.png",
    "SCN_ALLEY": "media/01_AIGC/scene_refs/SC_04_secluded_alley_v001.png",
    "SCN_CORRIDOR": "media/01_AIGC/scene_refs/SC_05_abandoned_corridor_phonebooth_v001.png",
    "SCN_PHONE": "media/01_AIGC/scene_refs/SC_05_abandoned_corridor_phonebooth_v001.png",
    "SCN_8BIT": "media/01_AIGC/scene_refs/SC_06_8bit_stage_v001.png",
}

SCENE_DISPLAY_NAMES = {
    "SCN_COMPOUND": ("老小区角落", "Old Residential Compound Corner"),
    "SCN_ARCADE": ("隐藏游戏厅", "Hidden Arcade Room"),
    "SCN_ARCADE_EXIT": ("游戏厅出口", "Arcade Exit"),
    "SCN_ALLEY": ("回家小路", "Secluded Alley"),
    "SCN_CORRIDOR": ("废楼走廊", "Abandoned Corridor"),
    "SCN_PHONE": ("电话亭", "Phone Booth"),
    "SCN_8BIT": ("8-bit 舞台", "8-bit Stage"),
}

FIRST_ACT_BATCH_HINT = "B01"


def read_manifest(project_path: Path) -> dict[str, object]:
    manifest = project_path / "project.yaml"
    if not manifest.exists():
        return {}
    text = manifest.read_text(encoding="utf-8")
    if yaml is None:
        return {}
    data = yaml.safe_load(text)
    return data if isinstance(data, dict) else {}


def manifest_project_value(manifest: dict[str, object], key: str) -> str:
    project = manifest.get("project")
    if isinstance(project, dict):
        value = project.get(key, "")
        return "" if value is None else str(value)
    return ""


def resolve_optional_path(value: str, *, project_path: Path, cwd: Path) -> Path | None:
    if not value or value.startswith("{{"):
        return None
    raw = Path(value)
    candidates = [raw] if raw.is_absolute() else [cwd / raw, project_path.parent.parent / raw, project_path / raw]
    for candidate in candidates:
        if candidate.exists():
            return candidate.resolve()
    return candidates[0].resolve()


def slugify(value: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return re.sub(r"-{2,}", "-", text) or "scene"


def read_shot_rows(project_path: Path) -> list[dict[str, str]]:
    shot_list = project_path / "07_shots" / "shot_list.csv"
    if not shot_list.exists():
        raise FileNotFoundError(f"Missing shot list: {shot_list}")
    with shot_list.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def row_matches_batch(row: dict[str, str], batch: str) -> bool:
    if not batch:
        return True
    needle = f"/{batch.upper()}/"
    haystack = " ".join(
        str(row.get(key, ""))
        for key in ("start_frame", "end_frame", "prompt_path", "shot_id")
    ).replace("\\", "/").upper()
    return needle in haystack


def row_matches_sequence(row: dict[str, str], sequences: set[str]) -> bool:
    if not sequences:
        return True
    return str(row.get("sequence", "")).strip() in sequences


def resolve_asset(rel_path: str, *, project_path: Path, resource_root: Path | None) -> Path | None:
    if not rel_path:
        return None
    raw = Path(rel_path)
    candidates: list[Path] = [raw] if raw.is_absolute() else [project_path / raw]
    if resource_root is not None:
        candidates.extend(
            [
                resource_root / raw,
                resource_root / "media" / "01_AIGC" / raw,
                resource_root / "media" / raw,
            ]
        )
    for candidate in candidates:
        if candidate.exists() and candidate.is_file():
            return candidate.resolve()
    return None


def display_asset(path: Path | None, *, project_path: Path, resource_root: Path | None) -> str:
    if path is None:
        return ""
    for label, root in (("project", project_path), ("resource", resource_root)):
        if root is None:
            continue
        try:
            return f"{label}:{path.relative_to(root).as_posix()}"
        except ValueError:
            continue
    return str(path)


def quote_cell(value: object) -> str:
    return str(value).replace("|", "/").replace("\n", " ").strip()


def clean_block(text: str) -> str:
    cleaned = re.sub(r"(?m)^ {4,12}", "", text).strip()
    return cleaned + "\n"


def markdown_table(headers: list[str], rows: list[list[object]]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(quote_cell(value) for value in row) + " |")
    return "\n".join(lines)


def unique(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        cleaned = value.strip()
        if cleaned and cleaned not in seen:
            result.append(cleaned)
            seen.add(cleaned)
    return result


def write_yaml(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if yaml is not None:
        text = yaml.safe_dump(payload, allow_unicode=True, sort_keys=False)
    else:
        text = json.dumps(payload, ensure_ascii=False, indent=2)
    path.write_text(text, encoding="utf-8", newline="\n")


def write_camera_manifest(path: Path, rows: list[dict[str, str]]) -> None:
    columns = [
        "shot_id",
        "sequence",
        "story_beat",
        "duration_sec",
        "aspect_ratio",
        "location",
        "camera",
        "action",
        "lighting",
        "start_frame",
        "end_frame",
        "prompt_path",
        "status",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row.get(column, "") for column in columns})


def font(size: int):
    if ImageFont is None:
        return None
    for name in (
        "C:/Windows/Fonts/msyh.ttc",
        "C:/Windows/Fonts/simhei.ttf",
        "C:/Windows/Fonts/simsun.ttc",
        "C:/Windows/Fonts/arial.ttf",
        "msyh.ttc",
        "simhei.ttf",
        "arial.ttf",
    ):
        try:
            return ImageFont.truetype(name, size)
        except Exception:
            continue
    return ImageFont.load_default()


def make_contact_sheet(
    output_path: Path,
    title: str,
    items: list[tuple[str, Path]],
    *,
    width: int = 1920,
    height: int = 1080,
) -> bool:
    if Image is None or ImageDraw is None or ImageOps is None or not items:
        return False
    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas = Image.new("RGB", (width, height), "#f4f6f5")
    draw = ImageDraw.Draw(canvas)
    title_font = font(38)
    label_font = font(20)
    small_font = font(16)
    draw.rectangle((0, 0, width, 92), fill="#18332f")
    draw.text((32, 26), title, fill="#ffffff", font=title_font)

    cols = 4
    rows = 3
    gap = 18
    margin_x = 28
    margin_y = 118
    tile_w = (width - margin_x * 2 - gap * (cols - 1)) // cols
    tile_h = (height - margin_y - 28 - gap * (rows - 1)) // rows
    image_h = tile_h - 44

    for index, (label, path) in enumerate(items[: cols * rows]):
        col = index % cols
        row = index // cols
        x = margin_x + col * (tile_w + gap)
        y = margin_y + row * (tile_h + gap)
        draw.rounded_rectangle((x, y, x + tile_w, y + tile_h), radius=8, fill="#ffffff", outline="#d7dfdb")
        try:
            with Image.open(path) as source:
                image = source.convert("RGB")
                image = ImageOps.contain(image, (tile_w - 16, image_h - 12), method=Image.Resampling.LANCZOS)
        except Exception:
            draw.rectangle((x + 8, y + 8, x + tile_w - 8, y + image_h), fill="#dce4e0")
            draw.text((x + 18, y + 40), "unreadable image", fill="#63716c", font=small_font)
            image = None
        if image is not None:
            image_x = x + (tile_w - image.width) // 2
            image_y = y + 8 + (image_h - image.height) // 2
            canvas.paste(image, (image_x, image_y))
        label_text = label[:48]
        draw.rectangle((x, y + image_h, x + tile_w, y + tile_h), fill="#f8faf9")
        draw.text((x + 10, y + image_h + 10), label_text, fill="#1f2926", font=label_font)
    canvas.save(output_path)
    return True


def scene_markdown(
    *,
    project_name: str,
    scene_id: str,
    batch: str,
    generated_at: str,
    rows: list[dict[str, str]],
    master_ref: str,
    preview_path: str,
    anchors: list[str],
    lighting: list[str],
) -> str:
    cn_name, en_name = SCENE_DISPLAY_NAMES.get(scene_id, (scene_id, scene_id))
    shot_table = markdown_table(
        ["Shot", "Seq", "Beat", "Camera", "Action", "Prompt"],
        [
            [
                row.get("shot_id", ""),
                row.get("sequence", ""),
                row.get("story_beat", ""),
                row.get("camera", ""),
                row.get("action", ""),
                row.get("prompt_path", ""),
            ]
            for row in rows
        ],
    )
    return clean_block(
        f"""\
        # Scene Lock Pack - {scene_id}

        Generated at: {generated_at}

        ## 中文

        - 项目: {project_name}
        - 场景: {cn_name} (`{scene_id}`)
        - 批次: {batch}
        - 主参考: `{master_ref or "pending"}`
        - 预览图: `{preview_path or "pending"}`

        这个锁包用于减少同一场景跨镜头生成时的漂移。进入批量生图/视频前，导演应确认主参考、空间轴线、机位、光源、色彩、角色状态和禁错项。

        ### 必须锁定

        - 场景几何、入口/出口方向、前中后景层次、镜头高度和屏幕方向保持一致。
        - 参考图、白模、镜头表和提示词必须指向同一个空间。
        - 允许天气、烟雾、角色表情、轻微构图微调；不允许地点时代、材质、光源逻辑和角色状态漂移。

        ## English

        - Project: {project_name}
        - Scene: {en_name} (`{scene_id}`)
        - Batch: {batch}
        - Master reference: `{master_ref or "pending"}`
        - Preview: `{preview_path or "pending"}`

        This pack is the scene continuity contract for image and video generation. It locks the approved reference, spatial axis, camera family, lighting logic, color behavior, control evidence, and reject rules before batch production.

        ### Locked Anchors

        {chr(10).join(f"- {item}" for item in anchors) if anchors else "- pending"}

        ### Lighting Logic

        {chr(10).join(f"- {item}" for item in lighting) if lighting else "- pending"}

        ## Shot Subset

        {shot_table}
        """
    )


def reference_assets_markdown(
    *,
    scene_id: str,
    master_ref: str,
    rows: list[dict[str, str]],
    asset_rows: list[dict[str, str]],
) -> str:
    asset_table = markdown_table(
        ["Kind", "Shot", "Asset"],
        [[item["kind"], item["shot_id"], item["asset"]] for item in asset_rows],
    )
    return clean_block(
        f"""\
        # Reference Assets - {scene_id}

        ## 中文

        主参考图应作为场景身份锚点，不负责每个镜头的精确构图；精确构图由白模、机位和镜头提示词共同约束。

        ## English

        The master reference is the scene identity anchor. Exact shot composition should be constrained by whitebox, camera manifest, and shot prompts.

        - Master reference: `{master_ref or "pending"}`
        - Shot count: {len(rows)}

        {asset_table}
        """
    )


def control_layers_markdown(scene_id: str, rows: list[dict[str, str]], whitebox_count: int) -> str:
    return clean_block(
        f"""\
        # Control Layers - {scene_id}

        ## 中文

        当前锁包已经索引 `{whitebox_count}` 张白模/空间参考。下一步建议为本场景补齐这些可复用控制层：

        - Depth: 固定前中后景、距离压缩和遮挡关系。
        - Line / Canny: 锁定门框、街机、墙面、地面边界和透视线。
        - Segmentation: 分离角色、街机/门帘、墙体、地面、水面反射。
        - Normal: 需要 Blender 或 3D 白模更完整时再产出。

        ## English

        The pack currently indexes `{whitebox_count}` whitebox/spatial references. Add depth, line, segmentation, and normal layers when a shot becomes part of the next generation batch.

        ## Shot Priority

        {markdown_table(["Shot", "Camera", "Whitebox"], [[row.get("shot_id", ""), row.get("camera", ""), row.get("start_frame", "")] for row in rows])}
        """
    )


def generation_constraints_markdown(scene_id: str, rows: list[dict[str, str]], anchors: list[str]) -> str:
    story_stages = unique([row.get("character_stage_lock", "") for row in rows])
    continuity = unique([row.get("continuity_lock", "") for row in rows])
    return clean_block(
        f"""\
        # Generation Constraints - {scene_id}

        ## Prompt Anchor / 正向锚点

        - Use the scene master reference and the matching whitebox for each shot.
        - Preserve 1990s small-town China, damp lived-in surfaces, restrained VHS grain, low-key realism.
        - Keep practical lighting motivated by CRT screens, old bulbs, street spill, and wet reflections.
        - Maintain locked scene geography, screen direction, child scale, and foreground/midground/background relation.

        ## Continuity Anchors / 连续性锚点

        {chr(10).join(f"- {item}" for item in anchors + story_stages + continuity) if anchors or story_stages or continuity else "- pending"}

        ## Negative Rules / 禁止漂移

        - No modern phones, clean malls, LED signage, fashionable contemporary wardrobe, glossy cyberpunk neon, or ad-style lighting.
        - No text, captions, labels, arrows, diagrams, watermarks, or storyboard borders in generation outputs.
        - Do not let the location mutate between shots; only camera angle, character blocking, smoke density, and minor light flicker may vary.
        - Do not mix later-stage injury, alley dirt, phone booth glow, or 8-bit world states into this scene unless the shot list explicitly says so.
        """
    )


def build_scene_pack(
    *,
    project_path: Path,
    resource_root: Path | None,
    project_name: str,
    output_root: Path,
    scene_id: str,
    rows: list[dict[str, str]],
    batch: str,
    generated_at: str,
) -> dict[str, object]:
    scene_slug = slugify(scene_id)
    scene_dir = output_root / scene_slug
    scene_dir.mkdir(parents=True, exist_ok=True)

    scene_ref = resolve_asset(SCENE_REFERENCE_HINTS.get(scene_id, ""), project_path=project_path, resource_root=resource_root)
    asset_rows: list[dict[str, str]] = []
    contact_items: list[tuple[str, Path]] = []
    if scene_ref is not None:
        contact_items.append((f"{scene_id} master", scene_ref))

    for row in rows:
        shot_id = row.get("shot_id", "")
        for kind, field in (("whitebox", "start_frame"), ("keyframe", "end_frame")):
            resolved = resolve_asset(row.get(field, ""), project_path=project_path, resource_root=resource_root)
            asset_label = display_asset(resolved, project_path=project_path, resource_root=resource_root) or row.get(field, "")
            asset_rows.append({"kind": kind, "shot_id": shot_id, "asset": asset_label})
            if resolved is not None and len(contact_items) < 11:
                contact_items.append((f"{shot_id} {kind}", resolved))

    preview_path = scene_dir / f"{scene_slug}_preview.png"
    preview_created = make_contact_sheet(preview_path, f"{project_name} / {scene_id} Scene Lock", contact_items)

    anchors = unique([row.get("continuity_lock", "") for row in rows])
    lighting = unique([row.get("lighting", "") for row in rows])
    master_ref = display_asset(scene_ref, project_path=project_path, resource_root=resource_root)
    preview_ref = display_asset(preview_path, project_path=project_path, resource_root=resource_root)

    payload = {
        "schema_version": 1,
        "project": project_name,
        "scene_id": scene_id,
        "batch": batch,
        "generated_at": generated_at,
        "master_reference": master_ref,
        "preview_image": preview_ref,
        "shot_count": len(rows),
        "shots": [
            {
                "shot_id": row.get("shot_id", ""),
                "sequence": row.get("sequence", ""),
                "story_beat": row.get("story_beat", ""),
                "camera": row.get("camera", ""),
                "action": row.get("action", ""),
                "lighting": row.get("lighting", ""),
                "start_frame": row.get("start_frame", ""),
                "end_frame": row.get("end_frame", ""),
                "prompt_path": row.get("prompt_path", ""),
            }
            for row in rows
        ],
        "continuity_anchors": anchors,
        "lighting_rules": lighting,
        "allowed_variation": [
            "minor lens framing shift",
            "CRT flicker and haze density",
            "child expression and body micro-blocking",
            "small practical-light intensity changes",
        ],
        "forbidden_drift": [
            "modern era props or signage",
            "changed room/building geography",
            "unmotivated neon or glossy ad lighting",
            "later story-stage injury or dirt unless shot-listed",
            "text, captions, labels, watermarks, or storyboard borders",
        ],
    }

    write_yaml(scene_dir / "scene_lock.yaml", payload)
    (scene_dir / "scene_lock.md").write_text(
        scene_markdown(
            project_name=project_name,
            scene_id=scene_id,
            batch=batch,
            generated_at=generated_at,
            rows=rows,
            master_ref=master_ref,
            preview_path=preview_ref if preview_created else "",
            anchors=anchors,
            lighting=lighting,
        ),
        encoding="utf-8",
        newline="\n",
    )
    write_camera_manifest(scene_dir / "camera_manifest.csv", rows)
    (scene_dir / "reference_assets.md").write_text(
        reference_assets_markdown(scene_id=scene_id, master_ref=master_ref, rows=rows, asset_rows=asset_rows),
        encoding="utf-8",
        newline="\n",
    )
    (scene_dir / "control_layers.md").write_text(
        control_layers_markdown(scene_id, rows, sum(1 for item in asset_rows if item["kind"] == "whitebox" and item["asset"])),
        encoding="utf-8",
        newline="\n",
    )
    (scene_dir / "generation_constraints.md").write_text(
        generation_constraints_markdown(scene_id, rows, anchors),
        encoding="utf-8",
        newline="\n",
    )

    return {
        "scene_id": scene_id,
        "scene_dir": str(scene_dir),
        "shot_count": len(rows),
        "preview_image": str(preview_path) if preview_created else "",
        "master_reference": master_ref,
    }


def build_index(
    *,
    output_root: Path,
    project_name: str,
    batch: str,
    generated_at: str,
    scene_results: list[dict[str, object]],
    rows: list[dict[str, str]],
    overview_image: Path | None,
) -> None:
    table = markdown_table(
        ["Scene", "Shots", "Preview", "Folder"],
        [
            [
                item.get("scene_id", ""),
                item.get("shot_count", 0),
                Path(str(item.get("preview_image", ""))).name if item.get("preview_image") else "-",
                Path(str(item.get("scene_dir", ""))).name,
            ]
            for item in scene_results
        ],
    )
    shot_table = markdown_table(
        ["Shot", "Seq", "Location", "Beat", "Camera"],
        [[row.get("shot_id", ""), row.get("sequence", ""), row.get("location", ""), row.get("story_beat", ""), row.get("camera", "")] for row in rows],
    )
    output_root.mkdir(parents=True, exist_ok=True)
    (output_root / "index.md").write_text(
        clean_block(
            f"""\
            # Scene Lock Index

            Generated at: {generated_at}

            ## 中文

            项目 `{project_name}` 的 `{batch}` 场景锁包已建立。它用于在批量生图/视频前固定场景身份、空间关系、机位家族、光照逻辑、负面约束和允许变化范围。

            ## English

            Scene Lock Packs for `{project_name}` / `{batch}` are ready. Use them as the continuity contract before batch image or video generation.

            - Overview image: `{overview_image.name if overview_image else "pending"}`
            - Shot rows included: {len(rows)}

            ## Scene Packs

            {table}

            ## Included Shots

            {shot_table}
            """
        ),
        encoding="utf-8",
        newline="\n",
    )


def build_scene_locks(args: argparse.Namespace) -> dict[str, object]:
    project_path = Path(args.project_path).expanduser().resolve()
    cwd = Path.cwd().resolve()
    manifest = read_manifest(project_path)
    project_name = manifest_project_value(manifest, "name") or project_path.name
    resource_root = resolve_optional_path(args.resource_root or manifest_project_value(manifest, "resource_root"), project_path=project_path, cwd=cwd)
    output_root = (project_path / args.output_root).resolve() if not Path(args.output_root).is_absolute() else Path(args.output_root).resolve()

    rows = read_shot_rows(project_path)
    sequence_filter = {item.strip() for item in args.sequence.split(",") if item.strip()} if args.sequence else set()
    selected_rows = [
        row
        for row in rows
        if row_matches_sequence(row, sequence_filter) and row_matches_batch(row, args.batch)
    ]
    if not selected_rows:
        raise ValueError(f"No shot rows matched sequence={args.sequence or '*'} batch={args.batch or '*'}")

    by_scene: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in selected_rows:
        scene_id = row.get("location", "").strip() or "SCN_UNKNOWN"
        by_scene[scene_id].append(row)

    generated_at = datetime.now().astimezone().isoformat(timespec="seconds")
    output_root.mkdir(parents=True, exist_ok=True)
    scene_results = [
        build_scene_pack(
            project_path=project_path,
            resource_root=resource_root,
            project_name=project_name,
            output_root=output_root,
            scene_id=scene_id,
            rows=scene_rows,
            batch=args.batch or "all",
            generated_at=generated_at,
        )
        for scene_id, scene_rows in sorted(by_scene.items())
    ]

    overview_items: list[tuple[str, Path]] = []
    for item in scene_results:
        preview = item.get("preview_image")
        if preview:
            overview_items.append((str(item.get("scene_id", "")), Path(str(preview))))
    for row in selected_rows:
        resolved = resolve_asset(row.get("end_frame", ""), project_path=project_path, resource_root=resource_root)
        if resolved is not None:
            overview_items.append((f"{row.get('shot_id', '')} keyframe", resolved))
        if len(overview_items) >= 12:
            break
    label = args.label or ("first_act" if args.batch.upper() == FIRST_ACT_BATCH_HINT else slugify(args.batch or "scene_locks"))
    overview_image = output_root / f"{slugify(label)}_{slugify(args.batch or 'all')}_scene_lock_overview.png"
    overview_created = make_contact_sheet(overview_image, f"{project_name} / {args.batch or 'all'} Scene Locks", overview_items)
    build_index(
        output_root=output_root,
        project_name=project_name,
        batch=args.batch or "all",
        generated_at=generated_at,
        scene_results=scene_results,
        rows=selected_rows,
        overview_image=overview_image if overview_created else None,
    )

    return {
        "status": "ok",
        "project_path": str(project_path),
        "resource_root": str(resource_root) if resource_root else "",
        "output_root": str(output_root),
        "batch": args.batch,
        "sequence": args.sequence,
        "shot_rows": len(selected_rows),
        "scene_count": len(scene_results),
        "overview_image": str(overview_image) if overview_created else "",
        "scenes": scene_results,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build Scene Lock Packs from a standardized AIGC project.")
    parser.add_argument("project_path", help="Path to projects/<slug>")
    parser.add_argument("--batch", default=FIRST_ACT_BATCH_HINT, help="Filter rows by asset batch folder, e.g. B01. Empty means all.")
    parser.add_argument("--sequence", default="", help="Optional comma-separated sequence filter, e.g. 01,02,03.")
    parser.add_argument("--label", default="first_act", help="Human label used for overview filenames.")
    parser.add_argument("--output-root", default="06_previs/scene_locks", help="Output root under the project folder.")
    parser.add_argument("--resource-root", default="", help="Override resource root instead of project.yaml.")
    parser.add_argument("--print-json", action="store_true", help="Print machine-readable summary.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        result = build_scene_locks(args)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    if args.print_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"status={result['status']}")
        print(f"output_root={result['output_root']}")
        print(f"scene_count={result['scene_count']}")
        print(f"shot_rows={result['shot_rows']}")
        print(f"overview_image={result['overview_image']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
