import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const SCRIPT_DIR = path.dirname(fileURLToPath(import.meta.url));
const PROJECT_ROOT = path.resolve(SCRIPT_DIR, "../..");
const REJECTED = new Set(["MSB020", "MSB021"]);

function parseCSV(text) {
  const rows = [];
  let row = [];
  let field = "";
  let inQuotes = false;
  for (let i = 0; i < text.length; i += 1) {
    const ch = text[i];
    if (inQuotes) {
      if (ch === "\"") {
        if (text[i + 1] === "\"") {
          field += "\"";
          i += 1;
        } else {
          inQuotes = false;
        }
      } else {
        field += ch;
      }
    } else if (ch === "\"") {
      inQuotes = true;
    } else if (ch === ",") {
      row.push(field);
      field = "";
    } else if (ch === "\n") {
      row.push(field);
      rows.push(row);
      row = [];
      field = "";
    } else if (ch !== "\r") {
      field += ch;
    }
  }
  if (field.length || row.length) {
    row.push(field);
    rows.push(row);
  }
  if (rows.length && rows[0][0]?.charCodeAt(0) === 0xfeff) rows[0][0] = rows[0][0].slice(1);
  return rows;
}

function csvEscape(value) {
  const s = String(value ?? "");
  return /[",\n\r]/.test(s) ? `"${s.replace(/"/g, "\"\"")}"` : s;
}

function writeCSV(file, rows, bom) {
  fs.writeFileSync(file, `${bom ? "\ufeff" : ""}${rows.map((row) => row.map(csvEscape).join(",")).join("\n")}\n`, "utf8");
}

function headerIndex(header) {
  return Object.fromEntries(header.map((name, index) => [name, index]));
}

function toV003(value) {
  return value.replace("_v002.png", "_v003.png").replace("_v002_annotated.png", "_v003_annotated.png");
}

function update(rel, updater) {
  const file = path.join(PROJECT_ROOT, rel);
  const raw = fs.readFileSync(file, "utf8");
  const bom = raw.charCodeAt(0) === 0xfeff;
  const rows = parseCSV(raw);
  const idx = headerIndex(rows[0]);
  let changed = 0;
  for (const row of rows.slice(1)) {
    if (updater(row, idx)) changed += 1;
  }
  if (changed) writeCSV(file, rows, bom);
  console.log(`${rel}: ${changed}`);
}

update("01_AIGC/exports/real_image_generation_queue.csv", (row, idx) => {
  if (!REJECTED.has(row[idx.panel_id])) return false;
  row[idx.pure_path] = toV003(row[idx.pure_path]);
  row[idx.annotated_path] = toV003(row[idx.annotated_path]);
  row[idx.status] = "queued";
  const note = "v002 rejected: wrong_camera_subject_relation; regenerate v003 as rear_follow, backs/three-quarter backs to camera, gaze into crowded arcade";
  if (!row[idx.notes].includes("wrong_camera_subject_relation")) row[idx.notes] = `${row[idx.notes]} | ${note}`;
  return true;
});

update("01_AIGC/exports/visual_asset_dual_version_plan.csv", (row, idx) => {
  if (!REJECTED.has(row[idx.asset_id])) return false;
  row[idx.pure_path] = toV003(row[idx.pure_path]);
  row[idx.annotated_path] = toV003(row[idx.annotated_path]);
  row[idx.status] = "planned";
  return true;
});

update("01_AIGC/exports/visual_asset_qa_checklist.csv", (row, idx) => {
  if (!REJECTED.has(row[idx.asset_id])) return false;
  row[idx.pure_path] = toV003(row[idx.pure_path]);
  row[idx.annotated_path] = toV003(row[idx.annotated_path]);
  row[idx.pure_exists] = "pending";
  row[idx.no_text_or_labels] = "pending";
  row[idx.identity_ok] = "pending";
  row[idx.space_ok] = "pending";
  row[idx.lighting_ok] = "pending";
  row[idx.whitebox_ok] = "pending";
  row[idx.overall_status] = "planned";
  row[idx.issue_summary] = "v002 rejected: wrong_camera_subject_relation; rear-follow entrance shot must show backs/three-quarter backs and gaze into crowded arcade";
  row[idx.root_cause] = "character-sheet/front-facing bias in storyboard prompt";
  row[idx.replacement_needed] = "yes";
  row[idx.replacement_path] = row[idx.pure_path];
  return true;
});

update("01_AIGC/exports/micro_storyboard_pure_image_prompts.csv", (row, idx) => {
  if (!REJECTED.has(row[idx.panel_id])) return false;
  row[idx.pure_path] = toV003(row[idx.pure_path]);
  row[idx.annotated_path] = toV003(row[idx.annotated_path]);
  const logic = " Camera-subject logic lock: camera_subject_relation=rear_follow; character_facing=backs to camera or three-quarter back; gaze_target=crowded arcade interior and CRT cabinets; camera_motivation=follows the brothers entering the space; characters must not look at camera or pose front-facing.";
  if (!row[idx.pure_prompt].includes("camera_subject_relation=rear_follow")) row[idx.pure_prompt] += logic;
  if (!row[idx.negative_prompt].includes("front-facing portrait")) {
    row[idx.negative_prompt] += ", front-facing portrait, posing for camera, looking at camera, character sheet, staged lineup, all faces toward viewer";
  }
  return true;
});
