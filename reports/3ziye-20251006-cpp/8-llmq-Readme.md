# LLM.Q
Quantized LLM training in pure CUDA/C++.

## Overview
`llm.q` is an implementation of (quantized) large language model training in CUDA, inspired by [llm.c](https://github.com/karpathy/llm.c). It is particularly aimed at medium-sized training setups, i.e., a single node with multiple GPUs.

## Build instructions
The code is written in C++20 and requires CUDA 12 or later.  It depends on [nccl](https://developer.nvidia.com/nccl) for communication, and [cudnn](https://developer.nvidia.com/cudnn) for fast attention. Multi-GPU training can either be run in multi-process mode (requires OpenMPI) or in multi-thread mode. On a recent ubuntu system, this should provide
the required dependencies (adapt cuda version as needed):
```´shell
# build tools
apt install cmake ninja-build git gcc-13 g++-13
# libs
apt install cuda-12-8 cudnn9-cuda-12-8 libnccl2 libnccl-dev libopenmpi-dev
```

Additional header-only dependencies are automatically downloaded by cmake during the build process.
These are:
* [json](https://github.com/nlohmann/json)
* [cudnn-frontend](https://github.com/NVIDIA/cudnn-frontend)
* [CLI11](https://github.com/CLIUtils/CLI11)

To build the training executable, run
```shell
mkdir build
cmake -S . -B build
cmake --build build --parallel --target train
```

## How to train your (quantized) llm
### Data preparation
In order to train/fine-tune a model, you first need some data. The [tokenize_data](tokenize_data.py) script provides a utility to prepare token files for training.
It only supports a limited number of datasets, but hacking it for your own dataset should be straightforward.
```shell
uv run tokenize_data.py --dataset tiny-shakespeare --model qwen
```
This will create `tiny-shakespeare-qwen-train.bin` and `tiny-shakespeare-qwen-eval.bin`.

### Training run
Let's fine-tune the smallest Qwen model on this data:
```shell
./build/train --model=Qwen/Qwen2.5-0.5B \
  --train-file=data/tiny-shakespeare-qwen/train.bin \
  --eval-file=data/tiny-shakespeare-qwen/eval.bin \
  --model-dtype=bf16 --opt-m-dtype=bf16 --opt-v-dtype=bf16 \
  --matmul-dtype=e4m3 \
  --recompute-ffn --recompute-att \
  --grad-accumulation=8 --steps=30 \
  --learning-rate=1e-5 --gpus=1 --batch-size=8
```
The program will print some logging information, such as the following:
```text
[Options]
  recompute-swiglu  : true
  recompute-norm    : false
  [...]

[System 0]
  Device 0: NVIDIA GeForce RTX 4090
  CUDA version: driver 13000, runtime 13000
  Memory: 906 MiB / 24080 MiB
  
Loading model from `/huggingface/hub/models--Qwen--Qwen2.5-0.5B/snapshots/060db6499f32faf8b98477b0a26969ef7d8b9987/model.safetensors`
 done
 
[Dataset]
 train:  329k tokens
   data/tiny-shakespeare-qwen/train.bin :     329663
 eval:   33k tokens
   data/tiny-shakespeare-qwen/eval.bin :      33698

[Allocator State]
        Adam V:   942 MiB
        Adam M:   942 MiB
     Gradients:   942 MiB
   Activations:  4505 MiB
        Master:   682 MiB
       Weights:   601 MiB
          Free: 14078 MiB
      Reserved:   483 MiB
         Other:   903 MiB
```

If `[Allocator State]` shows a lot of `Free` memory (as it does here), you can try increasing the batch size (and adjust `--grad-accumulation` accordingly), or reduce the amount of activation checkpointing.
For example, on a 16GiB 4060Ti, `--recompute-ffn --recompute-att` can be replaced by `--recompute-swiglu`, which increases the activation memory from `4.5 GiB` to `9 GiB`, and
the speed from ~11k tps to ~13k tps.

Then, the actual training will begin:
````text
[T] step     0 [ 19.9%] | time:  1869 ms | norm   4.315545 | loss   3.282568 | tps 35064 | sol 42.9%
[T] step     1 [ 39.8%] | time:  1709 ms | norm   8.423664 | loss   3.310652 | tps 38347 | sol 46.9%
[T] step     2 [ 59.6%] | time:  1708 ms | norm   4.818971 | loss   3.330125 | tps 38370 | sol 47.0%
[T] step     3 [ 79.5%] | time:  1715 ms | norm   5.247286 | loss   3.259991 | tps 38213 | sol 46.8%
[V] step     4 [  0.0%] | time:   165 ms | eval   2.945187 | train  3.295834 | tps  148k
````
Each `[T]` line is a training step (in contrast to `[V]` validation). It shows the step number, the progress within the epoch,
the elapsed time, as well as the current loss and gradient norm. It also calculates the current throuput in tokens per second,
and sets this in relation to the GPU's speed of light (SOL), i.e., the fastest possible speed if the GPU was only running strictly necessary matmuls at peak flop/s.

### Inspecting the logs
After 50 steps, the training will finish, and save the final model to `model.safetensors`. In addition, a log file will be created,
which contains the training log in JSON format. We can visualize the log using the `plot-training-run.py` utility script:`
```shell
uv run python/plot-training-run.py log.json
```
This shows the training and evaluation losses over time, for quick inspection.
For a more detailed and interactive workflow, you can export the log to weights&biases:
```shell
uv run python/export-wandb.py --log-file log.jso