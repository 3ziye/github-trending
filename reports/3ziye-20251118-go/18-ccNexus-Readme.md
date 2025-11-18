# ccNexus (Claude Code Nexus)

<div align="center">

**A smart API endpoint rotation proxy for Claude Code**

[![Build Status](https://github.com/lich0821/ccNexus/workflows/Build%20and%20Release/badge.svg)](https://github.com/lich0821/ccNexus/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Go Version](https://img.shields.io/badge/Go-1.22+-00ADD8?logo=go)](https://go.dev/)
[![Wails](https://img.shields.io/badge/Wails-v2-blue)](https://wails.io/)

[English](README.md) | [简体中文](README_CN.md)

</div>

## 📸 Screenshot

![ccNexus Screenshot](docs/images/screenshot-EN.png)

## ✨ Features

- 🔄 **Automatic Endpoint Rotation** - Seamlessly switches between endpoints on errors
- 🌐 **Multi-Provider Support** - Use official Claude API and third-party providers
- 🔀 **Multi-Format Transformer** - Support Claude, OpenAI, and Gemini API formats
- 🔁 **Smart Retry** - Retries on any non-200 response
- 📊 **Real-time Statistics** - Monitor requests, errors, and endpoint usage
- 💰 **Token Usage Tracking** - Track input/output tokens for each endpoint
- 🎯 **Endpoint Management** - Enable/disable endpoints with toggle switches
- 🔐 **Secure API Key Display** - Shows only last 4 characters of API keys
- 🚦 **Smart Load Balancing** - Distributes requests only to enabled endpoints
- 📋 **Comprehensive Logging** - Multi-level logging (DEBUG/INFO/WARN/ERROR) with real-time viewing
- 🖥️ **Desktop GUI** - Beautiful cross-platform interface built with Wails
- 🚀 **Single Binary** - No dependencies, just download and run
- 🔧 **Easy Configuration** - Manage endpoints through GUI or config file
- 💾 **Persistent Config** - Automatically saves configuration and preferences
- 🔒 **Local First** - All data stays on your machine

## 🚀 Quick Start

### Download

Download the latest release for your platform:

- **Windows**: `ccNexus-windows-amd64.zip`
- **macOS (Intel)**: `ccNexus-darwin-amd64.zip`
- **macOS (Apple Silicon)**: `ccNexus-darwin-arm64.zip`
- **Linux**: `ccNexus-linux-amd64.tar.gz`

[📥 Download Latest Release](https://github.com/lich0821/ccNexus/releases/latest)

### Installation

#### Windows

1. Extract the ZIP file
2. Double-click `ccNexus.exe`
3. The application will start with a default configuration

#### macOS

1. Extract the ZIP file
2. Move `ccNexus.app` to Applications folder
3. Right-click and select "Open" (first time only)
4. The application will start with a default configuration

#### Linux

```bash
tar -xzf ccNexus-linux-amd64.tar.gz
chmod +x ccNexus
./ccNexus
```

### Configuration

1. **Add Endpoints**: Click "Add Endpoint" button
2. **Fill in Details**:
   - Name: A friendly name (e.g., "Claude Official")
   - API URL: The API server address (e.g., `api.anthropic.com`)
   - API Key: Your API key
   - Transformer: Select API format (Claude/OpenAI/Gemini)
   - Model: Required for OpenAI and Gemini (e.g., `gpt-4-turbo`, `gemini-pro`)
3. **Save**: Click "Save" to add the endpoint

### Configure Claude Code

In Claude Code settings:
- **API Base URL**: `http://localhost:3000`
- **API Key**: Any value (will be replaced by proxy)

## 📖 How It Works

```
Claude Code → Proxy (localhost:3000) → Endpoint #1 (non-200 response)
                                     → Endpoint #2 (success) ✅
```

1. **Request Interception**: Proxy receives all API requests
2. **Endpoint Selection**: Uses current available endpoint
3. **Error Detection**: Monitors response status codes
4. **Auto Retry**: Switches endpoint and retries on non-200 responses
5. **Round Robin**: Cycles through all endpoints

## 🔧 Configuration File

Configuration is stored at:
- **Windows**: `%USERPROFILE%\.ccNexus\config.json`
- **macOS/Linux**: `~/.ccNexus/config.json`

Example:

```json
{
  "port": 3000,
  "logLevel": 1,
  "endpoints": [
    {
      "name": "Claude Official 1",
      "apiUrl": "api.anthropic.com",
      "apiKey": "sk-ant-api03-your-key-1",
      "transformer": "claude",
      "enabled": true
    },
    {
      "name": "OpenAI Compatible",
      "apiUrl": "api.openai.com",
      "apiKey": "sk-your-openai-key",
      "transformer": "openai",
      "model": "gpt-4-turbo",
      "enabled": true
    },
    {
      "name": "Google Gemini",
      "apiUrl": "generativelanguage.googleapis.com",
      "apiKey": "your-gemini-key",
      "transformer": "gemini",
      "model": "gemini-pro",
      "enabled": true
    }
  ]
}
```

**Configuration Fields:**
- `port`: Proxy server port (default: 3000)
- `logLevel`: Logging level - 0=DEBUG, 1=INFO, 2=WARN, 3=ERROR (default: 1)
- `endpoints`: Array of API endpoints
  - `name`: Friendly name for the endpoint
  - `apiUrl`: API server address
  - `apiKey`: API authentication key
  - `transformer`: API format - "claude" (default), "openai", or "gemini"
  - `model`: Model name (required for OpenAI and Gemini 