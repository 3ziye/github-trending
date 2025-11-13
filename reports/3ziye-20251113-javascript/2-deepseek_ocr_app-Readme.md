# 🚀 DeepSeek OCR - React + FastAPI

Modern OCR web application powered by DeepSeek-OCR with a stunning React frontend and FastAPI backend.

![DeepSeek OCR in Action](assets/multi-bird.png)

> **Recent Updates (v2.1.1)**
> - ✅ Fixed image removal button - now properly clears and allows re-upload
> - ✅ Fixed multiple bounding boxes parsing - handles `[[x1,y1,x2,y2], [x1,y1,x2,y2]]` format
> - ✅ Simplified to 4 core working modes for better stability
> - ✅ Fixed bounding box coordinate scaling (normalized 0-999 → actual pixels)
> - ✅ Fixed HTML rendering (model outputs HTML, not Markdown)
> - ✅ Increased file upload limit to 100MB (configurable)
> - ✅ Added .env configuration support

## Quick Start

1. **Clone and configure:**
   ```bash
   git clone <repository-url>
   cd deepseek_ocr_app
   
   # Copy and customize environment variables
   cp .env.example .env
   # Edit .env to configure ports, upload limits, etc.
   ```

2. **Start the application:**
   ```bash
   docker compose up --build
   ```

   The first run will download the model (~5-10GB), which may take some time.

3. **Access the application:**
   - **Frontend**: http://localhost:3000 (or your configured FRONTEND_PORT)
   - **Backend API**: http://localhost:8000 (or your configured API_PORT)
   - **API Docs**: http://localhost:8000/docs

## Features

### 4 Core OCR Modes
- **Plain OCR** - Raw text extraction from any image
- **Describe** - Generate intelligent image descriptions
- **Find** - Locate specific terms with visual bounding boxes
- **Freeform** - Custom prompts for specialized tasks

### UI Features
- 🎨 Glass morphism design with animated gradients
- 🎯 Drag & drop file upload (up to 100MB by default)
- 🗑️ Easy image removal and re-upload
- 📦 Grounding box visualization with proper coordinate scaling
- ✨ Smooth animations (Framer Motion)
- 📋 Copy/Download results
- 🎛️ Advanced settings dropdown
- 📝 HTML and Markdown rendering for formatted output
- 🔍 Multiple bounding box support (handles multiple instances of found terms)

## Configuration

The application can be configured via the `.env` file:

```bash
# API Configuration
API_HOST=0.0.0.0
API_PORT=8000

# Frontend Configuration
FRONTEND_PORT=3000

# Model Configuration
MODEL_NAME=deepseek-ai/DeepSeek-OCR
HF_HOME=/models

# Upload Configuration
MAX_UPLOAD_SIZE_MB=100  # Maximum file upload size

# Processing Configuration
BASE_SIZE=1024         # Base processing resolution
IMAGE_SIZE=640         # Tile processing resolution
CROP_MODE=true         # Enable dynamic cropping for large images
```

### Environment Variables

- `API_HOST`: Backend API host (default: 0.0.0.0)
- `API_PORT`: Backend API port (default: 8000)
- `FRONTEND_PORT`: Frontend port (default: 3000)
- `MODEL_NAME`: HuggingFace model identifier
- `HF_HOME`: Model cache directory
- `MAX_UPLOAD_SIZE_MB`: Maximum file upload size in megabytes
- `BASE_SIZE`: Base image processing size (affects memory usage)
- `IMAGE_SIZE`: Tile size for dynamic cropping
- `CROP_MODE`: Enable/disable dynamic image cropping

## Tech Stack

- **Frontend**: React 18 + Vite 5 + TailwindCSS 3 + Framer Motion 11
- **Backend**: FastAPI + PyTorch + Transformers 4.46 + DeepSeek-OCR
- **Configuration**: python-decouple for environment management
- **Server**: Nginx (reverse proxy)
- **Container**: Docker + Docker Compose with multi-stage builds
- **GPU**: NVIDIA CUDA support (tested on RTX 3090, RTX 5090)

## Project Structure

```
deepseek-ocr/
├── backend/           # FastAPI backend
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/          # React frontend
│   ├── src/
│   │   ├── components/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   ├── nginx.conf
│   └── Dockerfile
├── models/            # Model cache
└── docker-compose.yml
```

## Development

Docker compose cycle to test:
```bash
docker compose down
docker compose up --build
```

## Requirements

### Hardware
- NVIDIA GPU with CUDA support
  - Recommended: RTX 3090, RTX 4090, RTX 5090, or better
  - Minimum: 8-12GB VRAM for the model
  - More VRAM always good!

### Software
- **Docker & Docker Compose** (latest version recommended)

- **NVIDIA Driver** - Installing NVIDIA Drivers on Ubuntu (Blackwell/RTX 5090)

  **Note**: Getting NVIDIA drivers working on Blackwell GPUs can be a pain! Here's what worked:

  The key requirements for RTX 5090 on Ubuntu 24.04:
  - Use the open-source driver (nvidia-driver-570-open or newer, like nvidia-driver-580-open)
  - Upgrade to kernel 6.11+ (6.14+ recommended for best stability)
  - Enable Resize Bar in BIOS/UEFI (critical!)

  **Step-by-Step Instructions:**

  1. Install NVIDIA Open Driver (580 or newer)
     ```bash
     sudo add-apt-repository ppa:graphics-drivers/ppa
     sudo apt update
     sudo apt remove --purge nvidia*
     sudo nvidia-installer --uninstall  # If you have it
     sudo apt autoremove
     sudo apt install nvidia-driver-580-open
     ```

  2. Upgrade Linux Kernel to 6.11+ (for Ubuntu 24.