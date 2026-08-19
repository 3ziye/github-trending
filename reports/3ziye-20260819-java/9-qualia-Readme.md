<div align="center">

# Qualia

**Enterprise-grade Java AI Agent Framework**

*Build LLM-driven intelligent applications quickly with the ReAct pattern and MCP toolchain integration*

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Java](https://img.shields.io/badge/Java-17+-orange.svg)](https://adoptium.net/)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.x-green.svg)](https://spring.io/projects/spring-boot)
[![Maven](https://img.shields.io/badge/Maven-3.8+-C71A36.svg)](https://maven.apache.org/)
[![MCP](https://img.shields.io/badge/MCP-Protocol-purple.svg)](https://modelcontextprotocol.io/)

[Quick Start](#-quick-start) · [Showcase](#showcase) · [Release](#-release)

**English** | [简体中文](README.zh-CN.md)

</div>

---

## Overview

Qualia is a lightweight, modular Java framework for building LLM-powered agent applications. It provides a complete agent development framework with multi-model access, tool invocation, knowledge base retrieval, and skill extension capabilities, suitable for building enterprise AI assistants, intelligent customer service, code assistants, and more.

Based on the ReAct (Reasoning + Acting) paradigm, it supports complex task decomposition through think-act-observe loops; a unified interface adapts to mainstream LLMs such as DashScope, OpenAI, and Claude; an annotation-driven tool system with MCP protocol integration makes tool capabilities easy to extend; JSON/MySQL-based conversation memory management supports sliding windows and summary compression; and a skill system with reusable prompt templates and script execution supports progressive loading.

## Modules

```
qualia/
├── qualia-core/          # Core module
├── qualia-code/          # Code module (includes web service)
├── qualia-code-desktop/  # Code desktop app
├── qualia-claw/          # Claw module (includes web service)
├── qualia-claw-desktop/  # Claw desktop app
└── qualia-docs/          # Project documentation
```

**Qualia-core** The framework core module, providing the agent core architecture (ReActAgent, HarnessAgent), the model protocol abstraction layer (ChatModel, EmbeddingModel, RerankModel), the tool system and MCP integration, conversation memory management, the RAG retrieval pipeline, and the skill system.

**Qualia-code** An AI coding assistant product built on the Qualia framework, delivering a complete Web IDE experience: multi-session management and workspace switching, code generation and analysis, file read/write and search, terminal command execution, tool-call visualization, MCP server management, multi-model configuration with dynamic switching, streaming responses and real-time interaction, available in both desktop and web deployment modes.

**Qualia-code-desktop** The desktop application module, built on SWT with an embedded browser loading the Web IDE UI. Provides a native desktop experience with window state persistence (size, position, maximized state), system title-bar theme synchronization (automatic dark/light adaptation), and cross-platform support (Windows/macOS).

**Qualia-claw** A multi-agent collaboration product built on the Qualia framework. Each agent has its own workstation (system-managed workspace + independent conversation memory), supporting role personas, parallel multi-agent conversations, global skills and MCP servers referenced via per-agent allowlists, workspace file browsing and preview, and per-session token usage statistics. All configuration is consolidated in the user home directory, isolated per product, and it likewise supports both desktop and web deployment modes.

**Qualia-claw-desktop** The Claw desktop application module, architecturally identical to Qualia-code-desktop (SWT + system WebView). Lock files, window state, and crash logs are isolated per product directory, so it can run alongside the Qualia Code desktop app.

## 🚀 Quick Start

### Installation

qualia-core is published via GitHub Packages. Consuming the dependency requires repository authentication and repository configuration:

#### 1. Configure Authentication

Add GitHub credentials to your Maven `settings.xml` (or a project-level `settings.xml`):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<settings>
    <servers>
        <server>
            <id>github</id>
            <username>your-github-username</username>
            <password>your-github-token (requires read:packages scope)</password>
        </server>
    </servers>
</settings>
```

#### 2. Add Repository and Dependency

Add the following to your project `pom.xml`:

```xml
<repositories>
    <repository>
        <id>github</id>
        <url>https://maven.pkg.github.com/lunar-landing/qualia</url>
    </repository>
</repositories>

<dependency>
    <groupId>com.lunarlanding</groupId>
    <artifactId>qualia-core</artifactId>
    <version>0.1.0</version>
</dependency>
```

### 5-Minute Tutorial

```java
// 1. Initialize the model and memory
ChatModel model = new DashscopeChatModel("your