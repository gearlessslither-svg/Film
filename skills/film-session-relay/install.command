#!/bin/zsh
# Deploy the canonical film-session-relay skill into both Codex and Claude Code.
# Canonical source lives in this folder (git-tracked with the Film tool).
set -e
SRC="$(cd "$(dirname "$0")" && pwd)"
NAME="film-session-relay"

CODEX_DST="$HOME/.codex/skills/$NAME"
CLAUDE_DST="$HOME/.claude/skills/$NAME"

for DST in "$CODEX_DST" "$CLAUDE_DST"; do
  mkdir -p "$DST"
  rsync -a --delete \
    --exclude ".git" --exclude "__pycache__" --exclude "install.command" \
    "$SRC"/ "$DST"/
  echo "deployed -> $DST"
done

# Claude Code reads SKILL.md frontmatter only; the Codex copy also needs agents/openai.yaml (kept).
echo "done. Codex: \$film-session-relay   Claude: /film-session-relay (or auto-trigger)."
