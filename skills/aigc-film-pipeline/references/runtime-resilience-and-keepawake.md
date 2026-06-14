# 投币口 / 运行时续跑与防睡眠规则 v1

本文件处理用户离开、黑屏、屏保、网络波动、额度恢复和线程恢复时的运行边界。

## 能做到的事

- 屏幕关闭或进入屏保时，只要 Windows 没有睡眠、Codex 线程还活着，任务可以继续。
- heartbeat automation 可以定期唤起当前线程继续执行。
- `TASK_LOG.md` 能让恢复后的 Codex 从中断点继续。
- `codex-connection-resilience` 的 watchdog 能准备恢复提示，并在有可启动 Codex CLI 时可选执行 `codex resume`。
- `scripts/keep-codex-awake.ps1` 可以在运行期间调用 Windows execution state，阻止系统自动睡眠。

## 做不到的事

- 电脑关机、重启、强制系统更新后，当前模型不能凭空继续。
- Codex Desktop 进程被关闭后，当前线程不能自行继续。
- 网络彻底断开时，模型不能继续调用远端能力。
- 当前本机 WindowsApps 打包版 `codex.exe` 从 PowerShell 启动会 `Access is denied`，所以自动 CLI resume 需要另一个可启动 CLI 路径。

## 推荐运行组合

### 1. 线程续跑

保持 heartbeat automation：

- 当前建议 automation id：`continue-production-pipeline` 或当前 `TASK_LOG.md` 中记录的 active heartbeat。
- 每次 heartbeat 第一动作必须读取 `TASK_LOG.md`。

### 2. 网络恢复提示

安全模式：

```powershell
powershell -ExecutionPolicy Bypass -File "C:\Users\user1\.codex\skills\codex-connection-resilience\scripts\watch-codex-link.ps1" -Workspace "E:\视觉\投币口"
```

它只写日志和恢复提示，不主动消耗模型请求。

### 3. 防睡眠

允许黑屏但阻止睡眠：

```powershell
powershell -ExecutionPolicy Bypass -File "E:\视觉\投币口\scripts\keep-codex-awake.ps1" -Workspace "E:\视觉\投币口"
```

如果需要同时保持屏幕常亮：

```powershell
powershell -ExecutionPolicy Bypass -File "E:\视觉\投币口\scripts\keep-codex-awake.ps1" -Workspace "E:\视觉\投币口" -KeepDisplayOn
```

默认推荐允许显示器关闭，避免长时间亮屏。

## 当前电源状态记录

2026-05-22 检查结果：

- Windows 当前电源方案中自动睡眠为 0 秒，等同禁用。
- 自动休眠为 0 秒，等同禁用。
- 显示器关闭时间不等于系统睡眠；显示器关闭通常不影响任务继续。
- `powercfg /requests` 需要管理员权限，本轮无法读取完整请求列表。

## 停止条件

只有以下情况才停止自动续跑：

- `TASK_LOG.md` 标记所有 known tasks 完成。
- final validation failed=0 且 pure photoreal 替换达到目标。
- 用户明确要求暂停。
- 遇到账号、验证码、付费权限、不可恢复工具故障或强制系统中断。

