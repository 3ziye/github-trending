# rvLLM

LLM inference engine. Rust+CUDA on GPU, JAX+XLA on TPU.

Three Gemma 4 models on TPU v6e-4: **E4B** (16,794 tok/s peak, 78.3 tok/s B=1, PPL 5.87), **26B-A4B MoE** (14,899 tok/s peak), **31B** (9,600 tok/s peak, 128K context). GPU: 31B on H100 at **8,786 tok/s** (FP8, CUDA graph, PPL 14.75). Zero custom kernels on TPU -- ~500 lines of JAX. Native Rust binary on GPU -- zero Python in the serving path.

**[Full benchmarks](https://docs.solidsf.com/docs/bench.html)**

## At a glance

| | E4B (4B) | 26B-A4B (MoE) | 31B TPU | 31B GPU | vLLM H100 |
|---|---|---|---|---|---|
| **B=1 tok/s** | **78.3** | 52.9 | 44.2 | 53 | 66.9 |
| **Peak tok/s** | **16,794** | 14,899 | 9,600 | 8,786 | 3,848 |
| **PPL** | **5.87** | 90.21 | 24.76 | 14.75 | - |
| **Cached TTFT** | **25.9 ms** | 35.3 ms | 73.3 ms | 63 ms | - |
| **Peak tok/s/$** | **3,230** | 2,865 | 1,846 | 4,576 | 2,004 |

TPU: v6e-4, $5.20/hr, int8, max-ctx 2048. GPU: H100 SXM, $1.92/hr, FP8. All measured.

## TPU: Gemma 4 on v6e-4

Pure JAX + XLA. No custom kernels. XLA compiles the entire forward pass to TPU machine code from a ~500 line JAX script. Three models, one codebase.

### Models supported

| Property | E4B (4B) | 26B-A4B (MoE) | 31B |
|---|---|---|---|
| Total / active params | ~4B / 4B | 26B / ~4B | 31B / 31B |
| Layers | 42 | 30 | 60 |
| Hidden size | 2,560 | 2,816 | 5,376 |
| Q / KV heads (sliding) | 8 / 2 | 16 / 8 | 32 / 16 |
| Q / KV heads (global) | 8 / 2 | 16 / 2 (V=K) | 32 / 4 (V=K) |
| Head dim (sliding / global) | 256 / 512 | 256 / 512 | 256 / 512 |
| Sliding window | 512 | 1,024 | 1,024 |
| MoE | none | 128 experts, top-8 | none |
| KV-shared layers | 18 (of 42) | 0 | 0 |
| Per-layer input injection | 256-d gated (5.6 GB embed) | none | none |

### Batch scaling (max-ctx 2048)

| Batch | E4B tok/s | 26B-A4B tok/s | 31B tok/s | vLLM H100 |
|---|---|---|---|---|
| 1 | 78 | 53 | 44 | 66.9 |
| 8 | 542 | 390 | 318 | 515 |
| 64 | 3,661 | 2,662 | 2,112 | 2,794 |
| 128 | 6,298 | 4,915 | 3,853 | 3,848 |
| 256 | 10,214 | 8,192 | 6,246 | 3,709 |
| 512 | 13,773 | 12,390 | 8,550 | 3,788 |
| **768** | **15,514** | **14,899** | **9,600** | 3,671 |
| **1024** | **16,794** | - | - | - |

### 31B context scaling (B=1)

| Context | ms/step | tok/s | Architecture | KV type |
|---|---|---|---|---|
| 512 | 12.79 | 78.2 | Single-scan, 60-layer scan + cond | bf16 |
| 2,048 | 22.6 | 44.2 | Single-scan | bf16 |
| 32K | ~66 | ~15 | Single-scan | bf16 |
| 64K | ~91 | ~11 | Split-cache, 10 groups x 6 | int8 |
| 128K | 40.56 | 24.7 | Split-cache + blockwise global | int8 |

Dual-path architecture auto-switches at the 32K boundary.

### TPU deployment

```bash
# Create TPU v6e-4 ($5.20/hr)
gcloud compute tpus tpu-vm create rvllm-gemma4 \
  --zone=us-east5-b --accelerator-type=v6e-4 --version=v2-alpha-tpuv6e \
  --boot-disk-size=200

# Install (30 seconds)
pip3 install 'jax[tpu]' huggingface_hub tokenizers \
  -f https://storage.googleapis.com/jax-releases/libtpu_releases.html

# Download model
huggingface-cli download google/gemma-4-E4B-it --local-dir ~/models/gemma-4-E4B-it

# Run E4B (78.3 tok/s B=1)
python3 tpu/harness/gemma4_tpu_infer.py \
  --model-dir ~/models/gemma-4-E4B-it --max-tokens 200 --max-ctx 2048

# Run 31B batched (9,600 tok/s B=768)
LIBTPU_INIT_ARGS="--xla_tpu_enable_async_collective_fusion=true \
  --xla_tpu_enable_async_collective_fusion_fuse_all_gather=true \
  --xla_tpu_enable_async_collective_fusion_multiple_steps=true \
  --xla_tpu_overlap_compute_collective_tc=true \
  --xla_tpu_scoped_vmem_limit_kib=131072" \
python3 tpu/harness/gemma4_tpu_infer.py \
  --model-dir ~/models/gemma-4-31B-it --fused --max-tokens 200 --max-ctx 2048 --batch 768

# 128K context (24.7 tok/s)
python3 tpu/harness/gemma4_tpu_infer.py \
  --model-dir ~/models/gemma-4-31B-it --fused --max-tokens 200 --max-ctx 131072

# API server (OpenAI-compatible)
python3 tpu/harness/api_server.py --model-dir ~/models/gemma-4-31B-it --port 8080

# Perplexity
python3 tpu/harness/gemma4_tpu_infer.py \
  --model-dir ~/models/gemma-4-31B-it --perplexity --max-ctx 2048
```

No Docker. No conda. No torch. No vLLM. One pip install, one Python file, one command.


## EAGLE-3 Speculative Decoding (TPU, experimental)

450M-param draft head proposes K=5 tokens per cycle; the full 31B verifies K+1=6 in one forward pass. Lossless for greedy decode.

| Metric | Value |
|---|---|
| Baseline (B=1, 512 ctx) | 78.2 tok/s, 12.79 ms/step |
| EAGLE-3 fused cycle | 31.0 ms/cycle |
| Projected @ tau=3.5 | ~145 tok/s (1.8x) |
| Hardware ceiling | ~300 tok/s (3.8x) |

Requires 50K+ training examples for production tau. Current: 2K examples, loss 7.1, pipeline validated end-to-end. See [`tpu/harness/EAGLE3_SPEC.md`](tpu/harness/EAGLE3_SPEC.md).


## GPU: 31B Gemma 4 on H100

Rust + CUDA on H100 SXM 80GB. FP8 weights with per-channel scales + CUTLASS channelscale epilogue, F16 KV cache, F16 paged attention (FA3 SM90). All 60 layers captured in a single CUDA graph (~935 nodes). **8,786 tok/s** peak (B=512), **