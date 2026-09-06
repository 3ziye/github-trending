<div align="center">

<img src="https://raw.githubusercontent.com/GangTailorUpgrade/dress-ai-service/main/docs/logo.png" alt="Dress AI Service" width="180">

# 👗 Dress AI Service

**Self-Hosted AI Outfit Generator & Virtual Wardrobe Stylist**

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-009688.svg)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/GangTailorUpgrade/dress-ai-service?style=social)](https://github.com/GangTailorUpgrade/undress-service)

🚀 **Turn your closet into an AI-powered fashion assistant.** Upload your wardrobe, get smart outfit recommendations for any occasion, and visualize your looks with generative AI — all self-hosted, private, and free.

[🎥 Demo Video](#) · [📖 Documentation](docs/) · [🐳 Quick Start](#quick-start) · [💬 Discord](#)

</div>

---

## ✨ What is Dress AI Service?

**Dress AI Service** is an open-source, self-hosted AI fashion platform that helps you:

- 📸 **Digitize your wardrobe** — Upload photos of your clothes; AI auto-tags them by category, color, style, and season
- 🧠 **Get smart outfit recommendations** — AI suggests perfect combinations based on occasion, weather, and your personal style
- 🎨 **Visualize outfits before wearing** — Generate AI renderings of how recommended outfits will look
- 🌤️ **Weather-aware styling** — Integrates real-time weather to suggest appropriate layers and fabrics
- 🏠 **100% self-hosted** — Your photos stay on your machine. No cloud uploads. No privacy concerns.

Whether you're a fashion enthusiast, a boutique owner, or a developer building the next generation of fashion tech, Dress AI Service gives you a complete, production-ready foundation.

---

## 🖼️ Screenshots

| Wardrobe Upload | AI Tagging | Outfit Recommendations | AI Visualization |
|---|---|---|---|
| ![Upload](docs/screenshots/upload.png) | ![Tagging](docs/screenshots/tagging.png) | ![Outfits](docs/screenshots/outfits.png) | ![Visualize](docs/screenshots/visualize.png) |

---
## 💖 Sponsors

Dress AI Service is made possible by our amazing sponsors. Support the project and get your logo here!

<div align="center">


[<img width="1672" height="941" alt="5259cbc0-c12f-40e1-934b-d0f6802f745c" src="https://github.com/user-attachments/assets/43a0f5ad-c0b0-427d-9d24-0824c5bb8fa7"/>](https://undress.design/undress/?utm_source=github.com%2FGangTailorUpgrade%2Fundress-service&utm_medium=sponsorship&utm_campaign=github-september-2026&utm_content=readme-sponsor)

### Option 1: Docker (Recommended)

```bash
git clone https://github.com/GangTailorUpgrade/undress-service.git
cd dress-ai-service
cp .env.example .env
docker-compose up --build
```

Visit `http://localhost:8080` — your personal AI stylist is live! 🎉

### Option 2: Local Python

```bash
git clone https://github.com/GangTailorUpgrade/undress-service.git
cd dress-ai-service
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Download AI models (first run)
python scripts/download_models.py

# Start the server
uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Dress AI Service                        │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │  Wardrobe   │  │   Outfit    │  │   AI Visualization  │ │
│  │   Upload    │  │   Engine    │  │      Pipeline       │ │
│  │  & Storage  │  │  (Rules +   │  │  (Stable Diffusion  │ │
│  │             │  │   LLM)      │  │   / FLUX / SDXL)    │ │
│  └──────┬──────┘  └──────┬──────┘  └──────────┬──────────┘ │
│         │                │                     │            │
│  ┌──────▼────────────────▼─────────────────────▼──────────┐ │
│  │              FastAPI Backend (Python 3.11)             │ │
│  │  • SQLite / PostgreSQL  • CLIP Tagging  • Weather API │ │
│  └─────────────────────────┬──────────────────────────────┘ │
│                            │                                │
│  ┌─────────────────────────▼──────────────────────────────┐ │
│  │              Self-Hosted Frontend (HTML/JS)            │ │
│  │         • Drag & Drop Upload  • Live Preview          │ │
│  └────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend** | FastAPI + Python 3.11 | High-performance async API |
| **AI/ML** | CLIP, Stable Diffusion XL, FLUX.1-schnell | Image understanding & generation |
| **Database** | SQLite (default) / PostgreSQL | Wardrobe & outfit storage |
| **Frontend** | 