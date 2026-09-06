<h1 align="center">WeMM-Embedding: WeChat Multi-Modal Embedding</h1>

<p align="center">
  <b>English</b> | <a href="./README_zh.md">中文</a>
</p>

<p align="center">
  <a href="https://huggingface.co/collections/tencent/wemm-embedding">
    <img src="https://img.shields.io/badge/🤗-Hugging%20Face-yellow" alt="Hugging Face">
  </a>
  <a href="https://arxiv.org/abs/2608.24053">
    <img src="https://img.shields.io/badge/📄-Technical%20Report-red" alt="Technical Report">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License">
  </a>
</p>

WeMM-Embedding is a family of universal multimodal embedding models developed by the WeChat Vision team. It provides unified representations for text, images, videos, visual documents, and interleaved multimodal inputs, achieving state-of-the-art performance across multiple benchmarks covering diverse tasks and domains.

<p align="center">
  <a href="assets/performance-overview.pdf">
    <img src="assets/performance-overview.png" width="100%" alt="WeMM-Embedding Performance Overview">
  </a>
</p>

## Model Zoo

| Model | Matryoshka dimensions | Hugging Face |
| --- | --- | --- |
| WeMM-Embedding-2B | `64, 128, 256, 512, 1024, 2048` | [🤗 Link](https://huggingface.co/tencent/WeMM-Embedding-2B) |
| WeMM-Embedding-4B | `64, 128, 256, 512, 1024, 2560` | [🤗 Link](https://huggingface.co/tencent/WeMM-Embedding-4B) |
| WeMM-Embedding-9B | `64, 128, 256, 512, 1024, 2048, 4096` | [🤗 Link](https://huggingface.co/tencent/WeMM-Embedding-9B) |

All models support text, images, videos, visual documents, and interleaved multimodal inputs. Embeddings are obtained from the last-layer hidden state at the dedicated `<embedding>` token position, followed by L2 normalization. Audio input is not currently supported.


## Installation

```bash
pip install -r requirements.txt
```

## Transformers
We recommend using `transformers==5.2.0` for inference and reproducibility, as newer versions may differ in preprocessing behavior.

```bash
python examples/transformers_inference.py \
  --model /path/to/WeMM-Embedding-2B \
  --image /path/to/image.jpg \
  --video /path/to/video.mp4 \
  --dimension 2048
```

The example produces independent text, image, and video embeddings. Omit `--dimension` for the full embedding dimension.

## Sentence Transformers

```bash
python examples/sentence_transformers_inference.py \
  --model /path/to/WeMM-Embedding-2B \
  --image /path/to/image.jpg \
  --video /path/to/video.mp4 \
  --dimension 2048
```

`SentenceTransformer` loads the model directly, so a Hugging Face model id such as `tencent/WeMM-Embedding-2B` also works in place of a local path. Text, image, and video inputs go through `SentenceTransformer.encode()`, and MRL is selected with `--dimension`.

## Serving

Tested versions: vLLM `0.27.0` and SGLang `0.5.9`.

vLLM:

```bash
MODEL_PATH=/path/to/WeMM-Embedding-2B
vllm serve "$MODEL_PATH" \
  --runner pooling \
  --chat-template "$MODEL_PATH/embedding_chat_template.jinja"
```

SGLang:

```bash
MODEL_PATH=/path/to/WeMM-Embedding-2B
python scripts/patch_sglang_video.py
python -m sglang.launch_server \
  --model-path "$MODEL_PATH" \
  --is-embedding \
  --enable-precise-embedding-interpolation
```

Equivalent one-command wrappers are available in `scripts/serve_vllm.sh` and `scripts/serve_sglang.sh`.

## Matryoshka Embeddings

For a supported dimension `d`, truncate the full embedding and normalize it again:

```python
embedding = torch.nn.functional.normalize(embedding[..., :d], dim=-1)
```

On MMEB-v2, the 2B model at 256 dimensions retains 98.7% of its full-dimensional image and video performance.

## Evaluation

### MMEB-v2

Results on 78 datasets from Table 1 of the [technical report](assets/WeMM_Embedding_tech_report.pdf). Image and video tasks use Hit@1, while visual-document tasks use NDCG@5. Higher is better.

| Model | Size | AVG | Image | Video | VisDoc |
| --- | ---: | ---: | ---: | ---: | ---: |
| VLM2Vec | 2B | 47.8 | 59.7 | 29.0 | 44.0 |
| GME | 2B | 55.4 | 51.9 | 33.9 | 76.8 |
| VLM2Vec-V2 | 2B | 59.3 | 64.9 | 34.9 | 69.2 |
| Qwen3-VL-Embedding | 2B | 73.2 | 75.0 | 61.9 | 79.2 |
| DME-Small† | 2B | 74.8 | 75.9 | 65.6 | 79.9 |
| **WeMM-Embedding** | **2B** | **77.9** | **79.6** | **70.8** | **80.7** |
| **WeMM-Embedding** | **4B** | **79.2** | **80.8** | **72.1** | **82.0** |
| VLM2Vec | 8B | 53.2 | 65.5 | 34.0 | 49.1 |
| GME | 8B | 59.2 | 56.0 | 38.6 | 79.3 |
| Qwen3-VL-Embedding | 8B | 77.8 | 80.1 | 67.1 | 82.4 |
| DME-Medium† | 9B | 78.4 | 79.8 | 70.8 | 82.0 |
| **WeMM-Embedding** | **9B** | **80.6** | **81.9** | **74.3** | **83.3** |

† Closed-source leaderboard submission without publicly released model weights or a public inference endpoint.

### MMEB-v3

Results on all 190 tasks from Table 2 of the [technical report](assets/WeMM_Embedding_tech_report.pdf). V3-All includes the 78 MMEB-v2 tasks, 53 text tasks, 47 agent tasks, 11 audio tasks, and MCMR. Unsupported tasks are assigned a score of