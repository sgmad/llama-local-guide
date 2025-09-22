#!/usr/bin/env bash
# Install dependencies and build llama.cpp for LLaMA-3.1 local runs

set -e

# Core Python dependencies (CPU-first; replace with CUDA wheels if needed)
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
pip install transformers accelerate huggingface_hub sentencepiece

# Clone and build llama.cpp
if [ ! -d "llama.cpp" ]; then
  git clone https://github.com/ggerganov/llama.cpp.git
fi

cd llama.cpp
make -j$(nproc)
cd ..

# Ensure all .sh scripts are executable
chmod +x scripts/*.sh
