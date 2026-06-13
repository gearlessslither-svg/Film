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
  if (/[",\n\r]/.test(s)) {
    return `"${s.replace(/"/g, "\"\"")}"`;
  }
  return s;
}

function writeCSV(file, rows, bom) {
  const text = rows.map((row) => row.map(csvEscape).join(",")).join("\n") + "\n";
  fs.writeFileSync(file, `${bom ? "\ufeff" : ""}${text}`, "utf8");
}

function indexHeader(header) {
  return Object.fromEntries(header.map((name, index) => [name, index]));
}

const mapFile = path.join(
  ROOT,
  "environment_lookdev/SCN_ARCADE/camera_whiteboxes_v001/SCN_ARCADE_panel_camera_constraint_map_v001.csv",
);
const promptPack = "environment_lookdev/SCN_ARCADE/camera_whiteboxes_v001/SCN_ARCADE_formal_storyboard_prompt_pack_v001.csv";
const mother = "environment_lookdev/SCN_ARCADE/SCN_ARCADE_lookdev_A_entrance_wide_v002_game_screens.png";
const mapRows = parseCSV(fs.readFileSync(mapFile, "utf8"));
const mapIdx = indexHeader(mapRows[0]);
const byPanel = new Map();

for (const row of mapRows.slice(1)) {
  const panel = row[mapIdx.panel_id];
  if (!panel) continue;
  byPanel.set(panel, {
    constraint: row[mapIdx.constraint_whitebox_path],
    camera: row[mapIdx.selected_constraint_camera],
  });
}

function updateFile(relPath, updater) {
  const file = path.join(PROJECT_ROOT, relPath);
  const raw = fs.readFileSync(file, "utf8");
  const hadBom = raw.charCodeAt(0) === 0xfeff;
  const rows = parseCSV(raw);
  const idx = indexHeader(rows[0]);
  let changed = 0;

  for (const row of rows.slice(1)) {
    const panel = row[idx.panel_id] ?? row[idx.asset_id];
    const mapping = byPanel.get(panel);
    if (!mapping) continue;
    if (updater(row, idx, mapping)) changed += 1;
  }

  if (changed) writeCSV(file, rows, hadBom);
  return `${relPath}: ${changed}`;
}

const results = [];

results.push(updateFile("01_AIGC/exports/real_image_generation_queue.csv", (row, idx, mapping) => {
  const old = row[idx.whitebox_reference_path];
  row[idx.whitebox_reference_path] = mapping.constraint;
  const add = `SCN_ARCADE mother_style=${mother}; constraint_camera=${mapping.camera}`;
  if (idx.notes !== undefined && !row[idx.notes].includes("SCN_ARCADE mother_style=")) {
    row[idx.notes] = `${row[idx.notes]} | ${add}`;
  }
  return old !== mapping.constraint;
}));

results.push(updateFile("01_AIGC/exports/visual_asset_dual_version_plan.csv", (row, idx, mapping) => {
  const old = row[idx.whitebox_reference_path];
  row[idx.whitebox_reference_path] = mapping.constraint;
  if (idx.prompt_source !== undefined) row[idx.prompt_source] = promptPack;
  return old !== mapping.constraint;
}));

results.push(updateFile("01_AIGC/exports/micro_storyboard_pure_image_prompts.csv", (row, idx, mapping) => {
  const old = row[idx.whitebox_reference_path];
  row[idx.whitebox_reference_path] = mapping.constraint;
  const existingPrompt = row[idx.pure_prompt] ?? "";
  const arcadeNote = `SCN_ARCADE formal generation uses mother style reference ${mother} and constraint camera ${mapping.camera}.`;
  const replacedPrompt = existingPrompt.replace(/whitebox_renders_v2\/[^,"\s]+/g, mapping.constraint);
  row[idx.pure_prompt] = replacedPrompt.includes("SCN_ARCADE formal generation uses mother style reference")
    ? replacedPrompt
    : `${replacedPrompt} ${arcadeNote}`;
  return old !== mapping.constraint;
}));

console.log(results.join("\n"));
