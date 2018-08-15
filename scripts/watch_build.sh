#!/usr/bin/env bash

./pants binary ./src/python/app:app
watchmedo shell-command \
    --patterns="*.py" \
    --recursive \
    --command='./pants binary ./src/python/app:app' \
    ./src
