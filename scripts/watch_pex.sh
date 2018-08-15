#!/usr/bin/env bash

watchmedo auto-restart --directory=/apps \
          --patterns="*/${1}" \
          --signal=SIGTERM \
          /apps/$1
