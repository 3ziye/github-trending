# NeuTTS Air ☁️

HuggingFace 🤗: [Model](https://huggingface.co/neuphonic/neutts-air), [Q8 GGUF](https://huggingface.co/neuphonic/neutts-air-q8-gguf), [Q4 GGUF](https://huggingface.co/neuphonic/neutts-air-q4-gguf) [Spaces](https://huggingface.co/spaces/neuphonic/neutts-air)

[Demo Video](https://github.com/user-attachments/assets/020547bc-9e3e-440f-b016-ae61ca645184)

*Created by [Neuphonic](http://neuphonic.com/) - building faster, smaller, on-device voice AI*

State-of-the-art Voice AI has been locked behind web APIs for too long. NeuTTS Air is the world’s first super-realistic, on-device, TTS speech language model with instant voice cloning. Built off a 0.5B LLM backbone, NeuTTS Air brings natural-sounding speech, real-time performance, built-in security and speaker cloning to your local device - unlocking a new category of embedded voice agents, assistants, toys, and compliance-safe apps.

## Key Features

- 🗣Best-in-class realism for its size - produces natural, ultra-realistic voices that sound human
- 📱Optimised for on-device deployment - provided in GGML format, ready to run on phones, laptops, or even Raspberry Pis
- 👫Instant voice cloning - create your own speaker with as little as 3 seconds of audio
- 🚄Simple LM + codec architecture built off a 0.5B backbone - the sweet spot between speed, size, and quality for real-world applications

> [!CAUTION]
> Websites like neutts.com are popping up and they're not affliated with Neuphonic, our github or this repo.
>
> We are on neuphonic.com only. Please be careful out there! 🙏

## Model Details

NeuTTS Air is built off Qwen 0.5B - a lightweight yet capable language model optimised for text understanding and generation - as well as a powerful combination of technologies designed for efficiency and quality:
- **Supported Languages**: English
- **Audio Codec**: [NeuCodec](https://huggingface.co/neuphonic/neucodec) - our 50hz neural audio codec that achieves exceptional audio quality at low bitrates using a single codebook
- **Context Window**: 2048 tokens, enough for processing ~30 seconds of audio (including prompt duration)
- **Format**: Available in GGML format for efficient on-device inference
- **Responsibility**: Watermarked outputs
- **Inference Speed**: Real-time generation on mid-range devices
- **Power Consumption**: Optimised for mobile and embedded devices

## Get Started

1. **Clone Git Repo**
   ```bash
   git clone https://github.com/neuphonic/neutts-air.git
   ```
   ```bash
   cd neutts-air
   ```

2. **Install `espeak` (required dependency)**

   Please refer to the following link for instructions on how to install `espeak`:

   https://github.com/espeak-ng/espeak-ng/blob/master/docs/guide.md

   ```bash
   # Mac OS
   brew install espeak

   # Ubuntu/Debian
   sudo apt install espeak
   ```

   Mac users may need to put the following lines at the top of the neutts.py file.
   ```python
   from phonemizer.backend.espeak.wrapper import EspeakWrapper
   _ESPEAK_LIBRARY = '/opt/homebrew/Cellar/espeak/1.48.04_1/lib/libespeak.1.1.48.dylib'  #use the Path to the library.
   EspeakWrapper.set_library(_ESPEAK_LIBRARY)
   ```

   Windows users may need to run (see https://github.com/bootphon/phonemizer/issues/163)
   ```pwsh
   $env:PHONEMIZER_ESPEAK_LIBRARY = "c:\Program Files\eSpeak NG\libespeak-ng.dll"
   $env:PHONEMIZER_ESPEAK_PATH = "c:\Program Files\eSpeak NG"
   setx PHONEMIZER_ESPEAK_LIBRARY "c:\Program Files\eSpeak NG\libespeak-ng.dll"
   setx PHONEMIZER_ESPEAK_PATH "c:\Program Files\eSpeak NG"
   ```

3. **Install Python dependencies**

   The requirements file includes the dependencies needed to run the model with PyTorch.
   When using an ONNX decoder or a GGML model, some dependencies (such as PyTorch) are no longer required.

   The inference is compatible and tested on `python>=3.11`.

    ```
    pip install -r requirements.txt
    ```

4. **(Optional) Install Llama-cpp-python to use the `GGUF` models.**
   ```
   pip install llama-cpp-python
   ```
   To run llama-cpp with GPU suport (CUDA, MPS) support please refer to:
   https://pypi.org/project/llama-cpp-python/

5. **(Optional) Install onnxruntime to use the `.onnx` decoder.**
   If you want to run the onnxdecoder
   ```
   pip install onnxruntime
   ```

## Running the Model

Run the basic example script to synthesize speech:
```bash
python -m examples.basic_example \
  --input_text "My name is Dave, and um, I'm from London" \
  --ref_audio samples/dave.wav \
  --ref_text samples/dave.txt
```

To specify a particular model repo for the backbone or codec, add the `--backbone` argument. Available backbones are listed in [NeuTTS-Air huggingface collection](https://huggingface.co/collections/neuphonic/neutts-air-68cc14b7033b4c56197ef350).

Several examples are available, including a Jupyter notebook in the `examples` folder.

### One-Code Block Usage

```python
from neuttsair.neutts import NeuTTSAir
import soundfile as sf

tts = NeuTTSAir(
   backbone_repo="neuphonic/neutts-air", #