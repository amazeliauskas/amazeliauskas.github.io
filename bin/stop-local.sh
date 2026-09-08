#!/bin/bash
# Stop the local Jekyll dev server started by bin/serve-local.sh
if pkill -f "jekyll serve"; then
    echo "Jekyll server stopped."
else
    echo "No running Jekyll server found."
fi
