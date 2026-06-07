![](./assets/banner.png)

# HRM-Text: Efficient Pretraining Beyond Scaling

<p align="center">
  <a href="https://arxiv.org/pdf/2605.20613"><img src="https://img.shields.io/badge/Paper-arXiv-red?logo=arxiv&logoColor=white" alt="arXiv Paper"></a>
  <a href="https://huggingface.co/sapientinc/HRM-Text-1B"><img src="https://img.shields.io/badge/Model-HuggingFace-yellow" alt="Model"></a>
</p>

<p align="center"><strong>🌟 Pretrain a foundation model from scratch with ~$1000. 🌠</strong></p>

HRM-Text is a 1B text generation model based on the HRM architecture, strengthened by task completion and latent space reasoning. It offers a full pretraining framework, making foundation model pretraining accessible with 130-600x less compute and 150-900x less data. It is built upon a hierarchical recurrent architecture, PrefixLM sequence packing, FlashAttention 3 kernels, PyTorch FSDP2 training, evaluation, and checkpoint conversion tooling.

**Join 1200+ HRM Developers on Our Discord Community: [https://discord.gg/sapient](https://discord.gg/sapient)**

![](./assets/benchmark_scatter.png)

## Launch the Pretraining 🚀

### Required Resources

Choose a target size and prepare the corresponding GPU nodes.

- **L, 0.6B parameters:** 8 H100s, single node, about 50 hours (~$800).
- **XL, 1B parameters:** 16 H100s, two nodes, about 46 hours (~$1472).

*Price estimation based on $2/H100 hour.*

The following are benchmark results from the reference runs.

| Size | GPUs | Time | GSM8k | MATH | DROP | MMLU | ARC-C | HellaSwag | Winogrande | BoolQ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **L (0.6B)** | 8 | 50 hrs | 77.6% | 51.2% | 78.6% | 56.6% | 75.9% | 52.7% | 67.6% | 85.0% |
| **XL (1B)** | 16 | 46 hrs | 84.7% | 56.5% | 82.3% | 60.7% | 81.9% | 63.4% | 72.4% | 86.2% |

> Hopper-class GPUs are the expected training target because the attention path depends on FlashAttention 3.

### 1. Prepare Data

HRM-Text trains from sampled, tokenized data produced by the companion `data_io` pipeline. Use `data_io` to clean, tokenize, and stratified-sample the pretraining corpus, then point HRM-Text at the sampled output.

<p align="center">
  <a href="https://github.com/sapientinc/data_io"><img alt="data_io" src="https://img.shields.io/badge/GitHub-sapientinc%2Fdata__io-181717?logo=github&logoColor=white"></a>
</p>

Recommended setups:

1. **Single node:** run the data pipeline and pretraining on the same node. After tokenization, stratified-sample into that node's shared memory at `/dev/shm/sampled`.
2. **Multi-node:** keep `data_io` and the tokenized data on shared storage. Mount or expose that directory on every pretraining node, then run stratified sampling independently on each node. Sampling is fast and deterministic, so every node produces the same in-memory training data.

Please first setup `data_io`, then run the pipeline. After tokenization, run stratified sampling on each training node.

```bash
cd <DATA_IO_PATH>
python sample_tokenized.py epochs=4 output_path=/dev/shm/sampled > show_analytics.md
```

HRM-Text uses 4 training epochs by default. If you change `epochs` in the training config, change the sampling command to match.

### 2. Start the Environment

Set up the same environment on every pretraining node.

#### Recommended: Docker

We recommend running through the published Docker image that contains the full environment. Make sure Docker can see your GPUs, for example through NVIDIA Container Toolkit.

From the repo's directory:

```bash
docker run --gpus all --ipc=host --network=host -it \
  -v "$PWD":/workspace \
  sapientai/hrm-text:latest
```

For multi-node runs, mount the same shared workspace on every node. Keeping the code, tokenized data, and checkpoint directory at identical paths avoids version drift between ranks and makes FSDP2 checkpointing straightforward. A common layout is:

```text
/shared/
|-- HRM-Text/
   |--- checkpoints/
|-- data_io/
```

#### Alternative: Install from Source

If you are not using Docker, first install PyTorch, CUDA, and FlashAttention 3. The tested versions are documented in [`docker/Dockerfile`](docker/Dockerfile).

Then install the Python dependencies:

```bash
pip install -r requirements.txt
```

#### Check Distributed Communication

For multi-node runs, verify NCCL before starting a long job. At minimum, confirm that `torchrun` can initialize across the intended nodes. If your cluster provides `nccl-tests`, run both intra-node and inter-node bandwidth checks.

#### Set Up W&B Tracking

HRM-Text logs training metrics to [Weights & Biases](https://wandb.ai/). Log in before launching training:

```bash
wandb login
```

For headless runs, get an API key from <https://wandb.ai/authorize> and run:

```bash
wandb login <API_KEY>
```

### 3. Launch Pretraining

For the **L**-size reference run on one 8xH100 node:

```bash
OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
torchrun --nproc_per_node=8 pretrain.py arch/size@arch=L lr=2.5e-4 global_batch_size=172032
`