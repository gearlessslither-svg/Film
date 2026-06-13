const state = {
  projects: [],
  selectedSlug: null,
  detail: null,
  busy: false,
};

const STAGE_LABELS = {
  "00_admin": "项目控制、导演意图、模型配置、日志",
  "01_intake": "输入归档、参考素材、AI 分析",
  "02_direction": "创意方向、方案、确认记录",
  "03_story": "大纲、剧本、节拍、台词",
  "04_lookdev": "风格帧、色彩、光照、美术参考",
  "05_asset_bible": "角色、场景、道具、连续性锁",
  "06_previs": "白模、机位、控制层、空间 QA",
  "07_shots": "镜头表、关键帧、图片/视频提示词",
  "08_generation": "生成任务、图片/视频输出、废片记录",
  "09_edit": "粗剪、声音、字幕、调色",
  "10_qa": "QA 报告、修复队列、审片记录",
  "11_delivery": "最终导出、交付包、交付清单",
};

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
  return `${project.slug} · readiness ${readiness} · P0 ${project.p0_count ?? 0}`;
}

function renderProjects() {
  const root = $("projectList");
  if (!state.projects.length) {
    root.innerHTML = `<div class="empty-state">还没有项目。先创建一个项目。</div>`;
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

function renderHeader() {
  const detail = state.detail;
  if (!detail) {
    $("projectTitle").textContent = "未选择项目";
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
    pill(report.status || "unscanned", report.status === "needs_work" ? "danger" : report.status === "warn" ? "warn" : "ok"),
    pill(`P0 ${p0}`, p0 > 0 ? "danger" : "ok"),
    pill(report.exists ? "有分析报告" : "未分析", report.exists ? "ok" : "warn"),
    pill(autofill.exists ? `Autofill ${autofill.status || "done"}` : "Autofill idle", autofill.status === "ready_for_director_review" ? "ok" : autofill.exists ? "warn" : ""),
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
  $("stageHint").textContent = `${stages.length} stages`;
  if (!stages.length) {
    $("stageList").innerHTML = `<div class="empty-state">没有阶段数据。</div>`;
    return;
  }
  $("stageList").innerHTML = stages
    .map((stage) => {
      const weak = (stage.weak || []).slice(0, 3).join(", ");
      const missing = (stage.missing || []).slice(0, 3).join(", ");
      const note = missing || weak || `${stage.file_count} 个文件`;
      const title = STAGE_LABELS[stage.id] || stage.description;
      return `
        <div class="stage-row">
          <span class="stage-code">${escapeHtml(stage.id)}</span>
          <span class="stage-title">
            <strong>${escapeHtml(title)}</strong>
            <span>${escapeHtml(note)}</span>
          </span>
          <span class="status-dot ${escapeHtml(stage.status)}">${escapeHtml(stage.status)}</span>
        </div>
      `;
    })
    .join("");
}

function renderShots() {
  const shots = state.detail?.shots;
  const rows = shots?.rows || [];
  const columns = (shots?.columns || []).slice(0, 8);
  $("shotHint").textContent = shots?.exists ? `${shots.row_count || 0} rows` : "missing";
  if (!shots?.exists) {
    $("shotTable").innerHTML = `<div class="empty-state">缺少 07_shots/shot_list.csv。</div>`;
    return;
  }
  if (!rows.length) {
    $("shotTable").innerHTML = `<div class="empty-state">镜头表存在，但目前没有镜头行。</div>`;
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
  $("reportView").textContent = report.text || "还没有分析报告。点击“分析”生成。";
}

function renderAutofill() {
  const autofill = state.detail?.autofill || {};
  $("autofillHint").textContent = autofill.generated_at || "";
  $("autofillView").textContent = autofill.text || "No autofill run yet.";
}

function renderAll() {
  renderProjects();
  renderHeader();
  renderMetrics();
  renderLinks();
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
  state.detail = await requestJson(`/api/projects/${encodeURIComponent(slug)}`);
  renderAll();
}

async function selectProject(slug) {
  try {
    await loadDetail(slug);
  } catch (error) {
    toast(`读取项目失败：${error.message}`);
  }
}

async function runAction(label, fn) {
  if (state.busy) return;
  state.busy = true;
  toast(`${label}中...`);
  try {
    await fn();
    toast(`${label}完成`);
  } catch (error) {
    toast(`${label}失败：${error.message}`);
  } finally {
    state.busy = false;
  }
}

async function validateCurrentProject() {
  if (!state.selectedSlug) return;
  await runAction("验证", async () => {
    const result = await requestJson(`/api/projects/${state.selectedSlug}/validate`, { method: "POST", body: "{}" });
    if (!result.ok) {
      toast(`验证发现问题，详见返回结果`);
    }
    await loadProjects();
  });
}

async function analyzeCurrentProject() {
  if (!state.selectedSlug) return;
  const sampleSize = Number($("sampleSize").value || 24);
  const includeSourceRoot = $("includeSourceRoot").checked;
  await runAction("分析", async () => {
    const result = await requestJson(`/api/projects/${state.selectedSlug}/analyze`, {
      method: "POST",
      body: JSON.stringify({ sample_size: sampleSize, include_source_root: includeSourceRoot }),
    });
    if (result.json?.status) {
      toast(`分析完成：${result.json.status}`);
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
  await runAction("Autofill", async () => {
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
      toast(`Autofill: ${result.json.status}`);
    }
    await loadProjects();
  });
}

async function createProject(event) {
  event.preventDefault();
  const form = event.currentTarget;
  const payload = Object.fromEntries(new FormData(form).entries());
  await runAction("创建项目", async () => {
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
  await runAction("链接资源", async () => {
    state.detail = await requestJson(`/api/projects/${state.selectedSlug}/links`, {
      method: "POST",
      body: JSON.stringify(payload),
    });
    await loadProjects();
  });
}

function bindEvents() {
  $("refreshBtn").addEventListener("click", () => runAction("刷新", loadProjects));
  $("validateBtn").addEventListener("click", validateCurrentProject);
  $("analyzeBtn").addEventListener("click", analyzeCurrentProject);
  $("autofillBtn").addEventListener("click", autofillCurrentProject);
  $("createForm").addEventListener("submit", createProject);
  $("linkForm").addEventListener("submit", updateLinks);
}

bindEvents();
loadProjects().catch((error) => {
  toast(`初始化失败：${error.message}`);
  renderAll();
});
