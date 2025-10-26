[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/yusufkaraaslan-skill-seekers-badge.png)](https://mseep.ai/app/yusufkaraaslan-skill-seekers)

# Skill Seeker

[![Version](https://img.shields.io/badge/version-1.2.0-blue.svg)](https://github.com/yusufkaraaslan/Skill_Seekers/releases/tag/v1.2.0)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![MCP Integration](https://img.shields.io/badge/MCP-Integrated-blue.svg)](https://modelcontextprotocol.io)
[![Tested](https://img.shields.io/badge/Tests-207%20Passing-brightgreen.svg)](tests/)
[![Project Board](https://img.shields.io/badge/Project-Board-purple.svg)](https://github.com/users/yusufkaraaslan/projects/2)

**Automatically convert any documentation website into a Claude AI skill in minutes.**

> 📋 **[View Development Roadmap & Tasks](https://github.com/users/yusufkaraaslan/projects/2)** - 134 tasks across 10 categories, pick any to contribute!

## What is Skill Seeker?

Skill Seeker is an automated tool that transforms any documentation website into a production-ready [Claude AI skill](https://claude.ai). Instead of manually reading and summarizing documentation, Skill Seeker:

1. **Scrapes** documentation websites automatically
2. **Organizes** content into categorized reference files
3. **Enhances** with AI to extract best examples and key concepts
4. **Packages** everything into an uploadable `.zip` file for Claude

**Result:** Get comprehensive Claude skills for any framework, API, or tool in 20-40 minutes instead of hours of manual work.

## Why Use This?

- 🎯 **For Developers**: Quickly create Claude skills for your favorite frameworks (React, Vue, Django, etc.)
- 🎮 **For Game Devs**: Generate skills for game engines (Godot, Unity documentation, etc.)
- 🔧 **For Teams**: Create internal documentation skills for your company's APIs
- 📚 **For Learners**: Build comprehensive reference skills for technologies you're learning

## Key Features

### 🌐 Documentation Scraping
- ✅ **llms.txt Support** - Automatically detects and uses LLM-ready documentation files (10x faster)
- ✅ **Universal Scraper** - Works with ANY documentation website
- ✅ **Smart Categorization** - Automatically organizes content by topic
- ✅ **Code Language Detection** - Recognizes Python, JavaScript, C++, GDScript, etc.
- ✅ **8 Ready-to-Use Presets** - Godot, React, Vue, Django, FastAPI, and more

### 📄 PDF Support (**v1.2.0**)
- ✅ **Basic PDF Extraction** - Extract text, code, and images from PDF files
- ✅ **OCR for Scanned PDFs** - Extract text from scanned documents
- ✅ **Password-Protected PDFs** - Handle encrypted PDFs
- ✅ **Table Extraction** - Extract complex tables from PDFs
- ✅ **Parallel Processing** - 3x faster for large PDFs
- ✅ **Intelligent Caching** - 50% faster on re-runs

### 🤖 AI & Enhancement
- ✅ **AI-Powered Enhancement** - Transforms basic templates into comprehensive guides
- ✅ **No API Costs** - FREE local enhancement using Claude Code Max
- ✅ **MCP Server for Claude Code** - Use directly from Claude Code with natural language

### ⚡ Performance & Scale
- ✅ **Large Documentation Support** - Handle 10K-40K+ page docs with intelligent splitting
- ✅ **Router/Hub Skills** - Intelligent routing to specialized sub-skills
- ✅ **Parallel Scraping** - Process multiple skills simultaneously
- ✅ **Checkpoint/Resume** - Never lose progress on long scrapes
- ✅ **Caching System** - Scrape once, rebuild instantly

### ✅ Quality Assurance
- ✅ **Fully Tested** - 207 tests with 100% pass rate

## Quick Example

### Option 1: Use from Claude Code (Recommended)

```bash
# One-time setup (5 minutes)
./setup_mcp.sh

# Then in Claude Code, just ask:
"Generate a React skill from https://react.dev/"
"Scrape PDF at docs/manual.pdf and create skill"
```

**Time:** Automated | **Quality:** Production-ready | **Cost:** Free

### Option 2: Use CLI Directly (HTML Docs)

```bash
# Install dependencies (2 pip packages)
pip3 install requests beautifulsoup4

# Generate a React skill in one command
python3 cli/doc_scraper.py --config configs/react.json --enhance-local

# Upload output/react.zip to Claude - Done!
```

**Time:** ~25 minutes | **Quality:** Production-ready | **Cost:** Free

### Option 3: Use CLI for PDF Documentation

```bash
# Install PDF support
pip3 install PyMuPDF

# Basic PDF extraction
python3 cli/pdf_scraper.py --pdf docs/manual.pdf --name myskill

# Advanced features
python3 cli/pdf_scraper.py --pdf docs/manual.pdf --name myskill \
    --extract-tables \        # Extract tables
    --parallel \              # Fast parallel processing
    --workers 8               # Use 8 CPU cores

# Scanned PDFs (requires: pip install pytesseract Pillow)
python3 cli/pdf_scraper.py --pdf docs/scanned.pdf --name myskill --ocr

# Password-protected PDFs
python3 cli/pdf_scraper.py --pdf docs/encrypted.pdf --name myskill --password