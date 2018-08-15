#!/usr/bin/env bash

./pants binary ::
watchmedo shell-command \
    --patterns="*.py" \
    --recursive \
    --command='./pants binary ::' \
    ./src
