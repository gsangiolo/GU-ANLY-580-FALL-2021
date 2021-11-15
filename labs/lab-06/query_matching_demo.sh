#!/bin/bash

gunicorn query_matching_demo:app \
  --workers 1 \
  --worker-class virtex.VirtexWorker \
  --bind localhost:8080 \
  --worker-connections 10000 \
  --timeout 60 \
  --log-level INFO
