# Multi-Source Media MCP Server (M3S)

[![Go](https://img.shields.io/badge/go-1.25.1%2B-blue.svg)](https://go.dev/) [![MCP Go SDK](https://img.shields.io/badge/mcp--go--sdk-v1.0.0-green.svg)](https://github.com/modelcontextprotocol/go-sdk) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 📖 Overview

**Multi-Source Media MCP Server (M3S)** is a high-performance, extensible MCP (Model Context Protocol) tool server written in Go. It provides a unified interface for Large Language Models (LLMs) to access, generate, and manipulate media content from a variety of sources.

By acting as a bridge between LLMs and diverse media APIs, web sources, and local files, M3S enables complex, media-rich workflows in AI applications.

### ✨ Key Features

- **Multi-Source Access**: Unified interface to fetch images and videos from platforms like Unsplash and Pexels.
- **AI-Powered Generation**: Built-in tools for text-to-image and image-to-image generation using various AI backends.
- **Web Content Crawling**: Asynchronously crawl and retrieve images from web pages.
- **Extensible by Design**: Easily add new tools, media sources, or AI backends.

---

## 🚀 Build & Run

1.  **Build the server:**

    ```bash
    go build -o m3s-server ./cmd/server
    ```

2.  **Run the server:**

    The server loads configuration from `configs/config.yaml` by default.

    ```bash
    ./m3s-server    
    ```

    To use a different configuration file, use the `-config` flag:

    ```bash
    ./m3s-server --config=path/to/your/config.yaml
    ```

For more detailed instructions, see [docs/build.md](docs/build.md).

---

## 📝 Future Work

- [ ] **User Content Management**: Implement tools for uploading, listing, and managing user-owned images.
- [ ] **Text-to-Video Generation**: Add a new tool for generating video content from text prompts.
- [ ] **Embedding-based Similarity Search**: Implement a tool to find visually similar images based on an input image.
- [ ] **Caching & Performance**: Introduce a caching layer for API responses to improve performance and reduce rate-limit consumption.
- [ ] **AI-based Tagging**: Add a tool to automatically generate descriptive tags or captions for images.
