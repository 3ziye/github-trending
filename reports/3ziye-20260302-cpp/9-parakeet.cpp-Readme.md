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

Choose decoder at call site:
```cpp
auto result = t.transcribe("audio.wav", parakeet::Decoder::CTC);  // fast greedy
auto result = t.transcribe("audio.wav", parakeet::Decoder::TDT);  // better accuracy (default)
```

Batch transcription (multiple files in one forward pass):
```cpp
auto results = t.transcribe_batch({"audio1.wav", "audio2.wav", "audio3.wav"});
for (const auto &r : results)
    std::cout << r.text << std::endl;
```

Word-level timestamps with confidence:
```cpp
auto result = t.transcribe("audio.wav", parakeet::Decoder::TDT, /*timestamps=*/true);
for (const auto &w : result.word_timestamps) {
    std::cout << "[" << w.start << "s - " << w.end << "s] "
              << "(" << w.confidence << ") " << w.word << std::endl;
}
// [0.24s - 0.48s] (0.98) Well
// [0.48s - 0.56s] (0.95) I
// [0.56s - 0.96s] (0.87) don't
```

Phrase boosting for domain-specific vocabulary:
```cpp
parakeet::TranscribeOptions opts;
opts.boost_phrases = {"Phoebe", "portrait"};
opts.boost_score = 5.0f;  // log-prob bias (default)
auto result = t.transcribe("audio.wav", opts);
```

## High-Level API

### Offline Transcription (TDT-CTC 110M)

```cpp
parakeet::Transcriber t("model.safetensors", "vocab.txt");
t.to_gpu();
auto result = t.transcribe("audio.wav");
```

### Batch Transcription

Process multiple audio files in a single batched encoder forward pass for better GPU utilization:

```cpp
parakeet::Transcriber t("model.safetensors", "vocab.txt");
t.to_gpu();

auto results = t.transcribe_batch({"audio1.wav", "audio2.wav", "audio3.wav"});
for (size_t i = 0; i < results.size(); ++i)
    std::cout << results[i].text << std::endl;

// Works with options too
parakeet::TranscribeOptions opts;
opts.timestamps = true;
auto results = t.transcribe_batch({"a.wav", "b.wav"}, opts);
```

Also available on `TDTTranscriber` for the 600M model, via C API (`parakeet_transcriber_transcribe_batch`), and the CLI (multiple positional args).

### Offline Transcription (TDT 600M Multilingual)

```cpp
parakeet::TDTTranscriber t("model.safetensors", "vocab.txt",
                            parakeet::make_tdt_600m_config());
auto result = t.transcribe("audio.wav");
```

### Streaming Transcription (EOU 120M)

```cpp
parakeet::StreamingTranscriber t("model.safetensors", "vocab.txt",
                                  parakeet::make_eou_120m_config());

// Feed audio chunks (e.g., from microphone)
while (auto chunk = get_audio_chunk()) {
    auto text = t.transcribe_chunk(chunk);
    if (!text.empty()) std::cout << text << std::flush;
}
std::cout << t.get_text() << std::endl;
```

### Streaming Transcription (Nemotron 600M)

```cpp
// Latency modes: 0=80ms, 1=160ms, 6=560ms, 13=1120ms
auto cfg = parakeet::make_nemotron_600m_config(/*latency_frames=*/1);
parakeet::NemotronTranscriber t("model.safetensors", "vocab.txt", cfg);

while (auto chunk = get_audio_chunk()) {
    auto text = t.transcribe_chunk(chunk);
    if (!text.empty()) std::cout << text << std::flush;
}
```

### Speaker Diarization (Sortformer 117M)

Identify who spoke when — detects up to 4 speakers with per-frame activity probabilities:

```cpp
parakeet::Sortformer model(parakeet::make_sortformer_117m_config());
model.load_state_dict(axiom::io::safetensors::load("sortformer.safetensors"));

auto audio = parakeet::read_audio("meeting.wav");
auto features = parakeet::preprocess_audi