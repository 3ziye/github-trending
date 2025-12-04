# Supertonic — Lightning Fast, On-Device TTS

[![Demo](https://img.shields.io/badge/🤗%20Hugging%20Face-Demo-yellow)](https://huggingface.co/spaces/Supertone/supertonic#interactive-demo)
[![Models](https://img.shields.io/badge/🤗%20Hugging%20Face-Models-blue)](https://huggingface.co/Supertone/supertonic)

<p align="center">
  <img src="img/Supertonic_IMG_v02_4x.webp" alt="Supertonic Banner">
</p>

**Supertonic** is a lightning-fast, on-device text-to-speech system designed for **extreme performance** with minimal computational overhead. Powered by ONNX Runtime, it runs entirely on your device—no cloud, no API calls, no privacy concerns.

## Demo

### Raspberry Pi

Watch Supertonic running on a **Raspberry Pi**, demonstrating on-device, real-time text-to-speech synthesis:

https://github.com/user-attachments/assets/ea66f6d6-7bc5-4308-8a88-1ce3e07400d2

### E-Reader

Experience Supertonic on an **Onyx Boox Go 6** e-reader in airplane mode, achieving an average RTF of 0.3× with zero network dependency:

https://github.com/user-attachments/assets/64980e58-ad91-423a-9623-78c2ffc13680

---

> 🎧 **Try it now**: Experience Supertonic in your browser with our [**Interactive Demo**](https://huggingface.co/spaces/Supertone/supertonic#interactive-demo), or get started with pre-trained models from [**Hugging Face Hub**](https://huggingface.co/Supertone/supertonic)

## 📰 Update News

**2025.11.24** - Added Flutter SDK support with macOS compatibility

### Table of Contents

- [Why Supertonic?](#why-supertonic)
- [Language Support](#language-support)
- [Getting Started](#getting-started)
- [Performance](#performance)
- [Citation](#citation)
- [License](#license)

## Why Supertonic?

- **⚡ Blazingly Fast**: Generates speech up to **167× faster than real-time** on consumer hardware (M4 Pro)—unmatched by any other TTS system
- **🪶 Ultra Lightweight**: Only **66M parameters**, optimized for efficient on-device performance with minimal footprint
- **📱 On-Device Capable**: **Complete privacy** and **zero latency**—all processing happens locally on your device
- **🎨 Natural Text Handling**: Seamlessly processes numbers, dates, currency, abbreviations, and complex expressions without pre-processing
- **⚙️ Highly Configurable**: Adjust inference steps, batch processing, and other parameters to match your specific needs
- **🧩 Flexible Deployment**: Deploy seamlessly across servers, browsers, and edge devices with multiple runtime backends.

## Language Support

We provide ready-to-use TTS inference examples across multiple ecosystems:

| Language/Platform | Path | Description |
|-------------------|------|-------------|
| [**Python**](py/) | `py/` | ONNX Runtime inference |
| [**Node.js**](nodejs/) | `nodejs/` | Server-side JavaScript |
| [**Browser**](web/) | `web/` | WebGPU/WASM inference |
| [**Java**](java/) | `java/` | Cross-platform JVM |
| [**C++**](cpp/) | `cpp/` | High-performance C++ |
| [**C#**](csharp/) | `csharp/` | .NET ecosystem |
| [**Go**](go/) | `go/` | Go implementation |
| [**Swift**](swift/) | `swift/` | macOS applications |
| [**iOS**](ios/) | `ios/` | Native iOS apps |
| [**Rust**](rust/) | `rust/` | Memory-safe systems |
| [**Flutter**](flutter/) | `flutter/` | Cross-platform apps |

> For detailed usage instructions, please refer to the README.md in each language directory.

## Getting Started

First, clone the repository:

```bash
git clone https://github.com/supertone-inc/supertonic.git
cd supertonic
```

### Prerequisites

Before running the examples, download the ONNX models and preset voices, and place them in the `assets` directory:

> **Note:** The Hugging Face repository uses Git LFS. Please ensure Git LFS is installed and initialized before cloning or pulling large model files.
> - macOS: `brew install git-lfs && git lfs install`
> - Generic: see `https://git-lfs.com` for installers

```bash
git clone https://huggingface.co/Supertone/supertonic assets
```

### Quick Start

**Python Example** ([Details](py/))
```bash
cd py
uv sync
uv run example_onnx.py
```

**Node.js Example** ([Details](nodejs/))
```bash
cd nodejs
npm install
npm start
```

**Browser Example** ([Details](web/))
```bash
cd web
npm install
npm run dev
```

**Java Example** ([Details](java/))
```bash
cd java
mvn clean install
mvn exec:java
```

**C++ Example** ([Details](cpp/))
```bash
cd cpp
mkdir build && cd build
cmake .. && cmake --build . --config Release
./example_onnx
```

**C# Example** ([Details](csharp/))
```bash
cd csharp
dotnet restore
dotnet run
```

**Go Example** ([Details](go/))
```bash
cd go
go mod download
go run example_onnx.go helper.go
```

**Swift Example** ([Details](swift/))
```bash
cd swift
swift build -c release
.build/release/example_onnx
```

**Rust Example** ([Details](rust/))
```bash
cd rust
cargo build --release
./target/release/example_onnx
```

**iOS Example** ([Details](ios/))
```bash
cd ios/ExampleiOSApp
xcodegen generate
open ExampleiOSApp.xcodeproj
```
- In Xcode: Targets → ExampleiOSApp → Signing: 