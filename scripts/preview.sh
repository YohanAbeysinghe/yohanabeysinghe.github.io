#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

# macOS ships an older Ruby; use the installed Homebrew 3.3 runtime when present.
if [[ -x /opt/homebrew/opt/ruby@3.3/bin/ruby ]]; then
  export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"
fi
bundle check >/dev/null || { echo "Install dependencies first; see README.md."; exit 1; }
exec bundle exec jekyll serve --host 127.0.0.1 --port 4000 "$@"
