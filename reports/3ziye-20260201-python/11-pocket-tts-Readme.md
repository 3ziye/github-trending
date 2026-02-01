# Pocket TTS

<img width="1446" height="622" alt="pocket-tts-logo-v2-transparent" src="https://github.com/user-attachments/assets/637b5ed6-831f-4023-9b4c-741be21ab238" />

A lightweight text-to-speech (TTS) application designed to run efficiently on CPUs.
Forget about the hassle of using GPUs and web APIs serving TTS models. With Kyutai's Pocket TTS, generating audio is just a pip install and a function call away.

Supports Python 3.10, 3.11, 3.12, 3.13 and 3.14. Requires PyTorch 2.5+. Does not require the gpu version of PyTorch.

[🔊 Demo](https://kyutai.org/pocket-tts) | 
[🐱‍💻GitHub Repository](https://github.com/kyutai-labs/pocket-tts) | 
[🤗 Hugging Face Model Card](https://huggingface.co/kyutai/pocket-tts) | 
[⚙️ Tech report](https://kyutai.org/blog/2026-01-13-pocket-tts) |
[📄 Paper](https://arxiv.org/abs/2509.06926) | 
[📚 Documentation](https://github.com/kyutai-labs/pocket-tts/tree/main/docs)


## Main takeaways
* Runs on CPU
* Small model size, 100M parameters
* Audio streaming
* Low latency, ~200ms to get the first audio chunk
* Faster than real-time, ~6x real-time on a CPU of MacBook Air M4
* Uses only 2 CPU cores
* Python API and CLI
* Voice cloning
* English only at the moment
* Can handle infinitely long text inputs
* [Can run on client-side in the browser](#in-browser-implementations)

## Trying it from the website, without installing anything

Navigate to the [Kyutai website](https://kyutai.org/pocket-tts) to try it out directly in your browser. You can input text, select different voices, and generate speech without any installation.

## Trying it with the CLI

### The `generate` command
You can use pocket-tts directly from the command line. We recommend using
`uv` as it installs any dependencies on the fly in an isolated environment (uv installation instructions [here](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)).
You can also use `pip install pocket-tts` to install it manually.

This will generate a wav file `./tts_output.wav` saying the default text with the default voice, and display some speed statistics.
```bash
uvx pocket-tts generate
# or if you installed it manually with pip:
pocket-tts generate
```
Modify the voice with `--voice` and the text with `--text`. We provide a small catalog of voices.

You can take a look at [this page](https://huggingface.co/kyutai/tts-voices) which details the licenses
for each voice.

* [alba](https://huggingface.co/kyutai/tts-voices/blob/main/alba-mackenna/casual.wav)
* [marius](https://huggingface.co/kyutai/tts-voices/blob/main/voice-donations/Selfie.wav)
* [javert](https://huggingface.co/kyutai/tts-voices/blob/main/voice-donations/Butter.wav)
* [jean](https://huggingface.co/kyutai/tts-voices/blob/main/ears/p010/freeform_speech_01.wav)
* [fantine](https://huggingface.co/kyutai/tts-voices/blob/main/vctk/p244_023.wav)
* [cosette](https://huggingface.co/kyutai/tts-voices/blob/main/expresso/ex04-ex02_confused_001_channel1_499s.wav)
* [eponine](https://huggingface.co/kyutai/tts-voices/blob/main/vctk/p262_023.wav)
* [azelma](https://huggingface.co/kyutai/tts-voices/blob/main/vctk/p303_023.wav)

The `--voice` argument can also take a plain wav file as input for voice cloning.
You can use your own or check out our [voice repository](https://huggingface.co/kyutai/tts-voices).
We recommend [cleaning the sample](https://podcast.adobe.com/en/enhance) before using it with Pocket TTS, because the audio quality of the sample is also reproduced.

Feel free to check out the [generate documentation](https://github.com/kyutai-labs/pocket-tts/tree/main/docs/generate.md) for more details and examples.
For trying multiple voices and prompts quickly, prefer using the `serve` command.

### The `serve` command

You can also run a local server to generate audio via HTTP requests.
```bash
uvx pocket-tts serve
# or if you installed it manually with pip:
pocket-tts serve
```
Navigate to `http://localhost:8000` to try the web interface, it's faster than the command line as the model is kept in memory between requests.

You can check out the [serve documentation](https://github.com/kyutai-labs/pocket-tts/tree/main/docs/serve.md) for more details and examples.

### The `export-voice` command

Processing an audio file (e.g., a .wav or .mp3) for voice cloning is relatively slow, but loading a safetensors file -- a voice embedding converted from an audio file -- is very fast. You can use the `export-voice` command to do this conversion. See the [export-voice documentation](https://github.com/kyutai-labs/pocket-tts/tree/main/docs/export_voice.md) for more details and examples.


## Using it as a Python library

You can try out the Python library on Colab [here](https://colab.research.google.com/github/kyutai-labs/pocket-tts/blob/main/docs/pocket-tts-example.ipynb).

Install the package with
```bash
pip install pocket-tts
# or
uv add pocket-tts
```

You can use this package as a simple Python library to generate audio from text.
```python
from pocket_tts 