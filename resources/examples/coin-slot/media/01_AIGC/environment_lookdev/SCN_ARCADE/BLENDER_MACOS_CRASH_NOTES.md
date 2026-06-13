# Blender macOS crash notes

Updated: 2026-05-28 17:22:06 +0800

## Local machine

- Model: `MacBookPro18,2` (MacBook Pro with Apple M1 Max)
- CPU/GPU architecture in crash logs: `ARM-64`, `translated=false`
- GPU: Apple M1 Max, 32 cores
- Metal: supported
- macOS: `26.5 (25F71)`

## Tested Blender builds

- Installed app: `/Applications/Blender.app/Contents/MacOS/Blender`
  - Version command works.
  - Version: Blender `5.1.2`, macOS arm64.
  - CLI/background/script launch crashes before Python runs.
- Official downloaded app mounted at `/Volumes/Blender 1/Blender.app/Contents/MacOS/Blender`
  - Version command works.
  - Version: Blender `4.5.10 LTS`, build date `2026-05-19`, hash `6dc0b208d1b5`.
  - Background/script launch crashes before Python runs.
  - Non-background `--python-expr` launch from Codex shell also triggers an AppKit registration abort.

## Crash signatures

Blender's own crash file:

```text
supports_barycentric_whitelist
MTLBackend::metal_is_supported
GPU_backend_type_selection_detect
wm_homefile_read_ex
WM_init
main
```

macOS `.ips` reports include:

- `EXC_BAD_ACCESS / SIGSEGV / KERN_INVALID_ADDRESS at 0x0000000000000000`
- Faulting frame chain:

```text
_platform_strstr
blender::gpu::supports_barycentric_whitelist(id<MTLDevice>)
blender::gpu::MTLBackend::metal_is_supported()
blender::GPU_backend_type_selection_detect()
blender::wm_homefile_read_ex(...)
blender::WM_init(...)
main
```

Some non-background launches from the Codex shell also produce:

```text
SIGABRT / Abort trap: 6
___RegisterApplication_block_invoke
_RegisterApplication
GHOST_SystemCocoa::init()
WM_init
main
```

## Interpretation

This does not look like a scene complexity, Python script, file path, or memory-pressure problem. The most consistent failure happens before project Python runs, during Blender's Apple Metal backend/device support detection. The M1 Max is relevant because the crash path goes through the Apple Silicon Metal stack, but this is not a sign that M1 Max is too weak. It is more likely a compatibility bug between the tested Blender arm64 builds, macOS `26.5`, and the local Apple GPU/Metal driver path.

## Operational decision

For this project, do not depend on Blender CLI/headless automation on this Mac until a stable Blender/macOS combination is found. Continue SCN_ARCADE with:

- the generated mother image as style reference,
- the OBJ/MTL visual constraint whitebox as Blender-importable geometry,
- 2D whitebox/overlay renders for immediate image-generation constraints,
- optional manual GUI Blender work only when needed.

Current usable fallback assets:

- `whitebox_obj/SCN_ARCADE_mother_visual_constraint_whitebox_v001.obj`
- `whitebox_obj/SCN_ARCADE_mother_visual_constraint_whitebox_v001.mtl`
- `whitebox_obj/SCN_ARCADE_mother_camera_lock_v001.json`
- `whitebox_obj/SCN_ARCADE_scene_asset_design_list_v001.csv`
- `whitebox_obj/SCN_ARCADE_visual_constraint_compare_v001.jpg`
