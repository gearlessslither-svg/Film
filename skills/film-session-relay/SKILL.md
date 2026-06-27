---
name: film-session-relay
description: Use at the START of any AIGC Film Pipeline session, and whenever working in Story/Film projects (storyboards, idea_board, image generation, Pipeline Hub). Prevents the Codex memory/OOM crash caused by one window accumulating too many turns + inline images, by enforcing a per-window size budget, danger-node handoffs, and project continuity across windows. Also triggers when Codex is crashing/restarting, when the user says the session/对话太大/太长/换窗口/接续/交接, or when more than one film project is touched in a single window.
---

# Film Session Relay / 分镜项目接续与防崩

This skill lets a NEW window pick up an AIGC film project instantly (without re-analyzing the
tool or the project), and stops the Codex crash caused by oversized sessions. It works in both
**Codex** and **Claude Code**. Pair it with `aigc-film-pipeline` (how to produce) and
`codex-health-guard` (how to clean oversized session files).

Real project root: `/Users/jaychoupp/Story` (`/Users/jaychoupp/Desktop/Story` is a symlink to it).

## 0. 为什么存在 / Why (the failure this prevents)

One window ran an AIGC MV from 2026-06-02 to 06-27 (25,342 events, 1.6M tokens) until its Codex
session `.jsonl` reached **2.9GB** and crashed the Electron main process (V8 OOM, `SIGTRAP`) every
~15 minutes. Measured bloat: ~80% accumulated text (tool args + full-board returns + event log),
~20% inline base64 images (same images re-embedded up to 21×). The fix is not "stop showing the
model images" — it is **cap turns per window, keep tool returns compact, never re-embed images,
and hand off cleanly to a fresh window.**

## 1. 开机自检 / Run this at session start

```bash
python3 ~/Story/Film/skills/film-session-relay/scripts/relay.py status
```

- Read the band: `OK / WARN(150MB) / DANGER(300MB) / HIGH(800MB) / FATAL(2.4GB)`.
- If `DANGER` or worse on the **live** session: tell the user to wrap up and open a new window
  after a handoff. Do not start a big batch in a session that is already large.
- Then state the **one** project you are working on this window (see §5).

## 2. 单窗口预算 / Per-window budget (the core rule)

Treat these as hard stops for ONE window/conversation:

| 信号 / signal | 动作 / action |
|---|---|
| live session ≥ 300MB (relay status = DANGER) | 收尾本批 → 写交接 → **开新窗口** |
| 已生成 ≈ 30–40 张图 在同一窗口 | 写交接 → 开新窗口 |
| 即将开始一个大批量生图 (>10 张) | 先确认 session < 300MB；否则先换窗口 |
| 关窗 / 长时间离开前 | 写交接 |

新窗口承接成本几乎为零，因为交接包 + idea_board 就是完整状态。宁可多开窗口，不要把一个窗口堆爆。

## 3. 源头止血 / Stop the bloat at the source

回答"图片不在上下文里会不会影响生成":模型要分析/参考某张图,**那一次**必须看到它,这躲不掉也别躲。
要消灭的是**重复**和**回灌**,不是"看一次":

1. **本地图片处理走磁盘,不进对话**:QA、联系表、相似度、animatic、校验都用 `Film/scripts/...` 在磁盘上跑,
   只把结论(通过/失败/计数)带回对话,不要把整段输出或图片塞进来。
2. **看过的图用引用,不重贴**:一张参考图给模型看过后,后续轮次用 `item_id` / 文件路径指代,
   绝不把同一张 base64 再贴进新一轮。(上次崩溃里同一张图被嵌了 21 遍。)
3. **生成产出回路径,不回 base64**:回填 `http://127.0.0.1:8787/api/projects/<slug>/card-image-output`
   时只回 `output_path` + 紧凑 `row_updates`(按 `item_id` 打补丁),不要回传整张图的 base64,也不要 POST 整张 board。
4. **生成图默认落在** `~/.codex/generated_images/<thread-id>/`,复制进项目 `08_generation/jobs/<JOB>/outputs/` 后,
   对话里只留路径。

## 4. 危险节点清单 / Danger nodes — write a handoff at each

到达任一节点,**先更新交接再继续**:

- 大批量生图之前(把"打算生成哪些卡"写进 NEXT)。
- 一批生图完成、回填核验之后。
- relay status 报 DANGER 及以上。
- 关窗、重启 Codex、或预计长时间离开之前。
- 用户说"换个窗口 / 太卡 / 崩了 / 接着上次"。

写/刷新交接:

```bash
python3 ~/Story/Film/skills/film-session-relay/scripts/relay.py handoff <project-slug> --note "刚完成 X，下一步 Y"
```

它会在 `Film/projects/<slug>/00_admin/handoff/HANDOFF_<date>.md` 生成脚手架并更新 `HANDOFF_LATEST.md`。
`HANDOFF_LATEST.md` 必须是完整交接副本，而不是只含链接的索引，这样新窗口可以直接读取它继续。
**把 `_(填...)_` 段落补全**:创意主线、锁定设定、已完成、下一批、怎么继续。交接跟着项目走,
任何工具任何新窗口都能 `cat .../00_admin/handoff/HANDOFF_LATEST.md` 捡起来。

## 5. 一窗口一项目 / One project per window

开窗时声明当前项目,并只动这一个项目。**若本窗口出现第二个项目**(用户提到另一个 slug,或路径跨到
`Film/projects/<另一个>`),立即提醒:

> ⚠️ 这个窗口已经在做项目 `A`。你现在提到 `B`。混在一个窗口里会让会话更快变大、也会污染交接。
> 建议:给 `A` 写一份交接,然后为 `B` 开一个新窗口。要我现在给 A 写交接吗?

除非用户明确说"就在这个窗口一起做",否则不要在同一窗口并行两个项目。

## 6. 崩溃恢复快速通道 / Crash recovery

如果 Codex 刚崩/重启,或新窗口从零开始:

1. `python3 ~/Story/Film/skills/film-session-relay/scripts/relay.py status` —— 看是否仍有超大会话在拖累。
   若有 ≥800MB 的会话,用 `codex-health-guard` 隔离它(可还原),否则会继续崩:
   `python3 ~/.codex/skills/codex-health-guard/scripts/session_guard.py scan --threshold 150MB`
2. 找到项目最新交接:`cat ~/Story/Film/projects/<slug>/00_admin/handoff/HANDOFF_LATEST.md`
3. 读 `03_story/idea_board/idea_board.json` 确认卡片真实状态。
4. 校验:`python3 ~/Story/Film/scripts/validate_pipeline_state.py ~/Story/Film/projects/<slug>`
5. 从交接的 **NEXT** 段继续。不要重新分析整个项目或工具。

## 7. 工具速查 / Pipeline tool quickstart（不必重读代码）

- **启动 Hub**:双击 `/Users/jaychoupp/Story/Film_Tool_Launcher.command`(或 `python3 ~/Story/Film/apps/pipeline-hub/server.py`),
  打开 `http://127.0.0.1:8787`。
- **项目布局**:`Film/projects/<slug>/` 标准 12 段(`00_admin` … `11_delivery`);
  分镜数据在 `03_story/idea_board/idea_board.json`(行 = 卡,键 `item_id`、`status`、`output_path`)。
- **核心脚本**(全在 `Film/scripts/`):`validate_pipeline_state.py`、`analyze_aigc_project.py`、
  `autofill_aigc_project.py`、`visual/make_contact_sheet.py`、`visual/qa_whitebox_images.py`、
  `visual/build_storyboard_animatic.py`、`visual/validate_final_delivery.py`。
- **REST 回调**(本机 `127.0.0.1:8787/api/projects/<slug>/...`):`idea-board`、`card-image-packet`、
  `card-image-preflight`、`card-image-output`、`whitebox-job`、`idea-image-output`。
  回调一律 **紧凑**:路径 + `row_updates`,不回 base64、不回整张 board(详见 §3 和 `aigc-film-pipeline` 的 Handoff Rule)。
- 详细生产规则用 `aigc-film-pipeline`;一键体检用 `aigc-film-project-auditor`。

## 维护 / Maintenance

Canonical 源在 `~/Story/Film/skills/film-session-relay/`。改完后重新部署到两个工具:

```bash
bash ~/Story/Film/skills/film-session-relay/install.command
```

行为变化时,同步更新本 SKILL.md(与改动同批提交)。
