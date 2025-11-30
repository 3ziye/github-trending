<div align="center">

[中文阅读](./README_zh.md)

</div>

<div align="center">

# HunyuanOCR

</div>

<p align="center">
 <img src="./assets/hyocr-head-img.png" width="80%"/> <br>
</p>


<p align="center">
<a href="https://huggingface.co/spaces/tencent/HunyuanOCR"><b>🎯 Demo</b></a> |
<a href="https://huggingface.co/tencent/HunyuanOCR"><b>📥 Model Download</b></a> |
<a href="https://arxiv.org/abs/2511.19575"><b>📄 Technical Report</b></a>
</p>

## 🤝 Join Our Community

<div align="center">

| Wechat Discussion Group | Discord Group |
| :---: | :---: |
| <img src="./assets/qrcode_for_hunyuanocr_wechat.jpg" width="150"> | [Join HunyuanOCR Discord](https://discord.gg/XeD3p2MRDk) |

</div>

## 🔥 News
- **[2025/11/28]** 🛠️ We fixed vLLM inference bugs and hyperparameter configuration issues such as system prompt. It is recommended to use the latest vLLM installation steps and the [inference script](https://github.com/Tencent-Hunyuan/HunyuanOCR/blob/main/Hunyuan-OCR-master/Hunyuan-OCR-vllm/run_hy_ocr.py) for performance testing. Currently, there is still a certain accuracy difference between Transformers and the vLLM framework (we are working on fixing this).
- **[2025/11/25]** 📝 Inference code and model weights publicly available.


## 📖 Introduction
**HunyuanOCR** stands as a leading end-to-end OCR expert VLM powered by Hunyuan's native multimodal architecture. With a remarkably lightweight 1B parameter design, it has achieved multiple state-of-the-art benchmarks across the industry. The model demonstrates mastery in **complex multilingual document parsing** while excelling in practical applications including **text spotting, open-field information extraction, video subtitle extraction, and photo translation**.


## ✨ Key Features

- 💪 **Efficient Lightweight Architecture**: Built on Hunyuan's native multimodal architecture and training strategy, achieving SOTA performance with only 1B parameters, significantly reducing deployment costs.

- 📑 **Comprehensive OCR Capabilities**: A single model covering classic OCR tasks including text detection and recognition, complex document parsing, open-field information extraction and video subtitle extraction, while supporting end-to-end photo translation and document QA.

- 🚀 **Ultimate Usability**: Deeply embraces the "end-to-end" philosophy of large models - achieving SOTA results with single instruction and single inference, offering greater efficiency and convenience compared to industry cascade solutions.

- 🌏 **Extensive Language Support**: Robust support for over 100 languages, excelling in both single-language and mixed-language scenarios across various document types.

<div align="left">
  <img src="./assets/hyocr-pipeline-v1.png" alt="HunyuanOCR framework" width="80%">
</div>




## 🛠️ Dependencies and Installation

### System Requirements
- 🖥️ Operating System: Linux
- 🐍 Python: 3.12+ (recommended and tested)
- ⚡ CUDA: 12.9
- 🔥 PyTorch: 2.7.1
- 🎮 GPU: NVIDIA GPU with CUDA support
- 🧠 GPU Memory: 20GB (for vLLM)
- 💾 Disk Space: 6GB

## 🚀 Quick Start with vLLM (⭐ Recommended)

- **[HunyuanOCR Usage Guide](https://docs.vllm.ai/projects/recipes/en/latest/Tencent-Hunyuan/HunyuanOCR.html)**

### Installation
```bash
uv venv hunyuanocr
source hunyuanocr/bin/activate

uv pip install -U vllm --pre --extra-index-url https://wheels.vllm.ai/nightly
uv pip install -r requirements.txt
```

Note: We suggest to install [cuda-compat-12-9](https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/):
```bash
sudo dpkg -i cuda-compat-12-9_575.57.08-0ubuntu1_amd64.deb
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-12.9/compat:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
# verify cuda-compat-12-9
ls /usr/local/cuda-12.9/compat
```

### Model Deploy
```bash
vllm serve tencent/HunyuanOCR \
    --no-enable-prefix-caching \
    --mm-processor-cache-gb 0 \
    --gpu-memory-utilization 0.2
```

### Model Inference
```python
from vllm import LLM, SamplingParams
from PIL import Image
from transformers import AutoProcessor

def clean_repeated_substrings(text):
    """Clean repeated substrings in text"""
    n = len(text)
    if n<8000:
        return text
    for length in range(2, n // 10 + 1):
        candidate = text[-length:] 
        count = 0
        i = n - length
        
        while i >= 0 and text[i:i + length] == candidate:
            count += 1
            i -= length

        if count >= 10:
            return text[:n - length * (count - 1)]  

    return text

model_path = "tencent/HunyuanOCR"
llm = LLM(model=model_path, trust_remote_code=True)
processor = AutoProcessor.from_pretrained(model_path)
sampling_params = SamplingParams(temperature=0, max_tokens=16384)

img_path = "/path/to/image.jpg"
img = Image.open(img_path)
messages = [
    {"role": "system", "content": ""},
    {"role": "user", "content": [
        {"type": "image", "image": img_path},
        {"type": "text", "text": "检测并识别图片中的文字，将文本坐标格式化输出。"}
    ]}
]
prompt = processor.apply_chat_template(messag