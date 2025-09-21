<div align="center">

# AI Video Transcriber

English | [中文](README_ZH.md)

An AI-powered video transcription and summarization tool that supports multiple video platforms including YouTube, Tiktok, Bilibili, and 30+ platforms.

![Interface](en-video.png)

</div>

## ✨ Features

- 🎥 **Multi-Platform Support**: Works with YouTube, Tiktok, Bilibili, and 30+ more
- 🗣️ **Intelligent Transcription**: High-accuracy speech-to-text using Faster-Whisper
- 🤖 **AI Text Optimization**: Automatic typo correction, sentence completion, and intelligent paragraphing
- 🌍 **Multi-Language Summaries**: Generate intelligent summaries in multiple languages
- ⚡ **Real-Time Progress**: Live progress tracking and status updates
- ⚙️ **Conditional Translation**: When the selected summary language differs from the detected transcript language, the system auto-translates with GPT‑4o
- 📱 **Mobile-Friendly**: Perfect support for mobile devices

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- FFmpeg
- Optional: OpenAI API key (for AI summary features)

### Installation

#### Method 1: Automatic Installation

```bash
# Clone the repository
git clone https://github.com/wendy7756/AI-Video-Transcriber.git
cd AI-Video-Transcriber

# Run installation script
chmod +x install.sh
./install.sh
```

#### Method 2: Docker

```bash
# Clone the repository
git clone https://github.com/wendy7756/AI-Video-Transcriber.git
cd AI-Video-Transcriber

# Using Docker Compose (easiest)
cp .env.example .env
# Edit .env file and set your OPENAI_API_KEY
docker-compose up -d

# Or using Docker directly
docker build -t ai-video-transcriber .
docker run -p 8000:8000 -e OPENAI_API_KEY="your_api_key_here" ai-video-transcriber
```

#### Method 3: Manual Installation

1. **Install Python Dependencies**
```bash
# macOS (PEP 668) strongly recommends using a virtualenv
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

2. **Install FFmpeg**
```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# CentOS/RHEL
sudo yum install ffmpeg
```

3. **Configure Environment Variables**
```bash
# Required for AI summary/translation features
export OPENAI_API_KEY="your_api_key_here"

# Optional: only if you use a custom OpenAI-compatible gateway

### Start the Service

```bash
python3 start.py
```

After the service starts, open your browser and visit `http://localhost:8000`

#### Production Mode (Recommended for long videos)

To avoid SSE disconnections during long processing, start in production mode (hot-reload disabled):

```bash
python3 start.py --prod
```

This keeps the SSE connection stable throughout long tasks (30–60+ min).

#### Run with explicit env (example)

```bash
source .venv/bin/activate
export OPENAI_API_KEY=your_api_key_here
# export OPENAI_BASE_URL=https://oneapi.basevec.com/v1   # if using a custom endpoint
python3 start.py --prod
```

## 📖 Usage Guide

1. **Enter Video URL**: Paste a video link from YouTube, Bilibili, or other supported platforms
2. **Select Summary Language**: Choose the language for the generated summary
3. **Start Processing**: Click the "Start" button
4. **Monitor Progress**: Watch real-time progress through multiple stages:
   - Video download and parsing
   - Audio transcription with Faster-Whisper
   - AI-powered transcript optimization (typo correction, sentence completion, intelligent paragraphing)
   - AI summary generation in selected language
5. **View Results**: Review the optimized transcript and intelligent summary
   - If transcript language ≠ selected summary language, a third tab “Translation” is shown containing a translated transcript
6. **Download Files**: Click download buttons to save Markdown-formatted files (Transcript / Translation / Summary)

## 🛠️ Technical Architecture

### Backend Stack
- **FastAPI**: Modern Python web framework
- **yt-dlp**: Video downloading and processing
- **Faster-Whisper**: Efficient speech transcription
- **OpenAI API**: Intelligent text summarization

### Frontend Stack
- **HTML5 + CSS3**: Responsive interface design
- **JavaScript (ES6+)**: Modern frontend interactions
- **Marked.js**: Markdown rendering
- **Font Awesome**: Icon library

### Project Structure
```
AI-Video-Transcriber/
├── backend/                 # Backend code
│   ├── main.py             # FastAPI main application
│   ├── video_processor.py  # Video processing module
│   ├── transcriber.py      # Transcription module
│   ├── summarizer.py       # Summary module
│   └── translator.py       # Translation module
├── static/                 # Frontend files
│   ├── index.html          # Main page
│   └── app.js              # Frontend logic
├── temp/                   # Temporary files directory
├── Dockerfile              # Docker image configuration
├── docker-compose.yml      # Docker Compose configuration
├── .dockerignore           # Docker ignore rules
├── .env.example            # Environment variables templ