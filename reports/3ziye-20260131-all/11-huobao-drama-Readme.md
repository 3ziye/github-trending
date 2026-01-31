# 🎬 Huobao Drama - AI Short Drama Production Platform

<div align="center">

**Full-stack AI Short Drama Automation Platform Based on Go + Vue3**

[![Go Version](https://img.shields.io/badge/Go-1.23+-00ADD8?style=flat&logo=go)](https://golang.org)
[![Vue Version](https://img.shields.io/badge/Vue-3.x-4FC08D?style=flat&logo=vue.js)](https://vuejs.org)
[![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

[Features](#features) • [Quick Start](#quick-start) • [Deployment](#deployment)

[简体中文](README-CN.md) | [English](README.md) | [日本語](README-JA.md)

</div>

---

## 📖 About

Huobao Drama is an AI-powered short drama production platform that automates the entire workflow from script generation, character design, storyboarding to video composition.

### 🎯 Core Features

- **🤖 AI-Driven**: Parse scripts using large language models to extract characters, scenes, and storyboards
- **🎨 Intelligent Creation**: AI-generated character portraits and scene backgrounds
- **📹 Video Generation**: Automatic storyboard video generation using text-to-video and image-to-video models
- **🔄 Complete Workflow**: End-to-end production workflow from idea to final video。

### 🛠️ Technical Architecture

Based on **DDD (Domain-Driven Design)** with clear layering:

```
├── API Layer (Gin HTTP)
├── Application Service Layer (Business Logic)
├── Domain Layer (Domain Models)
└── Infrastructure Layer (Database, External Services)
```

### 🎥 Demo Videos

Experience AI short drama generation:

<div align="center">

**Sample Work 1**

<video src="https://ffile.chatfire.site/cf/public/20260114094337396.mp4" controls width="640"></video>

**Sample Work 2**

<video src="https://ffile.chatfire.site/cf/public/fcede75e8aeafe22031dbf78f86285b8.mp4" controls width="640"></video>

[Watch Video 1](https://ffile.chatfire.site/cf/public/20260114094337396.mp4) | [Watch Video 2](https://ffile.chatfire.site/cf/public/fcede75e8aeafe22031dbf78f86285b8.mp4)

</div>

---

## ✨ Features

### 🎭 Character Management

- ✅ AI-generated character portraits
- ✅ Batch character generation
- ✅ Character image upload and management

### 🎬 Storyboard Production

- ✅ Automatic storyboard script generation
- ✅ Scene descriptions and shot design
- ✅ Storyboard image generation (text-to-image)
- ✅ Frame type selection (first frame/key frame/last frame/panel)

### 🎥 Video Generation

- ✅ Automatic image-to-video generation
- ✅ Video composition and editing
- ✅ Transition effects

### 📦 Asset Management

- ✅ Unified asset library management
- ✅ Local storage support
- ✅ Asset import/export
- ✅ Task progress tracking

---

## 🚀 Quick Start

### 📋 Prerequisites

| Software    | Version | Description                     |
| ----------- | ------- | ------------------------------- |
| **Go**      | 1.23+   | Backend runtime                 |
| **Node.js** | 18+     | Frontend build environment      |
| **npm**     | 9+      | Package manager                 |
| **FFmpeg**  | 4.0+    | Video processing (**Required**) |
| **SQLite**  | 3.x     | Database (built-in)             |

#### Installing FFmpeg

**macOS:**

```bash
brew install ffmpeg
```

**Ubuntu/Debian:**

```bash
sudo apt update
sudo apt install ffmpeg
```

**Windows:**
Download from [FFmpeg Official Site](https://ffmpeg.org/download.html) and configure environment variables

Verify installation:

```bash
ffmpeg -version
```

### ⚙️ Configuration

Copy and edit the configuration file:

```bash
cp configs/config.example.yaml configs/config.yaml
vim configs/config.yaml
```

Configuration file format (`configs/config.yaml`):

```yaml
app:
  name: "Huobao Drama API"
  version: "1.0.0"
  debug: true # Set to true for development, false for production

server:
  port: 5678
  host: "0.0.0.0"
  cors_origins:
    - "http://localhost:3012"
  read_timeout: 600
  write_timeout: 600

database:
  type: "sqlite"
  path: "./data/drama_generator.db"
  max_idle: 10
  max_open: 100

storage:
  type: "local"
  local_path: "./data/storage"
  base_url: "http://localhost:5678/static"

ai:
  default_text_provider: "openai"
  default_image_provider: "openai"
  default_video_provider: "doubao"
```

**Key Configuration Items:**

- `app.debug`: Debug mode switch (recommended true for development)
- `server.port`: Service port
- `server.cors_origins`: Allowed CORS origins for frontend
- `database.path`: SQLite database file path
- `storage.local_path`: Local file storage path
- `storage.base_url`: Static resource access URL
- `ai.default_*_provider`: AI service provider configuration (API keys configured in Web UI)

### 📥 Installation

```bash
# Clone the project
git clone https://github.com/chatfire-AI/huobao-drama.git
cd huobao-drama

# Install Go dependencies
go mod download

# Install frontend dependencies
cd web
npm install
cd ..
```

### 🎯 Starting the Project

#### Method 1: Development Mode (Recommended)

**Frontend and backend separation with hot reload**

`