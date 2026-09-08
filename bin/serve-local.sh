#!/bin/bash
# Start the local Jekyll dev server (live-reloading) in the background.
# Serves at http://localhost:4000/  — stop with bin/stop-local.sh
set -e
cd "$(dirname "$0")/.."

bundle exec jekyll serve --livereload --detach

echo "Jekyll started at http://localhost:4000/  (stop with: bin/stop-local.sh)"
