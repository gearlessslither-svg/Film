param(
    [string]$Workspace = "",
    [int]$IntervalSec = 60,
    [int]$Hours = 0,
    [switch]$KeepDisplayOn,
    [switch]$Once,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"

function Resolve-FullPath {
    param([string]$Path)
    return [System.IO.Path]::GetFullPath($Path)
}

if ($Workspace.Trim().Length -eq 0) {
    $Workspace = (Get-Location).Path
}

$script:WorkspacePath = Resolve-FullPath $Workspace
if (-not (Test-Path -Path $script:WorkspacePath -PathType Container)) {
    throw "Workspace does not exist: $script:WorkspacePath"
}

$resumeDir = Join-Path $script:WorkspacePath ".codex-resume"
$logPath = Join-Path $resumeDir "keep-awake.log"

if (-not $DryRun -and -not (Test-Path -Path $resumeDir -PathType Container)) {
    New-Item -ItemType Directory -Force -Path $resumeDir | Out-Null
}

function Write-KeepAwakeLog {
    param(
        [string]$Message,
        [string]$Level = "INFO"
    )
    $timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    $line = "[$timestamp][$Level] $Message"
    Write-Host $line
    if (-not $DryRun) {
        Add-Content -Path $logPath -Value $line -Encoding UTF8
    }
}

if (-not $DryRun) {
    Add-Type @"
using System;
using System.Runtime.InteropServices;

public static class ExecutionStateKeeper {
    [DllImport("kernel32.dll", SetLastError = true)]
    public static extern uint SetThreadExecutionState(uint esFlags);
}
"@
}

$ES_CONTINUOUS = [UInt32]2147483648
$ES_SYSTEM_REQUIRED = [UInt32]1
$ES_DISPLAY_REQUIRED = [UInt32]2

$flags = [UInt32]($ES_CONTINUOUS -bor $ES_SYSTEM_REQUIRED)
if ($KeepDisplayOn) {
    $flags = [UInt32]($flags -bor $ES_DISPLAY_REQUIRED)
}

$started = Get-Date
$mode = if ($KeepDisplayOn) { "system-and-display-awake" } else { "system-awake-display-may-sleep" }

Write-KeepAwakeLog "Starting keep-awake. Workspace=$script:WorkspacePath Mode=$mode IntervalSec=$IntervalSec Hours=$Hours Once=$Once DryRun=$DryRun"

try {
    do {
        if ($DryRun) {
            Write-KeepAwakeLog "DryRun: would call SetThreadExecutionState flags=$flags"
        }
        else {
            $result = [ExecutionStateKeeper]::SetThreadExecutionState($flags)
            if ($result -eq 0) {
                $err = [Runtime.InteropServices.Marshal]::GetLastWin32Error()
                Write-KeepAwakeLog "SetThreadExecutionState failed. Win32Error=$err" "ERROR"
            }
            else {
                Write-KeepAwakeLog "Keep-awake assertion refreshed."
            }
        }

        if ($Once) {
            break
        }

        if ($Hours -gt 0) {
            $elapsed = (Get-Date) - $started
            if ($elapsed.TotalHours -ge $Hours) {
                Write-KeepAwakeLog "Requested duration reached. Exiting."
                break
            }
        }

        Start-Sleep -Seconds $IntervalSec
    } while ($true)
}
finally {
    if (-not $DryRun) {
        [ExecutionStateKeeper]::SetThreadExecutionState([UInt32]$ES_CONTINUOUS) | Out-Null
    }
    Write-KeepAwakeLog "Keep-awake stopped. Windows power policy restored for this process."
}
