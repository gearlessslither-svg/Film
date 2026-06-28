const APP_PAGE = document.body?.dataset?.page || "main";

function isExternalRetouchPage() {
  return APP_PAGE === "external-retouch";
}

const state = {
  projects: [],
  recycledProjects: [],
  recycleBinOpen: false,
  dailyIdeasOpen: false,
  dailyIdeas: {
    dates: [],
    selectedDate: "",
    detail: null,
    calendarYear: new Date().getFullYear(),
    calendarMonth: new Date().getMonth() + 1,
    seed: "",
    handoffs: [],
  },
  projectMutationBusy: false,
  selectedSlug: null,
  detail: null,
  busy: false,
  selectedDocIndex: 0,
  selectedSceneLockIndex: 0,
  selectedSceneId: "",
  selectedFrameRef: "",
  storyboardStage: "final",
  referenceSelection: {},
  ideaHandoffs: [],
  ideaActiveRowIndex: 0,
  ideaActiveBibleIndex: 0,
  ideaBatchRows: [],
  cardVersionPreview: {},
  ideaRefFilters: {
    act: "all",
    tag: "all",
    query: "",
  },
  imageLibraryFilters: {
    scope: "all",
    tag: "all",
    query: "",
  },
  cardFilters: {
    scope: "",
    tag: "all",
    mode: "all",
    query: "",
  },
  boardOpen: false,
  boardNodes: [],
  boardEdges: [],
  boardHandoffs: [],
  boardHandoffCollapsed: false,
  boardScale: 1,
  boardLinkSourceId: "",
  boardTargetCard: null,
  whiteboxOpen: false,
  whiteboxSourceRef: "",
  whiteboxSelectedTargets: [],
  whiteboxHandoffs: [],
  whiteboxFilters: {
    scene: "current",
    query: "",
  },
  externalRetouch: {
    folderPath: "",
    recursive: true,
    maxImages: 300,
    scanResults: [],
    selectedScanPaths: [],
    globalReferenceNote: "",
    query: "",
    activeRowIndex: 0,
    folderPickerOpen: false,
    folderPickerPath: "",
    folderPickerListing: null,
    folderPickerError: "",
    nativeFolderPickerOpen: false,
  },
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
  ideaHandoffPollTimer: null,
  filters: {
    stage: "all",
    kind: "all",
    decision: "all",
    query: "",
  },
};

const PROJECT_BIBLE_SCENE_ID = "__PROJECT_BIBLE__";
const IDEA_ACT_SCENE_PREFIX = "__IDEA_ACT__:";
const IDEA_HANDOFF_ID_PLACEHOLDER = "__IDEA_HANDOFF_ID__";
const PROJECT_BIBLE_SCOPE_OPTIONS = [
  { value: "project", label: "全项目 / Project" },
  { value: "act", label: "单幕 / Act" },
];
const PROJECT_BIBLE_CATEGORY_OPTIONS = [
  { value: "character", label: "人物 / Character" },
  { value: "location", label: "场景 / Location" },
  { value: "prop", label: "道具 / Prop" },
  { value: "lookdev", label: "美术 / Lookdev" },
  { value: "mood", label: "氛围 / Mood" },
  { value: "period", label: "年代 / Period" },
  { value: "constraint", label: "约束 / Constraint" },
];
const CARD_VERSION_STATUS_LABELS = {
  candidate: "候选 / Candidate",
  current: "采用 / Current",
  final: "Final / 最终",
  reference: "参考 / Reference",
  rejected: "淘汰 / Rejected",
};

function newIdeaCardUid() {
  return `CARD_${Date.now().toString(36)}_${Math.random().toString(16).slice(2, 8)}`;
}

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
  prop_ref: "道具参考 / Prop reference",
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
  { value: "card_concept", label: "概念卡图 / Concept card images" },
  { value: "card_storyboard", label: "分镜卡图 / Storyboard card images" },
  { value: "scope_global", label: "全局设定图 / Global scope" },
  { value: "scope_act", label: "幕级设定图 / Act scope" },
  { value: "character", label: "人物 / Character" },
  { value: "scene", label: "场景 / Scene" },
  { value: "prop", label: "道具 / Prop" },
  { value: "whitebox", label: "白模 / Whitebox" },
  { value: "keyframe", label: "关键帧 / Keyframe" },
  { value: "lookdev", label: "风格 / Lookdev" },
  { value: "version_current", label: "采用版本 / Current version" },
  { value: "version_final", label: "Final 版本 / Final version" },
  { value: "version_candidate", label: "候选版本 / Candidate version" },
  { value: "version_reference", label: "参考版本 / Reference version" },
  { value: "version_rejected", label: "淘汰版本 / Rejected version" },
  { value: "qa_ok", label: "技术合格 / QA OK" },
  { value: "qa_warn", label: "需检查 / QA warn" },
  { value: "qa_danger", label: "低分风险 / QA risk" },
  { value: "qa_unscored", label: "未质检 / QA missing" },
  { value: "marked_use", label: "✅ 已选 / Marked use" },
  { value: "marked_reject", label: "× 不用 / Rejected" },
  { value: "unmarked", label: "未标注 / Unmarked" },
];
const BOARD_OUTPUT_KIND_OPTIONS = [
  { value: "storyboard_keyframe", label: "分镜关键帧 / Storyboard keyframe" },
  { value: "character_ref", label: "人设参考 / Character reference" },
  { value: "scene_ref", label: "场景参考 / Scene reference" },
  { value: "prop_ref", label: "道具参考 / Prop reference" },
  { value: "lookdev", label: "风格参考 / Lookdev reference" },
  { value: "whitebox", label: "白模参考 / Whitebox reference" },
  { value: "image", label: "普通图片 / Image" },
];
const CARD_FILTER_OPTIONS = [
  { value: "all", label: "全部卡片 / All cards" },
  { value: "selected", label: "本次生成 / Selected" },
  { value: "unselected", label: "未勾选 / Unselected" },
  { value: "no_image", label: "未出图 / No image" },
  { value: "has_image", label: "已有图 / Has image" },
  { value: "current", label: "有采用版本 / Has current" },
  { value: "final", label: "有 Final 版本 / Has final" },
  { value: "reference", label: "有参考版本 / Has reference" },
  { value: "candidate", label: "有候选版本 / Has candidate" },
  { value: "rejected", label: "有淘汰版本 / Has rejected" },
  { value: "qa_unscored", label: "主版本未质检 / Current unscored" },
  { value: "qa_ok", label: "主版本合格 / QA OK" },
  { value: "qa_warn", label: "主版本需检查 / QA warn" },
  { value: "qa_risk", label: "主版本低分 / QA risk" },
];

const $ = (id) => document.getElementById(id);
const NATURAL_COLLATOR = new Intl.Collator(["zh-Hans-CN", "en"], { numeric: true, sensitivity: "base" });
const externalImageDragCache = new Map();

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
  if (!node) return;
  node.textContent = message;
  node.classList.add("show");
  clearTimeout(node._timer);
  node._timer = setTimeout(() => node.classList.remove("show"), 2800);
}

function imageMimeFromPath(path = "") {
  const lower = String(path || "").toLowerCase();
  if (lower.endsWith(".jpg") || lower.endsWith(".jpeg")) return "image/jpeg";
  if (lower.endsWith(".webp")) return "image/webp";
  if (lower.endsWith(".gif")) return "image/gif";
  return "image/png";
}

function imageFileNameFromPath(path = "", fallback = "pipeline-image.png") {
  const clean = String(path || "").split("?")[0].split("#")[0];
  const name = clean.split("/").filter(Boolean).pop() || fallback;
  if (/\.(png|jpe?g|webp|gif)$/i.test(name)) return name;
  return `${name.replace(/\.+$/, "") || "pipeline-image"}.png`;
}

function absoluteAssetUrl(url = "") {
  if (!url) return "";
  try {
    return new URL(url, window.location.href).href;
  } catch {
    return url;
  }
}

function externalImageDragAttrs(url, path, name = "", options = {}) {
  if (!url || !isImagePath(path || url)) return "";
  const fileName = imageFileNameFromPath(path || name || url, name || "pipeline-image.png");
  // Links are draggable by default; emit an explicit draggable="false" so the <a>
  // wrapper never starts a URL/.webloc drag and the inner <img> is always the source.
  const draggable = options.draggable === false ? 'draggable="false"' : 'draggable="true"';
  return [
    'data-external-image-drag="true"',
    `data-drag-image-url="${escapeHtml(url)}"`,
    `data-drag-image-path="${escapeHtml(path || "")}"`,
    `data-drag-image-name="${escapeHtml(fileName)}"`,
    draggable,
  ].join(" ");
}

function downloadImageAttrs(url, path, name = "") {
  if (!url || !isImagePath(path || url)) return "";
  return `href="${escapeHtml(url)}" download="${escapeHtml(imageFileNameFromPath(path || name || url, name || "pipeline-image.png"))}"`;
}

const EXTERNAL_IMAGE_DRAG_CACHE_LIMIT = 48;

// Keep the cache bounded so a long session of hovering/dragging images doesn't pin
// dozens of full-resolution blobs in memory (Map preserves insertion order → FIFO).
function rememberExternalImageDragFile(absoluteUrl, file) {
  externalImageDragCache.set(absoluteUrl, { file });
  while (externalImageDragCache.size > EXTERNAL_IMAGE_DRAG_CACHE_LIMIT) {
    const oldest = externalImageDragCache.keys().next().value;
    if (oldest === undefined || oldest === absoluteUrl) break;
    externalImageDragCache.delete(oldest);
  }
}

async function preloadExternalImageDrag(element) {
  const url = element?.dataset?.dragImageUrl || "";
  if (!url) return null;
  const absoluteUrl = absoluteAssetUrl(url);
  const cached = externalImageDragCache.get(absoluteUrl);
  if (cached?.file) return cached.file;
  if (cached?.promise) return cached.promise;
  const path = element.dataset.dragImagePath || "";
  const name = element.dataset.dragImageName || imageFileNameFromPath(path || absoluteUrl);
  const promise = fetch(absoluteUrl)
    .then((response) => {
      if (!response.ok) throw new Error(response.statusText || `HTTP ${response.status}`);
      return response.blob();
    })
    .then((blob) => {
      const file = new File([blob], name, { type: blob.type || imageMimeFromPath(path || name) });
      rememberExternalImageDragFile(absoluteUrl, file);
      return file;
    })
    .catch((error) => {
      externalImageDragCache.delete(absoluteUrl);
      throw error;
    });
  externalImageDragCache.set(absoluteUrl, { promise });
  return promise;
}

function blobFromDataUrl(dataUrl) {
  const [meta = "", data = ""] = dataUrl.split(",");
  const mime = meta.match(/data:([^;]+)/)?.[1] || "image/png";
  const binary = atob(data);
  const bytes = new Uint8Array(binary.length);
  for (let index = 0; index < binary.length; index += 1) bytes[index] = binary.charCodeAt(index);
  return new Blob([bytes], { type: mime });
}

function fileFromLoadedImage(element) {
  const img = element.matches?.("img") ? element : element.querySelector?.("img");
  if (!img?.complete || !img.naturalWidth || !img.naturalHeight) return null;
  const path = element.dataset.dragImagePath || "";
  const name = element.dataset.dragImageName || imageFileNameFromPath(path || img.currentSrc || img.src);
  const mime = imageMimeFromPath(path || name);
  try {
    const canvas = document.createElement("canvas");
    canvas.width = img.naturalWidth;
    canvas.height = img.naturalHeight;
    const context = canvas.getContext("2d");
    context.drawImage(img, 0, 0);
    const dataUrl = canvas.toDataURL(mime, 0.96);
    const blob = blobFromDataUrl(dataUrl);
    return new File([blob], name, { type: blob.type || mime });
  } catch {
    return null;
  }
}

function attachExternalImageDragData(event, element) {
  const transfer = event.dataTransfer;
  if (!transfer || !element) return;
  const url = element.dataset.dragImageUrl || "";
  const path = element.dataset.dragImagePath || "";
  const name = element.dataset.dragImageName || imageFileNameFromPath(path || url);
  const absoluteUrl = absoluteAssetUrl(url);
  let addedFile = false;
  const cached = externalImageDragCache.get(absoluteUrl);
  const file = cached?.file || fileFromLoadedImage(element);
  if (file && transfer.items?.add) {
    try {
      transfer.items.add(file);
      addedFile = true;
      // Cache the loaded-pixel file so the next drag of this image is instant.
      if (!cached?.file && absoluteUrl) rememberExternalImageDragFile(absoluteUrl, file);
    } catch {
      addedFile = false;
    }
  }
  // DownloadURL drives drops onto the OS desktop/Finder; uri-list/text covers web
  // drop targets. Both are set unconditionally, so a drag always carries the image
  // even when no File object is attached — no "drag again" retry needed.
  transfer.setData("text/plain", absoluteUrl || path);
  transfer.setData("text/uri-list", absoluteUrl || path);
  transfer.setData("DownloadURL", `${file?.type || imageMimeFromPath(path || name)}:${name}:${absoluteUrl}`);
  transfer.effectAllowed = "copy";
  if (!addedFile) {
    // No File this time (image not yet decoded); warm it for subsequent drags.
    preloadExternalImageDrag(element).catch(() => {});
  }
}

async function blobToPngBlob(blob) {
  if (!blob || blob.type === "image/png") return blob;
  // The clipboard reliably accepts image/png; re-encode other formats (jpeg/webp).
  const bitmap = await createImageBitmap(blob);
  const canvas = document.createElement("canvas");
  canvas.width = bitmap.width;
  canvas.height = bitmap.height;
  canvas.getContext("2d").drawImage(bitmap, 0, 0);
  bitmap.close?.();
  return await new Promise((resolve, reject) => {
    canvas.toBlob((out) => (out ? resolve(out) : reject(new Error("PNG encode failed"))), "image/png");
  });
}

// Synchronously turn an already-decoded <img> into a PNG Blob (no network, no async),
// so we can hand the clipboard a real Blob inside the click's user-gesture window.
function pngBlobFromLoadedImage(element) {
  const img = element?.matches?.("img") ? element : element?.querySelector?.("img");
  if (!img?.complete || !img.naturalWidth || !img.naturalHeight) return null;
  try {
    const canvas = document.createElement("canvas");
    canvas.width = img.naturalWidth;
    canvas.height = img.naturalHeight;
    canvas.getContext("2d").drawImage(img, 0, 0);
    return blobFromDataUrl(canvas.toDataURL("image/png"));
  } catch {
    return null; // cross-origin taint or oversized canvas
  }
}

async function copyExternalImageToClipboard(element) {
  if (!navigator.clipboard?.write || typeof ClipboardItem === "undefined") {
    toast("此浏览器不支持复制图片到剪贴板 / Clipboard image copy unsupported here");
    return;
  }
  try {
    // Preferred: a real Blob written synchronously within the gesture. Avoids the
    // Promise-valued ClipboardItem form, which several Chromium builds (incl. Atlas)
    // accept without actually placing the image on the OS pasteboard.
    let blob = pngBlobFromLoadedImage(element);
    if (!blob) {
      const cached = externalImageDragCache.get(absoluteAssetUrl(element?.dataset?.dragImageUrl || ""));
      if (cached?.file) blob = await blobToPngBlob(cached.file);
    }
    if (!blob) {
      const absoluteUrl = absoluteAssetUrl(element?.dataset?.dragImageUrl || "");
      if (!absoluteUrl) {
        toast("没有可复制的图片 / No image to copy");
        return;
      }
      blob = await blobToPngBlob(await fetch(absoluteUrl).then((response) => {
        if (!response.ok) throw new Error(response.statusText || `HTTP ${response.status}`);
        return response.blob();
      }));
    }
    await navigator.clipboard.write([new ClipboardItem({ "image/png": blob })]);
    toast("已复制图片，可在 GPT/邮件/文档里按 ⌘V 粘贴 / Image copied — paste with ⌘V");
  } catch (error) {
    // Surface the real error name (e.g. NotAllowedError) so failures are diagnosable.
    toast(`复制失败 / Copy failed: ${error.name || "Error"} — ${error.message || error}`);
  }
}

let _imageCopyFab = null;
let _imageCopyFabTarget = null;

function imageCopyFab() {
  if (_imageCopyFab) return _imageCopyFab;
  const button = document.createElement("button");
  button.type = "button";
  button.className = "image-copy-fab";
  button.textContent = "复制 / Copy";
  button.title = "复制图片到剪贴板，然后按 ⌘V 粘贴 / Copy image, then paste with ⌘V";
  button.hidden = true;
  button.addEventListener("click", (event) => {
    event.preventDefault();
    event.stopPropagation();
    if (_imageCopyFabTarget) copyExternalImageToClipboard(_imageCopyFabTarget);
  });
  document.body.appendChild(button);
  _imageCopyFab = button;
  return button;
}

function showImageCopyFab(element) {
  const img = element.matches?.("img") ? element : element.querySelector?.("img");
  const anchor = img || element;
  const rect = anchor.getBoundingClientRect();
  if (rect.width < 48 || rect.height < 48) {
    hideImageCopyFab();
    return;
  }
  const button = imageCopyFab();
  _imageCopyFabTarget = element;
  button.hidden = false;
  button.style.left = `${Math.round(rect.right - button.offsetWidth - 6)}px`;
  button.style.top = `${Math.round(rect.top + 6)}px`;
}

function hideImageCopyFab() {
  if (_imageCopyFab) _imageCopyFab.hidden = true;
  _imageCopyFabTarget = null;
}

function installImageCopyButton() {
  const dragSelector = "[data-external-image-drag='true']";
  document.addEventListener(
    "mouseover",
    (event) => {
      if (event.target === _imageCopyFab || event.target?.closest?.(".image-copy-fab")) return;
      const element = event.target?.closest?.(dragSelector);
      if (element) showImageCopyFab(element);
      else hideImageCopyFab();
    },
    { passive: true },
  );
  // The fixed-position button would drift from its image on scroll/drag — just hide it.
  document.addEventListener("scroll", hideImageCopyFab, { capture: true, passive: true });
  document.addEventListener("dragstart", hideImageCopyFab, { capture: true });
}

function installExternalImageDrag() {
  installImageCopyButton();
  const dragSelector = "[data-external-image-drag='true']";
  const warm = (target) => {
    const element = target?.closest?.(dragSelector);
    if (element) preloadExternalImageDrag(element).catch(() => {});
  };
  // Warm only on press (fires right before dragstart) — not on every hover, which
  // otherwise triggers a fetch for each image the pointer passes over.
  document.addEventListener("pointerdown", (event) => warm(event.target), { capture: true });
  document.addEventListener(
    "dragstart",
    (event) => {
      const element = event.target?.closest?.(dragSelector);
      if (!element) return;
      attachExternalImageDragData(event, element);
      document.body.classList.add("external-image-dragging");
    },
    { capture: true },
  );
  document.addEventListener("dragend", () => {
    document.body.classList.remove("external-image-dragging");
  });
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

function recycledProjectLabel(project) {
  const recycledAt = project.recycled_at ? ` · ${project.recycled_at}` : "";
  return `${project.slug || project.trash_name}${recycledAt}`;
}

function todayDateString() {
  const now = new Date();
  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, "0");
  const day = String(now.getDate()).padStart(2, "0");
  return `${year}-${month}-${day}`;
}

function dailyIdeaHandoffStorageKey() {
  return state.dailyIdeas.selectedDate ? `pipeline-daily-idea-handoffs:${state.dailyIdeas.selectedDate}` : "pipeline-daily-idea-handoffs";
}

function loadDailyIdeaHandoffs() {
  try {
    const parsed = JSON.parse(localStorage.getItem(dailyIdeaHandoffStorageKey()) || "[]");
    state.dailyIdeas.handoffs = Array.isArray(parsed) ? parsed : [];
  } catch {
    state.dailyIdeas.handoffs = [];
  }
}

function saveDailyIdeaHandoffs() {
  localStorage.setItem(dailyIdeaHandoffStorageKey(), JSON.stringify(state.dailyIdeas.handoffs || []));
}

function dailyIdeaSummaryLabel(item) {
  const rows = Number(item.row_count || 0);
  const images = Number(item.image_count || 0);
  return `${rows} 条灵感 · ${images} 张图`;
}

function renderProjects() {
  const root = $("projectList");
  if (!root) return;
  const createForm = $("createForm");
  if (createForm) createForm.hidden = Boolean(state.dailyIdeasOpen);
  if (state.dailyIdeasOpen) {
    const dates = state.dailyIdeas.dates || [];
    const selected = state.dailyIdeas.selectedDate || todayDateString();
    root.innerHTML = dates.length
      ? dates
          .map(
            (item) => `
              <article class="project-item daily-date-item ${item.date === selected ? "active" : ""}">
                <button class="project-select-button" data-date="${escapeHtml(item.date)}" data-no-help="true" type="button">
                  <strong>${escapeHtml(item.date)}</strong>
                  <span>${escapeHtml(dailyIdeaSummaryLabel(item))}</span>
                </button>
              </article>
            `,
          )
          .join("")
      : `<div class="empty-state">还没有每日灵感。点击右侧生成今天的灵感。/ No daily ideas yet.</div>`;
    root.querySelectorAll(".project-select-button").forEach((button) => {
      button.addEventListener("click", () => selectDailyIdeaDate(button.dataset.date));
    });
    renderRecycleBinPage();
    return;
  }
  if (!state.projects.length) {
    root.innerHTML = `<div class="empty-state">还没有项目。先创建一个项目。/ No projects yet. Create one first.</div>`;
    renderRecycleBinPage();
    return;
  }
  root.innerHTML = state.projects
    .map(
      (project) => `
        <article class="project-item ${project.slug === state.selectedSlug ? "active" : ""}">
          <button class="project-select-button" data-slug="${escapeHtml(project.slug)}" data-no-help="true" type="button">
            <strong>${escapeHtml(project.name)}</strong>
            <span>${escapeHtml(projectLabel(project))}</span>
          </button>
          <button class="project-recycle-button" data-slug="${escapeHtml(project.slug)}" data-no-help="true" type="button" title="回收项目 / Move project to recycle bin" ${state.projectMutationBusy ? "disabled" : ""}>回收</button>
        </article>
      `,
    )
    .join("");
  root.querySelectorAll(".project-select-button").forEach((button) => {
    button.addEventListener("click", () => selectProject(button.dataset.slug));
  });
  root.querySelectorAll(".project-recycle-button").forEach((button) => {
    button.addEventListener("click", (event) => {
      event.stopPropagation();
      recycleProject(button.dataset.slug);
    });
  });
  renderRecycleBinPage();
}

function renderRecycleBinPage() {
  const root = $("recycleBinPage");
  if (!root) return;
  root.hidden = !state.recycleBinOpen;
  if (!state.recycleBinOpen) return;
  const count = state.recycledProjects.length;
  const rows = count
    ? state.recycledProjects
        .map(
          (project) => `
            <article class="recycle-item">
              <div>
                <strong>${escapeHtml(project.name || project.slug || project.trash_name)}</strong>
                <span>${escapeHtml(recycledProjectLabel(project))}</span>
              </div>
              <button class="command-button recycle-restore-button" data-trash-name="${escapeHtml(project.trash_name)}" type="button" ${state.projectMutationBusy ? "disabled" : ""}>恢复</button>
            </article>
          `,
        )
        .join("")
    : `<div class="empty-state">回收站为空 / Recycle bin is empty.</div>`;
  root.innerHTML = `
    <div class="panel-header recycle-bin-page-header">
      <div>
        <h3>项目回收站 / Project Recycle Bin</h3>
        <span>${count} 个已回收项目 / ${count} recycled projects</span>
      </div>
      <div class="recycle-bin-page-actions">
        <button id="refreshRecycleBinBtn" class="command-button" type="button">刷新 / Refresh</button>
        <button id="closeRecycleBinBtn" class="icon-button" type="button" title="关闭回收站 / Close recycle bin">×</button>
      </div>
    </div>
    <div class="recycle-bin-list">${rows}</div>
  `;
  $("refreshRecycleBinBtn")?.addEventListener("click", () => runAction("刷新回收站 / Refresh recycle bin", refreshProjectCollections));
  $("closeRecycleBinBtn")?.addEventListener("click", closeRecycleBinPage);
  root.querySelectorAll(".recycle-restore-button").forEach((button) => {
    button.addEventListener("click", () => restoreProject(button.dataset.trashName));
  });
}

async function openRecycleBinPage() {
  state.recycleBinOpen = true;
  await refreshProjectCollections();
  renderRecycleBinPage();
  $("recycleBinPage")?.scrollIntoView({ behavior: "smooth", block: "start" });
}

function closeRecycleBinPage() {
  state.recycleBinOpen = false;
  renderRecycleBinPage();
}

function renderDailyIdeaCalendar() {
  const root = $("sidebarSceneNavigator");
  if (!root) return;
  const year = Number(state.dailyIdeas.calendarYear || new Date().getFullYear());
  const month = Number(state.dailyIdeas.calendarMonth || new Date().getMonth() + 1);
  const selected = state.dailyIdeas.selectedDate || todayDateString();
  const generated = new Set((state.dailyIdeas.dates || []).filter((item) => Number(item.row_count || 0) || Number(item.image_count || 0)).map((item) => item.date));
  const firstDay = new Date(year, month - 1, 1);
  const daysInMonth = new Date(year, month, 0).getDate();
  const leading = (firstDay.getDay() + 6) % 7;
  const cells = [];
  for (let i = 0; i < leading; i += 1) cells.push(`<span class="daily-calendar-cell empty"></span>`);
  for (let day = 1; day <= daysInMonth; day += 1) {
    const date = `${year}-${String(month).padStart(2, "0")}-${String(day).padStart(2, "0")}`;
    cells.push(`
      <button class="daily-calendar-cell ${generated.has(date) ? "has-daily" : ""} ${date === selected ? "active" : ""}" data-date="${escapeHtml(date)}" type="button">
        ${day}
      </button>
    `);
  }
  root.innerHTML = `
    <section class="sidebar-scene-panel daily-calendar-panel">
      <div class="sidebar-scene-header">
        <span>灵感日历 / Calendar</span>
        <small>${year}-${String(month).padStart(2, "0")}</small>
      </div>
      <div class="daily-calendar-controls">
        <button class="mini-command daily-calendar-prev" type="button">‹</button>
        <input class="daily-calendar-year" type="number" min="2020" max="2100" value="${year}" />
        <select class="daily-calendar-month">
          ${Array.from({ length: 12 }, (_, index) => index + 1)
            .map((value) => `<option value="${value}" ${value === month ? "selected" : ""}>${String(value).padStart(2, "0")}</option>`)
            .join("")}
        </select>
        <button class="mini-command daily-calendar-next" type="button">›</button>
      </div>
      <div class="daily-calendar-weekdays">
        <span>一</span><span>二</span><span>三</span><span>四</span><span>五</span><span>六</span><span>日</span>
      </div>
      <div class="daily-calendar-grid">${cells.join("")}</div>
    </section>
  `;
  root.querySelector(".daily-calendar-prev")?.addEventListener("click", () => shiftDailyIdeaMonth(-1));
  root.querySelector(".daily-calendar-next")?.addEventListener("click", () => shiftDailyIdeaMonth(1));
  root.querySelector(".daily-calendar-year")?.addEventListener("change", (event) => {
    state.dailyIdeas.calendarYear = Number(event.target.value || year);
    renderDailyIdeaCalendar();
  });
  root.querySelector(".daily-calendar-month")?.addEventListener("change", (event) => {
    state.dailyIdeas.calendarMonth = Number(event.target.value || month);
    renderDailyIdeaCalendar();
  });
  root.querySelectorAll(".daily-calendar-cell[data-date]").forEach((button) => {
    button.addEventListener("click", () => selectDailyIdeaDate(button.dataset.date));
  });
}

function shiftDailyIdeaMonth(delta) {
  const base = new Date(Number(state.dailyIdeas.calendarYear), Number(state.dailyIdeas.calendarMonth) - 1 + delta, 1);
  state.dailyIdeas.calendarYear = base.getFullYear();
  state.dailyIdeas.calendarMonth = base.getMonth() + 1;
  renderDailyIdeaCalendar();
}

function renderSidebarSceneNavigator() {
  const root = $("sidebarSceneNavigator");
  if (!root) return;
  if (state.dailyIdeasOpen) {
    renderDailyIdeaCalendar();
    return;
  }
  const scenes = state.detail?.scene_workbench?.scenes || [];
  const board = currentIdeaBoard();
  const acts = storyActEntries(board);
  if (!state.detail || !acts.length) {
    root.innerHTML = "";
    return;
  }
  const activeActId = activeStoryActId();
  const scene = selectedScene();
  const selectedIdeaActId = selectedIdeaActIdFromState();
  root.innerHTML = `
    <section class="sidebar-scene-panel">
      <div class="sidebar-scene-header">
        <span>工程结构 / Structure</span>
        <small>${acts.length} 幕</small>
      </div>
      <button class="sidebar-scene-button project-bible ${isProjectBibleSelected() ? "active" : ""}" data-project-bible="true" type="button">
        <span>设定 / Settings</span>
        <small>人物 · 道具 · 场景风格 · 视觉圣经</small>
      </button>
      <section class="sidebar-act primary-acts">
        <div class="sidebar-act-title">
          <strong>幕 / Acts</strong>
          <button class="mini-command sidebar-add-act" type="button">新增幕</button>
        </div>
        ${acts
          .map((act) => {
            const actId = act.act_id || "";
            const rowCount = (board.rows || []).filter((row) => rowMatchesStoryAct(row, actId, board)).length;
            const active = act.scene_id ? act.scene_id === scene?.scene_id : selectedIdeaActId === actId;
            return `
              <button class="sidebar-scene-button idea-act-button ${active ? "active" : ""}" ${act.scene_id ? `data-scene-id="${escapeHtml(act.scene_id)}"` : `data-idea-act-id="${escapeHtml(actId)}"`} type="button">
                <span>${escapeHtml(act.title || actId)}</span>
                <small>${escapeHtml(actId)} · ${rowCount} 分镜卡 · ${escapeHtml(sceneStatusLabel(act.status))}</small>
              </button>
            `;
          })
          .join("")}
      </section>
    </section>
  `;
  root.querySelector(".sidebar-add-act")?.addEventListener("click", (event) => {
    event.preventDefault();
    event.stopPropagation();
    addIdeaAct();
  });
  root.querySelectorAll(".sidebar-scene-button").forEach((button) => {
    button.addEventListener("click", () => {
      if (button.dataset.projectBible === "true") {
        selectProjectBible();
        renderAll();
        return;
      }
      if (button.dataset.ideaActId) {
        selectIdeaAct(button.dataset.ideaActId || activeActId || "");
        renderAll();
        return;
      }
      selectScene(button.dataset.sceneId || "");
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
  if (!$("projectTitle") || !$("projectPath") || !$("statusPills")) return;
  if (state.dailyIdeasOpen) {
    const daily = state.dailyIdeas.detail;
    const date = state.dailyIdeas.selectedDate || todayDateString();
    $("projectTitle").textContent = `${date} 每日灵感 / Daily Inspiration`;
    $("projectPath").textContent = daily?.path || "";
    $("statusPills").innerHTML = [
      pill("灵感页 / Inspiration", "ok"),
      pill(date, "ok"),
      pill(`${daily?.row_count || 0} 条`, Number(daily?.row_count || 0) ? "ok" : "warn"),
      pill(`${daily?.image_count || 0} 张图`, Number(daily?.image_count || 0) ? "ok" : "warn"),
    ].join("");
    return;
  }
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

function classToken(value) {
  return String(value || "").replace(/[^a-z0-9_-]/gi, "");
}

function autoCopyHandoffText(text) {
  const value = String(text || "");
  if (!value || !navigator.clipboard?.writeText) return;
  navigator.clipboard.writeText(value).catch(() => {
    // Browser clipboard permissions vary; manual copy/drag remains available.
  });
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
    <a class="preview-tile" href="${escapeHtml(item.url)}" target="_blank" title="${title}" ${externalImageDragAttrs(item.url, item.path, item.name, { draggable: false })}>
      <img src="${escapeHtml(item.url)}" alt="${escapeHtml(item.name)}" loading="lazy" ${externalImageDragAttrs(item.url, item.path, item.name)} />
      <span>${escapeHtml(item.name)}</span>
      <small>${escapeHtml(assetSummary(item))}</small>
      ${annotationBadge(item)}
    </a>
  `;
}

function renderSceneLockThumb(item, label = "场景 / Scene") {
  if (item?.url && item.previewable && !item.lfs_missing) {
    return `<img src="${escapeHtml(item.url)}" alt="${escapeHtml(label)}" loading="lazy" ${externalImageDragAttrs(item.url, item.path, item.name || label)} />`;
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
      <a class="scene-overview-link" href="${escapeHtml(overview.url)}" target="_blank" title="${escapeHtml(overview.path)}" ${externalImageDragAttrs(overview.url, overview.path, overview.name, { draggable: false })}>
        <img src="${escapeHtml(overview.url)}" alt="${escapeHtml(overview.name)}" loading="lazy" ${externalImageDragAttrs(overview.url, overview.path, overview.name)} />
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
      return `<a class="resource-thumb" href="${escapeHtml(item.url)}" target="_blank" ${externalImageDragAttrs(item.url, item.path, item.name, { draggable: false })}><img src="${escapeHtml(item.url)}" alt="${escapeHtml(item.name)}" loading="lazy" ${externalImageDragAttrs(item.url, item.path, item.name)} /></a>`;
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
  if (isConceptWorkspaceSelected() || isIdeaActSelected()) return null;
  const scenes = state.detail?.scene_workbench?.scenes || [];
  if (!scenes.length) return null;
  if (!state.selectedSceneId || !scenes.some((scene) => scene.scene_id === state.selectedSceneId)) {
    state.selectedSceneId = scenes[0].scene_id || "";
  }
  return scenes.find((scene) => scene.scene_id === state.selectedSceneId) || scenes[0];
}

function isProjectBibleSelected() {
  return state.selectedSceneId === PROJECT_BIBLE_SCENE_ID;
}

function ideaActWorkspaceId(actId) {
  return `${IDEA_ACT_SCENE_PREFIX}${encodeURIComponent(actId || "")}`;
}

function isIdeaActSelected() {
  return String(state.selectedSceneId || "").startsWith(IDEA_ACT_SCENE_PREFIX);
}

function selectedIdeaActIdFromState() {
  if (!isIdeaActSelected()) return "";
  return decodeURIComponent(String(state.selectedSceneId || "").slice(IDEA_ACT_SCENE_PREFIX.length));
}

function isConceptWorkspaceSelected() {
  return isProjectBibleSelected();
}

function selectProjectBible() {
  cacheIdeaBoardFromDom();
  state.selectedSceneId = PROJECT_BIBLE_SCENE_ID;
  state.selectedFrameRef = "";
  state.activeChangeRequest = null;
  state.recreate = null;
  state.ideaBatchRows = [];
  if (!state.cardFilters.scope || state.cardFilters.scope === "current_scene" || state.cardFilters.scope === "current_act") state.cardFilters.scope = "all";
}

function selectIdeaAct(actId) {
  cacheIdeaBoardFromDom();
  state.selectedSceneId = ideaActWorkspaceId(actId || "");
  state.selectedFrameRef = "";
  state.activeChangeRequest = null;
  state.recreate = null;
  state.ideaBatchRows = [];
  if (!state.cardFilters.scope || state.cardFilters.scope === "all" || state.cardFilters.scope === "current_scene") {
    state.cardFilters.scope = "current_act";
  }
  ensureIdeaActiveRowForScene(currentIdeaBoard());
}

function selectScene(sceneId) {
  cacheIdeaBoardFromDom();
  const fromConceptWorkspace = isProjectBibleSelected() || isIdeaActSelected();
  state.selectedSceneId = sceneId || "";
  state.selectedFrameRef = "";
  state.activeChangeRequest = null;
  state.recreate = null;
  if (fromConceptWorkspace && (!state.cardFilters.scope || state.cardFilters.scope === "all" || state.cardFilters.scope === "current_act")) state.cardFilters.scope = "current_scene";
  ensureIdeaActiveRowForScene(currentIdeaBoard());
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
  if (haystack.includes("prop") || haystack.includes("道具")) return "prop_ref";
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
  const isImage = isImagePath(path);
  const copyButton = $("assetPreviewCopy");
  if (copyButton) copyButton.hidden = !isImage;
  const downloadLink = $("assetPreviewDownload");
  if (downloadLink) {
    downloadLink.hidden = !isImage;
    downloadLink.href = asset.url;
    downloadLink.download = imageFileNameFromPath(path || asset.asset_id || "pipeline-image.png");
  }
  modal.hidden = false;
  document.body.classList.add("modal-open");
  if (isImagePath(path)) {
    body.innerHTML = `<img class="asset-preview-image" src="${escapeHtml(asset.url)}" alt="${escapeHtml(title.textContent)}" title="单击关闭 / Click to close" ${externalImageDragAttrs(asset.url, path, asset.asset_id || asset.role || path)} />`;
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

function assetIsWhitebox(asset) {
  const haystack = [asset?.asset_id, asset?.role, asset?.path, asset?.kind, asset?.stage].join(" ").toLowerCase();
  return asset?.kind === "whitebox" || haystack.includes("whitebox") || haystack.includes("previs");
}

function storyboardActId(scene) {
  return scene?.act_id || scene?.scene_id || "";
}

function storyboardRowsForAct(scene, board = currentIdeaBoard()) {
  const actId = scene?.act_id || "";
  const sceneId = scene?.scene_id || "";
  return (board.rows || [])
    .map((row, index) => ({ row, index }))
    .filter(({ row }) => {
      const rowActId = row.act_id || sceneForIdeaRow(row).act_id || "";
      if (actId) return rowActId === actId;
      return sceneId ? row.scene_id === sceneId : true;
    });
}

function finalStoryboardFrames(scene) {
  const board = currentIdeaBoard();
  return storyboardRowsForAct(scene, board)
    .map(({ row, index }) => {
      const current = [...cardVersionEntries(row)].reverse().find((version) => version.status === "final" || version.final === true);
      const path = current?.output_path || "";
      if (!isImagePath(path)) return null;
      const rowScene = sceneForIdeaRow(row);
      const rowActId = row.act_id || rowScene.act_id || scene?.act_id || "";
      return {
        asset_id: row.item_id || `IDEA_SHOT_${index + 1}`,
        role: row.beat || row.frame_description || row.item_id || "Storyboard keyframe",
        path,
        origin: "project",
        url: sceneAssetUrl(path),
        ref: `project:${path}`,
        kind: "storyboard_keyframe",
        stage: "08_generation",
        scene_id: row.scene_id || "",
        scene_title: rowScene.title || "",
        act_id: rowActId,
        act_title: rowActId ? projectBibleActLabel(board, rowActId) : rowScene.act_title || "",
        shot_id: row.item_id || "",
        asset_order: index,
        sort_text: [row.item_id, row.beat, current?.version_id, path].filter(Boolean).join(" "),
        version_id: current?.version_id || "",
        version_status: "final",
        card_type: "storyboard",
        card_id: row.item_id || "",
        card_scope: rowActId ? "act" : "scene",
        card_act_id: rowActId,
        card_act_title: rowActId ? projectBibleActLabel(board, rowActId) : "",
        card_title: row.beat || row.item_id || "",
        card_category: "storyboard",
        card_summary: row.frame_description || "",
        card_prompt: [storyboardLinkValue(row.linked_cards || []), row.spatial_logic, row.image_prompt, row.video_prompt, row.revision_note, row.notes].filter(Boolean).join(" "),
        qa_score: current?.qa?.score ?? null,
        is_final_storyboard_frame: true,
        row_index: index,
        previewable: true,
        tags: [],
      };
    })
    .filter(Boolean)
    .map((asset) => ({ ...asset, tags: boardAssetTags(asset) }))
    .sort((a, b) => {
      const order = Number(a.row_index ?? 9999) - Number(b.row_index ?? 9999);
      if (order) return order;
      return naturalCompare(a.shot_id || a.path, b.shot_id || b.path);
    });
}

function assetMatchesStoryboardAct(asset, scene) {
  const actId = scene?.act_id || "";
  const sceneId = scene?.scene_id || "";
  if (actId) {
    return asset.act_id === actId || asset.card_act_id === actId;
  }
  return sceneId ? asset.scene_id === sceneId : true;
}

function pendingStoryboardFrames(scene) {
  const finalPaths = new Set(finalStoryboardFrames(scene).map((frame) => frame.path));
  return allBoardImageAssets()
    .filter((asset) => {
      if (!asset?.path || !asset?.url || !isImagePath(asset.path)) return false;
      if (!assetMatchesStoryboardAct(asset, scene)) return false;
      return !finalPaths.has(asset.path);
    })
    .sort((a, b) => {
      const shot = naturalCompare(a.shot_id || a.card_id || "ZZZ", b.shot_id || b.card_id || "ZZZ");
      if (shot) return shot;
      const priority = framePriority(a) - framePriority(b);
      if (priority) return priority;
      const status = naturalCompare(a.version_status || "ZZZ", b.version_status || "ZZZ");
      if (status) return status;
      return naturalCompare(a.asset_id || a.path, b.asset_id || b.path);
    });
}

function storyboardFrames(scene) {
  const stage = state.storyboardStage || "final";
  if (stage === "final") return finalStoryboardFrames(scene);
  const pending = pendingStoryboardFrames(scene);
  if (stage === "pending") return pending;
  if (stage === "kind:whitebox") return pending.filter(assetIsWhitebox);
  if (stage?.startsWith("kind:")) return pending.filter((asset) => asset.kind === stage.slice(5));
  return pending.filter((asset) => asset.stage === stage);
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

function keepActiveFrameThumbVisible() {
  const strip = document.querySelector(".frame-strip");
  const active = strip?.querySelector(".frame-thumb.active");
  if (!strip || !active) return;
  const activeLeft = active.offsetLeft;
  const activeRight = activeLeft + active.offsetWidth;
  const visibleLeft = strip.scrollLeft;
  const visibleRight = visibleLeft + strip.clientWidth;
  if (activeLeft < visibleLeft || activeRight > visibleRight) {
    strip.scrollLeft = Math.max(0, activeLeft - (strip.clientWidth - active.offsetWidth) / 2);
  }
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
  const scrollX = window.scrollX;
  const scrollY = window.scrollY;
  state.selectedFrameRef = frames[nextIndex].ref;
  renderStoryboardStudio();
  window.setTimeout(() => {
    keepActiveFrameThumbVisible();
    window.scrollTo(scrollX, scrollY);
  }, 40);
  return true;
}

function storyboardStageOptions(scene) {
  const pending = pendingStoryboardFrames(scene);
  const counts = new Map();
  pending.forEach((asset) => {
    counts.set(asset.stage, (counts.get(asset.stage) || 0) + 1);
  });
  const finalCount = finalStoryboardFrames(scene).length;
  const whiteboxCount = pending.filter(assetIsWhitebox).length;
  const options = [
    { value: "final", label: `最终分镜预览 / Final keyframes (${finalCount})`, help: "只看当前幕按分镜顺序排列的最终采用关键帧。" },
    { value: "pending", label: `待定区 / Pending (${pending.length})`, help: "查看当前幕未被采用的候选图、废图、参考图和其他临时资产。" },
  ];
  if (whiteboxCount) options.push({ value: "kind:whitebox", label: `白模 / Whitebox (${whiteboxCount})`, help: "只看当前幕的白模/预演图，用于空间、机位和光照参考。" });
  return [
    ...options,
    ...Object.entries(STAGE_LABELS)
      .filter(([stage]) => counts.has(stage))
      .map(([stage]) => ({ value: stage, label: `${stageShortLabel(stage)} (${counts.get(stage)})`, help: `只看待定区里属于 ${stageShortLabel(stage)} 的图片。` })),
  ];
}

function frameTitle(frame) {
  if (!frame) return "";
  const shot = frame.shot_id ? `${frame.shot_id} · ` : "";
  return `${shot}${frame.asset_id || frame.role || frame.path}`;
}

function relatedFrameAssets(scene, frame) {
  if (!scene || !frame) return [];
  const allowWhitebox = assetIsWhitebox(frame);
  const assets = flattenSceneAssets(scene).filter((asset) => allowWhitebox || !assetIsWhitebox(asset));
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

const BOARD_MIN_SCALE = 0.3;
const BOARD_MAX_SCALE = 3;
const BOARD_STAGE_WIDTH = 2400;
const BOARD_STAGE_HEIGHT = 1500;
const BOARD_NODE_WIDTH = 420;
const BOARD_NODE_HEIGHT_FOR_LINKS = 280;
let boardLinkDragActive = false;

function boardStorageKey() {
  return state.selectedSlug ? `pipeline-board:${state.selectedSlug}` : "pipeline-board";
}

function clampBoardScale(value) {
  return clamp(Number(value) || 1, BOARD_MIN_SCALE, BOARD_MAX_SCALE);
}

function boardScale() {
  return clampBoardScale(state.boardScale);
}

// Push the scale into the DOM without a full re-render so pinch/zoom stays smooth.
function applyBoardScale() {
  const scale = boardScale();
  const stage = $("referenceBoardCanvas")?.querySelector(".board-canvas-stage");
  const viewport = $("referenceBoardCanvas")?.querySelector(".board-canvas-viewport");
  if (stage) stage.style.transform = `scale(${scale})`;
  if (viewport) {
    viewport.style.width = `${Math.round(BOARD_STAGE_WIDTH * scale)}px`;
    viewport.style.height = `${Math.round(BOARD_STAGE_HEIGHT * scale)}px`;
  }
  const indicator = $("referenceBoardCanvas")?.querySelector(".board-zoom-level");
  if (indicator) indicator.textContent = `${Math.round(scale * 100)}%`;
}

// Set a new zoom level, keeping the content point under `anchor` (client coords) fixed.
function setBoardScale(nextScale, anchor) {
  const canvas = $("referenceBoardCanvas");
  const old = boardScale();
  const next = clampBoardScale(nextScale);
  if (!canvas || next === old) return;
  const rect = canvas.getBoundingClientRect();
  const anchorX = anchor ? anchor.clientX - rect.left : rect.width / 2;
  const anchorY = anchor ? anchor.clientY - rect.top : rect.height / 2;
  const contentX = canvas.scrollLeft + anchorX;
  const contentY = canvas.scrollTop + anchorY;
  const ratio = next / old;
  state.boardScale = next;
  applyBoardScale();
  canvas.scrollLeft = contentX * ratio - anchorX;
  canvas.scrollTop = contentY * ratio - anchorY;
  saveBoardState();
}

function resetBoardScale() {
  setBoardScale(1);
}

function loadBoardState() {
  try {
    const raw = window.localStorage.getItem(boardStorageKey());
    const parsed = raw ? JSON.parse(raw) : {};
    state.boardNodes = Array.isArray(parsed.nodes) ? parsed.nodes : [];
    state.boardEdges = Array.isArray(parsed.edges) ? parsed.edges : [];
    state.boardHandoffs = Array.isArray(parsed.handoffs) ? parsed.handoffs : [];
    state.boardHandoffCollapsed = Boolean(parsed.handoffCollapsed);
    state.boardScale = clampBoardScale(Number(parsed.scale) || 1);
  } catch {
    state.boardNodes = [];
    state.boardEdges = [];
    state.boardHandoffs = [];
    state.boardHandoffCollapsed = false;
    state.boardScale = 1;
  }
}

function saveBoardState() {
  if (!state.selectedSlug) return;
  try {
    window.localStorage.setItem(
      boardStorageKey(),
      JSON.stringify({
        nodes: state.boardNodes,
        edges: state.boardEdges,
        handoffs: state.boardHandoffs,
        handoffCollapsed: state.boardHandoffCollapsed,
        scale: state.boardScale,
      }),
    );
  } catch {
    // Local persistence is a convenience; generation packets remain project-backed.
  }
}

function projectBibleCategoryKind(category) {
  if (category === "character") return "character_ref";
  if (category === "location") return "scene_ref";
  if (category === "prop") return "prop_ref";
  if (["lookdev", "mood", "period", "constraint"].includes(category)) return "lookdev";
  return "image";
}

function boardAssetTags(asset) {
  const tags = new Set();
  const haystack = [
    asset.asset_id,
    asset.role,
    asset.path,
    asset.kind,
    asset.stage,
    asset.card_type,
    asset.card_scope,
    asset.card_act_id,
    asset.card_act_title,
    asset.card_category,
    asset.card_title,
  ].join(" ").toLowerCase();
  if (asset.card_type === "concept") tags.add("card_concept");
  if (asset.card_type === "storyboard") tags.add("card_storyboard");
  if (asset.card_type === "concept" && (asset.card_scope || "project") === "project") tags.add("scope_global");
  if (asset.card_type === "concept" && (asset.card_scope === "act" || asset.card_act_id || asset.act_id)) tags.add("scope_act");
  if (asset.kind === "character_ref" || haystack.includes("character") || haystack.includes("person") || haystack.includes("三视图")) tags.add("character");
  if (asset.kind === "scene_ref" || haystack.includes("location") || haystack.includes("scene") || haystack.includes("environment")) tags.add("scene");
  if (asset.kind === "prop_ref" || haystack.includes("prop") || haystack.includes("道具")) tags.add("prop");
  if (asset.kind === "whitebox" || haystack.includes("whitebox") || haystack.includes("previs")) tags.add("whitebox");
  if (asset.kind === "storyboard_keyframe" || haystack.includes("keyframe") || haystack.includes("storyboard")) tags.add("keyframe");
  if (asset.kind === "lookdev" || haystack.includes("lookdev") || haystack.includes("style") || haystack.includes("palette")) tags.add("lookdev");
  if (asset.version_status) tags.add(`version_${asset.version_status}`);
  if (asset.version_status || asset.card_type) {
    const qaScore = Number(asset.qa_score);
    if (asset.qa_score === undefined || asset.qa_score === null || asset.qa_score === "" || !Number.isFinite(qaScore)) tags.add("qa_unscored");
    else if (qaScore >= 82) tags.add("qa_ok");
    else if (qaScore >= 68) tags.add("qa_warn");
    else tags.add("qa_danger");
  }
  const annotation = annotationForRef(asset.ref);
  if (annotation.status === "use") tags.add("marked_use");
  if (annotation.status === "reject") tags.add("marked_reject");
  if (!annotation.status) tags.add("unmarked");
  return [...tags];
}

function mergeBoardImageAsset(byRef, incoming) {
  if (!incoming?.ref) return;
  incoming.tags = incoming.tags || boardAssetTags(incoming);
  const existing = byRef.get(incoming.ref);
  if (!existing) {
    byRef.set(incoming.ref, incoming);
    return;
  }
  const merged = { ...existing };
  [
    "asset_id",
    "role",
    "path",
    "origin",
    "url",
    "kind",
    "stage",
    "shot_id",
    "sort_text",
    "version_id",
    "version_status",
    "card_type",
    "card_id",
    "card_scope",
    "card_act_id",
    "card_act_title",
    "card_title",
    "card_category",
    "card_summary",
    "card_prompt",
    "qa_score",
  ].forEach((key) => {
    if (!merged[key] && incoming[key]) merged[key] = incoming[key];
  });
  ["scene_id", "scene_title", "scene_slug", "act_id", "act_title"].forEach((key) => {
    if (!merged[key] && incoming[key]) merged[key] = incoming[key];
  });
  merged.scene_order = Math.min(Number(existing.scene_order ?? 9999), Number(incoming.scene_order ?? 9999));
  merged.asset_order = Math.min(Number(existing.asset_order ?? 9999), Number(incoming.asset_order ?? 9999));
  merged.tags = [...new Set([...(existing.tags || []), ...(incoming.tags || []), ...boardAssetTags(merged)])];
  byRef.set(incoming.ref, merged);
}

function cardVersionImageAssets() {
  const board = currentIdeaBoard();
  const scenes = state.detail?.scene_workbench?.scenes || [];
  const sceneIndexById = new Map(scenes.map((scene, index) => [scene.scene_id, index]));
  const assets = [];
  (board.project_bible || []).forEach((card, cardIndex) => {
    const cardScope = card.scope || "project";
    const cardActLabel = card.act_id ? projectBibleActLabel(board, card.act_id) : "全项目 / Project";
    cardVersionEntries(card).forEach((version, versionIndex) => {
      const path = version.output_path || "";
      if (!isImagePath(path)) return;
      const ref = `project:${path}`;
      const kind = projectBibleCategoryKind(card.category || "");
      assets.push({
        asset_id: `${card.card_id || "BIBLE"}_${version.version_id || versionIndex + 1}`,
        role: card.title || card.card_id || "Project Bible version",
        path,
        origin: "project",
        url: sceneAssetUrl(path),
        ref,
        kind,
        stage: "08_generation",
        scene_id: "",
        scene_title: "设定 / Settings",
        scene_slug: "",
        act_id: card.act_id || "",
        act_title: cardActLabel,
        shot_id: "",
        scene_order: 9000 + cardIndex,
        asset_order: versionIndex,
        sort_text: [card.card_id, card.title, card.category, version.version_id, version.notes, path].filter(Boolean).join(" "),
        version_id: version.version_id || "",
        version_status: version.status || "candidate",
        card_type: "concept",
        card_id: card.card_id || "",
        card_scope: cardScope,
        card_act_id: card.act_id || "",
        card_act_title: cardActLabel,
        card_title: card.title || "",
        card_category: card.category || "",
        card_summary: card.summary || "",
        card_prompt: [card.visual_direction, card.prompt_notes, card.revision_note, card.negative_prompt].filter(Boolean).join(" "),
        qa_score: version.qa?.score ?? null,
      });
    });
  });
  (board.rows || []).forEach((row, rowIndex) => {
    const scene = scenes.find((item) => item.scene_id === row.scene_id) || {};
    cardVersionEntries(row).forEach((version, versionIndex) => {
      const path = version.output_path || "";
      if (!isImagePath(path)) return;
      const ref = `project:${path}`;
      assets.push({
        asset_id: `${row.item_id || "IDEA_SHOT"}_${version.version_id || versionIndex + 1}`,
        role: row.beat || row.item_id || "Storyboard version",
        path,
        origin: "project",
        url: sceneAssetUrl(path),
        ref,
        kind: "storyboard_keyframe",
        stage: "08_generation",
        scene_id: row.scene_id || "",
        scene_title: scene.title || "",
        scene_slug: scene.scene_slug || "",
        act_id: row.act_id || scene.act_id || "",
        act_title: row.act_id ? projectBibleActLabel(board, row.act_id) : scene.act_title || "",
        shot_id: row.item_id || "",
        scene_order: sceneIndexById.get(row.scene_id) ?? 8000 + rowIndex,
        asset_order: versionIndex,
        sort_text: [row.item_id, row.beat, row.shot_type, version.version_id, version.notes, path].filter(Boolean).join(" "),
        version_id: version.version_id || "",
        version_status: version.status || "candidate",
        card_type: "storyboard",
        card_id: row.item_id || "",
        card_scope: row.act_id || scene.act_id ? "act" : "scene",
        card_act_id: row.act_id || scene.act_id || "",
        card_act_title: row.act_id ? projectBibleActLabel(board, row.act_id) : scene.act_title || "",
        card_title: row.beat || row.item_id || "",
        card_category: "storyboard",
        card_summary: row.frame_description || "",
        card_prompt: [storyboardLinkValue(row.linked_cards || []), row.spatial_logic, row.image_prompt, row.revision_note, row.notes].filter(Boolean).join(" "),
        qa_score: version.qa?.score ?? null,
      });
    });
  });
  return assets.map((asset) => ({ ...asset, tags: boardAssetTags(asset) }));
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
        mergeBoardImageAsset(byRef, boardAsset);
      });
  });
  const previews = state.detail?.previews || {};
  const previewImages = (previews.assets || previews.images || []).filter((item) => item?.category === "image" || isImagePath(item?.path || ""));
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
    mergeBoardImageAsset(byRef, boardAsset);
  });
  cardVersionImageAssets().forEach((asset) => {
    mergeBoardImageAsset(byRef, asset);
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

function imageLibraryScopeOptions(assets) {
  const countFor = (scope) => assets.filter((asset) => imageAssetMatchesScope(asset, scope)).length;
  const options = [{ value: "all", label: `全部图片 / All images (${assets.length})` }];
  const scene = selectedScene();
  const activeActId = activeStoryActId();
  const activeAct = storyActEntryForId(currentIdeaBoard(), activeActId);
  if (scene?.scene_id) {
    options.push({ value: "current_scene", label: `当前场戏 / Current scene (${scene.scene_id}) (${countFor("current_scene")})` });
  }
  if (activeActId) {
    options.push({ value: "current_act", label: `当前幕 / Current act (${activeAct?.title || activeActId}) (${countFor("current_act")})` });
  }
  options.push({ value: "global", label: `全局/未绑定 / Global (${countFor("global")})` });
  const acts = new Map();
  assets.forEach((asset) => {
    if (asset.act_id) acts.set(asset.act_id, asset.act_title || asset.act_id);
  });
  acts.forEach((label, actId) => options.push({ value: `act:${actId}`, label: `${label} (${countFor(`act:${actId}`)})` }));
  const scenes = new Map();
  assets.forEach((asset) => {
    if (asset.scene_id) scenes.set(asset.scene_id, `${asset.scene_id} · ${asset.scene_title || ""}`);
  });
  scenes.forEach((label, sceneId) => options.push({ value: `scene:${sceneId}`, label: `${label} (${countFor(`scene:${sceneId}`)})` }));
  return options;
}

function effectiveImageScope(scope, assets) {
  const normalized = normalizedImageScope(scope);
  const options = imageLibraryScopeOptions(assets);
  return options.some((option) => option.value === normalized) ? normalized : "all";
}

function normalizedImageScope(scope) {
  if (scope === "current") return "current_scene";
  return scope || "all";
}

function imageAssetMatchesScope(asset, scope) {
  const value = normalizedImageScope(scope);
  const scene = selectedScene();
  const activeActId = activeStoryActId();
  const activeAct = storyActEntryForId(currentIdeaBoard(), activeActId);
  if (value === "all") return true;
  if (value === "global") return !asset.scene_id && !asset.act_id;
  if (value === "current_scene") return Boolean(scene?.scene_id) && asset.scene_id === scene.scene_id;
  if (value === "current_act") {
    if (!activeActId) return false;
    if (activeAct?.scene_id) return asset.scene_id === activeAct.scene_id;
    return asset.act_id === activeActId;
  }
  if (value.startsWith("act:")) return asset.act_id === value.slice(4);
  if (value.startsWith("scene:")) return asset.scene_id === value.slice(6);
  return true;
}

function imageAssetMatchesLibraryFilters(asset, filters = {}, scopeKey = "scene") {
  const tags = asset.tags || [];
  const scope = filters[scopeKey] || filters.scope || "all";
  if (!imageAssetMatchesScope(asset, scope)) return false;
  if ((filters.tag || "all") === "all" && tags.includes("whitebox")) return false;
  if ((filters.tag || "all") !== "all" && !tags.includes(filters.tag)) return false;
  const query = String(filters.query || "").trim().toLowerCase();
  if (!query) return true;
  const annotation = annotationForRef(asset.ref);
  return [
    asset.asset_id,
    asset.role,
    asset.path,
    asset.scene_id,
    asset.scene_title,
    asset.act_title,
    asset.shot_id,
    asset.version_id,
    asset.version_status,
    asset.card_type,
    asset.card_id,
    asset.card_scope,
    asset.card_act_id,
    asset.card_act_title,
    asset.card_title,
    asset.card_category,
    asset.card_summary,
    asset.card_prompt,
    asset.qa_score,
    kindLabel(asset.kind),
    tags.join(" "),
    annotation.note,
  ]
    .join(" ")
    .toLowerCase()
    .includes(query);
}

function imageLibraryFilterPatch(filters = {}) {
  const patch = {};
  const has = (key) => Object.prototype.hasOwnProperty.call(filters, key);
  if (has("scope") || has("scene") || has("act")) {
    patch.scope = filters.scope ?? filters.scene ?? filters.act ?? "all";
  }
  if (has("tag")) patch.tag = filters.tag ?? "all";
  if (has("query")) patch.query = filters.query ?? "";
  return patch;
}

function normalizedImageLibraryFilters(filters = {}) {
  const patch = imageLibraryFilterPatch(filters);
  return {
    scope: patch.scope || "all",
    tag: patch.tag || "all",
    query: patch.query || "",
  };
}

function mirrorImageLibraryFilters(filters) {
  state.ideaRefFilters.act = filters.scope;
  state.ideaRefFilters.tag = filters.tag;
  state.ideaRefFilters.query = filters.query;
  state.boardFilters.scene = filters.scope;
  state.boardFilters.tag = filters.tag;
  state.boardFilters.query = filters.query;
  state.whiteboxFilters.scene = filters.scope;
  state.whiteboxFilters.query = filters.query;
}

function setImageLibraryFilters(patch = {}, assets = allBoardImageAssets()) {
  const previous = normalizedImageLibraryFilters(state.imageLibraryFilters || state.ideaRefFilters || state.boardFilters || {});
  const next = {
    ...previous,
    ...imageLibraryFilterPatch(patch),
  };
  next.scope = effectiveImageScope(next.scope, assets);
  state.imageLibraryFilters = next;
  mirrorImageLibraryFilters(next);
  return next;
}

function currentImageLibraryFilters(assets = allBoardImageAssets()) {
  const next = normalizedImageLibraryFilters(state.imageLibraryFilters || state.ideaRefFilters || state.boardFilters || {});
  next.scope = effectiveImageScope(next.scope, assets);
  state.imageLibraryFilters = next;
  mirrorImageLibraryFilters(next);
  return next;
}

function boardAssetByRef(ref) {
  return allBoardImageAssets().find((asset) => asset.ref === ref) || null;
}

function boardNodeAsset(node) {
  return boardAssetByRef(node?.assetRef || "");
}

function boardSceneForNode(asset) {
  const scenes = state.detail?.scene_workbench?.scenes || [];
  if (asset?.scene_id) {
    const assetScene = scenes.find((item) => item.scene_id === asset.scene_id);
    if (assetScene) return assetScene;
  }
  return selectedScene() || scenes[0] || null;
}

function showBoardImageLightbox(asset) {
  const modal = $("boardImageLightbox");
  const img = $("boardImageLightboxImg");
  if (!asset?.url || !modal || !img) return;
  img.src = asset.url;
  img.alt = asset.asset_id || asset.path || "Board image";
  img.dataset.externalImageDrag = "true";
  img.dataset.dragImageUrl = asset.url || "";
  img.dataset.dragImagePath = asset.path || "";
  img.dataset.dragImageName = imageFileNameFromPath(asset.path || asset.asset_id || "");
  img.draggable = true;
  const download = $("boardImageLightboxDownload");
  if (download) {
    download.href = asset.url;
    download.download = imageFileNameFromPath(asset.path || asset.asset_id || "pipeline-image.png");
  }
  modal.hidden = false;
  document.body.classList.add("modal-open");
}

function openBoardImageLightbox(nodeId) {
  const node = state.boardNodes.find((item) => item.id === nodeId);
  showBoardImageLightbox(boardNodeAsset(node));
}

function openBoardAssetLightbox(assetRef) {
  showBoardImageLightbox(boardAssetByRef(assetRef));
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
  return imageLibraryScopeOptions(assets);
}

function boardAssetMatches(asset) {
  const filters = normalizedImageLibraryFilters(state.imageLibraryFilters || {});
  return imageAssetMatchesLibraryFilters(asset, { scene: filters.scope, tag: filters.tag, query: filters.query }, "scene");
}

function assetQaLabel(asset) {
  const score = asset?.qa_score;
  if (score === undefined || score === null || score === "") return "";
  return ` · QA ${score}`;
}

function boardNodeTitle(node) {
  const asset = boardNodeAsset(node);
  return asset?.asset_id || asset?.role || asset?.path || "Image";
}

function boardSceneById(sceneId) {
  const scenes = state.detail?.scene_workbench?.scenes || [];
  return scenes.find((scene) => scene.scene_id === sceneId) || null;
}

function boardOutputKindLabel(kind) {
  return BOARD_OUTPUT_KIND_OPTIONS.find((option) => option.value === kind)?.label || kindLabel(kind);
}

function boardOutputScopeOptions() {
  const scenes = state.detail?.scene_workbench?.scenes || [];
  const options = [{ value: "global", label: "全局资料库 / Global library" }];
  const acts = new Map();
  scenes.forEach((scene) => {
    if (scene.act_id) acts.set(scene.act_id, scene.act_title || scene.act_id);
  });
  acts.forEach((label, actId) => options.push({ value: `act:${actId}`, label: `整幕：${label}` }));
  scenes.forEach((scene) => {
    if (scene.scene_id) options.push({ value: `scene:${scene.scene_id}`, label: `${scene.scene_id} · ${scene.title || ""}` });
  });
  return options;
}

function boardOutputScopeLabel(scope) {
  const value = scope || "global";
  return boardOutputScopeOptions().find((option) => option.value === value)?.label || value;
}

function inferBoardOutputTarget(node, asset) {
  const haystack = [asset?.asset_id, asset?.role, asset?.path, asset?.kind, node?.note].join(" ").toLowerCase();
  let kind = asset?.kind && BOARD_OUTPUT_KIND_OPTIONS.some((option) => option.value === asset.kind) ? asset.kind : "storyboard_keyframe";
  if (haystack.includes("character") || haystack.includes("person") || haystack.includes("人设") || haystack.includes("人物") || haystack.includes("三视图")) kind = "character_ref";
  else if (haystack.includes("prop") || haystack.includes("道具")) kind = "prop_ref";
  else if (haystack.includes("scene_ref") || haystack.includes("location") || haystack.includes("environment") || haystack.includes("场景设定") || haystack.includes("场景参考")) kind = "scene_ref";
  else if (haystack.includes("lookdev") || haystack.includes("style") || haystack.includes("风格") || haystack.includes("色彩") || haystack.includes("光影")) kind = "lookdev";
  else if (haystack.includes("whitebox") || haystack.includes("白模")) kind = "whitebox";
  else if (asset?.kind === "image") kind = asset?.scene_id ? "storyboard_keyframe" : "image";

  const globallyUseful = ["character_ref", "prop_ref", "lookdev"].includes(kind) || haystack.includes("global") || haystack.includes("通用") || haystack.includes("全局");
  if (globallyUseful) return { scope: "global", kind };
  if (asset?.scene_id) return { scope: `scene:${asset.scene_id}`, kind };
  if (asset?.act_id) return { scope: `act:${asset.act_id}`, kind };
  const scene = selectedScene();
  return { scope: scene?.scene_id ? `scene:${scene.scene_id}` : "global", kind };
}

function boardOutputTargetForNode(node, asset = boardNodeAsset(node)) {
  const inferred = inferBoardOutputTarget(node, asset);
  const scopeOptions = boardOutputScopeOptions();
  const scope = node?.outputScope && scopeOptions.some((option) => option.value === node.outputScope) ? node.outputScope : inferred.scope;
  const kind = node?.outputKind && BOARD_OUTPUT_KIND_OPTIONS.some((option) => option.value === node.outputKind) ? node.outputKind : inferred.kind;
  return {
    scope,
    kind,
    note: node?.outputNote || "",
    inferred_scope: inferred.scope,
    inferred_kind: inferred.kind,
  };
}

function renderBoardOutputScopeOptions(selected) {
  return boardOutputScopeOptions()
    .map((option) => `<option value="${escapeHtml(option.value)}" ${selected === option.value ? "selected" : ""}>${escapeHtml(option.label)}</option>`)
    .join("");
}

function renderBoardOutputKindOptions(selected) {
  return BOARD_OUTPUT_KIND_OPTIONS.map(
    (option) => `<option value="${escapeHtml(option.value)}" ${selected === option.value ? "selected" : ""}>${escapeHtml(option.label)}</option>`,
  ).join("");
}

function boardOutputSuggestedCatalogPath(node, asset) {
  const target = boardOutputTargetForNode(node, asset);
  const stamp = new Date().toISOString().slice(0, 10).replaceAll("-", "");
  const stem = String(asset?.asset_id || asset?.path?.split("/").pop() || node?.id || "generated_image")
    .replace(/\.[^.]+$/, "")
    .replace(/[^A-Za-z0-9_-]+/g, "_")
    .replace(/^_+|_+$/g, "")
    .slice(0, 72) || "generated_image";
  const file = `${stem}_${stamp}.png`;
  if (target.scope === "global") {
    if (target.kind === "character_ref") return `05_asset_bible/characters/generated_refs/${file}`;
    if (target.kind === "scene_ref") return `05_asset_bible/locations/generated_refs/${file}`;
    if (target.kind === "prop_ref") return `05_asset_bible/props/generated_refs/${file}`;
    if (target.kind === "lookdev") return `04_lookdev/references/generated_refs/${file}`;
    return `08_generation/outputs/images/global/${file}`;
  }
  if (target.scope.startsWith("act:")) {
    const actId = target.scope.slice(4) || "act";
    return `08_generation/outputs/images/${actId}/${target.kind}/${file}`;
  }
  const sceneId = target.scope.startsWith("scene:") ? target.scope.slice(6) : asset?.scene_id || "PROJECT";
  return `08_generation/outputs/images/${sceneId}/${target.kind}/${file}`;
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
  return { x: Number(node.x || 0) + BOARD_NODE_WIDTH / 2, y: Number(node.y || 0) + BOARD_NODE_HEIGHT_FOR_LINKS / 2 };
}

function boardCanvasPoint(event) {
  const stage = $("referenceBoardCanvas")?.querySelector(".board-canvas-stage");
  const rect = stage?.getBoundingClientRect();
  if (!rect) return { x: 40, y: 40 };
  // rect is the post-transform (scaled) box, so divide back into the stage's logical coordinates.
  const scale = boardScale();
  return {
    x: clamp((event.clientX - rect.left) / scale - BOARD_NODE_WIDTH / 2, 12, Math.max(12, BOARD_STAGE_WIDTH - BOARD_NODE_WIDTH - 20)),
    y: clamp((event.clientY - rect.top) / scale - 80, 12, Math.max(12, BOARD_STAGE_HEIGHT - 260)),
  };
}

function boardDefaultNodePoint() {
  const lastNode = state.boardNodes[state.boardNodes.length - 1];
  if (lastNode) {
    const nextX = Number(lastNode.x || 0) + BOARD_NODE_WIDTH + 60;
    if (nextX <= 1600) return { x: nextX, y: Number(lastNode.y || 0) };
    return { x: 40, y: Number(lastNode.y || 0) + 380 };
  }
  return {
    x: 40,
    y: 40,
  };
}

function addBoardNode(assetRef, point) {
  const asset = boardAssetByRef(assetRef);
  if (!assetRef || !asset) return;
  const id = `node_${Date.now()}_${Math.random().toString(16).slice(2, 8)}`;
  const role = state.boardNodes.some((node) => node.role === "main") ? "reference" : "main";
  const outputTarget = inferBoardOutputTarget({ assetRef, note: "" }, asset);
  state.boardNodes.push({
    id,
    assetRef,
    role,
    note: "",
    outputScope: outputTarget.scope,
    outputKind: outputTarget.kind,
    outputNote: "",
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
    return false;
  }
  if (!targetId || sourceId === targetId) {
    toast("请选择另一张图片作为关联图 / Choose another image as reference");
    return false;
  }
  const existing = state.boardEdges.find((edge) => edge.sourceId === sourceId && edge.targetId === targetId);
  if (existing) {
    toast("这条关联已经存在 / Relation already exists");
    return false;
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
  return true;
}

function createBoardRelation(sourceId, targetId) {
  const source = state.boardNodes.find((node) => node.id === sourceId);
  const target = state.boardNodes.find((node) => node.id === targetId);
  if (!source || !target) return false;
  if (target.role === "main" && source.role !== "main") {
    return createBoardEdge(targetId, sourceId);
  }
  return createBoardEdge(sourceId, targetId);
}

function boardPromptForNode(node) {
  const asset = boardNodeAsset(node);
  const scene = boardSceneForNode(asset);
  const outputTarget = boardOutputTargetForNode(node, asset);
  const cardTarget = boardTargetCardForNode(node, asset);
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
    `Scene / 场戏: ${asset?.scene_id || scene?.scene_id || ""} ${asset?.scene_title || scene?.title || ""}`,
    `Main image / 主图: ${asset?.asset_id || asset?.path || ""}`,
    `Main path / 主图路径: ${asset?.path || ""}`,
    `Output routing / 出图归档: ${boardOutputScopeLabel(outputTarget.scope)} · ${boardOutputKindLabel(outputTarget.kind)}`,
    `Output routing note / 归档备注: ${outputTarget.note || "Use this routing when saving and cataloging the generated image."}`,
    "",
    "Target card / 目标卡片:",
    cardTarget
      ? `- ${cardTarget.card_type === "storyboard" ? "Storyboard" : "Concept"}: ${boardTargetCardLabel(cardTarget) || boardTargetCardId(cardTarget)}`
      : "- No fixed target card. Use output routing.",
    cardTarget ? "- Generated output must be saved as a new version on this target card, even if the main image comes from another source." : "",
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
    "- Before generating, optimize the brief like a film keyframe: sharpen staging, lighting, lens language, character continuity, and negative constraints.",
    "- Avoid noise, distorted anatomy, inconsistent character identity, unreadable composition, watermarks, random text, and unwanted new props.",
  ].join("\n");
}

function projectAbsolutePath(path = "") {
  const root = String(state.detail?.path || "").replace(/\/+$/, "");
  return root && path ? `${root}/${path}` : path;
}

function boardReferenceLines(node) {
  return boardNodeOutgoingEdges(node.id)
    .map((edge, index) => {
      const refNode = state.boardNodes.find((item) => item.id === edge.targetId);
      const refAsset = boardNodeAsset(refNode);
      if (!refNode || !refAsset) return "";
      return [
        `### Reference ${index + 1} / 关联图 ${index + 1}`,
        `- Asset: ${refAsset.asset_id || refAsset.path}`,
        `- Scene: ${refAsset.scene_id || "PROJECT"} ${refAsset.scene_title || ""}`,
        `- Project relative path: ${refAsset.path || ""}`,
        `- Absolute path: ${projectAbsolutePath(refAsset.path || "")}`,
        `- Browser URL: ${location.origin}${refAsset.url || ""}`,
        `- Reference note: ${refNode.note || ""}`,
        `- Relation note: ${edge.note || ""}`,
      ].join("\n");
    })
    .filter(Boolean)
    .join("\n\n");
}

function boardCardTargetForAsset(asset) {
  if (!asset?.card_type || !asset?.card_id) return null;
  if (asset.card_type === "concept") return { card_type: "concept", card_id: asset.card_id };
  if (asset.card_type === "storyboard") return { card_type: "storyboard", item_id: asset.card_id };
  return null;
}

function currentBoardTargetCard() {
  const target = state.boardTargetCard || null;
  if (!target?.card_type) return null;
  if (target.card_type === "concept" && target.card_id) return target;
  if (target.card_type === "storyboard" && target.item_id) return target;
  return null;
}

function storyboardCanvasTargetFromRow(row = {}, index = 0) {
  if (!row?.item_id) return null;
  return {
    card_type: "storyboard",
    item_id: row.item_id || "",
    row_index: index,
    act_id: row.act_id || "",
    scene_id: row.scene_id || "",
    title: row.beat || row.frame_description || row.item_id || "",
    summary: row.frame_description || row.image_prompt || row.notes || "",
  };
}

function boardTargetCardForNode(node, asset = boardNodeAsset(node)) {
  return currentBoardTargetCard() || boardCardTargetForAsset(asset);
}

function boardTargetCardId(target = currentBoardTargetCard()) {
  if (!target) return "";
  return target.card_type === "concept" ? target.card_id || "" : target.item_id || "";
}

function boardTargetCardLabel(target = currentBoardTargetCard()) {
  if (!target) return "";
  const id = boardTargetCardId(target);
  const title = target.title || target.summary || "";
  return [id, title].filter(Boolean).join(" · ");
}

function renderBoardTargetBanner() {
  const target = currentBoardTargetCard();
  if (!target) return "";
  return `
    <div class="board-target-banner">
      <div>
        <strong>分镜专属画布 / Shot-specific canvas</strong>
        <span>输出默认回传到：${escapeHtml(boardTargetCardLabel(target) || "当前分镜")}</span>
      </div>
      <small>仍可拖入任意主图和多张参考图；生成按钮只为这张分镜创建精修回填包。</small>
    </div>
  `;
}

function boardReferencePayloads(node) {
  return boardNodeOutgoingEdges(node.id)
    .map((edge, index) => {
      const refNode = state.boardNodes.find((item) => item.id === edge.targetId);
      const refAsset = boardNodeAsset(refNode);
      if (!refNode || !refAsset) return null;
      return {
        index: index + 1,
        asset_ref: refAsset.ref || "",
        asset_id: refAsset.asset_id || refAsset.path || "",
        path: refAsset.path || "",
        origin: refAsset.origin || "project",
        kind: refAsset.kind || "image",
        scene_id: refAsset.scene_id || "",
        scene_title: refAsset.scene_title || "",
        version_id: refAsset.version_id || "",
        version_status: refAsset.version_status || "",
        card_type: refAsset.card_type || "",
        card_id: refAsset.card_id || "",
        note: refNode.note || "",
        relation_note: edge.note || "",
        browser_url: `${location.origin}${refAsset.url || ""}`,
      };
    })
    .filter(Boolean);
}

function boardCardPacketPayload(node, asset) {
  const target = boardTargetCardForNode(node, asset);
  const outputTarget = boardOutputTargetForNode(node, asset);
  const catalogPath = boardOutputSuggestedCatalogPath(node, asset);
  return {
    ...target,
    source_asset: {
      asset_ref: asset.ref || "",
      asset_id: asset.asset_id || asset.path || "",
      path: asset.path || "",
      origin: asset.origin || "project",
      kind: asset.kind || "image",
      scene_id: asset.scene_id || "",
      scene_title: asset.scene_title || "",
      act_id: asset.act_id || "",
      act_title: asset.act_title || "",
      version_id: asset.version_id || "",
      version_status: asset.version_status || "",
      card_type: asset.card_type || "",
      card_id: asset.card_id || "",
      card_title: asset.card_title || "",
      card_category: asset.card_category || "",
      card_summary: asset.card_summary || "",
      card_prompt: asset.card_prompt || "",
      qa_score: asset.qa_score ?? "",
      browser_url: `${location.origin}${asset.url || ""}`,
    },
    references: boardReferencePayloads(node),
    routing: {
      scope: outputTarget.scope,
      scope_label: boardOutputScopeLabel(outputTarget.scope),
      kind: outputTarget.kind,
      kind_label: boardOutputKindLabel(outputTarget.kind),
      note: outputTarget.note || "",
      suggested_catalog_path: catalogPath,
      suggested_catalog_absolute_path: projectAbsolutePath(catalogPath),
    },
    board_note: node.note || "",
    generation_prompt: boardPromptForNode(node),
  };
}

function buildBoardHandoffText(node, result) {
  const asset = boardNodeAsset(node);
  const scene = boardSceneForNode(asset);
  const outputTarget = boardOutputTargetForNode(node, asset);
  const catalogPath = boardOutputSuggestedCatalogPath(node, asset);
  const packetPath = result.outputPath || "";
  const suggestedOutput = packetPath
    ? packetPath.replace(/\/outputs\/(.+?)\.md$/i, "/outputs/$1.png")
    : `08_generation/outputs/${asset?.asset_id || "board_image"}_${Date.now()}.png`;
  return [
    "# Codex Image Generation Handoff / Codex 生图交接包",
    "",
    "请解析这个资料包，调用当前聊天里的真实生图能力生成新图。生成完成后，将图片写回本地项目，并优先保存到 Suggested output path；如果我要替换原图，再替换 Target asset path 并更新相关记录。",
    "",
    "## Codex Run Mode / Codex 执行模式",
    "- 快速出图：除非素材缺失、路径错误或安全策略阻止，不要逐步汇报读取、复制、写入、API 回填等执行细节；直接完成生成并展示图片。",
    "- 生成前优化：先根据主图备注、关联图、连线说明和电影制作经验，做一次电影级提示词优化，再调用真实生图能力。",
    "- 回填前看 Output Routing：它决定生成图是分镜关键帧，还是全局/场景内的人设、场景、道具、风格参考。",
    "- 输出保持短：只给 3 条以内关键优化意见、最终图片预览、保存路径和是否已回填记录。",
    "- 不要覆盖 Target asset path，除非我明确说替换原图。",
    "",
    "## Cinematic Optimization Brief / 电影级优化要求",
    "- 强化镜头语言：构图层次、机位、景别、主体动线、视线方向必须清楚。",
    "- 强化光影和质感：明确主光、环境光、雨夜/室内/霓虹等材质反应，避免灰脏、噪点和随机纹理。",
    "- 强化连续性：人物身份、服装、道具、空间关系要和主图及关联图一致。",
    "- 强化负面约束：避免畸形手脸、乱码文字、水印、额外人物、无关道具、过度锐化、低清噪点。",
    "",
    "## Project / 项目",
    `- Project slug: ${state.selectedSlug || ""}`,
    `- Project root: ${state.detail?.path || ""}`,
    `- Scene: ${scene?.scene_id || asset?.scene_id || ""} ${scene?.title || asset?.scene_title || ""}`,
    `- Created at: ${new Date().toLocaleString()}`,
    `- Adapter result: ${result.message || ""}`,
    "",
    "## Output Routing / 出图归档标签",
    `- Routing scope: ${outputTarget.scope}`,
    `- Routing scope label: ${boardOutputScopeLabel(outputTarget.scope)}`,
    `- Asset kind: ${outputTarget.kind}`,
    `- Asset kind label: ${boardOutputKindLabel(outputTarget.kind)}`,
    `- Auto inferred scope: ${outputTarget.inferred_scope}`,
    `- Auto inferred kind: ${outputTarget.inferred_kind}`,
    `- User routing note: ${outputTarget.note || ""}`,
    `- Suggested catalog path: ${catalogPath}`,
    `- Suggested catalog absolute path: ${projectAbsolutePath(catalogPath)}`,
    "- Save first to Suggested output path. If the result is accepted, also catalog/copy it according to this routing tag.",
    "",
    "## Main Image / 主图",
    `- Asset: ${asset?.asset_id || asset?.path || ""}`,
    `- Source card type: ${asset?.card_type || ""}`,
    `- Source card id: ${asset?.card_id || ""}`,
    `- Source card version: ${asset?.version_id || ""} · ${asset?.version_status || ""}`,
    `- Stage: ${asset?.stage || ""}`,
    `- Kind: ${kindLabel(asset?.kind)}`,
    `- Target asset path: ${asset?.path || ""}`,
    `- Target absolute path: ${projectAbsolutePath(asset?.path || "")}`,
    `- Browser URL: ${location.origin}${asset?.url || ""}`,
    `- Main note: ${node.note || ""}`,
    "",
    "## References / 关联图",
    boardReferenceLines(node) || "- No linked references.",
    "",
    "## Generation Prompt / 生成提示词",
    "```text",
    boardPromptForNode(node),
    "```",
    "",
    "## Existing Task Packet / 现有任务包",
    `- Packet path: ${packetPath}`,
    `- Packet absolute path: ${projectAbsolutePath(packetPath)}`,
    `- Change request id: ${result.changeRequestId || ""}`,
    `- Queue id: ${result.queueId || ""}`,
    `- Target version: ${result.targetVersion || ""}`,
    `- Suggested output path: ${suggestedOutput}`,
    `- Suggested output absolute path: ${projectAbsolutePath(suggestedOutput)}`,
    `- Scene output callback: POST ${location.origin}/api/projects/${state.selectedSlug || ""}/scene-output`,
    "",
    "## Replacement Instruction / 回填说明",
    "- Generate one clean high-quality image first.",
    "- Save the generated file into Suggested output path.",
    "- Then update the project version/change-request record with Scene output callback when Change request id and Queue id are present.",
    "- If Output Routing says global character/scene/prop/lookdev reference, keep it as reusable reference material instead of treating it as a shot replacement.",
    "- Do not overwrite Target asset path unless I explicitly say replace original.",
  ].join("\n");
}

function addBoardHandoff(node, result) {
  const asset = boardNodeAsset(node);
  if (!node || !asset) return;
  const id = `handoff_${Date.now()}_${Math.random().toString(16).slice(2, 8)}`;
  const handoff = {
    id,
    title: `${asset.asset_id || asset.path || "Board image"} → Codex`,
    scene: asset.scene_id || selectedScene()?.scene_id || "PROJECT",
    status: result.status || "packet",
    outputPath: result.outputPath || "",
    createdAt: new Date().toLocaleString(),
    text: result.handoffText || buildBoardHandoffText(node, result),
    autoCopy: true,
  };
  state.boardHandoffs = [handoff, ...state.boardHandoffs.filter((item) => item.outputPath !== handoff.outputPath)].slice(0, 12);
  state.boardHandoffCollapsed = false;
  autoCopyHandoffText(handoff.text);
  syncIdeaHandoffCompletionPolling();
}

function removeBoardHandoff(handoffId) {
  state.boardHandoffs = state.boardHandoffs.filter((item) => item.id !== handoffId);
  if (!state.boardHandoffs.length) state.boardHandoffCollapsed = false;
  saveBoardState();
  renderReferenceBoard();
}

function clearBoardHandoffs() {
  state.boardHandoffs = [];
  state.boardHandoffCollapsed = false;
  saveBoardState();
  renderReferenceBoard();
}

function toggleBoardHandoffDock() {
  state.boardHandoffCollapsed = !state.boardHandoffCollapsed;
  saveBoardState();
  renderBoardHandoffDock();
  bindBoardHandoffEvents();
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
      queueId: packetItem?.queue_id || "",
      assetId: packetItem?.asset_id || "",
      targetVersion: packetItem?.target_version || "",
      message: "已生成任务包，当前未启用直接出图适配器 / Packet ready; no direct image adapter is enabled.",
    };
  }
  if (finalItem?.final_output_path) {
    return {
      status: "image",
      outputPath: finalItem.final_output_path,
      queueId: finalItem.queue_id || "",
      assetId: finalItem.asset_id || "",
      targetVersion: finalItem.target_version || "",
      message: `图片已生成 / Image generated: ${finalItem.final_output_path}`,
    };
  }
  return {
    status: run.status === "generation_failed" ? "failed" : "packet",
    outputPath: packetItem?.packet_path || packetItem?.result_path || "",
    queueId: packetItem?.queue_id || finalItem?.queue_id || "",
    assetId: packetItem?.asset_id || finalItem?.asset_id || "",
    targetVersion: packetItem?.target_version || finalItem?.target_version || "",
    message: "生成器已运行，但没有回填图片路径 / Adapter ran, but no image output path was attached.",
  };
}

async function createBoardCardGenerationPacket(nodeId) {
  const node = state.boardNodes.find((item) => item.id === nodeId);
  const asset = boardNodeAsset(node);
  const target = boardTargetCardForNode(node, asset);
  if (!node || !asset || !target) {
    toast("这张图没有绑定到文字卡片，或未打开分镜专属画布 / This image is not linked to a card version or shot canvas target");
    return;
  }
  if (state.busy) {
    toast("已有任务正在执行 / Another task is running");
    return;
  }
  state.busy = true;
  node.lastGeneration = {
    status: "running",
    message: "正在创建卡片精修包 / Creating card refinement packet...",
    outputPath: "",
  };
  setBoardGeneration(nodeId, 18, node.lastGeneration.message);
  try {
    setBoardGeneration(nodeId, 58, "正在写入回填信息 / Writing card callback...");
    const result = await requestJson(`/api/projects/${state.selectedSlug}/board-card-packet`, {
      method: "POST",
      body: JSON.stringify(boardCardPacketPayload(node, asset)),
    });
    state.detail = result.project || state.detail;
    const packetResult = {
      status: "packet",
      outputPath: result.packet_path || "",
      message: "已生成卡片精修包，可拖给 Codex 生图并回填到目标卡片 / Card refinement packet ready.",
      handoffText: result.handoff_text || "",
      suggestedOutputPath: result.suggested_output_path || "",
      cardTarget: target,
    };
    node.lastGeneration = {
      ...packetResult,
      completedAt: new Date().toLocaleString(),
    };
    addBoardHandoff(node, packetResult);
    saveBoardState();
    setBoardGeneration(nodeId, 100, packetResult.message);
    renderAll();
    renderReferenceBoard();
    toast(packetResult.message);
  } catch (error) {
    node.lastGeneration = {
      status: "failed",
      message: error.message,
      outputPath: "",
      completedAt: new Date().toLocaleString(),
    };
    saveBoardState();
    setBoardGeneration(nodeId, 100, `生成失败 / Failed: ${error.message}`);
    toast(`卡片精修包失败 / Card refinement failed: ${error.message}`);
  } finally {
    state.busy = false;
    window.setTimeout(clearBoardGeneration, 1600);
  }
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
  const scene = boardSceneForNode(asset);
  if (!node || !asset) {
    toast("画布节点缺少图片信息 / Board node is missing image context");
    return;
  }
  if (boardTargetCardForNode(node, asset)) {
    await createBoardCardGenerationPacket(nodeId);
    return;
  }
  if (!scene) {
    toast("项目还没有可用于生成任务的场戏 / Project has no scene context for generation");
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
    const result = {
      ...boardGenerationMessageFromRun(runResult, adapter),
      changeRequestId: request.change_request_id || "",
      adapterId,
    };
    node.lastGeneration = {
      ...result,
      completedAt: new Date().toLocaleString(),
    };
    addBoardHandoff(node, result);
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
  const outputTarget = boardOutputTargetForNode(node, asset);
  const cardTarget = boardTargetCardForNode(node, asset);
  const cardTargetLabel = boardTargetCardLabel(cardTarget);
  return `
    <article class="board-node-card ${escapeHtml(node.role || "reference")} ${activeLink ? "linking" : ""} ${activeGeneration ? "generating" : ""}" data-node-id="${escapeHtml(node.id)}" style="left:${Number(node.x || 0)}px; top:${Number(node.y || 0)}px;">
      <header class="board-node-header">
        <div class="board-node-role-row">
          <select class="board-node-role" data-node-id="${escapeHtml(node.id)}">
            <option value="main" ${node.role === "main" ? "selected" : ""}>主图 / Main</option>
            <option value="reference" ${node.role !== "main" ? "selected" : ""}>关联图 / Reference</option>
          </select>
          <button class="icon-button board-node-remove" data-node-id="${escapeHtml(node.id)}" type="button" title="移除 / Remove">×</button>
        </div>
        <div class="board-node-link-row">
          <button class="mini-command board-link-source" data-help="从这张图发起一条关系线。通常主图用它连接到人物、白模、道具等关联图。" data-node-id="${escapeHtml(node.id)}" type="button" title="从这张图发起关联线 / Link from this image">${activeLink ? "等待 / Linking" : "主图线 / From"}</button>
          <button class="mini-command board-link-target" data-help="把这张图接到上一张主图线上，作为参考元素参与重生成。" data-node-id="${escapeHtml(node.id)}" type="button" title="把这张图连为关联图 / Link this as a reference">关联 / To</button>
          <button class="board-link-drag" data-help="按住拖到另一张图上建立关联线。拖到主图时会自动把这张图作为参考放进主图生成包。" data-node-id="${escapeHtml(node.id)}" type="button" title="拖拽建立关联 / Drag to link">↗</button>
        </div>
      </header>
      <img class="board-node-image" data-node-id="${escapeHtml(node.id)}" src="${escapeHtml(asset.url)}" alt="${escapeHtml(asset.asset_id || asset.path)}" title="双击预览大图；也可拖到外部上传区 / Double-click to preview; drag to external upload" ${externalImageDragAttrs(asset.url, asset.path, asset.asset_id || asset.path)} />
      <div class="board-node-meta">
        <strong>${escapeHtml(asset.asset_id || asset.role || asset.path)}</strong>
        <small>${escapeHtml(asset.scene_id || "PROJECT")} · ${escapeHtml(kindLabel(asset.kind))} · ${escapeHtml(asset.path || "")}</small>
        ${cardTarget ? `<small class="board-card-target">回填目标 / Target card: ${escapeHtml(cardTargetLabel || boardTargetCardId(cardTarget))}</small>` : ""}
      </div>
      <label>${escapeHtml(boardNodeNoteLabel(node))}
        <textarea class="board-node-note" data-node-id="${escapeHtml(node.id)}" rows="4" placeholder="${node.role === "main" ? "完整描述要生成的新图 / Describe the full new image" : "说明要借用什么元素 / Describe what to borrow"}">${escapeHtml(node.note || "")}</textarea>
      </label>
      <div class="board-output-routing">
        <label>归档位置 / Save to
          <select class="board-output-scope" data-node-id="${escapeHtml(node.id)}">
            ${renderBoardOutputScopeOptions(outputTarget.scope)}
          </select>
        </label>
        <label>资产类型 / Asset type
          <select class="board-output-kind" data-node-id="${escapeHtml(node.id)}">
            ${renderBoardOutputKindOptions(outputTarget.kind)}
          </select>
        </label>
        <input class="board-output-note" data-node-id="${escapeHtml(node.id)}" value="${escapeHtml(outputTarget.note || "")}" placeholder="归档备注，可留空 / Routing note" />
      </div>
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
        <a class="board-download-link" ${downloadImageAttrs(asset.url, asset.path, asset.asset_id || asset.path)}>下载原图</a>
        <button class="command-button primary board-generate-node" data-help="${cardTarget ? "把当前主图、关联图和画布备注整理成单卡精修包，生成后默认回填到目标卡片。" : "汇总主图、关联图、连线说明和备注，生成可交给 Codex 处理的图片任务包。"}" data-node-id="${escapeHtml(node.id)}" type="button" ${state.busy ? "disabled" : ""}>${activeGeneration ? `生成中 ${progress}%` : cardTarget ? "精修入卡 / Revise Card" : "生成 / Generate"}</button>
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
  const scale = boardScale();
  root.innerHTML = `
    ${renderBoardTargetBanner()}
    <div class="board-zoom-toolbar-wrap">
      <div class="board-zoom-toolbar" role="group" aria-label="缩放 / Zoom">
        <button class="board-zoom-out" type="button" title="缩小 / Zoom out">−</button>
        <button class="board-zoom-level" type="button" title="重置缩放 / Reset zoom">${Math.round(scale * 100)}%</button>
        <button class="board-zoom-in" type="button" title="放大 / Zoom in">+</button>
      </div>
    </div>
    <div class="board-canvas-viewport" style="width:${Math.round(BOARD_STAGE_WIDTH * scale)}px; height:${Math.round(BOARD_STAGE_HEIGHT * scale)}px;">
      <div class="board-canvas-stage" style="transform:scale(${scale}); transform-origin:0 0;">
        ${renderBoardEdges()}
        ${
          state.boardNodes.length
            ? state.boardNodes.map(renderBoardNode).join("")
            : `<div class="board-empty-state">从下方素材栏拖入图片 / Drag images from the dock below</div>`
        }
      </div>
    </div>
  `;
}

function renderBoardFilters(assets) {
  const sceneFilter = $("boardSceneFilter");
  const tagFilter = $("boardTagFilter");
  const search = $("boardSearchInput");
  if (!sceneFilter || !tagFilter || !search) return;
  const filters = currentImageLibraryFilters(assets);
  sceneFilter.innerHTML = boardSceneFilterOptions(assets)
    .map((option) => `<option value="${escapeHtml(option.value)}" ${filters.scope === option.value ? "selected" : ""}>${escapeHtml(option.label)}</option>`)
    .join("");
  tagFilter.innerHTML = BOARD_TAG_OPTIONS.map(
    (option) => `<option value="${escapeHtml(option.value)}" ${filters.tag === option.value ? "selected" : ""}>${escapeHtml(option.label)}</option>`,
  ).join("");
  search.value = filters.query || "";
}

function renderBoardHandoffDock() {
  const root = $("boardHandoffDock");
  if (!root) return;
  if (!state.boardHandoffs.length) {
    root.innerHTML = `
      <div class="board-handoff-empty">
        <strong>Codex 交接区 / Codex handoff</strong>
        <span>点击节点 Generate 后，这里会出现可拖进聊天框的生图资料包。</span>
      </div>
    `;
    return;
  }
  const latest = state.boardHandoffs[0];
  const collapsed = Boolean(state.boardHandoffCollapsed);
  root.innerHTML = `
    <div class="board-handoff-header">
      <div>
        <strong>Codex 交接区 / Codex handoff</strong>
        <span>${state.boardHandoffs.length} 个资料包${collapsed && latest ? ` · 最新: ${escapeHtml(latest.title)}` : " · 拖拽到聊天框或复制"}</span>
      </div>
      <div class="board-handoff-header-actions">
        <button class="mini-command board-clear-handoffs" data-help="清掉画板里的临时 Codex 交接卡，不删除图片和项目记录。" type="button">清空 / Clear</button>
        <button class="mini-command board-toggle-handoffs" data-help="只展开或收起交接区，不影响任务包文件。" type="button">${collapsed ? "展开 / Expand" : "最小化 / Minimize"}</button>
      </div>
    </div>
    <div class="board-handoff-list" ${collapsed ? "hidden" : ""}>
      ${state.boardHandoffs
        .map(
          (handoff) => `
            <article class="board-handoff-card ${escapeHtml(handoff.status || "")}" draggable="true" data-handoff-id="${escapeHtml(handoff.id)}">
              <div>
                <strong>${escapeHtml(handoff.title)}</strong>
                <small>${escapeHtml(handoff.scene || "PROJECT")} · ${escapeHtml(handoff.createdAt || "")}</small>
                ${handoff.outputPath ? `<small>${escapeHtml(handoff.outputPath)}</small>` : ""}
                ${handoff.autoCopy ? `<small class="handoff-copy-hint">已尝试自动复制 / Auto-copy attempted</small>` : ""}
              </div>
              <div class="board-handoff-actions">
                <button class="mini-command board-copy-handoff" data-handoff-id="${escapeHtml(handoff.id)}" type="button">复制 / Copy</button>
                <button class="icon-button board-delete-handoff" data-handoff-id="${escapeHtml(handoff.id)}" type="button" title="删除交接卡 / Delete handoff">×</button>
              </div>
              <details class="board-handoff-detail">
                <summary>展开完整资料包 / Show packet text</summary>
                <textarea readonly rows="6">${escapeHtml(handoff.text || "")}</textarea>
              </details>
            </article>
          `,
        )
        .join("")}
    </div>
  `;
}

function renderBoardAssetTray() {
  const tray = $("boardAssetTray");
  if (!tray) return;
  const assets = allBoardImageAssets();
  currentImageLibraryFilters(assets);
  renderBoardFilters(assets);
  const visible = assets.filter(boardAssetMatches).slice(0, 160);
  tray.innerHTML = visible.length
    ? visible
        .map(
          (asset) => {
            const versionLabel = asset.version_status ? CARD_VERSION_STATUS_LABELS[asset.version_status] || asset.version_status : "";
            return `
            <article class="board-asset-card" data-ref="${escapeHtml(asset.ref)}" title="双击预览大图；拖入画板建立节点 / Double-click to preview; drag into board · ${escapeHtml(asset.path || "")}">
              <img src="${escapeHtml(asset.url)}" alt="${escapeHtml(asset.asset_id || asset.path)}" draggable="false" />
              <strong>${escapeHtml(asset.asset_id || asset.role || asset.path)}</strong>
              <small>${escapeHtml(asset.scene_id || asset.act_id || "PROJECT")} · ${escapeHtml(kindLabel(asset.kind))}${versionLabel ? ` · ${escapeHtml(versionLabel)}` : ""}${escapeHtml(assetQaLabel(asset))}</small>
              ${asset.card_id ? `<small>${escapeHtml(asset.card_id)}${asset.card_title ? ` · ${escapeHtml(asset.card_title)}` : ""}</small>` : ""}
              <div class="board-asset-actions">
                <a class="board-download-link" ${downloadImageAttrs(asset.url, asset.path, asset.asset_id || asset.path)}>下载</a>
              </div>
            </article>
          `;
          },
        )
        .join("")
    : `<div class="empty-state">没有匹配图片 / No matching images.</div>`;
}

function startBoardLinkDrag(event, sourceId, moveEventName = "pointermove", upEventName = "pointerup") {
  const canvas = $("referenceBoardCanvas");
  const sourceCard = [...(canvas?.querySelectorAll(".board-node-card") || [])].find((card) => card.dataset.nodeId === sourceId);
  if (!canvas || !sourceId || !sourceCard) return;
  if (boardLinkDragActive) return;
  boardLinkDragActive = true;
  event.preventDefault();
  event.stopPropagation();
  let moved = false;
  let targetCard = null;
  const ghost = document.createElement("div");
  ghost.className = "board-link-drag-ghost";
  ghost.textContent = "↗";
  document.body.appendChild(ghost);
  document.body.classList.add("board-link-dragging");
  sourceCard.classList.add("board-link-drag-source");
  const setTarget = (card) => {
    if (targetCard === card) return;
    targetCard?.classList.remove("board-link-drop-target");
    targetCard = card;
    targetCard?.classList.add("board-link-drop-target");
  };
  const onMove = (moveEvent) => {
    moved = true;
    ghost.style.left = `${moveEvent.clientX}px`;
    ghost.style.top = `${moveEvent.clientY}px`;
    const card = document
      .elementFromPoint(moveEvent.clientX, moveEvent.clientY)
      ?.closest?.(".board-node-card");
    setTarget(card && canvas.contains(card) && card.dataset.nodeId !== sourceId ? card : null);
  };
  const onUp = (upEvent) => {
    document.removeEventListener(moveEventName, onMove);
    document.removeEventListener(upEventName, onUp);
    boardLinkDragActive = false;
    ghost.remove();
    document.body.classList.remove("board-link-dragging");
    sourceCard.classList.remove("board-link-drag-source");
    const dropCard = document
      .elementFromPoint(upEvent.clientX, upEvent.clientY)
      ?.closest?.(".board-node-card");
    const targetId = dropCard && canvas.contains(dropCard) ? dropCard.dataset.nodeId || "" : "";
    setTarget(null);
    if (targetId && targetId !== sourceId) {
      createBoardRelation(sourceId, targetId);
    } else if (moved) {
      toast("把指针拖到另一张卡片上建立关联 / Drop on another card to link");
    }
  };
  document.addEventListener(moveEventName, onMove);
  document.addEventListener(upEventName, onUp);
}

function bindBoardNodeDrag() {
  const canvas = $("referenceBoardCanvas");
  if (!canvas) return;
  canvas.onpointerdown = (event) => {
    if (event.button !== 0) return;
    const linkHandle = event.target?.closest?.(".board-link-drag");
    if (linkHandle && canvas.contains(linkHandle)) {
      startBoardLinkDrag(event, linkHandle.dataset.nodeId || "");
      return;
    }
    const armedTargetCard = event.target?.closest?.(".board-node-card");
    if (
      state.boardLinkSourceId &&
      armedTargetCard &&
      canvas.contains(armedTargetCard) &&
      !event.target?.closest?.("button, input, select, textarea, a") &&
      armedTargetCard.dataset.nodeId !== state.boardLinkSourceId
    ) {
      event.preventDefault();
      createBoardRelation(state.boardLinkSourceId, armedTargetCard.dataset.nodeId || "");
      return;
    }
    if (event.target?.closest?.("button, input, select, textarea, a, .board-node-image")) return;
    const card = event.target?.closest?.(".board-node-card");
    if (!card || !canvas.contains(card)) return;
    const nodeId = card.dataset.nodeId || "";
    const node = state.boardNodes.find((item) => item.id === nodeId);
    const stage = canvas.querySelector(".board-canvas-stage");
    if (!node || !stage) return;
    event.preventDefault();
    card.setPointerCapture?.(event.pointerId);
    const startX = event.clientX;
    const startY = event.clientY;
    const originalX = Number(node.x || 0);
    const originalY = Number(node.y || 0);
    const scale = boardScale();
    const maxX = Math.max(12, BOARD_STAGE_WIDTH - BOARD_NODE_WIDTH - 20);
    const maxY = Math.max(12, BOARD_STAGE_HEIGHT - 320);
    const onMove = (moveEvent) => {
      // Pointer travel is in screen pixels; divide by scale to move in stage units.
      node.x = Math.round(clamp(originalX + (moveEvent.clientX - startX) / scale, 12, maxX));
      node.y = Math.round(clamp(originalY + (moveEvent.clientY - startY) / scale, 12, maxY));
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
  };
  canvas.onmousedown = (event) => {
    if (event.button !== 0) return;
    const linkHandle = event.target?.closest?.(".board-link-drag");
    if (!linkHandle || !canvas.contains(linkHandle)) return;
    startBoardLinkDrag(event, linkHandle.dataset.nodeId || "", "mousemove", "mouseup");
  };
}

function bindBoardAssetTrayEvents() {
  const tray = $("boardAssetTray");
  if (!tray) return;
  tray.onpointerdown = (event) => {
    if (event.button !== 0) return;
    if (event.target?.closest?.("a, button")) return;
    const card = event.target?.closest?.(".board-asset-card");
    if (!card || !tray.contains(card)) return;
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
  };
  tray.ondblclick = (event) => {
    const card = event.target?.closest?.(".board-asset-card");
    if (!card || !tray.contains(card)) return;
    event.preventDefault();
    openBoardAssetLightbox(card.dataset.ref || "");
  };
}

function bindBoardHandoffEvents() {
  const dock = $("boardHandoffDock");
  if (!dock) return;
  dock.ondragstart = (event) => {
    const card = event.target?.closest?.(".board-handoff-card");
    if (!card || !dock.contains(card)) return;
    const handoff = state.boardHandoffs.find((item) => item.id === card.dataset.handoffId);
    if (!handoff) return;
    event.dataTransfer?.setData("text/plain", handoff.text || "");
    event.dataTransfer?.setData("text/markdown", handoff.text || "");
    event.dataTransfer?.setData("text/codex-handoff-id", handoff.id);
    event.dataTransfer.effectAllowed = "copy";
  };
  dock.onclick = async (event) => {
    const toggleButton = event.target?.closest?.(".board-toggle-handoffs");
    if (toggleButton && dock.contains(toggleButton)) {
      event.preventDefault();
      toggleBoardHandoffDock();
      return;
    }
    const clearButton = event.target?.closest?.(".board-clear-handoffs");
    if (clearButton && dock.contains(clearButton)) {
      event.preventDefault();
      clearBoardHandoffs();
      toast("已清空交接卡 / Handoff cards cleared");
      return;
    }
    const copyButton = event.target?.closest?.(".board-copy-handoff");
    if (copyButton && dock.contains(copyButton)) {
      event.stopPropagation();
      const handoff = state.boardHandoffs.find((item) => item.id === copyButton.dataset.handoffId);
      if (!handoff) return;
      try {
        await navigator.clipboard.writeText(handoff.text || "");
        toast("已复制 Codex 资料包 / Handoff copied");
      } catch {
        const textarea = copyButton.closest(".board-handoff-card")?.querySelector("textarea");
        textarea?.select?.();
        const copied = document.execCommand?.("copy");
        toast(copied ? "已复制 Codex 资料包 / Handoff copied" : "复制失败，可展开文本手动复制 / Copy failed; expand text and copy manually");
      }
      return;
    }
    const deleteButton = event.target?.closest?.(".board-delete-handoff");
    if (deleteButton && dock.contains(deleteButton)) {
      event.preventDefault();
      event.stopPropagation();
      removeBoardHandoff(deleteButton.dataset.handoffId || "");
    }
  };
}

function bindReferenceBoardEvents() {
  bindBoardHandoffEvents();
  bindBoardAssetTrayEvents();
  const sceneFilter = $("boardSceneFilter");
  if (sceneFilter) sceneFilter.onchange = (event) => {
    setImageLibraryFilters({ scope: event.target.value }, allBoardImageAssets());
    renderReferenceBoard();
  };
  const tagFilter = $("boardTagFilter");
  if (tagFilter) tagFilter.onchange = (event) => {
    setImageLibraryFilters({ tag: event.target.value }, allBoardImageAssets());
    renderReferenceBoard();
  };
  const searchInput = $("boardSearchInput");
  if (searchInput) searchInput.oninput = (event) => {
    setImageLibraryFilters({ query: event.target.value }, allBoardImageAssets());
    renderBoardAssetTray();
  };
  const canvas = $("referenceBoardCanvas");
  if (canvas) {
    canvas.onchange = (event) => {
      const roleSelect = event.target?.closest?.(".board-node-role");
      if (roleSelect && canvas.contains(roleSelect)) {
        const node = state.boardNodes.find((item) => item.id === roleSelect.dataset.nodeId);
        if (node) node.role = roleSelect.value === "main" ? "main" : "reference";
        saveBoardState();
        renderReferenceBoard();
        return;
      }
      const outputScope = event.target?.closest?.(".board-output-scope");
      if (outputScope && canvas.contains(outputScope)) {
        const node = state.boardNodes.find((item) => item.id === outputScope.dataset.nodeId);
        if (node) node.outputScope = outputScope.value || "";
        saveBoardState();
        return;
      }
      const outputKind = event.target?.closest?.(".board-output-kind");
      if (outputKind && canvas.contains(outputKind)) {
        const node = state.boardNodes.find((item) => item.id === outputKind.dataset.nodeId);
        if (node) node.outputKind = outputKind.value || "";
        saveBoardState();
      }
    };
    canvas.oninput = (event) => {
      const nodeNote = event.target?.closest?.(".board-node-note");
      if (nodeNote && canvas.contains(nodeNote)) {
        const node = state.boardNodes.find((item) => item.id === nodeNote.dataset.nodeId);
        if (node) node.note = nodeNote.value;
        saveBoardState();
        return;
      }
      const outputNote = event.target?.closest?.(".board-output-note");
      if (outputNote && canvas.contains(outputNote)) {
        const node = state.boardNodes.find((item) => item.id === outputNote.dataset.nodeId);
        if (node) node.outputNote = outputNote.value;
        saveBoardState();
        return;
      }
      const edgeNote = event.target?.closest?.(".board-edge-note");
      if (edgeNote && canvas.contains(edgeNote)) {
        const edge = state.boardEdges.find((item) => item.id === edgeNote.dataset.edgeId);
        if (edge) edge.note = edgeNote.value;
        saveBoardState();
      }
    };
    canvas.ondblclick = (event) => {
      const image = event.target?.closest?.(".board-node-image");
      if (!image) return;
      event.preventDefault();
      openBoardImageLightbox(image.dataset.nodeId || "");
    };
    // Trackpad pinch on Chromium/Atlas arrives as a wheel event with ctrlKey set.
    canvas.onwheel = (event) => {
      if (!event.ctrlKey) return;
      event.preventDefault();
      const factor = Math.exp(-event.deltaY * 0.01);
      setBoardScale(boardScale() * factor, event);
    };
    canvas.ondragstart = (event) => {
      const linkHandle = event.target?.closest?.(".board-link-drag");
      if (!linkHandle || !canvas.contains(linkHandle)) return;
      event.dataTransfer?.setData("application/x-board-link-node", linkHandle.dataset.nodeId || "");
      event.dataTransfer?.setData("text/plain", `board-link:${linkHandle.dataset.nodeId || ""}`);
      event.dataTransfer.effectAllowed = "link";
    };
    canvas.ondragover = (event) => {
      const types = [...(event.dataTransfer?.types || [])];
      if (!types.includes("application/x-board-link-node")) return;
      const card = event.target?.closest?.(".board-node-card");
      if (!card || !canvas.contains(card)) return;
      event.preventDefault();
      event.dataTransfer.dropEffect = "link";
    };
    canvas.ondrop = (event) => {
      const sourceId = event.dataTransfer?.getData("application/x-board-link-node") || "";
      if (!sourceId) return;
      const card = event.target?.closest?.(".board-node-card");
      const targetId = card && canvas.contains(card) ? card.dataset.nodeId || "" : "";
      if (!targetId || targetId === sourceId) return;
      event.preventDefault();
      createBoardRelation(sourceId, targetId);
    };
    canvas.onclick = (event) => {
      const zoomIn = event.target?.closest?.(".board-zoom-in");
      if (zoomIn) {
        event.preventDefault();
        setBoardScale(boardScale() * 1.2);
        return;
      }
      const zoomOut = event.target?.closest?.(".board-zoom-out");
      if (zoomOut) {
        event.preventDefault();
        setBoardScale(boardScale() / 1.2);
        return;
      }
      const zoomReset = event.target?.closest?.(".board-zoom-level");
      if (zoomReset) {
        event.preventDefault();
        resetBoardScale();
        return;
      }
      const sourceButton = event.target?.closest?.(".board-link-source");
      if (sourceButton) {
        event.preventDefault();
        state.boardLinkSourceId = state.boardLinkSourceId === sourceButton.dataset.nodeId ? "" : sourceButton.dataset.nodeId || "";
        renderReferenceBoard();
        return;
      }
      const linkHandle = event.target?.closest?.(".board-link-drag");
      if (linkHandle) {
        event.preventDefault();
        state.boardLinkSourceId = state.boardLinkSourceId === linkHandle.dataset.nodeId ? "" : linkHandle.dataset.nodeId || "";
        renderReferenceBoard();
        return;
      }
      const targetButton = event.target?.closest?.(".board-link-target");
      if (targetButton) {
        event.preventDefault();
        createBoardRelation(state.boardLinkSourceId, targetButton.dataset.nodeId || "");
        return;
      }
      const armedTargetCard = event.target?.closest?.(".board-node-card");
      if (
        state.boardLinkSourceId &&
        armedTargetCard &&
        canvas.contains(armedTargetCard) &&
        !event.target?.closest?.("button, input, select, textarea, a") &&
        armedTargetCard.dataset.nodeId !== state.boardLinkSourceId
      ) {
        event.preventDefault();
        createBoardRelation(state.boardLinkSourceId, armedTargetCard.dataset.nodeId || "");
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
  renderBoardHandoffDock();
  renderBoardAssetTray();
  bindReferenceBoardEvents();
}

function openReferenceBoard() {
  if (!state.detail) {
    toast("请先选择项目 / Select a project first");
    return;
  }
  state.boardTargetCard = null;
  state.boardOpen = true;
  loadBoardState();
  renderReferenceBoard();
}

function addStoryboardTargetDefaultNode(target) {
  if (!target?.item_id) return false;
  const candidates = allBoardImageAssets().filter((asset) => asset.card_type === "storyboard" && asset.card_id === target.item_id && asset.path);
  const asset =
    candidates.find((item) => item.version_status === "final") ||
    candidates.find((item) => item.version_status === "current") ||
    candidates.find((item) => item.version_status === "candidate") ||
    candidates[0];
  if (!asset) return false;
  if (!state.boardNodes.some((node) => node.assetRef === asset.ref)) {
    addBoardNode(asset.ref, boardDefaultNodePoint());
    return true;
  }
  return false;
}

function openStoryboardCanvas(index) {
  const board = collectIdeaBoardFromDom();
  const row = board.rows?.[index];
  const target = storyboardCanvasTargetFromRow(row, index);
  if (!row || !target) {
    toast("没有找到这张分镜卡 / Storyboard card not found");
    return;
  }
  state.ideaActiveRowIndex = index;
  setIdeaBoardLocal(board);
  state.boardOpen = true;
  loadBoardState();
  state.boardTargetCard = target;
  setImageLibraryFilters({ scope: row.act_id ? `act:${row.act_id}` : row.scene_id ? `scene:${row.scene_id}` : "all", tag: "all" }, allBoardImageAssets());
  const inserted = addStoryboardTargetDefaultNode(target);
  if (!inserted) renderReferenceBoard();
  toast(`已打开分镜专属画布 / Shot canvas: ${boardTargetCardLabel(target) || target.item_id}`);
}

function closeReferenceBoard() {
  state.boardOpen = false;
  state.boardTargetCard = null;
  state.boardLinkSourceId = "";
  renderReferenceBoard();
}

function clearReferenceBoard() {
  state.boardNodes = [];
  state.boardEdges = [];
  state.boardHandoffs = [];
  state.boardLinkSourceId = "";
  saveBoardState();
  renderReferenceBoard();
}

function whiteboxSourceAssets() {
  return allBoardImageAssets()
    .filter((asset) => frameIsUsable(asset))
    .filter((asset) => asset.kind !== "whitebox");
}

function whiteboxSceneFilterOptions(assets) {
  return imageLibraryScopeOptions(assets);
}

function whiteboxAssetMatches(asset) {
  const filters = normalizedImageLibraryFilters(state.imageLibraryFilters || {});
  if (!imageAssetMatchesScope(asset, filters.scope)) return false;
  const query = (filters.query || "").trim().toLowerCase();
  if (!query) return true;
  return [asset.asset_id, asset.role, asset.path, asset.scene_id, asset.scene_title, asset.act_title, asset.shot_id, kindLabel(asset.kind)]
    .join(" ")
    .toLowerCase()
    .includes(query);
}

function selectedWhiteboxSource() {
  const assets = whiteboxSourceAssets();
  if (!state.whiteboxSourceRef || !assets.some((asset) => asset.ref === state.whiteboxSourceRef)) {
    const scene = selectedScene();
    const preferred = assets.find((asset) => asset.scene_id === scene?.scene_id) || assets[0];
    state.whiteboxSourceRef = preferred?.ref || "";
  }
  return assets.find((asset) => asset.ref === state.whiteboxSourceRef) || null;
}

function wordsForWhiteboxMatch(text) {
  return [...new Set((text || "").toLowerCase().match(/[\u4e00-\u9fa5]{2,}|[a-z0-9_]{3,}/g) || [])]
    .filter((word) => !["cinematic", "storyboard", "keyframe", "image", "prompt", "scene", "shot"].includes(word))
    .slice(0, 28);
}

function whiteboxTargetRowsForSource(source) {
  const board = currentIdeaBoard();
  const rows = board.rows || [];
  if (!source) return [];
  const sourceWords = wordsForWhiteboxMatch([source.asset_id, source.role, source.path, source.scene_id, source.scene_title, source.act_title].join(" "));
  const queryWords = wordsForWhiteboxMatch(state.whiteboxFilters.query || "");
  const hasQuery = Boolean((state.whiteboxFilters.query || "").trim());
  const words = [...new Set([...sourceWords, ...queryWords])];
  return rows
    .map((row, index) => {
      const text = [row.item_id, row.scene_id, row.beat, row.shot_type, row.frame_description, row.spatial_logic, row.image_prompt, row.notes].join(" ").toLowerCase();
      const sameScene = source.scene_id && row.scene_id === source.scene_id;
      const score = (sameScene ? 8 : 0) + words.filter((word) => text.includes(word)).length;
      return { row, index, score, sameScene };
    })
    .filter((entry) => {
      if (source.scene_id && !hasQuery) return entry.sameScene;
      return entry.sameScene || entry.score > 0;
    })
    .sort((a, b) => b.score - a.score || naturalCompare(a.row.item_id || "", b.row.item_id || ""));
}

function defaultWhiteboxTargetIds(source) {
  return whiteboxTargetRowsForSource(source).map(({ row }) => row.item_id).filter(Boolean);
}

function renderWhiteboxSourceGrid() {
  const root = $("whiteboxSourceGrid");
  if (!root) return;
  const assets = whiteboxSourceAssets().filter(whiteboxAssetMatches).slice(0, 80);
  root.innerHTML = assets.length
    ? assets
        .map(
          (asset) => `
            <button class="whitebox-source-card ${asset.ref === state.whiteboxSourceRef ? "active" : ""}" data-asset-ref="${escapeHtml(asset.ref)}" type="button">
              <img src="${escapeHtml(asset.url)}" alt="${escapeHtml(asset.asset_id || asset.path)}" loading="lazy" />
              <strong>${escapeHtml(asset.asset_id || asset.role || asset.path)}</strong>
              <span>${escapeHtml(asset.scene_id || "PROJECT")} · ${escapeHtml(kindLabel(asset.kind))}</span>
            </button>
          `,
        )
        .join("")
    : `<div class="empty-state">没有匹配的源图 / No matching source images.</div>`;
}

function renderWhiteboxSelectedSource(source) {
  const root = $("whiteboxSelectedSource");
  if (!root) return;
  if (!source) {
    root.innerHTML = `<div class="empty-state">先选择一张要复刻成白模的母图。</div>`;
    return;
  }
  root.innerHTML = `
    <article class="whitebox-source-summary">
      <img src="${escapeHtml(source.url)}" alt="${escapeHtml(source.asset_id || source.path)}" />
      <div>
        <strong>${escapeHtml(source.asset_id || source.role || source.path)}</strong>
        <span>${escapeHtml(source.scene_id || "PROJECT")} · ${escapeHtml(source.scene_title || "")}</span>
        <small>${escapeHtml(source.path || "")}</small>
      </div>
    </article>
  `;
}

function renderWhiteboxTargetList(source) {
  const root = $("whiteboxTargetList");
  if (!root) return;
  const entries = whiteboxTargetRowsForSource(source);
  const selectedSet = new Set(state.whiteboxSelectedTargets || []);
  $("whiteboxTargetHint").textContent = `${selectedSet.size}/${entries.length} 已选 / selected`;
  root.innerHTML = entries.length
    ? entries
        .map(({ row, score, sameScene }) => {
          const itemId = row.item_id || "";
          return `
            <label class="whitebox-target-row">
              <input class="whitebox-target-check" type="checkbox" value="${escapeHtml(itemId)}" ${selectedSet.has(itemId) ? "checked" : ""} />
              <span>
                <strong>${escapeHtml(itemId || "Untitled")}</strong>
                <small>${escapeHtml(row.scene_id || "")} · ${sameScene ? "同场景 / same scene" : `匹配分 ${score}`}</small>
              </span>
              <em>${escapeHtml(row.beat || row.frame_description || "")}</em>
            </label>
          `;
        })
        .join("")
    : `<div class="empty-state">没有自动匹配到分镜。换一张源图，或在搜索里输入场景/道具关键词。</div>`;
}

function renderWhiteboxHandoffs() {
  const root = $("whiteboxHandoffDock");
  if (!root) return;
  const serverJobs = state.detail?.whitebox_lab?.jobs || [];
  const cards = [...(state.whiteboxHandoffs || []), ...serverJobs.slice(-4).reverse().map((job) => ({
    id: job.job_id,
    title: `${job.job_id} · ${job.source_asset?.asset_id || "whitebox"}`,
    path: job.handoff_path || "",
    text: "",
  }))];
  root.innerHTML = cards.length
    ? cards
        .map(
          (card) => `
            <article class="whitebox-handoff-card" draggable="${card.text ? "true" : "false"}" data-whitebox-handoff-id="${escapeHtml(card.id || "")}">
              <strong>${escapeHtml(card.title || "Whitebox job")}</strong>
              <small>${escapeHtml(card.path || "")}</small>
              ${card.text ? `<textarea readonly rows="5">${escapeHtml(card.text)}</textarea>` : ""}
            </article>
          `,
        )
        .join("")
    : `<div class="empty-state">白模任务包会出现在这里 / Whitebox packets will appear here.</div>`;
}

function renderWhiteboxLab() {
  const modal = $("whiteboxLabModal");
  if (!modal) return;
  modal.hidden = !state.whiteboxOpen;
  document.body.classList.toggle("board-open", state.whiteboxOpen || state.boardOpen);
  if (!state.whiteboxOpen) return;
  const assets = whiteboxSourceAssets();
  const filters = currentImageLibraryFilters(assets);
  const sceneFilter = $("whiteboxSceneFilter");
  if (sceneFilter) {
    sceneFilter.innerHTML = whiteboxSceneFilterOptions(assets)
      .map((option) => `<option value="${escapeHtml(option.value)}" ${filters.scope === option.value ? "selected" : ""}>${escapeHtml(option.label)}</option>`)
      .join("");
  }
  const search = $("whiteboxSearchInput");
  if (search) search.value = filters.query || "";
  renderWhiteboxSourceGrid();
  const source = selectedWhiteboxSource();
  if (!state.whiteboxSelectedTargets.length) state.whiteboxSelectedTargets = defaultWhiteboxTargetIds(source);
  renderWhiteboxSelectedSource(source);
  renderWhiteboxTargetList(source);
  renderWhiteboxHandoffs();
  bindWhiteboxLabEvents();
}

function openWhiteboxLab() {
  if (!state.detail) {
    toast("请先选择项目 / Select a project first");
    return;
  }
  state.whiteboxOpen = true;
  renderWhiteboxLab();
}

function closeWhiteboxLab() {
  state.whiteboxOpen = false;
  renderWhiteboxLab();
}

function whiteboxSourcePayload(asset) {
  return {
    asset_ref: asset.ref,
    asset_id: asset.asset_id || asset.role || asset.path,
    path: asset.path || "",
    origin: asset.origin || "project",
    kind: asset.kind || "image",
    scene_id: asset.scene_id || "",
    scene_title: asset.scene_title || "",
    act_id: asset.act_id || "",
    act_title: asset.act_title || "",
  };
}

async function createWhiteboxJob() {
  const source = selectedWhiteboxSource();
  if (!source) {
    toast("请先选择母图 / Select a source image first");
    return;
  }
  const board = collectIdeaBoardFromDom();
  const selectedSet = new Set(state.whiteboxSelectedTargets || []);
  const targets = (board.rows || []).filter((row) => selectedSet.has(row.item_id));
  if (!targets.length) {
    toast("请至少选择一个目标分镜 / Select at least one target row");
    return;
  }
  await runAction("白模任务包 / Whitebox packet", async () => {
    await persistIdeaBoard(board, { toast: false, render: false });
    const result = await requestJson(`/api/projects/${state.selectedSlug}/whitebox-job`, {
      method: "POST",
      body: JSON.stringify({
        source_asset: whiteboxSourcePayload(source),
        targets,
        replica_note: $("whiteboxReplicaNote")?.value || "",
        tags: ($("whiteboxTagInput")?.value || "").split(",").map((item) => item.trim()).filter(Boolean),
        attach_to_rows: $("whiteboxAttachToRows")?.checked ?? true,
      }),
    });
    state.detail = result.project || state.detail;
    state.whiteboxHandoffs = [
      {
        id: result.job?.job_id || `whitebox_${Date.now()}`,
        title: `${result.job?.job_id || "Whitebox"} · ${result.attached_rows || 0} 条分镜已挂载`,
        path: result.job?.handoff_path || "",
        text: result.handoff_text || "",
      },
      ...(state.whiteboxHandoffs || []),
    ].slice(0, 8);
    toast(`白模任务包已生成，已挂载 ${result.attached_rows || 0} 条分镜 / Whitebox packet ready`);
    renderWhiteboxLab();
  });
}

function bindWhiteboxLabEvents() {
  const closeButton = $("closeWhiteboxLabBtn");
  if (closeButton) closeButton.onclick = closeWhiteboxLab;
  const buildButton = $("buildWhiteboxJobBtn");
  if (buildButton) buildButton.onclick = createWhiteboxJob;
  const sceneFilter = $("whiteboxSceneFilter");
  if (sceneFilter) sceneFilter.onchange = (event) => {
    setImageLibraryFilters({ scope: event.target.value || "all" }, whiteboxSourceAssets());
    state.whiteboxSelectedTargets = [];
    renderWhiteboxLab();
  };
  const searchInput = $("whiteboxSearchInput");
  if (searchInput) searchInput.oninput = (event) => {
    setImageLibraryFilters({ query: event.target.value || "" }, whiteboxSourceAssets());
    state.whiteboxSelectedTargets = [];
    renderWhiteboxLab();
  };
  $("whiteboxSourceGrid")?.querySelectorAll(".whitebox-source-card").forEach((button) => {
    button.addEventListener("click", () => {
      state.whiteboxSourceRef = button.dataset.assetRef || "";
      state.whiteboxSelectedTargets = defaultWhiteboxTargetIds(selectedWhiteboxSource());
      renderWhiteboxLab();
    });
  });
  document.querySelectorAll(".whitebox-target-check").forEach((checkbox) => {
    checkbox.addEventListener("change", () => {
      const set = new Set(state.whiteboxSelectedTargets || []);
      if (checkbox.checked) set.add(checkbox.value);
      else set.delete(checkbox.value);
      state.whiteboxSelectedTargets = [...set];
      renderWhiteboxTargetList(selectedWhiteboxSource());
    });
  });
  document.querySelectorAll(".whitebox-handoff-card").forEach((card) => {
    card.addEventListener("dragstart", (event) => {
      const text = card.querySelector("textarea")?.value || "";
      if (!text) return;
      event.dataTransfer?.setData("text/plain", text);
      event.dataTransfer?.setData("text/markdown", text);
      event.dataTransfer.effectAllowed = "copy";
    });
  });
}

function ideaHandoffStorageKey() {
  return state.selectedSlug ? `pipeline-idea-handoffs:${state.selectedSlug}` : "pipeline-idea-handoffs";
}

function loadIdeaHandoffs() {
  try {
    const raw = window.localStorage.getItem(ideaHandoffStorageKey());
    const parsed = raw ? JSON.parse(raw) : [];
    state.ideaHandoffs = Array.isArray(parsed) ? parsed : [];
  } catch {
    state.ideaHandoffs = [];
  }
}

function saveIdeaHandoffs() {
  if (!state.selectedSlug) return;
  try {
    window.localStorage.setItem(ideaHandoffStorageKey(), JSON.stringify(state.ideaHandoffs.slice(0, 12)));
  } catch {
    // Handoff cards are convenience UI; the saved idea board is project-backed.
  }
}

function normalizeIdeaHandoffIds(value) {
  if (!Array.isArray(value)) return [];
  return [...new Set(value.map((item) => String(item || "").trim()).filter(Boolean))];
}

function ideaHandoffCompletionNote(handoffId = IDEA_HANDOFF_ID_PLACEHOLDER) {
  return [
    "## Codex Analysis Card Metadata / Codex 分析卡元数据",
    `- codex_handoff_id: ${handoffId}`,
    "- 完成本卡要求的分析、生成或回填后，必须在 callback JSON body 顶层带上 completed_handoff_id。",
    `- Example: "completed_handoff_id": "${handoffId}"`,
    "- App 会用这个 id 自动删除已经完成的本地 Codex 分析卡；不要删除项目里的设定、幕、分镜或图片数据。",
  ].join("\n");
}

function withIdeaHandoffCompletionNote(text, handoffId) {
  const body = String(text || "");
  const note = ideaHandoffCompletionNote(handoffId);
  if (!body.trim()) return note;
  if (body.includes("codex_handoff_id:")) {
    return body.replaceAll(IDEA_HANDOFF_ID_PLACEHOLDER, handoffId);
  }
  return `${note}\n\n${body.replaceAll(IDEA_HANDOFF_ID_PLACEHOLDER, handoffId)}`;
}

function pruneCompletedIdeaHandoffs(completedIds) {
  const idSet = new Set(normalizeIdeaHandoffIds(completedIds));
  if (!idSet.size || !state.ideaHandoffs.length) return 0;
  const before = state.ideaHandoffs.length;
  state.ideaHandoffs = state.ideaHandoffs.filter((handoff) => !idSet.has(handoff.id));
  const removed = before - state.ideaHandoffs.length;
  if (removed > 0) saveIdeaHandoffs();
  return removed;
}

function pruneCompletedBoardHandoffs(completedIds) {
  const ids = normalizeIdeaHandoffIds(completedIds);
  const idSet = new Set(ids);
  if (!idSet.size || !state.boardHandoffs.length) return 0;
  const before = state.boardHandoffs.length;
  state.boardHandoffs = state.boardHandoffs.filter((handoff) => {
    if (idSet.has(handoff.id) || idSet.has(handoff.outputPath)) return false;
    const text = [handoff.title, handoff.outputPath, handoff.text].filter(Boolean).join("\n");
    return !ids.some((id) => text.includes(id));
  });
  const removed = before - state.boardHandoffs.length;
  if (removed > 0) saveBoardState();
  return removed;
}

function stopIdeaHandoffCompletionPolling() {
  if (!state.ideaHandoffPollTimer) return;
  window.clearInterval(state.ideaHandoffPollTimer);
  state.ideaHandoffPollTimer = null;
}

async function pollIdeaHandoffCompletions() {
  if (!state.selectedSlug || (!state.ideaHandoffs.length && !state.boardHandoffs.length)) {
    stopIdeaHandoffCompletionPolling();
    return;
  }
  try {
    const payload = await requestJson(`/api/projects/${encodeURIComponent(state.selectedSlug)}/idea-handoffs/completed`);
    const completedIds = payload.completed_handoff_ids || [];
    const removed = pruneCompletedIdeaHandoffs(completedIds);
    const removedBoard = pruneCompletedBoardHandoffs(completedIds);
    if (removed > 0) {
      renderIdeaLab();
    }
    if (removedBoard > 0 && state.boardOpen) {
      renderBoardHandoffDock();
      bindBoardHandoffEvents();
    }
    if (removed || removedBoard) {
      toast(`已自动删除 ${removed + removedBoard} 张完成的 Codex 卡 / Completed cards removed`);
    }
  } catch {
    // Completion cleanup is best-effort; manual delete stays available.
  }
  if (!state.ideaHandoffs.length && !state.boardHandoffs.length) stopIdeaHandoffCompletionPolling();
}

function syncIdeaHandoffCompletionPolling() {
  if (!state.selectedSlug || (!state.ideaHandoffs.length && !state.boardHandoffs.length)) {
    stopIdeaHandoffCompletionPolling();
    return;
  }
  if (!state.ideaHandoffPollTimer) {
    state.ideaHandoffPollTimer = window.setInterval(pollIdeaHandoffCompletions, 5000);
  }
}

function clearIdeaHandoffs() {
  state.ideaHandoffs = [];
  saveIdeaHandoffs();
  stopIdeaHandoffCompletionPolling();
  renderIdeaLab();
}

// Memoized: this is called hundreds of thousands of times per render (via default
// params like `board = currentIdeaBoard()` inside nested row/asset loops). Rebuilding
// the wrapper each time was the dominant cost of renderIdeaLab (~3.8s). The wrapper is
// derived purely from state.detail.idea_board (replaced wholesale on every edit, see
// setIdeaBoardLocal) and state.selectedSlug, so we cache on those identities.
let _ideaBoardCacheWrapper = null;
let _ideaBoardCacheSource = null;
let _ideaBoardCacheSlug = null;

function invalidateIdeaBoardCache() {
  _ideaBoardCacheWrapper = null;
  _ideaBoardCacheSource = null;
  _ideaBoardCacheSlug = null;
  _storyActEntriesCache = null;
  _storyActEntriesBoard = null;
  _storyActEntriesScenes = null;
}

function currentIdeaBoard() {
  const source = state.detail?.idea_board || null;
  const slug = state.selectedSlug || "";
  if (_ideaBoardCacheWrapper && _ideaBoardCacheSource === source && _ideaBoardCacheSlug === slug) {
    return _ideaBoardCacheWrapper;
  }
  const board = source || {};
  _ideaBoardCacheWrapper = {
    schema_version: 1,
    project_slug: slug,
    idea: board.idea || "",
    story_title: board.story_title || "",
    logline: board.logline || "",
    story_outline: board.story_outline || "",
    style_notes: board.style_notes || "",
    act_inputs: board.act_inputs && typeof board.act_inputs === "object" ? board.act_inputs : {},
    acts: Array.isArray(board.acts) ? board.acts : [],
    project_bible: Array.isArray(board.project_bible) ? board.project_bible : [],
    global_references: Array.isArray(board.global_references) ? board.global_references : [],
    rows: Array.isArray(board.rows) ? board.rows : [],
    completed_handoff_ids: normalizeIdeaHandoffIds(board.completed_handoff_ids || []),
  };
  _ideaBoardCacheSource = source;
  _ideaBoardCacheSlug = slug;
  return _ideaBoardCacheWrapper;
}

function nextIdeaItemId(rows) {
  const count = (rows || []).length + 1;
  return `IDEA_SHOT_${String(count).padStart(3, "0")}`;
}

function nextIdeaItemIdForAct(rows, actId) {
  if (!actId) return nextIdeaItemId(rows);
  const scopedBoard = { ...currentIdeaBoard(), rows: rows || [] };
  const count = (rows || []).filter((row) => rowMatchesStoryAct(row, actId, scopedBoard)).length + 1;
  return `${actId}_SHOT_${String(count).padStart(3, "0")}`;
}

function parseStoryboardLinkInput(value) {
  if (Array.isArray(value)) {
    return [...new Set(value.map((item) => String(item || "").trim()).filter(Boolean))];
  }
  return [...new Set(String(value || "").split(/[,，\s]+/).map((item) => item.trim()).filter(Boolean))];
}

function storyboardLinkValue(value) {
  return parseStoryboardLinkInput(value).join(", ");
}

function parseRenumberableShotId(value) {
  const text = String(value || "").trim();
  const match = text.match(/^(.+?)(\d{2,})(.*)$/);
  if (!match) return null;
  return {
    prefix: match[1],
    number: Number(match[2]),
    width: match[2].length,
    suffix: match[3] || "",
  };
}

function rowInsertScopeKey(row = {}) {
  if (row.scene_id) return `scene:${row.scene_id}`;
  if (row.act_id) return `act:${row.act_id}`;
  return "all";
}

function rowMatchesInsertScope(row = {}, scopeKey = "") {
  return rowInsertScopeKey(row) === scopeKey;
}

function replaceMappedCardId(value, idMap) {
  const text = String(value || "").trim();
  return idMap.get(text) || text;
}

function updateStoryboardIdReferences(board, idMap) {
  if (!idMap.size) return board;
  board.rows = (board.rows || []).map((row) => ({
    ...row,
    sort_after: replaceMappedCardId(row.sort_after || "", idMap),
    linked_cards: parseStoryboardLinkInput(row.linked_cards || []).map((item) => replaceMappedCardId(item, idMap)),
  }));
  return board;
}

function renumberRowsAfterInsert(board, insertIndex, baseRow) {
  const parsedBase = parseRenumberableShotId(baseRow?.item_id || "");
  if (!parsedBase) return board;
  const scopeKey = rowInsertScopeKey(baseRow);
  const idMap = new Map();
  let nextNumber = parsedBase.number + 1;
  for (let index = insertIndex + 1; index < (board.rows || []).length; index += 1) {
    const row = board.rows[index];
    if (!rowMatchesInsertScope(row, scopeKey)) continue;
    const parsed = parseRenumberableShotId(row.item_id || "");
    if (parsed && parsed.prefix !== parsedBase.prefix) continue;
    const suffix = parsed?.suffix || "";
    const oldId = row.item_id || "";
    const newId = `${parsedBase.prefix}${String(nextNumber).padStart(parsedBase.width, "0")}${suffix}`;
    row.item_id = newId;
    if (oldId && oldId !== newId) idMap.set(oldId, newId);
    nextNumber += 1;
  }
  return updateStoryboardIdReferences(board, idMap);
}

function renumberRowsBeforeInsert(board, insertIndex, baseRow) {
  const parsedBase = parseRenumberableShotId(baseRow?.item_id || "");
  if (!parsedBase) return board;
  const scopeKey = rowInsertScopeKey(baseRow);
  const idMap = new Map();
  let nextNumber = parsedBase.number;
  for (let index = insertIndex; index < (board.rows || []).length; index += 1) {
    const row = board.rows[index];
    if (!rowMatchesInsertScope(row, scopeKey)) continue;
    const parsed = parseRenumberableShotId(row.item_id || "");
    if (parsed && parsed.prefix !== parsedBase.prefix) continue;
    const suffix = parsed?.suffix || "";
    const oldId = row.item_id || "";
    const newId = `${parsedBase.prefix}${String(nextNumber).padStart(parsedBase.width, "0")}${suffix}`;
    row.item_id = newId;
    if (oldId && oldId !== newId) idMap.set(oldId, newId);
    nextNumber += 1;
  }
  return updateStoryboardIdReferences(board, idMap);
}

function previousRowInInsertScope(board, index, baseRow) {
  const scopeKey = rowInsertScopeKey(baseRow);
  for (let cursor = index - 1; cursor >= 0; cursor -= 1) {
    const row = board.rows?.[cursor];
    if (row && rowMatchesInsertScope(row, scopeKey)) return row;
  }
  return null;
}

function nextIdeaActId(acts) {
  const count = Math.max(storyActEntries().length, (acts || []).length) + 1;
  return `ACT${String(count).padStart(2, "0")}`;
}

function nextProjectBibleCardId(cards) {
  return `BIBLE_${String((cards || []).length + 1).padStart(3, "0")}`;
}

function sceneDerivedStoryAct(scene, index = 0, boardAct = {}) {
  const clipSummary = Array.isArray(scene?.clip_summary) ? scene.clip_summary : [];
  const clipText = clipSummary
    .map((clip) => [clip.clip, clip.title, clip.shot_count ? `${clip.shot_count} 镜头` : ""].filter(Boolean).join(" · "))
    .join("\n");
  const shotIds = Array.isArray(scene?.shot_ids) ? scene.shot_ids : [];
  return {
    source: "scene",
    scene_id: scene?.scene_id || "",
    act_id: scene?.scene_id || `ACT${String(index + 1).padStart(2, "0")}`,
    title: boardAct.title || scene?.title || scene?.scene_id || "",
    summary: boardAct.summary || clipText || scene?.story_stage || "",
    dramatic_purpose: boardAct.dramatic_purpose || scene?.act_title || "",
    key_beats: boardAct.key_beats || shotIds.join(", "),
    status: boardAct.status || scene?.status || "draft",
  };
}

// Memoized: called ~690k times per render (via storyActEntryForId in row/asset loops).
// Pure for a given board wrapper + scenes array, both stable within a render.
let _storyActEntriesCache = null;
let _storyActEntriesBoard = null;
let _storyActEntriesScenes = null;

function storyActEntries(board = currentIdeaBoard()) {
  const scenes = state.detail?.scene_workbench?.scenes || [];
  if (_storyActEntriesCache && _storyActEntriesBoard === board && _storyActEntriesScenes === scenes) {
    return _storyActEntriesCache;
  }
  const result = computeStoryActEntries(board, scenes);
  _storyActEntriesCache = result;
  _storyActEntriesBoard = board;
  _storyActEntriesScenes = scenes;
  return result;
}

function computeStoryActEntries(board, scenes) {
  const sceneIds = new Set(scenes.map((scene) => scene.scene_id).filter(Boolean));
  const manifestGroupActIds = new Set(scenes.map((scene) => scene.act_id).filter(Boolean));
  const boardActs = Array.isArray(board.acts) ? board.acts : [];
  const sceneEntries = scenes.map((scene, index) => {
    const boardAct = boardActs.find((act) => (act.act_id || "") === (scene.scene_id || "")) || {};
    return sceneDerivedStoryAct(scene, index, boardAct);
  });
  const customEntries = boardActs
    .filter((act) => {
      const actId = act.act_id || "";
      if (!actId) return false;
      if (sceneIds.has(actId)) return false;
      if (manifestGroupActIds.has(actId)) return false;
      return true;
    })
    .map((act) => ({ ...act, source: "custom", scene_id: "" }));
  return [...sceneEntries, ...customEntries];
}

function storyActEntryForId(board = currentIdeaBoard(), actId = activeStoryActId()) {
  return storyActEntries(board).find((act) => (act.act_id || "") === actId) || null;
}

function activeStoryActId() {
  if (isConceptWorkspaceSelected()) return "";
  const customActId = selectedIdeaActIdFromState();
  if (customActId) {
    if (storyActEntries(currentIdeaBoard()).some((act) => (act.act_id || "") === customActId)) return customActId;
    const firstSceneId = state.detail?.scene_workbench?.scenes?.[0]?.scene_id || "";
    if (firstSceneId) {
      state.selectedSceneId = firstSceneId;
      return firstSceneId;
    }
    return "";
  }
  const scene = selectedScene();
  return scene?.scene_id || "";
}

function rowMatchesStoryAct(row, actId = activeStoryActId(), board = currentIdeaBoard()) {
  if (!actId) return true;
  const entry = storyActEntryForId(board, actId);
  if (entry?.scene_id) return (row.scene_id || "") === entry.scene_id;
  return (row.act_id || "") === actId;
}

function activeIdeaActId() {
  if (isConceptWorkspaceSelected()) return "";
  const selectedActId = selectedIdeaActIdFromState();
  if (selectedActId) return selectedActId;
  const scope = state.cardFilters?.scope || "";
  if (scope.startsWith("act:")) return scope.slice(4);
  const scene = selectedScene();
  return scene?.act_id || "";
}

function defaultSceneIdForAct(board = currentIdeaBoard(), actId = activeStoryActId()) {
  if (!actId) return selectedScene()?.scene_id || "";
  if ((state.detail?.scene_workbench?.scenes || []).some((scene) => scene.scene_id === actId)) return actId;
  const rowScene = (board.rows || []).find((row) => (row.act_id || "") === actId && row.scene_id)?.scene_id || "";
  if (rowScene) return rowScene;
  return (state.detail?.scene_workbench?.scenes || []).find((scene) => (scene.act_id || "") === actId)?.scene_id || "";
}

function activeIdeaInputs(board = currentIdeaBoard()) {
  const actId = activeStoryActId();
  if (!actId) {
    return {
      idea: board.idea || "",
      story_title: board.story_title || "",
      logline: board.logline || "",
    };
  }
  const scoped = board.act_inputs?.[actId] || {};
  return {
    idea: scoped.idea || "",
    story_title: scoped.story_title || "",
    logline: scoped.logline || "",
  };
}

function boardWithActiveIdeaInputs(board = currentIdeaBoard()) {
  return {
    ...board,
    ...activeIdeaInputs(board),
  };
}

function cacheIdeaBoardFromDom() {
  if (!state.detail || !$("ideaSeedInput")) return;
  setIdeaBoardLocal(collectIdeaBoardFromDom());
}

function ensureIdeaActiveBibleForScope(board = currentIdeaBoard()) {
  const entries = (board.project_bible || []).map((card, index) => ({ card, index }));
  if (!entries.length) return null;
  if (!entries.some(({ index }) => index === Number(state.ideaActiveBibleIndex || 0))) {
    state.ideaActiveBibleIndex = entries[0].index;
  }
  return state.ideaActiveBibleIndex;
}

function ensureProjectBibleActiveForFilteredCards(board = currentIdeaBoard()) {
  const entries = filteredProjectBibleEntries(board);
  if (!entries.length) return ensureIdeaActiveBibleForScope(board);
  const activeIndex = Number(state.ideaActiveBibleIndex || 0);
  if (!entries.some(({ index }) => index === activeIndex)) {
    state.ideaActiveBibleIndex = entries[0].index;
  }
  return state.ideaActiveBibleIndex;
}

function collectIdeaActsFromDom(current) {
  const root = $("ideaActList");
  if (!root) return current.acts || [];
  const acts = Array.isArray(current.acts) ? [...current.acts] : [];
  Array.from(root.querySelectorAll(".idea-act-row")).forEach((row, index) => {
    const value = (field) => row.querySelector(`[data-idea-act-field="${field}"]`)?.value || "";
    const originalId = row.dataset.ideaActId || "";
    const next = {
      act_id: value("act_id") || originalId || `ACT${String(index + 1).padStart(2, "0")}`,
      title: value("title"),
      summary: value("summary"),
      dramatic_purpose: value("dramatic_purpose"),
      key_beats: value("key_beats"),
      status: value("status") || "draft",
    };
    const targetIndex = acts.findIndex((act) => (act.act_id || "") === originalId || (act.act_id || "") === next.act_id);
    if (targetIndex >= 0) {
      acts[targetIndex] = { ...acts[targetIndex], ...next };
    } else {
      acts.push(next);
    }
  });
  return acts;
}

function collectProjectBibleFromDom(current) {
  const root = $("projectBibleCardList");
  if (!root) return current.project_bible || [];
  const cards = Array.isArray(current.project_bible) ? [...current.project_bible] : [];
  Array.from(root.querySelectorAll(".project-bible-card")).forEach((card, index) => {
    const value = (field) => card.querySelector(`[data-bible-field="${field}"]`)?.value || "";
    const cardIndex = Number(card.dataset.bibleIndex);
    const existing = current.project_bible?.[Number.isInteger(cardIndex) ? cardIndex : index] || {};
    const targetIndex = Number.isInteger(cardIndex) && cardIndex >= 0 ? cardIndex : cards.length;
    cards[targetIndex] = {
      card_id: value("card_id") || existing.card_id || `BIBLE_${String(index + 1).padStart(3, "0")}`,
      scope: value("scope") || existing.scope || "project",
      act_id: value("act_id") || existing.act_id || "",
      category: value("category") || existing.category || "lookdev",
      title: value("title"),
      summary: value("summary"),
      visual_direction: value("visual_direction"),
      prompt_notes: value("prompt_notes"),
      revision_note: value("revision_note"),
      negative_prompt: value("negative_prompt"),
      selected: card.querySelector('[data-bible-field="selected"]')?.checked ?? true,
      image_selected: card.querySelector('[data-bible-field="image_selected"]')?.checked ?? true,
      status: value("status") || "draft",
      references: Array.isArray(existing.references) ? existing.references : [],
      preview_path: existing.preview_path || "",
      versions: Array.isArray(existing.versions) ? existing.versions : [],
    };
  });
  return cards.filter(Boolean);
}

function ideaRowEntriesForCurrentScene(board = currentIdeaBoard()) {
  if (isConceptWorkspaceSelected()) return [];
  const rows = board.rows || [];
  const activeActId = activeStoryActId();
  const entries = rows.map((row, index) => ({ row, index }));
  if (!activeActId) return entries;
  return entries.filter(({ row }) => rowMatchesStoryAct(row, activeActId, board));
}

function ensureIdeaActiveRowForScene(board = currentIdeaBoard()) {
  const entries = ideaRowEntriesForCurrentScene(board);
  if (!entries.length) return null;
  const activeIndex = Number(state.ideaActiveRowIndex || 0);
  if (!entries.some(({ index }) => index === activeIndex)) {
    state.ideaActiveRowIndex = entries[0].index;
  }
  return state.ideaActiveRowIndex;
}

function ideaSceneSummary(board = currentIdeaBoard()) {
  const activeActId = activeStoryActId();
  const activeAct = storyActEntryForId(board, activeActId);
  const visibleCount = ideaRowEntriesForCurrentScene(board).length;
  const totalCount = (board.rows || []).length;
  if (!activeActId) return `${totalCount} 条分镜文本 / storyboard prompt rows`;
  return `${activeActId} · ${escapeHtml(activeAct?.title || "")} · ${visibleCount}/${totalCount} 条分镜文本`;
}

function compactProjectSceneContext() {
  const scenes = state.detail?.scene_workbench?.scenes || [];
  if (!Array.isArray(scenes) || !scenes.length) return "- No existing scene map yet.";
  return scenes
    .slice(0, 24)
    .map((scene) => `- ${scene.scene_id || ""}: ${scene.title || ""} (${scene.act_title || scene.act_id || ""})`)
    .join("\n");
}

function collectIdeaBoardFromDom() {
  const current = currentIdeaBoard();
  const editedRows = new Map();
  Array.from(document.querySelectorAll(".idea-shot-row")).forEach((row, fallbackIndex) => {
    const value = (field) => row.querySelector(`[data-idea-field="${field}"]`)?.value || "";
    const rowIndex = Number(row.dataset.ideaIndex);
    const hasStableIndex = Number.isInteger(rowIndex) && rowIndex >= 0;
    const indexedExisting = hasStableIndex ? current.rows[rowIndex] : null;
    const itemId = value("item_id") || indexedExisting?.item_id || `IDEA_SHOT_${String(fallbackIndex + 1).padStart(3, "0")}`;
    const existing =
      indexedExisting ||
      current.rows.find((item) => item.item_id === itemId) ||
      {};
    editedRows.set(hasStableIndex ? rowIndex : current.rows.length + fallbackIndex, {
      card_uid: existing.card_uid || row.dataset.cardUid || newIdeaCardUid(),
      item_id: itemId,
      act_id: value("act_id") || existing.act_id || sceneForIdeaRow(existing).act_id || "",
      scene_id: value("scene_id"),
      beat: value("beat"),
      shot_type: value("shot_type"),
      frame_description: value("frame_description"),
      linked_cards: parseStoryboardLinkInput(value("linked_cards")),
      spatial_logic: value("spatial_logic"),
      image_prompt: value("image_prompt"),
      video_prompt: value("video_prompt"),
      notes: value("notes"),
      revision_note: value("revision_note"),
      sort_after: value("sort_after"),
      selected: row.querySelector('[data-idea-field="selected"]')?.checked ?? true,
      status: value("status") || "draft",
      output_path: value("output_path"),
      output_notes: value("output_notes"),
      output_attached_at: existing.output_attached_at || "",
      versions: Array.isArray(existing.versions) ? existing.versions : [],
      references: Array.isArray(existing.references) ? existing.references : [],
    });
  });
  const rows = current.rows.map((row, index) => editedRows.get(index) || row);
  [...editedRows.entries()]
    .filter(([index]) => index >= current.rows.length)
    .sort(([a], [b]) => a - b)
    .forEach(([, row]) => rows.push(row));
  const board = {
    idea: current.idea || "",
    story_title: current.story_title || "",
    logline: current.logline || "",
    story_outline: $("ideaOutline")?.value || "",
    style_notes: $("ideaStyleNotes")?.value || "",
    act_inputs: { ...(current.act_inputs || {}) },
    acts: collectIdeaActsFromDom(current),
    project_bible: collectProjectBibleFromDom(current),
    global_references: current.global_references,
    rows,
  };
  const textInputs = {
    idea: $("ideaSeedInput")?.value || "",
    story_title: $("ideaStoryTitle")?.value || "",
    logline: $("ideaLogline")?.value || "",
  };
  const actId = activeStoryActId();
  if (actId) {
    board.act_inputs[actId] = {
      ...(board.act_inputs[actId] || {}),
      ...textInputs,
    };
  } else {
    board.idea = textInputs.idea;
    board.story_title = textInputs.story_title;
    board.logline = textInputs.logline;
  }
  syncIdeaReferenceNotesFromDom(board);
  return board;
}

function setIdeaBoardLocal(board) {
  state.detail.idea_board = {
    ...currentIdeaBoard(),
    ...board,
    acts: Array.isArray(board.acts) ? board.acts : [],
    project_bible: Array.isArray(board.project_bible) ? board.project_bible : [],
    global_references: Array.isArray(board.global_references) ? board.global_references : [],
    rows: Array.isArray(board.rows) ? board.rows : [],
  };
  invalidateIdeaBoardCache();
}

function syncIdeaReferenceNotesFromDom(board) {
  document.querySelectorAll(".idea-ref-note").forEach((textarea) => {
    const scope = textarea.dataset.refScope || "row";
    const key = textarea.dataset.refKey || "";
    const note = textarea.value || "";
    const updateRefs = (refs = []) => refs.map((ref) => (ideaReferenceKey(ref) === key ? { ...ref, note } : ref));
    if (scope === "global") {
      board.global_references = updateRefs(board.global_references || []);
    } else if (scope === "bible") {
      const card = board.project_bible?.[state.ideaActiveBibleIndex];
      if (card) card.references = updateRefs(card.references || []);
    } else {
      const row = board.rows?.[state.ideaActiveRowIndex];
      if (row) row.references = updateRefs(row.references || []);
    }
  });
}

function ideaReferenceKey(ref) {
  return ref?.asset_ref || `${ref?.origin || ""}:${ref?.path || ""}` || ref?.ref_id || "";
}

function ideaReferenceAsset(ref) {
  const key = ideaReferenceKey(ref);
  return allBoardImageAssets().find((asset) => asset.ref === key || asset.path === ref?.path) || null;
}

function ideaReferenceOrigin(ref) {
  const origin = String(ref?.origin || "").trim();
  if (origin === "resource" || origin === "project") return origin;
  const assetRef = String(ref?.asset_ref || "").trim();
  if (assetRef.startsWith("resource:")) return "resource";
  if (assetRef.startsWith("project:")) return "project";
  const asset = ideaReferenceAsset(ref);
  return asset?.origin === "resource" ? "resource" : "project";
}

function ideaReferenceUrl(ref) {
  return sceneAssetUrl(ref?.path || "", ideaReferenceOrigin(ref));
}

function makeIdeaReference(asset) {
  const versionLabel = asset.version_status ? CARD_VERSION_STATUS_LABELS[asset.version_status] || asset.version_status : "";
  const sourceNote = asset.card_id
    ? `${asset.card_id}${asset.version_id ? ` ${asset.version_id}` : ""}${versionLabel ? ` · ${versionLabel}` : ""}`
    : "";
  return {
    ref_id: asset.asset_id || asset.path || asset.ref,
    asset_ref: asset.ref,
    asset_id: asset.asset_id || asset.role || asset.path,
    path: asset.path || "",
    origin: asset.origin || "project",
    kind: asset.kind || "image",
    role: asset.role || "",
    version_id: asset.version_id || "",
    version_status: asset.version_status || "",
    card_type: asset.card_type || "",
    card_id: asset.card_id || "",
    card_title: asset.card_title || "",
    note: sourceNote ? `参考卡片版本 / Use card version: ${sourceNote}` : "",
  };
}

function normalizeIdeaReferenceList(refs) {
  const byKey = new Map();
  (refs || []).forEach((ref) => {
    const key = ideaReferenceKey(ref);
    if (key) byKey.set(key, ref);
  });
  return [...byKey.values()];
}

function activeProjectBibleCard(board = currentIdeaBoard()) {
  const cards = board.project_bible || [];
  if (!cards.length) return null;
  const index = clamp(Number(state.ideaActiveBibleIndex || 0), 0, Math.max(0, cards.length - 1));
  state.ideaActiveBibleIndex = index;
  return cards[index] || null;
}

function activeIdeaRow(board = currentIdeaBoard()) {
  const rows = board.rows || [];
  const visibleIndex = ensureIdeaActiveRowForFilteredCards(board);
  if (visibleIndex === null && selectedScene()?.scene_id) return null;
  const index = clamp(Number(state.ideaActiveRowIndex || 0), 0, Math.max(0, rows.length - 1));
  state.ideaActiveRowIndex = index;
  return rows[index] || null;
}

function cleanIdeaBatchRows(board = currentIdeaBoard()) {
  const maxIndex = Math.max(0, (board.rows || []).length - 1);
  const sceneId = selectedScene()?.scene_id || "";
  const visibleIndexes = sceneId ? new Set(filteredIdeaRowEntriesForCurrentScene(board).map(({ index }) => index)) : null;
  state.ideaBatchRows = [
    ...new Set(
      (state.ideaBatchRows || [])
        .map((index) => Number(index))
        .filter((index) => Number.isInteger(index) && index >= 0 && index <= maxIndex)
        .filter((index) => !visibleIndexes || visibleIndexes.has(index)),
    ),
  ];
  return state.ideaBatchRows;
}

function ideaBatchRowSet(board = currentIdeaBoard()) {
  return new Set(cleanIdeaBatchRows(board));
}

function ensureIdeaActiveRowForFilteredCards(board = currentIdeaBoard()) {
  const entries = filteredIdeaRowEntriesForCurrentScene(board);
  if (!entries.length) return ensureIdeaActiveRowForScene(board);
  const activeIndex = Number(state.ideaActiveRowIndex || 0);
  if (!entries.some(({ index }) => index === activeIndex)) {
    state.ideaActiveRowIndex = entries[0].index;
  }
  return state.ideaActiveRowIndex;
}

function ideaReferenceActOptions(assets = allBoardImageAssets()) {
  return imageLibraryScopeOptions(assets);
}

function ideaReferenceAssets() {
  const assets = allBoardImageAssets().filter((asset) => frameIsUsable(asset));
  const filters = currentImageLibraryFilters(assets);
  return assets.filter((asset) => imageAssetMatchesLibraryFilters(asset, { act: filters.scope, tag: filters.tag, query: filters.query }, "act"));
}

function addIdeaReferenceToRows(board, asset, rowIndexes) {
  const ref = makeIdeaReference(asset);
  let count = 0;
  [...new Set(rowIndexes.map((index) => Number(index)).filter((index) => Number.isInteger(index)))]
    .forEach((index) => {
      const row = board.rows[index];
      if (!row) return;
      row.references = normalizeIdeaReferenceList([...(row.references || []), ref]);
      count += 1;
    });
  return count;
}

function addIdeaReference(scope, assetRef, rowIndexes = null) {
  const board = collectIdeaBoardFromDom();
  const asset = allBoardImageAssets().find((item) => item.ref === assetRef);
  if (!asset) return;
  let count = 0;
  if (scope === "global") {
    const ref = makeIdeaReference(asset);
    board.global_references = normalizeIdeaReferenceList([...(board.global_references || []), ref]);
    count = 1;
  } else if (scope === "bible") {
    const ref = makeIdeaReference(asset);
    const targetIndex = rowIndexes?.length ? Number(rowIndexes[0]) : state.ideaActiveBibleIndex;
    const card = board.project_bible?.[targetIndex];
    if (card) {
      card.references = normalizeIdeaReferenceList([...(card.references || []), ref]);
      state.ideaActiveBibleIndex = targetIndex;
      count = 1;
    }
  } else if (scope === "batch") {
    const targets = Array.isArray(rowIndexes) ? rowIndexes : cleanIdeaBatchRows(board);
    count = addIdeaReferenceToRows(board, asset, targets);
  } else {
    const targetIndex = rowIndexes?.length ? Number(rowIndexes[0]) : state.ideaActiveRowIndex;
    count = addIdeaReferenceToRows(board, asset, [targetIndex]);
    if (!Number.isNaN(targetIndex)) state.ideaActiveRowIndex = targetIndex;
  }
  setIdeaBoardLocal(board);
  renderIdeaLab();
  if (count) {
    if (scope === "global") toast("已加入全局参考 / Added to global refs");
    else if (scope === "bible") toast("已加入设定卡 / Added to settings card");
    else toast(`已绑定到 ${count} 条分镜 / Added to ${count} rows`);
  }
  else if (scope === "batch") toast("请先勾选同步参考条目 / Select rows to sync refs");
}

function removeIdeaReference(scope, key, rowIndex = null) {
  const board = collectIdeaBoardFromDom();
  const removeFrom = (refs = []) => refs.filter((ref) => ideaReferenceKey(ref) !== key);
  if (scope === "global") {
    board.global_references = removeFrom(board.global_references);
  } else if (scope === "bible") {
    if (rowIndex !== null && !Number.isNaN(Number(rowIndex))) state.ideaActiveBibleIndex = Number(rowIndex);
    const card = board.project_bible?.[state.ideaActiveBibleIndex];
    if (card) card.references = removeFrom(card.references || []);
  } else {
    if (rowIndex !== null && !Number.isNaN(Number(rowIndex))) state.ideaActiveRowIndex = Number(rowIndex);
    const row = board.rows[state.ideaActiveRowIndex];
    if (row) row.references = removeFrom(row.references || []);
  }
  setIdeaBoardLocal(board);
  renderIdeaLab();
}

function updateIdeaReferenceNote(scope, key, note) {
  const board = collectIdeaBoardFromDom();
  const updateRefs = (refs = []) =>
    refs.map((ref) => (ideaReferenceKey(ref) === key ? { ...ref, note } : ref));
  if (scope === "global") {
    board.global_references = updateRefs(board.global_references || []);
  } else if (scope === "bible") {
    const card = board.project_bible?.[state.ideaActiveBibleIndex];
    if (card) card.references = updateRefs(card.references || []);
  } else {
    const row = board.rows[state.ideaActiveRowIndex];
    if (row) row.references = updateRefs(row.references || []);
  }
  setIdeaBoardLocal(board);
}

function renderIdeaReferenceChip(ref, scope, rowIndex = "") {
  const asset = ideaReferenceAsset(ref);
  const label = ref.asset_id || asset?.asset_id || ref.path || "Reference";
  const key = ideaReferenceKey(ref);
  const imageRef = {
    ...ref,
    path: ref.path || asset?.path || "",
    origin: ref.origin || asset?.origin || "",
    asset_ref: ref.asset_ref || asset?.ref || "",
  };
  const imageUrl = isImagePath(imageRef.path || "") ? ideaReferenceUrl(imageRef) : "";
  return `
    <div class="idea-ref-chip" data-ref-key="${escapeHtml(key)}">
      ${imageUrl ? `<img src="${escapeHtml(imageUrl)}" alt="${escapeHtml(label)}" loading="lazy" />` : ""}
      <span>${escapeHtml(label)}</span>
      <button class="icon-button idea-remove-ref" data-ref-scope="${escapeHtml(scope)}" data-ref-key="${escapeHtml(key)}" data-idea-index="${escapeHtml(rowIndex)}" type="button" title="移除参考 / Remove">×</button>
    </div>
  `;
}

function renderIdeaReferenceEditor(ref, scope) {
  const asset = ideaReferenceAsset(ref);
  const label = ref.asset_id || asset?.asset_id || ref.path || "Reference";
  const key = ideaReferenceKey(ref);
  const imageRef = {
    ...ref,
    path: ref.path || asset?.path || "",
    origin: ref.origin || asset?.origin || "",
    asset_ref: ref.asset_ref || asset?.ref || "",
  };
  const imageUrl = isImagePath(imageRef.path || "") ? ideaReferenceUrl(imageRef) : "";
  return `
    <article class="idea-ref-editor">
      <div class="idea-ref-editor-head">
        ${imageUrl ? `<img src="${escapeHtml(imageUrl)}" alt="${escapeHtml(label)}" loading="lazy" />` : ""}
        <div>
          <strong>${escapeHtml(label)}</strong>
          <small>${escapeHtml(kindLabel(ref.kind || asset?.kind))} · ${escapeHtml(ref.path || asset?.path || "")}</small>
        </div>
        <button class="icon-button idea-remove-ref" data-ref-scope="${escapeHtml(scope)}" data-ref-key="${escapeHtml(key)}" type="button" title="移除参考 / Remove">×</button>
      </div>
      <textarea class="idea-ref-note" data-ref-scope="${escapeHtml(scope)}" data-ref-key="${escapeHtml(key)}" rows="2" placeholder="说明要借用什么：人物身份、服装、场景结构、道具、光影等">${escapeHtml(ref.note || "")}</textarea>
    </article>
  `;
}

function renderIdeaReferenceAssetGrid(row) {
  const assets = ideaReferenceAssets().slice(0, 36);
  const batchCount = cleanIdeaBatchRows().length;
  const bibleMode = isProjectBibleSelected();
  return assets.length
    ? assets
        .map(
          (asset) => {
            const versionLabel = asset.version_status ? CARD_VERSION_STATUS_LABELS[asset.version_status] || asset.version_status : "";
            return `
            <article class="idea-ref-asset" draggable="true" data-asset-ref="${escapeHtml(asset.ref)}">
              <img src="${escapeHtml(asset.url)}" alt="${escapeHtml(asset.asset_id || asset.path)}" loading="lazy" />
              <strong>${escapeHtml(asset.asset_id || asset.role || asset.path)}</strong>
              <small>${escapeHtml(asset.scene_id || asset.act_id || "PROJECT")} · ${escapeHtml(kindLabel(asset.kind))}${versionLabel ? ` · ${escapeHtml(versionLabel)}` : ""}${escapeHtml(assetQaLabel(asset))}</small>
              ${asset.card_id ? `<small>${escapeHtml(asset.card_id)}${asset.card_title ? ` · ${escapeHtml(asset.card_title)}` : ""}</small>` : ""}
              <div>
                <button class="mini-command idea-add-ref" data-ref-scope="global" data-asset-ref="${escapeHtml(asset.ref)}" type="button">全局</button>
                ${
                  bibleMode
                    ? `<button class="mini-command idea-add-ref" data-ref-scope="bible" data-asset-ref="${escapeHtml(asset.ref)}" type="button" ${activeProjectBibleCard() ? "" : "disabled"}>当前卡</button>`
                    : `<button class="mini-command idea-add-ref" data-ref-scope="row" data-asset-ref="${escapeHtml(asset.ref)}" type="button" ${row ? "" : "disabled"}>当前卡</button>
                       <button class="mini-command idea-add-ref" data-ref-scope="batch" data-asset-ref="${escapeHtml(asset.ref)}" type="button" ${batchCount ? "" : "disabled"}>勾选卡</button>`
                }
              </div>
            </article>
          `;
          },
        )
        .join("")
    : `<div class="empty-state">没有匹配参考图 / No matching references.</div>`;
}

function bindIdeaReferenceAssetButtons(root = document) {
  root.querySelectorAll(".idea-add-ref").forEach((button) => {
    button.addEventListener("click", () => addIdeaReference(button.dataset.refScope || "row", button.dataset.assetRef || ""));
  });
  root.querySelectorAll(".idea-ref-asset").forEach((card) => {
    card.addEventListener("dragstart", (event) => {
      const assetRef = card.dataset.assetRef || "";
      if (!assetRef) return;
      event.dataTransfer?.setData("text/plain", assetRef);
      event.dataTransfer?.setData("application/x-pipeline-asset-ref", assetRef);
      event.dataTransfer.effectAllowed = "copy";
    });
  });
}

function refreshIdeaReferenceAssetGrid() {
  const board = collectIdeaBoardFromDom();
  setIdeaBoardLocal(board);
  const grid = document.querySelector(".idea-ref-asset-grid");
  if (!grid) return;
  grid.innerHTML = renderIdeaReferenceAssetGrid(activeIdeaRow(board));
  bindIdeaReferenceAssetButtons(grid);
}

function renderIdeaReferenceMapping(board, entries = filteredIdeaRowEntriesForCurrentScene(board)) {
  const globalRefs = board.global_references || [];
  const rowRefTotal = (board.rows || []).reduce((sum, row) => sum + (Array.isArray(row.references) ? row.references.length : 0), 0);
  const scene = selectedScene();
  return `
    <details class="idea-ref-mapping" open>
      <summary>
        <span>参考映射表 / Reference mapping</span>
        <small>${globalRefs.length} 全局 · ${rowRefTotal} 条目参考 · 当前筛选 ${entries.length}</small>
      </summary>
      <div class="idea-map-global">
        <strong>全局作用于全部分镜 / Global refs apply to all rows</strong>
        <div>${globalRefs.length ? globalRefs.map((ref) => renderIdeaReferenceChip(ref, "global")).join("") : `<span class="muted-inline">暂无全局参考</span>`}</div>
      </div>
      <div class="idea-map-table">
        ${
          entries.length
            ? entries
                .map(({ row, index }) => {
                  const refs = Array.isArray(row.references) ? row.references : [];
                  return `
                    <article class="idea-map-row ${state.ideaActiveRowIndex === index ? "active" : ""}" data-idea-index="${index}">
                      <button class="mini-command idea-map-focus" data-idea-index="${index}" type="button">${escapeHtml(row.item_id || `#${index + 1}`)}</button>
                      <span>${escapeHtml(row.beat || row.frame_description || "未命名分镜")}</span>
                      <div>${refs.length ? refs.map((ref) => renderIdeaReferenceChip(ref, "row", index)).join("") : `<span class="muted-inline">可把参考图拖到这一条</span>`}</div>
                    </article>
                  `;
                })
                .join("")
            : `<div class="empty-state">当前范围暂无分镜条目 / No storyboard rows for this scope.</div>`
        }
      </div>
    </details>
  `;
}

function renderIdeaReferencePanel(board) {
  const entries = filteredIdeaRowEntriesForCurrentScene(board);
  ensureIdeaActiveRowForFilteredCards(board);
  cleanIdeaBatchRows(board);
  const row = activeIdeaRow(board);
  const globalRefs = board.global_references || [];
  const rowRefs = row?.references || [];
  const batchSet = ideaBatchRowSet(board);
  const filters = currentImageLibraryFilters(allBoardImageAssets().filter((asset) => frameIsUsable(asset)));
  return `
    <details class="idea-reference-panel" open>
      <summary>
        <span>参考库 / References</span>
        <small>${globalRefs.length} 全局 · ${rowRefs.length} 当前条目</small>
      </summary>
      <div class="idea-reference-content">
        <div class="idea-reference-controls">
          <select id="ideaRefActFilter">
            ${ideaReferenceActOptions().map((option) => `<option value="${escapeHtml(option.value)}" ${filters.scope === option.value ? "selected" : ""}>${escapeHtml(option.label)}</option>`).join("")}
          </select>
          <select id="ideaRefTagFilter">
            ${BOARD_TAG_OPTIONS.map((option) => `<option value="${escapeHtml(option.value)}" ${filters.tag === option.value ? "selected" : ""}>${escapeHtml(option.label)}</option>`).join("")}
          </select>
          <input id="ideaRefSearchInput" value="${escapeHtml(filters.query || "")}" placeholder="搜索人设、场景、道具 / Search refs" />
        </div>
        <div class="idea-target-controls">
          <div class="idea-current-target">
            <strong>当前分镜卡 / Current card</strong>
            <span>${escapeHtml(row?.item_id || "当前场戏暂无条目")}</span>
            <small>点每条分镜里的“参考 / Refs”切换。</small>
          </div>
          <div class="idea-batch-control">
            <strong>批量绑定参考 / Batch refs</strong>
            <div class="idea-batch-list">
              ${entries.length
                ? entries
                    .map(
                      ({ row: item, index }) => `
                    <label class="idea-batch-item">
                      <input class="idea-batch-check" data-idea-index="${index}" type="checkbox" ${batchSet.has(index) ? "checked" : ""} />
                      <span>${escapeHtml(item.item_id || `#${index + 1}`)}</span>
                    </label>
                  `,
                    )
                    .join("")
                : `<span class="muted-inline">当前范围暂无可批量绑定的条目。</span>`}
            </div>
          </div>
        </div>
        <section class="idea-ref-section">
          <strong>全局参考 / Global</strong>
          <div class="idea-ref-list">${globalRefs.length ? globalRefs.map((ref) => renderIdeaReferenceEditor(ref, "global")).join("") : `<span class="muted-inline">适合人设、统一场景、道具和风格。</span>`}</div>
        </section>
        <section class="idea-ref-section">
          <strong>当前条目 / Current: ${escapeHtml(row?.item_id || "无")}</strong>
          <div class="idea-ref-list">${rowRefs.length ? rowRefs.map((ref) => renderIdeaReferenceEditor(ref, "row")).join("") : `<span class="muted-inline">只影响当前选中的分镜。</span>`}</div>
        </section>
        <div class="idea-ref-asset-grid">
          ${renderIdeaReferenceAssetGrid(row)}
        </div>
        ${renderIdeaReferenceMapping(board, entries)}
      </div>
    </details>
  `;
}

function renderActAutopilotPanel(board) {
  const actId = activeStoryActId() || nextIdeaActId(board.acts || []);
  const activeAct = storyActEntryForId(board, actId) || {};
  const inputs = activeIdeaInputs(board);
  const missingRows = (board.rows || []).filter((row) => rowMatchesStoryAct(row, actId, board)).length;
  return `
    <details class="idea-autopilot-panel">
      <summary>
        <span>远程总控 / Act Autopilot</span>
        <small>${escapeHtml(actId || "ACT")} · ${missingRows} cards</small>
      </summary>
      <div class="idea-autopilot-content">
        <div class="idea-meta-grid">
          <label>目标幕 / Target act <input id="actAutopilotActId" value="${escapeHtml(actId || "")}" /></label>
        </div>
        <label>这一幕主要剧情 / Main plot
          <textarea id="actAutopilotBrief" rows="6" placeholder="把第三幕主要剧情写在这里；Codex 会按它扩写幕结构、拆分镜、找参考、判断白模并生成图片包。">${escapeHtml(inputs.idea || activeAct.summary || "")}</textarea>
        </label>
        <div class="idea-autopilot-gates">
          <span>01 扩写幕</span>
          <span>02 拆分镜</span>
          <span>03 自动找参考</span>
          <span>04 白模门禁</span>
          <span>05 生图回填</span>
        </div>
        <button id="actAutopilotBtn" class="command-button primary full" data-help="可选入口：生成一张 Codex 远程总控分析卡。真正远程时，用户也可以直接在聊天里给剧情，由 Codex 调用后台接口继续执行。" type="button">远程生成 / Autopilot Act</button>
      </div>
    </details>
  `;
}

function buildIdeaActsHandoff(board) {
  const apiUrl = `${location.origin}/api/projects/${state.selectedSlug}/idea-board`;
  const schema = {
    idea: board.idea || "",
    story_title: board.story_title || "短片片名",
    logline: board.logline || "一句话故事",
    story_outline: board.story_outline || "完整故事大纲",
    style_notes: board.style_notes || "整体风格与连续性，所有幕共用",
    act_inputs: {
      ACT01: {
        idea: "第一幕独立故事草稿",
        story_title: "",
        logline: "",
      },
      ACT02: {
        idea: "第二幕独立故事草稿",
        story_title: "",
        logline: "",
      },
    },
    acts: [
      {
        act_id: "ACT01",
        title: "幕标题",
        summary: "这一幕从哪里开始到哪里结束",
        dramatic_purpose: "这一幕承担的戏剧功能",
        key_beats: "关键剧情点",
        status: "draft",
      },
    ],
    project_bible: board.project_bible || [],
    global_references: board.global_references || [],
    rows: board.rows || [],
    completed_handoff_ids: [IDEA_HANDOFF_ID_PLACEHOLDER],
  };
  return [
    "# Codex Build Acts Handoff / Codex 生成幕交接包",
    "",
    "请根据完整故事大纲，把故事扩展成一幕幕独立的戏。这个动作只负责生成或更新幕结构，不生成分镜卡。",
    "",
    "## Codex Run Mode / 执行模式",
    "- “设定”和“幕”是平行结构：project_bible/global_references 是设定；acts/act_inputs 是一幕幕独立的戏。",
    "- 只根据 story_outline、title、logline 和已有设定拆分 acts，并为每一幕写入 act_inputs[act_id].idea。",
    "- style_notes 是整体风格与连续性，所有幕共用；不要把它拆散到单幕。",
    "- project_bible、global_references、rows、已有 versions 必须保留；不要新增、删除或重写 rows。",
    "- 每一幕要有明确起点、终点、戏剧功能和关键剧情点。",
    "- 回填成功后只汇报幕数量、每幕一句话和是否保留了既有分镜卡。",
    "",
    "## Project / 项目",
    `- Project slug: ${state.selectedSlug || ""}`,
    `- Project root: ${state.detail?.path || ""}`,
    `- Callback: POST ${apiUrl}`,
    "",
    "## Existing Scene Context / 现有场景资源（仅作参考，不决定幕结构）",
    compactProjectSceneContext(),
    "",
    "## Current Idea Board / 当前内容",
    "```json",
    JSON.stringify(schema, null, 2),
    "```",
    "",
    "## Required Callback / 必须回填",
    `POST ${apiUrl}`,
    "Content-Type: application/json",
    "Body must include the full board shape above and completed_handoff_ids containing the codex_handoff_id above. Update only acts and act_inputs unless the user explicitly asked otherwise. Preserve project_bible/global_references/rows/versions.",
  ].join("\n");
}

function buildIdeaStoryboardCardsHandoff(board) {
  const apiUrl = `${location.origin}/api/projects/${state.selectedSlug}/idea-board`;
  const actId = activeStoryActId();
  const targetAct = storyActEntryForId(board, actId) || {};
  const actInput = board.act_inputs?.[actId] || {};
  const scene = selectedScene();
  const sceneId = targetAct.scene_id || scene?.scene_id || defaultSceneIdForAct(board, actId);
  const targetRows = (board.rows || []).filter((row) => rowMatchesStoryAct(row, actId, board));
  const targetScope = {
    selected_act_id: actId,
    selected_act_title: targetAct.title || actId,
    selected_scene_id: sceneId || "",
    default_scene_id: sceneId || "",
    existing_rows_for_act: targetRows.map((row) => row.item_id || ""),
    card_filter_scope: normalizedCardFilters("storyboard", board).scope,
  };
  const schema = {
    idea: board.idea || actInput.idea || "",
    story_title: board.story_title || actInput.story_title || "",
    logline: board.logline || actInput.logline || "",
    story_outline: board.story_outline || "",
    style_notes: board.style_notes || "",
    act_inputs: board.act_inputs || {},
    acts: board.acts || [],
    project_bible: board.project_bible || [],
    global_references: board.global_references || [],
    rows: board.rows || [
      {
        item_id: `${actId || "ACT"}_SHOT_001`,
        act_id: scene?.act_id || actId || "ACT01",
        scene_id: targetScope.default_scene_id || "",
        beat: "剧情点",
        shot_type: "远景/中景/近景/特写/运动镜头等",
        frame_description: "这一帧看到什么，谁在哪里，情绪和动作是什么",
        linked_cards: [],
        spatial_logic: "空间硬规则：门内外方向、人物视线、左右关系、屏幕位置、遮挡关系等",
        image_prompt: "可直接用于生成高质量分镜关键帧的图片提示词",
        video_prompt: "后续视频生成提示词，可选",
        notes: "导演备注、连续性、参考资产需求",
        revision_note: "",
        references: [],
        selected: true,
        versions: [],
        status: "draft",
      },
    ],
    completed_handoff_ids: [IDEA_HANDOFF_ID_PLACEHOLDER],
  };
  return [
    "# Codex Build Storyboard Cards Handoff / Codex 生成分镜卡交接包",
    "",
    "请只根据当前幕的故事内容，把这一幕拆成一张张分镜文字卡。这个动作不生成图片，只生成 rows。",
    "",
    "## Codex Run Mode / 执行模式",
    "- 当前目标是单幕分镜卡：只处理 Target Act 对应的 rows。",
    "- 如果 Target Act 有 selected_scene_id，只新增或替换 scene_id 等于 selected_scene_id 的 rows；否则只处理 act_id 等于 selected_act_id 的 rows。",
    "- act_inputs[selected_act_id].idea 是当前幕独立故事内容；story_outline 只作为全局背景。",
    "- project_bible/global_references/style_notes 是全局设定，必须继承到 image_prompt 的连续性里。",
    "- 保留其他幕 rows、project_bible、global_references 和所有 versions；只新增或替换当前幕 rows。",
    "- 每张分镜卡必须有 item_id、act_id、scene_id、beat、shot_type、frame_description、linked_cards、spatial_logic、image_prompt、video_prompt、notes。",
    "- item_id 建议使用 ACTxx_SHOT_001 这种格式，必须跟当前幕编号一致。",
    "- 如果当前幕已有 rows，可以按当前幕故事重排当前幕 rows，但不要碰其他幕。",
    "- 回填成功后只汇报当前幕生成了多少张分镜卡和最关键的镜头节奏建议。",
    "",
    "## Project / 项目",
    `- Project slug: ${state.selectedSlug || ""}`,
    `- Project root: ${state.detail?.path || ""}`,
    `- Callback: POST ${apiUrl}`,
    "",
    "## Target Act / 当前幕",
    "```json",
    JSON.stringify(targetScope, null, 2),
    "```",
    "",
    "## Current Act Story / 当前幕故事",
    actInput.idea || targetAct.summary || targetAct.key_beats || board.idea || "- 当前幕故事为空，请根据这一幕的 summary/key_beats 保守拆分。",
    "",
    "## Current Idea Board / 当前内容",
    "```json",
    JSON.stringify(schema, null, 2),
    "```",
    "",
    "## Required Callback / 必须回填",
    `POST ${apiUrl}`,
    "Content-Type: application/json",
    "Body must include the full board shape above and completed_handoff_ids containing the codex_handoff_id above. Modify only rows for the Target Act: if selected_scene_id is present, match rows by scene_id; otherwise match rows by selected_act_id. Preserve all unrelated rows, settings, references, and versions.",
  ].join("\n");
}

function buildProjectBibleAnalysisHandoff(board) {
  const apiUrl = `${location.origin}/api/projects/${state.selectedSlug}/idea-board`;
  const schema = {
    idea: board.idea || "",
    story_title: board.story_title || "短片片名",
    logline: board.logline || "一句话故事",
    story_outline: board.story_outline || "剧本大纲",
    style_notes: board.style_notes || "全局风格与连续性",
    acts: board.acts || [],
    project_bible: [
      {
        card_id: "BIBLE_CHARACTER_001",
        scope: "project",
        act_id: "",
        category: "character / location / prop / lookdev / mood / period / constraint",
        title: "设定卡标题",
        summary: "分析对象的核心设定，不写剧情分镜",
        visual_direction: "造型、材质、色彩、光线、年代细节和设计规则",
        prompt_notes: "可直接加入后续分镜图片提示词的稳定描述",
        revision_note: "本轮生成或精修时要重点改变什么；留空则按长期设定生成",
        negative_prompt: "必须避免的偏差、现代元素、错误风格或误读",
        references: [
          {
            asset_ref: "project:path-or-resource:path",
            asset_id: "参考图",
            path: "reference image path",
            origin: "project or resource",
            kind: "character_ref / scene_ref / prop_ref / lookdev / image",
            note: "说明这张参考图在设定里的作用",
          },
        ],
        selected: true,
        image_selected: true,
        preview_path: "",
        versions: [],
        status: "draft",
      },
    ],
    global_references: board.global_references || [],
    rows: board.rows || [],
    completed_handoff_ids: [IDEA_HANDOFF_ID_PLACEHOLDER],
  };
  return [
    "# Codex Settings Handoff / Codex 设定卡交接包",
    "",
    "请解析当前项目资料，重点产出人物、美术、场景、道具、氛围、年代和负面约束等设定卡。不要扩写剧情分镜，除非 rows 已存在则原样保留。",
    "",
    "## Codex Run Mode / 执行模式",
    "- 分析目标不是故事推进，而是项目级设定：人物、场景、道具、美术、氛围、年代、统一负面约束。",
    "- 每张 concept card 都是独立可生成/可精修的卡片；scope=project 表示全片通用，scope=act 且 act_id 有值表示只服务某一幕。",
    "- 每张 project_bible 卡都要能直接服务后续图片生成；prompt_notes 必须可执行、稳定、具体。",
    "- references 和 global_references 要保留；可根据已有参考图 note 推断它属于人物、场景、道具或美术。",
    "- 不要删除现有 acts 或 rows；只更新 project_bible、style_notes 和必要的 global reference notes。",
    "- 回填成功后，只汇报卡片数量和最关键的视觉统一建议。",
    "",
    "## Project / 项目",
    `- Project slug: ${state.selectedSlug || ""}`,
    `- Project root: ${state.detail?.path || ""}`,
    `- Callback: POST ${apiUrl}`,
    "",
    "## Current Context / 当前上下文",
    "```json",
    JSON.stringify({
      idea: board.idea || "",
      story_title: board.story_title || "",
      logline: board.logline || "",
      story_outline: board.story_outline || "",
      style_notes: board.style_notes || "",
      acts: board.acts || [],
      project_bible: board.project_bible || [],
      global_references: board.global_references || [],
    }, null, 2),
    "```",
    "",
    "## Required JSON Schema / 必须回填的 JSON 结构",
    "```json",
    JSON.stringify(schema, null, 2),
    "```",
    "",
    "## Callback Instruction / 回填说明",
    `POST ${apiUrl}`,
    "Content-Type: application/json",
    "Body must include the full board shape above and completed_handoff_ids containing the codex_handoff_id above. Preserve rows unless explicitly asked to change them.",
  ].join("\n");
}

function addIdeaHandoff(handoff) {
  const id = `idea_handoff_${Date.now()}_${Math.random().toString(16).slice(2, 8)}`;
  const text = handoff.text || "";
  const includeCompletionNote = handoff.codexCompletionNote !== false;
  const nextHandoff = {
    id,
    createdAt: new Date().toLocaleString(),
    autoCopy: true,
    ...handoff,
    text: includeCompletionNote ? withIdeaHandoffCompletionNote(text, id) : text,
  };
  state.ideaHandoffs = [nextHandoff, ...state.ideaHandoffs].slice(0, 12);
  saveIdeaHandoffs();
  autoCopyHandoffText(nextHandoff.text);
  syncIdeaHandoffCompletionPolling();
}

function renderIdeaHandoffs() {
  if (!state.ideaHandoffs.length) {
    return `<div class="idea-handoff-empty">生成的 Codex 分析卡/交接卡会出现在这里，可以拖进聊天框。</div>`;
  }
  return `
    <div class="idea-handoff-toolbar">
      <span>${state.ideaHandoffs.length} 张 Codex 分析卡 · 回填完成后会自动清除</span>
      <button class="mini-command idea-clear-handoffs" data-help="清掉本地显示的临时 Codex 分析卡，不删除已经保存的分镜、图片和项目文件。" type="button">清空 / Clear</button>
    </div>
    <div class="idea-handoff-list">
      ${state.ideaHandoffs
        .map(
          (handoff) => `
            <article class="idea-handoff-card ${escapeHtml(classToken(handoff.status))}" draggable="true" data-idea-handoff-id="${escapeHtml(handoff.id)}">
              <div>
                <strong>${escapeHtml(handoff.title || "Codex handoff")}</strong>
                <small>${escapeHtml(handoff.kind || "")} · ${escapeHtml(handoff.createdAt || "")}</small>
                ${handoff.path ? `<small>${escapeHtml(handoff.path)}</small>` : ""}
                ${handoff.openFolder ? `<small>位置 / Folder: ${escapeHtml(handoff.openFolder)}</small>` : ""}
                ${handoff.imageFolder ? `<small>图片包 / Images: ${escapeHtml(handoff.imageFolder)}</small>` : ""}
                ${handoff.message ? `<small class="idea-handoff-message">${escapeHtml(handoff.message)}</small>` : ""}
                ${handoff.autoCopy ? `<small class="handoff-copy-hint">已尝试自动复制 / Auto-copy attempted</small>` : ""}
              </div>
              <div class="idea-handoff-actions">
                <button class="mini-command idea-copy-handoff" data-idea-handoff-id="${escapeHtml(handoff.id)}" type="button">复制 / Copy</button>
                ${handoff.openFolder || handoff.imageFolder ? `<button class="mini-command idea-open-image-folder" data-idea-handoff-id="${escapeHtml(handoff.id)}" type="button">${escapeHtml(handoff.openFolderLabel || (handoff.openFolder ? "打开位置 / Open" : "打开图片包 / Open"))}</button>` : ""}
                <button class="icon-button idea-delete-handoff" data-idea-handoff-id="${escapeHtml(handoff.id)}" type="button" title="删除 / Delete">×</button>
              </div>
              <details>
                <summary>展开文本 / Show text</summary>
                <textarea readonly rows="7">${escapeHtml(handoff.text || "")}</textarea>
              </details>
            </article>
          `,
        )
        .join("")}
    </div>
  `;
}

function addDailyIdeaHandoff(handoff) {
  const id = `daily_idea_handoff_${Date.now()}_${Math.random().toString(16).slice(2, 8)}`;
  const text = String(handoff.text || handoff.handoff_text || "").replaceAll(IDEA_HANDOFF_ID_PLACEHOLDER, id);
  const next = {
    id,
    createdAt: new Date().toLocaleString(),
    autoCopy: true,
    ...handoff,
    text,
  };
  state.dailyIdeas.handoffs = [next, ...(state.dailyIdeas.handoffs || [])].slice(0, 12);
  saveDailyIdeaHandoffs();
  autoCopyHandoffText(text);
}

function renderDailyIdeaHandoffs() {
  const handoffs = state.dailyIdeas.handoffs || [];
  if (!handoffs.length) {
    return `<div class="idea-handoff-empty">点击“生成今日热点”后，这里会出现可复制给 Codex 的生产卡。</div>`;
  }
  return `
    <div class="idea-handoff-toolbar">
      <span>${handoffs.length} 张灵感生产卡 · 复制后我会执行并回填到当天页面</span>
      <button class="mini-command daily-clear-handoffs" type="button">清空 / Clear</button>
    </div>
    <div class="idea-handoff-list">
      ${handoffs
        .map(
          (handoff) => `
            <article class="idea-handoff-card ready" draggable="true" data-daily-handoff-id="${escapeHtml(handoff.id)}">
              <div>
                <strong>${escapeHtml(handoff.title || "每日灵感生产卡")}</strong>
                <small>${escapeHtml(handoff.createdAt || "")}</small>
                ${handoff.callbackUrl ? `<small>${escapeHtml(handoff.callbackUrl)}</small>` : ""}
                ${handoff.autoCopy ? `<small class="handoff-copy-hint">已尝试自动复制 / Auto-copy attempted</small>` : ""}
              </div>
              <div class="idea-handoff-actions">
                <button class="mini-command daily-copy-handoff" data-daily-handoff-id="${escapeHtml(handoff.id)}" type="button">复制 / Copy</button>
                <button class="icon-button daily-delete-handoff" data-daily-handoff-id="${escapeHtml(handoff.id)}" type="button" title="删除 / Delete">×</button>
              </div>
              <details>
                <summary>展开生产卡 / Show packet</summary>
                <textarea readonly rows="7">${escapeHtml(handoff.text || "")}</textarea>
              </details>
            </article>
          `,
        )
        .join("")}
    </div>
  `;
}

function dailyIdeaAssetForRow(row) {
  const path = row?.output_path || "";
  return (state.dailyIdeas.detail?.assets || []).find((asset) => asset.path === path || asset.item_id === row?.item_id) || null;
}

function renderDailyIdeaRows() {
  const board = state.dailyIdeas.detail?.idea_board || {};
  const rows = Array.isArray(board.rows) ? board.rows : [];
  if (!rows.length) {
    return `<div class="empty-state">当天还没有灵感卡。先点击“生成今日热点”。/ No idea cards yet.</div>`;
  }
  return rows
    .map((row) => {
      const asset = dailyIdeaAssetForRow(row);
      return `
        <article class="daily-idea-card">
          <div class="daily-idea-thumb">
            ${
              asset?.url
                ? `<img src="${escapeHtml(asset.url)}" alt="${escapeHtml(row.beat || row.item_id || "")}" loading="lazy" />`
                : `<div class="daily-idea-placeholder">待生成图片</div>`
            }
          </div>
          <div class="daily-idea-card-body">
            <div class="daily-idea-card-title">
              <strong>${escapeHtml(row.beat || row.item_id || "Untitled")}</strong>
              <span>${escapeHtml(row.item_id || "")} · ${escapeHtml(row.status || "draft")}</span>
            </div>
            <p>${escapeHtml(row.frame_description || row.notes || "")}</p>
            <div class="daily-idea-meta">
              ${row.output_path ? `<span>${escapeHtml(row.output_path)}</span>` : "<span>无图片路径 / no image path</span>"}
            </div>
            <details>
              <summary>图片提示词 / Image prompt</summary>
              <textarea readonly rows="4">${escapeHtml(row.image_prompt || "")}</textarea>
            </details>
            <details>
              <summary>AIGC 视频提示词 / Video prompt</summary>
              <textarea readonly rows="4">${escapeHtml(row.video_prompt || "")}</textarea>
            </details>
            <details>
              <summary>备注 / Notes</summary>
              <textarea readonly rows="3">${escapeHtml(row.notes || "")}</textarea>
            </details>
          </div>
        </article>
      `;
    })
    .join("");
}

function renderDailyIdeasPage() {
  const root = $("dailyIdeasPage");
  if (!root) return;
  root.hidden = !state.dailyIdeasOpen;
  if (!state.dailyIdeasOpen) return;
  const detail = state.dailyIdeas.detail;
  const date = state.dailyIdeas.selectedDate || todayDateString();
  const board = detail?.idea_board || {};
  root.innerHTML = `
    <div class="daily-ideas-header panel">
      <div>
        <p class="eyebrow">Daily Inspiration</p>
        <h3>${escapeHtml(date)} 每日灵感</h3>
        <span>${Number(detail?.row_count || 0)} 条灵感 · ${Number(detail?.image_count || 0)} 张图</span>
      </div>
      <div class="daily-ideas-actions">
        <input id="dailyIdeaDateInput" type="date" value="${escapeHtml(date)}" />
        <button id="dailyIdeaRefreshBtn" class="command-button" type="button">刷新 / Refresh</button>
        <button id="dailyIdeaOpenFolderBtn" class="command-button" type="button">打开目录 / Open</button>
      </div>
    </div>
    <section class="daily-ideas-layout">
      <aside class="daily-ideas-control panel">
        <label>灵感要求 / Seed
          <textarea id="dailyIdeaSeedInput" rows="6" placeholder="例如：今天中文互联网热点，偏怪诞、怀旧、民俗、梦核，适合直接做AIGC短片。">${escapeHtml(state.dailyIdeas.seed || "")}</textarea>
        </label>
        <label>数量 / Count
          <input id="dailyIdeaCountInput" type="number" min="1" max="12" value="10" />
        </label>
        <button id="dailyIdeaBuildHandoffBtn" class="command-button primary full" type="button">生成今日热点 / Build Today</button>
        <div class="daily-idea-board-summary">
          <strong>${escapeHtml(board.story_title || "今日灵感")}</strong>
          <span>${escapeHtml(board.logline || "")}</span>
        </div>
        <div id="dailyIdeaHandoffDock" class="idea-handoff-dock">${renderDailyIdeaHandoffs()}</div>
      </aside>
      <section class="daily-ideas-results panel">
        <div class="panel-header">
          <h3>热点卡片 / Idea Cards</h3>
          <span>图片和视频提示词会回填到这里</span>
        </div>
        <div class="daily-idea-card-list">${renderDailyIdeaRows()}</div>
      </section>
    </section>
  `;
  bindDailyIdeaEvents();
}

function renderIdeaActPlanner(board) {
  const acts = storyActEntries(board);
  const activeActId = activeStoryActId() || acts[0]?.act_id || "";
  const activeAct = storyActEntryForId(board, activeActId) || acts[0] || null;
  const activeIndex = activeAct ? acts.findIndex((act) => (act.act_id || "") === (activeAct.act_id || "")) : -1;
  const boardActs = Array.isArray(board.acts) ? board.acts : [];
  const boardIndex = activeAct ? boardActs.findIndex((act) => (act.act_id || "") === (activeAct.act_id || "")) : -1;
  const writeIndex = boardIndex >= 0 ? boardIndex : boardActs.length;
  return `
    <details class="idea-act-panel" open>
      <summary>
        <span>当前幕结构 / Current Act</span>
        <small>${activeAct ? `${activeIndex + 1}/${acts.length} · ${escapeHtml(activeAct.act_id || "")}` : "未选择幕 / No act selected"}</small>
      </summary>
      <div class="idea-act-panel-actions">
        <button class="mini-command idea-add-act" type="button">新增幕 / Add Act</button>
      </div>
      <div id="ideaActList" class="idea-act-list">
        ${
          activeAct
            ? `
                    <article class="idea-act-row" data-idea-act-index="${writeIndex}" data-idea-act-id="${escapeHtml(activeAct.act_id || "")}">
                      <header>
                        <label>幕编号 / Act ID <input data-idea-act-field="act_id" value="${escapeHtml(activeAct.act_id || "")}" /></label>
                        <label>标题 / Title <input data-idea-act-field="title" value="${escapeHtml(activeAct.title || "")}" /></label>
                        <label>状态 / Status <input data-idea-act-field="status" value="${escapeHtml(activeAct.status || "draft")}" /></label>
                        <button class="icon-button idea-delete-act" data-idea-act-index="${boardIndex}" type="button" title="删除这一幕 / Delete act" ${boardIndex < 0 ? "disabled" : ""}>×</button>
                      </header>
                      <label>这一幕表达什么 / Act expression
                        <textarea data-idea-act-field="summary" rows="3">${escapeHtml(activeAct.summary || "")}</textarea>
                      </label>
                      <label>戏剧功能 / Dramatic purpose
                        <textarea data-idea-act-field="dramatic_purpose" rows="2">${escapeHtml(activeAct.dramatic_purpose || "")}</textarea>
                      </label>
                      <label>关键剧情点 / Key beats
                        <textarea data-idea-act-field="key_beats" rows="2">${escapeHtml(activeAct.key_beats || "")}</textarea>
                      </label>
                    </article>
                  `
            : `<div class="empty-state">还没有幕结构。可以先点“生成幕”，让 AI 根据故事大纲拆成一幕幕独立的戏。</div>`
        }
      </div>
      <button class="mini-command idea-add-act" type="button">新增幕 / Add Act</button>
    </details>
  `;
}

function projectBibleCategoryLabel(value) {
  return PROJECT_BIBLE_CATEGORY_OPTIONS.find((option) => option.value === value)?.label || value || "设定 / Settings";
}

function projectBibleScopeLabel(value) {
  return PROJECT_BIBLE_SCOPE_OPTIONS.find((option) => option.value === value)?.label || value || "全项目 / Project";
}

function projectBibleActLabel(board, actId) {
  if (!actId) return "全部幕 / All acts";
  const act = (board.acts || []).find((item) => item.act_id === actId);
  return act ? `${act.act_id} · ${act.title || "未命名幕"}` : actId;
}

function renderProjectBibleScopeOptions(selected) {
  const known = PROJECT_BIBLE_SCOPE_OPTIONS.some((option) => option.value === selected);
  const options = known || !selected
    ? PROJECT_BIBLE_SCOPE_OPTIONS
    : [...PROJECT_BIBLE_SCOPE_OPTIONS, { value: selected, label: selected }];
  return options
    .map((option) => `<option value="${escapeHtml(option.value)}" ${selected === option.value ? "selected" : ""}>${escapeHtml(option.label)}</option>`)
    .join("");
}

function renderProjectBibleActOptions(board, selected) {
  const acts = storyActEntries(board);
  const known = !selected || acts.some((act) => act.act_id === selected);
  const options = [
    { value: "", label: "全部幕 / All acts" },
    ...acts.map((act) => ({ value: act.act_id, label: `${act.act_id} · ${act.title || "未命名幕"}` })),
  ];
  if (!known) options.push({ value: selected, label: selected });
  return options
    .map((option) => `<option value="${escapeHtml(option.value)}" ${selected === option.value ? "selected" : ""}>${escapeHtml(option.label)}</option>`)
    .join("");
}

function cardVersionEntries(cardOrRow) {
  const currentPath = cardOrRow?.preview_path || cardOrRow?.output_path || "";
  const versions = Array.isArray(cardOrRow?.versions)
    ? cardOrRow.versions.map((version) => ({
        ...version,
        status: version.status || (version.output_path === currentPath ? "current" : "candidate"),
      }))
    : [];
  const hasCurrentVersion = versions.some((version) => version.status === "current");
  if (currentPath && !versions.some((version) => version.output_path === currentPath)) {
    versions.push({
      version_id: "current",
      output_path: currentPath,
      notes: cardOrRow?.output_notes || "",
      created_at: cardOrRow?.output_attached_at || "",
      status: hasCurrentVersion ? "candidate" : "current",
    });
  }
  return versions.filter((version) => version?.output_path);
}

function cardVersionPreviewKey(cardOrRow) {
  if (!cardOrRow) return "";
  if (cardOrRow.card_id) return `concept:${cardOrRow.card_id}`;
  if (cardOrRow.card_uid) return `storyboard:${cardOrRow.card_uid}`;
  if (cardOrRow.item_id) return `storyboard:${cardOrRow.item_id}`;
  if (cardOrRow.output_path) return `output:${cardOrRow.output_path}`;
  if (cardOrRow.preview_path) return `preview:${cardOrRow.preview_path}`;
  return "";
}

function preferredCardVersion(cardOrRow, versions) {
  const key = cardVersionPreviewKey(cardOrRow);
  const selectedPath = key ? state.cardVersionPreview[key] || "" : "";
  if (selectedPath) {
    const selected = versions.find((version) => version.output_path === selectedPath);
    if (selected) return selected;
    delete state.cardVersionPreview[key];
  }
  return [...versions].reverse().find((version) => version.status === "final")
    || [...versions].reverse().find((version) => version.status === "current")
    || versions[versions.length - 1];
}

function cardVersionPreviewKeyFromControl(control) {
  const { target } = cardVersionTargetFromButton(control);
  return cardVersionPreviewKey(target);
}

function selectCardVersionPreview(control, { openLightbox = false } = {}) {
  const path = control?.dataset?.versionPath || "";
  const versionId = control?.dataset?.versionId || "";
  if (!path) return;
  if (openLightbox) {
    openCardVersionImagePreview(path, versionId);
    return;
  }
  const key = cardVersionPreviewKeyFromControl(control);
  if (!key) {
    openCardVersionImagePreview(path, versionId);
    return;
  }
  state.cardVersionPreview[key] = path;
  if (control.closest(".external-retouch-card")) {
    const board = collectExternalRetouchBoardFromDom();
    setIdeaBoardLocal(board);
    renderExternalRetouchLab();
  } else {
    const board = collectIdeaBoardFromDom();
    setIdeaBoardLocal(board);
    renderIdeaLab();
  }
}

let pendingCardVersionThumbClick = null;

function handleCardVersionPreviewClick(event) {
  event.preventDefault();
  const link = event.currentTarget;
  if (link.classList.contains("card-version-thumb-link")) {
    const path = link.dataset.versionPath || "";
    if (pendingCardVersionThumbClick?.path === path) {
      clearTimeout(pendingCardVersionThumbClick.timer);
      pendingCardVersionThumbClick = null;
      selectCardVersionPreview(link, { openLightbox: true });
      return;
    }
    if (pendingCardVersionThumbClick?.timer) {
      clearTimeout(pendingCardVersionThumbClick.timer);
    }
    pendingCardVersionThumbClick = {
      path,
      timer: window.setTimeout(() => {
        pendingCardVersionThumbClick = null;
        selectCardVersionPreview(link);
      }, 180),
    };
    return;
  }
  openCardVersionImagePreview(link.dataset.versionPath || "", link.dataset.versionId || "");
}

function renderCardVersionPreview(cardOrRow, label = "版本 / Versions") {
  const versions = cardVersionEntries(cardOrRow);
  if (!versions.length) {
    return `<div class="card-version-empty">暂无图片版本 / No image versions yet.</div>`;
  }
  const current = preferredCardVersion(cardOrRow, versions);
  const previewKey = cardVersionPreviewKey(cardOrRow);
  const statusLabel = (status) => CARD_VERSION_STATUS_LABELS[status || "candidate"] || CARD_VERSION_STATUS_LABELS.candidate;
  const statusClass = (status) => (["final", "current", "reference", "rejected", "candidate"].includes(status) ? status : "candidate");
  const actionStateAttrs = (version, status) => {
    const active = version.status === status;
    return `class="mini-command card-version-status${active ? " active" : ""}" aria-pressed="${active ? "true" : "false"}"`;
  };
  const versionLabel = (version) => [version.version_id || "current", version.candidate_id || ""].filter(Boolean).join(" · ");
  const versionDownloadLink = (version, labelText = "下载") => {
    const path = version.output_path || "";
    const url = sceneAssetUrl(path);
    if (!path || !url) return "";
    return `<a class="mini-command card-version-download" ${downloadImageAttrs(url, path, version.version_id || path)} title="下载这张图片 / Download this image">${escapeHtml(labelText)}</a>`;
  };
  const qaBadge = (version) => {
    const score = version.qa?.score;
    if (score === undefined || score === null || score === "") return `<span class="card-version-qa muted">未质检</span>`;
    return `<span class="card-version-qa ${scoreClass(Number(score))}">技术分 ${escapeHtml(score)}</span>`;
  };
  const currentUrl = sceneAssetUrl(current.output_path || "");
  return `
    <div class="card-version-panel" data-card-version-key="${escapeHtml(previewKey)}">
      <div class="card-version-hero">
        <a class="card-version-preview-link card-version-hero-link" href="${escapeHtml(currentUrl)}" target="_blank" title="点击预览大图 / Click to preview full image" data-version-id="${escapeHtml(current.version_id || "current")}" data-version-path="${escapeHtml(current.output_path || "")}" ${externalImageDragAttrs(currentUrl, current.output_path || "", current.version_id || "current", { draggable: false })}>
          <img src="${escapeHtml(currentUrl)}" alt="${escapeHtml(current.version_id || "current")}" loading="lazy" ${externalImageDragAttrs(currentUrl, current.output_path || "", current.version_id || "current")} />
        </a>
      </div>
      <div class="card-version-summary">
        <div class="card-version-meta">
          <strong>${escapeHtml(label)}</strong>
          <span>${escapeHtml(versionLabel(current))} · ${escapeHtml(current.created_at || "")}</span>
          <div class="card-version-badges">
            <span class="card-version-state ${escapeHtml(statusClass(current.status))}">${escapeHtml(statusLabel(current.status))}</span>
            ${qaBadge(current)}
          </div>
          <small>${escapeHtml(current.notes || current.output_path || "")}</small>
        </div>
        <div class="card-version-actions">
          <button class="mini-command card-version-qa-run" data-help="对这张版本图做技术评分，检查清晰度、噪点、曝光和对比。" data-version-id="${escapeHtml(current.version_id || "")}" data-version-path="${escapeHtml(current.output_path || "")}" type="button">质检 / QA</button>
          <button class="mini-command card-version-to-board" data-help="把这张图送入画板，用主图/关联图/备注方式继续精修。" data-version-path="${escapeHtml(current.output_path || "")}" type="button">画板精修 / Board refine</button>
          ${versionDownloadLink(current, "下载 / Download")}
        </div>
      </div>
      <div class="card-version-strip">
        ${versions
          .map(
            (version) => {
              const previewing = version.output_path === current.output_path;
              return `
              <div class="card-version-thumb ${escapeHtml(statusClass(version.status))}${previewing ? " previewing" : ""}" title="${escapeHtml(version.notes || version.output_path || "")}">
                <a class="card-version-preview-link card-version-thumb-link" href="${escapeHtml(sceneAssetUrl(version.output_path || ""))}" target="_blank" title="单击切换上方预览，双击打开大图 / Click to preview above, double-click to enlarge" data-version-id="${escapeHtml(version.version_id || "version")}" data-version-path="${escapeHtml(version.output_path || "")}" ${externalImageDragAttrs(sceneAssetUrl(version.output_path || ""), version.output_path || "", version.version_id || "version", { draggable: false })}>
                  <img src="${escapeHtml(sceneAssetUrl(version.output_path || ""))}" alt="${escapeHtml(version.version_id || "version")}" loading="lazy" ${externalImageDragAttrs(sceneAssetUrl(version.output_path || ""), version.output_path || "", version.version_id || "version")} />
                  <span>${escapeHtml(versionLabel(version))}</span>
                </a>
                ${previewing ? `<small class="card-version-preview-state">预览中 / Preview</small>` : ""}
                <small class="card-version-state ${escapeHtml(statusClass(version.status))}">${escapeHtml(statusLabel(version.status))}</small>
                ${qaBadge(version)}
                <div class="card-version-mini-actions">
                  <button ${actionStateAttrs(version, "final")} data-help="标记为最终分镜图；只有 Final 图会进入下方最终分镜 preview。" data-version-id="${escapeHtml(version.version_id || "")}" data-version-path="${escapeHtml(version.output_path || "")}" data-version-status="final" type="button">Final</button>
                  <button ${actionStateAttrs(version, "current")} data-help="设为当前采用候选；不会进入最终分镜 preview，除非再标记 Final。" data-version-id="${escapeHtml(version.version_id || "")}" data-version-path="${escapeHtml(version.output_path || "")}" data-version-status="current" type="button">采用</button>
                  <button ${actionStateAttrs(version, "reference")} data-help="保留为参考图；不会进入最终大图预览，但可在画板和参考包里使用。" data-version-id="${escapeHtml(version.version_id || "")}" data-version-path="${escapeHtml(version.output_path || "")}" data-version-status="reference" type="button">参考</button>
                  <button ${actionStateAttrs(version, "rejected")} data-help="标记为不用；它会离开最终预览，留在待定/废图管理逻辑里。" data-version-id="${escapeHtml(version.version_id || "")}" data-version-path="${escapeHtml(version.output_path || "")}" data-version-status="rejected" type="button">淘汰</button>
                  <button class="mini-command card-version-qa-run" data-help="对这张版本图做技术评分。" data-version-id="${escapeHtml(version.version_id || "")}" data-version-path="${escapeHtml(version.output_path || "")}" type="button">质检</button>
                  <button class="mini-command card-version-to-board" data-help="送入画板继续单图精修。" data-version-path="${escapeHtml(version.output_path || "")}" type="button">画板</button>
                  ${versionDownloadLink(version)}
                </div>
              </div>
            `;
            },
          )
          .join("")}
      </div>
    </div>
  `;
}

function openCardVersionImagePreview(path, name = "") {
  const cleanPath = String(path || "").trim();
  const url = sceneAssetUrl(cleanPath);
  if (!cleanPath || !url) {
    toast("这张版本图还没有路径 / This version has no image path");
    return;
  }
  showBoardImageLightbox({
    url,
    path: cleanPath,
    asset_id: name || imageFileNameFromPath(cleanPath),
  });
}

function fileIsImage(file) {
  return Boolean(file?.type?.startsWith("image/") || /\.(png|jpe?g|webp|gif)$/i.test(file?.name || ""));
}

function readFileAsDataUrl(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => resolve(String(reader.result || ""));
    reader.onerror = () => reject(reader.error || new Error("File read failed"));
    reader.readAsDataURL(file);
  });
}

async function uploadDroppedStoryboardVersion(rowElement, file) {
  if (!state.selectedSlug || !rowElement || !fileIsImage(file)) {
    toast("只能拖入图片文件 / Drop an image file");
    return;
  }
  const index = Number(rowElement.dataset.ideaIndex || 0);
  const board = collectIdeaBoardFromDom();
  const row = board.rows?.[index];
  if (!row?.item_id) {
    toast("没有找到这张分镜卡 / Storyboard card not found");
    return;
  }
  setIdeaBoardLocal(board);
  const dataUrl = await readFileAsDataUrl(file);
  const payload = await requestJson(`/api/projects/${encodeURIComponent(state.selectedSlug)}/card-version-upload`, {
    method: "POST",
    body: JSON.stringify({
      card_type: "storyboard",
      item_id: row.item_id,
      card_uid: row.card_uid || "",
      file_name: file.name || "dropped-image.png",
      mime_type: file.type || "",
      data_url: dataUrl,
      notes: `外部拖拽导入备选图 / External drop candidate: ${file.name || "image"}`,
    }),
  });
  state.detail = payload.project || state.detail;
  renderIdeaLab();
  toast("已放入这张分镜卡的备选区 / Added to this card's candidates");
}

function sendVersionImageToBoard(path) {
  const cleanPath = String(path || "").trim();
  if (!cleanPath) {
    toast("这张版本图还没有路径 / This version has no image path");
    return;
  }
  const asset = allBoardImageAssets().find(
    (item) => item.path === cleanPath || item.ref === cleanPath || item.ref === `project:${cleanPath}` || item.ref === `resource:${cleanPath}`,
  );
  if (!asset) {
    toast("当前资源库还没扫描到这张图，请刷新后再送入画板 / Refresh before sending this image to the board");
    return;
  }
  state.boardOpen = true;
  const existing = state.boardNodes.find((node) => node.assetRef === asset.ref);
  if (!existing) {
    addBoardNode(asset.ref, boardDefaultNodePoint());
    toast("已送入画板精修 / Sent to board refinement");
    return;
  }
  renderReferenceBoard();
  toast("这张图已在画板中 / Image is already on the board");
}

function normalizeCardVersionsForEdit(cardOrRow) {
  return (Array.isArray(cardOrRow?.versions) ? cardOrRow.versions : [])
    .filter((version) => version?.output_path)
    .map((version, index) => ({
      version_id: version.version_id || `v${String(index + 1).padStart(3, "0")}`,
      output_path: version.output_path || "",
      notes: version.notes || "",
      created_at: version.created_at || "",
      status: version.status || (version.output_path === (cardOrRow.preview_path || cardOrRow.output_path || "") ? "current" : "candidate"),
      candidate_id: version.candidate_id || "",
      task_id: version.task_id || "",
      packet_id: version.packet_id || "",
      video_prompt: version.video_prompt || "",
      image_analysis: version.image_analysis || "",
      qa: version.qa && typeof version.qa === "object" ? version.qa : {},
    }));
}

function findOrCreateCardVersion(cardOrRow, versionId, versionPath) {
  const versions = normalizeCardVersionsForEdit(cardOrRow);
  let target = versions.find((version) => version.version_id === versionId && version.output_path === versionPath)
    || versions.find((version) => version.output_path === versionPath)
    || versions.find((version) => version.version_id === versionId);
  if (!target && versionPath) {
    target = {
      version_id: versionId || `v${String(versions.length + 1).padStart(3, "0")}`,
      output_path: versionPath,
      notes: "",
      created_at: "",
      status: "candidate",
      candidate_id: "",
      task_id: "",
      packet_id: "",
      video_prompt: "",
      image_analysis: "",
      qa: {},
    };
    versions.push(target);
  }
  cardOrRow.versions = versions;
  return target || null;
}

function applyVersionStatusToCard(cardOrRow, versionId, versionPath, nextStatus, cardType) {
  const target = findOrCreateCardVersion(cardOrRow, versionId, versionPath);
  const versions = cardOrRow.versions || [];
  if (!target) return false;
  if (nextStatus === "final") {
    versions.forEach((version) => {
      if (version.status === "final") version.status = "candidate";
    });
    target.status = "final";
  } else if (nextStatus === "current") {
    versions.forEach((version) => {
      if (version.status === "current") version.status = "candidate";
    });
    target.status = "current";
  } else {
    target.status = nextStatus;
  }
  const currentPath = cardType === "concept" ? cardOrRow.preview_path : cardOrRow.output_path;
  if (["reference", "rejected"].includes(nextStatus) && target.output_path === currentPath) {
    const fallback = [...versions].reverse().find((version) => version.output_path !== target.output_path && version.status !== "rejected");
    if (fallback) {
      versions.forEach((version) => {
        if (version.status === "current") version.status = "candidate";
      });
      fallback.status = "current";
      if (cardType === "concept") {
        cardOrRow.preview_path = fallback.output_path;
      } else {
        cardOrRow.output_path = fallback.output_path;
        cardOrRow.output_notes = fallback.notes || "";
        cardOrRow.output_attached_at = fallback.created_at || cardOrRow.output_attached_at || "";
      }
    } else if (cardType === "concept") {
      cardOrRow.preview_path = "";
    } else {
      cardOrRow.output_path = "";
      cardOrRow.output_notes = "";
    }
  } else if (nextStatus === "current" || nextStatus === "final") {
    if (cardType === "concept") {
      cardOrRow.preview_path = target.output_path;
      cardOrRow.status = "image_ready";
    } else {
      cardOrRow.output_path = target.output_path;
      cardOrRow.output_notes = target.notes || "";
      cardOrRow.output_attached_at = target.created_at || cardOrRow.output_attached_at || "";
      cardOrRow.status = "image_ready";
    }
  }
  cardOrRow.versions = versions;
  return true;
}

function cardVersionTargetFromButton(button) {
  const board = collectExternalRetouchBoardFromDom(collectIdeaBoardFromDom());
  const bibleCard = button.closest(".project-bible-card");
  const shotRow = button.closest(".idea-shot-row");
  const externalCard = button.closest(".external-retouch-card");
  if (bibleCard) {
    const index = Number(bibleCard.dataset.bibleIndex || state.ideaActiveBibleIndex || 0);
    return { board, cardType: "concept", target: board.project_bible?.[index] || null };
  }
  if (shotRow) {
    const index = Number(shotRow.dataset.ideaIndex || state.ideaActiveRowIndex || 0);
    return { board, cardType: "storyboard", target: board.rows?.[index] || null };
  }
  if (externalCard) {
    const index = Number(externalCard.dataset.ideaIndex || 0);
    return { board, cardType: "storyboard", target: board.rows?.[index] || null };
  }
  return { board, cardType: "", target: null };
}

async function updateCardVersionStatus(button) {
  if (!button) return;
  const status = button.dataset.versionStatus || "candidate";
  const versionId = button.dataset.versionId || "";
  const versionPath = button.dataset.versionPath || "";
  const { board, cardType, target } = cardVersionTargetFromButton(button);
  if (!target || !applyVersionStatusToCard(target, versionId, versionPath, status, cardType)) {
    toast("没有找到这个版本 / Version not found");
    return;
  }
  const previewKey = cardVersionPreviewKey(target);
  if (previewKey && versionPath) state.cardVersionPreview[previewKey] = versionPath;
  await runAction("更新版本状态 / Update version status", async () => {
    const result = await persistIdeaBoard(board, { toast: false, render: false });
    setIdeaBoardLocal(result?.idea_board || board);
    if (button.closest(".external-retouch-card")) renderAll();
    else renderIdeaLab();
    toast(`版本已标记为 ${CARD_VERSION_STATUS_LABELS[status] || status}`);
  });
}

function analyzeImageUrl(url) {
  return new Promise((resolve, reject) => {
    const img = new Image();
    img.onload = () => {
      try {
        resolve(analyzeImageElement(img));
      } catch (error) {
        reject(error);
      }
    };
    img.onerror = () => reject(new Error("图片无法载入 / Image failed to load"));
    img.src = url;
  });
}

async function runCardVersionQa(button) {
  if (!button) return;
  const versionId = button.dataset.versionId || "";
  const versionPath = button.dataset.versionPath || "";
  const { board, target } = cardVersionTargetFromButton(button);
  const version = target ? findOrCreateCardVersion(target, versionId, versionPath) : null;
  if (!target || !version?.output_path) {
    toast("没有找到这个版本 / Version not found");
    return;
  }
  await runAction("卡片版本质检 / Card version QA", async () => {
    const result = await analyzeImageUrl(sceneAssetUrl(version.output_path));
    version.qa = {
      ...result,
      analyzed_at: new Date().toISOString(),
    };
    const saved = await persistIdeaBoard(board, { toast: false, render: false });
    setIdeaBoardLocal(saved?.idea_board || board);
    if (button.closest(".external-retouch-card")) renderAll();
    else renderIdeaLab();
    toast(`技术分 ${result.score} / QA score ${result.score}`);
  });
}

function currentVersionForQa(cardOrRow) {
  const versions = cardVersionEntries(cardOrRow);
  if (!versions.length) return null;
  return [...versions].reverse().find((version) => version.status === "final")
    || [...versions].reverse().find((version) => version.status === "current")
    || [...versions].reverse().find((version) => version.status !== "rejected")
    || versions[versions.length - 1];
}

function cardSelectedForGeneration(card, cardType) {
  return cardType === "concept" ? card.image_selected !== false : card.selected !== false;
}

function cardQaBucket(card) {
  const version = currentVersionForQa(card);
  if (!version?.output_path) return "no_image";
  const rawScore = version.qa?.score;
  const score = Number(rawScore);
  if (rawScore === undefined || rawScore === null || rawScore === "" || !Number.isFinite(score)) return "qa_unscored";
  if (score >= 82) return "qa_ok";
  if (score >= 68) return "qa_warn";
  return "qa_risk";
}

function sceneForIdeaRow(row) {
  const scenes = state.detail?.scene_workbench?.scenes || [];
  return scenes.find((scene) => scene.scene_id === row?.scene_id) || {};
}

function cardFilterAsset(card, cardType, board = currentIdeaBoard(), index = 0) {
  if (cardType === "concept") {
    const actLabel = card.act_id ? projectBibleActLabel(board, card.act_id) : "";
    return {
      ref: `card:concept:${card.card_id || index}`,
      asset_id: card.card_id || `BIBLE_${index + 1}`,
      role: card.title || card.summary || card.card_id || "Concept card",
      path: card.preview_path || "",
      kind: projectBibleCategoryKind(card.category || ""),
      stage: "08_generation",
      scene_id: "",
      scene_title: "设定 / Settings",
      act_id: card.act_id || "",
      act_title: actLabel,
      card_type: "concept",
      card_id: card.card_id || "",
      card_scope: card.scope || "project",
      card_act_id: card.act_id || "",
      card_act_title: actLabel,
      card_title: card.title || "",
      card_category: card.category || "",
      card_summary: card.summary || "",
      card_prompt: [card.visual_direction, card.prompt_notes, card.revision_note, card.negative_prompt].filter(Boolean).join(" "),
    };
  }
  const scene = sceneForIdeaRow(card);
  const rowActId = card.act_id || scene.act_id || "";
  const rowActTitle = card.act_id ? projectBibleActLabel(board, card.act_id) : scene.act_title || "";
  return {
    ref: `card:storyboard:${card.item_id || index}`,
    asset_id: card.item_id || `IDEA_SHOT_${index + 1}`,
    role: card.beat || card.frame_description || card.item_id || "Storyboard card",
    path: card.output_path || "",
    kind: "storyboard_keyframe",
    stage: "08_generation",
    scene_id: card.scene_id || "",
    scene_title: scene.title || "",
    act_id: rowActId,
    act_title: rowActTitle,
    shot_id: card.item_id || "",
    card_type: "storyboard",
    card_id: card.item_id || "",
    card_scope: rowActId ? "act" : "scene",
    card_act_id: rowActId,
    card_act_title: rowActTitle,
    card_title: card.beat || card.item_id || "",
    card_category: "storyboard",
    card_summary: card.frame_description || "",
    card_prompt: [storyboardLinkValue(card.linked_cards || []), card.spatial_logic, card.image_prompt, card.video_prompt, card.revision_note, card.notes].filter(Boolean).join(" "),
  };
}

function cardFilterTags(card, cardType, board = currentIdeaBoard(), index = 0) {
  const baseAsset = cardFilterAsset(card, cardType, board, index);
  const tags = new Set(
    boardAssetTags(baseAsset).filter((tag) => !tag.startsWith("version_") && !tag.startsWith("qa_")),
  );
  cardVersionEntries(card).forEach((version) => {
    boardAssetTags({
      ...baseAsset,
      ref: `${baseAsset.ref}:${version.version_id || version.output_path || "version"}`,
      path: version.output_path || baseAsset.path,
      version_id: version.version_id || "",
      version_status: version.status || "candidate",
      qa_score: version.qa?.score ?? null,
    }).forEach((tag) => tags.add(tag));
  });
  return [...tags];
}

function cardFilterAssets(board = currentIdeaBoard(), cardType = "storyboard") {
  const cards = cardType === "concept" ? board.project_bible || [] : board.rows || [];
  return cards.map((card, index) => {
    const asset = cardFilterAsset(card, cardType, board, index);
    return {
      ...asset,
      tags: cardFilterTags(card, cardType, board, index),
    };
  });
}

function defaultCardFilterScope(cardType) {
  if (cardType === "concept") return "all";
  return isIdeaActSelected() ? "current_act" : "current_scene";
}

function effectiveCardFilterScope(cardType, board = currentIdeaBoard()) {
  const fallback = defaultCardFilterScope(cardType);
  const raw = state.cardFilters?.scope || fallback;
  const options = imageLibraryScopeOptions(cardFilterAssets(board, cardType));
  if (options.some((option) => option.value === raw)) return raw;
  if (options.some((option) => option.value === fallback)) return fallback;
  return "all";
}

function normalizedCardFilters(cardType, board = currentIdeaBoard()) {
  return {
    scope: effectiveCardFilterScope(cardType, board),
    tag: state.cardFilters?.tag || "all",
    mode: state.cardFilters?.mode || "all",
    query: state.cardFilters?.query || "",
  };
}

function cardMatchesCardScope(card, cardType, board = currentIdeaBoard(), index = 0) {
  const filters = normalizedCardFilters(cardType, board);
  return imageAssetMatchesScope(cardFilterAsset(card, cardType, board, index), filters.scope);
}

function cardMatchesCardFilters(card, cardType, board = currentIdeaBoard(), index = 0) {
  const filters = normalizedCardFilters(cardType, board);
  const mode = filters.mode || "all";
  const versions = cardVersionEntries(card);
  const hasImage = versions.length > 0;
  const selected = cardSelectedForGeneration(card, cardType);
  if (!imageAssetMatchesScope(cardFilterAsset(card, cardType, board, index), filters.scope)) return false;
  const tag = filters.tag || "all";
  if (tag !== "all" && !cardFilterTags(card, cardType, board, index).includes(tag)) return false;
  if (mode === "selected" && !selected) return false;
  if (mode === "unselected" && selected) return false;
  if (mode === "no_image" && hasImage) return false;
  if (mode === "has_image" && !hasImage) return false;
  if (["current", "final", "reference", "candidate", "rejected"].includes(mode) && !versions.some((version) => version.status === mode)) return false;
  if (mode.startsWith("qa_") && cardQaBucket(card) !== mode) return false;
  const query = String(filters.query || "").trim().toLowerCase();
  if (!query) return true;
  const scopeSearchFields = cardType === "concept"
    ? [card.scope, card.act_id, projectBibleScopeLabel(card.scope), projectBibleActLabel(currentIdeaBoard(), card.act_id)]
    : [card.act_id, projectBibleActLabel(currentIdeaBoard(), card.act_id)];
  return [
    card.card_id,
    card.item_id,
    ...scopeSearchFields,
    card.title,
    card.category,
    card.summary,
    card.visual_direction,
    card.prompt_notes,
    card.negative_prompt,
    card.beat,
    card.act_id,
    card.scene_id,
    card.shot_type,
    card.frame_description,
    storyboardLinkValue(card.linked_cards || []),
    card.spatial_logic,
    card.image_prompt,
    card.video_prompt,
    card.notes,
    card.revision_note,
    card.status,
    ...(card.references || []).flatMap((ref) => [ref.asset_id, ref.path, ref.kind, ref.note]),
    ...versions.flatMap((version) => [version.version_id, version.status, version.notes, version.output_path, version.qa?.score]),
  ]
    .join(" ")
    .toLowerCase()
    .includes(query);
}

function cardScopeOptions(board = currentIdeaBoard(), cardType = "storyboard") {
  const allLabel = cardType === "concept" ? "全部概念卡 / All concept cards" : "全部分镜卡 / All storyboard cards";
  return imageLibraryScopeOptions(cardFilterAssets(board, cardType)).map((option) => (
    option.value === "all" ? { ...option, label: option.label.replace(/^全部图片 \/ All images/, allLabel) } : option
  ));
}

function cardTagOptions() {
  return BOARD_TAG_OPTIONS.map((option) => (
    option.value === "all" ? { ...option, label: "全部类别 / All types" } : option
  ));
}

function filteredProjectBibleEntries(board = currentIdeaBoard()) {
  return (board.project_bible || [])
    .map((card, index) => ({ card, index }))
    .filter(({ card, index }) => cardMatchesCardFilters(card, "concept", board, index));
}

function projectBibleEntriesForCardScope(board = currentIdeaBoard()) {
  return (board.project_bible || [])
    .map((card, index) => ({ card, index }))
    .filter(({ card, index }) => cardMatchesCardScope(card, "concept", board, index));
}

// These two filter the full row list and are called ~10x per render with identical
// inputs (renderIdeaLab, filter-count controls, active-row bookkeeping, etc.). Each
// row match is expensive, so memoize per render. Inputs: board content (wrapper
// identity, replaced on every edit) + the card filter state + selected scene.
let _ideaScopeEntries = { board: null, key: "", value: null };
let _ideaFilterEntries = { board: null, key: "", value: null };

function ideaRowEntriesCacheKey() {
  const f = state.cardFilters || {};
  return `${state.selectedSlug || ""}|${state.selectedSceneId || ""}|${f.scope || ""}|${f.tag || "all"}|${f.mode || "all"}|${f.query || ""}`;
}

function ideaRowEntriesForCardScope(board = currentIdeaBoard()) {
  const key = ideaRowEntriesCacheKey();
  if (_ideaScopeEntries.value && _ideaScopeEntries.board === board && _ideaScopeEntries.key === key) {
    return _ideaScopeEntries.value;
  }
  const value = (board.rows || [])
    .map((row, index) => ({ row, index }))
    .filter(({ row, index }) => cardMatchesCardScope(row, "storyboard", board, index));
  _ideaScopeEntries = { board, key, value };
  return value;
}

function filteredIdeaRowEntriesForCurrentScene(board = currentIdeaBoard()) {
  const key = ideaRowEntriesCacheKey();
  if (_ideaFilterEntries.value && _ideaFilterEntries.board === board && _ideaFilterEntries.key === key) {
    return _ideaFilterEntries.value;
  }
  const value = ideaRowEntriesForCardScope(board).filter(({ row, index }) => cardMatchesCardFilters(row, "storyboard", board, index));
  _ideaFilterEntries = { board, key, value };
  return value;
}

function renderCardFilterControls(total, visible, cardType, board = currentIdeaBoard()) {
  const filters = normalizedCardFilters(cardType, board);
  const scopeOptions = cardScopeOptions(board, cardType);
  return `
    <div class="card-filter-controls">
      <select id="cardFilterScope">
        ${scopeOptions.map((option) => `<option value="${escapeHtml(option.value)}" ${filters.scope === option.value ? "selected" : ""}>${escapeHtml(option.label)}</option>`).join("")}
      </select>
      <select id="cardFilterTag">
        ${cardTagOptions().map((option) => `<option value="${escapeHtml(option.value)}" ${filters.tag === option.value ? "selected" : ""}>${escapeHtml(option.label)}</option>`).join("")}
      </select>
      <select id="cardFilterMode">
        ${CARD_FILTER_OPTIONS.map((option) => `<option value="${escapeHtml(option.value)}" ${(filters.mode || "all") === option.value ? "selected" : ""}>${escapeHtml(option.label)}</option>`).join("")}
      </select>
      <input id="cardFilterQuery" value="${escapeHtml(filters.query || "")}" placeholder="搜索卡片、提示词、版本 / Search cards" />
      <button id="cardFilterClearBtn" class="mini-command" type="button">清除 / Clear</button>
      <span>${visible}/${total}</span>
    </div>
  `;
}

function visibleCardsForBatchQa(board) {
  if (isProjectBibleSelected()) {
    return filteredProjectBibleEntries(board).map(({ card }) => ({ cardType: "concept", target: card }));
  }
  return filteredIdeaRowEntriesForCurrentScene(board).map(({ row }) => ({ cardType: "storyboard", target: row }));
}

async function runVisibleCardVersionQa() {
  if (!state.selectedSlug || !state.detail) return;
  await runAction("批量质检当前卡片 / Batch QA", async () => {
    const board = collectIdeaBoardFromDom();
    const targets = visibleCardsForBatchQa(board)
      .map((item) => ({ ...item, version: currentVersionForQa(item.target) }))
      .filter((item) => item.version?.output_path);
    if (!targets.length) {
      toast("当前没有可质检的图片版本 / No visible image versions to QA");
      return;
    }
    let passed = 0;
    let failed = 0;
    for (const item of targets) {
      const version = findOrCreateCardVersion(item.target, item.version.version_id || "", item.version.output_path || "");
      if (!version?.output_path) {
        failed += 1;
        continue;
      }
      try {
        const result = await analyzeImageUrl(sceneAssetUrl(version.output_path));
        version.qa = {
          ...result,
          analyzed_at: new Date().toISOString(),
        };
        passed += 1;
      } catch {
        failed += 1;
      }
    }
    const saved = await persistIdeaBoard(board, { toast: false, render: false });
    setIdeaBoardLocal(saved?.idea_board || board);
    renderIdeaLab();
    toast(`批量质检完成 / Batch QA done: ${passed} 成功, ${failed} 失败`);
  });
}

function renderProjectBibleReferencePanel(board) {
  const cards = board.project_bible || [];
  ensureProjectBibleActiveForFilteredCards(board);
  const card = activeProjectBibleCard(board);
  const globalRefs = board.global_references || [];
  const cardRefs = card?.references || [];
  const filters = currentImageLibraryFilters(allBoardImageAssets().filter((asset) => frameIsUsable(asset)));
  return `
    <details class="idea-reference-panel project-bible-reference-panel" open>
      <summary>
        <span>设定参考库 / Settings References</span>
        <small>${globalRefs.length} 全局 · ${cardRefs.length} 当前卡</small>
      </summary>
      <div class="idea-reference-content">
        <div class="idea-reference-controls">
          <select id="ideaRefActFilter">
            ${ideaReferenceActOptions().map((option) => `<option value="${escapeHtml(option.value)}" ${filters.scope === option.value ? "selected" : ""}>${escapeHtml(option.label)}</option>`).join("")}
          </select>
          <select id="ideaRefTagFilter">
            ${BOARD_TAG_OPTIONS.map((option) => `<option value="${escapeHtml(option.value)}" ${filters.tag === option.value ? "selected" : ""}>${escapeHtml(option.label)}</option>`).join("")}
          </select>
          <input id="ideaRefSearchInput" value="${escapeHtml(filters.query || "")}" placeholder="搜索人设、场景、道具、美术 / Search bible refs" />
        </div>
        <section class="idea-ref-section">
          <strong>全局参考 / Global</strong>
          <div class="idea-ref-list">${globalRefs.length ? globalRefs.map((ref) => renderIdeaReferenceEditor(ref, "global")).join("") : `<span class="muted-inline">所有幕默认继承的人设、场景、道具和风格参考。</span>`}</div>
        </section>
        <section class="idea-ref-section">
          <strong>当前卡 / Current: ${escapeHtml(card?.title || card?.card_id || "无")}</strong>
          <div class="idea-ref-list">${cardRefs.length ? cardRefs.map((ref) => renderIdeaReferenceEditor(ref, "bible")).join("") : `<span class="muted-inline">只影响当前设定卡。</span>`}</div>
        </section>
        <div class="idea-ref-asset-grid">
          ${renderIdeaReferenceAssetGrid(card)}
        </div>
        <div class="project-bible-mini-map">
          ${cards.length
            ? cards
                .map(
                  (item, index) => `
                    <button class="project-bible-map-item ${state.ideaActiveBibleIndex === index ? "active" : ""}" data-bible-index="${index}" type="button">
                      <span>${escapeHtml(projectBibleCategoryLabel(item.category))}</span>
                      <strong>${escapeHtml(item.title || item.card_id || `#${index + 1}`)}</strong>
                      <small>${escapeHtml(projectBibleScopeLabel(item.scope))}${item.act_id ? ` · ${escapeHtml(projectBibleActLabel(board, item.act_id))}` : ""} · ${(item.references || []).length} refs</small>
                    </button>
                  `,
                )
                .join("")
            : `<div class="empty-state">还没有设定卡 / No settings cards yet.</div>`}
        </div>
      </div>
    </details>
  `;
}

function renderProjectBibleCards(board, entries = filteredProjectBibleEntries(board)) {
  const cards = board.project_bible || [];
  if (!cards.length) {
    return `<div class="empty-state">还没有设定卡。建议先新增人物、场景、道具、美术或氛围卡，再绑定参考图。</div>`;
  }
  if (!entries.length) {
    return `<div class="empty-state">没有匹配的设定卡 / No matching settings cards.</div>`;
  }
  return entries
    .map(
      ({ card, index }) => `
        <article class="project-bible-card ${state.ideaActiveBibleIndex === index ? "active" : ""}" data-bible-index="${index}">
          <header>
            <label>编号 / ID <input data-bible-field="card_id" value="${escapeHtml(card.card_id || `BIBLE_${String(index + 1).padStart(3, "0")}`)}" /></label>
            <label>层级 / Scope
              <select data-bible-field="scope">
                ${renderProjectBibleScopeOptions(card.scope || "project")}
              </select>
            </label>
            <label>所属幕 / Act
              <select data-bible-field="act_id">
                ${renderProjectBibleActOptions(board, card.act_id || "")}
              </select>
            </label>
            <label>分类 / Type
              <select data-bible-field="category">
                ${PROJECT_BIBLE_CATEGORY_OPTIONS.map((option) => `<option value="${escapeHtml(option.value)}" ${card.category === option.value ? "selected" : ""}>${escapeHtml(option.label)}</option>`).join("")}
              </select>
            </label>
            <label>标题 / Title <input data-bible-field="title" value="${escapeHtml(card.title || "")}" /></label>
            <label class="checkbox-label"><input data-bible-field="selected" type="checkbox" ${card.selected === false ? "" : "checked"} /> 启用 / Use</label>
            <label class="checkbox-label"><input data-bible-field="image_selected" type="checkbox" ${card.image_selected === false ? "" : "checked"} /> 本次生成</label>
            <button class="mini-command project-bible-focus ${state.ideaActiveBibleIndex === index ? "active" : ""}" data-help="把这张概念卡设为当前参考绑定目标，图库拖入的图片会挂到它身上。" data-bible-index="${index}" type="button">参考 / Refs</button>
            <button class="mini-command card-generate-one" data-help="只为这一张概念卡生成图片包，适合单独精修人物、场景或道具。" data-card-type="concept" data-card-id="${escapeHtml(card.card_id || "")}" type="button">只生成此卡</button>
            <button class="icon-button project-bible-delete" data-bible-index="${index}" type="button" title="删除设定卡 / Delete card">×</button>
          </header>
          <div class="idea-row-ref-strip">
            <span>${(card.references || []).length} 当前参考 / refs · ${escapeHtml(projectBibleScopeLabel(card.scope))}${card.act_id ? ` · ${escapeHtml(projectBibleActLabel(board, card.act_id))}` : ""} · ${escapeHtml(projectBibleCategoryLabel(card.category))}</span>
            ${(card.references || []).slice(0, 8).map((ref) => renderIdeaReferenceChip(ref, "bible", index)).join("")}
          </div>
          ${renderCardVersionPreview(card, "概念图版本 / Concept image versions")}
          <label>概念说明 / Summary
            <textarea data-bible-field="summary" rows="3">${escapeHtml(card.summary || "")}</textarea>
          </label>
          <label>视觉方向 / Visual direction
            <textarea data-bible-field="visual_direction" rows="3">${escapeHtml(card.visual_direction || "")}</textarea>
          </label>
          <label>提示词要点 / Prompt notes
            <textarea data-bible-field="prompt_notes" rows="3">${escapeHtml(card.prompt_notes || "")}</textarea>
          </label>
          <label>本次修图意见 / Revision note
            <textarea data-bible-field="revision_note" rows="2" placeholder="只写这一轮要改什么，例如：保留人物，降低饱和度，改成阴天窗边侧光">${escapeHtml(card.revision_note || "")}</textarea>
          </label>
          <label>负面约束 / Negative prompt
            <textarea data-bible-field="negative_prompt" rows="2">${escapeHtml(card.negative_prompt || "")}</textarea>
          </label>
          <footer>
            <label>状态 / Status <input data-bible-field="status" value="${escapeHtml(card.status || "draft")}" /></label>
          </footer>
        </article>
      `,
    )
    .join("");
}

function renderProjectBibleLab(board) {
  const cardCount = (board.project_bible || []).length;
  const enabledCount = (board.project_bible || []).filter((card) => card.selected !== false).length;
  const scopeEntries = projectBibleEntriesForCardScope(board);
  const visibleEntries = filteredProjectBibleEntries(board);
  ensureProjectBibleActiveForFilteredCards(board);
  return `
    <div class="idea-header">
      <div>
        <p class="eyebrow">Settings</p>
        <h3>设定 / Settings</h3>
        <p>管理全项目人物、场景、道具、美术、氛围和负面约束；所有幕和分镜默认继承这里的设定。</p>
        <ol class="workflow-steps">
          <li><strong>01</strong><span>写全局设定</span></li>
          <li><strong>02</strong><span>生成设定卡</span></li>
          <li><strong>03</strong><span>出图并选采用版本</span></li>
          <li><strong>04</strong><span>进入分镜/画板复用</span></li>
        </ol>
      </div>
      <div class="idea-actions">
        <button id="projectBibleBuildHandoffBtn" class="command-button primary" data-help="把当前设定文字交给 Codex 扩展成人物、场景、道具、美术等设定卡。" type="button">生成设定卡 / Build Settings</button>
        <button id="cardBuildImagePacketBtn" class="command-button" data-help="只把当前范围里勾选的概念卡打包成图片生成任务，不会自动处理未勾选卡。" type="button">生成图片包 / Image Pack</button>
        <button id="currentVersionPackageBtn" class="command-button" data-help="收集当前范围已经标为 Final 或参考的图片，做成后续视频生成参考包。" type="button">Final图包 / Final Pack</button>
        <button id="batchVersionQaBtn" class="command-button" data-help="对当前可见卡片的采用图做技术质检，给出清晰度、噪点、曝光等分数。" type="button">批量质检 / Batch QA</button>
        <button id="qaRepairPacketBtn" class="command-button" data-help="把当前范围里低分或未质检的图片整理成修复生图包。" type="button">低分修复包 / QA Fix</button>
        <button id="cardSelectVisibleBtn" class="command-button" data-help="勾选当前筛选结果里的所有卡片，下一次图片包只处理这些可见卡。" type="button">全选当前 / Select All</button>
        <button id="cardClearVisibleBtn" class="command-button" data-help="取消当前筛选结果里的生成勾选，不删除卡片内容。" type="button">清空当前 / Clear</button>
        <button id="ideaSaveBtn" class="command-button" data-help="手动把当前文字、勾选、参考图和备注保存到项目文件。" type="button">手动保存 / Save now</button>
        <button id="projectBibleAddCardBtn" class="command-button" data-help="新增一张设定卡，用于单独描述人物、场景、道具或风格。" type="button">新增设定卡 / Add Card</button>
      </div>
    </div>
    <div class="idea-layout project-bible-layout">
      <section class="idea-seed-panel">
        <label>项目核心 idea / Core idea
          <textarea id="ideaSeedInput" rows="4">${escapeHtml(board.idea || "")}</textarea>
        </label>
        <div class="idea-meta-grid">
          <label>片名 / Title <input id="ideaStoryTitle" value="${escapeHtml(board.story_title || "")}" /></label>
          <label>一句话 / Logline <input id="ideaLogline" value="${escapeHtml(board.logline || "")}" /></label>
        </div>
        <label>剧本大纲 / Story outline
          <textarea id="ideaOutline" rows="4">${escapeHtml(board.story_outline || "")}</textarea>
        </label>
        <label>全局风格与连续性 / Global style and continuity
          <textarea id="ideaStyleNotes" rows="4">${escapeHtml(board.style_notes || "")}</textarea>
        </label>
        ${renderProjectBibleReferencePanel(board)}
        <div id="ideaHandoffDock" class="idea-handoff-dock">${renderIdeaHandoffs()}</div>
      </section>
      <section class="idea-rows-panel project-bible-panel">
        <div class="idea-rows-header">
          <div class="idea-rows-title">
            <strong>设定卡 / ${enabledCount}/${cardCount} enabled</strong>
            <span>人物、场景、道具、美术、氛围和年代设定；分镜局部备注优先级更高。</span>
          </div>
          ${renderCardFilterControls(scopeEntries.length, visibleEntries.length, "concept", board)}
        </div>
        <div id="projectBibleCardList" class="idea-rows project-bible-cards">${renderProjectBibleCards(board, visibleEntries)}</div>
      </section>
    </div>
  `;
}

function renderIdeaRows(entries, allRows = currentIdeaBoard().rows || []) {
  if (!entries.length) {
    const scene = selectedScene();
    const actId = activeStoryActId();
    const sceneTotal = ideaRowEntriesForCardScope(currentIdeaBoard()).length;
    if (sceneTotal) return `<div class="empty-state">没有匹配的分镜卡片 / No matching storyboard cards.</div>`;
    return `<div class="empty-state">当前范围 ${escapeHtml(actId || scene?.scene_id || "ALL")} 还没有分镜文本。点击“新增条目”会自动创建到当前幕。</div>`;
  }
  const batchSet = ideaBatchRowSet({ rows: allRows });
  return entries
    .map(
      ({ row, index }) => `
        <article class="idea-shot-row ${state.ideaActiveRowIndex === index ? "active" : ""}" data-idea-index="${index}" data-card-uid="${escapeHtml(row.card_uid || "")}">
          <div class="idea-insert-before">
            <button class="idea-insert-row-before" data-help="在这张卡前面插入一张空白分镜卡，并自动关联当前卡；适合在第一帧之前补镜头。" data-idea-index="${index}" type="button" title="在这张卡前面插入一张空白分镜卡，并自动关联当前卡。">＋</button>
          </div>
          <header>
            <label>编号 / ID <input data-idea-field="item_id" value="${escapeHtml(row.item_id || nextIdeaItemId(allRows))}" /></label>
            <label>幕 / Act <input data-idea-field="act_id" value="${escapeHtml(row.act_id || sceneForIdeaRow(row).act_id || "")}" /></label>
            <label>场戏 / Scene <input data-idea-field="scene_id" value="${escapeHtml(row.scene_id || "")}" /></label>
            <label>镜头 / Shot <input data-idea-field="shot_type" value="${escapeHtml(row.shot_type || "")}" /></label>
            <label class="checkbox-label"><input data-idea-field="selected" type="checkbox" ${row.selected === false ? "" : "checked"} /> 本次生成</label>
            <label class="checkbox-label"><input class="idea-batch-check" data-idea-index="${index}" type="checkbox" ${batchSet.has(index) ? "checked" : ""} /> 同步参考</label>
            <button class="mini-command idea-focus-row ${state.ideaActiveRowIndex === index ? "active" : ""}" data-help="把这张分镜设为当前参考绑定目标，下面图库拖入的图片会挂到它身上。" data-idea-index="${index}" type="button">参考 / Refs</button>
            <button class="mini-command card-generate-one" data-help="只为这一张分镜文字卡生成图片包，适合单张精修。" data-card-type="storyboard" data-card-id="${escapeHtml(row.item_id || "")}" type="button">只生成此卡</button>
            <button class="mini-command storyboard-canvas-open" data-help="打开只回填到这张分镜的专属画布；可选择任意主图和多张参考图。" data-idea-index="${index}" type="button">专属画布</button>
            <button class="icon-button idea-delete-row" data-idea-index="${index}" type="button" title="删除条目 / Delete row">×</button>
          </header>
          <div class="idea-row-ref-strip">
            <span>${(row.references || []).length} 当前参考 / refs · ${escapeHtml(row.card_uid || "UID pending")} · 可拖入图片</span>
            ${(row.references || []).slice(0, 6).map((ref) => renderIdeaReferenceChip(ref, "row", index)).join("")}
          </div>
          ${renderCardVersionPreview(row, "分镜图版本 / Storyboard image versions")}
          <label>剧情点 / Beat
            <textarea data-idea-field="beat" rows="2">${escapeHtml(row.beat || "")}</textarea>
          </label>
          <label>画面描述 / Frame description
            <textarea data-idea-field="frame_description" rows="3">${escapeHtml(row.frame_description || "")}</textarea>
          </label>
          <label>关联分镜 / Linked cards
            <input data-idea-field="linked_cards" value="${escapeHtml(storyboardLinkValue(row.linked_cards || []))}" placeholder="例如：ACT1_SHOT_003, MSB058；留空表示无硬关联" />
          </label>
          <label>空间逻辑 / Spatial logic
            <textarea data-idea-field="spatial_logic" rows="2" placeholder="门内外方向、视线、左右关系、屏幕位置、遮挡关系等硬规则">${escapeHtml(row.spatial_logic || "")}</textarea>
          </label>
          <label>图片提示词 / Image prompt
            <textarea data-idea-field="image_prompt" rows="4">${escapeHtml(row.image_prompt || "")}</textarea>
          </label>
          <label>视频提示词 / Video prompt
            <textarea data-idea-field="video_prompt" rows="2">${escapeHtml(row.video_prompt || "")}</textarea>
          </label>
          <label>备注 / Notes
            <textarea data-idea-field="notes" rows="2">${escapeHtml(row.notes || "")}</textarea>
          </label>
          <label>本次修图意见 / Revision note
            <textarea data-idea-field="revision_note" rows="2" placeholder="只写这一轮要改什么，例如：加一道关着的门，三个孩子更靠左，画面更干净">${escapeHtml(row.revision_note || "")}</textarea>
          </label>
          <label>排序 / 放在谁后面
            <input data-idea-field="sort_after" value="${escapeHtml(row.sort_after || "")}" placeholder="例如：05、MSB058、ACT2_SHOT_006 或情绪卡名字" />
          </label>
          <footer>
            <label>状态 / Status <input data-idea-field="status" value="${escapeHtml(row.status || "draft")}" /></label>
            <label>图片路径 / Output <input data-idea-field="output_path" value="${escapeHtml(row.output_path || "")}" /></label>
            <input data-idea-field="output_notes" value="${escapeHtml(row.output_notes || "")}" hidden />
            ${
              row.output_path
                ? `<a class="mini-command" href="/api/projects/${escapeHtml(state.selectedSlug || "")}/asset?origin=project&path=${encodeURIComponent(row.output_path)}" target="_blank">预览 / Preview</a>`
                : ""
            }
          </footer>
          <div class="idea-insert-after">
            <button class="idea-insert-row-after" data-help="在这张卡后面插入一张空白分镜卡，并自动关联当前卡。" data-idea-index="${index}" type="button" title="在这张卡后面插入一张空白分镜卡，并自动关联当前卡。">＋</button>
          </div>
        </article>
      `,
    )
    .join("");
}

function renderIdeaLab() {
  const root = $("ideaLab");
  if (!root) return;
  if (!state.detail) {
    root.innerHTML = "";
    return;
  }
  const board = currentIdeaBoard();
  if (isProjectBibleSelected()) {
    root.innerHTML = renderProjectBibleLab(board);
    bindIdeaLabEvents();
    return;
  }
  const sceneEntries = ideaRowEntriesForCardScope(board);
  const visibleEntries = filteredIdeaRowEntriesForCurrentScene(board);
  const activeInputs = activeIdeaInputs(board);
  ensureIdeaActiveRowForFilteredCards(board);
  root.innerHTML = `
    <div class="idea-header">
      <div>
        <p class="eyebrow">Idea Lab</p>
        <h3>创意到分镜 / Idea to Storyboard</h3>
        <p>每一步都会生成对应的 Codex 分析卡：先用故事大纲生成幕，再按当前幕生成分镜卡，最后把勾选分镜卡打成图片包。</p>
        <ol class="workflow-steps">
          <li><strong>01</strong><span>故事大纲生成幕</span></li>
          <li><strong>02</strong><span>当前幕生成分镜卡</span></li>
          <li><strong>03</strong><span>白模锁定空间/道具/人物关系</span></li>
          <li><strong>04</strong><span>分镜卡生成图片包</span></li>
          <li><strong>05</strong><span>Final版本进入图片页</span></li>
        </ol>
      </div>
      <div class="idea-actions">
        <button id="ideaBuildActsBtn" class="command-button priority" data-help="故事只有大纲时使用：让 AI 把整体故事扩展成一幕幕独立的戏，只更新幕结构和每幕故事草稿。" type="button">生成幕 / Build Acts</button>
        <button id="ideaBuildStoryboardCardsBtn" class="command-button primary" data-help="当前幕故事内容确定后使用：只按当前幕生成一张张分镜文字卡，不改其他幕。" type="button">生成分镜卡 / Build Cards</button>
        <button id="ideaWhiteboxBtn" class="command-button" data-help="在最终出图前锁定复杂空间、核心道具和人物关系；适合街机、并排对战、背后机位和走位复杂镜头。" type="button">生成白模 / Whitebox</button>
        <button id="cardPreflightBtn" class="command-button" data-help="在生成图片包前检查重复编号、空提示词、缺白模、缺连续性锁和空间逻辑风险。" type="button">生成前检查 / Preflight</button>
        <button id="cardBuildImagePacketBtn" class="command-button" data-help="把当前可见且勾选的分镜卡打包成图片生成任务。" type="button">生成图片包 / Image Pack</button>
        <button id="currentVersionPackageBtn" class="command-button" data-help="收集当前幕/场景已标为 Final 或参考的图片，供视频生成阶段使用。" type="button">Final图包 / Final Pack</button>
        <button id="ideaBoardPackageBtn" class="command-button" data-help="打包全项目创意区所有文字卡、图片提示词、视频提示词和已生成图片，并提供打开总包入口。" type="button">创意总包 / Idea Pack</button>
        <button id="actBoardPackageBtn" class="command-button" data-help="只打包当前幕的文字卡、图片提示词、视频提示词和已生成图片，并提供打开幕总包入口。" type="button">幕总包 / Act Pack</button>
        <button id="videoUploadPackageBtn" class="command-button primary" data-help="按当前幕顺序复制所有可用分镜图到上传文件夹，并生成一份可粘贴到 AIGC 视频网站的连续镜头提示词。" type="button">视频上传包 / Video Upload</button>
        <button id="batchVersionQaBtn" class="command-button" data-help="批量检查当前可见分镜图的清晰度、噪点、曝光和对比。" type="button">批量质检 / Batch QA</button>
        <button id="qaRepairPacketBtn" class="command-button" data-help="把低分图片整理成修复包，便于集中重生成。" type="button">低分修复包 / QA Fix</button>
        <button id="cardSelectVisibleBtn" class="command-button" data-help="勾选当前筛选出来的分镜卡，下一步只生成这些卡。" type="button">全选当前 / Select All</button>
        <button id="cardClearVisibleBtn" class="command-button" data-help="取消当前筛选结果的生成勾选，不删除文字卡。" type="button">清空当前 / Clear</button>
        <button id="ideaSaveBtn" class="command-button" data-help="手动保存当前所有文字、勾选、参考图和备注。" type="button">手动保存 / Save now</button>
        <button id="ideaAddRowBtn" class="command-button" data-help="在当前幕/场景下新增一张空白分镜文字卡。" type="button">新增条目 / Add Row</button>
      </div>
    </div>
    <div class="idea-layout">
      <section class="idea-seed-panel">
        <label>当前幕故事 / Act story
          <textarea id="ideaSeedInput" rows="5" placeholder="只写当前幕的故事内容；切换到其他幕会使用该幕自己的草稿 / Story for the current act only">${escapeHtml(activeInputs.idea || "")}</textarea>
        </label>
        <div class="idea-meta-grid">
          <label>片名 / Title <input id="ideaStoryTitle" value="${escapeHtml(activeInputs.story_title || "")}" /></label>
          <label>一句话 / Logline <input id="ideaLogline" value="${escapeHtml(activeInputs.logline || "")}" /></label>
        </div>
        <label>剧本大纲 / Story outline
          <textarea id="ideaOutline" rows="5">${escapeHtml(board.story_outline || "")}</textarea>
        </label>
        <label>风格与连续性 / Style and continuity
          <textarea id="ideaStyleNotes" rows="4">${escapeHtml(board.style_notes || "")}</textarea>
        </label>
        ${renderIdeaActPlanner(board)}
        ${renderActAutopilotPanel(board)}
        ${renderIdeaReferencePanel(board)}
        <div id="ideaHandoffDock" class="idea-handoff-dock">${renderIdeaHandoffs()}</div>
      </section>
      <section class="idea-rows-panel">
        <div class="idea-rows-header">
          <div class="idea-rows-title">
            <strong>${ideaSceneSummary(board)}</strong>
            <span>当前筛选显示 ${visibleEntries.length}/${sceneEntries.length}；保存会保留其他场戏和被隐藏条目。</span>
          </div>
          ${renderCardFilterControls(sceneEntries.length, visibleEntries.length, "storyboard", board)}
        </div>
        <div id="ideaRows" class="idea-rows">${renderIdeaRows(visibleEntries, board.rows)}</div>
      </section>
    </div>
  `;
  bindIdeaLabEvents();
}

function externalRetouchRows(board = currentIdeaBoard()) {
  return (board.rows || [])
    .map((row, index) => ({ row, index }))
    .filter(({ row }) => (row.act_id || "") === "EXT_RETOUCH");
}

function externalRetouchFilteredRows(board = currentIdeaBoard()) {
  const query = String(state.externalRetouch.query || "").trim().toLowerCase();
  const entries = externalRetouchRows(board);
  if (!query) return entries;
  return entries.filter(({ row }) => [
    row.item_id,
    row.beat,
    row.shot_type,
    row.frame_description,
    row.spatial_logic,
    row.image_prompt,
    row.video_prompt,
    row.notes,
    row.revision_note,
    row.status,
    row.output_path,
    ...(row.references || []).flatMap((ref) => [ref.asset_id, ref.path, ref.note, ref.role]),
    ...cardVersionEntries(row).flatMap((version) => [version.version_id, version.status, version.notes, version.output_path]),
  ].join(" ").toLowerCase().includes(query));
}

function collectExternalRetouchBoardFromDom(baseBoard = collectIdeaBoardFromDom()) {
  const board = {
    ...baseBoard,
    rows: Array.isArray(baseBoard.rows) ? [...baseBoard.rows] : [],
  };
  document.querySelectorAll(".external-retouch-card").forEach((card) => {
    const index = Number(card.dataset.ideaIndex || -1);
    if (!Number.isInteger(index) || index < 0 || !board.rows[index]) return;
    const existing = board.rows[index];
    const value = (field) => card.querySelector(`[data-ext-field="${field}"]`)?.value || "";
    board.rows[index] = {
      ...existing,
      item_id: value("item_id") || existing.item_id || "",
      act_id: "EXT_RETOUCH",
      scene_id: value("scene_id") || existing.scene_id || "SCN_EXTERNAL_RETOUCH",
      beat: value("beat"),
      shot_type: value("shot_type"),
      frame_description: value("frame_description"),
      linked_cards: parseStoryboardLinkInput(value("linked_cards")),
      spatial_logic: value("spatial_logic"),
      image_prompt: value("image_prompt"),
      video_prompt: value("video_prompt"),
      notes: value("notes"),
      revision_note: value("revision_note"),
      sort_after: value("sort_after"),
      selected: card.querySelector('[data-ext-field="selected"]')?.checked ?? true,
      status: value("status") || existing.status || "image_ready",
      output_path: existing.output_path || "",
      output_notes: existing.output_notes || "",
      output_attached_at: existing.output_attached_at || "",
      versions: Array.isArray(existing.versions) ? existing.versions : [],
      references: Array.isArray(existing.references) ? existing.references : [],
    };
  });
  return board;
}

function externalRetouchTargets(board = currentIdeaBoard()) {
  return externalRetouchFilteredRows(board)
    .filter(({ row }) => row.selected !== false)
    .map(({ row }) => ({
      card_type: "storyboard",
      card_uid: row.card_uid || "",
      item_id: row.item_id || "",
    }))
    .filter((target) => target.item_id);
}

function renderExternalRetouchScanList() {
  const results = state.externalRetouch.scanResults || [];
  if (!results.length) return `<div class="empty-state">还没有扫描结果 / No scanned images yet.</div>`;
  const selected = new Set(state.externalRetouch.selectedScanPaths || []);
  return `
    <div class="external-scan-list">
      ${results
        .map((item, index) => `
          <label class="external-scan-row" title="${escapeHtml(item.abs_path || "")}">
            <input class="external-scan-check" data-scan-index="${index}" type="checkbox" ${selected.has(item.abs_path) ? "checked" : ""} />
            <strong>${escapeHtml(item.name || "")}</strong>
            <span>${escapeHtml(item.extension || "")} · ${Math.round(Number(item.size || 0) / 1024)} KB</span>
          </label>
        `)
        .join("")}
    </div>
  `;
}

function renderExternalRetouchFolderPicker() {
  if (!state.externalRetouch.folderPickerOpen) return "";
  const listing = state.externalRetouch.folderPickerListing || {};
  const currentPath = listing.path || state.externalRetouch.folderPickerPath || "桌面 / Desktop";
  const directories = Array.isArray(listing.directories) ? listing.directories : [];
  const error = state.externalRetouch.folderPickerError || listing.error || "";
  return `
    <div class="external-folder-modal" role="dialog" aria-modal="true" aria-label="选择本地文件夹 / Choose local folder">
      <section class="external-folder-window">
        <header>
          <div>
            <p class="eyebrow">Local Folder</p>
            <h3>选择图片文件夹 / Choose image folder</h3>
            <p>${escapeHtml(currentPath)}</p>
          </div>
          <button id="externalFolderPickerClose" class="icon-button" type="button" title="关闭 / Close">×</button>
        </header>
        <div class="external-folder-toolbar">
          <button id="externalFolderPickerDesktop" class="command-button" type="button">桌面 / Desktop</button>
          <button id="externalFolderPickerParent" class="command-button" type="button" ${listing.parent ? "" : "disabled"}>上一级 / Parent</button>
          <button id="externalFolderPickerChoose" class="command-button primary" type="button" ${listing.path ? "" : "disabled"}>选择此文件夹 / Choose</button>
        </div>
        ${error ? `<div class="empty-state compact">${escapeHtml(error)}</div>` : ""}
        <div class="external-folder-list">
          ${
            directories.length
              ? directories
                  .map((item) => `
                    <button class="external-folder-row" data-folder-path="${escapeHtml(item.path || "")}" type="button">
                      <span>▸</span>
                      <strong>${escapeHtml(item.name || item.path || "")}</strong>
                      <small>${escapeHtml(item.path || "")}</small>
                    </button>
                  `)
                  .join("")
              : `<div class="empty-state compact">这个文件夹下没有可进入的子文件夹 / No subfolders here.</div>`
          }
        </div>
      </section>
    </div>
  `;
}

function renderExternalRetouchReferenceList(board = currentIdeaBoard()) {
  const refs = (board.global_references || []).filter((ref) => String(ref.role || "").includes("external_retouch"));
  if (!refs.length) return `<div class="empty-state compact">暂无外部修图全局参考 / No global retouch references.</div>`;
  return `
    <div class="external-ref-list">
      ${refs
        .slice(-8)
        .reverse()
        .map((ref) => `
          <a class="external-ref-chip" href="${escapeHtml(ideaReferenceUrl(ref))}" target="_blank" title="${escapeHtml(ref.note || ref.path || "")}">
            ${isImagePath(ref.path || "") ? `<img src="${escapeHtml(ideaReferenceUrl(ref))}" alt="${escapeHtml(ref.asset_id || "")}" loading="lazy" />` : ""}
            <span>${escapeHtml(ref.note || ref.asset_id || ref.path || "")}</span>
          </a>
        `)
        .join("")}
    </div>
  `;
}

function externalRetouchActiveRowEntry(board = currentIdeaBoard()) {
  const entries = externalRetouchRows(board);
  if (!entries.length) {
    state.externalRetouch.activeRowIndex = 0;
    return null;
  }
  let index = Number(state.externalRetouch.activeRowIndex ?? entries[0].index);
  if (!entries.some((entry) => entry.index === index)) index = entries[0].index;
  state.externalRetouch.activeRowIndex = index;
  return entries.find((entry) => entry.index === index) || entries[0];
}

function externalRetouchReferenceAssets() {
  const assets = allBoardImageAssets().filter((asset) => frameIsUsable(asset));
  const filters = currentImageLibraryFilters(assets);
  return assets.filter((asset) => imageAssetMatchesLibraryFilters(asset, { act: filters.scope, tag: filters.tag, query: filters.query }, "act"));
}

function renderExternalRetouchReferenceLibrary(board = currentIdeaBoard()) {
  const allAssets = allBoardImageAssets().filter((asset) => frameIsUsable(asset));
  const filters = currentImageLibraryFilters(allAssets);
  const assets = externalRetouchReferenceAssets().slice(0, 60);
  const activeEntry = externalRetouchActiveRowEntry(board);
  return `
    <div class="external-control-card external-reference-library">
      <div class="external-library-head">
        <strong>项目图片库 / Reference library</strong>
        <span>${assets.length}/${allAssets.length} 匹配 · 当前卡 ${escapeHtml(activeEntry?.row?.item_id || "未选择")}</span>
      </div>
      <div class="external-library-filters">
        <label>范围 / Scope
          <select id="externalRetouchRefScopeFilter">
            ${ideaReferenceActOptions(allAssets).map((option) => `<option value="${escapeHtml(option.value)}" ${filters.scope === option.value ? "selected" : ""}>${escapeHtml(option.label)}</option>`).join("")}
          </select>
        </label>
        <label>标签 / Tag
          <select id="externalRetouchRefTagFilter">
            ${BOARD_TAG_OPTIONS.map((option) => `<option value="${escapeHtml(option.value)}" ${filters.tag === option.value ? "selected" : ""}>${escapeHtml(option.label)}</option>`).join("")}
          </select>
        </label>
        <label>搜索 / Search
          <input id="externalRetouchRefSearchInput" value="${escapeHtml(filters.query || "")}" placeholder="人物、场景、白模、镜头、路径 / character, scene, whitebox, shot, path" />
        </label>
      </div>
      <div class="idea-ref-asset-grid external-ref-asset-grid">
        ${
          assets.length
            ? assets
                .map((asset) => {
                  const versionLabel = asset.version_status ? CARD_VERSION_STATUS_LABELS[asset.version_status] || asset.version_status : "";
                  return `
                    <article class="idea-ref-asset external-ref-asset" draggable="true" data-asset-ref="${escapeHtml(asset.ref)}">
                      <img src="${escapeHtml(asset.url)}" alt="${escapeHtml(asset.asset_id || asset.path)}" loading="lazy" />
                      <strong>${escapeHtml(asset.asset_id || asset.role || asset.path)}</strong>
                      <small>${escapeHtml(asset.scene_id || asset.act_id || "PROJECT")} · ${escapeHtml(kindLabel(asset.kind))}${versionLabel ? ` · ${escapeHtml(versionLabel)}` : ""}${escapeHtml(assetQaLabel(asset))}</small>
                      ${asset.card_id ? `<small>${escapeHtml(asset.card_id)}${asset.card_title ? ` · ${escapeHtml(asset.card_title)}` : ""}</small>` : ""}
                      <div>
                        <button class="mini-command external-add-library-ref" data-ref-scope="global" data-asset-ref="${escapeHtml(asset.ref)}" type="button">全局参考</button>
                        <button class="mini-command external-add-library-ref" data-ref-scope="card" data-asset-ref="${escapeHtml(asset.ref)}" type="button" ${activeEntry ? "" : "disabled"}>当前卡参考</button>
                        <button class="mini-command external-send-library-board" data-asset-ref="${escapeHtml(asset.ref)}" type="button">送入画板</button>
                      </div>
                    </article>
                  `;
                })
                .join("")
            : `<div class="empty-state">没有匹配参考图 / No matching references.</div>`
        }
      </div>
    </div>
  `;
}

function addExternalRetouchAssetReference(scope, assetRef) {
  const board = collectExternalRetouchBoardFromDom();
  const asset = allBoardImageAssets().find((item) => item.ref === assetRef);
  if (!asset) return;
  const ref = {
    ...makeIdeaReference(asset),
    role: scope === "global" ? "external_retouch_global_reference" : "external_retouch_card_reference",
  };
  if (scope === "global") {
    const note = $("externalRetouchGlobalRefNote")?.value.trim() || state.externalRetouch.globalReferenceNote || "";
    ref.note = note || ref.note || "外部修图全局参考 / Global retouch reference";
    board.global_references = normalizeIdeaReferenceList([...(board.global_references || []), ref]);
    setIdeaBoardLocal(board);
    renderExternalRetouchLab();
    toast("已加入外部修图全局参考 / Added global retouch reference");
    return;
  }
  const activeEntry = externalRetouchActiveRowEntry(board);
  if (!activeEntry?.row) {
    toast("请先选择一张外部修图卡 / Select a retouch card first");
    return;
  }
  ref.note = ref.note || "外部修图单张参考 / Card retouch reference";
  activeEntry.row.references = normalizeIdeaReferenceList([...(activeEntry.row.references || []), ref]);
  board.rows[activeEntry.index] = activeEntry.row;
  state.externalRetouch.activeRowIndex = activeEntry.index;
  setIdeaBoardLocal(board);
  renderExternalRetouchLab();
  toast(`已绑定到 ${activeEntry.row.item_id || "当前卡"} / Added to current card`);
}

function sendExternalRetouchAssetToBoard(assetRef) {
  if (!state.detail) return;
  state.boardOpen = true;
  loadBoardState();
  addBoardNode(assetRef, boardDefaultNodePoint());
  toast("已送入画板 / Sent to board");
}

function renderExternalRetouchCard(row, index) {
  const active = Number(state.externalRetouch.activeRowIndex || 0) === index;
  return `
    <article class="external-retouch-card ${active ? "active" : ""}" data-idea-index="${index}" data-card-uid="${escapeHtml(row.card_uid || "")}">
      <header>
        <label>编号 / ID <input data-ext-field="item_id" value="${escapeHtml(row.item_id || "")}" /></label>
        <label>场戏 / Scene <input data-ext-field="scene_id" value="${escapeHtml(row.scene_id || "SCN_EXTERNAL_RETOUCH")}" /></label>
        <label>镜头 / Shot <input data-ext-field="shot_type" value="${escapeHtml(row.shot_type || "")}" /></label>
        <label class="checkbox-label"><input data-ext-field="selected" type="checkbox" ${row.selected === false ? "" : "checked"} /> 本次修图</label>
        <button class="mini-command external-card-active" type="button">${active ? "当前卡" : "设当前"}</button>
        <button class="mini-command external-card-save" type="button">保存</button>
        <button class="mini-command external-card-packet-one" type="button">只修这张</button>
      </header>
      <div class="external-card-main">
        ${renderCardVersionPreview(row, "外部图版本 / External image versions")}
      </div>
      <section class="external-card-priority-note">
        <label>本次修图意见 / Revision note
          <textarea data-ext-field="revision_note" rows="3" placeholder="例如：把人物替换成三兄弟；黄毛按全局参考；保留构图和灯光">${escapeHtml(row.revision_note || "")}</textarea>
        </label>
      </section>
      <details class="external-card-details" open>
        <summary>文字分析、提示词与排序 / Analysis, prompts and ordering</summary>
        <div class="external-card-fields">
          <label>剧情点 / Beat
            <textarea data-ext-field="beat" rows="2">${escapeHtml(row.beat || "")}</textarea>
          </label>
          <label>画面描述 / Frame description
            <textarea data-ext-field="frame_description" rows="3">${escapeHtml(row.frame_description || "")}</textarea>
          </label>
          <label>空间逻辑 / Spatial logic
            <textarea data-ext-field="spatial_logic" rows="2">${escapeHtml(row.spatial_logic || "")}</textarea>
          </label>
          <label>图片提示词 / Image prompt
            <textarea data-ext-field="image_prompt" rows="4">${escapeHtml(row.image_prompt || "")}</textarea>
          </label>
          <label>视频生成提示词 / Video prompt
            <textarea data-ext-field="video_prompt" rows="4">${escapeHtml(row.video_prompt || "")}</textarea>
          </label>
          <label>图片基本分析 / Basic analysis
            <textarea data-ext-field="notes" rows="3">${escapeHtml(row.notes || "")}</textarea>
          </label>
          <label>关联分镜 / Linked cards
            <input data-ext-field="linked_cards" value="${escapeHtml(storyboardLinkValue(row.linked_cards || []))}" />
          </label>
          <label>排序 / Sort after
            <input data-ext-field="sort_after" value="${escapeHtml(row.sort_after || "")}" />
          </label>
          <label>状态 / Status
            <input data-ext-field="status" value="${escapeHtml(row.status || "image_ready")}" />
          </label>
        </div>
      </details>
      <section class="external-card-reference-panel">
        <div>
          <strong>单张参考 / Card references</strong>
          <span>${(row.references || []).length} refs</span>
        </div>
        <div class="external-ref-list">
          ${(row.references || [])
            .map((ref) => `
              <a class="external-ref-chip" href="${escapeHtml(ideaReferenceUrl(ref))}" target="_blank" title="${escapeHtml(ref.note || ref.path || "")}">
                ${isImagePath(ref.path || "") ? `<img src="${escapeHtml(ideaReferenceUrl(ref))}" alt="${escapeHtml(ref.asset_id || "")}" loading="lazy" />` : ""}
                <span>${escapeHtml(ref.note || ref.asset_id || ref.path || "")}</span>
              </a>
            `)
            .join("")}
        </div>
        <div class="external-reference-upload">
          <input class="external-card-reference-file" type="file" accept="image/*" multiple />
          <input class="external-card-reference-note" value="" placeholder="这张参考要用哪里：脸、衣服、门、灯光、构图..." />
          <button class="mini-command external-card-reference-upload" type="button">上传到本卡 / Upload</button>
        </div>
        <div class="external-reference-hint">也可以在左侧图片库点击“当前卡参考”，会绑定到标记为“当前卡”的这张分镜卡。</div>
        <div class="external-version-drop">拖入新图可直接成为本卡候选版本 / Drop a new image here as a candidate version</div>
      </section>
    </article>
  `;
}

function renderExternalRetouchLab() {
  const root = $("externalRetouchLab");
  if (!root) return;
  if (!state.detail) {
    root.innerHTML = "";
    return;
  }
  const board = currentIdeaBoard();
  const rows = externalRetouchFilteredRows(board);
  const allRows = externalRetouchRows(board);
  if (rows.length && !rows.some(({ index }) => index === Number(state.externalRetouch.activeRowIndex || 0))) {
    state.externalRetouch.activeRowIndex = rows[0].index;
  }
  const selectedCount = rows.filter(({ row }) => row.selected !== false).length;
  root.innerHTML = `
    <div class="external-retouch-header">
      <div>
        <p class="eyebrow">External Retouch</p>
        <h3>外部修图 / Batch external image retouch</h3>
        <ol class="workflow-steps">
          <li><strong>01</strong><span>扫描本地图片</span></li>
          <li><strong>02</strong><span>导入为分镜卡</span></li>
          <li><strong>03</strong><span>绑定全局/单张参考</span></li>
          <li><strong>04</strong><span>生成分析卡或修图包</span></li>
          <li><strong>05</strong><span>选择 Final</span></li>
        </ol>
      </div>
      <div class="external-retouch-actions">
        <button id="externalRetouchSaveBtn" class="command-button" type="button">保存 / Save</button>
        <button id="externalRetouchAnalysisBtn" class="command-button primary" type="button">生成分析卡 / Analysis Card</button>
        <button id="externalRetouchPacketBtn" class="command-button priority" type="button">生成修图包 / Retouch Pack</button>
        <button id="externalRetouchSelectBtn" class="command-button" type="button">全选当前 / Select</button>
        <button id="externalRetouchClearBtn" class="command-button" type="button">清空当前 / Clear</button>
      </div>
    </div>
    <div class="external-retouch-layout">
      <section class="external-retouch-control">
        <div class="external-control-card">
          <strong>扫描外部图片 / Scan local images</strong>
          <label>本地文件夹 / Local folder</label>
          <div class="external-folder-field">
            <input id="externalRetouchFolder" value="${escapeHtml(state.externalRetouch.folderPath || "")}" placeholder="点击打开 macOS 文件夹选择器 / Click to open macOS folder picker" readonly />
            <button id="externalRetouchBrowseFolderBtn" class="command-button" type="button">浏览 / Browse</button>
          </div>
          <div class="external-control-row">
            <label class="checkbox-label"><input id="externalRetouchRecursive" type="checkbox" ${state.externalRetouch.recursive ? "checked" : ""} /> 包含子文件夹</label>
            <label>上限 / Max <input id="externalRetouchMax" type="number" min="1" max="2000" value="${escapeHtml(state.externalRetouch.maxImages || 300)}" /></label>
          </div>
          <div class="external-control-row">
            <button id="externalRetouchScanBtn" class="command-button" type="button">扫描 / Scan</button>
            <button id="externalRetouchImportBtn" class="command-button primary" type="button">导入为卡片 / Import Cards</button>
          </div>
          <small>${state.externalRetouch.scanResults.length} 扫描结果 / scanned · ${(state.externalRetouch.selectedScanPaths || []).length} 已选 / selected</small>
          ${renderExternalRetouchScanList()}
        </div>
        <div class="external-control-card">
          <strong>全局参考 / Global references</strong>
          <textarea id="externalRetouchGlobalRefNote" rows="4" placeholder="例如：所有出现三兄弟的图，都按这张人设替换脸和服装；黄毛按另一张图替换发型和气质">${escapeHtml(state.externalRetouch.globalReferenceNote || "")}</textarea>
          <input id="externalRetouchGlobalRefFiles" type="file" accept="image/*" multiple />
          <button id="externalRetouchGlobalRefUploadBtn" class="command-button" type="button">上传全局参考 / Upload Global Ref</button>
          ${renderExternalRetouchReferenceList(board)}
        </div>
        ${renderExternalRetouchReferenceLibrary(board)}
      </section>
      <section class="external-retouch-cards">
        <div class="external-retouch-card-toolbar">
          <strong>${selectedCount}/${rows.length} 当前可见 · ${allRows.length} 外部修图卡</strong>
          <input id="externalRetouchSearch" value="${escapeHtml(state.externalRetouch.query || "")}" placeholder="搜索外部卡、提示词、版本、参考 / Search" />
        </div>
        ${
          rows.length
            ? rows.map(({ row, index }) => renderExternalRetouchCard(row, index)).join("")
            : `<div class="empty-state">还没有外部修图卡。先扫描并导入图片 / No external retouch cards yet. Scan and import images first.</div>`
        }
      </section>
    </div>
    ${renderExternalRetouchFolderPicker()}
  `;
  bindExternalRetouchEvents();
}

async function persistExternalRetouchBoard(options = {}) {
  if (!state.selectedSlug || !state.detail) return null;
  const board = collectExternalRetouchBoardFromDom();
  const result = await requestJson(`/api/projects/${state.selectedSlug}/idea-board`, {
    method: "POST",
    body: JSON.stringify(board),
  });
  state.detail = result.project || state.detail;
  setIdeaBoardLocal(result.idea_board || board);
  if (options.toast !== false) toast("外部修图已保存 / External retouch saved");
  if (options.render !== false) renderAll();
  return result;
}

function updateExternalRetouchScanSelection() {
  state.externalRetouch.selectedScanPaths = Array.from(document.querySelectorAll(".external-scan-check:checked"))
    .map((input) => state.externalRetouch.scanResults[Number(input.dataset.scanIndex || -1)]?.abs_path || "")
    .filter(Boolean);
}

async function loadExternalRetouchFolder(path = "") {
  if (!state.selectedSlug) return;
  state.externalRetouch.folderPickerError = "";
  try {
    const result = await requestJson(`/api/projects/${state.selectedSlug}/external-retouch-folder-list`, {
      method: "POST",
      body: JSON.stringify({ path }),
    });
    state.externalRetouch.folderPickerListing = result;
    state.externalRetouch.folderPickerPath = result.path || path || "";
  } catch (error) {
    state.externalRetouch.folderPickerError = error.message;
  }
  renderExternalRetouchLab();
}

async function openExternalRetouchFolderPicker(path = "") {
  state.externalRetouch.folderPickerOpen = true;
  state.externalRetouch.folderPickerListing = null;
  state.externalRetouch.folderPickerError = "";
  renderExternalRetouchLab();
  await loadExternalRetouchFolder(path || "");
}

async function chooseExternalRetouchFolderNative() {
  if (!state.selectedSlug || state.externalRetouch.nativeFolderPickerOpen) return;
  state.externalRetouch.nativeFolderPickerOpen = true;
  toast("正在打开 macOS 文件夹选择器 / Opening folder picker...");
  try {
    const result = await requestJson(`/api/projects/${state.selectedSlug}/external-retouch-choose-folder`, {
      method: "POST",
      body: JSON.stringify({ path: state.externalRetouch.folderPath || "" }),
    });
    if (result.ok && result.path) {
      state.externalRetouch.folderPath = result.path;
      state.externalRetouch.folderPickerOpen = false;
      state.externalRetouch.scanResults = [];
      state.externalRetouch.selectedScanPaths = [];
      renderExternalRetouchLab();
      toast("已选择本地文件夹 / Folder selected");
      return;
    }
    if (result.canceled) return;
    toast(result.error || "系统文件夹选择器不可用，改用列表选择 / Native picker unavailable; using list picker");
    await openExternalRetouchFolderPicker("");
  } catch (error) {
    toast(`系统文件夹选择器失败 / Native picker failed: ${error.message}`);
    await openExternalRetouchFolderPicker("");
  } finally {
    state.externalRetouch.nativeFolderPickerOpen = false;
  }
}

function closeExternalRetouchFolderPicker() {
  state.externalRetouch.folderPickerOpen = false;
  renderExternalRetouchLab();
}

function chooseExternalRetouchFolder(path = "") {
  const selectedPath = path || state.externalRetouch.folderPickerListing?.path || "";
  if (!selectedPath) return;
  state.externalRetouch.folderPath = selectedPath;
  state.externalRetouch.folderPickerOpen = false;
  state.externalRetouch.scanResults = [];
  state.externalRetouch.selectedScanPaths = [];
  renderExternalRetouchLab();
  toast("已选择本地文件夹 / Folder selected");
}

async function scanExternalRetouchImages() {
  if (!state.selectedSlug) return;
  state.externalRetouch.folderPath = $("externalRetouchFolder")?.value.trim() || "";
  state.externalRetouch.recursive = $("externalRetouchRecursive")?.checked ?? true;
  state.externalRetouch.maxImages = Number($("externalRetouchMax")?.value || 300);
  await runAction("扫描外部图片 / Scan external images", async () => {
    const result = await requestJson(`/api/projects/${state.selectedSlug}/external-retouch-scan`, {
      method: "POST",
      body: JSON.stringify({
        folder_path: state.externalRetouch.folderPath,
        recursive: state.externalRetouch.recursive,
        max_images: state.externalRetouch.maxImages,
      }),
    });
    state.externalRetouch.scanResults = result.images || [];
    state.externalRetouch.selectedScanPaths = state.externalRetouch.scanResults.map((item) => item.abs_path).filter(Boolean);
    renderExternalRetouchLab();
  });
}

async function importExternalRetouchImages() {
  if (!state.selectedSlug) return;
  updateExternalRetouchScanSelection();
  const images = (state.externalRetouch.scanResults || []).filter((item) => (state.externalRetouch.selectedScanPaths || []).includes(item.abs_path));
  if (!images.length) {
    toast("请先勾选要导入的图片 / Select images to import");
    return;
  }
  await runAction("导入外部修图卡 / Import external retouch cards", async () => {
    const result = await requestJson(`/api/projects/${state.selectedSlug}/external-retouch-import`, {
      method: "POST",
      body: JSON.stringify({ images }),
    });
    state.detail = result.project || state.detail;
    state.externalRetouch.selectedScanPaths = [];
    renderAll();
  });
}

async function uploadExternalRetouchReference({ scope = "global", card = null } = {}) {
  if (!state.selectedSlug) return;
  const fileInput = scope === "global" ? $("externalRetouchGlobalRefFiles") : card?.querySelector(".external-card-reference-file");
  const files = [...(fileInput?.files || [])].filter(fileIsImage);
  if (!files.length) {
    toast("请选择参考图片 / Select reference images");
    return;
  }
  const note = scope === "global"
    ? ($("externalRetouchGlobalRefNote")?.value.trim() || "外部修图全局参考 / Global retouch reference")
    : (card?.querySelector(".external-card-reference-note")?.value.trim() || "外部修图单张参考 / Card retouch reference");
  if (scope === "global") state.externalRetouch.globalReferenceNote = note;
  await runAction(scope === "global" ? "上传全局参考 / Upload global reference" : "上传单张参考 / Upload card reference", async () => {
    let latestProject = null;
    for (const file of files) {
      const dataUrl = await readFileAsDataUrl(file);
      const result = await requestJson(`/api/projects/${state.selectedSlug}/external-retouch-reference-upload`, {
        method: "POST",
        body: JSON.stringify({
          scope,
          item_id: card?.querySelector('[data-ext-field="item_id"]')?.value || "",
          card_uid: card?.dataset.cardUid || "",
          file_name: file.name || "reference.png",
          data_url: dataUrl,
          note,
        }),
      });
      latestProject = result.project || latestProject;
    }
    if (latestProject) state.detail = latestProject;
    renderAll();
  });
}

async function uploadExternalRetouchCandidate(card, file) {
  if (!state.selectedSlug || !card || !fileIsImage(file)) {
    toast("只能拖入图片文件 / Drop an image file");
    return;
  }
  const board = collectExternalRetouchBoardFromDom();
  setIdeaBoardLocal(board);
  const rowIndex = Number(card.dataset.ideaIndex || 0);
  const row = board.rows?.[rowIndex];
  if (!row?.item_id) {
    toast("没有找到这张外部修图卡 / External retouch card not found");
    return;
  }
  const dataUrl = await readFileAsDataUrl(file);
  const payload = await requestJson(`/api/projects/${encodeURIComponent(state.selectedSlug)}/card-version-upload`, {
    method: "POST",
    body: JSON.stringify({
      card_type: "storyboard",
      item_id: row.item_id,
      card_uid: row.card_uid || "",
      file_name: file.name || "external-retouch-candidate.png",
      mime_type: file.type || "",
      data_url: dataUrl,
      notes: `外部修图候选图 / External retouch candidate: ${file.name || "image"}`,
    }),
  });
  state.detail = payload.project || state.detail;
  renderAll();
  toast("已加入外部修图卡候选版本 / Added candidate version");
}

async function createExternalRetouchAnalysisPacket() {
  if (!state.selectedSlug || !state.detail) return;
  await runAction("外部修图分析卡 / External retouch analysis", async () => {
    const board = collectExternalRetouchBoardFromDom();
    const targets = externalRetouchTargets(board);
    if (!targets.length) {
      toast("请先勾选外部修图卡 / Select retouch cards first");
      return;
    }
    const result = await requestJson(`/api/projects/${state.selectedSlug}/external-retouch-analysis-packet`, {
      method: "POST",
      body: JSON.stringify({ ...board, targets }),
    });
    state.detail = result.project || state.detail;
    addIdeaHandoff({
      kind: "external_retouch_analysis",
      title: `${result.target_count || 0} 张外部图 → Codex 解析`,
      path: result.packet_path || "",
      text: result.handoff_text || "",
    });
    renderAll();
  });
}

async function createExternalRetouchPacket(singleCard = null) {
  if (!state.selectedSlug || !state.detail) return;
  await runAction("外部修图包 / External retouch packet", async () => {
    const board = collectExternalRetouchBoardFromDom();
    const targets = singleCard
      ? [{
          card_type: "storyboard",
          card_uid: singleCard.dataset.cardUid || "",
          item_id: singleCard.querySelector('[data-ext-field="item_id"]')?.value || "",
        }]
      : externalRetouchTargets(board);
    await createCardImagePacketForTargets(board, targets, "external_retouch_image", "请先勾选要修图的外部卡 / Select external retouch cards first");
  });
}

function setExternalRetouchVisibleSelection(checked) {
  const board = collectExternalRetouchBoardFromDom();
  externalRetouchFilteredRows(board).forEach(({ index }) => {
    if (board.rows[index]) board.rows[index].selected = checked;
  });
  setIdeaBoardLocal(board);
  renderExternalRetouchLab();
}

function bindExternalVersionButtons(root) {
  root.querySelectorAll(".card-version-preview-link").forEach((link) => {
    link.addEventListener("click", handleCardVersionPreviewClick);
  });
  root.querySelectorAll(".card-version-to-board").forEach((button) => {
    button.addEventListener("click", () => sendVersionImageToBoard(button.dataset.versionPath || ""));
  });
  root.querySelectorAll(".card-version-status").forEach((button) => {
    button.addEventListener("click", () => updateCardVersionStatus(button));
  });
  root.querySelectorAll(".card-version-qa-run").forEach((button) => {
    button.addEventListener("click", () => runCardVersionQa(button));
  });
}

function bindExternalRetouchEvents() {
  const root = $("externalRetouchLab");
  if (!root) return;
  $("externalRetouchFolder")?.addEventListener("click", () => {
    chooseExternalRetouchFolderNative();
  });
  $("externalRetouchFolder")?.addEventListener("focus", () => {
    chooseExternalRetouchFolderNative();
  });
  $("externalRetouchBrowseFolderBtn")?.addEventListener("click", () => {
    chooseExternalRetouchFolderNative();
  });
  $("externalRetouchRecursive")?.addEventListener("change", (event) => {
    state.externalRetouch.recursive = event.target.checked;
  });
  $("externalRetouchMax")?.addEventListener("input", (event) => {
    state.externalRetouch.maxImages = Number(event.target.value || 300);
  });
  $("externalRetouchSearch")?.addEventListener("input", (event) => {
    state.externalRetouch.query = event.target.value || "";
    const board = collectExternalRetouchBoardFromDom();
    setIdeaBoardLocal(board);
    renderExternalRetouchLab();
  });
  $("externalRetouchScanBtn")?.addEventListener("click", scanExternalRetouchImages);
  $("externalRetouchImportBtn")?.addEventListener("click", importExternalRetouchImages);
  $("externalRetouchSaveBtn")?.addEventListener("click", () => persistExternalRetouchBoard());
  $("externalRetouchAnalysisBtn")?.addEventListener("click", createExternalRetouchAnalysisPacket);
  $("externalRetouchPacketBtn")?.addEventListener("click", () => createExternalRetouchPacket());
  $("externalRetouchSelectBtn")?.addEventListener("click", () => setExternalRetouchVisibleSelection(true));
  $("externalRetouchClearBtn")?.addEventListener("click", () => setExternalRetouchVisibleSelection(false));
  $("externalRetouchGlobalRefNote")?.addEventListener("input", (event) => {
    state.externalRetouch.globalReferenceNote = event.target.value || "";
  });
  $("externalRetouchGlobalRefUploadBtn")?.addEventListener("click", () => uploadExternalRetouchReference({ scope: "global" }));
  $("externalFolderPickerClose")?.addEventListener("click", closeExternalRetouchFolderPicker);
  $("externalFolderPickerDesktop")?.addEventListener("click", () => loadExternalRetouchFolder(""));
  $("externalFolderPickerParent")?.addEventListener("click", () => loadExternalRetouchFolder(state.externalRetouch.folderPickerListing?.parent || ""));
  $("externalFolderPickerChoose")?.addEventListener("click", () => chooseExternalRetouchFolder());
  root.querySelectorAll(".external-folder-row").forEach((button) => {
    button.addEventListener("click", () => loadExternalRetouchFolder(button.dataset.folderPath || ""));
  });
  $("externalRetouchRefScopeFilter")?.addEventListener("change", (event) => {
    setImageLibraryFilters({ scope: event.target.value || "all" }, allBoardImageAssets());
    renderExternalRetouchLab();
  });
  $("externalRetouchRefTagFilter")?.addEventListener("change", (event) => {
    setImageLibraryFilters({ tag: event.target.value || "all" }, allBoardImageAssets());
    renderExternalRetouchLab();
  });
  $("externalRetouchRefSearchInput")?.addEventListener("input", (event) => {
    setImageLibraryFilters({ query: event.target.value || "" }, allBoardImageAssets());
    renderExternalRetouchLab();
  });
  root.querySelectorAll(".external-add-library-ref").forEach((button) => {
    button.addEventListener("click", () => addExternalRetouchAssetReference(button.dataset.refScope || "card", button.dataset.assetRef || ""));
  });
  root.querySelectorAll(".external-send-library-board").forEach((button) => {
    button.addEventListener("click", () => sendExternalRetouchAssetToBoard(button.dataset.assetRef || ""));
  });
  root.querySelectorAll(".external-ref-asset").forEach((card) => {
    card.addEventListener("dragstart", (event) => {
      const assetRef = card.dataset.assetRef || "";
      if (!assetRef) return;
      event.dataTransfer?.setData("text/plain", assetRef);
      event.dataTransfer?.setData("application/x-pipeline-asset-ref", assetRef);
      event.dataTransfer.effectAllowed = "copy";
    });
  });
  root.querySelectorAll(".external-scan-check").forEach((checkbox) => {
    checkbox.addEventListener("change", updateExternalRetouchScanSelection);
  });
  root.querySelectorAll(".external-card-active").forEach((button) => {
    button.addEventListener("click", () => {
      const card = button.closest(".external-retouch-card");
      state.externalRetouch.activeRowIndex = Number(card?.dataset.ideaIndex || 0);
      setIdeaBoardLocal(collectExternalRetouchBoardFromDom());
      renderExternalRetouchLab();
    });
  });
  root.querySelectorAll(".external-card-save").forEach((button) => {
    button.addEventListener("click", () => persistExternalRetouchBoard());
  });
  root.querySelectorAll(".external-card-packet-one").forEach((button) => {
    button.addEventListener("click", () => createExternalRetouchPacket(button.closest(".external-retouch-card")));
  });
  root.querySelectorAll(".external-card-reference-upload").forEach((button) => {
    button.addEventListener("click", () => uploadExternalRetouchReference({ scope: "card", card: button.closest(".external-retouch-card") }));
  });
  root.querySelectorAll(".external-retouch-card").forEach((card) => {
    card.addEventListener("dragover", (event) => {
      const types = Array.from(event.dataTransfer?.types || []);
      if (!types.includes("Files")) return;
      event.preventDefault();
      event.dataTransfer.dropEffect = "copy";
      card.classList.add("drop-target");
    });
    card.addEventListener("dragleave", () => card.classList.remove("drop-target"));
    card.addEventListener("drop", async (event) => {
      event.preventDefault();
      card.classList.remove("drop-target");
      const file = [...(event.dataTransfer?.files || [])].find(fileIsImage);
      if (!file) return;
      try {
        await uploadExternalRetouchCandidate(card, file);
      } catch (error) {
        toast(`导入候选图失败 / Candidate import failed: ${error.message}`);
      }
    });
  });
  bindExternalVersionButtons(root);
}

async function saveIdeaBoard(options = {}) {
  if (!state.selectedSlug || !state.detail) return null;
  const board = collectIdeaBoardFromDom();
  return persistIdeaBoard(board, options);
}

async function persistIdeaBoard(board, options = {}) {
  if (!state.selectedSlug || !state.detail) return null;
  const result = await requestJson(`/api/projects/${state.selectedSlug}/idea-board`, {
    method: "POST",
    body: JSON.stringify(board),
  });
  state.detail = result.project || state.detail;
  if (options.toast !== false) toast("Idea Board 已保存 / Idea Board saved");
  if (options.render !== false) renderIdeaLab();
  return result;
}

async function createIdeaActsHandoff() {
  if (!state.detail) return;
  await runAction("生成幕 / Build acts", async () => {
    const board = collectIdeaBoardFromDom();
    const result = await persistIdeaBoard(board, { toast: false, render: false });
    const savedBoard = result?.idea_board || board;
    setIdeaBoardLocal(savedBoard);
    addIdeaHandoff({
      kind: "build_acts",
      title: `${savedBoard.story_title || "Story outline"} → 生成幕`,
      text: buildIdeaActsHandoff(savedBoard),
    });
    renderIdeaLab();
    toast("已自动保存并生成幕交接卡 / Saved and build-acts handoff ready");
  });
}

async function createIdeaStoryboardCardsHandoff() {
  if (!state.detail) return;
  if (!activeStoryActId()) {
    toast("请先在左侧选择一幕 / Select an act first");
    return;
  }
  await runAction("生成分镜卡 / Build storyboard cards", async () => {
    const board = collectIdeaBoardFromDom();
    const result = await persistIdeaBoard(board, { toast: false, render: false });
    const savedBoard = result?.idea_board || board;
    setIdeaBoardLocal(savedBoard);
    const activeBoard = boardWithActiveIdeaInputs(savedBoard);
    const actId = activeStoryActId();
    addIdeaHandoff({
      kind: "build_storyboard_cards",
      title: `${actId || "Act"} → 生成分镜卡`,
      text: buildIdeaStoryboardCardsHandoff(activeBoard),
    });
    renderIdeaLab();
    toast("已自动保存并生成分镜卡交接卡 / Saved and storyboard-card handoff ready");
  });
}

async function createActAutopilotPacket() {
  if (!state.selectedSlug || !state.detail) return;
  await runAction("远程总控 / Act autopilot", async () => {
    const board = collectIdeaBoardFromDom();
    const actId = ($("actAutopilotActId")?.value || activeStoryActId() || "").trim();
    const storyBrief = ($("actAutopilotBrief")?.value || "").trim();
    if (!actId) {
      toast("请填写目标幕编号 / Enter target act id");
      return;
    }
    if (!storyBrief) {
      toast("请先填写这一幕主要剧情 / Enter the act plot first");
      return;
    }
    const result = await requestJson(`/api/projects/${state.selectedSlug}/act-autopilot-packet`, {
      method: "POST",
      body: JSON.stringify({ ...board, act_id: actId, story_brief: storyBrief }),
    });
    state.detail = result.project || state.detail;
    addIdeaHandoff({
      kind: "act_autopilot",
      title: `${result.act_id || actId} → 远程总控`,
      path: result.packet_path || "",
      text: result.handoff_text || "",
    });
    renderAll();
    toast("远程总控分析卡已生成 / Act autopilot handoff ready");
  });
}

async function createProjectBibleAnalysisHandoff() {
  if (!state.detail) return;
  await runAction("生成设定卡 / Build settings cards", async () => {
    const board = collectIdeaBoardFromDom();
    const result = await persistIdeaBoard(board, { toast: false, render: false });
    const savedBoard = result?.idea_board || board;
    setIdeaBoardLocal(savedBoard);
    addIdeaHandoff({
      kind: "project_bible",
      title: `${savedBoard.story_title || "Project"} → 生成设定卡`,
      text: buildProjectBibleAnalysisHandoff(savedBoard),
    });
    renderIdeaLab();
    toast("已自动保存并生成设定卡交接卡 / Saved and settings handoff ready");
  });
}

async function createIdeaImagePacket() {
  if (!state.selectedSlug || !state.detail) return;
  await runAction("生成图片包 / Image packet", async () => {
    const board = collectIdeaBoardFromDom();
    const result = await requestJson(`/api/projects/${state.selectedSlug}/idea-image-packet`, {
      method: "POST",
      body: JSON.stringify(board),
    });
    state.detail = result.project || state.detail;
    addIdeaHandoff({
      kind: "image_batch",
      title: `${result.task_count || 0} 张分镜图 → Codex 生图`,
      path: result.packet_path || "",
      text: result.handoff_text || "",
    });
    toast("已自动保存并生成图片包 / Saved and image packet ready");
    renderAll();
  });
}

function collectVisibleCardTargets() {
  if (isProjectBibleSelected()) {
    return Array.from(document.querySelectorAll(".project-bible-card"))
      .filter((card) => card.querySelector('[data-bible-field="image_selected"]')?.checked)
      .map((card) => ({
        card_type: "concept",
        card_id: card.querySelector('[data-bible-field="card_id"]')?.value || "",
      }))
      .filter((target) => target.card_id);
  }
  return Array.from(document.querySelectorAll(".idea-shot-row"))
    .filter((row) => row.querySelector('[data-idea-field="selected"]')?.checked)
    .map((row) => ({
      card_type: "storyboard",
      card_uid: row.dataset.cardUid || "",
      item_id: row.querySelector('[data-idea-field="item_id"]')?.value || "",
    }))
    .filter((target) => target.item_id);
}

function referenceLooksLikeWhitebox(ref) {
  const text = [
    ref?.kind,
    ref?.role,
    ref?.asset_id,
    ref?.asset_ref,
    ref?.path,
    ref?.note,
    ref?.generation_guidance,
  ].join(" ").toLowerCase();
  return text.includes("whitebox") || text.includes("白模") || text.includes("previs") || text.includes("blender");
}

function storyboardRowNeedsWhitebox(row) {
  const text = [
    row.item_id,
    row.beat,
    row.shot_type,
    row.frame_description,
    row.spatial_logic,
    row.image_prompt,
    row.video_prompt,
    row.notes,
    row.revision_note,
  ].join(" ").toLowerCase();
  const keywords = [
    "街机",
    "真人快打",
    "游戏机",
    "屏幕",
    "操作位",
    "投币",
    "并排",
    "背后",
    "后脑",
    "脑袋后",
    "对战",
    "围观",
    "空间关系",
    "机位",
    "道具锁",
    "arcade",
    "cabinet",
    "screen",
    "coin slot",
    "side-by-side",
    "over-the-shoulder",
    "behind the heads",
    "spatial",
  ];
  return keywords.some((keyword) => text.includes(keyword));
}

function rowHasWhiteboxContext(row, board = currentIdeaBoard()) {
  const rowRefs = Array.isArray(row.references) ? row.references : [];
  const globalRefs = Array.isArray(board.global_references) ? board.global_references : [];
  const bibleRefs = (board.project_bible || [])
    .filter((card) => card?.selected !== false)
    .flatMap((card) => Array.isArray(card.references) ? card.references : []);
  return [...rowRefs, ...globalRefs, ...bibleRefs].some(referenceLooksLikeWhitebox);
}

function whiteboxPreflightIssues(board, targets) {
  const targetIds = new Set(
    targets
      .filter((target) => (target.card_type || target.type) === "storyboard")
      .map((target) => target.item_id || target.card_id || "")
      .filter(Boolean),
  );
  if (!targetIds.size) return [];
  return (board.rows || [])
    .filter((row) => targetIds.has(row.item_id || ""))
    .filter((row) => storyboardRowNeedsWhitebox(row) && !rowHasWhiteboxContext(row, board))
    .map((row) => `${row.item_id || ""} ${row.beat || row.frame_description || ""}`.trim());
}

async function requestCardImagePreflight(board, targets) {
  if (!state.selectedSlug) return null;
  return requestJson(`/api/projects/${state.selectedSlug}/card-image-preflight`, {
    method: "POST",
    body: JSON.stringify({ ...board, targets }),
  });
}

function cardImagePreflightMessage(preflight = {}) {
  const summary = preflight.summary || {};
  const lines = [
    `状态 / Status: ${preflight.status || "unknown"}`,
    `目标 / Targets: ${preflight.target_count || 0}`,
    `可直接生成 / Ready: ${summary.ready || 0}`,
    `缺白模 / Whitebox missing: ${summary.whitebox_missing || 0}`,
    `连续性锁 / Continuity locks: ${summary.continuity_locks || 0}`,
    `缺连续性锁 / Continuity missing: ${summary.continuity_missing || 0}`,
    `缺提示词 / Prompt gaps: ${summary.prompt_gaps || 0}`,
    `重复编号 / Duplicate IDs: ${summary.duplicate_item_ids || 0}`,
    `找不到目标 / Unresolved: ${summary.unresolved_targets || 0}`,
  ];
  if ((preflight.duplicate_item_ids || []).length) {
    lines.push("", `重复编号: ${(preflight.duplicate_item_ids || []).join(", ")}`);
  }
  if ((preflight.prompt_gaps || []).length) {
    lines.push("", "缺提示词:");
    (preflight.prompt_gaps || []).slice(0, 8).forEach((item) => lines.push(`- ${item.item_id || ""} ${item.beat || ""}`.trim()));
  }
  if ((preflight.missing_whitebox || []).length) {
    lines.push("", "建议先补白模:");
    (preflight.missing_whitebox || []).slice(0, 10).forEach((item) => lines.push(`- ${item.item_id || ""} ${item.beat || ""}`.trim()));
  }
  if ((preflight.missing_continuity || []).length) {
    lines.push("", "建议先补连续性参考:");
    (preflight.missing_continuity || []).slice(0, 10).forEach((item) => {
      const missing = (item.continuity_missing || []).map((entry) => entry.anchor_label || entry.anchor_id).filter(Boolean).join(" / ");
      lines.push(`- ${item.item_id || ""} ${item.beat || ""}${missing ? ` · ${missing}` : ""}`.trim());
    });
  }
  return lines.join("\n");
}

function cardImagePreflightHandoffText(preflight = {}) {
  return [
    "# Card Image Preflight / 生成前检查",
    "",
    "这张卡只记录生成前检查结果，不生成图片。",
    "",
    "```json",
    JSON.stringify(preflight, null, 2),
    "```",
  ].join("\n");
}

async function runVisibleCardImagePreflight() {
  if (!state.selectedSlug || !state.detail) return;
  await runAction("生成前检查 / Card image preflight", async () => {
    const board = collectIdeaBoardFromDom();
    const targets = collectVisibleCardTargets();
    if (!targets.length) {
      toast("请先勾选要检查的卡片 / Select cards first");
      return;
    }
    const preflight = await requestCardImagePreflight(board, targets);
    addIdeaHandoff({
      kind: "preflight",
      status: preflight?.status || "",
      title: `生成前检查 · ${preflight?.target_count || 0} 张卡`,
      message: cardImagePreflightMessage(preflight).split("\n").slice(0, 3).join(" · "),
      text: cardImagePreflightHandoffText(preflight),
    });
    toast(`生成前检查完成 / Preflight: ${preflight?.status || "unknown"}`);
    renderIdeaLab();
  });
}

async function createCardImagePacket(singleTarget = null) {
  if (!state.selectedSlug || !state.detail) return;
  await runAction("生成电影卡片图片包 / Film card image packet", async () => {
    const board = collectIdeaBoardFromDom();
    const targets = singleTarget ? [singleTarget] : collectVisibleCardTargets();
    if (!targets.length) {
      toast("请先勾选要生成的卡片 / Select target cards first");
      return;
    }
    const preflight = await requestCardImagePreflight(board, targets);
    if (preflight?.status === "blocked") {
      window.alert(`生成前检查未通过，请先修复：\n\n${cardImagePreflightMessage(preflight)}`);
      addIdeaHandoff({
        kind: "preflight_blocked",
        status: "blocked",
        title: "生成前检查未通过 / Preflight blocked",
        message: "存在重复编号、空提示词或找不到目标卡。",
        text: cardImagePreflightHandoffText(preflight),
      });
      renderIdeaLab();
      return;
    }
    if (preflight?.status === "review") {
      const proceed = window.confirm(`${cardImagePreflightMessage(preflight)}\n\n确定：继续生成探索图。取消：先打开白模入口。`);
      if (!proceed) {
        openWhiteboxLab();
        return;
      }
    }
    await createCardImagePacketForTargets(board, targets, "card_image", "请先勾选要生成的卡片 / Select target cards first");
  });
}

async function createCardImagePacketForTargets(board, targets, kind = "card_image", emptyMessage = "没有可生成的卡片 / No target cards") {
  if (!targets.length) {
    toast(emptyMessage);
    return null;
  }
  const result = await requestJson(`/api/projects/${state.selectedSlug}/card-image-packet`, {
    method: "POST",
    body: JSON.stringify({ ...board, targets, packet_kind: kind }),
  });
  state.detail = result.project || state.detail;
  addIdeaHandoff({
    kind,
    title: `${result.task_count || 0} 张电影卡片 → Codex 生图`,
    path: result.packet_path || "",
    text: result.handoff_text || "",
  });
  toast("已自动保存并生成图片包 / Image packet ready");
  renderAll();
  return result;
}

function qaRepairDirective(version) {
  const qa = version?.qa && typeof version.qa === "object" ? version.qa : {};
  const score = qa.score;
  const suggestions = Array.isArray(qa.suggestions) ? qa.suggestions : [];
  if (score === undefined || score === null || score === "") {
    return [
      "QA repair / 技术修复：当前主版本尚未质检，重新生成时优先保证干净、稳定、高清。",
      "Add: clean high-resolution key image, crisp edges, readable silhouettes, no sensor noise, no dirty texture, balanced exposure.",
    ].join("\n");
  }
  return [
    `QA repair / 技术修复：当前主版本技术分 ${score}/100，需要重新生成一个更稳定的版本。`,
    ...suggestions.map((item) => `- ${item}`),
    "Preserve the card intent, references, characters, scene continuity, and composition unless the revision note says otherwise.",
  ].join("\n");
}

function repairTargetsFromVisibleQa(board) {
  return visibleCardsForBatchQa(board)
    .map((item) => ({ ...item, version: currentVersionForQa(item.target) }))
    .filter((item) => {
      if (!item.version?.output_path) return false;
      const rawScore = item.version.qa?.score;
      const score = Number(rawScore);
      return rawScore === undefined || rawScore === null || rawScore === "" || !Number.isFinite(score) || score < 82;
    })
    .map((item) => {
      item.target.revision_note = [item.target.revision_note || "", qaRepairDirective(item.version)].filter(Boolean).join("\n\n");
      if (item.cardType === "concept") {
        return { card_type: "concept", card_id: item.target.card_id || "" };
      }
      return { card_type: "storyboard", item_id: item.target.item_id || "" };
    })
    .filter((target) => target.card_id || target.item_id);
}

async function createQaRepairPacket() {
  if (!state.selectedSlug || !state.detail) return;
  await runAction("生成低分修复包 / QA repair packet", async () => {
    const board = collectIdeaBoardFromDom();
    const targets = repairTargetsFromVisibleQa(board);
    await createCardImagePacketForTargets(board, targets, "qa_repair_image", "当前可见卡片没有低分或未质检主版本 / No visible QA issues");
  });
}

function currentVersionPackageScope() {
  const assets = allBoardImageAssets();
  return currentImageLibraryFilters(assets).scope;
}

function videoReferenceGateLabel(gate = {}) {
  const status = gate.status || "";
  if (status === "ready") return "QA READY";
  if (status === "blocked") return "QA BLOCKED";
  if (status === "review") return "QA REVIEW";
  if (status === "reference_review") return "REF REVIEW";
  return "QA CHECK";
}

function videoReferenceGateMessage(gate = {}) {
  const currentIssues = Number(gate.current_issues || 0);
  const referenceIssues = Number(gate.reference_issues || 0);
  if (gate.status === "ready") return "Final 图包已生成，Final 图均达 QA OK / Final assets are QA OK";
  if (gate.status === "blocked") {
    return `Final 图包已生成，但 ${currentIssues} 张 Final 图未质检或低分；建议先批量质检/低分修复 / ${currentIssues} final assets need QA or repair`;
  }
  if (gate.status === "review") {
    return `Final 图包已生成，但 ${currentIssues} 张 Final 图需复核 / ${currentIssues} final assets need review`;
  }
  if (gate.status === "reference_review") {
    return `采用图包已生成，${referenceIssues} 张辅助参考需复核 / ${referenceIssues} reference assets need review`;
  }
  return "已生成 Final 图包 / Final version package ready";
}

async function createCurrentVersionPackage() {
  if (!state.selectedSlug || !state.detail) return;
  await runAction("生成 Final 图包 / Final version package", async () => {
    const board = collectIdeaBoardFromDom();
    await persistIdeaBoard(board, { toast: false, render: false });
    const scene = selectedScene();
    const scope = currentVersionPackageScope();
    const result = await requestJson(`/api/projects/${state.selectedSlug}/current-version-package`, {
      method: "POST",
      body: JSON.stringify({
        scope,
        scene_id: scene?.scene_id || "",
        act_id: activeStoryActId() || scene?.act_id || "",
      }),
    });
    state.detail = result.project || state.detail;
    const gate = result.quality_gate || {};
    addIdeaHandoff({
      kind: "video_reference_package",
      status: gate.status || "",
      message: videoReferenceGateMessage(gate),
      title: `${videoReferenceGateLabel(gate)} · ${result.current_count || 0} Final · ${result.reference_count || 0} 参考 → 视频参考图包`,
      path: result.package_path || "",
      text: result.handoff_text || "",
    });
    toast(videoReferenceGateMessage(gate));
    renderAll();
  });
}

async function createVideoUploadPackage() {
  if (!state.selectedSlug || !state.detail) return;
  await runAction("生成视频上传包 / Video upload package", async () => {
    const board = collectIdeaBoardFromDom();
    await persistIdeaBoard(board, { toast: false, render: false });
    const actId = activeStoryActId() || board.acts?.[0]?.act_id || "";
    const result = await requestJson(`/api/projects/${state.selectedSlug}/video-upload-package`, {
      method: "POST",
      body: JSON.stringify({ act_id: actId }),
    });
    state.detail = result.project || state.detail;
    const missing = Number(result.missing_count || 0);
    const message = missing
      ? `视频上传包已生成：${result.image_count || 0} 张图片，${missing} 张缺图 / Video upload package ready with missing images`
      : `视频上传包已生成：${result.image_count || 0} 张图片 / Video upload package ready`;
    addIdeaHandoff({
      kind: "video_upload_package",
      status: missing ? "missing_images" : "ready",
      message,
      title: `${result.act_id || actId} · ${result.image_count || 0} 张图 → 视频上传包`,
      path: result.package_path || "",
      imageFolder: result.image_package_dir || result.images_dir || "",
      codexCompletionNote: false,
      text: result.clipboard_text || result.handoff_text || "",
    });
    toast(`${message} · ${result.image_package_dir || result.images_dir || ""}`);
    renderAll();
  });
}

async function createIdeaBoardPackageForScope(scope) {
  if (!state.selectedSlug || !state.detail) return;
  const isActPackage = scope === "act";
  await runAction(isActPackage ? "生成幕总包 / Act package" : "生成创意总包 / Idea board package", async () => {
    const board = collectIdeaBoardFromDom();
    await persistIdeaBoard(board, { toast: false, render: false });
    const actId = activeStoryActId() || board.acts?.[0]?.act_id || "";
    if (isActPackage && !actId) {
      toast("没有可打包的当前幕 / No current act to package");
      return;
    }
    const result = await requestJson(`/api/projects/${state.selectedSlug}/idea-board-package`, {
      method: "POST",
      body: JSON.stringify(isActPackage ? { scope: "act", act_id: actId } : { scope: "all" }),
    });
    state.detail = result.project || state.detail;
    const missing = Number(result.missing_count || 0);
    const label = isActPackage ? "幕总包" : "创意总包";
    const labelEn = isActPackage ? "Act package" : "Idea package";
    const message = missing
      ? `${label}已生成：${result.row_count || 0} 条，${result.image_count || 0} 张图片，${missing} 条缺图 / ${labelEn} ready with missing images`
      : `${label}已生成：${result.row_count || 0} 条，${result.image_count || 0} 张图片 / ${labelEn} ready`;
    addIdeaHandoff({
      kind: isActPackage ? "act_board_package" : "idea_board_package",
      status: missing ? "missing_images" : "ready",
      message,
      title: isActPackage
        ? `${result.act_id || actId} · ${result.row_count || 0} 条 · ${result.image_count || 0} 张图 → 幕总包`
        : `${result.row_count || 0} 条 · ${result.image_count || 0} 张图 → 创意总包`,
      path: result.package_path || "",
      openFolder: result.package_dir || "",
      openFolderLabel: isActPackage ? "打开幕总包 / Open Act Pack" : "打开创意总包 / Open Idea Pack",
      imageFolder: result.image_package_dir || result.images_dir || "",
      codexCompletionNote: false,
      text: result.clipboard_text || result.handoff_text || "",
    });
    toast(`${message} · ${result.package_dir || ""}`);
    renderAll();
  });
}

async function createIdeaBoardPackage() {
  await createIdeaBoardPackageForScope("all");
}

async function createActBoardPackage() {
  await createIdeaBoardPackageForScope("act");
}

function setVisibleCardSelection(checked) {
  if (isProjectBibleSelected()) {
    document.querySelectorAll('.project-bible-card [data-bible-field="image_selected"]').forEach((input) => {
      input.checked = checked;
    });
  } else {
    document.querySelectorAll('.idea-shot-row [data-idea-field="selected"]').forEach((input) => {
      input.checked = checked;
    });
  }
  setIdeaBoardLocal(collectIdeaBoardFromDom());
  renderIdeaLab();
}

function addIdeaAct() {
  const board = collectIdeaBoardFromDom();
  board.acts = Array.isArray(board.acts) ? board.acts : [];
  const nextAct = {
    act_id: nextIdeaActId(board.acts),
    title: "",
    summary: "",
    dramatic_purpose: "",
    key_beats: "",
    status: "draft",
  };
  board.acts.push(nextAct);
  setIdeaBoardLocal(board);
  selectIdeaAct(nextAct.act_id);
  renderAll();
}

function deleteIdeaAct(index) {
  const board = collectIdeaBoardFromDom();
  board.acts = Array.isArray(board.acts) ? board.acts : [];
  board.acts.splice(index, 1);
  setIdeaBoardLocal(board);
  renderIdeaLab();
}

function addProjectBibleCard(category = "lookdev") {
  const board = collectIdeaBoardFromDom();
  board.project_bible = Array.isArray(board.project_bible) ? board.project_bible : [];
  board.project_bible.push({
    card_id: nextProjectBibleCardId(board.project_bible),
    scope: "project",
    act_id: "",
    category,
    title: "",
    summary: "",
    visual_direction: "",
    prompt_notes: "",
    revision_note: "",
    negative_prompt: "",
    selected: true,
    image_selected: true,
    status: "draft",
    references: [],
    preview_path: "",
    versions: [],
  });
  state.ideaActiveBibleIndex = board.project_bible.length - 1;
  setIdeaBoardLocal(board);
  renderIdeaLab();
}

function deleteProjectBibleCard(index) {
  const board = collectIdeaBoardFromDom();
  board.project_bible = Array.isArray(board.project_bible) ? board.project_bible : [];
  board.project_bible.splice(index, 1);
  state.ideaActiveBibleIndex = clamp(state.ideaActiveBibleIndex, 0, Math.max(0, board.project_bible.length - 1));
  setIdeaBoardLocal(board);
  renderIdeaLab();
}

function addIdeaRow() {
  const board = collectIdeaBoardFromDom();
  const storyActId = activeStoryActId();
  const storyAct = storyActEntryForId(board, storyActId);
  const scene = selectedScene();
  const sceneId = storyAct?.scene_id || scene?.scene_id || defaultSceneIdForAct(board, storyActId) || "";
  const rowActId = scene?.act_id || (storyAct?.source === "custom" ? storyActId : "") || storyActId || "";
  board.rows.push({
    card_uid: newIdeaCardUid(),
    item_id: nextIdeaItemIdForAct(board.rows, storyActId || rowActId || ""),
    act_id: rowActId,
    scene_id: sceneId,
    beat: "",
    shot_type: "",
    frame_description: "",
    linked_cards: [],
    spatial_logic: "",
    image_prompt: "",
    video_prompt: "",
    notes: "",
    revision_note: "",
    sort_after: "",
    selected: true,
    status: "draft",
    output_path: "",
    versions: [],
    references: [],
  });
  state.ideaActiveRowIndex = board.rows.length - 1;
  setIdeaBoardLocal(board);
  renderIdeaLab();
}

function insertIdeaRowAfter(index) {
  const board = collectIdeaBoardFromDom();
  const baseRow = board.rows?.[index];
  if (!baseRow) return;
  const linkedId = baseRow.item_id || "";
  const parsedLinkedId = parseRenumberableShotId(linkedId);
  const insertedId = parsedLinkedId
    ? `${parsedLinkedId.prefix}${String(parsedLinkedId.number + 1).padStart(parsedLinkedId.width, "0")}`
    : nextIdeaItemIdForAct(board.rows, baseRow.act_id || activeStoryActId() || "");
  const newRow = {
    card_uid: newIdeaCardUid(),
    item_id: insertedId,
    act_id: baseRow.act_id || "",
    scene_id: baseRow.scene_id || "",
    beat: "",
    shot_type: "",
    frame_description: "",
    linked_cards: linkedId ? [linkedId] : [],
    spatial_logic: "",
    image_prompt: "",
    video_prompt: "",
    notes: "",
    revision_note: "",
    sort_after: linkedId,
    selected: true,
    status: "draft",
    output_path: "",
    output_notes: "",
    versions: [],
    references: [],
  };
  board.rows.splice(index + 1, 0, newRow);
  renumberRowsAfterInsert(board, index, baseRow);
  state.ideaBatchRows = (state.ideaBatchRows || []).map((item) => (Number(item) > index ? Number(item) + 1 : Number(item)));
  state.ideaActiveRowIndex = index + 1;
  setIdeaBoardLocal(board);
  renderIdeaLab();
  document.querySelector(`.idea-shot-row[data-idea-index="${state.ideaActiveRowIndex}"]`)?.scrollIntoView({ behavior: "smooth", block: "center" });
}

function insertIdeaRowBefore(index) {
  const board = collectIdeaBoardFromDom();
  const baseRow = board.rows?.[index];
  if (!baseRow) return;
  const linkedId = baseRow.item_id || "";
  const previousRow = previousRowInInsertScope(board, index, baseRow);
  const parsedLinkedId = parseRenumberableShotId(linkedId);
  const insertedId = parsedLinkedId
    ? linkedId
    : nextIdeaItemIdForAct(board.rows, baseRow.act_id || activeStoryActId() || "");
  const newRow = {
    card_uid: newIdeaCardUid(),
    item_id: insertedId,
    act_id: baseRow.act_id || "",
    scene_id: baseRow.scene_id || "",
    beat: "",
    shot_type: "",
    frame_description: "",
    linked_cards: linkedId ? [linkedId] : [],
    spatial_logic: "",
    image_prompt: "",
    video_prompt: "",
    notes: "",
    revision_note: "",
    sort_after: previousRow?.item_id || "",
    selected: true,
    status: "draft",
    output_path: "",
    output_notes: "",
    versions: [],
    references: [],
  };
  board.rows.splice(index, 0, newRow);
  renumberRowsBeforeInsert(board, index, baseRow);
  state.ideaBatchRows = (state.ideaBatchRows || []).map((item) => (Number(item) >= index ? Number(item) + 1 : Number(item)));
  state.ideaActiveRowIndex = index;
  setIdeaBoardLocal(board);
  renderIdeaLab();
  document.querySelector(`.idea-shot-row[data-idea-index="${state.ideaActiveRowIndex}"]`)?.scrollIntoView({ behavior: "smooth", block: "center" });
}

function deleteIdeaRow(index) {
  const board = collectIdeaBoardFromDom();
  board.rows.splice(index, 1);
  state.ideaBatchRows = (state.ideaBatchRows || [])
    .filter((item) => Number(item) !== index)
    .map((item) => (Number(item) > index ? Number(item) - 1 : Number(item)));
  ensureIdeaActiveRowForScene(board);
  setIdeaBoardLocal(board);
  renderIdeaLab();
}

function bindDailyIdeaEvents() {
  $("dailyIdeaDateInput")?.addEventListener("change", (event) => selectDailyIdeaDate(event.target.value));
  $("dailyIdeaRefreshBtn")?.addEventListener("click", async () => {
    await refreshDailyIdeas();
    await loadDailyIdeaDetail(state.dailyIdeas.selectedDate || todayDateString());
    renderAll();
    toast("灵感页已刷新 / Daily ideas refreshed");
  });
  $("dailyIdeaOpenFolderBtn")?.addEventListener("click", openDailyIdeaFolder);
  $("dailyIdeaBuildHandoffBtn")?.addEventListener("click", buildDailyIdeaHandoff);
  $("dailyIdeaSeedInput")?.addEventListener("input", (event) => {
    state.dailyIdeas.seed = event.target.value || "";
  });
  $("dailyIdeaHandoffDock")?.querySelector(".daily-clear-handoffs")?.addEventListener("click", (event) => {
    event.preventDefault();
    state.dailyIdeas.handoffs = [];
    saveDailyIdeaHandoffs();
    renderDailyIdeasPage();
  });
  $("dailyIdeaHandoffDock")?.querySelectorAll(".idea-handoff-card").forEach((card) => {
    card.addEventListener("dragstart", (event) => {
      const handoff = state.dailyIdeas.handoffs.find((item) => item.id === card.dataset.dailyHandoffId);
      if (!handoff) return;
      event.dataTransfer?.setData("text/plain", handoff.text || "");
      event.dataTransfer?.setData("text/markdown", handoff.text || "");
      event.dataTransfer?.setData("text/codex-handoff-id", handoff.id || "");
      event.dataTransfer.effectAllowed = "copy";
    });
  });
  $("dailyIdeaHandoffDock")?.querySelectorAll(".daily-copy-handoff").forEach((button) => {
    button.addEventListener("click", async (event) => {
      event.preventDefault();
      event.stopPropagation();
      const handoff = state.dailyIdeas.handoffs.find((item) => item.id === button.dataset.dailyHandoffId);
      if (!handoff) return;
      try {
        await navigator.clipboard.writeText(handoff.text || "");
        toast("已复制每日灵感生产卡 / Daily idea packet copied");
      } catch {
        const textarea = button.closest(".idea-handoff-card")?.querySelector("textarea");
        textarea?.select?.();
        document.execCommand?.("copy");
      }
    });
  });
  $("dailyIdeaHandoffDock")?.querySelectorAll(".daily-delete-handoff").forEach((button) => {
    button.addEventListener("click", (event) => {
      event.preventDefault();
      event.stopPropagation();
      state.dailyIdeas.handoffs = state.dailyIdeas.handoffs.filter((item) => item.id !== button.dataset.dailyHandoffId);
      saveDailyIdeaHandoffs();
      renderDailyIdeasPage();
    });
  });
}

function bindIdeaHandoffEvents() {
  $("ideaHandoffDock")?.querySelector(".idea-clear-handoffs")?.addEventListener("click", (event) => {
    event.preventDefault();
    clearIdeaHandoffs();
    toast("已清空交接卡 / Handoff cards cleared");
  });
  $("ideaHandoffDock")?.querySelectorAll(".idea-handoff-card").forEach((card) => {
    card.addEventListener("dragstart", (event) => {
      const handoff = state.ideaHandoffs.find((item) => item.id === card.dataset.ideaHandoffId);
      if (!handoff) return;
      event.dataTransfer?.setData("text/plain", handoff.text || "");
      event.dataTransfer?.setData("text/markdown", handoff.text || "");
      event.dataTransfer?.setData("text/codex-handoff-id", handoff.id || "");
      event.dataTransfer.effectAllowed = "copy";
    });
  });
  $("ideaHandoffDock")?.querySelectorAll(".idea-copy-handoff").forEach((button) => {
    button.addEventListener("click", async (event) => {
      event.preventDefault();
      event.stopPropagation();
      const handoff = state.ideaHandoffs.find((item) => item.id === button.dataset.ideaHandoffId);
      if (!handoff) return;
      try {
        await navigator.clipboard.writeText(handoff.text || "");
        toast("已复制交接卡 / Handoff copied");
      } catch {
        const textarea = button.closest(".idea-handoff-card")?.querySelector("textarea");
        textarea?.select?.();
        document.execCommand?.("copy");
      }
    });
  });
  $("ideaHandoffDock")?.querySelectorAll(".idea-open-image-folder").forEach((button) => {
    button.addEventListener("click", async (event) => {
      event.preventDefault();
      event.stopPropagation();
      const handoff = state.ideaHandoffs.find((item) => item.id === button.dataset.ideaHandoffId);
      const folder = handoff?.openFolder || handoff?.imageFolder || "";
      if (!folder || !state.selectedSlug) return;
      try {
        await requestJson(`/api/projects/${state.selectedSlug}/open-project-path`, {
          method: "POST",
          body: JSON.stringify({ path: folder }),
        });
        toast("已打开位置 / Folder opened");
      } catch (error) {
        toast(error?.message || "打开位置失败 / Failed to open folder");
      }
    });
  });
  $("ideaHandoffDock")?.querySelectorAll(".idea-delete-handoff").forEach((button) => {
    button.addEventListener("click", (event) => {
      event.preventDefault();
      event.stopPropagation();
      state.ideaHandoffs = state.ideaHandoffs.filter((item) => item.id !== button.dataset.ideaHandoffId);
      saveIdeaHandoffs();
      syncIdeaHandoffCompletionPolling();
      renderIdeaLab();
    });
  });
}

function bindIdeaLabEvents() {
  $("projectBibleBuildHandoffBtn")?.addEventListener("click", createProjectBibleAnalysisHandoff);
  $("projectBibleAddCardBtn")?.addEventListener("click", () => addProjectBibleCard());
  $("cardBuildImagePacketBtn")?.addEventListener("click", () => createCardImagePacket());
  $("currentVersionPackageBtn")?.addEventListener("click", createCurrentVersionPackage);
  $("ideaBoardPackageBtn")?.addEventListener("click", createIdeaBoardPackage);
  $("actBoardPackageBtn")?.addEventListener("click", createActBoardPackage);
  $("videoUploadPackageBtn")?.addEventListener("click", createVideoUploadPackage);
  $("batchVersionQaBtn")?.addEventListener("click", runVisibleCardVersionQa);
  $("qaRepairPacketBtn")?.addEventListener("click", createQaRepairPacket);
  $("cardSelectVisibleBtn")?.addEventListener("click", () => setVisibleCardSelection(true));
  $("cardClearVisibleBtn")?.addEventListener("click", () => setVisibleCardSelection(false));
  $("cardFilterScope")?.addEventListener("change", (event) => {
    state.cardFilters.scope = event.target.value || defaultCardFilterScope(isProjectBibleSelected() ? "concept" : "storyboard");
    const board = collectIdeaBoardFromDom();
    setIdeaBoardLocal(board);
    renderIdeaLab();
  });
  $("cardFilterTag")?.addEventListener("change", (event) => {
    state.cardFilters.tag = event.target.value || "all";
    const board = collectIdeaBoardFromDom();
    setIdeaBoardLocal(board);
    renderIdeaLab();
  });
  $("cardFilterMode")?.addEventListener("change", (event) => {
    state.cardFilters.mode = event.target.value || "all";
    const board = collectIdeaBoardFromDom();
    setIdeaBoardLocal(board);
    renderIdeaLab();
  });
  $("cardFilterQuery")?.addEventListener("input", (event) => {
    state.cardFilters.query = event.target.value || "";
    const board = collectIdeaBoardFromDom();
    setIdeaBoardLocal(board);
    renderIdeaLab();
  });
  $("cardFilterClearBtn")?.addEventListener("click", () => {
    state.cardFilters = {
      scope: defaultCardFilterScope(isProjectBibleSelected() ? "concept" : "storyboard"),
      tag: "all",
      mode: "all",
      query: "",
    };
    const board = collectIdeaBoardFromDom();
    setIdeaBoardLocal(board);
    renderIdeaLab();
  });
  $("ideaBuildActsBtn")?.addEventListener("click", createIdeaActsHandoff);
  $("ideaBuildStoryboardCardsBtn")?.addEventListener("click", createIdeaStoryboardCardsHandoff);
  $("actAutopilotBtn")?.addEventListener("click", createActAutopilotPacket);
  $("ideaWhiteboxBtn")?.addEventListener("click", openWhiteboxLab);
  $("cardPreflightBtn")?.addEventListener("click", runVisibleCardImagePreflight);
  $("ideaSaveBtn")?.addEventListener("click", () => saveIdeaBoard());
  document.querySelectorAll(".idea-add-act").forEach((button) => button.addEventListener("click", addIdeaAct));
  $("ideaAddRowBtn")?.addEventListener("click", addIdeaRow);
  $("ideaBuildImagePacketBtn")?.addEventListener("click", createIdeaImagePacket);
  document.querySelectorAll(".card-version-preview-link").forEach((link) => {
    link.addEventListener("click", handleCardVersionPreviewClick);
  });
  document.querySelectorAll(".card-version-to-board").forEach((button) => {
    button.addEventListener("click", () => sendVersionImageToBoard(button.dataset.versionPath || ""));
  });
  document.querySelectorAll(".card-version-status").forEach((button) => {
    button.addEventListener("click", () => updateCardVersionStatus(button));
  });
  document.querySelectorAll(".card-version-qa-run").forEach((button) => {
    button.addEventListener("click", () => runCardVersionQa(button));
  });
  document.querySelectorAll(".card-generate-one").forEach((button) => {
    button.addEventListener("click", () => {
      const type = button.dataset.cardType || "";
      if (type === "concept") {
        const card = button.closest(".project-bible-card");
        const cardId = card?.querySelector('[data-bible-field="card_id"]')?.value || button.dataset.cardId || "";
        createCardImagePacket({ card_type: "concept", card_id: cardId });
      } else if (type === "storyboard") {
        const row = button.closest(".idea-shot-row");
        const itemId = row?.querySelector('[data-idea-field="item_id"]')?.value || button.dataset.cardId || "";
        createCardImagePacket({ card_type: "storyboard", card_uid: row?.dataset.cardUid || "", item_id: itemId });
      }
    });
  });
  $("ideaActiveRowSelect")?.addEventListener("change", (event) => {
    state.ideaActiveRowIndex = Number(event.target.value || 0);
    const board = collectIdeaBoardFromDom();
    setIdeaBoardLocal(board);
    renderIdeaLab();
  });
  $("ideaRefActFilter")?.addEventListener("change", (event) => {
    setImageLibraryFilters({ scope: event.target.value || "all" }, allBoardImageAssets().filter((asset) => frameIsUsable(asset)));
    const board = collectIdeaBoardFromDom();
    setIdeaBoardLocal(board);
    renderIdeaLab();
  });
  $("ideaRefTagFilter")?.addEventListener("change", (event) => {
    setImageLibraryFilters({ tag: event.target.value || "all" }, allBoardImageAssets().filter((asset) => frameIsUsable(asset)));
    const board = collectIdeaBoardFromDom();
    setIdeaBoardLocal(board);
    renderIdeaLab();
  });
  $("ideaRefSearchInput")?.addEventListener("input", (event) => {
    setImageLibraryFilters({ query: event.target.value || "" }, allBoardImageAssets().filter((asset) => frameIsUsable(asset)));
    refreshIdeaReferenceAssetGrid();
  });
  $("ideaRows")?.querySelectorAll(".idea-focus-row").forEach((button) => {
    button.addEventListener("click", () => {
      state.ideaActiveRowIndex = Number(button.dataset.ideaIndex || 0);
      const board = collectIdeaBoardFromDom();
      setIdeaBoardLocal(board);
      renderIdeaLab();
    });
  });
  $("ideaRows")?.querySelectorAll(".storyboard-canvas-open").forEach((button) => {
    button.addEventListener("click", () => openStoryboardCanvas(Number(button.dataset.ideaIndex || 0)));
  });
  document.querySelectorAll(".idea-map-focus").forEach((button) => {
    button.addEventListener("click", () => {
      state.ideaActiveRowIndex = Number(button.dataset.ideaIndex || 0);
      const board = collectIdeaBoardFromDom();
      setIdeaBoardLocal(board);
      renderIdeaLab();
      document.querySelector(`.idea-shot-row[data-idea-index="${state.ideaActiveRowIndex}"]`)?.scrollIntoView({ behavior: "smooth", block: "center" });
    });
  });
  document.querySelectorAll(".idea-batch-check").forEach((checkbox) => {
    checkbox.addEventListener("change", () => {
      const index = Number(checkbox.dataset.ideaIndex || 0);
      const set = new Set(state.ideaBatchRows || []);
      if (checkbox.checked) set.add(index);
      else set.delete(index);
      state.ideaBatchRows = [...set].sort((a, b) => a - b);
      const board = collectIdeaBoardFromDom();
      setIdeaBoardLocal(board);
      renderIdeaLab();
    });
  });
  $("ideaRows")?.querySelectorAll(".idea-delete-row").forEach((button) => {
    button.addEventListener("click", () => deleteIdeaRow(Number(button.dataset.ideaIndex || 0)));
  });
  $("ideaRows")?.querySelectorAll(".idea-insert-row-before").forEach((button) => {
    button.addEventListener("click", () => insertIdeaRowBefore(Number(button.dataset.ideaIndex || 0)));
  });
  $("ideaRows")?.querySelectorAll(".idea-insert-row-after").forEach((button) => {
    button.addEventListener("click", () => insertIdeaRowAfter(Number(button.dataset.ideaIndex || 0)));
  });
  document.querySelectorAll(".idea-delete-act").forEach((button) => {
    button.addEventListener("click", () => deleteIdeaAct(Number(button.dataset.ideaActIndex || 0)));
  });
  document.querySelectorAll(".project-bible-focus, .project-bible-map-item").forEach((button) => {
    button.addEventListener("click", () => {
      state.ideaActiveBibleIndex = Number(button.dataset.bibleIndex || 0);
      const board = collectIdeaBoardFromDom();
      setIdeaBoardLocal(board);
      renderIdeaLab();
      document.querySelector(`.project-bible-card[data-bible-index="${state.ideaActiveBibleIndex}"]`)?.scrollIntoView({ behavior: "smooth", block: "center" });
    });
  });
  document.querySelectorAll(".project-bible-delete").forEach((button) => {
    button.addEventListener("click", () => deleteProjectBibleCard(Number(button.dataset.bibleIndex || 0)));
  });
  document.querySelectorAll(".project-bible-card").forEach((card) => {
    card.addEventListener("dragover", (event) => {
      const types = Array.from(event.dataTransfer?.types || []);
      if (!types.includes("application/x-pipeline-asset-ref") && !types.includes("text/plain")) return;
      event.preventDefault();
      card.classList.add("drop-target");
    });
    card.addEventListener("dragleave", () => card.classList.remove("drop-target"));
    card.addEventListener("drop", (event) => {
      event.preventDefault();
      card.classList.remove("drop-target");
      const assetRef = event.dataTransfer?.getData("application/x-pipeline-asset-ref") || event.dataTransfer?.getData("text/plain") || "";
      const index = Number(card.dataset.bibleIndex || 0);
      if (assetRef) addIdeaReference("bible", assetRef, [index]);
    });
  });
  document.querySelectorAll(".idea-shot-row, .idea-map-row").forEach((row) => {
    row.addEventListener("dragover", (event) => {
      const types = Array.from(event.dataTransfer?.types || []);
      if (!types.includes("Files") && !types.includes("application/x-pipeline-asset-ref") && !types.includes("text/plain")) return;
      event.preventDefault();
      event.dataTransfer.dropEffect = types.includes("Files") ? "copy" : "link";
      row.classList.add("drop-target");
    });
    row.addEventListener("dragleave", () => row.classList.remove("drop-target"));
    row.addEventListener("drop", async (event) => {
      event.preventDefault();
      row.classList.remove("drop-target");
      const files = [...(event.dataTransfer?.files || [])].filter(fileIsImage);
      if (files.length) {
        try {
          await uploadDroppedStoryboardVersion(row, files[0]);
        } catch (error) {
          toast(`导入备选图失败 / Import failed: ${error.message}`);
        }
        return;
      }
      const assetRef = event.dataTransfer?.getData("application/x-pipeline-asset-ref") || event.dataTransfer?.getData("text/plain") || "";
      const index = Number(row.dataset.ideaIndex || 0);
      if (assetRef) addIdeaReference("row", assetRef, [index]);
    });
  });
  bindIdeaReferenceAssetButtons();
  document.querySelectorAll(".idea-remove-ref").forEach((button) => {
    button.addEventListener("click", () => removeIdeaReference(button.dataset.refScope || "row", button.dataset.refKey || "", button.dataset.ideaIndex || null));
  });
  document.querySelectorAll(".idea-ref-note").forEach((textarea) => {
    textarea.addEventListener("input", () => updateIdeaReferenceNote(textarea.dataset.refScope || "row", textarea.dataset.refKey || "", textarea.value));
  });
  bindIdeaHandoffEvents();
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
        <button class="qa-repair-button ${recommended.has(key) ? "recommended" : ""}" data-help="${escapeHtml(intent.directive)}" data-repair-key="${escapeHtml(key)}" type="button">
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
  let scene = selectedScene();
  if (!scene && isIdeaActSelected()) {
    const board = currentIdeaBoard();
    const actId = activeStoryActId();
    const actTitle = storyActEntryForId(board, actId)?.title || actId;
    scene = {
      scene_id: "",
      scene_slug: "",
      title: actTitle,
      act_id: actId,
      act_title: actTitle,
      shot_ids: [],
      primary_steps: [],
      resource_manifest: {},
      version_registry: {},
      change_requests: [],
      review_log: {},
      snapshots: [],
    };
  }
  const stageOptions = storyboardStageOptions(scene);
  if (!stageOptions.some((option) => option.value === state.storyboardStage)) state.storyboardStage = "final";
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
        <ol class="workflow-steps">
          <li><strong>01</strong><span>选幕</span></li>
          <li><strong>02</strong><span>看最终分镜大图</span></li>
          <li><strong>03</strong><span>标注/质检/修图</span></li>
          <li><strong>04</strong><span>待定区查废图和白模</span></li>
        </ol>
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
            .map((option) => `<button class="studio-stage-filter ${state.storyboardStage === option.value ? "active" : ""}" data-help="${escapeHtml(option.help || "切换当前图片页显示范围。")}" data-stage="${escapeHtml(option.value)}" type="button">${escapeHtml(option.label)}</button>`)
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
                  <button class="decision-button use ${annotation.status === "use" ? "active" : ""}" data-help="标记这张图后续要参考或采用。" data-status="use" type="button">✓</button>
                  <button class="decision-button reject ${annotation.status === "reject" ? "active" : ""}" data-help="标记这张图不要用于后续参考。" data-status="reject" type="button">×</button>
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
                <button id="buildFixPromptBtn" class="command-button primary" data-help="根据当前图、导演备注、关联参考和质检结果，生成一段更适合重生成的提示词。" type="button">生成修正版提示词 / Build Fix Prompt</button>
                <textarea id="fixPromptOutput" rows="9" placeholder="点击上方按钮生成 / Click the button above"></textarea>
                <button id="createFramePacketBtn" class="command-button primary" data-help="把当前图和修图提示词打包成可交给 Codex 生图并回填的任务包。" type="button">生成任务包 / Build Generation Packet</button>
                <button id="createFrameChangeRequestBtn" class="command-button" data-help="只在项目里记录这次修改会影响哪些资产，不生成生图包。" type="button">仅写入影响表 / Impact Only</button>
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
      selectScene(button.dataset.sceneId || "");
      renderAll();
    });
  });
  root.querySelectorAll(".studio-stage-filter").forEach((button) => {
    button.addEventListener("click", () => {
      state.storyboardStage = button.dataset.stage || "final";
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
      selectScene(button.dataset.sceneId || "");
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
  if (scene && state.recreate?.sceneId === scene.scene_id) {
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
  if (!scene) {
    $("sceneStepLanes").innerHTML = `
      <div class="empty-state">
        当前正在编辑设定 / Settings。场景资源筛选会在选择具体幕或场景后显示。
      </div>
    `;
    return;
  }
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

function setDailyIdeasWorkspaceVisible(active) {
  const dailyPage = $("dailyIdeasPage");
  if (dailyPage) dailyPage.hidden = !active;
  ["ideaLab", "storyboardStudio"].forEach((id) => {
    const element = $(id);
    if (element) element.hidden = active;
  });
  const toolbox = document.querySelector(".toolbox-panel");
  if (toolbox) toolbox.hidden = active;
}

function renderAll() {
  if (isExternalRetouchPage()) {
    renderProjects();
    renderHeader();
    renderExternalRetouchLab();
    renderReferenceBoard();
    return;
  }
  setDailyIdeasWorkspaceVisible(Boolean(state.dailyIdeasOpen));
  if (state.dailyIdeasOpen) {
    renderProjects();
    renderSidebarSceneNavigator();
    renderHeader();
    renderDailyIdeasPage();
    renderRecycleBinPage();
    return;
  }
  renderProjects();
  renderSidebarSceneNavigator();
  renderHeader();
  renderIdeaLab();
  renderStoryboardStudio();
  renderExternalRetouchLab();
  renderReferenceBoard();
  renderWhiteboxLab();
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
  await refreshProjectCollections();
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

async function refreshDailyIdeas() {
  const payload = await requestJson("/api/daily-ideas");
  state.dailyIdeas.dates = payload.dates || [];
  if (!state.dailyIdeas.selectedDate) {
    state.dailyIdeas.selectedDate = payload.today || todayDateString();
  }
}

async function loadDailyIdeaDetail(date) {
  const targetDate = date || state.dailyIdeas.selectedDate || todayDateString();
  const detail = await requestJson(`/api/daily-ideas/${encodeURIComponent(targetDate)}`);
  state.dailyIdeas.selectedDate = detail.date || targetDate;
  state.dailyIdeas.detail = detail;
  const parsed = new Date(`${state.dailyIdeas.selectedDate}T00:00:00`);
  if (!Number.isNaN(parsed.getTime())) {
    state.dailyIdeas.calendarYear = parsed.getFullYear();
    state.dailyIdeas.calendarMonth = parsed.getMonth() + 1;
  }
  loadDailyIdeaHandoffs();
}

async function openDailyIdeasPage() {
  await runAction("打开灵感页 / Open inspiration", async () => {
    state.dailyIdeasOpen = true;
    state.recycleBinOpen = false;
    await refreshDailyIdeas();
    await loadDailyIdeaDetail(state.dailyIdeas.selectedDate || todayDateString());
    await refreshDailyIdeas();
    renderAll();
    $("dailyIdeasPage")?.scrollIntoView({ behavior: "smooth", block: "start" });
  });
}

async function selectDailyIdeaDate(date) {
  if (!date) return;
  try {
    state.dailyIdeasOpen = true;
    await loadDailyIdeaDetail(date);
    await refreshDailyIdeas();
    renderAll();
  } catch (error) {
    toast(`读取灵感日期失败 / Failed to load daily idea: ${error.message}`);
  }
}

async function buildDailyIdeaHandoff() {
  const date = state.dailyIdeas.selectedDate || todayDateString();
  const seed = $("dailyIdeaSeedInput")?.value.trim() || "";
  const count = Number($("dailyIdeaCountInput")?.value || 10);
  state.dailyIdeas.seed = seed;
  await runAction("生成今日热点生产卡 / Build daily idea packet", async () => {
    const result = await requestJson(`/api/daily-ideas/${encodeURIComponent(date)}/hotspot-handoff`, {
      method: "POST",
      body: JSON.stringify({ seed, count }),
    });
    state.dailyIdeas.detail = result.daily_idea || state.dailyIdeas.detail;
    addDailyIdeaHandoff({
      title: result.title || `${date} 今日灵感生产卡`,
      text: result.handoff_text || "",
      callbackUrl: result.callback_url || "",
      outputDir: result.output_dir || "",
    });
    toast("今日灵感生产卡已生成并尝试复制 / Daily idea packet ready");
    renderAll();
  });
}

async function openDailyIdeaFolder() {
  const date = state.dailyIdeas.selectedDate || todayDateString();
  try {
    await requestJson(`/api/daily-ideas/${encodeURIComponent(date)}/open-path`, {
      method: "POST",
      body: JSON.stringify({ path: "." }),
    });
    toast("已打开当天灵感目录 / Daily idea folder opened");
  } catch (error) {
    toast(error?.message || "打开目录失败 / Failed to open folder");
  }
}

async function refreshProjectCollections() {
  const [payload, recyclePayload] = await Promise.all([
    requestJson("/api/projects"),
    requestJson("/api/recycle-bin/projects"),
  ]);
  state.projects = payload.projects || [];
  state.recycledProjects = recyclePayload.projects || [];
  if (state.selectedSlug && !state.projects.some((project) => project.slug === state.selectedSlug)) {
    state.selectedSlug = null;
    state.detail = null;
  }
  renderProjects();
  renderRecycleBinPage();
}

async function loadDetail(slug) {
  state.selectedSlug = slug;
  state.selectedDocIndex = 0;
  state.selectedSceneLockIndex = 0;
  state.selectedSceneId = "";
  state.selectedFrameRef = "";
  state.storyboardStage = "final";
  state.referenceSelection = {};
  state.detail = await requestJson(`/api/projects/${encodeURIComponent(slug)}`);
  const firstActId = currentIdeaBoard().acts?.[0]?.act_id || "";
  state.selectedSceneId = firstActId ? ideaActWorkspaceId(firstActId) : "";
  loadBoardState();
  loadIdeaHandoffs();
  pruneCompletedIdeaHandoffs(currentIdeaBoard().completed_handoff_ids || []);
  pruneCompletedBoardHandoffs(currentIdeaBoard().completed_handoff_ids || []);
  syncIdeaHandoffCompletionPolling();
  renderAll();
}

async function selectProject(slug) {
  try {
    await loadDetail(slug);
  } catch (error) {
    toast(`读取项目失败 / Failed to load project: ${error.message}`);
  }
}

async function recycleProject(slug) {
  if (!slug) return;
  if (state.projectMutationBusy) {
    toast("上一个项目操作还在处理 / Previous project action is still running");
    return;
  }
  const project = state.projects.find((item) => item.slug === slug);
  const name = project?.name || slug;
  if (!window.confirm(`确定回收项目“${name}”？\n项目不会删除，可在回收站恢复。`)) return;
  state.projectMutationBusy = true;
  renderProjects();
  toast("回收项目中 / Recycling project...");
  try {
    const result = await requestJson(`/api/projects/${encodeURIComponent(slug)}/recycle`, { method: "POST", body: "{}" });
    state.projects = result.projects || state.projects.filter((item) => item.slug !== slug);
    state.recycledProjects = result.recycled_projects || state.recycledProjects;
    const wasSelected = state.selectedSlug === slug;
    if (state.selectedSlug === slug) {
      state.selectedSlug = null;
      state.detail = null;
    }
    state.recycleBinOpen = true;
    if (wasSelected) renderAll();
    else {
      renderProjects();
      renderRecycleBinPage();
    }
    toast("项目已回收 / Project recycled");
  } catch (error) {
    toast(`回收项目失败 / Recycle failed: ${error.message}`);
  } finally {
    state.projectMutationBusy = false;
    renderProjects();
    renderRecycleBinPage();
  }
}

async function restoreProject(trashName) {
  if (!trashName) return;
  if (state.projectMutationBusy) {
    toast("上一个项目操作还在处理 / Previous project action is still running");
    return;
  }
  const project = state.recycledProjects.find((item) => item.trash_name === trashName);
  const name = project?.name || trashName;
  if (!window.confirm(`恢复项目“${name}”？\n如果主项目区已有同名 slug，系统会阻止覆盖。`)) return;
  state.projectMutationBusy = true;
  renderProjects();
  renderRecycleBinPage();
  toast("恢复项目中 / Restoring project...");
  try {
    const result = await requestJson(`/api/recycle-bin/${encodeURIComponent(trashName)}/restore`, { method: "POST", body: "{}" });
    state.projects = result.projects || state.projects;
    state.recycledProjects = result.recycled_projects || state.recycledProjects.filter((item) => item.trash_name !== trashName);
    renderProjects();
    renderRecycleBinPage();
    if (result.project?.slug) {
      state.selectedSlug = result.project.slug;
      state.detail = result.project;
      renderAll();
    }
    toast("项目已恢复 / Project restored");
  } catch (error) {
    toast(`恢复项目失败 / Restore failed: ${error.message}`);
  } finally {
    state.projectMutationBusy = false;
    renderProjects();
    renderRecycleBinPage();
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
  $("stageFilter")?.addEventListener("change", (event) => {
    state.filters.stage = event.target.value;
    renderResourceBrowser();
  });
  $("kindFilter")?.addEventListener("change", (event) => {
    state.filters.kind = event.target.value;
    renderResourceBrowser();
  });
  $("decisionFilter")?.addEventListener("change", (event) => {
    state.filters.decision = event.target.value;
    renderResourceBrowser();
  });
  $("assetSearch")?.addEventListener("input", (event) => {
    state.filters.query = event.target.value;
    renderResourceBrowser();
  });
  $("clearResourceFilters")?.addEventListener("click", () => {
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
    if (event.key === "Escape" && state.whiteboxOpen) {
      closeWhiteboxLab();
      return;
    }
    if (event.key === "Escape" && state.boardOpen) {
      closeReferenceBoard();
      return;
    }
    if (event.key === "Escape" && state.recycleBinOpen) {
      closeRecycleBinPage();
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

const BUTTON_HELP_FALLBACKS = new Map([
  ["×", "关闭窗口、删除当前项，或移除这张临时卡片，具体取决于所在位置。"],
  ["✓", "标记当前图片后续可以采用或参考。"],
  ["打开原图 / Open", "在新窗口打开当前图片原始文件。"],
  ["复制 / Copy", "复制这张交接卡的完整文本。"],
  ["清空 / Clear", "清空当前临时选择或筛选结果，不删除项目文件。"],
  ["展开 / Expand", "展开当前交接卡列表。"],
  ["最小化 / Minimize", "收起当前交接卡列表，保留内容。"],
]);

function buttonHelpText(button) {
  if (!button) return "";
  const explicit = button.dataset.help || "";
  if (explicit) return explicit;
  const title = button.getAttribute("title") || "";
  if (title) return title;
  const text = button.textContent?.trim().replace(/\s+/g, " ") || "";
  if (BUTTON_HELP_FALLBACKS.has(text)) return BUTTON_HELP_FALLBACKS.get(text);
  if (button.type === "submit") return text ? `提交当前表单：${text}` : "提交当前表单。";
  if (button.classList.contains("studio-stage-filter")) return "切换图片页显示范围。";
  if (button.classList.contains("frame-thumb")) return "切换到这张图片页。";
  if (button.classList.contains("quick-filter")) return "快速切换资源筛选条件。";
  if (button.classList.contains("sidebar-scene-button")) return "切换当前幕/场戏。";
  return text ? `执行此操作：${text}` : "执行这个按钮对应的操作。";
}

function applyButtonHelpFallbacks(root = document) {
  root.querySelectorAll?.("button").forEach((button) => {
    if (button.dataset.noHelp === "true") return;
    button.dataset.help = buttonHelpText(button);
  });
}

function installButtonHelpObserver() {
  applyButtonHelpFallbacks(document);
  const observer = new MutationObserver((mutations) => {
    const roots = new Set();
    mutations.forEach((mutation) => {
      mutation.addedNodes.forEach((node) => {
        if (node.nodeType !== 1) return;
        roots.add(node);
      });
    });
    roots.forEach((node) => {
      if (node.matches?.("button")) {
        node.dataset.help = buttonHelpText(node);
      }
      applyButtonHelpFallbacks(node);
    });
  });
  observer.observe(document.body, { childList: true, subtree: true });
}

function bindEvents() {
  $("refreshBtn")?.addEventListener("click", () => (state.dailyIdeasOpen ? openDailyIdeasPage() : runAction("刷新 / Refresh", loadProjects)));
  $("openIdeaLabBtn")?.addEventListener("click", () => {
    state.dailyIdeasOpen = false;
    renderAll();
    $("ideaLab")?.scrollIntoView({ behavior: "smooth", block: "start" });
  });
  $("openDailyIdeasBtn")?.addEventListener("click", openDailyIdeasPage);
  $("openWhiteboxLabBtn")?.addEventListener("click", () => {
    state.dailyIdeasOpen = false;
    renderAll();
    openWhiteboxLab();
  });
  $("openRecycleBinBtn")?.addEventListener("click", () => {
    state.dailyIdeasOpen = false;
    renderAll();
    runAction("打开回收站 / Open recycle bin", openRecycleBinPage);
  });
  $("openExternalRetouchBtn")?.addEventListener("click", (event) => {
    event.preventDefault();
    state.dailyIdeasOpen = false;
    if (isExternalRetouchPage()) $("externalRetouchLab")?.scrollIntoView({ behavior: "smooth", block: "start" });
    else window.location.href = "/external-retouch";
  });
  $("openBoardBtn")?.addEventListener("click", () => {
    state.dailyIdeasOpen = false;
    renderAll();
    openReferenceBoard();
  });
  $("closeBoardBtn")?.addEventListener("click", closeReferenceBoard);
  $("clearBoardBtn")?.addEventListener("click", clearReferenceBoard);
  $("boardImageLightboxCopy")?.addEventListener("click", (event) => {
    event.preventDefault();
    event.stopPropagation();
    copyExternalImageToClipboard($("boardImageLightboxImg"));
  });
  // Let the native download proceed, but don't let the click bubble up and close the lightbox.
  $("boardImageLightboxDownload")?.addEventListener("click", (event) => event.stopPropagation());
  $("boardImageLightboxClose")?.addEventListener("click", closeBoardImageLightbox);
  $("boardImageLightbox")?.addEventListener("click", (event) => {
    event.preventDefault();
    closeBoardImageLightbox();
  });
  $("validateBtn")?.addEventListener("click", validateCurrentProject);
  $("analyzeBtn")?.addEventListener("click", analyzeCurrentProject);
  $("autofillBtn")?.addEventListener("click", autofillCurrentProject);
  $("sceneLockBtn")?.addEventListener("click", buildSceneLocksCurrentProject);
  $("createForm")?.addEventListener("submit", createProject);
  $("linkForm")?.addEventListener("submit", updateLinks);
  $("assetPreviewCopy")?.addEventListener("click", (event) => {
    event.preventDefault();
    event.stopPropagation();
    const image = $("assetPreviewBody")?.querySelector(".asset-preview-image");
    if (image) copyExternalImageToClipboard(image);
  });
  $("assetPreviewClose")?.addEventListener("click", closeAssetPreview);
  $("assetPreviewModal")?.addEventListener("click", (event) => {
    if (event.target?.id === "assetPreviewModal" || event.target?.closest?.(".asset-preview-image")) closeAssetPreview();
  });
  bindResourceFilters();
  bindKeyboardShortcuts();
  installButtonHelpObserver();
  installExternalImageDrag();
}

bindEvents();
loadProjects().catch((error) => {
  toast(`初始化失败 / Initialization failed: ${error.message}`);
  renderAll();
});
