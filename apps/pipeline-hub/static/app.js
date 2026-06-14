const state = {
  projects: [],
  selectedSlug: null,
  detail: null,
  busy: false,
  selectedDocIndex: 0,
  selectedSceneLockIndex: 0,
  selectedSceneId: "",
  selectedFrameRef: "",
  storyboardStage: "all",
  referenceSelection: {},
  boardOpen: false,
  boardNodes: [],
  boardEdges: [],
  boardLinkSourceId: "",
  boardFilters: {
    scene: "all",
    tag: "all",
    query: "",
  },
  boardGeneration: {
    nodeId: "",
    progress: 0,
    message: "",
  },
  sceneFilters: {
    step: "all",
    kind: "all",
    decision: "all",
    query: "",
  },
  recreate: null,
  activeChangeRequest: null,
  filters: {
    stage: "all",
    kind: "all",
    decision: "all",
    query: "",
  },
};

const STAGE_LABELS = {
  "00_admin": "项目控制、导演意图、模型配置、日志 / Admin, brief, model config, log",
  "01_intake": "输入归档、参考素材、AI 分析 / Intake, references, AI analysis",
  "02_direction": "创意方向、方案、确认记录 / Direction, options, approvals",
  "03_story": "大纲、剧本、节拍、台词 / Outline, script, beats, dialogue",
  "04_lookdev": "风格帧、色彩、光照、美术参考 / Lookdev, color, lighting, art refs",
  "05_asset_bible": "角色、场景、道具、连续性锁 / Character, scene, prop, continuity locks",
  "06_previs": "白模、机位、控制层、空间 QA / Whitebox, camera, control, spatial QA",
  "07_shots": "镜头表、关键帧、图片/视频提示词 / Shot list, keyframes, image/video prompts",
  "08_generation": "生成任务、图片/视频输出、废片记录 / Generation tasks, outputs, rejects",
  "09_edit": "粗剪、声音、字幕、调色 / Rough cut, sound, subtitles, color",
  "10_qa": "QA 报告、修复队列、审片记录 / QA reports, fix queue, review notes",
  "11_delivery": "最终导出、交付包、交付清单 / Final export, delivery package, checklist",
};

const EXTRA_STAGE_LABELS = {
  resources: "外部资源 / External resources",
  other: "其他 / Other",
};

const SCENE_STATUS_LABELS = {
  draft: "草稿 / Draft",
  in_progress: "制作中 / In progress",
  needs_changes: "需修改 / Needs changes",
  impact_ready: "影响表待确认 / Impact ready",
  generation_queued: "生成队列中 / Generation queued",
  generation_failed: "生成失败 / Generation failed",
  review_ready: "待审片 / Review ready",
  approved: "已通过 / Approved",
};

const IMPACT_ACTION_LABELS = {
  create: "新增 / Create",
  modify: "修改 / Modify",
  check: "检查 / Check",
};

const KIND_LABELS = {
  script: "剧本/文档 / Script or document",
  shot_prompt: "分镜提示词 / Shot prompt",
  video_prompt: "视频提示词 / Video prompt",
  whitebox: "白模/预演 / Whitebox or previs",
  storyboard_keyframe: "分镜关键帧 / Storyboard keyframe",
  scene_lock: "场景锁 / Scene lock",
  character_ref: "角色参考 / Character reference",
  scene_ref: "场景参考 / Scene reference",
  lookdev: "风格/Lookdev / Look development",
  audio: "音频 / Audio",
  video: "视频 / Video",
  three_d: "3D / 3D asset",
  image: "图片 / Image",
  document: "文档 / Document",
  other: "其他 / Other",
};

const RESOURCE_RENDER_LIMIT = 80;
const TEXT_PREVIEW_EXTENSIONS = /\.(md|txt|csv|json|ya?ml|srt)$/i;
const VIDEO_PREVIEW_EXTENSIONS = /\.(mp4|webm)$/i;
const AUDIO_PREVIEW_EXTENSIONS = /\.(mp3|wav|ogg)$/i;
const QA_REPAIR_INTENTS = {
  denoise: {
    label: "降噪 / Denoise",
    directive: "Repair target: remove visible grain, sensor noise, speckles, dirty texture, and compression artifacts. Keep clean surfaces and stable material detail.",
  },
  sharpen: {
    label: "提高清晰 / Sharpen",
    directive: "Repair target: increase edge clarity, crisp subject silhouette, facial/detail readability, and high-resolution focal sharpness without oversharpen halos.",
  },
  relight: {
    label: "提亮暗部 / Relight",
    directive: "Repair target: brighten muddy shadows with controlled soft lighting, preserve mood, and keep the scene readable without flattening the image.",
  },
  highlights: {
    label: "压高光 / Highlights",
    directive: "Repair target: recover blown highlights, balance bright areas, and keep luminous objects controlled without clipping.",
  },
  contrast: {
    label: "增强对比 / Contrast",
    directive: "Repair target: improve clean value separation, readable silhouette, foreground/background layering, and cinematic depth.",
  },
  palette: {
    label: "收敛色彩 / Palette",
    directive: "Repair target: reduce oversaturation, keep natural material colors, and maintain a restrained cinematic palette.",
  },
};
const BOARD_TAG_OPTIONS = [
  { value: "all", label: "全部图片 / All images" },
  { value: "character", label: "人物 / Character" },
  { value: "scene", label: "场景 / Scene" },
  { value: "whitebox", label: "白模 / Whitebox" },
  { value: "keyframe", label: "关键帧 / Keyframe" },
  { value: "lookdev", label: "风格 / Lookdev" },
  { value: "marked_use", label: "✅ 已选 / Marked use" },
  { value: "marked_reject", label: "× 不用 / Rejected" },
  { value: "unmarked", label: "未标注 / Unmarked" },
];

const $ = (id) => document.getElementById(id);
const NATURAL_COLLATOR = new Intl.Collator(["zh-Hans-CN", "en"], { numeric: true, sensitivity: "base" });

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function naturalCompare(a, b) {
  return NATURAL_COLLATOR.compare(String(a ?? ""), String(b ?? ""));
}

function toast(message) {
  const node = $("toast");
  node.textContent = message;
  node.classList.add("show");
  clearTimeout(node._timer);
  node._timer = setTimeout(() => node.classList.remove("show"), 2800);
}

async function requestJson(url, options = {}) {
  const response = await fetch(url, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  const text = await response.text();
  let payload = {};
  try {
    payload = text ? JSON.parse(text) : {};
  } catch (error) {
    payload = { raw: text };
  }
  if (!response.ok) {
    throw new Error(payload.error || response.statusText);
  }
  return payload;
}

function projectLabel(project) {
  const readiness = project.readiness == null ? "-" : `${project.readiness}%`;
  return `${project.slug} · 准备度/Readiness ${readiness} · P0 ${project.p0_count ?? 0}`;
}

function renderProjects() {
  const root = $("projectList");
  if (!state.projects.length) {
    root.innerHTML = `<div class="empty-state">还没有项目。先创建一个项目。/ No projects yet. Create one first.</div>`;
    return;
  }
  root.innerHTML = state.projects
    .map(
      (project) => `
        <button class="project-item ${project.slug === state.selectedSlug ? "active" : ""}" data-slug="${escapeHtml(project.slug)}" type="button">
          <strong>${escapeHtml(project.name)}</strong>
          <span>${escapeHtml(projectLabel(project))}</span>
        </button>
      `,
    )
    .join("");
  root.querySelectorAll(".project-item").forEach((button) => {
    button.addEventListener("click", () => selectProject(button.dataset.slug));
  });
}

function renderSidebarSceneNavigator() {
  const root = $("sidebarSceneNavigator");
  if (!root) return;
  const scenes = state.detail?.scene_workbench?.scenes || [];
  if (!state.detail || !scenes.length) {
    root.innerHTML = "";
    return;
  }
  const scene = selectedScene();
  const grouped = new Map();
  scenes.forEach((item) => {
    const key = `${item.act_id || "ACT"}|${item.act_title || "未分幕 / No act"}`;
    if (!grouped.has(key)) grouped.set(key, []);
    grouped.get(key).push(item);
  });
  root.innerHTML = `
    <section class="sidebar-scene-panel">
      <div class="sidebar-scene-header">
        <span>场戏 / Scenes</span>
        <small>${scenes.length}</small>
      </div>
      ${[...grouped.entries()]
        .map(([key, actScenes]) => {
          const [, actTitle] = key.split("|");
          return `
            <section class="sidebar-act">
              <strong>${escapeHtml(actTitle)}</strong>
              ${actScenes
                .map(
                  (item) => `
                    <button class="sidebar-scene-button ${item.scene_id === scene?.scene_id ? "active" : ""}" data-scene-id="${escapeHtml(item.scene_id)}" type="button">
                      <span>${escapeHtml(item.title || item.scene_id)}</span>
                      <small>${escapeHtml(item.scene_id)} · ${(item.shot_ids || []).length} 镜头 · ${escapeHtml(sceneStatusLabel(item.status))}</small>
                    </button>
                  `,
                )
                .join("")}
            </section>
          `;
        })
        .join("")}
    </section>
  `;
  root.querySelectorAll(".sidebar-scene-button").forEach((button) => {
    button.addEventListener("click", () => {
      state.selectedSceneId = button.dataset.sceneId || "";
      state.selectedFrameRef = "";
      state.activeChangeRequest = null;
      state.recreate = null;
      renderAll();
    });
  });
}

function pill(label, kind = "") {
  return `<span class="pill ${kind}">${escapeHtml(label)}</span>`;
}

function statusLabel(status) {
  const labels = {
    pass: "通过 / Pass",
    warn: "警告 / Warn",
    fail: "失败 / Fail",
    missing: "缺失 / Missing",
    needs_work: "需处理 / Needs work",
    ready_for_director_review: "待导演复核 / Ready for director review",
    done: "完成 / Done",
    unscanned: "未扫描 / Unscanned",
  };
  return labels[status] || status || "未知 / Unknown";
}

function renderHeader() {
  const detail = state.detail;
  if (!detail) {
    $("projectTitle").textContent = "未选择项目 / No project selected";
    $("projectPath").textContent = "";
    $("statusPills").innerHTML = "";
    return;
  }
  const report = detail.report || {};
  const autofill = detail.autofill || {};
  $("projectTitle").textContent = detail.name || detail.slug;
  $("projectPath").textContent = detail.path || "";
  const p0 = report.p0_count || 0;
  $("statusPills").innerHTML = [
    pill(detail.slug, "ok"),
    pill(statusLabel(report.status || "unscanned"), report.status === "needs_work" ? "danger" : report.status === "warn" ? "warn" : "ok"),
    pill(`P0 ${p0}`, p0 > 0 ? "danger" : "ok"),
    pill(report.exists ? "有分析报告 / Analysis report found" : "未分析 / Not analyzed", report.exists ? "ok" : "warn"),
    pill(autofill.exists ? `自动补全 / Autofill ${statusLabel(autofill.status || "done")}` : "自动补全空闲 / Autofill idle", autofill.status === "ready_for_director_review" ? "ok" : autofill.exists ? "warn" : ""),
    pill(`场景锁 / Scene locks ${(detail.scene_locks?.items || []).length}`, (detail.scene_locks?.items || []).length ? "ok" : "warn"),
  ].join("");
}

function renderMetrics() {
  const detail = state.detail;
  if (!detail) {
    $("readinessMetric").textContent = "-";
    $("p0Metric").textContent = "-";
    $("shotMetric").textContent = "-";
    $("stageMetric").textContent = "-";
    return;
  }
  const report = detail.report || {};
  const stages = detail.stages || [];
  const pass = stages.filter((stage) => stage.status === "pass").length;
  const warn = stages.filter((stage) => stage.status === "warn").length;
  const fail = stages.filter((stage) => stage.status === "fail" || stage.status === "missing").length;
  $("readinessMetric").textContent = report.readiness == null ? "-" : `${report.readiness}%`;
  $("p0Metric").textContent = report.p0_count ?? 0;
  $("shotMetric").textContent = detail.shot_stats?.rows ?? 0;
  $("stageMetric").textContent = `${pass}/${warn}/${fail}`;
}

function renderLinks() {
  const detail = state.detail;
  if (!detail) return;
  const form = $("linkForm");
  form.elements.source_root.value = detail.source_root || "";
  form.elements.resource_root.value = detail.resource_root || "";
}

function renderStages() {
  const stages = state.detail?.stages || [];
  $("stageHint").textContent = `${stages.length} 阶段 / stages`;
  if (!stages.length) {
    $("stageList").innerHTML = `<div class="empty-state">没有阶段数据 / No stage data.</div>`;
    return;
  }
  $("stageList").innerHTML = stages
    .map((stage) => {
      const weak = (stage.weak || []).slice(0, 3).join(", ");
      const missing = (stage.missing || []).slice(0, 3).join(", ");
      const note = missing || weak || `${stage.file_count} 个文件 / files`;
      const title = STAGE_LABELS[stage.id] || stage.description;
      return `
        <div class="stage-row">
          <span class="stage-code">${escapeHtml(stage.id)}</span>
          <span class="stage-title">
            <strong>${escapeHtml(title)}</strong>
            <span>${escapeHtml(note)}</span>
          </span>
          <span class="status-dot ${escapeHtml(stage.status)}">${escapeHtml(statusLabel(stage.status))}</span>
        </div>
      `;
    })
    .join("");
}

function renderShots() {
  const shots = state.detail?.shots;
  const rows = shots?.rows || [];
  const columns = (shots?.columns || []).slice(0, 8);
  $("shotHint").textContent = shots?.exists ? `${shots.row_count || 0} 行 / rows` : "缺失 / missing";
  if (!shots?.exists) {
    $("shotTable").innerHTML = `<div class="empty-state">缺少 07_shots/shot_list.csv / Missing 07_shots/shot_list.csv.</div>`;
    return;
  }
  if (!rows.length) {
    $("shotTable").innerHTML = `<div class="empty-state">镜头表存在，但目前没有镜头行 / Shot table exists, but it has no rows yet.</div>`;
    return;
  }
  $("shotTable").innerHTML = `
    <table>
      <thead>
        <tr>${columns.map((column) => `<th>${escapeHtml(column)}</th>`).join("")}</tr>
      </thead>
      <tbody>
        ${rows
          .map((row) => `<tr>${columns.map((column) => `<td>${escapeHtml(row[column])}</td>`).join("")}</tr>`)
          .join("")}
      </tbody>
    </table>
  `;
}

function renderReport() {
  const report = state.detail?.report || {};
  $("reportHint").textContent = report.generated_at || "";
  $("reportView").textContent = report.text || "还没有分析报告。点击“分析 / Analyze”生成。/ No analysis report yet. Click Analyze to generate one.";
}

function stageLabel(stage) {
  return STAGE_LABELS[stage] || EXTRA_STAGE_LABELS[stage] || stage || "其他 / Other";
}

function kindLabel(kind) {
  return KIND_LABELS[kind] || kind || "其他 / Other";
}

function annotationAssets() {
  return state.detail?.annotations?.assets || {};
}

function annotationForRef(ref) {
  const annotation = annotationAssets()[ref] || {};
  return typeof annotation === "object" && annotation ? annotation : {};
}

function annotationFor(item) {
  const latest = annotationForRef(item.ref);
  if (Object.keys(latest).length) return latest;
  return item.annotation || {};
}

function decisionLabel(status) {
  if (status === "use") return "✅ 参考 / Use";
  if (status === "reject") return "× 不用 / Reject";
  return "";
}

function decisionClass(status) {
  if (status === "use") return "marked-use";
  if (status === "reject") return "marked-reject";
  return "";
}

function annotationBadge(item) {
  const status = annotationFor(item).status || "";
  const label = decisionLabel(status);
  return label ? `<span class="annotation-badge ${escapeHtml(decisionClass(status))}">${escapeHtml(label)}</span>` : "";
}

function assetSummary(item) {
  const parts = [`${item.origin || "project"}`, `${item.size_kb ?? 0} KB`];
  const decision = decisionLabel(annotationFor(item).status || "");
  if (decision) parts.push(decision);
  if (item.fallback === "legacy_local") parts.push("本地兜底 / local fallback");
  if (item.lfs_missing) parts.push("未下载，需 git lfs pull / not downloaded, run git lfs pull");
  else if (item.lfs_pointer) parts.push("LFS 指针 / LFS pointer");
  return parts.join(" · ");
}

function previewSort(a, b) {
  return Number(Boolean(a.lfs_missing)) - Number(Boolean(b.lfs_missing));
}

function renderLfsPlaceholder(label = "未下载 / not downloaded") {
  return `
    <div class="lfs-placeholder" title="原图存在 Git LFS，需运行 git lfs pull 下载 / Original is in Git LFS; run git lfs pull to download">
      <strong>未下载图<br><span class="lfs-en">image not downloaded</span></strong>
      <em>${escapeHtml(label)}</em>
      <small>需 git lfs pull / run git lfs pull</small>
    </div>
  `;
}

function renderPreviewTile(item) {
  const title = escapeHtml(item.path);
  if (item.lfs_missing || !item.previewable) {
    return `
      <div class="preview-tile preview-tile-missing" title="${title}">
        ${renderLfsPlaceholder(item.lfs_missing ? "未下载 / missing" : "不可预览 / no preview")}
        <span>${escapeHtml(item.name)}</span>
        <small>${escapeHtml(assetSummary(item))}</small>
        ${annotationBadge(item)}
      </div>
    `;
  }
  return `
    <a class="preview-tile" href="${escapeHtml(item.url)}" target="_blank" title="${title}">
      <img src="${escapeHtml(item.url)}" alt="${escapeHtml(item.name)}" loading="lazy" />
      <span>${escapeHtml(item.name)}</span>
      <small>${escapeHtml(assetSummary(item))}</small>
      ${annotationBadge(item)}
    </a>
  `;
}

function renderSceneLockThumb(item, label = "场景 / Scene") {
  if (item?.url && item.previewable && !item.lfs_missing) {
    return `<img src="${escapeHtml(item.url)}" alt="${escapeHtml(label)}" loading="lazy" />`;
  }
  return `<span class="scene-lock-placeholder ${item?.lfs_missing ? "warning" : ""}" title="${item?.lfs_missing ? "需 git lfs pull 下载 / run git lfs pull" : ""}">${escapeHtml(item?.lfs_missing ? "未下载 / not downloaded" : label)}</span>`;
}

function renderVisualGallery() {
  const previews = state.detail?.previews || {};
  const allImages = previews.images || [];
  const images = [...allImages].sort(previewSort).slice(0, 24);
  const missingCount = allImages.filter((item) => item.lfs_missing).length;
  const previewCount = allImages.filter((item) => item.previewable && !item.lfs_missing).length;
  $("visualHint").textContent = missingCount
    ? `${previewCount}/${allImages.length} 可预览 / preview · ${missingCount} 张需 git lfs pull / need git lfs pull`
    : `${images.length} 图片 / images`;
  if (!images.length) {
    $("visualGallery").innerHTML = `<div class="empty-state">没有可预览图片 / No previewable images found.</div>`;
    return;
  }
  $("visualGallery").innerHTML = images.map(renderPreviewTile).join("");
}

function renderSceneLocks() {
  const sceneLocks = state.detail?.scene_locks || {};
  const items = sceneLocks.items || [];
  const overview = (sceneLocks.overview_images || [])[0];
  $("sceneLockHint").textContent = `${items.length} 场景 / scenes`;

  if (overview?.url && overview.previewable && !overview.lfs_missing) {
    $("sceneLockOverview").innerHTML = `
      <a class="scene-overview-link" href="${escapeHtml(overview.url)}" target="_blank" title="${escapeHtml(overview.path)}">
        <img src="${escapeHtml(overview.url)}" alt="${escapeHtml(overview.name)}" loading="lazy" />
      </a>
    `;
  } else if (overview?.lfs_missing) {
    $("sceneLockOverview").innerHTML = `<div class="scene-overview-link scene-overview-placeholder">${renderLfsPlaceholder("场景锁图未下载 / Scene-lock image missing")}</div>`;
  } else {
    $("sceneLockOverview").innerHTML = `<div class="empty-state">还没有场景锁预览。点击“场景锁 / Scene Lock”生成 B01。/ No scene-lock preview yet. Click Scene Lock to generate B01.</div>`;
  }

  if (!items.length) {
    $("sceneLockList").innerHTML = `<div class="empty-state">没有场景锁包 / No scene lock packs found.</div>`;
    $("sceneLockDoc").textContent = sceneLocks.index?.text || "";
    return;
  }
  if (state.selectedSceneLockIndex >= items.length) state.selectedSceneLockIndex = 0;
  $("sceneLockList").innerHTML = items
    .map((item, index) => {
      const preview = item.preview?.previewable ? item.preview : item.master_asset?.previewable ? item.master_asset : item.preview || item.master_asset || {};
      return `
        <button class="scene-lock-card ${index === state.selectedSceneLockIndex ? "active" : ""}" data-index="${index}" type="button">
          ${renderSceneLockThumb(preview, item.scene_id)}
          <span>
            <strong>${escapeHtml(item.scene_id)}</strong>
            <small>${escapeHtml(item.batch || "批次 / batch")} · ${escapeHtml(item.shot_count || 0)} 镜头 / shots</small>
          </span>
        </button>
      `;
    })
    .join("");
  $("sceneLockList").querySelectorAll(".scene-lock-card").forEach((button) => {
    button.addEventListener("click", () => {
      state.selectedSceneLockIndex = Number(button.dataset.index || 0);
      renderSceneLocks();
    });
  });
  const selected = items[state.selectedSceneLockIndex] || items[0];
  $("sceneLockDoc").textContent = selected.doc_text || sceneLocks.index?.text || "";
}

function renderDocs() {
  const previews = state.detail?.previews || {};
  const docs = previews.docs || [];
  $("docHint").textContent = `${docs.length} 文档 / docs`;
  if (!docs.length) {
    $("docTabs").innerHTML = "";
    $("docPreview").textContent = "没有找到剧本或制作文档 / No story or production documents found.";
    return;
  }
  if (state.selectedDocIndex >= docs.length) state.selectedDocIndex = 0;
  $("docTabs").innerHTML = docs
    .map(
      (doc, index) => `
        <button class="doc-tab ${index === state.selectedDocIndex ? "active" : ""}" data-index="${index}" type="button">
          <span>${escapeHtml(doc.kind || "文档 / doc")}</span>
          <strong>${escapeHtml(doc.name)}</strong>
        </button>
      `,
    )
    .join("");
  $("docTabs").querySelectorAll(".doc-tab").forEach((button) => {
    button.addEventListener("click", () => {
      state.selectedDocIndex = Number(button.dataset.index || 0);
      renderDocs();
    });
  });
  const doc = docs[state.selectedDocIndex] || docs[0];
  $("docPreview").textContent = doc.text || "";
}

function renderMediaPreview() {
  const previews = state.detail?.previews || {};
  const videos = (previews.videos || []).filter((item) => item.previewable).slice(0, 4);
  const audio = (previews.audio || []).filter((item) => item.previewable).slice(0, 6);
  $("mediaHint").textContent = `${videos.length} 视频 / video · ${audio.length} 音频 / audio`;
  const videoHtml = videos
    .map(
      (item) => `
        <figure class="media-item">
          <video controls preload="metadata" src="${escapeHtml(item.url)}"></video>
          <figcaption>${escapeHtml(item.name)}<small>${escapeHtml(assetSummary(item))}</small></figcaption>
        </figure>
      `,
    )
    .join("");
  const audioHtml = audio
    .map(
      (item) => `
        <div class="audio-item">
          <strong>${escapeHtml(item.name)}</strong>
          <audio controls preload="metadata" src="${escapeHtml(item.url)}"></audio>
          <small>${escapeHtml(assetSummary(item))}</small>
        </div>
      `,
    )
    .join("");
  $("mediaPreview").innerHTML = videoHtml || audioHtml ? videoHtml + audioHtml : `<div class="empty-state">没有可预览视频或音频 / No previewable video or audio found.</div>`;
}

function allAssets() {
  const previews = state.detail?.previews || {};
  if (Array.isArray(previews.assets)) return previews.assets;
  const seen = new Set();
  return [...(previews.docs || []), ...(previews.images || []), ...(previews.videos || []), ...(previews.audio || []), ...(previews.three_d || [])].filter((item) => {
    if (!item.ref || seen.has(item.ref)) return false;
    seen.add(item.ref);
    return true;
  });
}

function renderSelectOptions(select, options, value) {
  const values = new Set(options.map((option) => option.value));
  const selected = values.has(value) ? value : "all";
  select.innerHTML = options.map((option) => `<option value="${escapeHtml(option.value)}">${escapeHtml(option.label)}</option>`).join("");
  select.value = selected;
  return selected;
}

function renderResourceFilterOptions(assets) {
  const stageCounts = new Map();
  const kindCounts = new Map();
  assets.forEach((item) => {
    stageCounts.set(item.stage || "other", (stageCounts.get(item.stage || "other") || 0) + 1);
    kindCounts.set(item.kind || "other", (kindCounts.get(item.kind || "other") || 0) + 1);
  });
  const stageOptions = [
    { value: "all", label: `全部步骤 / All stages (${assets.length})` },
    ...Object.entries(STAGE_LABELS)
      .filter(([stage]) => stageCounts.has(stage))
      .map(([stage, label]) => ({ value: stage, label: `${label} (${stageCounts.get(stage)})` })),
    ...Object.entries(EXTRA_STAGE_LABELS)
      .filter(([stage]) => stageCounts.has(stage))
      .map(([stage, label]) => ({ value: stage, label: `${label} (${stageCounts.get(stage)})` })),
  ];
  const kindOptions = [
    { value: "all", label: `全部类别 / All kinds (${assets.length})` },
    ...Object.entries(KIND_LABELS)
      .filter(([kind]) => kindCounts.has(kind))
      .map(([kind, label]) => ({ value: kind, label: `${label} (${kindCounts.get(kind)})` })),
  ];
  state.filters.stage = renderSelectOptions($("stageFilter"), stageOptions, state.filters.stage);
  state.filters.kind = renderSelectOptions($("kindFilter"), kindOptions, state.filters.kind);
  $("decisionFilter").value = state.filters.decision;
  $("assetSearch").value = state.filters.query;
}

function filteredAssets() {
  const query = state.filters.query.trim().toLowerCase();
  return allAssets().filter((item) => {
    const annotation = annotationFor(item);
    const status = annotation.status || "";
    if (state.filters.stage !== "all" && item.stage !== state.filters.stage) return false;
    if (state.filters.kind !== "all" && item.kind !== state.filters.kind) return false;
    if (state.filters.decision === "use" && status !== "use") return false;
    if (state.filters.decision === "reject" && status !== "reject") return false;
    if (state.filters.decision === "unset" && status) return false;
    if (!query) return true;
    return [item.name, item.path, item.origin, item.category, stageLabel(item.stage), kindLabel(item.kind), annotation.note]
      .join(" ")
      .toLowerCase()
      .includes(query);
  });
}

function renderResourceThumb(item) {
  if (item.category === "image") {
    if (item.previewable && !item.lfs_missing) {
      return `<a class="resource-thumb" href="${escapeHtml(item.url)}" target="_blank"><img src="${escapeHtml(item.url)}" alt="${escapeHtml(item.name)}" loading="lazy" /></a>`;
    }
    return `<div class="resource-thumb">${renderLfsPlaceholder(item.lfs_missing ? "未下载 / missing" : "不可预览 / no preview")}</div>`;
  }
  const label = item.category === "video" ? "VID" : item.category === "audio" ? "AUD" : item.category === "3d" ? "3D" : item.category === "text" ? "TXT" : "FILE";
  return `<a class="resource-thumb resource-thumb-file" href="${escapeHtml(item.url)}" target="_blank"><strong>${escapeHtml(label)}</strong><span>${escapeHtml(item.extension || "")}</span></a>`;
}

function renderResourceCard(item) {
  const annotation = annotationFor(item);
  const status = annotation.status || "";
  const note = annotation.note || "";
  return `
    <article class="resource-card ${escapeHtml(decisionClass(status))}" data-ref="${escapeHtml(item.ref)}">
      ${renderResourceThumb(item)}
      <div class="resource-card-body">
        <div class="resource-card-title">
          <strong>${escapeHtml(item.name)}</strong>
          ${annotationBadge(item)}
        </div>
        <small class="resource-card-meta">${escapeHtml(stageLabel(item.stage))} · ${escapeHtml(kindLabel(item.kind))} · ${escapeHtml(assetSummary(item))}</small>
        <small class="resource-card-path">${escapeHtml(item.path)}</small>
        <div class="resource-card-actions">
          <button class="decision-button use ${status === "use" ? "active" : ""}" data-status="use" type="button" title="标为后续参考 / Mark as reference">✓</button>
          <button class="decision-button reject ${status === "reject" ? "active" : ""}" data-status="reject" type="button" title="标为不使用 / Mark as rejected">×</button>
          <a class="open-resource-link" href="${escapeHtml(item.url)}" target="_blank">打开 / Open</a>
        </div>
        <textarea class="resource-note" data-ref="${escapeHtml(item.ref)}" rows="2" placeholder="备注：哪里好 / 哪里不好 / Note: what works and what does not">${escapeHtml(note)}</textarea>
      </div>
    </article>
  `;
}

function bindResourceCardEvents() {
  const root = $("resourceBrowser");
  root.querySelectorAll(".decision-button").forEach((button) => {
    button.addEventListener("click", async () => {
      const card = button.closest(".resource-card");
      const ref = card?.dataset.ref || "";
      const current = annotationForRef(ref);
      const nextStatus = current.status === button.dataset.status ? "" : button.dataset.status;
      const note = card?.querySelector(".resource-note")?.value || current.note || "";
      await saveResourceAnnotation(ref, { status: nextStatus, note });
    });
  });
  root.querySelectorAll(".resource-note").forEach((textarea) => {
    const saveNote = async (showToast = false) => {
      const ref = textarea.dataset.ref || "";
      const current = annotationForRef(ref);
      await saveResourceAnnotation(ref, { status: current.status || "", note: textarea.value }, { rerender: false, toast: false });
      if (showToast) toast("备注已保存 / Note saved");
    };
    textarea.addEventListener("input", () => {
      clearTimeout(textarea._saveTimer);
      textarea._saveTimer = setTimeout(() => saveNote(false).catch((error) => toast(`备注保存失败 / Note save failed: ${error.message}`)), 650);
    });
    textarea.addEventListener("blur", async () => {
      clearTimeout(textarea._saveTimer);
      await saveNote(true);
    });
  });
}

function renderResourceBrowser() {
  const assets = allAssets();
  renderResourceFilterOptions(assets);
  const matches = filteredAssets();
  const visible = matches.slice(0, RESOURCE_RENDER_LIMIT);
  const markedUse = assets.filter((item) => annotationFor(item).status === "use").length;
  const markedReject = assets.filter((item) => annotationFor(item).status === "reject").length;
  $("resourceBrowserHint").textContent = `${visible.length}/${matches.length} 已显示 / shown · ✅ ${markedUse} · × ${markedReject}`;
  if (!visible.length) {
    $("resourceBrowser").innerHTML = `<div class="empty-state">没有匹配资源 / No matching assets.</div>`;
    return;
  }
  $("resourceBrowser").innerHTML = visible.map(renderResourceCard).join("");
  bindResourceCardEvents();
}

function sceneAssetUrl(path, origin = "project") {
  if (!state.selectedSlug || !path) return "";
  const assetOrigin = origin === "resource" ? "resource" : "project";
  return `/api/projects/${encodeURIComponent(state.selectedSlug)}/asset?origin=${encodeURIComponent(assetOrigin)}&path=${encodeURIComponent(path)}`;
}

function sceneAssetRef(asset) {
  const origin = asset.origin === "resource" ? "resource" : "project";
  return asset.path ? `${origin}:${asset.path}` : `scene:${asset.asset_id || asset.role || "asset"}`;
}

function selectedScene() {
  const scenes = state.detail?.scene_workbench?.scenes || [];
  if (!scenes.length) return null;
  if (!state.selectedSceneId || !scenes.some((scene) => scene.scene_id === state.selectedSceneId)) {
    state.selectedSceneId = scenes[0].scene_id || "";
  }
  return scenes.find((scene) => scene.scene_id === state.selectedSceneId) || scenes[0];
}

function sceneStatusLabel(status) {
  return SCENE_STATUS_LABELS[status] || status || "未标记 / Unmarked";
}

function queueableImpact(impact) {
  return ["create", "modify"].includes(impact.action || "");
}

function sceneAssetKind(asset, step) {
  if (asset?.kind && KIND_LABELS[asset.kind]) return asset.kind;
  const haystack = [asset?.asset_id, asset?.role, asset?.path, step].join(" ").toLowerCase();
  if (haystack.includes("video_prompt")) return "video_prompt";
  if (haystack.includes("image_prompt") || haystack.includes("/prompts/") || haystack.includes("shot_prompt")) return "shot_prompt";
  if (haystack.includes("keyframe") || haystack.includes("storyboard")) return "storyboard_keyframe";
  if (haystack.includes("scene_lock")) return "scene_lock";
  if (haystack.includes("whitebox") || haystack.includes("camera") || haystack.includes("previs") || haystack.includes("blender")) return "whitebox";
  if (haystack.includes("script") || haystack.includes("beat") || haystack.includes("outline") || haystack.includes("dialogue") || step === "03_story") return "script";
  if (haystack.includes("look") || haystack.includes("palette") || haystack.includes("lighting") || step === "04_lookdev") return "lookdev";
  if (haystack.includes("character")) return "character_ref";
  if (haystack.includes("location") || haystack.includes("visual_ref") || haystack.includes("reference_assets")) return "scene_ref";
  if (haystack.includes("audio") || haystack.includes("sound")) return "audio";
  if (haystack.includes("rough_cut") || haystack.endsWith(".mp4") || haystack.includes("/video/")) return "video";
  if (haystack.endsWith(".png") || haystack.endsWith(".jpg") || haystack.endsWith(".jpeg") || haystack.endsWith(".webp") || haystack.includes("/images/")) return "image";
  if (haystack.includes("delivery") || haystack.includes("review") || haystack.includes("fix_queue")) return "document";
  return "other";
}

function sceneKindOptions(stageAssets, steps) {
  const counts = new Map();
  steps.forEach((step) => {
    (stageAssets[step] || []).forEach((asset) => {
      const kind = sceneAssetKind(asset, step);
      counts.set(kind, (counts.get(kind) || 0) + 1);
    });
  });
  return [
    { value: "all", label: `全部类别 / All kinds (${[...counts.values()].reduce((sum, count) => sum + count, 0)})` },
    ...Object.entries(KIND_LABELS)
      .filter(([kind]) => counts.has(kind))
      .map(([kind, label]) => ({ value: kind, label: `${label} (${counts.get(kind)})` })),
  ];
}

function impactActionOptions(impact, disabled) {
  const current = IMPACT_ACTION_LABELS[impact?.action] ? impact.action : "modify";
  return `
    <select class="impact-action-select" data-impact-id="${escapeHtml(impact?.impact_id || "")}" ${disabled ? "disabled" : ""}>
      ${Object.entries(IMPACT_ACTION_LABELS)
        .map(([value, label]) => `<option value="${escapeHtml(value)}" ${current === value ? "selected" : ""}>${escapeHtml(label)}</option>`)
        .join("")}
    </select>
  `;
}

function isExampleChangeRequest(request) {
  return String(request?.status || "").endsWith("_example");
}

function scenePathLink(path, label = "打开 / Open") {
  const url = sceneAssetUrl(path || "");
  return url ? `<a href="${escapeHtml(url)}" target="_blank">${escapeHtml(label)}</a>` : "";
}

function sceneAssetLink(asset, label = "打开 / Open") {
  const url = sceneAssetUrl(asset.path || "", asset.origin || "project");
  return url ? `<a href="${escapeHtml(url)}" target="_blank">${escapeHtml(label)}</a>` : "";
}

function closeAssetPreview() {
  const modal = $("assetPreviewModal");
  if (!modal) return;
  modal.hidden = true;
  document.body.classList.remove("modal-open");
  $("assetPreviewTitle").textContent = "Preview";
  $("assetPreviewMeta").textContent = "";
  $("assetPreviewBody").innerHTML = "";
}

async function openAssetPreview(asset) {
  const modal = $("assetPreviewModal");
  const title = $("assetPreviewTitle");
  const meta = $("assetPreviewMeta");
  const body = $("assetPreviewBody");
  if (!modal || !title || !meta || !body || !asset?.url) return;
  const path = asset.path || "";
  title.textContent = asset.asset_id || asset.role || path || "Asset";
  meta.textContent = `${asset.stage || ""} · ${kindLabel(asset.kind)} · ${path}`;
  body.innerHTML = `<div class="qa-loading">读取中 / Loading...</div>`;
  modal.hidden = false;
  document.body.classList.add("modal-open");
  if (isImagePath(path)) {
    body.innerHTML = `<img class="asset-preview-image" src="${escapeHtml(asset.url)}" alt="${escapeHtml(title.textContent)}" />`;
    return;
  }
  if (VIDEO_PREVIEW_EXTENSIONS.test(path)) {
    body.innerHTML = `<video class="asset-preview-media" src="${escapeHtml(asset.url)}" controls></video>`;
    return;
  }
  if (AUDIO_PREVIEW_EXTENSIONS.test(path)) {
    body.innerHTML = `<audio class="asset-preview-audio" src="${escapeHtml(asset.url)}" controls></audio>`;
    return;
  }
  if (!TEXT_PREVIEW_EXTENSIONS.test(path)) {
    body.innerHTML = `
      <div class="empty-state">
        当前资源不是可内嵌预览格式 / This asset cannot be previewed inline.
        ${sceneAssetLink(asset, "打开文件 / Open file")}
      </div>
    `;
    return;
  }
  try {
    const response = await fetch(asset.url);
    if (!response.ok) throw new Error(response.statusText);
    const text = await response.text();
    body.innerHTML = `<pre class="asset-preview-text">${escapeHtml(text)}</pre>`;
  } catch (error) {
    body.innerHTML = `<div class="empty-state">预览失败 / Preview failed: ${escapeHtml(error.message)}</div>`;
  }
}

function generationAdapters() {
  const adapters = state.detail?.generation_adapters?.adapters || [];
  if (adapters.length) return adapters;
  return [
    {
      adapter_id: "manual_packet",
      label: "任务包 / Manual packet",
      type: "manual_packet",
      enabled: true,
    },
  ];
}

function preferredGenerationAdapter() {
  const adapters = generationAdapters();
  return (
    adapters.find((adapter) => adapter.type === "command" && adapter.enabled && !adapter.requires_confirmation) ||
    adapters.find((adapter) => adapter.adapter_id === "manual_packet") ||
    adapters[0]
  );
}

function stageShortLabel(stage) {
  const label = stageLabel(stage);
  return label.split(" / ")[0] || stage || "其他";
}

function isImagePath(path = "") {
  return /\.(png|jpe?g|webp|gif)$/i.test(path);
}

function shotIdFromText(value = "") {
  const match = String(value).match(/MSB\d{3}/i);
  return match ? match[0].toUpperCase() : "";
}

function sceneAssetShotId(asset) {
  return shotIdFromText([asset?.asset_id, asset?.path, asset?.role].join(" "));
}

function flattenSceneAssets(scene) {
  const stageAssets = scene?.resource_manifest?.stage_assets || {};
  return Object.entries(stageAssets).flatMap(([stage, assets]) =>
    (assets || []).map((asset) => ({
      ...asset,
      stage,
      kind: sceneAssetKind(asset, stage),
      ref: sceneAssetRef(asset),
      url: sceneAssetUrl(asset.path || "", asset.origin || "project"),
      shot_id: sceneAssetShotId(asset),
    })),
  );
}

function framePriority(frame) {
  const kindOrder = {
    storyboard_keyframe: 1,
    image: 2,
    whitebox: 3,
    scene_ref: 4,
    lookdev: 5,
  };
  const stageOrder = {
    "08_generation": 1,
    "07_shots": 2,
    "06_previs": 3,
    "04_lookdev": 4,
    "05_asset_bible": 5,
  };
  return (kindOrder[frame.kind] || 20) * 10 + (stageOrder[frame.stage] || 9);
}

function frameIsUsable(frame) {
  return frame && !frame.lfs_missing && frame.previewable !== false;
}

function storyboardFrames(scene) {
  const frames = flattenSceneAssets(scene).filter((asset) => {
    if (!asset.path || !asset.url) return false;
    if (state.storyboardStage !== "all" && asset.stage !== state.storyboardStage) return false;
    return isImagePath(asset.path);
  });
  return frames.sort((a, b) => {
    const usable = Number(!frameIsUsable(a)) - Number(!frameIsUsable(b));
    if (usable) return usable;
    const shotA = a.shot_id || "ZZZ";
    const shotB = b.shot_id || "ZZZ";
    if (shotA !== shotB) return shotA.localeCompare(shotB);
    const priority = framePriority(a) - framePriority(b);
    if (priority) return priority;
    return String(a.asset_id || a.path).localeCompare(String(b.asset_id || b.path));
  });
}

function selectedStoryboardFrame(scene) {
  const frames = storyboardFrames(scene);
  if (!frames.length) {
    state.selectedFrameRef = "";
    return { frame: null, frames };
  }
  const current = frames.find((frame) => frame.ref === state.selectedFrameRef);
  const frame = current && frameIsUsable(current) ? current : frames.find(frameIsUsable) || current || frames[0];
  state.selectedFrameRef = frame.ref;
  return { frame, frames };
}

function moveStoryboardFrame(delta) {
  if (!state.detail || document.body.classList.contains("modal-open")) return false;
  const scene = selectedScene();
  const { frame, frames } = selectedStoryboardFrame(scene);
  if (!frame || !frames.length) return false;
  const currentIndex = frames.findIndex((item) => item.ref === frame.ref);
  const nextIndex = clamp(currentIndex + delta, 0, frames.length - 1);
  if (nextIndex === currentIndex) {
    toast(delta > 0 ? "已经是最后一张 / Last frame" : "已经是第一张 / First frame");
    return true;
  }
  state.selectedFrameRef = frames[nextIndex].ref;
  renderStoryboardStudio();
  window.setTimeout(() => document.querySelector(".frame-thumb.active")?.scrollIntoView({ block: "nearest", inline: "center" }), 40);
  return true;
}

function storyboardStageOptions(scene) {
  const counts = new Map();
  flattenSceneAssets(scene)
    .filter((asset) => isImagePath(asset.path || ""))
    .forEach((asset) => counts.set(asset.stage, (counts.get(asset.stage) || 0) + 1));
  return [
    { value: "all", label: `全部图片 / All images (${[...counts.values()].reduce((sum, count) => sum + count, 0)})` },
    ...Object.entries(STAGE_LABELS)
      .filter(([stage]) => counts.has(stage))
      .map(([stage]) => ({ value: stage, label: `${stageShortLabel(stage)} (${counts.get(stage)})` })),
  ];
}

function frameTitle(frame) {
  if (!frame) return "";
  const shot = frame.shot_id ? `${frame.shot_id} · ` : "";
  return `${shot}${frame.asset_id || frame.role || frame.path}`;
}

function relatedFrameAssets(scene, frame) {
  if (!scene || !frame) return [];
  const assets = flattenSceneAssets(scene);
  const sameShot = assets.filter((asset) => frame.shot_id && asset.shot_id === frame.shot_id && asset.ref !== frame.ref);
  const context = assets.filter((asset) =>
    ["03_story", "04_lookdev", "05_asset_bible", "06_previs"].includes(asset.stage) &&
    asset.ref !== frame.ref &&
    !sameShot.some((item) => item.ref === asset.ref),
  );
  return [...sameShot, ...context].slice(0, 12);
}

function referenceSelectionFor(frameRef, ref) {
  const frameSelection = state.referenceSelection[frameRef] || {};
  return frameSelection[ref] || { selected: false, note: "" };
}

function setReferenceSelection(frameRef, ref, patch) {
  if (!state.referenceSelection[frameRef]) state.referenceSelection[frameRef] = {};
  const current = referenceSelectionFor(frameRef, ref);
  state.referenceSelection[frameRef][ref] = { ...current, ...patch };
}

function frameVersions(scene, frame) {
  const versions = scene?.version_registry?.versions || [];
  if (!frame?.asset_id || !Array.isArray(versions)) return [];
  return versions.filter((record) => record?.asset_id === frame.asset_id).slice().reverse();
}

function storyboardRequestsForFrame(scene, frame) {
  const requests = scene?.change_requests || [];
  if (!frame?.asset_id || !Array.isArray(requests)) return [];
  return requests
    .filter(
      (request) =>
        !isExampleChangeRequest(request) &&
        request?.trigger_step === frame.stage &&
        request?.trigger_asset_id === frame.asset_id,
    )
    .slice(0, 3);
}

function selectedQueueableImpacts(request) {
  const impacts = request?.impact_table || [];
  if (!Array.isArray(impacts)) return [];
  const direct = impacts.filter((impact) => impact?.impact_scope === "direct" && ["create", "modify"].includes(impact?.action));
  if (direct.length) return direct;
  return impacts.filter((impact) => impact?.selected && ["create", "modify"].includes(impact?.action));
}

function boardStorageKey() {
  return state.selectedSlug ? `pipeline-board:${state.selectedSlug}` : "pipeline-board";
}

function loadBoardState() {
  try {
    const raw = window.localStorage.getItem(boardStorageKey());
    const parsed = raw ? JSON.parse(raw) : {};
    state.boardNodes = Array.isArray(parsed.nodes) ? parsed.nodes : [];
    state.boardEdges = Array.isArray(parsed.edges) ? parsed.edges : [];
  } catch {
    state.boardNodes = [];
    state.boardEdges = [];
  }
}

function saveBoardState() {
  if (!state.selectedSlug) return;
  try {
    window.localStorage.setItem(boardStorageKey(), JSON.stringify({ nodes: state.boardNodes, edges: state.boardEdges }));
  } catch {
    // Local persistence is a convenience; generation packets remain project-backed.
  }
}

function boardAssetTags(asset) {
  const tags = new Set();
  const haystack = [asset.asset_id, asset.role, asset.path, asset.kind, asset.stage].join(" ").toLowerCase();
  if (asset.kind === "character_ref" || haystack.includes("character") || haystack.includes("person") || haystack.includes("三视图")) tags.add("character");
  if (asset.kind === "scene_ref" || haystack.includes("location") || haystack.includes("scene") || haystack.includes("environment")) tags.add("scene");
  if (asset.kind === "whitebox" || haystack.includes("whitebox") || haystack.includes("previs")) tags.add("whitebox");
  if (asset.kind === "storyboard_keyframe" || haystack.includes("keyframe") || haystack.includes("storyboard")) tags.add("keyframe");
  if (asset.kind === "lookdev" || haystack.includes("lookdev") || haystack.includes("style") || haystack.includes("palette")) tags.add("lookdev");
  const annotation = annotationForRef(asset.ref);
  if (annotation.status === "use") tags.add("marked_use");
  if (annotation.status === "reject") tags.add("marked_reject");
  if (!annotation.status) tags.add("unmarked");
  return [...tags];
}

function allBoardImageAssets() {
  const byRef = new Map();
  const scenes = state.detail?.scene_workbench?.scenes || [];
  scenes.forEach((scene, sceneIndex) => {
    flattenSceneAssets(scene)
      .filter((asset) => isImagePath(asset.path || "") && asset.url)
      .forEach((asset, assetIndex) => {
        const boardAsset = {
          ...asset,
          scene_id: scene.scene_id || "",
          scene_title: scene.title || "",
          scene_slug: scene.scene_slug || "",
          act_id: scene.act_id || "",
          act_title: scene.act_title || "",
          scene_order: sceneIndex,
          asset_order: assetIndex,
          sort_text: [asset.shot_id, asset.asset_id, asset.role, asset.path].filter(Boolean).join(" "),
        };
        boardAsset.tags = boardAssetTags(boardAsset);
        byRef.set(boardAsset.ref, boardAsset);
      });
  });
  const previewImages = state.detail?.previews?.images || [];
  previewImages.forEach((item, itemIndex) => {
    if (!item?.path || !item?.url || !isImagePath(item.path)) return;
    const origin = item.origin === "resource" ? "resource" : "project";
    const ref = `${origin}:${item.path}`;
    if (byRef.has(ref)) return;
    const kind = item.category || sceneAssetKind(item, "08_generation");
    const boardAsset = {
      asset_id: item.name || item.path.split("/").pop() || "image",
      role: item.category || "project_image",
      path: item.path,
      origin,
      url: item.url,
      ref,
      kind: KIND_LABELS[kind] ? kind : "image",
      stage: "08_generation",
      scene_id: "",
      scene_title: "未绑定场戏 / Unbound",
      scene_slug: "",
      act_id: "",
      act_title: "全项目 / Project",
      shot_id: shotIdFromText(item.path),
      scene_order: 9999,
      asset_order: itemIndex,
      sort_text: [shotIdFromText(item.path), item.name, item.path].filter(Boolean).join(" "),
    };
    boardAsset.tags = boardAssetTags(boardAsset);
    byRef.set(ref, boardAsset);
  });
  return [...byRef.values()].sort((a, b) => {
    const sceneOrder = Number(a.scene_order ?? 9999) - Number(b.scene_order ?? 9999);
    if (sceneOrder) return sceneOrder;
    const scene = naturalCompare(a.scene_id || "ZZZ", b.scene_id || "ZZZ");
    if (scene) return scene;
    const shot = naturalCompare(a.shot_id || a.sort_text || "ZZZ", b.shot_id || b.sort_text || "ZZZ");
    if (shot) return shot;
    const asset = naturalCompare(a.asset_id || a.path, b.asset_id || b.path);
    if (asset) return asset;
    return Number(a.asset_order ?? 9999) - Number(b.asset_order ?? 9999);
  });
}

function boardAssetByRef(ref) {
  return allBoardImageAssets().find((asset) => asset.ref === ref) || null;
}

function boardNodeAsset(node) {
  return boardAssetByRef(node?.assetRef || "");
}

function openBoardImageLightbox(nodeId) {
  const node = state.boardNodes.find((item) => item.id === nodeId);
  const asset = boardNodeAsset(node);
  const modal = $("boardImageLightbox");
  const img = $("boardImageLightboxImg");
  if (!asset?.url || !modal || !img) return;
  img.src = asset.url;
  img.alt = asset.asset_id || asset.path || "Board image";
  modal.hidden = false;
  document.body.classList.add("modal-open");
}

function closeBoardImageLightbox() {
  const modal = $("boardImageLightbox");
  const img = $("boardImageLightboxImg");
  if (!modal || !img) return;
  modal.hidden = true;
  img.removeAttribute("src");
  img.alt = "";
  document.body.classList.remove("modal-open");
}

function boardSceneFilterOptions(assets) {
  const options = [{ value: "all", label: `全部幕/场戏 / All (${assets.length})` }];
  const acts = new Map();
  assets.forEach((asset) => {
    if (asset.act_id) acts.set(asset.act_id, asset.act_title || asset.act_id);
  });
  acts.forEach((label, actId) => options.push({ value: `act:${actId}`, label: `${label}` }));
  const scenes = new Map();
  assets.forEach((asset) => {
    if (asset.scene_id) scenes.set(asset.scene_id, `${asset.scene_id} · ${asset.scene_title || ""}`);
  });
  scenes.forEach((label, sceneId) => options.push({ value: `scene:${sceneId}`, label }));
  return options;
}

function boardAssetMatches(asset) {
  const sceneFilter = state.boardFilters.scene;
  if (sceneFilter?.startsWith("act:") && asset.act_id !== sceneFilter.slice(4)) return false;
  if (sceneFilter?.startsWith("scene:") && asset.scene_id !== sceneFilter.slice(6)) return false;
  if (state.boardFilters.tag !== "all" && !(asset.tags || []).includes(state.boardFilters.tag)) return false;
  const query = state.boardFilters.query.trim().toLowerCase();
  if (!query) return true;
  return [
    asset.asset_id,
    asset.role,
    asset.path,
    asset.scene_id,
    asset.scene_title,
    asset.act_title,
    asset.shot_id,
    kindLabel(asset.kind),
  ]
    .join(" ")
    .toLowerCase()
    .includes(query);
}

function boardNodeTitle(node) {
  const asset = boardNodeAsset(node);
  return asset?.asset_id || asset?.role || asset?.path || "Image";
}

function boardNodeNoteLabel(node) {
  return node.role === "main" ? "主图备注 / Full generation brief" : "关联备注 / Reference element note";
}

function boardNodeIncomingEdges(nodeId) {
  return state.boardEdges.filter((edge) => edge.targetId === nodeId);
}

function boardNodeOutgoingEdges(nodeId) {
  return state.boardEdges.filter((edge) => edge.sourceId === nodeId);
}

function boardNodeCenter(node) {
  return { x: Number(node.x || 0) + 140, y: Number(node.y || 0) + 126 };
}

function boardCanvasPoint(event) {
  const stage = $("referenceBoardCanvas")?.querySelector(".board-canvas-stage");
  const rect = stage?.getBoundingClientRect();
  if (!rect) return { x: 40, y: 40 };
  return {
    x: clamp(event.clientX - rect.left + stage.scrollLeft - 140, 12, Math.max(12, stage.scrollWidth - 300)),
    y: clamp(event.clientY - rect.top + stage.scrollTop - 80, 12, Math.max(12, stage.scrollHeight - 260)),
  };
}

function boardDefaultNodePoint() {
  const lastNode = state.boardNodes[state.boardNodes.length - 1];
  if (lastNode) {
    const nextX = Number(lastNode.x || 0) + 340;
    if (nextX <= 1600) return { x: nextX, y: Number(lastNode.y || 0) };
    return { x: 40, y: Number(lastNode.y || 0) + 380 };
  }
  return {
    x: 40,
    y: 40,
  };
}

function addBoardNode(assetRef, point) {
  if (!assetRef || !boardAssetByRef(assetRef)) return;
  const id = `node_${Date.now()}_${Math.random().toString(16).slice(2, 8)}`;
  const role = state.boardNodes.some((node) => node.role === "main") ? "reference" : "main";
  state.boardNodes.push({
    id,
    assetRef,
    role,
    note: "",
    x: Math.round(point.x),
    y: Math.round(point.y),
  });
  saveBoardState();
  renderReferenceBoard();
}

function removeBoardNode(nodeId) {
  state.boardNodes = state.boardNodes.filter((node) => node.id !== nodeId);
  state.boardEdges = state.boardEdges.filter((edge) => edge.sourceId !== nodeId && edge.targetId !== nodeId);
  if (state.boardLinkSourceId === nodeId) state.boardLinkSourceId = "";
  saveBoardState();
  renderReferenceBoard();
}

function createBoardEdge(sourceId, targetId) {
  if (!sourceId) {
    toast("请先点击“设为主图” / Choose Link from first");
    return;
  }
  if (!targetId || sourceId === targetId) {
    toast("请选择另一张图片作为关联图 / Choose another image as reference");
    return;
  }
  const existing = state.boardEdges.find((edge) => edge.sourceId === sourceId && edge.targetId === targetId);
  if (existing) {
    toast("这条关联已经存在 / Relation already exists");
    return;
  }
  const source = state.boardNodes.find((node) => node.id === sourceId);
  const target = state.boardNodes.find((node) => node.id === targetId);
  if (source) source.role = "main";
  if (target) target.role = "reference";
  state.boardEdges.push({
    id: `edge_${Date.now()}_${Math.random().toString(16).slice(2, 8)}`,
    sourceId,
    targetId,
    note: "",
  });
  state.boardLinkSourceId = "";
  saveBoardState();
  renderReferenceBoard();
}

function boardPromptForNode(node) {
  const asset = boardNodeAsset(node);
  const outgoing = boardNodeOutgoingEdges(node.id);
  const references = outgoing
    .map((edge) => {
      const refNode = state.boardNodes.find((item) => item.id === edge.targetId);
      const refAsset = boardNodeAsset(refNode);
      if (!refNode || !refAsset) return "";
      return [
        `- Reference / 关联图: ${refAsset.asset_id || refAsset.path}`,
        `  Path: ${refAsset.path}`,
        `  Relation note / 连线说明: ${edge.note || "Use selected visual element from this reference."}`,
        `  Reference note / 关联图备注: ${refNode.note || "Borrow identity, layout, style, prop, pose, or spatial logic as applicable."}`,
      ].join("\n");
    })
    .filter(Boolean)
    .join("\n");
  return [
    `Board generation request / 画布生成请求`,
    "",
    `Scene / 场戏: ${asset?.scene_id || selectedScene()?.scene_id || ""} ${asset?.scene_title || selectedScene()?.title || ""}`,
    `Main image / 主图: ${asset?.asset_id || asset?.path || ""}`,
    `Main path / 主图路径: ${asset?.path || ""}`,
    "",
    "Main brief / 主图备注:",
    node.note || "- Describe the complete new image to generate from this main image.",
    "",
    "Reference stack / 关联素材:",
    references || "- No linked references. Use only the main image and note.",
    "",
    "Output goal / 输出目标:",
    "- Generate a clean, stable, high-quality key image suitable for downstream video AIGC.",
    "- Preserve the main composition unless the note explicitly changes it.",
    "- Integrate reference elements only according to relation notes.",
    "- Avoid noise, distorted anatomy, inconsistent character identity, unreadable composition, watermarks, random text, and unwanted new props.",
  ].join("\n");
}

function boardGenerationMessageFromRun(runResult, adapter) {
  const queue = runResult.generation_queue || [];
  const finalItem = queue.find((item) => item.final_output_path) || null;
  const packetItem = queue.find((item) => item.packet_path || item.result_path) || null;
  const run = runResult.change_request?.generation_run || {};
  const adapterType = run.adapter_type || adapter?.type || "manual_packet";
  if (adapterType === "manual_packet") {
    return {
      status: "packet",
      outputPath: packetItem?.packet_path || packetItem?.result_path || "",
      message: "已生成任务包，当前未启用直接出图适配器 / Packet ready; no direct image adapter is enabled.",
    };
  }
  if (finalItem?.final_output_path) {
    return {
      status: "image",
      outputPath: finalItem.final_output_path,
      message: `图片已生成 / Image generated: ${finalItem.final_output_path}`,
    };
  }
  return {
    status: run.status === "generation_failed" ? "failed" : "packet",
    outputPath: packetItem?.packet_path || packetItem?.result_path || "",
    message: "生成器已运行，但没有回填图片路径 / Adapter ran, but no image output path was attached.",
  };
}

function setBoardGeneration(nodeId, progress, message) {
  state.boardGeneration = { nodeId, progress, message };
  renderBoardCanvas();
  bindReferenceBoardEvents();
}

function clearBoardGeneration() {
  state.boardGeneration = { nodeId: "", progress: 0, message: "" };
  renderBoardCanvas();
  bindReferenceBoardEvents();
}

async function createBoardGenerationPacket(nodeId) {
  const node = state.boardNodes.find((item) => item.id === nodeId);
  const asset = boardNodeAsset(node);
  const scene = asset?.scene_id ? (state.detail?.scene_workbench?.scenes || []).find((item) => item.scene_id === asset.scene_id) : selectedScene();
  if (!node || !asset || !scene) {
    toast("画布节点缺少场戏信息 / Board node is missing scene context");
    return;
  }
  if (state.busy) {
    toast("已有任务正在执行 / Another task is running");
    return;
  }
  const adapter = preferredGenerationAdapter();
  const creativeDirection = boardPromptForNode(node);
  state.busy = true;
  node.lastGeneration = {
    status: "running",
    message: "正在分析画布关系 / Reading board graph...",
    outputPath: "",
  };
  setBoardGeneration(nodeId, 8, node.lastGeneration.message);
  toast("画布生成开始 / Board generation started");
  try {
    setBoardGeneration(nodeId, 18, "正在创建变更请求 / Creating change request...");
    const changeResult = await requestJson(`/api/projects/${state.selectedSlug}/scene-change-request`, {
      method: "POST",
      body: JSON.stringify({
        scene_id: scene.scene_id,
        trigger_step: asset.stage || "08_generation",
        trigger_asset_id: asset.asset_id || "",
        creative_direction: creativeDirection,
      }),
    });
    setBoardGeneration(nodeId, 42, "正在计算影响资产 / Selecting impacted assets...");
    const request = changeResult.change_request || {};
    const selectedImpacts = selectedQueueableImpacts(request);
    if (!selectedImpacts.length) {
      state.detail = changeResult.project || state.detail;
      state.activeChangeRequest = request;
      renderAll();
      throw new Error("已写入影响表，但没有可入队资产 / Impact table created, but no queueable asset.");
    }
    const selectedImpactIds = selectedImpacts.map((impact) => impact.impact_id);
    const actionOverrides = Object.fromEntries(selectedImpacts.map((impact) => [impact.impact_id, impact.action]));
    setBoardGeneration(nodeId, 62, "正在写入生成队列 / Writing generation queue...");
    const queueResult = await requestJson(`/api/projects/${state.selectedSlug}/scene-generate`, {
      method: "POST",
      body: JSON.stringify({
        change_request_id: request.change_request_id,
        selected_impact_ids: selectedImpactIds,
        action_overrides: actionOverrides,
        notes: `Reference board packet for ${boardNodeTitle(node)}`,
      }),
    });
    const adapterId = adapter?.adapter_id || "manual_packet";
    const runningMessage =
      adapter?.type === "command"
        ? `正在调用生成适配器 / Running adapter: ${adapterId}`
        : "正在生成任务包 / Writing manual packet...";
    setBoardGeneration(nodeId, 82, runningMessage);
    const runResult = await requestJson(`/api/projects/${state.selectedSlug}/scene-run-generation`, {
      method: "POST",
      body: JSON.stringify({
        change_request_id: request.change_request_id,
        adapter_id: adapterId,
      }),
    });
    state.detail = runResult.project || queueResult.project || changeResult.project || state.detail;
    state.activeChangeRequest = runResult.change_request || queueResult.change_request || request;
    const result = boardGenerationMessageFromRun(runResult, adapter);
    node.lastGeneration = {
      ...result,
      changeRequestId: request.change_request_id || "",
      adapterId,
      completedAt: new Date().toLocaleString(),
    };
    saveBoardState();
    setBoardGeneration(nodeId, 100, result.message);
    renderAll();
    renderReferenceBoard();
    toast(result.message);
  } catch (error) {
    node.lastGeneration = {
      status: "failed",
      message: error.message,
      outputPath: "",
      completedAt: new Date().toLocaleString(),
    };
    saveBoardState();
    setBoardGeneration(nodeId, 100, `生成失败 / Failed: ${error.message}`);
    toast(`画布生成失败 / Board generation failed: ${error.message}`);
  } finally {
    state.busy = false;
    window.setTimeout(clearBoardGeneration, 1600);
  }
}

function renderBoardEdges() {
  if (!state.boardEdges.length) return "";
  const nodesById = new Map(state.boardNodes.map((node) => [node.id, node]));
  return `
    <svg class="board-edge-layer" aria-hidden="true">
      <defs>
        <marker id="boardArrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
          <path d="M0,0 L0,6 L9,3 z"></path>
        </marker>
      </defs>
      ${state.boardEdges
        .map((edge) => {
          const source = nodesById.get(edge.sourceId);
          const target = nodesById.get(edge.targetId);
          if (!source || !target) return "";
          const a = boardNodeCenter(source);
          const b = boardNodeCenter(target);
          const midX = (a.x + b.x) / 2;
          return `<path d="M ${a.x} ${a.y} C ${midX} ${a.y}, ${midX} ${b.y}, ${b.x} ${b.y}" marker-end="url(#boardArrow)"></path>`;
        })
        .join("")}
    </svg>
  `;
}

function renderBoardNode(node) {
  const asset = boardNodeAsset(node);
  if (!asset) return "";
  const outgoingCount = boardNodeOutgoingEdges(node.id).length;
  const incoming = boardNodeIncomingEdges(node.id);
  const activeLink = state.boardLinkSourceId === node.id;
  const activeGeneration = state.boardGeneration.nodeId === node.id;
  const progress = clamp(Number(state.boardGeneration.progress || 0), 0, 100);
  const lastGeneration = node.lastGeneration || {};
  const generationMessage = activeGeneration ? state.boardGeneration.message : lastGeneration.message || "";
  const generationOutput = !activeGeneration && lastGeneration.outputPath ? lastGeneration.outputPath : "";
  const generationClass = activeGeneration ? "running" : lastGeneration.status || "";
  return `
    <article class="board-node-card ${escapeHtml(node.role || "reference")} ${activeLink ? "linking" : ""} ${activeGeneration ? "generating" : ""}" data-node-id="${escapeHtml(node.id)}" style="left:${Number(node.x || 0)}px; top:${Number(node.y || 0)}px;">
      <header>
        <select class="board-node-role" data-node-id="${escapeHtml(node.id)}">
          <option value="main" ${node.role === "main" ? "selected" : ""}>主图 / Main</option>
          <option value="reference" ${node.role !== "main" ? "selected" : ""}>关联图 / Reference</option>
        </select>
        <button class="mini-command board-link-source" data-node-id="${escapeHtml(node.id)}" type="button">${activeLink ? "等待连接 / Linking" : "设为主图 / Link from"}</button>
        <button class="mini-command board-link-target" data-node-id="${escapeHtml(node.id)}" type="button">连为关联图 / Link to</button>
        <button class="icon-button board-node-remove" data-node-id="${escapeHtml(node.id)}" type="button" title="移除 / Remove">×</button>
      </header>
      <img class="board-node-image" data-node-id="${escapeHtml(node.id)}" src="${escapeHtml(asset.url)}" alt="${escapeHtml(asset.asset_id || asset.path)}" draggable="false" title="双击预览大图 / Double-click to preview" />
      <div class="board-node-meta">
        <strong>${escapeHtml(asset.asset_id || asset.role || asset.path)}</strong>
        <small>${escapeHtml(asset.scene_id || "PROJECT")} · ${escapeHtml(kindLabel(asset.kind))} · ${escapeHtml(asset.path || "")}</small>
      </div>
      <label>${escapeHtml(boardNodeNoteLabel(node))}
        <textarea class="board-node-note" data-node-id="${escapeHtml(node.id)}" rows="4" placeholder="${node.role === "main" ? "完整描述要生成的新图 / Describe the full new image" : "说明要借用什么元素 / Describe what to borrow"}">${escapeHtml(node.note || "")}</textarea>
      </label>
      ${
        incoming.length
          ? `<div class="board-edge-notes">
              ${incoming
                .map(
                  (edge) => `
                    <label>连线说明 / Relation note
                      <textarea class="board-edge-note" data-edge-id="${escapeHtml(edge.id)}" rows="2" placeholder="例如：沿用白模机位，把人物放进主图 / Use whitebox camera, place character into main image">${escapeHtml(edge.note || "")}</textarea>
                    </label>
                  `,
                )
                .join("")}
            </div>`
          : ""
      }
      <footer>
        <span>${outgoingCount} 关联 / refs</span>
        <button class="command-button primary board-generate-node" data-node-id="${escapeHtml(node.id)}" type="button" ${state.busy ? "disabled" : ""}>${activeGeneration ? `生成中 ${progress}%` : "生成 / Generate"}</button>
      </footer>
      ${
        generationMessage
          ? `<div class="board-generation-status ${escapeHtml(generationClass)}">
              <div class="board-generation-line">
                <span>${escapeHtml(generationMessage)}</span>
                ${activeGeneration ? `<strong>${progress}%</strong>` : ""}
              </div>
              <div class="board-generation-bar"><span style="width:${activeGeneration ? progress : 100}%"></span></div>
              ${
                generationOutput
                  ? `<small>${lastGeneration.status === "image" ? "图片路径 / Image" : "任务包 / Packet"}: ${escapeHtml(generationOutput)}</small>`
                  : ""
              }
            </div>`
          : ""
      }
    </article>
  `;
}

function renderBoardCanvas() {
  const root = $("referenceBoardCanvas");
  if (!root) return;
  root.innerHTML = `
    <div class="board-canvas-stage">
      ${renderBoardEdges()}
      ${
        state.boardNodes.length
          ? state.boardNodes.map(renderBoardNode).join("")
          : `<div class="board-empty-state">从下方素材栏拖入图片 / Drag images from the dock below</div>`
      }
    </div>
  `;
}

function renderBoardFilters(assets) {
  const sceneFilter = $("boardSceneFilter");
  const tagFilter = $("boardTagFilter");
  const search = $("boardSearchInput");
  if (!sceneFilter || !tagFilter || !search) return;
  sceneFilter.innerHTML = boardSceneFilterOptions(assets)
    .map((option) => `<option value="${escapeHtml(option.value)}" ${state.boardFilters.scene === option.value ? "selected" : ""}>${escapeHtml(option.label)}</option>`)
    .join("");
  tagFilter.innerHTML = BOARD_TAG_OPTIONS.map(
    (option) => `<option value="${escapeHtml(option.value)}" ${state.boardFilters.tag === option.value ? "selected" : ""}>${escapeHtml(option.label)}</option>`,
  ).join("");
  search.value = state.boardFilters.query || "";
}

function renderBoardAssetTray() {
  const tray = $("boardAssetTray");
  if (!tray) return;
  const assets = allBoardImageAssets();
  renderBoardFilters(assets);
  const visible = assets.filter(boardAssetMatches).slice(0, 160);
  tray.innerHTML = visible.length
    ? visible
        .map(
          (asset) => `
            <article class="board-asset-card" data-ref="${escapeHtml(asset.ref)}" title="${escapeHtml(asset.path || "")}">
              <img src="${escapeHtml(asset.url)}" alt="${escapeHtml(asset.asset_id || asset.path)}" draggable="false" />
              <strong>${escapeHtml(asset.asset_id || asset.role || asset.path)}</strong>
              <small>${escapeHtml(asset.scene_id || "PROJECT")} · ${escapeHtml(kindLabel(asset.kind))}</small>
            </article>
          `,
        )
        .join("")
    : `<div class="empty-state">没有匹配图片 / No matching images.</div>`;
}

function bindBoardNodeDrag() {
  $("referenceBoardCanvas")?.querySelectorAll(".board-node-card").forEach((card) => {
    card.addEventListener("pointerdown", (event) => {
      if (event.target?.closest?.("button, input, select, textarea, a, .board-node-image")) return;
      const nodeId = card.dataset.nodeId || "";
      const node = state.boardNodes.find((item) => item.id === nodeId);
      const stage = $("referenceBoardCanvas")?.querySelector(".board-canvas-stage");
      if (!node || !stage) return;
      event.preventDefault();
      card.setPointerCapture?.(event.pointerId);
      const startX = event.clientX;
      const startY = event.clientY;
      const originalX = Number(node.x || 0);
      const originalY = Number(node.y || 0);
      const maxX = Math.max(12, stage.scrollWidth - 300);
      const maxY = Math.max(12, stage.scrollHeight - 320);
      const onMove = (moveEvent) => {
        node.x = Math.round(clamp(originalX + moveEvent.clientX - startX, 12, maxX));
        node.y = Math.round(clamp(originalY + moveEvent.clientY - startY, 12, maxY));
        card.style.left = `${node.x}px`;
        card.style.top = `${node.y}px`;
      };
      const onUp = () => {
        document.removeEventListener("pointermove", onMove);
        document.removeEventListener("pointerup", onUp);
        saveBoardState();
        renderReferenceBoard();
      };
      document.addEventListener("pointermove", onMove);
      document.addEventListener("pointerup", onUp);
    });
  });
}

function bindBoardAssetTrayEvents() {
  $("boardAssetTray")?.querySelectorAll(".board-asset-card").forEach((card) => {
    card.addEventListener("pointerdown", (event) => {
      if (event.button !== 0) return;
      const ref = card.dataset.ref || "";
      const startX = event.clientX;
      const startY = event.clientY;
      let dragging = false;
      let ghost = null;
      const onMove = (moveEvent) => {
        const moved = Math.hypot(moveEvent.clientX - startX, moveEvent.clientY - startY);
        if (!dragging && moved < 8) return;
        if (!dragging) {
          dragging = true;
          ghost = card.cloneNode(true);
          ghost.classList.add("board-drag-ghost");
          document.body.appendChild(ghost);
          document.body.classList.add("board-dragging");
        }
        if (ghost) {
          ghost.style.left = `${moveEvent.clientX}px`;
          ghost.style.top = `${moveEvent.clientY}px`;
        }
      };
      const onUp = (upEvent) => {
        document.removeEventListener("pointermove", onMove);
        document.removeEventListener("pointerup", onUp);
        ghost?.remove();
        document.body.classList.remove("board-dragging");
        if (!dragging) return;
        const canvas = $("referenceBoardCanvas");
        const rect = canvas?.getBoundingClientRect();
        const insideCanvas =
          rect &&
          upEvent.clientX >= rect.left &&
          upEvent.clientX <= rect.right &&
          upEvent.clientY >= rect.top &&
          upEvent.clientY <= rect.bottom;
        if (insideCanvas) addBoardNode(ref, boardCanvasPoint(upEvent));
      };
      document.addEventListener("pointermove", onMove);
      document.addEventListener("pointerup", onUp);
    });
    card.addEventListener("dblclick", () => addBoardNode(card.dataset.ref || "", boardDefaultNodePoint()));
  });
}

function bindReferenceBoardEvents() {
  bindBoardAssetTrayEvents();
  const sceneFilter = $("boardSceneFilter");
  if (sceneFilter) sceneFilter.onchange = (event) => {
    state.boardFilters.scene = event.target.value;
    renderReferenceBoard();
  };
  const tagFilter = $("boardTagFilter");
  if (tagFilter) tagFilter.onchange = (event) => {
    state.boardFilters.tag = event.target.value;
    renderReferenceBoard();
  };
  const searchInput = $("boardSearchInput");
  if (searchInput) searchInput.oninput = (event) => {
    state.boardFilters.query = event.target.value;
    renderBoardAssetTray();
    bindBoardAssetTrayEvents();
  };
  $("referenceBoardCanvas")?.querySelectorAll(".board-node-role").forEach((select) => {
    select.addEventListener("change", () => {
      const node = state.boardNodes.find((item) => item.id === select.dataset.nodeId);
      if (node) node.role = select.value === "main" ? "main" : "reference";
      saveBoardState();
      renderReferenceBoard();
    });
  });
  $("referenceBoardCanvas")?.querySelectorAll(".board-node-note").forEach((textarea) => {
    textarea.addEventListener("input", () => {
      const node = state.boardNodes.find((item) => item.id === textarea.dataset.nodeId);
      if (node) node.note = textarea.value;
      saveBoardState();
    });
  });
  $("referenceBoardCanvas")?.querySelectorAll(".board-edge-note").forEach((textarea) => {
    textarea.addEventListener("input", () => {
      const edge = state.boardEdges.find((item) => item.id === textarea.dataset.edgeId);
      if (edge) edge.note = textarea.value;
      saveBoardState();
    });
  });
  const canvas = $("referenceBoardCanvas");
  if (canvas) {
    canvas.ondblclick = (event) => {
      const image = event.target?.closest?.(".board-node-image");
      if (!image) return;
      event.preventDefault();
      openBoardImageLightbox(image.dataset.nodeId || "");
    };
    canvas.onclick = (event) => {
      const sourceButton = event.target?.closest?.(".board-link-source");
      if (sourceButton) {
        event.preventDefault();
        state.boardLinkSourceId = state.boardLinkSourceId === sourceButton.dataset.nodeId ? "" : sourceButton.dataset.nodeId || "";
        renderReferenceBoard();
        return;
      }
      const targetButton = event.target?.closest?.(".board-link-target");
      if (targetButton) {
        event.preventDefault();
        createBoardEdge(state.boardLinkSourceId, targetButton.dataset.nodeId || "");
        return;
      }
      const removeButton = event.target?.closest?.(".board-node-remove");
      if (removeButton) {
        event.preventDefault();
        removeBoardNode(removeButton.dataset.nodeId || "");
        return;
      }
      const generateButton = event.target?.closest?.(".board-generate-node");
      if (generateButton) {
        event.preventDefault();
        createBoardGenerationPacket(generateButton.dataset.nodeId || "");
      }
    };
  }
  bindBoardNodeDrag();
}

function renderReferenceBoard() {
  const modal = $("referenceBoardModal");
  if (!modal) return;
  modal.hidden = !state.boardOpen;
  document.body.classList.toggle("board-open", state.boardOpen);
  if (!state.boardOpen) return;
  renderBoardCanvas();
  renderBoardAssetTray();
  bindReferenceBoardEvents();
}

function openReferenceBoard() {
  if (!state.detail) {
    toast("请先选择项目 / Select a project first");
    return;
  }
  state.boardOpen = true;
  loadBoardState();
  renderReferenceBoard();
}

function closeReferenceBoard() {
  state.boardOpen = false;
  state.boardLinkSourceId = "";
  renderReferenceBoard();
}

function clearReferenceBoard() {
  state.boardNodes = [];
  state.boardEdges = [];
  state.boardLinkSourceId = "";
  saveBoardState();
  renderReferenceBoard();
}

function baseFixPrompt(scene, frame, qa = null) {
  const note = $("storyboardDirectorNote")?.value.trim() || annotationForRef(frame?.ref || "").note || "";
  const selectedRefs = relatedFrameAssets(scene, frame).filter((asset) => referenceSelectionFor(frame.ref, asset.ref).selected);
  const referenceText = selectedRefs
    .map((asset) => {
      const refState = referenceSelectionFor(frame.ref, asset.ref);
      return `- ${asset.asset_id || asset.role || asset.path}: ${refState.note || "参考其造型、空间或风格 / use as visual reference"}`;
    })
    .join("\n");
  const qaText = qa?.suggestions?.length ? qa.suggestions.map((item) => `- ${item}`).join("\n") : "- clean high-resolution image, no film grain, no dirty texture, crisp edges";
  return [
    `Scene / 场戏: ${scene?.scene_id || ""} ${scene?.title || ""}`,
    `Frame / 图片: ${frameTitle(frame)}`,
    `Current stage / 当前步骤: ${frame?.stage || ""} ${stageShortLabel(frame?.stage || "")}`,
    "",
    "Director note / 导演修改意见:",
    note || "- 保留剧情意图，提升图片质量与可读性 / keep story intent, improve image quality and readability",
    "",
    "Technical fixes / 技术修正:",
    qaText,
    "",
    "Reference stack / 关联参考:",
    referenceText || "- 使用当前场戏已标记为参考的角色、场景、白模和提示词 / use selected scene references",
    "",
    "Output goal / 输出目标:",
    "- Generate a clean, stable, high-quality key image suitable for downstream video AIGC.",
    "- Preserve the story beat, spatial relation, character identity, and shot intent.",
    "- Avoid noise, muddy shadows, distorted hands/faces, unreadable composition, text, watermark, and random new objects.",
  ].join("\n");
}

function scoreClass(score) {
  if (score >= 82) return "ok";
  if (score >= 68) return "warn";
  return "danger";
}

function clamp(value, min, max) {
  return Math.max(min, Math.min(max, value));
}

function analyzeImageElement(img) {
  const size = 128;
  const canvas = document.createElement("canvas");
  canvas.width = size;
  canvas.height = size;
  const ctx = canvas.getContext("2d", { willReadFrequently: true });
  ctx.drawImage(img, 0, 0, size, size);
  const data = ctx.getImageData(0, 0, size, size).data;
  const luminance = [];
  let satSum = 0;
  let dark = 0;
  let bright = 0;
  for (let i = 0; i < data.length; i += 4) {
    const r = data[i];
    const g = data[i + 1];
    const b = data[i + 2];
    const max = Math.max(r, g, b);
    const min = Math.min(r, g, b);
    const lum = 0.2126 * r + 0.7152 * g + 0.0722 * b;
    luminance.push(lum);
    satSum += max ? (max - min) / max : 0;
    if (lum < 35) dark += 1;
    if (lum > 235) bright += 1;
  }
  const mean = luminance.reduce((sum, value) => sum + value, 0) / luminance.length;
  const variance = luminance.reduce((sum, value) => sum + (value - mean) ** 2, 0) / luminance.length;
  const contrast = Math.sqrt(variance);
  let edge = 0;
  let highFreq = 0;
  let samples = 0;
  for (let y = 1; y < size - 1; y += 1) {
    for (let x = 1; x < size - 1; x += 1) {
      const index = y * size + x;
      const dx = Math.abs(luminance[index] - luminance[index + 1]);
      const dy = Math.abs(luminance[index] - luminance[index + size]);
      edge += dx + dy;
      highFreq += Math.abs(luminance[index] * 4 - luminance[index - 1] - luminance[index + 1] - luminance[index - size] - luminance[index + size]);
      samples += 1;
    }
  }
  edge /= samples * 2;
  highFreq /= samples;
  const darkRatio = dark / luminance.length;
  const brightRatio = bright / luminance.length;
  const saturation = satSum / luminance.length;
  const exposureScore = clamp(100 - Math.abs(mean - 118) * 0.55 - darkRatio * 35 - brightRatio * 30, 0, 100);
  const contrastScore = clamp(100 - Math.abs(contrast - 52) * 1.25, 0, 100);
  const sharpnessScore = clamp(edge * 5.3, 0, 100);
  const noiseScore = clamp(100 - Math.max(0, highFreq - edge * 1.8) * 1.9, 0, 100);
  const score = Math.round(exposureScore * 0.25 + contrastScore * 0.2 + sharpnessScore * 0.25 + noiseScore * 0.3);
  const suggestions = [];
  if (noiseScore < 72) suggestions.push("疑似高频噪点或脏纹偏多：提示词加入 no film grain, no sensor noise, clean smooth surfaces。");
  if (sharpnessScore < 66) suggestions.push("边缘清晰度偏弱：强调 crisp edges, sharp focal subject, high-resolution keyframe。");
  if (mean < 70 || darkRatio > 0.42) suggestions.push("暗部比例偏高：减少 gritty/dark/moody，改成 controlled soft lighting。");
  if (brightRatio > 0.12) suggestions.push("高光可能过曝：加入 balanced highlights, no blown-out light。");
  if (contrastScore < 70) suggestions.push("对比度不够稳定：要求 clean value separation, readable silhouette。");
  if (saturation > 0.48) suggestions.push("色彩可能过饱和：加入 restrained palette, natural material color。");
  if (!suggestions.length) suggestions.push("技术状态可用：下一步重点检查角色一致性、剧情匹配和导演审美。");
  return {
    score,
    exposureScore: Math.round(exposureScore),
    contrastScore: Math.round(contrastScore),
    sharpnessScore: Math.round(sharpnessScore),
    noiseScore: Math.round(noiseScore),
    mean: Math.round(mean),
    contrast: Math.round(contrast),
    darkRatio: Math.round(darkRatio * 100),
    brightRatio: Math.round(brightRatio * 100),
    saturation: Math.round(saturation * 100),
    edge: Math.round(edge),
    highFrequency: Math.round(highFreq),
    formula: "总分 = 曝光 25% + 对比 20% + 清晰 25% + 噪点 30%",
    sample: "浏览器端 128x128 采样估算 / browser-side 128x128 sampled estimate",
    suggestions,
  };
}

function currentQaResult() {
  try {
    return JSON.parse($("imageQaPanel")?.dataset.qa || "null");
  } catch {
    return null;
  }
}

function repairDirectiveFor(key, result = null) {
  const intent = QA_REPAIR_INTENTS[key] || QA_REPAIR_INTENTS.denoise;
  const qa = result
    ? `Current QA: score ${result.score}/100, sharpness ${result.sharpnessScore}, noise ${result.noiseScore}, exposure ${result.exposureScore}, contrast ${result.contrastScore}.`
    : "";
  return `${intent.directive}\n${qa}`.trim();
}

function qaRepairButtons(result) {
  const recommended = new Set();
  if ((result?.noiseScore ?? 100) < 72) recommended.add("denoise");
  if ((result?.sharpnessScore ?? 100) < 66) recommended.add("sharpen");
  if ((result?.mean ?? 118) < 70 || (result?.darkRatio ?? 0) > 42) recommended.add("relight");
  if ((result?.brightRatio ?? 0) > 12) recommended.add("highlights");
  if ((result?.contrastScore ?? 100) < 70) recommended.add("contrast");
  if ((result?.saturation ?? 0) > 48) recommended.add("palette");
  return Object.entries(QA_REPAIR_INTENTS)
    .map(
      ([key, intent]) => `
        <button class="qa-repair-button ${recommended.has(key) ? "recommended" : ""}" data-repair-key="${escapeHtml(key)}" type="button">
          ${escapeHtml(intent.label)}
        </button>
      `,
    )
    .join("");
}

function renderQaResult(result) {
  const node = $("imageQaPanel");
  if (!node) return;
  const cls = scoreClass(result.score);
  node.innerHTML = `
    <div class="qa-score ${cls}">
      <strong>${result.score}</strong>
      <span>/100 技术分 / technical</span>
    </div>
    <div class="qa-bars">
      <span>清晰 ${result.sharpnessScore}</span>
      <span>噪点 ${result.noiseScore}</span>
      <span>曝光 ${result.exposureScore}</span>
      <span>对比 ${result.contrastScore}</span>
    </div>
    <ul>${result.suggestions.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}</ul>
    <details class="qa-basis">
      <summary>技术分依据 / Scoring basis</summary>
      <p>${escapeHtml(result.formula)}</p>
      <p>${escapeHtml(result.sample)}</p>
      <dl>
        <div><dt>平均亮度 / Mean luminance</dt><dd>${result.mean}</dd></div>
        <div><dt>暗部比例 / Dark area</dt><dd>${result.darkRatio}%</dd></div>
        <div><dt>高光比例 / Bright area</dt><dd>${result.brightRatio}%</dd></div>
        <div><dt>饱和度 / Saturation</dt><dd>${result.saturation}%</dd></div>
        <div><dt>边缘强度 / Edge</dt><dd>${result.edge}</dd></div>
        <div><dt>高频纹理 / High frequency</dt><dd>${result.highFrequency}</dd></div>
      </dl>
    </details>
    <div class="qa-repair-actions">
      <strong>快捷修复 / Quick repair</strong>
      <div>${qaRepairButtons(result)}</div>
    </div>
  `;
  node.dataset.qa = JSON.stringify(result);
}

function analyzeCurrentStoryboardImage() {
  const img = $("storyboardMainImage");
  const panel = $("imageQaPanel");
  if (!panel) return;
  if (!img) {
    panel.innerHTML = `<div class="empty-state">当前页没有可质检图片 / No image to inspect.</div>`;
    return;
  }
  panel.innerHTML = `<div class="qa-loading">正在估算清晰度、噪点、曝光和对比 / Checking sharpness, noise, exposure, and contrast...</div>`;
  const run = () => {
    try {
      renderQaResult(analyzeImageElement(img));
    } catch (error) {
      panel.innerHTML = `<div class="empty-state">质检失败 / QA failed: ${escapeHtml(error.message)}</div>`;
    }
  };
  if (img.complete && img.naturalWidth) {
    window.setTimeout(run, 60);
  } else {
    img.addEventListener("load", run, { once: true });
    img.addEventListener("error", () => {
      panel.innerHTML = `<div class="empty-state">图片未能加载，无法质检 / Image failed to load.</div>`;
    }, { once: true });
  }
}

function renderStoryboardStudio() {
  const root = $("storyboardStudio");
  if (!root) return;
  const scenes = state.detail?.scene_workbench?.scenes || [];
  if (!state.detail) {
    root.innerHTML = `<div class="empty-state">请选择项目 / Select a project.</div>`;
    return;
  }
  if (!scenes.length) {
    root.innerHTML = `<div class="empty-state">还没有幕/场戏清单 / No act or scene manifest yet.</div>`;
    return;
  }
  const scene = selectedScene();
  const stageOptions = storyboardStageOptions(scene);
  if (!stageOptions.some((option) => option.value === state.storyboardStage)) state.storyboardStage = "all";
  const { frame, frames } = selectedStoryboardFrame(scene);
  const annotation = frame ? annotationForRef(frame.ref) : {};
  const related = relatedFrameAssets(scene, frame);
  const versions = frameVersions(scene, frame);
  const frameRequests = storyboardRequestsForFrame(scene, frame);
  const frameIndex = frame ? frames.findIndex((item) => item.ref === frame.ref) : -1;
  root.innerHTML = `
    <div class="studio-header">
      <div>
        <p class="eyebrow">Storyboard Studio</p>
        <h3>按幕制作图片页 / Act-based image workspace</h3>
      </div>
      <div class="studio-status">
        <span>${escapeHtml(scene?.act_title || "")}</span>
        <strong>${escapeHtml(scene?.title || scene?.scene_id || "")}</strong>
        <small class="frame-count">${frameIndex + 1 > 0 ? frameIndex + 1 : 0}/${frames.length} 图片页 / frames</small>
      </div>
    </div>
    <div class="studio-layout">
      <section class="studio-stage">
        <div class="studio-filter-tabs">
          ${stageOptions
            .map((option) => `<button class="studio-stage-filter ${state.storyboardStage === option.value ? "active" : ""}" data-stage="${escapeHtml(option.value)}" type="button">${escapeHtml(option.label)}</button>`)
            .join("")}
        </div>
        ${
          frame
            ? `
              <figure class="frame-hero ${escapeHtml(decisionClass(annotation.status || ""))}">
                <div class="frame-image-wrap">
                  ${
                    frameIsUsable(frame)
                      ? `<img id="storyboardMainImage" src="${escapeHtml(frame.url)}" alt="${escapeHtml(frameTitle(frame))}" />`
                      : renderLfsPlaceholder(frame.lfs_missing ? "原图未下载 / source missing" : "不可预览 / no preview")
                  }
                </div>
                <figcaption>
                  <strong>${escapeHtml(frameTitle(frame))}</strong>
                  <span>${escapeHtml(frame.stage)} · ${escapeHtml(kindLabel(frame.kind))} · ${escapeHtml(frame.path || "")}</span>
                </figcaption>
              </figure>
              <div id="imageQaPanel" class="image-qa-panel"></div>
              <div class="frame-strip">
                ${frames
                  .map(
                    (item, index) => `
                      <button class="frame-thumb ${item.ref === frame.ref ? "active" : ""} ${frameIsUsable(item) ? "" : "missing"}" data-ref="${escapeHtml(item.ref)}" type="button" title="${escapeHtml(item.path)}">
                        ${frameIsUsable(item) ? `<img src="${escapeHtml(item.url)}" alt="${escapeHtml(item.asset_id || item.role || item.path)}" loading="lazy" />` : `<em>缺失</em>`}
                        <span>${index + 1}</span>
                      </button>
                    `,
                  )
                  .join("")}
              </div>
            `
            : `<div class="empty-state">当前场戏还没有图片页 / This scene has no image frames yet.</div>`
        }
      </section>
      <aside class="studio-inspector">
        ${
          frame
            ? `
              <section class="inspector-block">
                <h4>当前图片 / Current Frame</h4>
                <dl>
                  <div><dt>场戏</dt><dd>${escapeHtml(scene.scene_id)} · ${escapeHtml(scene.title || "")}</dd></div>
                  <div><dt>镜头</dt><dd>${escapeHtml(frame.shot_id || "未绑定 / unbound")}</dd></div>
                  <div><dt>步骤</dt><dd>${escapeHtml(frame.stage)} · ${escapeHtml(stageShortLabel(frame.stage))}</dd></div>
                  <div><dt>类别</dt><dd>${escapeHtml(kindLabel(frame.kind))}</dd></div>
                </dl>
                <div class="frame-actions" data-ref="${escapeHtml(frame.ref)}">
                  <button class="decision-button use ${annotation.status === "use" ? "active" : ""}" data-status="use" type="button">✓</button>
                  <button class="decision-button reject ${annotation.status === "reject" ? "active" : ""}" data-status="reject" type="button">×</button>
                  <a class="open-resource-link" href="${escapeHtml(frame.url)}" target="_blank">打开原图 / Open</a>
                </div>
                <label>导演备注 / Director note
                  <textarea id="storyboardDirectorNote" rows="4" placeholder="这张图哪里好、哪里要改 / What works and what should change">${escapeHtml(annotation.note || "")}</textarea>
                </label>
              </section>
              <section class="inspector-block">
                <h4>关联素材 / Reference Stack</h4>
                <div class="reference-stack">
                  ${
                    related.length
                      ? related
                          .map((asset) => {
                            const refState = referenceSelectionFor(frame.ref, asset.ref);
                            return `
                              <div class="reference-item" data-ref="${escapeHtml(asset.ref)}">
                                <label class="checkbox-label">
                                  <input class="reference-checkbox" type="checkbox" ${refState.selected ? "checked" : ""} />
                                  <span>${escapeHtml(asset.asset_id || asset.role || asset.path)}</span>
                                </label>
                                <small>${escapeHtml(asset.stage)} · ${escapeHtml(kindLabel(asset.kind))}</small>
                                <small class="reference-open-hint">双击预览 / Double-click to preview</small>
                                <input class="reference-note-input" value="${escapeHtml(refState.note || "")}" placeholder="怎么参考它 / how to use this reference" />
                              </div>
                            `;
                          })
                          .join("")
                      : `<div class="empty-state">暂无关联素材 / No related assets.</div>`
                  }
                </div>
              </section>
              <section class="inspector-block">
                <h4>修正版提示词 / Fix Prompt</h4>
                <button id="buildFixPromptBtn" class="command-button primary" type="button">生成修正版提示词 / Build Fix Prompt</button>
                <textarea id="fixPromptOutput" rows="9" placeholder="点击上方按钮生成 / Click the button above"></textarea>
                <button id="createFramePacketBtn" class="command-button primary" type="button">生成任务包 / Build Generation Packet</button>
                <button id="createFrameChangeRequestBtn" class="command-button" type="button">仅写入影响表 / Impact Only</button>
              </section>
              <section class="inspector-block">
                <h4>任务包 / Packets</h4>
                <div class="request-list-mini">
                  ${
                    frameRequests.length
                      ? frameRequests
                          .map((request) => {
                            const queue = Array.isArray(request.generation_queue) ? request.generation_queue : [];
                            return `
                              <div>
                                <strong>${escapeHtml(request.change_request_id || "")}</strong>
                                <span>${escapeHtml(request.status || "")} · ${queue.length} queue</span>
                                ${queue
                                  .map(
                                    (item) => `
                                      <small>
                                        ${escapeHtml(item.asset_id || item.queue_id || "")} · ${escapeHtml(item.target_version || "")} · ${escapeHtml(item.status || "")}
                                        ${scenePathLink(item.result_path || item.packet_path, "任务包 / Packet")}
                                      </small>
                                    `,
                                  )
                                  .join("")}
                              </div>
                            `;
                          })
                          .join("")
                      : `<div class="empty-state">还没有从当前图片生成任务包 / No packet from this frame yet.</div>`
                  }
                </div>
              </section>
              <section class="inspector-block">
                <h4>版本 / Versions</h4>
                <div class="version-list-mini">
                  ${
                    versions.length
                      ? versions
                          .map((version) => `<div><strong>${escapeHtml(version.version || "")}</strong><span>${escapeHtml(version.status || "")}</span><small>${escapeHtml(version.final_output_path || version.output_path || "")}</small></div>`)
                          .join("")
                      : `<div class="empty-state">还没有版本记录 / No version records yet.</div>`
                  }
                </div>
              </section>
            `
            : `<div class="empty-state">选择一张图片查看提示词、关联素材和质检 / Select an image to inspect prompts, references, and QA.</div>`
        }
      </aside>
    </div>
  `;
  bindStoryboardStudioEvents(scene, frame, related);
  analyzeCurrentStoryboardImage();
}

function bindStoryboardStudioEvents(scene, frame, related = []) {
  const root = $("storyboardStudio");
  root.querySelectorAll(".studio-scene-button").forEach((button) => {
    button.addEventListener("click", () => {
      state.selectedSceneId = button.dataset.sceneId || "";
      state.selectedFrameRef = "";
      state.activeChangeRequest = null;
      state.recreate = null;
      renderAll();
    });
  });
  root.querySelectorAll(".studio-stage-filter").forEach((button) => {
    button.addEventListener("click", () => {
      state.storyboardStage = button.dataset.stage || "all";
      state.selectedFrameRef = "";
      renderStoryboardStudio();
    });
  });
  root.querySelectorAll(".frame-thumb").forEach((button) => {
    button.addEventListener("click", () => {
      state.selectedFrameRef = button.dataset.ref || "";
      renderStoryboardStudio();
    });
  });
  root.querySelectorAll(".frame-actions .decision-button").forEach((button) => {
    button.addEventListener("click", async () => {
      if (!frame) return;
      const current = annotationForRef(frame.ref);
      const nextStatus = current.status === button.dataset.status ? "" : button.dataset.status;
      const note = $("storyboardDirectorNote")?.value || current.note || "";
      await saveResourceAnnotation(frame.ref, { status: nextStatus, note });
    });
  });
  const note = $("storyboardDirectorNote");
  if (note && frame) {
    const saveNote = async (showToast = false) => {
      const current = annotationForRef(frame.ref);
      await saveResourceAnnotation(frame.ref, { status: current.status || "", note: note.value }, { rerender: false, toast: false });
      if (showToast) toast("导演备注已保存 / Director note saved");
    };
    note.addEventListener("input", () => {
      clearTimeout(note._saveTimer);
      note._saveTimer = setTimeout(() => saveNote(false).catch((error) => toast(`备注保存失败 / Note save failed: ${error.message}`)), 650);
    });
    note.addEventListener("blur", async () => {
      clearTimeout(note._saveTimer);
      await saveNote(true);
    });
  }
  root.querySelectorAll(".reference-item").forEach((item) => {
    const ref = item.dataset.ref || "";
    const checkbox = item.querySelector(".reference-checkbox");
    const input = item.querySelector(".reference-note-input");
    const asset = related.find((candidate) => candidate.ref === ref);
    item.addEventListener("dblclick", (event) => {
      if (event.target?.closest?.("input, textarea, button, a")) return;
      if (asset) openAssetPreview(asset);
    });
    checkbox?.addEventListener("change", () => setReferenceSelection(frame?.ref || "", ref, { selected: checkbox.checked }));
    input?.addEventListener("input", () => setReferenceSelection(frame?.ref || "", ref, { note: input.value }));
  });
  if (root._qaRepairHandler) root.removeEventListener("click", root._qaRepairHandler);
  root._qaRepairHandler = async (event) => {
    const button = event.target?.closest?.(".qa-repair-button");
    if (!button || !frame) return;
    const key = button.dataset.repairKey || "denoise";
    const intent = QA_REPAIR_INTENTS[key] || QA_REPAIR_INTENTS.denoise;
    await createStoryboardGenerationPacket(scene, frame, `Quick repair / 快捷修复: ${intent.label}\n${repairDirectiveFor(key, currentQaResult())}`);
  };
  root.addEventListener("click", root._qaRepairHandler);
  $("buildFixPromptBtn")?.addEventListener("click", () => {
    if (!frame) return;
    $("fixPromptOutput").value = baseFixPrompt(scene, frame, currentQaResult());
  });
  $("createFramePacketBtn")?.addEventListener("click", async () => {
    if (!scene || !frame) return;
    await createStoryboardGenerationPacket(scene, frame);
  });
  $("createFrameChangeRequestBtn")?.addEventListener("click", async () => {
    if (!scene || !frame) return;
    const creativeDirection = $("fixPromptOutput")?.value.trim() || baseFixPrompt(scene, frame);
    await runAction("再生成请求 / Re-generation request", async () => {
      const result = await requestJson(`/api/projects/${state.selectedSlug}/scene-change-request`, {
        method: "POST",
        body: JSON.stringify({
          scene_id: scene.scene_id,
          trigger_step: frame.stage,
          trigger_asset_id: frame.asset_id || "",
          creative_direction: creativeDirection,
        }),
      });
      state.detail = result.project || state.detail;
      state.activeChangeRequest = result.change_request || null;
      state.recreate = null;
      renderAll();
    });
  });
}

async function createStoryboardGenerationPacket(scene, frame, repairIntent = "") {
  const promptOutput = $("fixPromptOutput");
  const baseDirection = promptOutput?.value.trim() || baseFixPrompt(scene, frame, currentQaResult());
  const creativeDirection = repairIntent ? `${baseDirection}\n\n${repairIntent}` : baseDirection;
  if (promptOutput) promptOutput.value = creativeDirection;
  await runAction("当前图片任务包 / Frame packet", async () => {
    const changeResult = await requestJson(`/api/projects/${state.selectedSlug}/scene-change-request`, {
      method: "POST",
      body: JSON.stringify({
        scene_id: scene.scene_id,
        trigger_step: frame.stage,
        trigger_asset_id: frame.asset_id || "",
        creative_direction: creativeDirection,
      }),
    });
    const request = changeResult.change_request || {};
    const selectedImpacts = selectedQueueableImpacts(request);
    if (!selectedImpacts.length) {
      state.detail = changeResult.project || state.detail;
      state.activeChangeRequest = request;
      renderAll();
      throw new Error("没有可入队的当前图片资产 / No queueable frame asset.");
    }
    const selectedImpactIds = selectedImpacts.map((impact) => impact.impact_id);
    const actionOverrides = Object.fromEntries(selectedImpacts.map((impact) => [impact.impact_id, impact.action]));
    const queueResult = await requestJson(`/api/projects/${state.selectedSlug}/scene-generate`, {
      method: "POST",
      body: JSON.stringify({
        change_request_id: request.change_request_id,
        selected_impact_ids: selectedImpactIds,
        action_overrides: actionOverrides,
        notes: repairIntent ? `Storyboard Studio quick repair for ${frameTitle(frame)}` : `Storyboard Studio packet for ${frameTitle(frame)}`,
      }),
    });
    const runResult = await requestJson(`/api/projects/${state.selectedSlug}/scene-run-generation`, {
      method: "POST",
      body: JSON.stringify({
        change_request_id: request.change_request_id,
        adapter_id: "manual_packet",
      }),
    });
    state.detail = runResult.project || queueResult.project || changeResult.project || state.detail;
    state.activeChangeRequest = runResult.change_request || queueResult.change_request || request;
    state.recreate = null;
    renderAll();
  });
}

function changeRequestSummary(request) {
  const impacts = request.impact_table || [];
  const queueable = impacts.filter(queueableImpact).length;
  const selected = impacts.filter((impact) => impact.selected && queueableImpact(impact)).length;
  const sample = isExampleChangeRequest(request) ? " · 样板 / example" : "";
  return `${escapeHtml(request.trigger_step || "")} · ${selected}/${queueable} 新增/修改 / create or modify · ${escapeHtml(request.status || "")}${sample}`;
}

function renderSceneTree(scenes) {
  const grouped = new Map();
  scenes.forEach((scene) => {
    const key = `${scene.act_id || "ACT"}|${scene.act_title || "未分幕 / No act"}`;
    if (!grouped.has(key)) grouped.set(key, []);
    grouped.get(key).push(scene);
  });
  $("sceneTree").innerHTML = [...grouped.entries()]
    .map(([key, actScenes]) => {
      const [, actTitle] = key.split("|");
      return `
        <div class="scene-act-group">
          <strong>${escapeHtml(actTitle)}</strong>
          ${actScenes
            .map(
              (scene) => `
                <button class="scene-tree-item ${scene.scene_id === state.selectedSceneId ? "active" : ""}" data-scene-id="${escapeHtml(scene.scene_id)}" type="button">
                  <span>${escapeHtml(scene.title || scene.scene_id)}</span>
                  <small>${escapeHtml(scene.scene_id)} · ${(scene.shot_ids || []).length} 镜头 / shots · ${escapeHtml(sceneStatusLabel(scene.status))}</small>
                </button>
              `,
            )
            .join("")}
        </div>
      `;
    })
    .join("");
  $("sceneTree").querySelectorAll(".scene-tree-item").forEach((button) => {
    button.addEventListener("click", () => {
      state.selectedSceneId = button.dataset.sceneId || "";
      state.selectedFrameRef = "";
      state.activeChangeRequest = null;
      state.recreate = null;
      renderAll();
    });
  });
}

function sceneAssetMatches(asset, step) {
  const annotation = annotationForRef(sceneAssetRef(asset));
  const status = annotation.status || "";
  const query = state.sceneFilters.query.trim().toLowerCase();
  const kind = sceneAssetKind(asset, step);
  if (state.sceneFilters.step !== "all" && step !== state.sceneFilters.step) return false;
  if (state.sceneFilters.kind !== "all" && kind !== state.sceneFilters.kind) return false;
  if (state.sceneFilters.decision === "use" && status !== "use") return false;
  if (state.sceneFilters.decision === "reject" && status !== "reject") return false;
  if (state.sceneFilters.decision === "unset" && status) return false;
  if (!query) return true;
  return [asset.asset_id, asset.role, asset.path, kindLabel(kind), annotation.note].join(" ").toLowerCase().includes(query);
}

function renderSceneAsset(asset, step) {
  const ref = sceneAssetRef(asset);
  const annotation = annotationForRef(ref);
  const status = annotation.status || "";
  const note = annotation.note || "";
  const kind = sceneAssetKind(asset, step);
  return `
    <div class="scene-asset-row ${escapeHtml(decisionClass(status))}" data-ref="${escapeHtml(ref)}">
      <span class="scene-asset-main">
        <strong>${escapeHtml(asset.asset_id || asset.role || "asset")}</strong>
        <small>${escapeHtml(step)} · ${escapeHtml(kindLabel(kind))} · ${escapeHtml(asset.role || "资源 / asset")} · ${escapeHtml(asset.path || "")}</small>
      </span>
      <span class="scene-asset-actions">
        <button class="decision-button use ${status === "use" ? "active" : ""}" data-status="use" type="button" title="标为后续参考 / Mark as reference">✓</button>
        <button class="decision-button reject ${status === "reject" ? "active" : ""}" data-status="reject" type="button" title="标为不使用 / Mark as rejected">×</button>
        ${sceneAssetLink(asset)}
      </span>
      <textarea class="scene-asset-note" data-ref="${escapeHtml(ref)}" rows="2" placeholder="备注：这份资源哪里好 / 哪里要改 / Note: what works and what should change">${escapeHtml(note)}</textarea>
    </div>
  `;
}

function renderSceneLoopPanel(scene, versions, changeRequests) {
  const queue = scene?.generation_queue || [];
  const reviews = scene?.review_log?.reviews || [];
  const snapshots = scene?.snapshots || [];
  const latestVersions = versions.slice().reverse().slice(0, 8);
  const latestRequests = changeRequests.slice(0, 6);
  const latestQueue = queue.slice(0, 8);
  const latestSnapshots = snapshots.slice(0, 5);
  return `
    <section class="scene-loop-panel">
      <form id="sceneStatusForm" class="scene-status-form">
        <label>场戏状态 / Scene status
          <select id="sceneStatusSelect">
            ${Object.entries(SCENE_STATUS_LABELS)
              .map(([value, label]) => `<option value="${escapeHtml(value)}" ${scene?.status === value ? "selected" : ""}>${escapeHtml(label)}</option>`)
              .join("")}
          </select>
        </label>
        <label>审片备注 / Review note
          <textarea id="sceneStatusNotes" rows="2" placeholder="这一场当前哪里通过，哪里还要改 / What passes and what still needs work"></textarea>
        </label>
        <button class="command-button" type="submit">记录状态 / Save status</button>
      </form>
      <div class="scene-loop-columns">
        <section>
          <h4>变更请求 / Change Requests</h4>
          ${
            latestRequests.length
              ? latestRequests
                  .map(
                    (request) => `
                      <button class="scene-request-button ${state.activeChangeRequest?.change_request_id === request.change_request_id ? "active" : ""}" data-change-request-id="${escapeHtml(request.change_request_id)}" type="button">
                        <strong>${escapeHtml(request.change_request_id)}</strong>
                        <span>${changeRequestSummary(request)}</span>
                      </button>
                    `,
                  )
                  .join("")
              : `<div class="scene-ledger-empty">暂无变更请求 / No change requests yet</div>`
          }
        </section>
        <section>
          <h4>生成队列 / Generation Queue</h4>
          ${
            latestQueue.length
              ? latestQueue
                .map(
                    (item) => {
                      const resultLink = scenePathLink(item.result_path, "任务包 / Packet");
                      const packetLink = item.packet_path && item.packet_path !== item.result_path ? scenePathLink(item.packet_path, "任务包 / Packet") : "";
                      const finalLink = scenePathLink(item.final_output_path, "输出 / Output");
                      const targetLink = scenePathLink(item.path, "目标 / Target");
                      return `
                      <div class="scene-ledger-row">
                        <strong>${escapeHtml(item.asset_id || item.queue_id || "asset")}</strong>
                        <span>${escapeHtml(item.target_version || "")} · ${escapeHtml(item.stage_id || "")} · ${escapeHtml(item.status || "queued")}${item.final_output_path && item.output_exists === false ? " · 未落盘 / Missing" : ""}</span>
                        <small>${escapeHtml(item.change_request_id || "")}</small>
                        <span class="scene-ledger-links">${finalLink} ${resultLink} ${packetLink} ${targetLink}</span>
                        <form class="scene-output-form" data-change-request-id="${escapeHtml(item.change_request_id || "")}" data-queue-id="${escapeHtml(item.queue_id || "")}">
                          <input name="output_path" value="${escapeHtml(item.final_output_path || "")}" placeholder="真实输出路径 / Final output path" />
                          <button class="mini-command" type="submit">回填 / Attach</button>
                        </form>
                      </div>
                    `;
                    },
                  )
                  .join("")
              : `<div class="scene-ledger-empty">暂无生成队列 / No queued generation</div>`
          }
        </section>
        <section>
          <h4>版本历史 / Version History</h4>
          ${
            latestVersions.length
              ? latestVersions
                .map(
                    (version) => {
                      const outputLink = scenePathLink(version.final_output_path || version.output_path || version.target_path, "打开 / Open");
                      const packetLink = scenePathLink(version.packet_path, "任务包 / Packet");
                      const canPromote = version.status !== "current";
                      return `
                      <div class="scene-ledger-row">
                        <strong>${escapeHtml(version.asset_id || "asset")} · ${escapeHtml(version.version || "")}</strong>
                        <span>${escapeHtml(version.stage_id || "")} · ${escapeHtml(version.status || "")}${version.final_output_path && version.output_exists === false ? " · 未落盘 / Missing" : ""}</span>
                        <small>${escapeHtml(version.change_request_id || "")} · ${escapeHtml(version.trigger_step || "")}</small>
                        <span class="scene-ledger-links">
                          ${outputLink}
                          ${packetLink}
                          ${
                            canPromote
                              ? `<button class="mini-command scene-version-button" data-asset-id="${escapeHtml(version.asset_id || "")}" data-version="${escapeHtml(version.version || "")}" data-action="${version.status === "superseded" ? "rollback" : "promote"}" type="button">${version.status === "superseded" ? "回滚 / Roll back" : "设为当前 / Set current"}</button>`
                              : `<span>当前 / Current</span>`
                          }
                        </span>
                      </div>
                    `;
                    },
                  )
                  .join("")
              : `<div class="scene-ledger-empty">暂无版本记录 / No version records</div>`
          }
        </section>
        <section>
          <h4>审片记录 / Review Log</h4>
          ${
            reviews.length
              ? reviews
                  .slice()
                  .reverse()
                  .slice(0, 5)
                  .map(
                    (review) => `
                      <div class="scene-ledger-row">
                        <strong>${escapeHtml(sceneStatusLabel(review.status))}</strong>
                        <span>${escapeHtml(review.notes || "无备注 / No note")}</span>
                        <small>${escapeHtml(review.created_at || "")}</small>
                      </div>
                    `,
                  )
                  .join("")
              : `<div class="scene-ledger-empty">暂无审片记录 / No review records</div>`
          }
        </section>
        <section>
          <h4>场戏快照 / Scene Snapshots</h4>
          ${
            latestSnapshots.length
              ? latestSnapshots
                  .map(
                    (snapshot) => `
                      <div class="scene-ledger-row">
                        <strong>${escapeHtml(snapshot.snapshot_id || "snapshot")}</strong>
                        <span>${escapeHtml(sceneStatusLabel(snapshot.status))} · ${escapeHtml(snapshot.created_at || "")}</span>
                        <small>${escapeHtml(snapshot.change_request_id || "")}</small>
                        <span class="scene-ledger-links">${scenePathLink(snapshot.path, "快照 / Snapshot")}</span>
                      </div>
                    `,
                  )
                  .join("")
              : `<div class="scene-ledger-empty">暂无场戏快照 / No scene snapshots</div>`
          }
        </section>
      </div>
    </section>
  `;
}

function renderSceneChangePanel(scene) {
  const request = state.activeChangeRequest?.scene_id === scene?.scene_id ? state.activeChangeRequest : null;
  if (request) {
    const impacts = request.impact_table || [];
    const queued = request.status === "generation_queued";
    const reviewReady = request.status === "review_ready";
    const example = isExampleChangeRequest(request);
    const queue = request.generation_queue || [];
    const canRunGeneration = !example && queue.some((item) => ["queued", "failed"].includes(item.status || ""));
    const adapters = generationAdapters();
    return `
      <section class="scene-change-panel">
        <header>
          <strong>影响评估表 / Impact Table</strong>
          <span>${escapeHtml(request.change_request_id)} · ${escapeHtml(request.trigger_step)} · ${escapeHtml(request.status)}</span>
        </header>
        <p>${escapeHtml(request.creative_direction || "")}</p>
        <p>勾选要处理的资产，并可把动作改为新增、修改或只检查。/ Select affected assets, then choose create, modify, or check.</p>
        <div class="impact-table-wrap">
          <table>
            <thead>
              <tr><th>选 / Select</th><th>动作 / Action</th><th>范围 / Scope</th><th>步骤 / Step</th><th>资源 / Asset</th><th>原因 / Why</th></tr>
            </thead>
            <tbody>
              ${impacts
                .map(
                  (impact) => {
                    const canEdit = !queued && !example;
                    return `
                    <tr>
                      <td><input class="impact-checkbox" type="checkbox" value="${escapeHtml(impact.impact_id)}" ${impact.selected ? "checked" : ""} ${canEdit ? "" : "disabled"} /></td>
                      <td>${impactActionOptions(impact, !canEdit)}</td>
                      <td>${escapeHtml(impact.impact_scope)}</td>
                      <td>${escapeHtml(impact.stage_id)}</td>
                      <td><strong>${escapeHtml(impact.asset_id)}</strong><small>${escapeHtml(impact.path || "")}</small></td>
                      <td>${escapeHtml(impact.why || "")}</td>
                    </tr>
                  `;
                  },
                )
                .join("")}
            </tbody>
          </table>
        </div>
        ${
          queue.length
            ? `<div class="scene-active-queue">
                <strong>本次生成队列 / This queue</strong>
                ${queue
                  .map(
                    (item) => `
                      <span>
                        ${escapeHtml(item.asset_id || item.queue_id || "asset")} · ${escapeHtml(item.target_version || "")} · ${escapeHtml(item.status || "")}
                        ${scenePathLink(item.result_path, "任务包 / Packet")}
                      </span>
                    `,
                  )
                  .join("")}
              </div>`
            : ""
        }
        <textarea id="approvalNotes" rows="2" placeholder="确认备注，可写为什么选择这些资产 / Optional approval note"></textarea>
        <button id="queueSceneGenerationBtn" class="command-button primary" type="button" ${queued || reviewReady || example ? "disabled" : ""}>
          ${example ? "样板不可入队 / Example only" : queued || reviewReady ? "已写入生成队列 / Already queued" : "确认并写入生成队列 / Confirm & queue generation"}
        </button>
        ${
          queue.length
            ? `<label class="scene-adapter-select">生成适配器 / Generation adapter
                <select id="sceneGenerationAdapter">
                  ${adapters
                    .map((adapter) => {
                      const enabled = adapter.enabled !== false && adapter.requires_confirmation !== true;
                      const label = adapter.label || adapter.adapter_id || "adapter";
                      const suffix = enabled ? "" : " · 未启用 / disabled";
                      return `<option value="${escapeHtml(adapter.adapter_id || "")}" ${adapter.adapter_id === "manual_packet" ? "selected" : ""} ${enabled ? "" : "disabled"}>${escapeHtml(label + suffix)}</option>`;
                    })
                    .join("")}
                </select>
              </label>
              <button id="runSceneGenerationBtn" class="command-button" type="button" ${canRunGeneration ? "" : "disabled"}>
                ${example ? "样板不可执行 / Example only" : canRunGeneration ? "开始生成任务包 / Start generation packet" : "任务包已准备审片 / Packet ready for review"}
              </button>`
            : ""
        }
      </section>
    `;
  }
  if (state.recreate?.sceneId === scene?.scene_id) {
    return `
      <section class="scene-change-panel">
        <header>
          <strong>再创作方向 / Re-create Direction</strong>
          <span>${escapeHtml(scene.scene_id)} · ${escapeHtml(state.recreate.triggerStep)}</span>
        </header>
        <textarea id="creativeDirection" rows="3" placeholder="写下这一轮要改变什么，例如：入口更潮湿，门帘运动更明确 / Describe what should change in this iteration"></textarea>
        <button id="createImpactTableBtn" class="command-button primary" type="button">生成影响评估表 / Build impact table</button>
      </section>
    `;
  }
  return `<div class="scene-change-placeholder">选择某一步的“再创作”后，会先生成影响评估表，不会直接生成素材。/ Click Re-create on a step to build an impact table before any generation.</div>`;
}

function renderSceneWorkbench() {
  const scenes = state.detail?.scene_workbench?.scenes || [];
  $("sceneWorkbenchHint").textContent = `${scenes.length} 场戏 / scenes`;
  if (!scenes.length) {
    $("sceneTree").innerHTML = "";
    $("sceneStepLanes").innerHTML = `<div class="empty-state">还没有场戏清单 / No scene manifest yet.</div>`;
    return;
  }
  const scene = selectedScene();
  renderSceneTree(scenes);
  const stageAssets = scene?.resource_manifest?.stage_assets || {};
  const steps = scene?.primary_steps || Object.keys(stageAssets);
  const versions = scene?.version_registry?.versions || [];
  const changeRequests = scene?.change_requests || [];
  const visibleSteps = steps.filter((step) => state.sceneFilters.step === "all" || step === state.sceneFilters.step);
  const kindOptions = sceneKindOptions(stageAssets, visibleSteps);
  state.sceneFilters.kind = kindOptions.some((option) => option.value === state.sceneFilters.kind) ? state.sceneFilters.kind : "all";
  const hasSceneAssetFilter = state.sceneFilters.kind !== "all" || state.sceneFilters.decision !== "all" || state.sceneFilters.query.trim();
  const laneRows = visibleSteps
    .map((step) => ({ step, assets: (stageAssets[step] || []).filter((asset) => sceneAssetMatches(asset, step)) }))
    .filter((row) => row.assets.length || state.sceneFilters.step !== "all" || !hasSceneAssetFilter);
  $("sceneStepLanes").innerHTML = `
    <div class="scene-workbench-summary">
      <strong>${escapeHtml(scene?.title || scene?.scene_id || "")}</strong>
      <span>${escapeHtml(scene?.scene_id || "")} · ${escapeHtml(sceneStatusLabel(scene?.status))} · ${(scene?.shot_ids || []).length} 镜头 / shots · ${versions.length} 版本记录 / version records · ${changeRequests.length} 变更请求 / change requests</span>
    </div>
    <div class="scene-workbench-controls">
      <label>步骤 / Step
        <select id="sceneStepFilter">
          <option value="all">全部步骤 / All steps</option>
          ${steps.map((step) => `<option value="${escapeHtml(step)}" ${state.sceneFilters.step === step ? "selected" : ""}>${escapeHtml(step)} · ${escapeHtml(stageLabel(step))}</option>`).join("")}
        </select>
      </label>
      <label>类别 / Kind
        <select id="sceneKindFilter">
          ${kindOptions.map((option) => `<option value="${escapeHtml(option.value)}" ${state.sceneFilters.kind === option.value ? "selected" : ""}>${escapeHtml(option.label)}</option>`).join("")}
        </select>
      </label>
      <label>标注 / Mark
        <select id="sceneDecisionFilter">
          <option value="all" ${state.sceneFilters.decision === "all" ? "selected" : ""}>全部 / All</option>
          <option value="use" ${state.sceneFilters.decision === "use" ? "selected" : ""}>✅ 参考 / Use</option>
          <option value="reject" ${state.sceneFilters.decision === "reject" ? "selected" : ""}>× 不用 / Reject</option>
          <option value="unset" ${state.sceneFilters.decision === "unset" ? "selected" : ""}>未标注 / Unmarked</option>
        </select>
      </label>
      <label>搜索 / Search
        <input id="sceneAssetSearch" value="${escapeHtml(state.sceneFilters.query)}" placeholder="资源 / 路径 / 备注 / Asset, path, note" />
      </label>
    </div>
    ${renderSceneLoopPanel(scene, versions, changeRequests)}
    <div class="scene-lane-grid">
      ${
        laneRows.length
          ? laneRows
              .map(({ step, assets }) => `
            <section class="scene-step-lane">
              <header>
                <strong>${escapeHtml(step)}</strong>
                <span>${escapeHtml(stageLabel(step))}</span>
              </header>
              ${assets.length ? assets.map((asset) => renderSceneAsset(asset, step)).join("") : `<div class="scene-asset-empty">暂无匹配资源 / No matching assets</div>`}
              <button class="mini-command scene-recreate-button" data-step="${escapeHtml(step)}" type="button">再创作 / Re-create</button>
            </section>
          `)
              .join("")
          : `<div class="scene-asset-empty">没有匹配的场戏资源 / No matching scene assets</div>`
      }
    </div>
    ${renderSceneChangePanel(scene)}
  `;
  bindSceneWorkbenchEvents();
}

function bindSceneWorkbenchEvents() {
  const stepFilter = $("sceneStepFilter");
  if (stepFilter) {
    stepFilter.addEventListener("change", (event) => {
      state.sceneFilters.step = event.target.value;
      renderSceneWorkbench();
    });
  }
  const kindFilter = $("sceneKindFilter");
  if (kindFilter) {
    kindFilter.addEventListener("change", (event) => {
      state.sceneFilters.kind = event.target.value;
      renderSceneWorkbench();
    });
  }
  const decisionFilter = $("sceneDecisionFilter");
  if (decisionFilter) {
    decisionFilter.addEventListener("change", (event) => {
      state.sceneFilters.decision = event.target.value;
      renderSceneWorkbench();
    });
  }
  const search = $("sceneAssetSearch");
  if (search) {
    search.addEventListener("input", (event) => {
      state.sceneFilters.query = event.target.value;
      renderSceneWorkbench();
    });
  }
  $("sceneStepLanes").querySelectorAll(".scene-request-button").forEach((button) => {
    button.addEventListener("click", () => {
      const scene = selectedScene();
      const request = (scene?.change_requests || []).find((item) => item.change_request_id === button.dataset.changeRequestId);
      state.activeChangeRequest = request || null;
      state.recreate = null;
      renderSceneWorkbench();
    });
  });
  const sceneStatusForm = $("sceneStatusForm");
  if (sceneStatusForm) {
    sceneStatusForm.addEventListener("submit", updateSceneStatus);
  }
  $("sceneStepLanes").querySelectorAll(".scene-asset-row .decision-button").forEach((button) => {
    button.addEventListener("click", async () => {
      const row = button.closest(".scene-asset-row");
      const ref = row?.dataset.ref || "";
      const current = annotationForRef(ref);
      const nextStatus = current.status === button.dataset.status ? "" : button.dataset.status;
      const note = row?.querySelector(".scene-asset-note")?.value || current.note || "";
      await saveResourceAnnotation(ref, { status: nextStatus, note });
    });
  });
  $("sceneStepLanes").querySelectorAll(".scene-asset-note").forEach((textarea) => {
    const saveNote = async (showToast = false) => {
      const ref = textarea.dataset.ref || "";
      const current = annotationForRef(ref);
      await saveResourceAnnotation(ref, { status: current.status || "", note: textarea.value }, { rerender: false, toast: false });
      if (showToast) toast("场戏备注已保存 / Scene note saved");
    };
    textarea.addEventListener("input", () => {
      clearTimeout(textarea._saveTimer);
      textarea._saveTimer = setTimeout(() => saveNote(false).catch((error) => toast(`备注保存失败 / Note save failed: ${error.message}`)), 650);
    });
    textarea.addEventListener("blur", async () => {
      clearTimeout(textarea._saveTimer);
      await saveNote(true);
    });
  });
  $("sceneStepLanes").querySelectorAll(".scene-recreate-button").forEach((button) => {
    button.addEventListener("click", () => {
      const scene = selectedScene();
      state.activeChangeRequest = null;
      state.recreate = { sceneId: scene?.scene_id || "", triggerStep: button.dataset.step || "" };
      renderSceneWorkbench();
    });
  });
  const createImpactButton = $("createImpactTableBtn");
  if (createImpactButton) {
    createImpactButton.addEventListener("click", createSceneImpactTable);
  }
  const queueButton = $("queueSceneGenerationBtn");
  if (queueButton) {
    queueButton.addEventListener("click", queueSceneGeneration);
  }
  const runButton = $("runSceneGenerationBtn");
  if (runButton) {
    runButton.addEventListener("click", runSceneGeneration);
  }
  $("sceneStepLanes").querySelectorAll(".scene-version-button").forEach((button) => {
    button.addEventListener("click", () => updateSceneVersion(button));
  });
  $("sceneStepLanes").querySelectorAll(".scene-output-form").forEach((form) => {
    form.addEventListener("submit", updateSceneOutput);
  });
}

async function createSceneImpactTable() {
  const scene = selectedScene();
  const creativeDirection = $("creativeDirection")?.value.trim() || "";
  if (!scene || !state.recreate?.triggerStep || !creativeDirection) {
    toast("请先填写创作方向 / Please enter a creative direction");
    return;
  }
  await runAction("影响评估 / Impact analysis", async () => {
    const result = await requestJson(`/api/projects/${state.selectedSlug}/scene-change-request`, {
      method: "POST",
      body: JSON.stringify({
        scene_id: scene.scene_id,
        trigger_step: state.recreate.triggerStep,
        creative_direction: creativeDirection,
      }),
    });
    state.detail = result.project || state.detail;
    state.activeChangeRequest = result.change_request || null;
    state.recreate = null;
    renderAll();
  });
}

async function queueSceneGeneration() {
  const request = state.activeChangeRequest;
  if (!request?.change_request_id) return;
  const selectedImpactIds = Array.from(document.querySelectorAll(".impact-checkbox:checked")).map((input) => input.value);
  const actionOverrides = Object.fromEntries(
    Array.from(document.querySelectorAll(".impact-action-select")).map((select) => [select.dataset.impactId, select.value]),
  );
  if (!selectedImpactIds.length) {
    toast("请至少选择一个要新增或修改的资产 / Select at least one asset to create or modify");
    return;
  }
  const selectedQueueableIds = selectedImpactIds.filter((impactId) => ["create", "modify"].includes(actionOverrides[impactId]));
  if (!selectedQueueableIds.length) {
    toast("所选项都是检查项，不会进入生成队列 / Selected items are check-only and will not enter generation");
    return;
  }
  await runAction("生成队列 / Generation queue", async () => {
    const result = await requestJson(`/api/projects/${state.selectedSlug}/scene-generate`, {
      method: "POST",
      body: JSON.stringify({
        change_request_id: request.change_request_id,
        selected_impact_ids: selectedImpactIds,
        action_overrides: actionOverrides,
        notes: $("approvalNotes")?.value.trim() || "",
      }),
    });
    state.detail = result.project || state.detail;
    state.activeChangeRequest = result.change_request || null;
    renderAll();
  });
}

async function runSceneGeneration() {
  const request = state.activeChangeRequest;
  if (!request?.change_request_id) return;
  await runAction("生成任务包 / Generation packet", async () => {
    const result = await requestJson(`/api/projects/${state.selectedSlug}/scene-run-generation`, {
      method: "POST",
      body: JSON.stringify({
        change_request_id: request.change_request_id,
        adapter_id: $("sceneGenerationAdapter")?.value || "manual_packet",
      }),
    });
    state.detail = result.project || state.detail;
    state.activeChangeRequest = result.change_request || null;
    renderAll();
  });
}

async function updateSceneVersion(button) {
  const scene = selectedScene();
  const assetId = button.dataset.assetId || "";
  const version = button.dataset.version || "";
  const action = button.dataset.action || "promote";
  if (!scene || !assetId || !version) return;
  await runAction(action === "rollback" ? "版本回滚 / Version rollback" : "版本晋级 / Version promote", async () => {
    const result = await requestJson(`/api/projects/${state.selectedSlug}/scene-version`, {
      method: "POST",
      body: JSON.stringify({
        scene_id: scene.scene_id,
        asset_id: assetId,
        version,
        action,
      }),
    });
    state.detail = result.project || state.detail;
    renderAll();
  });
}

async function updateSceneOutput(event) {
  event.preventDefault();
  const form = event.currentTarget;
  const changeRequestId = form.dataset.changeRequestId || "";
  const queueId = form.dataset.queueId || "";
  const outputPath = new FormData(form).get("output_path") || "";
  if (!changeRequestId || !queueId || !String(outputPath).trim()) {
    toast("请填写真实输出路径 / Enter a final output path");
    return;
  }
  await runAction("输出回填 / Attach output", async () => {
    const result = await requestJson(`/api/projects/${state.selectedSlug}/scene-output`, {
      method: "POST",
      body: JSON.stringify({
        change_request_id: changeRequestId,
        queue_id: queueId,
        output_path: String(outputPath).trim(),
      }),
    });
    state.detail = result.project || state.detail;
    state.activeChangeRequest = result.change_request || null;
    renderAll();
  });
}

async function updateSceneStatus(event) {
  event.preventDefault();
  const scene = selectedScene();
  if (!scene) return;
  await runAction("场戏状态 / Scene status", async () => {
    const result = await requestJson(`/api/projects/${state.selectedSlug}/scene-status`, {
      method: "POST",
      body: JSON.stringify({
        scene_id: scene.scene_id,
        status: $("sceneStatusSelect")?.value || "in_progress",
        notes: $("sceneStatusNotes")?.value.trim() || "",
        change_request_id: state.activeChangeRequest?.change_request_id || "",
      }),
    });
    state.detail = result.project || state.detail;
    renderAll();
  });
}

function renderAssetList() {
  const previews = state.detail?.previews || {};
  const images = previews.images || [];
  const videos = previews.videos || [];
  const audio = previews.audio || [];
  const threeD = previews.three_d || [];
  const assets = [...images.slice(0, 12), ...videos, ...audio, ...threeD].slice(0, 48);
  const counts = previews.counts || {};
  $("assetHint").textContent = Object.entries(counts)
    .map(([key, value]) => `${key} ${value}`)
    .join(" · ");
  if (!assets.length) {
    $("assetList").innerHTML = `<div class="empty-state">没有资源 / No assets found.</div>`;
    return;
  }
  $("assetList").innerHTML = assets
    .map(
      (item) => `
        <a class="asset-row" href="${escapeHtml(item.url)}" target="_blank" title="${escapeHtml(item.path)}">
          <span>${escapeHtml(item.category)}</span>
          <strong>${escapeHtml(item.name)} ${annotationBadge(item)}</strong>
          <small>${escapeHtml(assetSummary(item))}</small>
        </a>
      `,
    )
    .join("");
}

function renderAutofill() {
  const autofill = state.detail?.autofill || {};
  $("autofillHint").textContent = autofill.generated_at || "";
  $("autofillView").textContent = autofill.text || "还没有自动补全记录 / No autofill run yet.";
}

function renderAll() {
  renderProjects();
  renderSidebarSceneNavigator();
  renderHeader();
  renderStoryboardStudio();
  renderReferenceBoard();
  renderMetrics();
  renderLinks();
  renderSceneWorkbench();
  renderResourceBrowser();
  renderSceneLocks();
  renderVisualGallery();
  renderDocs();
  renderMediaPreview();
  renderAssetList();
  renderStages();
  renderShots();
  renderReport();
  renderAutofill();
}

async function loadProjects() {
  const payload = await requestJson("/api/projects");
  state.projects = payload.projects || [];
  if (!state.selectedSlug && state.projects.length) {
    const coinSlot = state.projects.find((project) => project.slug === "coin-slot");
    state.selectedSlug = (coinSlot || state.projects[0]).slug;
  }
  renderProjects();
  if (state.selectedSlug) {
    await loadDetail(state.selectedSlug);
  } else {
    renderAll();
  }
}

async function loadDetail(slug) {
  state.selectedSlug = slug;
  state.selectedDocIndex = 0;
  state.selectedSceneLockIndex = 0;
  state.selectedSceneId = "";
  state.selectedFrameRef = "";
  state.storyboardStage = "all";
  state.referenceSelection = {};
  state.detail = await requestJson(`/api/projects/${encodeURIComponent(slug)}`);
  loadBoardState();
  renderAll();
}

async function selectProject(slug) {
  try {
    await loadDetail(slug);
  } catch (error) {
    toast(`读取项目失败 / Failed to load project: ${error.message}`);
  }
}

async function runAction(label, fn) {
  if (state.busy) return;
  state.busy = true;
  toast(`${label}中 / running...`);
  try {
    await fn();
    toast(`${label}完成 / done`);
  } catch (error) {
    toast(`${label}失败 / failed: ${error.message}`);
  } finally {
    state.busy = false;
  }
}

async function validateCurrentProject() {
  if (!state.selectedSlug) return;
  await runAction("验证 / Validate", async () => {
    const result = await requestJson(`/api/projects/${state.selectedSlug}/validate`, { method: "POST", body: "{}" });
    if (!result.ok) {
      toast(`验证发现问题，详见返回结果 / Validation found issues; see returned details`);
    }
    await loadProjects();
  });
}

async function analyzeCurrentProject() {
  if (!state.selectedSlug) return;
  const sampleSize = Number($("sampleSize").value || 24);
  const includeSourceRoot = $("includeSourceRoot").checked;
  await runAction("分析 / Analyze", async () => {
    const result = await requestJson(`/api/projects/${state.selectedSlug}/analyze`, {
      method: "POST",
      body: JSON.stringify({ sample_size: sampleSize, include_source_root: includeSourceRoot }),
    });
    if (result.json?.status) {
      toast(`分析完成 / Analysis done: ${statusLabel(result.json.status)}`);
    }
    await loadProjects();
  });
}

async function autofillCurrentProject() {
  if (!state.selectedSlug) return;
  const sampleSize = Number($("sampleSize").value || 24);
  const maxRounds = Number($("maxRounds").value || 3);
  const includeSourceRoot = $("includeSourceRoot").checked;
  const allowExternal = $("allowExternalTools").checked;
  const allowPluginInstall = $("allowPluginInstall").checked;
  await runAction("自动补全 / Autofill", async () => {
    const result = await requestJson(`/api/projects/${state.selectedSlug}/autofill`, {
      method: "POST",
      body: JSON.stringify({
        sample_size: sampleSize,
        max_rounds: maxRounds,
        include_source_root: includeSourceRoot,
        allow_external: allowExternal,
        allow_plugin_install: allowPluginInstall,
      }),
    });
    if (result.json?.status) {
      toast(`自动补全 / Autofill: ${statusLabel(result.json.status)}`);
    }
    await loadProjects();
  });
}

async function buildSceneLocksCurrentProject() {
  if (!state.selectedSlug) return;
  const batch = ($("sceneBatch").value || "B01").trim() || "B01";
  await runAction("场景锁 / Scene Lock", async () => {
    const result = await requestJson(`/api/projects/${state.selectedSlug}/scene-locks`, {
      method: "POST",
      body: JSON.stringify({ batch, label: "first_act" }),
    });
    if (result.json?.scene_count != null) {
      toast(`场景锁 / Scene Lock: ${result.json.scene_count} 场景 / scenes · ${result.json.shot_rows} 镜头 / shots`);
    }
    await loadProjects();
  });
}

async function createProject(event) {
  event.preventDefault();
  const form = event.currentTarget;
  const payload = Object.fromEntries(new FormData(form).entries());
  await runAction("创建项目 / Create project", async () => {
    const result = await requestJson("/api/projects", { method: "POST", body: JSON.stringify(payload) });
    const slug = result.json?.project_slug || payload.slug;
    form.reset();
    await loadProjects();
    if (slug) await loadDetail(slug);
  });
}

async function updateLinks(event) {
  event.preventDefault();
  if (!state.selectedSlug) return;
  const payload = Object.fromEntries(new FormData(event.currentTarget).entries());
  await runAction("链接资源 / Link resources", async () => {
    state.detail = await requestJson(`/api/projects/${state.selectedSlug}/links`, {
      method: "POST",
      body: JSON.stringify(payload),
    });
    await loadProjects();
  });
}

async function saveResourceAnnotation(ref, patch, options = {}) {
  if (!state.selectedSlug || !ref) return;
  const current = annotationForRef(ref);
  const status = patch.status ?? current.status ?? "";
  const note = patch.note ?? current.note ?? "";
  const payload = await requestJson(`/api/projects/${state.selectedSlug}/annotations`, {
    method: "POST",
    body: JSON.stringify({ asset_ref: ref, status, note }),
  });
  state.detail.annotations = payload.annotations || state.detail.annotations || { assets: {} };
  if (options.rerender !== false) {
    renderStoryboardStudio();
    renderSceneWorkbench();
    renderResourceBrowser();
    renderVisualGallery();
    renderAssetList();
  }
  if (options.toast !== false) toast("标注已保存 / Annotation saved");
}

function bindResourceFilters() {
  $("stageFilter").addEventListener("change", (event) => {
    state.filters.stage = event.target.value;
    renderResourceBrowser();
  });
  $("kindFilter").addEventListener("change", (event) => {
    state.filters.kind = event.target.value;
    renderResourceBrowser();
  });
  $("decisionFilter").addEventListener("change", (event) => {
    state.filters.decision = event.target.value;
    renderResourceBrowser();
  });
  $("assetSearch").addEventListener("input", (event) => {
    state.filters.query = event.target.value;
    renderResourceBrowser();
  });
  $("clearResourceFilters").addEventListener("click", () => {
    state.filters = { stage: "all", kind: "all", decision: "all", query: "" };
    renderResourceBrowser();
  });
  document.querySelectorAll(".quick-filter").forEach((button) => {
    button.addEventListener("click", () => {
      state.filters.kind = button.dataset.kindPreset || "all";
      state.filters.stage = "all";
      state.filters.decision = "all";
      state.filters.query = "";
      renderResourceBrowser();
    });
  });
}

function keyShouldStayInEditor(target) {
  return Boolean(target?.closest?.("input, textarea, select, [contenteditable='true']"));
}

function bindKeyboardShortcuts() {
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && !$("boardImageLightbox")?.hidden) {
      closeBoardImageLightbox();
      return;
    }
    if (event.key === "Escape" && state.boardOpen) {
      closeReferenceBoard();
      return;
    }
    if (event.key === "Escape" && document.body.classList.contains("modal-open")) {
      closeAssetPreview();
      return;
    }
    if (keyShouldStayInEditor(event.target)) return;
    if (event.key === "ArrowLeft" || event.key === "ArrowRight") {
      const handled = moveStoryboardFrame(event.key === "ArrowRight" ? 1 : -1);
      if (handled) event.preventDefault();
    }
  });
}

function bindEvents() {
  $("refreshBtn").addEventListener("click", () => runAction("刷新 / Refresh", loadProjects));
  $("openBoardBtn")?.addEventListener("click", openReferenceBoard);
  $("closeBoardBtn")?.addEventListener("click", closeReferenceBoard);
  $("clearBoardBtn")?.addEventListener("click", clearReferenceBoard);
  $("boardImageLightboxClose")?.addEventListener("click", closeBoardImageLightbox);
  $("boardImageLightbox")?.addEventListener("click", (event) => {
    if (event.target?.id === "boardImageLightbox") closeBoardImageLightbox();
  });
  $("validateBtn").addEventListener("click", validateCurrentProject);
  $("analyzeBtn").addEventListener("click", analyzeCurrentProject);
  $("autofillBtn").addEventListener("click", autofillCurrentProject);
  $("sceneLockBtn").addEventListener("click", buildSceneLocksCurrentProject);
  $("createForm").addEventListener("submit", createProject);
  $("linkForm").addEventListener("submit", updateLinks);
  $("assetPreviewClose")?.addEventListener("click", closeAssetPreview);
  $("assetPreviewModal")?.addEventListener("click", (event) => {
    if (event.target?.id === "assetPreviewModal") closeAssetPreview();
  });
  bindResourceFilters();
  bindKeyboardShortcuts();
}

bindEvents();
loadProjects().catch((error) => {
  toast(`初始化失败 / Initialization failed: ${error.message}`);
  renderAll();
});
