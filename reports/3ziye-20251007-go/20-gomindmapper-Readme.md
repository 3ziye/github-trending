<div align="center">

# GoMindMapper

🚀 **Advanced Go Function Relationship Visualizer** 🚀

Interactive function relationship visualization for Go codebases with intelligent type resolution, interface implementation detection, and external module analysis. Scan any Go repository and explore it through an expandable, pannable, zoomable mind map.

`Go (AST Analyzer + HTTP API)` + `React (Interactive Mind Map)` + `Notion‑style UI`

[![GitHub Stars](https://img.shields.io/github/stars/chinmay-sawant/gomindmapper?style=social)](https://github.com/chinmay-sawant/gomindmapper) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Go Version](https://img.shields.io/github/go-mod/go-version/chinmay-sawant/gomindmapper)](https://golang.org/)

---

</div>

## 📋 Table of Contents
1. [🚀 Quick Start](#quick-start)
2. [✨ Features Overview](#features-overview)
3. [🏗️ Architecture](#architecture)
4. [⚙️ Installation & Setup](#installation--setup)
5. [🔧 Development](#development)
6. [📖 Usage Guide](#usage-guide)
7. [🎯 Advanced Features](#advanced-features)
8. [🔍 API Reference](#api-reference)
9. [📊 Data Models](#data-models)
10. [🎨 Customization](#customization)
11. [🗺️ Roadmap](#roadmap)
12. [🤝 Contributing](#contributing)
13. [📄 License](#license)

---

<a id="quick-start"></a>
## 🚀 Quick Start

Get started with GoMindMapper in under 2 minutes:

### Single Command Deployment
```bash
# Clone and run (example analyzing the 'gopdfsuit' subdirectory)
git clone https://github.com/chinmay-sawant/gomindmapper.git
cd gomindmapper
go run cmd/server/main.go -path gopdfsuit -addr :8080 --include-external=true --skip-folders="golang.org,gin-gonic,bytedance,ugorji,go-playground"
```

**Command Flags:**
- `-path <dir>`: Repository/subfolder to analyze (e.g., `gopdfsuit`)
- `-addr <addr>`: HTTP server address (default `:8080`)
- `--include-external`: Include external module functions in analysis
- `--skip-folders`: Comma-separated dependency prefixes to skip during external scanning

**Access Points:**
- 🌐 **Overview**: http://localhost:8080/gomindmapper/
- 🗺️ **Mind Map**: http://localhost:8080/gomindmapper/view/

> **Note**: Production React assets are automatically served by the Go server — no separate frontend setup required!

### Makefile Shortcuts
```bash
make ui-build   # Build React frontend
make server     # Start Go server
make ui         # Start React dev server
make run        # Run CLI analyzer
```

---

<a id="features-overview"></a>
## ✨ Features Overview

GoMindMapper goes beyond simple function visualization with advanced Go code analysis capabilities:

### 🎯 Core Analysis Engine
* **🧠 AST-based Go Analysis** - Uses Go's built-in AST parsing for accurate function extraction
* **🔍 Smart Root Detection** - Automatically identify top-level entry points (functions not called by any other user function)
* **🏗️ Interface Implementation Detection** - Discover concrete implementations of interfaces and add them to call graphs
* **🔗 Type Resolution Engine** - Resolve method calls through comprehensive type analysis
* **📦 External Module Scanning** - Recursively scan external dependencies with intelligent filtering
* **🎛️ Advanced Filtering** - Multi-layer filtering: stdlib, external libraries, framework noise, custom patterns
* **⚡ Performance Optimization** - Parallel processing, in-memory caching, and efficient data structures

### 🎨 Interactive UI & Visualization
* **🗺️ Google NotebookLLM-inspired Nodes** - Custom-designed function nodes with color-coded types (main, handler, middleware, config, router)
* **🖱️ Intuitive Controls** - Pan (drag background), zoom (mouse wheel), expand/collapse nodes individually
* **🌓 Advanced Theming** - Dark/light theme with system preference detection and localStorage persistence
* **📤 Drag & Drop Upload** - Drop JSON files directly onto interface for offline analysis
* **🔎 Real-time Search** - Debounced search with instant results and pagination
* **📋 Function Details Panel** - Comprehensive information display on node selection (file path, line numbers, calls)
* **📱 Responsive Design** - Works seamlessly across desktop, tablet, and mobile devices
* **🎞️ Screenshot Slideshow** - Interactive feature showcase with auto-play and navigation
* **📊 Comparison Table** - Built-in comparison with other Go visualization tools

### 🔧 Data Management & Integration
* **🔄 Dual Data Modes** - Switch between offline JSON snapshots or live server API
* **🔥 Hot Reload Capability** - Refresh data from repository without restarting (`POST /api/reload`)
* **💾 Multi-format Export** - Download as JSON, with planned support for GraphML/DOT/SVG
* **📊 Multiple Output Formats** - Generate `functions.json`, `functionmap.json`, and `removed_calls.json`
* **🌐 Live Server Integration** - RESTful API with pagination, search, and real-time updates
* **🔒 Concurrent Safety** - Thread-safe operations with proper mutex handling

---

<a id="architecture"></a>
## 🏗️ Archit