#!/usr/bin/env python3
"""Run the global prompt/state validators and preserve their JSON evidence."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def run(command: list[str]) -> tuple[int, dict]:
    result = subprocess.run(command, check=False, capture_output=True, text=True)
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"validator did not return JSON: {command}\n{result.stdout}\n{result.stderr}") from exc
    return result.returncode, payload


def main() -> int:
    project = Path(__file__).resolve().parents[1]
    repo = project.parents[1]
    board = project / "03_story/idea_board/idea_board.json"
    prompt_validator = repo / "skills/aigc-production-hard-rules/scripts/validate_prompt_contract.py"
    state_validator = repo / "skills/aigc-production-hard-rules/scripts/validate_narrative_state_contract.py"
    prompt_code, prompt_report = run([sys.executable, str(prompt_validator), str(board)])
    state_code, state_report = run([
        sys.executable,
        str(state_validator),
        str(board),
        "--project-root",
        str(project),
    ])
    qa = project / "10_qa"
    qa.mkdir(parents=True, exist_ok=True)
    (qa / "prompt_contract_qa.json").write_text(json.dumps(prompt_report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (qa / "narrative_state_contract_qa.json").write_text(json.dumps(state_report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    result = {
        "ok": prompt_code == 0 and state_code == 0,
        "prompt_contract": prompt_report,
        "narrative_state_contract": state_report,
    }
    print(json.dumps({
        "ok": result["ok"],
        "prompt_errors": prompt_report.get("errors", []),
        "state_errors": state_report.get("errors", []),
    }, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
