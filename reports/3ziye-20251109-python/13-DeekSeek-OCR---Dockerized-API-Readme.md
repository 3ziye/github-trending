# DeepSeek-OCR: PDF to Markdown Converter

A powerful OCR solution that converts PDF documents to Markdown format using DeepSeek-OCR with FastAPI backend. This project provides both a batch processing script and a REST API for flexible document conversion.

## 🚀 Quick Start

### Option 1: Batch Processing with pdf_to_markdown_processor.py

1. Place your PDF files in the `data/` directory
2. Ensure the DeepSeek-OCR API is running (see Docker setup below)
3. Run the processor:

```bash
python pdf_to_markdown_processor.py
```

### Option 2: REST API with Docker Backend

1. Build and start the Docker container
2. Use the API endpoints to process documents
3. Integrate with your applications

---

## 📋 Prerequisites

### Hardware Requirements
- **NVIDIA GPU** with CUDA 11.8+ support
- **GPU Memory**: Minimum 12GB VRAM (Model takes ~9GB)
- **System RAM**: Minimum 32GB (recommended: 64GB+)
- **Storage**: 50GB+ free space for model and containers

### Software Requirements
- **Python 3.8+** (for local processing)
- **Docker** 20.10+ with GPU support
- **Docker Compose** 2.0+
- **NVIDIA Container Toolkit** installed
- **CUDA 11.8** compatible drivers

---

## 🐳 Docker Backend Setup

### 1. Download Model Weights

Create a directory for model weights and download the DeepSeek-OCR model:

```bash
# Create models directory
mkdir -p models

# Download using Hugging Face CLI
pip install huggingface_hub
huggingface-cli download deepseek-ai/DeepSeek-OCR --local-dir models/deepseek-ai/DeepSeek-OCR

# Or using git
git clone https://huggingface.co/deepseek-ai/DeepSeek-OCR models/deepseek-ai/DeepSeek-OCR
```

### 2. Build and Run the Docker Container

#### Windows Users

```cmd
REM Build the Docker image
build.bat

REM Start the service
docker-compose up -d

REM Check logs
docker-compose logs -f deepseek-ocr
```

#### Linux/macOS Users

```bash
# Build the Docker image
docker-compose build

# Start the service
docker-compose up -d

# Check logs
docker-compose logs -f deepseek-ocr
```

### 3. Verify Installation

```bash
# Health check
curl http://localhost:8000/health

# Expected response:
{
  "status": "healthy",
  "model_loaded": true,
  "model_path": "/app/models/deepseek-ai/DeepSeek-OCR",
  "cuda_available": true,
  "cuda_device_count": 1
}
```

---

## 📄 PDF Processing Scripts

This project provides several PDF processing scripts, each designed for different use cases. All scripts scan the `data/` directory for PDF files and convert them to Markdown format with different prompts and post-processing options.

### Output Naming Convention

All processors append a suffix to the output filename to indicate the processing method used:
- **-MD.md**: Markdown conversion (preserves document structure)
- **-OCR.md**: Plain OCR extraction (raw text without formatting)
- **-CUSTOM.md**: Custom prompt processing (uses prompt from YAML file)

For example, processing `document.pdf` will create:
- `document-MD.md` (markdown processors)
- `document-OCR.md` (OCR processor)
- `document-CUSTOM.md` (custom prompt processors)

---

### 1. pdf_to_markdown_processor.py

**Purpose**: Basic PDF to Markdown conversion using the standard markdown prompt

**Features**:
- Uses prompt: `'<image>\n<|grounding|>Convert the document to markdown.'`
- Converts PDFs to structured Markdown format
- Simple processing without image extraction
- Outputs files with `-MD.md` suffix

**Usage**:
```bash
# Place PDF files in the data directory
cp your_document.pdf data/

# Run the processor
python pdf_to_markdown_processor.py

# Check results
ls data/*-MD.md
```

---

### 2. pdf_to_markdown_processor_enhanced.py

**Purpose**: Enhanced PDF to Markdown conversion with post-processing

**Features**:
- Uses the same markdown prompt as the basic version
- **Post-processing features**:
  - Image extraction and saving to `data/images/` folder
  - Special token cleanup
  - Reference processing for layout information
  - Content cleaning and formatting
- Outputs files with `-MD.md` suffix

**Usage**:
```bash
# Place PDF files in the data directory
cp your_document.pdf data/

# Run the enhanced processor
python pdf_to_markdown_processor_enhanced.py

# Check results (including extracted images)
ls data/*-MD.md
ls data/images/
```

---

### 3. pdf_to_ocr_enhanced.py

**Purpose**: Plain OCR text extraction without markdown formatting

**Features**:
- Uses OCR prompt: `'<image>\nFree OCR.'`
- Extracts raw text without markdown structure
- Includes the same post-processing features as the enhanced markdown processor
- Outputs files with `-OCR.md` suffix

**Usage**:
```bash
# Place PDF files in the data directory
cp your_document.pdf data/

# Run the OCR processor
python pdf_to_ocr_enhanced.py

# Check results
ls data/*-OCR.md
```

---

### 4. pdf_to_custom_prompt.py

**Purpose**: PDF processing with custom prompts (raw output)

**Features**:
- Uses custom prompt loaded from `custom_prompt.yaml`
- Returns raw model response without post-processing
- Ideal for testing and debugging 