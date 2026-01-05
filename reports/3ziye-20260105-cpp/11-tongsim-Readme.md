# TongSIM

A high-fidelity platform for multimodal embodied agent training (Unreal Engine + Python SDK)


[![Static Badge](https://img.shields.io/badge/Home-TongSIM-blue?logo=googledocs&logoColor=white)](https://tongsim-platform.github.io/tongsim/)
[![Static Badge](https://img.shields.io/badge/Hugging_Face-TongSIM--Asset-yellow?logo=huggingface)](https://huggingface.co/datasets/bigai/TongSIM-Asset)
[![Static Badge](https://img.shields.io/badge/Docs-TongSIM-%23526CFE?logo=materialformkdocs&logoColor=white)](https://bigai-ai.github.io/tongsim/)
[![Static Badge](https://img.shields.io/badge/arXiv-2512.20206-red?logo=arxiv)](https://arxiv.org/abs/2512.20206)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/bigai-ai/tongsim/docs.yml)

![TongSIM Preview](docs/assets/tongsim-main.png)

**Links**

- Homepage: https://tongsim-platform.github.io/tongsim
- Documentation: https://bigai-ai.github.io/tongsim/
- Asset Library (Hugging Face): https://huggingface.co/datasets/bigai/TongSIM-Asset

TongSIM is a high-fidelity, general-purpose platform for embodied agent training and testing built on Unreal Engine, supporting tasks from low-level single-agent skills (e.g., navigation) to high-level scenarios such as multi-agent social simulation and human–AI collaboration. TongSIM constructs 100+ diverse multi-room indoor scenarios alongside an open-ended, interaction-rich outdoor simulated town, and incorporates thousands of interactive 3D object models spanning 500+ categories.

Currently, indoor rooms are fully accessible, while outdoor environments remain under continuous development and optimization. We will gradually open access to these outdoor assets based on actual research needs, with the goal of providing more comprehensive support for the scientific work of our community's researchers. Please stay tuned for updates.

On top of the environment, TongSIM provides a comprehensive evaluation system and a suite of benchmarks covering major agent capabilities: perception, cognition, decision-making, learning, execution, and social collaboration. The platform also offers high-fidelity and customizable scenes, rich annotations, and parallel training to accelerate research and development of general embodied intelligence.

This repository contains:

- Unreal Engine project (`unreal/`)
- Python SDK and examples (`src/`, `examples/`)
- Documentation site sources (`docs/`, `mkdocs.yml`)

## Highlights

- High-fidelity indoor + outdoor worlds: 100+ multi-room indoor scenes and an open-ended outdoor town
- Large-scale interactive assets: thousands of objects spanning 500+ categories
- Benchmarks and evaluation: perception, cognition, decision-making, learning, execution, and social collaboration
- Multimodal perception: built-in vision and audio; extensible to other modalities
- Physics-consistent simulation with causal world dynamics and rich annotations
- Parallel simulation for scalable training
- Easy integration: Python SDK over gRPC with practical examples
- Extensible, plugin-oriented architecture

## Requirements

- OS: Windows 10/11 or Ubuntu 22.04
- Unreal Engine: 5.6 (install via Epic Games Launcher)
- Python: 3.12+

## Getting Started

### Python Installation

Use either `uv` (recommended) or plain `pip`.

#### Option A: uv (recommended)

1. Install [`uv`](https://docs.astral.sh/uv/)
2. Create and sync a virtual environment (defaults to installing `dev` and `docs` groups as configured):
   ```powershell
   uv venv
   uv sync
   ```

3. Run examples (start the UE project first; gRPC at `127.0.0.1:5726`):
   ```powershell
   uv run examples/quickstart_demo.py
   uv run examples/voxel.py
   ```

#### Option B: pip

1. Install the package in editable mode:
   ```powershell
   pip install -e .
   ```
2. Optional: dev/docs tooling (for contributing or building docs):
   ```powershell
   pip install pre-commit black ruff mkdocs mkdocs-material mkdocstrings-python mkdocs-static-i18n mkdocs-redirects pytest pytest-asyncio
   pre-commit install
   ```
3. Run examples (start the UE project first):
   ```powershell
   python examples\quickstart_demo.py
   python examples\voxel.py
   ```

### Install UE 5.6
1. Install Unreal Engine 5.6 via Epic Games Launcher (Editor build matching your platform).
2. Install Git:
   ```powershell
   winget install Git.Git -s winget
   ```

### Run the UE Project

1. Clone the repo:
   ```powershell
   git clone https://github.com/bigai-ai/tongsim
   cd tongsim
   ```
2. Download Unreal Engine assets into `unreal/Content`:
   ```powershell
   uv run scripts/fetch_unreal_content.py
   ```
3. (First-time) Download and extract the TongSimGrpc gRPC dependency bundle (Release asset) to the repo root:
   - Windows (PowerShell):
     ```powershell
     $base = "https://github.com/bigai-ai/tongsim/releases/download/tongsimgrpc-deps-v1.0"
     Invoke-WebRequest "$base/TongSimGrpc_deps.zip" -OutFile TongSimGrpc_deps.zip
     Invoke-WebRequest "$base/TongSimGrpc_deps.zip.s