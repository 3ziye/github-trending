<h1 align="center">Large MoE models, powered by your SSD</h1>

<p align="center">
  <a href="https://wici.ai">
    <img src="docs/assets/wicissdinfer.png" width="600" alt="InferSSD">
  </a>
</p>

<p align="center">
  <a href="https://wici.ai/inferssd"><b>Website</b></a> &nbsp;·&nbsp;
  <a href="https://wici.ai/research"><b>Blog</b></a> &nbsp;·&nbsp;
  <a href="https://join.slack.com/t/wici-ai/shared_invite/zt-4f2e7ob2s-9nUg35Phqyqt4EI6qUjw5w"><b>Slack</b></a> &nbsp;·&nbsp;
  <a href="LICENSE">Apache-2.0</a>
</p>
<p align="center">macOS / Metal &nbsp;·&nbsp; Linux / CUDA &nbsp;·&nbsp; Windows (in progress)</p>

**Run models larger than your RAM or VRAM.** InferSSD builds on [llama.cpp](https://github.com/ggml-org/llama.cpp) to run large mixture-of-experts (MoE) models from SSD, using standard GGUF files, with browser chat and an OpenAI-compatible API. It supports **DeepSeek-V4.1-Flash-1017**, **Muse-Spark-Open**, **Qwen3.6-35B-A3B** and **Qwen3.8 Flash Next**, plus ordinary RAM inference for **Gemma4 E4B**.

## Models

These are the tested GGUF files, community conversions of the named model releases. DeepSeek's Q8_0 keeps the official bit widths: routed experts stay native 4-bit MXFP4, and FP8 tensors become 8-bit Q8_0. See [weight-format details](docs/benchmark.md#checkpoint-formats).

| Model | Parameter count | GGUF reference |
| --- | --- | --- |
| DeepSeek-V4.1-Flash-1017 | 763B total / 8–16B active | [mrfakename · Q8_0](https://huggingface.co/mrfakename/DeepSeek-V4.1-Flash-1017-GGUF) |
| Muse-Spark-Open | 816B total / 42B active | [Unsloth · UD-Q4_K_XL](https://huggingface.co/unsloth/Muse-Spark-Open-816B-A42B-GGUF) |
| Qwen3.6-35B-A3B | 35B total / 3B active | [Unsloth · UD-Q4_K_XL](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF) |
| Qwen3.8 Flash Next | 177B total / A3B | [Bartowski · IQ4_XS](https://huggingface.co/bartowski/Qwen3.8-Flash-Next-GGUF) |
| Gemma4 E4B | 7.46B total / E4B | [Google · QAT Q4_0](https://huggingface.co/google/gemma-4-E4B-it-qat-q4_0-gguf) |

Gemma uses the ordinary native loader without SSD expert offload. Before loading, the shared
launcher checks that weights, KV cache and working memory fit the memory budget, the machine's
physical memory unless a smaller one is configured; the system pages other memory out to make
room. On Apple silicon the per-layer embedding table, 2.15 GiB of the 4.80 GiB file, stays in the
file and its rows are read from the SSD as tokens use them; the other weights are held in memory.
A model that does not fit is rejected. macOS and Windows use the same model selection and launch
entry points.

## Performance benchmarks

**4K prompt tier · 256 output tokens · decode measured over tokens 129–256.** All rates are in **token/s**; higher is faster. The multiple next to each **InferSSD** rate is its speedup over llama.cpp on the same hardware. On the MacBook Pro, Colibri runs the official Safetensors on CPU; llama.cpp and InferSSD run the GGUF with Metal. See [measurement details](docs/benchmark.md).

### Test hardware

| Hardware | CPU (cores) | GPU | Memory | SSD |
| --- | --- | --- | --- | --- |
| MacBook&nbsp;Pro | Apple&nbsp;M5&nbsp;Max&nbsp;(18) | 40-core | 48&nbsp;GB&nbsp;unified | 2&nbsp;TB&nbsp;internal |
| RTX&nbsp;5060&nbsp;Ti | Intel&nbsp;Core&nbsp;3&nbsp;100U&nbsp;(6) | RTX&nbsp;5060&nbsp;Ti | 8&nbsp;GB&nbsp;+&nbsp;16&nbsp;GB&nbsp;VRAM | 2&nbsp;TB&nbsp;PCIe&nbsp;4&nbsp;×4 |
| RTX&nbsp;5090 | Intel&nbsp;Core&nbsp;Ultra&nbsp;5&nbsp;230F&nbsp;(10) | RTX&nbsp;5090 | 32&nbsp;GB&nbsp;+&nbsp;32&nbsp;GB&nbsp;VRAM | 2&nbsp;TB&nbsp;PCIe&nbsp;5&nbsp;×4 |
| DGX&nbsp;Spark | NVIDIA&nbsp;GB10&nbsp;(20) | Blackwell | 128&nbsp;GB&nbsp;unified | 4&nbsp;TB&nbsp;PCIe&nbsp;5&nbsp;×4 |

Unified memory is shared by the CPU and GPU. SSD capacities are nominal. See [hardware details](docs/benchmark.md#hardware-details) for SSD models, CPU core layouts, and configuration notes.

### DeepSeek-V4.1-Flash-1017

<table>
<thead>
<tr><th rowspan="2">Hardware</th><th colspan="3">Prefill (token/s)</th><th colspan="3">Decode (token/s)</th></tr>
<tr><th>llama.cpp</th><th>Colibri</th><th>InferSSD</th><th>llama.cpp</th><th>Colibri</th><th>InferSSD</th></tr>
</thead>
<tbody>
<tr><td>MacBook&nbsp;Pro</td><td align="right">5.929</td><td align="right">0.708</td><td align="right"><b>28.766</b>&nbsp;(4.85×)</td><td align="right">0.873</td><td align="right">0.437</td><td align="right"><b>2.874</b>&nbsp;(3.29×)</td></tr>
<tr><td>RTX 5060 Ti</td><td align="right">6.950</td><td align="right">7.020</td><td align="right"><b>75.100</b>&nbsp;(10.81×)</td><td align="right">0.242</td><td align="right">0.900</td><td align="right"><b>2.550</b>&nbsp;(10.54×)</td></tr>
<tr><td>RTX 5090</td><td align="right">8.060</td><td align="right">39.210</td><td align="right"><b>164.500</b>&nbsp;(20.41×)</td><td align="right">0.867</td><td align="right">1.878</td><td align="right"><b>7.270</b>&nbsp;(8.39×)</td></tr>
<tr><td>DGX Spark</td><td align="right">2.730</td><td align="right">0.826</td><td align="r