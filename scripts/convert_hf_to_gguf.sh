#!/usr/bin/env bash
# Convert a Hugging Face LLaMA-3.1 model to GGUF format with quantization

set -e

if [ -z "$1" ]; then
  echo "Usage: $0 <huggingface-model-path>"
  echo "Example: $0 meta-llama/Meta-Llama-3.1-8B"
  exit 1
fi

MODEL_PATH=$1
python3 llama.cpp/convert_hf_to_gguf.py $MODEL_PATH \
  --outfile ${MODEL_PATH##*/}-q4.gguf \
  --quantization q4_0
