#!/usr/bin/env bash
# Run LLaMA-3.1 8B (quantized GGUF) with llama.cpp

set -e

./llama.cpp/main \
  -m models/llama-3.1-8b-q4.gguf \
  -p "This is a prompt. Summarize the story of the Lord of the Rings in one paragraph." \
  -n 128 \
  --threads 8 \
  --ctx_size 2048
