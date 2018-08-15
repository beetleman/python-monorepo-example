#!/usr/bin/env bash

./pants binary ::
watchmedo shell-command \
          --patterns="*.py" \
          --ignore-patterns="*/.*" \
          --recursive \
          --command='./pants binary ::; echo "changed: ${watch_src_path}"' \
          --wait \
          ./src
