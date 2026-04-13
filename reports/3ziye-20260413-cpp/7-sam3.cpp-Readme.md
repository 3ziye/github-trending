# sam3.cpp

State-of-the-art image and video segmentation in portable C/C++

![SAM3 Image Segmentation Demo](media/image_demo.gif)
![SAM3 Video Segmentation Demo](media/video_demo.gif)

---

## Why sam3.cpp?

Running Meta's Segment Anything models typically requires Python, PyTorch, and a CUDA GPU. **sam3.cpp** eliminates all of that. It's a single C++ library that runs SAM 2, SAM 2.1, SAM 3, and EdgeTAM inference on CPU and Apple Metal. No Python runtime, no GPU drivers, no heavyweight dependencies. Just compile and segment.

- **4 model families**: SAM 2, SAM 2.1 (Hiera), SAM 3 (ViT + text detection), EdgeTAM (RepViT, 22x faster than SAM 2 on mobile)
- **4-bit quantization**: EdgeTAM in **15 MB**, SAM 2.1 Tiny in **22 MB** at ~1 fps on Metal, SAM 3 down to 673 MB
- **Apple Metal GPU acceleration** for the full backbone and transformer decoder
- **Text-prompted detection** (SAM 3 only): type `"cat"` and get every cat in the image, no clicks needed
- **Point/box segmentation + video tracking** with memory bank across all models
- **Single-file library**: `sam3.cpp` + `sam3.h`, C++14, no exceptions, no inheritance
- **Zero dependencies** beyond [ggml](https://github.com/ggerganov/ggml) and [stb](https://github.com/nothings/stb)

## Quick Start

```bash
# Clone
git clone --recursive https://github.com/PABannier/sam3.cpp
cd sam3.cpp

# Build (Metal GPU enabled automatically on macOS)
mkdir build && cd build
cmake ..
make -j

# Download a model (SAM 2.1 Tiny, 75 MB)
# See "Model Zoo" below for all available models and download links
curl -L -o ../models/sam2.1_hiera_tiny_f16.ggml \
  https://huggingface.co/PABannier/sam3.cpp/resolve/main/sam2.1_hiera_tiny_f16.ggml

# Segment an image interactively (requires SDL2)
./examples/sam3_image --model ../models/sam2.1_hiera_tiny_f16.ggml --image ../data/test_image.jpg

# Track objects in a video interactively (requires SDL2)
./examples/sam3_video --model ../models/sam2.1_hiera_tiny_f16.ggml --video ../data/test_video.mp4
```

The interactive apps use SDL2 + ImGui. If SDL2 isn't found, only the benchmark and quantize tools are built.

## Benchmarks

Video object tracking latency on **Apple M4 Pro (24 GB)**, 5 frames at 1008x1008 resolution, 4 threads. Each run is isolated in a forked subprocess.

### SAM 3 (Full: text detection + visual tracking)

| Model | Size | Track/frame Metal (s) | Track/frame CPU (s) | Total Metal (s) | Total CPU (s) |
|-------|------|-----------------------|---------------------|-----------------|---------------|
| sam3-f32 | 3.2 GB | - | 40.5 | - | 200.4 |
| sam3-f16 | 1.7 GB | **7.7** | 23.8 | 38.1 | 117.5 |
| sam3-q8_0 | 1.0 GB | **7.8** | 23.3 | 38.7 | 115.2 |
| sam3-q4_1 | 756 MB | - | 24.5 | - | 120.9 |
| sam3-q4_0 | 673 MB | **7.8** | 23.9 | 38.7 | 117.7 |

### SAM 3 Visual-Only (no text encoder, tracking only)

| Model | Size | Track/frame Metal (s) | Track/frame CPU (s) | Total Metal (s) | Total CPU (s) |
|-------|------|-----------------------|---------------------|-----------------|---------------|
| sam3-visual-f16 | 901 MB | **6.6** | 22.6 | 32.7 | 111.2 |
| sam3-visual-q8_0 | 493 MB | **6.7** | 22.0 | 33.0 | 108.4 |
| sam3-visual-q4_1 | 318 MB | - | 23.1 | - | 113.9 |
| sam3-visual-q4_0 | 275 MB | **6.7** | 22.3 | 33.0 | 110.0 |

### EdgeTAM (RepViT backbone + Perceiver)

| Model | Size | Track/frame Metal (s) | Track/frame CPU (s) | Total Metal (s) | Total CPU (s) |
|-------|------|-----------------------|---------------------|-----------------|---------------|
| edgetam_f16 | 27 MB | **0.4** | 1.1 | 2.2 | 5.2 |
| edgetam_q8_0 | 19 MB | **0.4** | 1.1 | 2.1 | 5.1 |
| edgetam_q4_0 | 15 MB | **0.4** | 1.1 | 2.1 | 5.1 |

### SAM 2 / SAM 2.1 (Hiera backbone)

| Model | Size | Track/frame Metal (s) | Track/frame CPU (s) | Total Metal (s) | Total CPU (s) |
|-------|------|-----------------------|---------------------|-----------------|---------------|
| sam2_hiera_tiny_f16 | 75 MB | **0.9** | 2.7 | 4.0 | 12.6 |
| sam2_hiera_tiny_q8_0 | 40 MB | **0.9** | 2.5 | 4.0 | 11.7 |
| sam2_hiera_tiny_q4_0 | **22 MB** | **0.9** | 2.5 | 4.0 | 11.7 |
| sam2_hiera_small_f16 | 89 MB | **0.9** | 2.9 | 4.1 | 13.7 |
| sam2_hiera_small_q8_0 | 47 MB | **0.9** | 2.7 | 4.1 | 12.5 |
| sam2_hiera_small_q4_0 | 26 MB | **0.9** | 2.7 | 4.1 | 12.7 |
| sam2_hiera_base_plus_f16 | 155 MB | **1.0** | 4.2 | 4.7 | 20.2 |
| sam2_hiera_base_plus_q8_0 | 83 MB | - | 3.9 | - | 18.9 |
| sam2_hiera_large_f16 | 429 MB | - | 8.4 | - | 40.9 |
| sam2_hiera_large_q8_0 | 230 MB | - | 7.6 | - | 37.1 |
| | | | | | |
| sam2.1_hiera_tiny_f16 | 75 MB | **0.8** | 2.6 | 4.0 | 12.3 |
| sam2.1_hiera_tiny_q8_0 | 40 MB | **0.9** | 2.4 | 4.0 | 11.4 |
| sam2.1_hiera_tiny_q4_0 | **22 MB** | **0.9** | 2.5 | 4.0 | 11.5 |
| sam2.1_hiera_small_f16 | 89 MB | **0.9** | 2.9 | 4.1 | 13.5 |
| sam2.1_hiera_small_q8_0 | 47 MB | **0.9** | 2.7 | 4.1 | 12.5 |
| sam2.1_hiera_small_q4_0 | 26 MB | **0.9** | 2.7 | 4.1 | 12.6 |
| sam2.1_hiera_base_plus_f16 | 155 MB | **1.0** | 4.2 | 4.7 | 20.1 |
| sam2.1_hiera_base_pl