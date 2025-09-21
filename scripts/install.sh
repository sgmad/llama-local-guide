#!/bin/bash
# Install dependencies for running LLaMA-3.1 locally with llama.cpp and Hugging Face tools

# Core Python deps
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
pip install transformers accelerate huggingface_hub sentencepiece

# llama.cpp build (CPU/GPU support)
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
make -j$(nproc)
cd ..
pip install git+https://github.com/ggerganov/llama.cpp.git