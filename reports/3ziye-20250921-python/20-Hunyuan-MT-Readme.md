
<p align="left">
    <a href="README_CN.md">中文</a>&nbsp ｜ English</a>
</p>
<br><br>

<p align="center">
 <img src="https://dscache.tencent-cloud.cn/upload/uploader/hunyuan-64b418fd052c033b228e04bc77bbc4b54fd7f5bc.png" width="400"/> <br>
</p><p></p>


<p align="center">
    🤗&nbsp;<a href="https://huggingface.co/collections/tencent/hunyuan-mt-68b42f76d473f82798882597"><b>Hugging Face</b></a>&nbsp;&nbsp;|&nbsp;&nbsp;
    <img src="https://avatars.githubusercontent.com/u/109945100?s=200&v=4" width="16"/>&nbsp;<a href="https://modelscope.cn/collections/Hunyuan-MT-2ca6b8e1b4934f"><b>ModelScope</b></a>&nbsp;&nbsp;|&nbsp;&nbsp;
</p>

<p align="center">
    🖥️&nbsp;<a href="https://hunyuan.tencent.com" style="color: red;"><b>Official Website</b></a>&nbsp;&nbsp;|&nbsp;&nbsp;
    🕹️&nbsp;<a href="https://hunyuan.tencent.com/chat/HunyuanDefault?from=modelSquare&modelId=hunyuan-mt-7b"><b>Demo</b></a>&nbsp;&nbsp;&nbsp;&nbsp;
</p>

<p align="center">
    <a href="https://github.com/Tencent-Hunyuan/Hunyuan-MT"><b>GITHUB</b></a>&nbsp;&nbsp;|&nbsp;&nbsp;
    <a href="https://www.arxiv.org/pdf/2509.05209"><b>Technical Report</b> </a>
</p>


## Model Introduction

The Hunyuan-MT comprises a translation model, Hunyuan-MT-7B, and an ensemble model, Hunyuan-MT-Chimera. The translation model is used to translate source text into the target language, while the ensemble model integrates multiple translation outputs to produce a higher-quality result. It primarily supports mutual translation among 33 languages, including five ethnic minority languages in China.

## Key Features and Advantages

- In the WMT25 competition, the model achieved first place in 30 out of the 31 language categories it participated in.
- Hunyuan-MT-7B achieves industry-leading performance among models of comparable scale
- Hunyuan-MT-Chimera-7B is the industry’s first open-source translation ensemble model, elevating translation quality to a new level
- A comprehensive training framework for translation models has been proposed, spanning from pretrain → continue pretraining (CPT) → supervised fine-tuning (SFT) → translation rl → ensemble rl, achieving state-of-the-art (SOTA) results for models of similar size

## Related News
* 2025.9.1 We have open-sourced  **Hunyuan-MT-7B** , **Hunyuan-MT-Chimera-7B** on Hugging Face.
<br>


## Performance

<div align='center'>
<img src="imgs/overall_performance.png" width = "80%" />
</div>
You can refer to our technical report for more experimental results and analysis.

<a href="https://www.arxiv.org/pdf/2509.05209"><b>Technical Report</b> </a>

&nbsp;

## Model Links
| Model Name  | Description | Download |
| ----------- | ----------- |-----------
| Hunyuan-MT-7B  | Hunyuan 7B translation model |🤗 [Model](https://huggingface.co/tencent/Hunyuan-MT-7B)|
| Hunyuan-MT-7B-fp8 | Hunyuan 7B translation model，fp8 quant    | 🤗 [Model](https://huggingface.co/tencent/Hunyuan-MT-7B-fp8)|
| Hunyuan-MT-Chimera | Hunyuan 7B translation ensemble model    | 🤗 [Model](https://huggingface.co/tencent/Hunyuan-MT-Chimera-7B)|
| Hunyuan-MT-Chimera-fp8 | Hunyuan 7B translation ensemble model，fp8 quant     | 🤗 [Model](https://huggingface.co/tencent/Hunyuan-MT-Chimera-7B-fp8)|

## Prompts

### Prompt Template for ZH<=>XX Translation.
```
把下面的文本翻译成<target_language>，不要额外解释。

<source_text>
```


### Prompt Template for XX<=>XX Translation, excluding ZH<=>XX.
```
Translate the following segment into <target_language>, without additional explanation.

<source_text>
```

### Prompt Template for Hunyuan-MT-Chimera-7B

```
Analyze the following multiple <target_language> translations of the <source_language> segment surrounded in triple backticks and generate a single refined <target_language> translation. Only output the refined translation, do not explain.

The <source_language> segment:
```<source_text>```

The multiple `<target_language>` translations:
1. ```<translated_text1>```
2. ```<translated_text2>```
3. ```<translated_text3>```
4. ```<translated_text4>```
5. ```<translated_text5>```
6. ```<translated_text6>```
```

&nbsp;

### Use with transformers
First, please install transformers, recommends v4.56.0
```SHELL
pip install transformers==4.56.0
```

*!!! If you want to load fp8 model with transformers, you need to change the name"ignored_layers" in config.json to "ignore" and upgrade the compressed-tensors to compressed-tensors-0.11.0.*

The following code snippet shows how to use the transformers library to load and apply the model.

we use tencent/Hunyuan-MT-7B for example

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import os

model_name_or_path = "tencent/Hunyuan-MT-7B"

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
model = AutoModelForCausalLM.from_pretrained(model_name_or_path, device_map="auto")  # You may want to use bfloat16 and/or move to GPU here
messages = [
    {"role": "user", "content": "Translate the following segment into Chinese, without additional explanation.\n\nIt’s on the house.