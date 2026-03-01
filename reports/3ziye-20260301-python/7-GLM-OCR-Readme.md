## GLM-OCR

<div align="center">
<img src=resources/logo.svg width="40%"/>
</div>
<p align="center">
    👋 Join our <a href="resources/WECHAT.md" target="_blank">WeChat</a> and <a href="https://discord.gg/QR7SARHRxK" target="_blank">Discord</a> community
    <br>
    📍 Use GLM-OCR's <a href="https://docs.z.ai/guides/vlm/glm-ocr" target="_blank">API</a>
</p>

<div align="center">
  <a href="README_zh.md">简体中文</a> | English
</div>

### Model Introduction

GLM-OCR is a multimodal OCR model for complex document understanding, built on the GLM-V encoder–decoder architecture. It introduces Multi-Token Prediction (MTP) loss and stable full-task reinforcement learning to improve training efficiency, recognition accuracy, and generalization. The model integrates the CogViT visual encoder pre-trained on large-scale image–text data, a lightweight cross-modal connector with efficient token downsampling, and a GLM-0.5B language decoder. Combined with a two-stage pipeline of layout analysis and parallel recognition based on PP-DocLayout-V3, GLM-OCR delivers robust and high-quality OCR performance across diverse document layouts.

**Key Features**

- **State-of-the-Art Performance**: Achieves a score of 94.62 on OmniDocBench V1.5, ranking #1 overall, and delivers state-of-the-art results across major document understanding benchmarks, including formula recognition, table recognition, and information extraction.

- **Optimized for Real-World Scenarios**: Designed and optimized for practical business use cases, maintaining robust performance on complex tables, code-heavy documents, seals, and other challenging real-world layouts.

- **Efficient Inference**: With only 0.9B parameters, GLM-OCR supports deployment via vLLM, SGLang, and Ollama, significantly reducing inference latency and compute cost, making it ideal for high-concurrency services and edge deployments.

- **Easy to Use**: Fully open-sourced and equipped with a comprehensive [SDK](https://github.com/zai-org/GLM-OCR) and inference toolchain, offering simple installation, one-line invocation, and smooth integration into existing production pipelines.

### News & Updates

- **[Coming Soon]** GLM-OCR Technical Report
- **[2026.2.12]** Fine-tuning tutorial based on LLaMA-Factory is now available. See: [GLM-OCR Fine-tuning Guide](examples/finetune/README.md)

### Download Model

| Model   | Download Links                                                                                                              | Precision |
| ------- | --------------------------------------------------------------------------------------------------------------------------- | --------- |
| GLM-OCR | [🤗 Hugging Face](https://huggingface.co/zai-org/GLM-OCR)<br> [🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/GLM-OCR) | BF16      |

## GLM-OCR SDK

We provide an SDK for using GLM-OCR more efficiently and conveniently.

### Install SDK

> [UV Installation](https://docs.astral.sh/uv/getting-started/installation/)

```bash
# Install from source
git clone https://github.com/zai-org/glm-ocr.git
cd glm-ocr
uv venv --python 3.12 --seed && source .venv/bin/activate
uv pip install -e .
```

### Model Deployment

Two ways to use GLM-OCR:

#### Option 1: Zhipu MaaS API (Recommended for Quick Start)

Use the hosted cloud API – no GPU needed. The cloud service runs the complete GLM-OCR pipeline internally, so the SDK simply forwards your request and returns the result.

1. Get an API key from https://open.bigmodel.cn
2. Configure `config.yaml`:

```yaml
pipeline:
  maas:
    enabled: true # Enable MaaS mode
    api_key: your-api-key # Required
```

That's it! When `maas.enabled=true`, the SDK acts as a thin wrapper that:

- Forwards your documents to the Zhipu cloud API
- Returns the results directly (Markdown + JSON layout details)
- No local processing, no GPU required

Input note (MaaS): the upstream API accepts `file` as a URL or a `data:<mime>;base64,...` data URI.
If you have raw base64 without the `data:` prefix, wrap it as a data URI (recommended). The SDK will
auto-wrap local file paths / bytes / raw base64 into a data URI when calling MaaS.

API documentation: https://docs.bigmodel.cn/cn/guide/models/vlm/glm-ocr

#### Option 2: Self-host with vLLM / SGLang

Deploy the GLM-OCR model locally for full control. The SDK provides the complete pipeline: layout detection, parallel region OCR, and result formatting.

##### Using vLLM

Install vLLM:

```bash
uv pip install -U vllm --torch-backend=auto --extra-index-url https://wheels.vllm.ai/nightly
# Or use Docker
docker pull vllm/vllm-openai:nightly
```

Launch the service:

```bash
# In docker container, uv may not be need for transformers install
uv pip install git+https://github.com/huggingface/transformers.git

# Run with MTP for better performance
vllm serve zai-org/GLM-OCR --allowed-local-media-path / --port 8080 --speculative-config '{"method": "mtp", "num_speculative_tokens": 1}' --served-model-name glm-ocr
```

##### Using SGLang

In