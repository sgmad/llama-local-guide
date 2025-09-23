#!/usr/bin/env bash
# Run LLaMA-3.1 13B (quantized GGUF) with llama.cpp

set -e

./llama.cpp/main \
  -m models/llama-3.1-13b-q4.gguf \
  -p "Explain the benefits and tradeoffs of running LLaMA models locally." \
  -n 128 \
  --threads 8 \
  --ctx_size 2048
