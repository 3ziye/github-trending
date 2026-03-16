# parakeet.cpp

Fast speech recognition with NVIDIA's [Parakeet](https://huggingface.co/collections/nvidia/parakeet) models in pure C++.

Built on [axiom](https://github.com/frikallo/axiom) — a lightweight tensor library with automatic Metal GPU acceleration. No ONNX runtime, no Python runtime, no heavyweight dependencies. Just C++ and one tensor library that outruns PyTorch MPS.

**~27ms encoder inference on Apple Silicon GPU** for 10s audio (110M model) — 96x faster than CPU. FP16 support for ~2x memory reduction.

## Supported Models

| Model | Class | Size | Type | Description |
|-------|-------|------|------|-------------|
| `tdt-ctc-110m` | `ParakeetTDTCTC` | 110M | Offline | English, dual CTC/TDT decoder heads |
| `tdt-600m` | `ParakeetTDT` | 600M | Offline | Multilingual, TDT decoder |
| `eou-120m` | `ParakeetEOU` | 120M | Streaming | English, RNNT with end-of-utterance detection |
| `nemotron-600m` | `ParakeetNemotron` | 600M | Streaming | Multilingual, configurable latency (80ms–1120ms) |
| `sortformer` | `Sortformer` | 117M | Streaming | Speaker diarization (up to 4 speakers) |
| `diarized` | `DiarizedTranscriber` | 110M+117M | Offline | ASR + diarization → speaker-attributed words |

All ASR models share the same audio pipeline: 16kHz mono WAV → 80-bin Mel spectrogram → FastConformer encoder.

## Quick Start

```cpp
#include <parakeet/parakeet.hpp>

parakeet::Transcriber t("model.safetensors", "vocab.txt");
t.to_gpu();   // optional — Metal acceleration
t.to_half();  // optional — FP16 inference (~2x memory reduction)

auto result = t.transcribe("audio.wav");
std::cout << result.text << std::endl;
```

## Features

- **Multiple decoders** — CTC greedy, TDT greedy, CTC beam search, TDT beam search (switch at call site)
- **Word timestamps** — Per-word start/end times and confidence scores on all decoders
- **Beam search + LM** — CTC and TDT beam search with optional ARPA n-gram language model fusion
- **Phrase boosting** — Context biasing via token-level trie for domain-specific vocabulary
- **Batch transcription** — Multiple files in one batched encoder forward pass
- **VAD preprocessing** — Silero VAD strips silence before ASR; timestamps auto-remapped
- **GPU acceleration** — Metal via axiom's MPSGraph compiler (96x speedup on Apple Silicon)
- **FP16 inference** — Half-precision weights and compute (~2x memory reduction)
- **Streaming** — EOU and Nemotron models with chunked audio input
- **Speaker diarization** — Sortformer (up to 4 speakers), combinable with ASR for speaker-attributed words
- **C API** — Flat `extern "C"` FFI for Python, Swift, Go, Rust, and other languages
- **Multi-format audio** — WAV, FLAC, MP3, OGG with automatic resampling

See [examples/](examples/) for code demonstrating each feature.

## Build

```bash
git clone --recursive https://github.com/frikallo/parakeet.cpp
cd parakeet.cpp
make build
make test
```

Requirements: C++20 (Clang 14+ or GCC 12+), CMake 3.20+, macOS 13+ for Metal GPU.

## Convert Weights

```bash
# Download from HuggingFace
huggingface-cli download nvidia/parakeet-tdt_ctc-110m --include "*.nemo" --local-dir .

# Convert to safetensors
pip install safetensors torch
python scripts/convert_nemo.py parakeet-tdt_ctc-110m.nemo -o model.safetensors
```

The converter supports all model types: `110m-tdt-ctc` (default), `600m-tdt`, `eou-120m`, `nemotron-600m`, `sortformer`.

```bash
python scripts/convert_nemo.py checkpoint.nemo -o model.safetensors --model 600m-tdt
```

Silero VAD weights:
```bash
python scripts/convert_silero_vad.py -o silero_vad_v5.safetensors
```

## Examples

| Example | Description |
|---------|-------------|
| [basic](examples/basic/) | Simplest transcription (~20 lines) |
| [timestamps](examples/timestamps/) | Word/token timestamps with confidence |
| [beam-search](examples/beam-search/) | CTC/TDT beam search with optional ARPA LM |
| [phrase-boost](examples/phrase-boost/) | Context biasing for domain vocabulary |
| [batch](examples/batch/) | Batch transcription of multiple files |
| [vad](examples/vad/) | Standalone VAD and ASR+VAD preprocessing |
| [gpu](examples/gpu/) | Metal GPU + FP16 with timing comparison |
| [stream](examples/stream/) | EOU streaming transcription |
| [nemotron](examples/nemotron/) | Nemotron streaming with latency modes |
| [diarize](examples/diarize/) | Sortformer speaker diarization |
| [diarized-transcription](examples/diarized-transcription/) | ASR + diarization combined |
| [c-api](examples/c-api/) | Pure C99 FFI usage |
| [cli](examples/cli/) | Full CLI with all options |

## Using as a Library

### CMake `find_package`

After installing (`make install` or `cmake --install build`):

```cmake
find_package(Parakeet REQUIRED)
target_link_libraries(myapp PRIVATE Parakeet::parakeet)
```

### CMake `add_subdirectory`

```cmake
add_subdirectory(third_party/parakeet.cpp)
target_link_libraries(myapp PRIVATE Parakeet::parakeet)
```

### pkg-config

```bash
g++ -std=c++20 myapp.cpp $(pkg-config --cflags --libs p