#!/usr/bin/env bash
set -e

uv sync || true

mkdir -p "$HOME/.codex"

cat > "$HOME/.codex/config.toml" <<'EOF'
sandbox_mode = "danger-full-access"
approval_policy = "never"
EOF

echo "Codex configured:"
command -v codex || true
codex --version || true