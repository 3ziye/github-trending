# Qwen3-ASR-Toolkit

[![PyPI version](https://badge.fury.io/py/qwen3-asr-toolkit.svg)](https://badge.fury.io/py/qwen3-asr-toolkit)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An advanced, high-performance Python command-line toolkit for using the **Qwen-ASR API** (formerly Qwen3-ASR-Flash). This implementation overcomes the API's 3-minute audio length limitation by intelligently splitting long audio/video files and processing them in parallel, enabling rapid transcription of hours-long content.

## 🚀 Key Features

-   **Break the 3-Minute Limit**: Seamlessly transcribe audio and video files of any length by bypassing the official API's duration constraint.
-   **Smart Audio Splitting**: Utilizes **Voice Activity Detection (VAD)** to split audio into meaningful chunks at natural silent pauses. This ensures that words and sentences are not awkwardly cut off.
-   **High-Speed Parallel Processing**: Leverages multi-threading to send audio chunks to the Qwen-ASR API concurrently, dramatically reducing the total transcription time for long files.
-   **Intelligent Post-Processing**: Automatically detects and removes common ASR **hallucinations and repetitive artifacts** for cleaner, more accurate transcripts.
-   **SRT Subtitle Generation**: Automatically create timestamped **`.srt` subtitle files** based on VAD segments, perfect for adding captions to video content.
-   **Automatic Audio Resampling**: Automatically converts audio from any sample rate and channel count to the 16kHz mono format required by the Qwen-ASR API. You can use any audio file without worrying about pre-processing.
-   **Universal Media Support**: Supports virtually any audio and video format (e.g., `.mp4`, `.mov`, `.mkv`, `.mp3`, `.wav`, `.m4a`) thanks to its reliance on FFmpeg.
-   **Simple & Easy to Use**: A straightforward command-line interface allows you to get started with just a single command.

## ⚙️ How It Works

This tool follows a robust pipeline to deliver fast and accurate transcriptions for long-form media:

1.  **Media Loading**: The script first loads your media file, whether it's a **local file or a remote URL**.
2.  **VAD-based Chunking**: It analyzes the audio stream using Voice Activity Detection (VAD) to identify silent segments.
3.  **Intelligent Splitting**: The audio is then split into smaller chunks based on the detected silences. Each chunk's duration is managed to stay under the 3-minute API limit, with a **user-configurable target length (defaulting to 120 seconds)**, preventing mid-sentence cuts.
4.  **Parallel API Calls**: A thread pool is initiated to upload and process these chunks concurrently using the DashScope Qwen-ASR API.
5.  **Result Aggregation & Cleaning**: The transcribed text segments from all chunks are collected, re-ordered, and then **post-processed to remove detected repetitions and hallucinations**.
6.  **Output Generation**: The final, cleaned transcription is printed to the console and saved to a `.txt` file. **Optionally, a timestamped `.srt` subtitle file can also be generated.**

## 🏁 Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

-   Python 3.8 or higher.
-   **FFmpeg**: The script requires FFmpeg to be installed on your system to handle media files.
    -   **Ubuntu/Debian**: `sudo apt update && sudo apt install ffmpeg`
    -   **macOS**: `brew install ffmpeg`
    -   **Windows**: Download from the [official FFmpeg website](https://ffmpeg.org/download.html) and add it to your system's PATH.
-   **DashScope API Key**: You need an API key from Alibaba Cloud's DashScope.
    -   You can obtain one from the [DashScope Console](https://dashscope.console.aliyun.com/apiKey). If you are calling the API services of Tongyi Qwen for the first time, you can follow the tutorial on [this website](https://help.aliyun.com/zh/model-studio/first-api-call-to-qwen) to create your own API Key.
    -   For better security and convenience, it is **highly recommended** to set your API key as an environment variable named `DASHSCOPE_API_KEY`. The script will automatically use it, and you won't need to pass the `--api-key` argument in the command.

        **On Linux/macOS:**
        ```bash
        export DASHSCOPE_API_KEY="your_api_key_here"
        ```
        *(To make this permanent, add the line to your `~/.bashrc`, `~/.zshrc`, or `~/.profile` file.)*

        **On Windows (Command Prompt):**
        ```cmd
        set DASHSCOPE_API_KEY="your_api_key_here"
        ```

        **On Windows (PowerShell):**
        ```powershell
        $env:DASHSCOPE_API_KEY="your_api_key_here"
        ```
        *(For a permanent setting on Windows, search for "Edit the system environment variables" in the Start Menu and add `DASHSCOPE_API_KEY` to your user variables.)*

### Installation

We recommen