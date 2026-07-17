#!/usr/bin/env python3
"""Validate, contact-sheet, manifest, and package the complete 42-frame delivery."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import zipfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def expected_items() -> list[str]:
    items = [f"SH{index:02d}" for index in range(1, 28)]
    items += ["SH28_KF01", "SH28_KF02"]
    items += [f"SH{index:02d}" for index in range(29, 35)]
    items += ["SH35_KF01", "SH35_KF02", "SH35_KF03", "SH36", "SH37", "SH38_KF01", "SH38_KF02"]
    return items


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = (
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial.ttf",
    )
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def fit_image(path: Path, width: int, height: int) -> Image.Image:
    with Image.open(path) as source:
        image = source.convert("RGB")
    image.thumbnail((width, height), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (width, height), (30, 35, 36))
    x = (width - image.width) // 2
    y = (height - image.height) // 2
    canvas.paste(image, (x, y))
    return canvas


def make_contact_sheet(paths: list[Path], labels: list[str], output: Path) -> None:
    columns = 4
    thumb_w, thumb_h = 450, 193
    gutter, label_h, margin, title_h = 20, 42, 30, 72
    rows = (len(paths) + columns - 1) // columns
    canvas_w = margin * 2 + columns * thumb_w + (columns - 1) * gutter
    canvas_h = title_h + margin + rows * (thumb_h + label_h + gutter)
    canvas = Image.new("RGB", (canvas_w, canvas_h), (31, 36, 36))
    draw = ImageDraw.Draw(canvas)
    title_font = font(34)
    label_font = font(24)
    draw.text((margin, 20), "ALL CAME — 120s / 38 SHOTS / 42 KEYFRAMES", fill=(228, 214, 173), font=title_font)
    for index, (path, label) in enumerate(zip(paths, labels)):
        row, column = divmod(index, columns)
        x = margin + column * (thumb_w + gutter)
        y = title_h + margin + row * (thumb_h + label_h + gutter)
        canvas.paste(fit_image(path, thumb_w, thumb_h), (x, y))
        draw.rectangle((x, y, x + thumb_w - 1, y + thumb_h - 1), outline=(117, 106, 83), width=2)
        draw.text((x, y + thumb_h + 8), label, fill=(235, 231, 216), font=label_font)
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output, format="PNG", optimize=True)


def make_numbered_sheet(selected: Path, shot_id: str, item_ids: list[str], output: Path) -> None:
    columns = len(item_ids)
    margin, gutter, title_h, label_h = 24, 18, 60, 44
    canvas_w = 1920
    cell_w = (canvas_w - margin * 2 - gutter * (columns - 1)) // columns
    cell_h = round(cell_w * 821 / 1915)
    canvas_h = title_h + cell_h + label_h + margin
    canvas = Image.new("RGB", (canvas_w, canvas_h), (28, 33, 34))
    draw = ImageDraw.Draw(canvas)
    draw.text((margin, 14), f"{shot_id} — NUMBERED KEYFRAME SEQUENCE", fill=(228, 214, 173), font=font(30))
    for index, item_id in enumerate(item_ids):
        x = margin + index * (cell_w + gutter)
        y = title_h
        canvas.paste(fit_image(selected / f"{item_id}.png", cell_w, cell_h), (x, y))
        draw.rectangle((x, y, x + cell_w - 1, y + cell_h - 1), outline=(117, 106, 83), width=2)
        draw.text((x, y + cell_h + 7), f"{index + 1:02d}  {item_id}", fill=(235, 231, 216), font=font(22))
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output, format="PNG", optimize=True)


def validate_images(selected: Path, items: list[str]) -> list[dict]:
    expected_names = {f"{item}.png" for item in items}
    actual_names = {path.name for path in selected.glob("*.png")}
    if expected_names != actual_names:
        missing = sorted(expected_names - actual_names)
        extra = sorted(actual_names - expected_names)
        raise ValueError(f"selected set mismatch; missing={missing}, extra={extra}")
    records = []
    for item in items:
        path = selected / f"{item}.png"
        with Image.open(path) as image:
            image.verify()
        with Image.open(path) as image:
            size = list(image.size)
            mode = image.mode
            image_format = image.format
        if size != [1915, 821]:
            raise ValueError(f"{item}: expected 1915x821, got {size}")
        if image_format != "PNG":
            raise ValueError(f"{item}: expected PNG, got {image_format}")
        records.append({
            "item_id": item,
            "path": f"images/{item}.png",
            "width": size[0],
            "height": size[1],
            "mode": mode,
            "format": image_format,
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
            "integrity": "pass",
        })
    return records


def require_qa(project: Path, item_count: int) -> dict:
    qa_dir = project / "08_generation/jobs/final_frames_v2/qa"
    surface_path = qa_dir / "final_image_quality_qa.json"
    semantic_path = qa_dir / "final_semantic_qa.json"
    if not surface_path.is_file() or not semantic_path.is_file():
        raise ValueError("final surface and semantic QA reports must exist before packaging")
    surface = json.loads(surface_path.read_text(encoding="utf-8"))
    semantic = json.loads(semantic_path.read_text(encoding="utf-8"))
    if surface.get("count") != item_count or surface.get("counts", {}).get("fail") != 0:
        raise ValueError("surface QA is incomplete or contains failures")
    semantic_rows = semantic.get("records", [])
    if len(semantic_rows) != item_count or any(row.get("status") != "pass" for row in semantic_rows):
        raise ValueError("semantic QA is incomplete or contains non-pass rows")
    return {
        "surface_report": "qa/final_image_quality_qa.json",
        "semantic_report": "qa/final_semantic_qa.json",
    }


def make_readme(delivery: Path, manifest: dict) -> Path:
    path = delivery / "README.md"
    text = f"""# 《所有人都来了》2分钟完整生产包

- 活动分支：`DFT_MASTERPLAN_WILD_RETURN_V4`
- 成片覆盖：`00:00–02:00`，38 个剪辑镜头，42 张关键帧
- 画幅：21:9，全部 1915×821 PNG
- 图像状态：生产选择候选；导演逐张批准状态仍为 pending
- 音乐方向：Oasis《The Masterplan》由后期剪辑加入；包内不含版权音乐，也不把音乐嵌入 AIGC 视频提示

## 包内结构

- `images/`：42 张按时间顺序命名的关键帧
- `prompts/`：三段逐镜图像提示词、图生视频提示词及结构化 idea board
- `storyboards/`：SH28、SH35、SH38 编号多锚点联系板与全片总联系表
- `qa/`：尺寸／文件完整性、低噪表面检查、逐镜语义硬质检
- `story_and_ledgers/`：120 秒故事、镜头覆盖、角色状态、尺度与群像动作账本

## 关键门禁

1. 建筑、门窗、家具与动物必须保持可信尺度；无明确例外时禁止玩具房屋或动物大过建筑。
2. 群像必须是多物种，动作动词、相位、朝向、眼线和手位不得复制。
3. 仅 SH35 允许从无衣两足到自然四足的非恐怖、错峰连续转换；SH36–SH38 全程无衣四足。
4. 每条视频时间线同时说明表演与摄影；所有视频严格继承输入关键帧的 DFT 旧纸蛋彩／哑光水粉语言。

完整哈希与逐帧状态见 `manifest.json`。ZIP 哈希写在交付目录外层的 `PACKAGE_SHA256.txt`。
"""
    path.write_text(text, encoding="utf-8")
    return path


def run_project_script(project: Path, name: str, extra: list[str] | None = None) -> None:
    command = [sys.executable, str(project / "scripts" / name)]
    if extra:
        command.extend(extra)
    result = subprocess.run(command, check=False, capture_output=True, text=True)
    if result.returncode:
        raise ValueError(f"{name} failed:\n{result.stdout}\n{result.stderr}")


def write_zip(project: Path, delivery: Path, items: list[str], manifest_path: Path, readme_path: Path) -> Path:
    zip_path = delivery / "ALL_CAME_2MIN_COMPLETE_V2.zip"
    selected = project / "08_generation/jobs/final_frames_v2/selected"
    storyboard_dir = project / "08_generation/jobs/final_frames_v2/storyboard_sheets"
    qa_dir = project / "08_generation/jobs/final_frames_v2/qa"
    sources = [
        (readme_path, "README.md"),
        (manifest_path, "manifest.json"),
        (project / "03_story/idea_board/idea_board.json", "prompts/idea_board.json"),
        (project / "07_shots/prompt_packages_v2/SH01_SH13_PRODUCTION_PROMPTS.md", "prompts/SH01_SH13_PRODUCTION_PROMPTS.md"),
        (project / "07_shots/prompt_packages_v2/SH14_SH26_PRODUCTION_PROMPTS.md", "prompts/SH14_SH26_PRODUCTION_PROMPTS.md"),
        (project / "07_shots/prompt_packages_v2/SH27_SH38_PRODUCTION_PROMPTS.md", "prompts/SH27_SH38_PRODUCTION_PROMPTS.md"),
        (project / "03_story/STORY_V2_MASTERPLAN_WILD_RETURN.md", "story_and_ledgers/STORY_V2_MASTERPLAN_WILD_RETURN.md"),
        (project / "07_shots/SHOT_COVERAGE_120S_V2.md", "story_and_ledgers/SHOT_COVERAGE_120S_V2.md"),
        (project / "05_asset_bible/CHARACTER_STATE_LEDGER_V2.json", "story_and_ledgers/CHARACTER_STATE_LEDGER_V2.json"),
        (project / "05_asset_bible/SCALE_LEDGER_V1.md", "story_and_ledgers/SCALE_LEDGER_V1.md"),
        (project / "07_shots/GROUP_ACTION_LEDGER_120S_V2.md", "story_and_ledgers/GROUP_ACTION_LEDGER_120S_V2.md"),
        (qa_dir / "dimension_and_integrity_qa.json", "qa/dimension_and_integrity_qa.json"),
        (qa_dir / "final_image_quality_qa.json", "qa/final_image_quality_qa.json"),
        (qa_dir / "final_semantic_qa.json", "qa/final_semantic_qa.json"),
        (qa_dir / "batch_SH01_SH13_semantic.json", "qa/batch_SH01_SH13_semantic.json"),
        (qa_dir / "batch_SH14_SH26_semantic.json", "qa/batch_SH14_SH26_semantic.json"),
        (qa_dir / "batch_SH27_SH38_semantic.json", "qa/batch_SH27_SH38_semantic.json"),
        (project / "10_qa/runtime_coverage_qa.json", "qa/runtime_coverage_qa.json"),
        (project / "10_qa/prompt_contract_qa.json", "qa/prompt_contract_qa.json"),
        (project / "10_qa/narrative_state_contract_qa.json", "qa/narrative_state_contract_qa.json"),
        (project / "10_qa/FINAL_42_CONTACT_SHEET_REVIEW.md", "qa/FINAL_42_CONTACT_SHEET_REVIEW.md"),
        (project / "10_qa/loops/LOOP_LEDGER.md", "qa/loops/LOOP_LEDGER.md"),
        (project / "10_qa/loops/loop_config.yaml", "qa/loops/loop_config.yaml"),
        (project / "10_qa/loops/rubrics/image_keyframe_rubric.yaml", "qa/loops/image_keyframe_rubric.yaml"),
        (project / "10_qa/loops/rubrics/video_prompt_rubric.yaml", "qa/loops/video_prompt_rubric.yaml"),
        (project / "10_qa/loops/rubrics/video_output_rubric.yaml", "qa/loops/video_output_rubric.yaml"),
        (project / "10_qa/loops/rubrics/delivery_rubric.yaml", "qa/loops/delivery_rubric.yaml"),
        (project / "10_qa/loops/failure_library/negative_examples/INDEX.md", "qa/loops/failure_library/negative_examples/INDEX.md"),
        (storyboard_dir / "ALL_42_CHRONOLOGICAL_CONTACT_SHEET.png", "storyboards/ALL_42_CHRONOLOGICAL_CONTACT_SHEET.png"),
        (storyboard_dir / "SH28_NUMBERED_SHEET.png", "storyboards/SH28_NUMBERED_SHEET.png"),
        (storyboard_dir / "SH35_NUMBERED_SHEET.png", "storyboards/SH35_NUMBERED_SHEET.png"),
        (storyboard_dir / "SH38_NUMBERED_SHEET.png", "storyboards/SH38_NUMBERED_SHEET.png"),
    ]
    sources.extend((selected / f"{item}.png", f"images/{item}.png") for item in items)
    for source, _ in sources:
        if not source.is_file():
            raise ValueError(f"delivery source missing: {source}")
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for source, arcname in sources:
            archive.write(source, arcname)
    return zip_path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=str(Path(__file__).resolve().parents[1]))
    args = parser.parse_args()
    project = Path(args.project_root).expanduser().resolve()
    selected = project / "08_generation/jobs/final_frames_v2/selected"
    storyboard_dir = project / "08_generation/jobs/final_frames_v2/storyboard_sheets"
    qa_dir = project / "08_generation/jobs/final_frames_v2/qa"
    delivery = project / "11_delivery/all_came_last_show_v2"
    delivery.mkdir(parents=True, exist_ok=True)
    items = expected_items()
    records = validate_images(selected, items)
    qa_sources = require_qa(project, len(items))

    make_numbered_sheet(selected, "SH28", ["SH28_KF01", "SH28_KF02"], storyboard_dir / "SH28_NUMBERED_SHEET.png")
    make_numbered_sheet(selected, "SH35", ["SH35_KF01", "SH35_KF02", "SH35_KF03"], storyboard_dir / "SH35_NUMBERED_SHEET.png")
    make_numbered_sheet(selected, "SH38", ["SH38_KF01", "SH38_KF02"], storyboard_dir / "SH38_NUMBERED_SHEET.png")
    paths = [selected / f"{item}.png" for item in items]
    make_contact_sheet(paths, items, storyboard_dir / "ALL_42_CHRONOLOGICAL_CONTACT_SHEET.png")

    run_project_script(project, "build_idea_board.py")
    run_project_script(project, "validate_runtime_coverage.py", ["--require-images"])
    run_project_script(project, "run_contract_qa.py")

    board_path = project / "03_story/idea_board/idea_board.json"
    board = json.loads(board_path.read_text(encoding="utf-8"))
    if [row.get("item_id") for row in board.get("rows", [])] != items:
        raise ValueError("idea board row order does not match the 42-frame delivery")
    manifest = {
        "schema_version": "2.0",
        "project": "all-came-last-show",
        "active_branch": "DFT_MASTERPLAN_WILD_RETURN_V4",
        "runtime_seconds": 120,
        "shot_count": 38,
        "keyframe_count": 42,
        "frame_spec": {"aspect_ratio": "21:9", "width": 1915, "height": 821, "format": "PNG"},
        "director_approval_status": "pending",
        "qa": qa_sources,
        "images": records,
    }
    manifest_path = delivery / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    qa_dir.mkdir(parents=True, exist_ok=True)
    (qa_dir / "dimension_and_integrity_qa.json").write_text(
        json.dumps({"ok": True, "count": len(records), "records": records}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    readme_path = make_readme(delivery, manifest)
    zip_path = write_zip(project, delivery, items, manifest_path, readme_path)
    checksum_path = delivery / "PACKAGE_SHA256.txt"
    checksum_path.write_text(f"{sha256(zip_path)}  {zip_path.name}\n", encoding="utf-8")
    print(json.dumps({
        "ok": True,
        "images": len(records),
        "contact_sheet": str(storyboard_dir / "ALL_42_CHRONOLOGICAL_CONTACT_SHEET.png"),
        "zip": str(zip_path),
        "zip_sha256": sha256(zip_path),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
