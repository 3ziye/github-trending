# HipKittens

HipKittens is a repository in the ThunderKittens cinematic universe! This work provides minimal, opinionated C++ embedded programming primitives to help you write speedy AMD AI kernels. HipKittens is built from the hardware up: we do what the silicon tells us. 

<div align="center" >
    <img src="assets/hipkittens.png" height=250 alt="HipKittens logo" style="margin-bottom:px"/> 
      <p><em>HipKittens surfing the ~wave~ (not warp).</em></p>
</div>

<br>

**Links**: [Paper (arXiv)](https://arxiv.org/abs/2511.08083) | [Blog: Fast and Furious AMD Kernels](https://hazyresearch.stanford.edu/blog/2025-11-09-hk) | [Blog: AMD GPUs go brrr](https://hazyresearch.stanford.edu/blog/2025-11-09-amd-brr)

**AI has largely used a single hardware vendor in the past, but how can we enable a *multi-silicon* future?** Towards the dream of a single software framework that translates across hardware platforms, we explore whether the primitives used in prior DSLs (like TK) suffice for AMD, or whether we need entirely new primitives.

We find that core tile and bulk compute interfaces carry over from TK to HK, but decisions around memory access patterns, scheduling compute and memory, and ordering thread blocks within the chiplet architecture differ. HipKittens features the following types of primitives. 
1. **Tile primitives**: sized according to the tensor core units. Tile memory ops are coalesced, bank conflict free, and eagerly use tensor core layouts. We focus on minimizing address computation costs. 
2. **Python-inspired functions**: bulk compute functions that operate over tiles. These are lightweight, wrapping assembly and HIP.
3. **Asynchronous loads/stores**: hide latencies and address generation using direct buffer loads to shared memory.
4. **Scheduling and overlapping**: we show two core patterns for overlapping compute and memory, 8-wave ping pong and 4-wave interelave, that appear across kernels.

We support CDNA3 and CDNA 4. 

## Setup

```bash
# clone the repo
git clone git@github.com:HazyResearch/HipKittens.git
**or**
git clone https://github.com/HazyResearch/HipKittens.git

# obtain an amd docker using docker pull or podman pull
podman pull docker.io/rocm/7.0-preview:rocm7.0_preview_pytorch_training_mi35x_beta

# enter the docker
podman run -it \
    --ipc=host \
    --network=host \
    --privileged \
    --cap-add=CAP_SYS_ADMIN \
    --cap-add=SYS_PTRACE \
    --security-opt seccomp=unconfined \
    --device=/dev/kfd \
    --device=/dev/dri \
    -v $(pwd):/workdir/ \
    -e USE_FASTSAFETENSOR=1 \
    -e SAFETENSORS_FAST_GPU=1 \
    rocm/7.0-preview:rocm7.0_preview_pytorch_training_mi35x_beta \
    bash

# set the environment variables
cd HipKittens/
source env.src

# install aiter (baseline kernels)
git clone --recursive https://github.com/ROCm/aiter.git
cd aiter
python3 setup.py develop
```

## Unit tests

We provide unit tests for you to optionally test the correctness of library functions. 

```bash
cd HipKittens/tests/unit
make -j64
```

## Quick start: running kernels

We assume you will run the following on an MI350X or MI355X unless otherwise specified. You should use the CDNA3 branch of HK to run on the MI300X or MI325X.

1. **BF16 GEMM**
```bash
# Defaults to 8192x8192x8192
# This will compare to AITER and PyTorch automatically.
cd kernels/gemm/bf16fp32/mi350x/
make clean && make
python test_python.py

# On the mi300x or mi325x run:
git checkout cdna3 # not the main branch!
cd kernels/gemm/bf16fp32/mi325x/
make clean && make
python test_python.py
```

2. **Attention forwards (MHA, GQA, Causal, Non-causal, Head dim 128 / 64)**

```bash
# GQA, Non-causal, D=128, N=2048, H=64, H_KV=8, B=16:
# This will compare to AITER automatically. 
cd kernels/attn/gqa/
make clean && make
python test_python.py
```

- Modify the ```ATTN_N``` sequence length (e.g., 1024, 2048, 4096, 8192), ```ATTN_H``` query heads and ```ATTN_H_KV``` key value heads (e.g., 16 and 16 for MHA), ```ATTN_D``` head dimension (i.e., 64 or 128) in the Makefile and test_python.py file to try other settings.
- Use the same process for [gqa_causal](https://github.com/HazyResearch/HipKittens/tree/main/kernels/attn/gqa_causal).

3. **Attention backwards (MHA, GQA, Causal, Non-causal, Head dim 128 / 64)**

```bash
# GQA, Non-causal, D=128, N=8192, H=64, H_KV=8, B=16:
# This will compare to AITER automatically. 
cd kernels/attn/gqa_backwards/
make clean && make
python test_python.py 
```

- Modify the settings in the same way as stated above for forwards.
- Try [gqa_causal_backwards](https://github.com/HazyResearch/HipKittens/tree/main/kernels/attn/gqa_causal_backwards).

4. **Memory bound**

```bash
# Rotary (default B=16, H=16, D=128, N=2048)
# This will compare to AITER, PyTorch, PyTorch compiled automatically.
cd kernels/rotary/
make clean && make
python test_python.py
```

```bash
# Layernorm fused (default B=16, H=16, D=128, N=4096)
# This will compare to PyTorch, PyTorch compiled automatically.
cd kernels/layernorm/
make clean 