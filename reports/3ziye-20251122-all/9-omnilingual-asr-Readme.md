<div align="center">
  <img src="./omniASR_header.jpg" alt="Header image with a collage of on-the-ground photos from the transcription gathering efforts in Pakistan and Liberia." width="100%" />
  <p><i>Photographs captured during corpus creation efforts in Pakistan and Liberia.</i></p>
</div>

# Omnilingual ASR: Open-Source Multilingual Speech Recognition for 1600+ Languages

Omnilingual ASR is an open-source speech recognition system supporting over 1,600 languages — including hundreds never previously covered by any ASR technology. Designed for broad accessibility, it enables new languages to be added with just a few paired examples without requiring specialized expertise or large datasets. By combining scalable zero-shot learning with a flexible model family, Omnilingual ASR aims to make speech technology more inclusive and adaptable for communities and researchers worldwide.

* [Huggingface Demo](https://huggingface.co/spaces/facebook/omniasr-transcriptions)
* [Huggingface Dataset](https://huggingface.co/datasets/facebook/omnilingual-asr-corpus)
* [Paper](https://ai.meta.com/research/publications/omnilingual-asr-open-source-multilingual-speech-recognition-for-1600-languages/)
* [Blogpost](http://ai.meta.com/blog/omnilingual-asr-advancing-automatic-speech-recognition)

<div align="center">
  <img src="./result_table.png" alt="Performance results table" width="100%" />
  <p><i>Our 7B-LLM-ASR system achieves state-of-the-art performance across 1,600+ languages, with character error rates (CER) below 10 for 78% of those languages.</i></p>
</div>


## Documentation

### Quick Start
- **[Installation & Basic Usage](#installation)** - Setup and first transcription
- **[Inference Pipeline](src/omnilingual_asr/models/inference/README.md)** - Comprehensive transcription guide with batch processing, language conditioning, and context examples
- **[Supported Languages](#supported-languages)** - View the complete list of 1600+ supported languages


### Models & Architecture
- **[Model Specifications](#model-architectures)** - Available models, parameters, and memory requirements
- **[Architecture Overview](src/omnilingual_asr/models/README.md)** - Technical details on W2V, CTC, and LLM model families
- **[Asset Management](src/omnilingual_asr/cards/README.md)** - Configuration system for models, tokenizers, and datasets

### Training & Data Pipeline
- **[Data Preparation](workflows/dataprep/README.md)** - End-to-end guide for multilingual dataset preparation, HuggingFace integration, and parquet processing
- **[Training Recipes](workflows/recipes/wav2vec2/asr/README.md)** - Pre-configured workflows for CTC and LLM model training

---

## Installation

The models were developed using [fairseq2](https://github.com/facebookresearch/fairseq2), a research-focused sequence modeling toolkit. While we provide a **reference** inference pipeline that works across platforms, audio support requires [libsndfile](https://github.com/facebookresearch/fairseq2?tab=readme-ov-file#system-dependencies) (Mac: `brew install libsndfile`; Windows may need an additional [setup](https://github.com/facebookresearch/fairseq2?tab=readme-ov-file#installing-on-windows)).

```bash
# using pip
pip install omnilingual-asr

# using uv
uv add omnilingual-asr
```

## Inference

```python
from omnilingual_asr.models.inference.pipeline import ASRInferencePipeline

pipeline = ASRInferencePipeline(model_card="omniASR_LLM_7B")

audio_files = ["/path/to/eng_audio1.flac", "/path/to/deu_audio2.wav"]
lang = ["eng_Latn", "deu_Latn"]
transcriptions = pipeline.transcribe(audio_files, lang=lang, batch_size=2)
```

More details on running specific models can be found in the [src/omnilingual_asr/models/inference](/src/omnilingual_asr/models/inference/README.md) directory.

> **⚠️ Important:** Currently only audio files shorter than 40 seconds are accepted for inference. We plan to add support for transcribing unlimited-length audio files shortly.

### Supported Languages

To view the full list of 1600+ supported languages, you can access the language list [programmatically](/src/omnilingual_asr/models/wav2vec2_llama/lang_ids.py):

```python
from omnilingual_asr.models.wav2vec2_llama.lang_ids import supported_langs

# Print all supported languages
print(f"Total supported languages: {len(supported_langs)}")
print(supported_langs)

# Check if a specific language is supported
if "eng_Latn" in supported_langs:
    print("English (Latin script) is supported!")
```

Languages follow the format `{language_code}_{script}`, for example `eng_Latn` - English (Latin script), `cmn_Hans` - Mandarin Chinese (Simplified), ...

### Using the HuggingFace Dataset 🤗

We provide a large-scale multilingual speech dataset on HuggingFace under CC-BY-4.0 License: [`facebook/omnilingual-asr-corpus`](https://huggingface.co/datasets/facebook/omnilingual-asr-corpus).
This dataset can be directly used with our inference pipeline for evaluation or testing:

```bash
pip install "omnilingual-asr[dat