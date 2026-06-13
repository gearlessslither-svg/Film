const state = {
  projects: [],
  selectedSlug: null,
  detail: null,
  busy: false,
  selectedDocIndex: 0,
  selectedSceneLockIndex: 0,
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

const $ = (id) => document.getElementById(id);

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
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
  if (item.lfs_missing) parts.push("LFS 未下载 / LFS missing");
  else if (item.lfs_pointer) parts.push("LFS 指针 / LFS pointer");
  return parts.join(" · ");
}

function previewSort(a, b) {
  return Number(Boolean(a.lfs_missing)) - Number(Boolean(b.lfs_missing));
}

function renderLfsPlaceholder(label = "LFS 未下载 / LFS missing") {
  return `
    <div class="lfs-placeholder">
      <strong>LFS</strong>
      <em>${escapeHtml(label)}</em>
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
  return `<span class="scene-lock-placeholder ${item?.lfs_missing ? "warning" : ""}">${escapeHtml(item?.lfs_missing ? "LFS" : label)}</span>`;
}

function renderVisualGallery() {
  const previews = state.detail?.previews || {};
  const allImages = previews.images || [];
  const images = [...allImages].sort(previewSort).slice(0, 24);
  const missingCount = allImages.filter((item) => item.lfs_missing).length;
  const previewCount = allImages.filter((item) => item.previewable && !item.lfs_missing).length;
  $("visualHint").textContent = missingCount
    ? `${previewCount}/${allImages.length} 可预览 / preview · ${missingCount} LFS 未下载 / missing`
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
  renderHeader();
  renderMetrics();
  renderLinks();
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
  state.detail = await requestJson(`/api/projects/${encodeURIComponent(slug)}`);
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

function bindEvents() {
  $("refreshBtn").addEventListener("click", () => runAction("刷新 / Refresh", loadProjects));
  $("validateBtn").addEventListener("click", validateCurrentProject);
  $("analyzeBtn").addEventListener("click", analyzeCurrentProject);
  $("autofillBtn").addEventListener("click", autofillCurrentProject);
  $("sceneLockBtn").addEventListener("click", buildSceneLocksCurrentProject);
  $("createForm").addEventListener("submit", createProject);
  $("linkForm").addEventListener("submit", updateLinks);
  bindResourceFilters();
}

bindEvents();
loadProjects().catch((error) => {
  toast(`初始化失败 / Initialization failed: ${error.message}`);
  renderAll();
});
