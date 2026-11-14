![gpu-unlock: full-speed tensor cores for GeForce RTX](assets/banner.svg)

### Your GeForce runs AI at half speed. This fixes it.

![Version](https://img.shields.io/badge/version-2.0.0-76b900)![RTX 20 | 30 | 40](https://img.shields.io/badge/GeForce-RTX%2020%20%7C%2030%20%7C%2040-76b900?logo=nvidia&logoColor=white)![Linux](https://img.shields.io/badge/platform-Linux-informational?logo=linux&logoColor=white)![License GPL-2.0](https://img.shields.io/badge/license-GPL--2.0-blue)![Stars](https://img.shields.io/github/stars/Zagitta/gpu-unlock?style=flat&color=yellow)

**Up to 2× FP16 / BF16 / TF32 tensor throughput** · **+25–55% LLM prefill** · **+25–50% fine-tuning** · **+30–55% image generation**

[Supported GPUs](#supported-gpus) · [Benchmarks](#what-you-get) · [Install](#how-to-install) · [FAQ](#faq) · [Support](#support-me)

---

NVIDIA ships GeForce cards with their tensor cores capped to **half speed** for
FP16, BF16 and TF32 math with FP32 accumulation, which is what nearly all AI
training and unquantized inference uses. The same silicon sold as an RTX A-series
or professional card runs at full rate. `gpu_unlock` removes that cap at boot,
before the stock NVIDIA driver loads. No patched driver, no VBIOS flash, nothing
to redo when NVIDIA releases a new driver.

---

## Supported GPUs

| Generation                | Cards                                                                                                                  | Status                    |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| **Ampere** (RTX 30)       | RTX 3050, 3060, 3060 Ti, 3070, 3070 Ti, 3080, 3080 Ti, 3090, 3090 Ti, plus RTX 3070/3080 Laptop GPUs                   | Stable, 100+ user reports |
| **Ada Lovelace** (RTX 40) | RTX 4060, 4060 Ti, 4070, 4070 SUPER, 4070 Ti, 4070 Ti SUPER, 4080, 4080 SUPER, 4090, 4090 D, RTX 4050/4060 Laptop GPUs | Experimental              |
| **Turing** (RTX 20)       | RTX 2060, 2060 SUPER, 2070, 2070 SUPER, 2080, 2080 SUPER, 2080 Ti, Titan RTX                                           | Experimental              |
| Blackwell (RTX 50)        |                                                                                                                        | Not supported             |

Laptops only stay unlocked if the dedicated GPU is never fully powered off.  
Many laptops power it down when idle, which silently resets the unlock. Turning  
off runtime power management with `options nvidia NVreg_DynamicPowerManagement=0x00`
in `/etc/modprobe.d/` helps on some models, but expect mixed results.

The exact PCI device IDs are in [`kernel/gpu_unlock/recipes.c`](kernel/gpu_unlock/recipes.c).
Linux only. For Windows see the [FAQ](#faq).

---

## What you get

The tensor core rate doubles. How much of that you see depends on how much of
your workload is FP16/BF16/TF32 matrix math, and on whether the card has the
power headroom to run it.

Dense matrix multiply (FP32 accumulation, stock power limits):

| Card | BF16 before | BF16 after | Gain |
| --- | --- | --- | --- |
| RTX 3060 12 GB | 27 TFLOPS | 51 TFLOPS | +87% |
| RTX 3060 Ti | 37 TFLOPS | 68 TFLOPS | +82% |
| RTX 3070 | 40 TFLOPS | 72 TFLOPS | +81% |
| RTX 3080 10 GB | 65 TFLOPS | 113 TFLOPS | +73% |
| RTX 3090 | 75 TFLOPS | 125 TFLOPS | +65% |
| RTX 3090 Ti (450 W) | 88 TFLOPS | 157 TFLOPS | +80% |
| RTX 4070 Ti | 81 TFLOPS | 150 TFLOPS | +84% |
| RTX 4080 | 104 TFLOPS | 193 TFLOPS | +87% |
| RTX 4090 | 165 TFLOPS | 329 TFLOPS | +100% (peak MMA rate) |

The RTX 4090 runs out of power before it runs out of tensor cores, so large
GEMMs at stock power limits gain much less than the peak rate suggests.

Real workloads:

| Workload | Typical speedup |
| --- | --- |
| LLM prefill / prompt processing, FP16/BF16 or AWQ/GPTQ (vLLM, PyTorch, Transformers) | +25–55% |
| Time to first token | 25–30% lower |
| LoRA and full fine-tuning in BF16 | +25–50% |
| Image generation, FP16/BF16 (SDXL, SD 1.5, Krea, DiT models in ComfyUI) | +30–55% |
| Video generation, BF16 compute (Wan 2.2) | +15–20% |
| FlashAttention / SDPA kernels | +50–60% |
| llama.cpp / Ollama with quantized GGUF | 0–15%, mostly at long context |
| LLM decode / token generation (memory bound) | No change |
| INT8, FP8 and INT4 models | No change |
| Gaming and FP32 CUDA | No change |

Outputs are bit-identical before and after; only the speed changes. These
numbers come from the [compatibility reports](https://github.com/Zagitta/gpu-unlock/issues)
users have filed, where you can find full benchmark details and post your own.

---

## How to install

First run:

```sh
git clone https://github.com/Zagitta/gpu-unlock
cd gpu-unlock
make install
```

Then append `gpu_unlock.targets=all` to your kernel command line, keeping
existing options:

- **GRUB (Debian/Ubuntu/Mint):** add it inside `GRUB_CMDLINE_LINUX_DEFAULT`
in `/etc/default/grub`, then run `sudo