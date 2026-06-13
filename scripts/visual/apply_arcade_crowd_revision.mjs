import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const SCRIPT_DIR = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(SCRIPT_DIR, "..");
const PROJECT_ROOT = path.resolve(ROOT, "..");

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
  if (rows.length && rows[0][0]?.charCodeAt(0) === 0xfeff) {
    rows[0][0] = rows[0][0].slice(1);
  }
  return rows;
}

function csvEscape(value) {
  const s = String(value ?? "");
  if (/[",\n\r]/.test(s)) return `"${s.replace(/"/g, "\"\"")}"`;
  return s;
}

function writeCSV(file, rows, bom) {
  const text = rows.map((row) => row.map(csvEscape).join(",")).join("\n") + "\n";
  fs.writeFileSync(file, `${bom ? "\ufeff" : ""}${text}`, "utf8");
}

function indexHeader(header) {
  return Object.fromEntries(header.map((name, index) => [name, index]));
}

function updateCSV(relPath, updater) {
  const file = path.join(PROJECT_ROOT, relPath);
  const raw = fs.readFileSync(file, "utf8");
  const hadBom = raw.charCodeAt(0) === 0xfeff;
  const rows = parseCSV(raw);
  const idx = indexHeader(rows[0]);
  let changed = 0;
  for (const row of rows.slice(1)) {
    if (updater(row, idx)) changed += 1;
  }
  if (changed) writeCSV(file, rows, hadBom);
  return `${relPath}: ${changed}`;
}

const arcadePanels = new Set();
const mapRows = parseCSV(fs.readFileSync(
  path.join(ROOT, "environment_lookdev/SCN_ARCADE/camera_whiteboxes_v001/SCN_ARCADE_panel_camera_constraint_map_v001.csv"),
  "utf8",
));
const mapIdx = indexHeader(mapRows[0]);
for (const row of mapRows.slice(1)) {
  if (row[mapIdx.panel_id]) arcadePanels.add(row[mapIdx.panel_id]);
}

const revisedPanels = new Set(["MSB019", "MSB020", "MSB021"]);
const crowdLock = "Crowd-density lock: the hidden arcade must feel very crowded and smoky, with shoulder-to-shoulder local kids, teenagers, and older bystanders packed around machines, silhouettes overlapping the aisle, cigarette-smoke haze, humid fog, and layered background faces; never make the arcade feel empty or spacious.";
const crowdNegative = "empty arcade, sparse people, clean open aisle, showroom-like room, only three people in the whole arcade, clear fresh air, smoke-free room";

const results = [];

results.push(updateCSV("01_AIGC/environment_lookdev/SCN_ARCADE/camera_whiteboxes_v001/SCN_ARCADE_formal_storyboard_prompt_pack_v001.csv", (row, idx) => {
  if (!arcadePanels.has(row[idx.panel_id])) return false;
  if (!row[idx.pure_prompt].includes("Crowd-density lock:")) {
    row[idx.pure_prompt] = `${row[idx.pure_prompt]} ${crowdLock}`;
  }
  if (!row[idx.negative_prompt].includes("empty arcade")) {
    row[idx.negative_prompt] = `${row[idx.negative_prompt]}, ${crowdNegative}`;
  }
  return true;
}));

results.push(updateCSV("01_AIGC/exports/micro_storyboard_pure_image_prompts.csv", (row, idx) => {
  if (!arcadePanels.has(row[idx.panel_id])) return false;
  if (revisedPanels.has(row[idx.panel_id])) {
    row[idx.pure_path] = row[idx.pure_path].replace("_v001.png", "_v002.png");
    row[idx.annotated_path] = row[idx.annotated_path].replace("_v001_annotated.png", "_v002_annotated.png");
  }
  if (!row[idx.pure_prompt].includes("Crowd-density lock:")) {
    row[idx.pure_prompt] = `${row[idx.pure_prompt]} ${crowdLock}`;
  }
  if (!row[idx.negative_prompt].includes("empty arcade")) {
    row[idx.negative_prompt] = `${row[idx.negative_prompt]}, ${crowdNegative}`;
  }
  return true;
}));

results.push(updateCSV("01_AIGC/exports/real_image_generation_queue.csv", (row, idx) => {
  if (!arcadePanels.has(row[idx.panel_id])) return false;
  if (revisedPanels.has(row[idx.panel_id])) {
    row[idx.pure_path] = row[idx.pure_path].replace("_v001.png", "_v002.png");
    row[idx.annotated_path] = row[idx.annotated_path].replace("_v001_annotated.png", "_v002_annotated.png");
    row[idx.status] = "queued";
  }
  const note = "crowd_density_revision=very_crowded_smoky; sparse v001 rejected for MSB019-MSB021";
  if (!row[idx.notes].includes("crowd_density_revision=very_crowded_smoky")) {
    row[idx.notes] = `${row[idx.notes]} | ${note}`;
  }
  return true;
}));

results.push(updateCSV("01_AIGC/exports/visual_asset_dual_version_plan.csv", (row, idx) => {
  if (!arcadePanels.has(row[idx.asset_id])) return false;
  if (revisedPanels.has(row[idx.asset_id])) {
    row[idx.pure_path] = row[idx.pure_path].replace("_v001.png", "_v002.png");
    row[idx.annotated_path] = row[idx.annotated_path].replace("_v001_annotated.png", "_v002_annotated.png");
    row[idx.status] = "planned";
  }
  return true;
}));

results.push(updateCSV("01_AIGC/exports/visual_asset_qa_checklist.csv", (row, idx) => {
  if (!revisedPanels.has(row[idx.asset_id])) return false;
  row[idx.pure_path] = row[idx.pure_path].replace("_v001.png", "_v002.png");
  row[idx.annotated_path] = row[idx.annotated_path].replace("_v001_annotated.png", "_v002_annotated.png");
  row[idx.pure_exists] = "pending";
  row[idx.no_text_or_labels] = "pending";
  row[idx.identity_ok] = "pending";
  row[idx.space_ok] = "pending";
  row[idx.lighting_ok] = "pending";
  row[idx.whitebox_ok] = "pending";
  row[idx.overall_status] = "planned";
  row[idx.issue_summary] = "v001 sparse arcade rejected; regenerate with very crowded smoky arcade density";
  row[idx.replacement_needed] = "yes";
  row[idx.replacement_path] = row[idx.pure_path];
  return true;
}));

console.log(results.join("\n"));
