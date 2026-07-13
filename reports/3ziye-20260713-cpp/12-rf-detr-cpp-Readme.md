<img width="1540" height="324" alt="RF-DETR CPP" src="https://github.com/user-attachments/assets/2b21c5d5-2ba7-498d-94f1-fe3f8e2bf871" />

<h3 align="center">Production-ready C++/TensorRT inference engine for RF-DETR.</h3>

<p align="center">
  <a href="#quick-start">Quick Start</a> ·
  <a href="#supported-models--tasks">Models</a> ·
  <a href="#api-reference">API</a> ·
  <a href="#benchmarks">Benchmarks</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/TensorRT-%E2%89%A5%2010.0-76B900?logo=nvidia&logoColor=white" alt="TensorRT"/>
  <img src="https://img.shields.io/badge/CUDA-%E2%89%A5%2012.0-76B900?logo=nvidia&logoColor=white" alt="CUDA"/>
  <img src="https://img.shields.io/badge/C%2B%2B-17-blue.svg?logo=cplusplus&logoColor=white" alt="C++17"/>
  <img src="https://img.shields.io/badge/license-Apache--2.0-ef4444" alt="License"/>
  <a href="https://github.com/infracv/rf-detr-cpp/releases"><img alt="GitHub release" src="https://img.shields.io/github/release/infracv/rf-detr-cpp.svg"></a>
</p>


---

## Overview

**RF-DETR C++** is a production-grade TensorRT inference engine for [RF-DETR](https://github.com/roboflow/rf-detr), Roboflow's transformer-based real-time object detection model built on a DINOv2 backbone.

```cpp
#include "rfdetr/tasks/detector.hpp"

rfdetr::RFDetrDetector detector("rf-detr-nano-fp32.engine");
rfdetr::Detections dets = detector.detect(cv::imread("image.jpg"), 0.5f);
```

Unlike YOLO models, RF-DETR uses a DETR-style architecture with **no NMS, no anchor grids, no letterboxing**. This requires a different inference pipeline, which this library implements entirely in C++ with zero Python at runtime.

Most RF-DETR deployments run Python at inference time. This library eliminates that dependency:

| | RF-DETR C++ | Python (PyTorch) |
|---|:---:|:---:|
| Runtime dependency | **C++ only** | Python + PyTorch + CUDA |
| Preprocessing | **GPU CUDA kernel** | CPU / torchvision |
| Host-to-device transfer | **Async** (pinned memory) | Synchronous |
| Precision | **FP32 / FP16 / INT8** | FP32 / FP16 |
| Inference dispatch | **CUDA Graph replay** | Per-frame forward pass |
| Latency (RTX 5070 Ti) | **2.0 ms (FP16)** | ~15–30 ms |

---

## Quick Start

```sh
# 1. Clone & build
git clone https://github.com/infracv/rf-detr-cpp.git
cd rf-detr-cpp
cmake -B build -S . -DCMAKE_BUILD_TYPE=Release -DCMAKE_CUDA_ARCHITECTURES=120
cmake --build build -j$(nproc)
# Replace 120 with your GPU arch: RTX 30xx=86, RTX 40xx=89, RTX 50xx=120
# Tarball TensorRT: add -DTENSORRT_DIR=/path/to/TensorRT

# 2. Export ONNX and build TRT engine (one-time, Python)
pip install -r requirements.txt
python trt-files/scripts/export_onnx.py --variant nano --out-dir trt-files/onnx

# FP32 engine
./build/rfdetr_build --onnx trt-files/onnx/rf-detr-nano.onnx --precision fp32

# FP16 engine
./build/rfdetr_build --onnx trt-files/onnx/rf-detr-nano.onnx --precision fp16

# 3. Run inference
./build/rfdetr_detect \
    --engine trt-files/onnx/rf-detr-nano-fp16.engine \
    --image  asset/test_img.jpg --out out/result.jpg
```

---

## Supported Models & Tasks

| Task | Variants |
|:-----|:---------|
| Object Detection | `nano`, `small`, `medium`, `base`, `large` |
| Instance Segmentation | `seg-nano`, `seg-small`, `seg-medium`, `seg-large`, `seg-xlarge`, `seg-2xlarge` |

### Precision support

| Precision | TRT < 11 | TRT 11+ | Notes |
|:---------:|:--------:|:-------:|-------|
| FP32 | ✅ | ✅ | Default |
| FP16 | ✅ (`kFP16` flag) | ✅ (`convert_fp16.py` → pre-converted ONNX) | ~25% faster than FP32 |
| INT8 | ✅ (calibration cache) | ✅ (QDQ ONNX via `convert_int8.py`) | Lowest memory |

> **FP16 NaN sanity check.** RF-DETR's transformer attention can produce values that exceed the FP16 range (±65,504), causing NaNs to propagate through the network and yield zero detections. After building an FP16 engine, run a single detection on `asset/test_img.jpg`. If you get zero detections on an image where FP32 finds objects, your FP16 engine is hitting overflow. Fall back to FP32 (`rfdetr_build --precision fp32`) or rebuild with mixed-precision settings.

---

## Installation

### Prerequisites

| Dependency | Version | Notes |
|:-----------|:-------:|:------|
| NVIDIA GPU | CC ≥ 8.0 | RTX 30xx / 40xx / 50xx |
| CUDA Toolkit | ≥ 12.0 | |
| TensorRT | ≥ 10.0 | TRT 11 supported (strongly-typed networks) |
| OpenCV | ≥ 4.5 | core, imgproc, imgcodecs, videoio, highgui |
| CMake | ≥ 3.20 | |
| C++ compiler | C++17 | GCC 9+, Clang 10+ |

### Build from Source

```sh
git clone https://github.com/infracv/rf-detr-cpp.git
cd rf-detr-cpp
cmake -B build -S . -DCMAKE_BUILD_TYPE=Release -DCMAKE_CUDA_ARCHITECTURES=120
cmake --build build -j$(nproc)
# Tarball TensorRT: add -DTENSORRT_DIR=/path/to/TensorRT
```

Replace `120` with your GPU's compute capability:

| GPU family | `CMAKE_CUDA_ARCHITECTURES` |
|:-----------|:--------------------------:|
| RTX 30xx (Ampere) | `86` |
| RTX 40xx (Ada Lovelace) | `89` |
| RTX 50xx (Blackwell) | `120` |
| Jetson O