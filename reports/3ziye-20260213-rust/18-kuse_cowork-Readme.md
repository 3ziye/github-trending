

<div align="center">
  <img src="public/kuse-logo.png" alt="Kuse Cowork Logo" width="200"/>
</div>


<br>

<div align="center">

[![DISCORD](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/Pp5aZjMMAC)

</div>


# Kuse Cowork：An Open-Source, Model-Agnostic [Alternative to Claude Cowork](https://www.claude-cowork.ai/)
>Kuse Cowork is a lightweight, open-source desktop cowork agent built for people who want local-first execution, full model freedom, and real privacy control.

**Works with any models, BYOK, written in Rust** 🚀

[*Demo video: Kuse Cowork in action*](https://github.com/user-attachments/assets/e128e657-c1be-4134-828d-01a9a94ef055)

It is an open-source desktop cowork agent created by [Kuse](https://www.kuse.ai/), an AI document generator & Presentation Maker from your knowledge base. Transform docs, PDFs, YouTube, and images into formatted docs, infographics, mind maps, and flashcards—instantly. Stunning, professional, and ready to use.

## ✨ Why Kuse Cowork?

### 🔐 **BYOK (Bring Your Own Key)**
Use your own API keys or even **bring your own local models** for ultimate privacy control.

### ⚡ **Pure Rust Agent**
Agent fully written in Rust with **zero external dependencies** - blazingly fast and memory-safe.

### 🌍 **Native Cross-Platform**
True native performance on macOS, Windows, and Linux.

### 🛡️ **Container Isolation & Security**
Uses Docker containers for secure command execution and complete isolation.

### 🧩 **Extensible Skills System**
Support for custom skills to extend agent capabilities.
Default skills are: docx, pdf, pptx, xlsx.

### 🔗 **MCP Protocol Support**
Full support for Model Context Protocol (MCP) for seamless tool integration.

---
## 📰 News & Updates

### Standard release
- **\[2026-01-26\]** Release of v0.0.2: Fixing issue where "start task" button actively needs the user to set a cloud-based api key.

### Experimental 
-  **\[2026-01-29\]** Kuse_cowork now supports basic operations on Docx with an integrated UI && support working trace tracking.
-  **\[2026-01-26\]** Kuse_cowork now supports basic operations on Excel with an integrated UI.
 
  
---


## 🚀 Features

- **🔒 Local & Private**: Runs entirely on your machine, API calls go directly to your chosen provider
- **🔑 BYOK Support**: Use your own Anthropic, OpenAI, or local model APIs
- **🎯 Model Agnostic**: Works with Claude, GPT, local models, and more
- **🖥️ Cross-Platform**: macOS (ARM & Intel), Windows, and Linux
- **🪶 Lightweight**: ~10MB app size using Tauri
- **🐳 Containerized**: Docker isolation for enhanced security
- **🧩 Skills**: Extensible skill system for custom capabilities
- **🔗 MCP**: Model Context Protocol support for tool integration

## Security Note
This is still an early project and please be super careful when connecting with your local folders.

## 🚀 Quick Start

Get up and running in minutes:

### 1. Build the project and start

Will update to a clean release build soon. 

### 2. ⚙️ Configure Your AI Model
1. Open **Settings** (gear icon in sidebar)
2. **Choose your AI provider:**
   - **Anthropic Claude** - Enter your Claude API key
   - **OpenAI GPT** - Enter your OpenAI API key
   - **Local Models** - Configure Ollama/LM Studio endpoint
3. **Select your preferred model** (Claude 3.5 Sonnet, GPT-4, etc.)

### 3. 🔑 Enter API Key
- Add your API key in the settings
- Keys are stored locally and never shared

### 4. 📁 Set Workspace Folder
- Click **"Select Project Path"** when creating a new task
- Choose your project folder or workspace directory
- The agent will work within this folder context

### 5. 🎯 Start Your First Task!
1. Click **"New Task"**
2. Describe what you want to accomplish
3. Watch the AI agent work on your project
4. Review the plan and implementation steps

**Example tasks:**
- *"Organize my folders"*
- *"Read all the receipts and make an expense reports"*
- *"Summarize the meeting notes and give me all the TODOs."*


---

## 🛠️ Development

### Prerequisites

- [Node.js](https://nodejs.org/) 18+
- [Rust](https://rustup.rs/) (for Tauri)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (required for container isolation)
- [Tauri Prerequisites](https://tauri.app/start/prerequisites/)

**Note**: Docker Desktop must be installed and running for container isolation features. Without Docker, the app will still work but commands will run without isolation.

### Setup

```bash
# Clone the repo
git clone https://github.com/kuse-ai/kuse-cowork.git
cd kuse-cowork

# Install dependencies
npm install

# Run in development mode
npm run tauri dev

# Build for production
npm run tauri build
```

### Project Structure

```
kuse-cowork/
├── src/                    # Frontend (SolidJS + TypeScript)
│   ├── components/         # UI components
│   ├── lib/               # Utilities (API clients, MCP)
│   └── stores/            # State management
├── src-tauri/             # Backend (Rust + Tauri)
│   ├── src/   