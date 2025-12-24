# Spring AI Playground

**Spring AI Playground is a self-hosted web UI platform for building low-code tools and dynamically exposing them via built-in MCP server for AI agents.**

Unlike most AI playgrounds that focus solely on prompt testing and chat visualization, it bridges the gap between **static AI conversations** and **real-world actions** by enabling you to create executable tools that AI agents can use.

It brings together **Large Language Models (LLMs)**, **Retrieval-Augmented Generation (RAG)**, and **low-code tool development** in a single environment. Tools created in the **Tool Studio** are dynamically evaluated and loaded at runtime, then automatically registered and exposed as **Model Context Protocol (MCP) tools**. This makes them instantly available to MCP-compatible clients without restarting or redeploying.

<p align="center">
  <b>Agentic Chat Demo</b><br/>
  Tool-enabled agentic AI built with Spring AI and MCP
</p>

<p align="center">
  <a href="https://youtu.be/FlzV7TN67f0">
    <img src="https://img.youtube.com/vi/FlzV7TN67f0/0.jpg" width="800"/>
  </a>
</p>

## Key Capabilities

### Tool Studio & Built-in MCP Server
Create AI tools using **JavaScript (ECMAScript 2023)** directly in the browser. Powered by **GraalVM Polyglot**, these tools run inside the JVM (Polyglot) with configurable security constraints and are immediately exposed via **built-in MCP Server**. Experience a no-restart, no-redeploy workflow: just write, test, and publish.

### MCP Server & Tool Inspection
Connect to external **MCP servers**, inspect available tools, and validate tool execution behavior. Test both your custom **Tool Studio tools** and third-party MCP services in a unified interface.

### Vector Database & RAG Pipeline
Upload documents, configure **chunking** and **embeddings**, and test retrieval pipelines. Evaluate prompt execution against selected RAG sources to validate **knowledge-grounded** responses.

### Agentic Chat & Agent Workflow
Interact with LLMs in a chat interface where models can reason, select tools, and execute actions. Combine **MCP tools** and **RAG-enhanced context** to validate end-to-end agent workflows.

## Why Spring AI Playground?

- **Dynamic MCP Hosting**: Build and expose tools in real-time with immediate MCP server exposure and no deployment overhead.
- **Unified Testing Hub**: Validate prompts, RAG pipelines, and agentic workflows in a single, cohesive environment.
- **Provider Agnostic**: Switch between Ollama, OpenAI, and other LLM providers (including OpenAI-compatible APIs) with ease.
- **Built for Modern AI**: Designed specifically for the Spring AI ecosystem, MCP protocol, and agent-oriented architectures.

## Table of Contents

* [Overview](#spring-ai-playground)
* [Key Capabilities](#key-capabilities)
    * [Tool Studio & Built-in MCP Server](#tool-studio--built-in-mcp-server)
    * [MCP Server & Tool Inspection](#mcp-server--tool-inspection)
    * [Vector Database & RAG Pipeline](#vector-database--rag-pipeline)
    * [Agentic Chat & Agent Workflow](#agentic-chat--agent-workflow)
* [Why Spring AI Playground?](#why-spring-ai-playground)
* [Quick Start](#quick-start)
    * [Prerequisites](#prerequisites)
    * [Getting Started](#getting-started)
    * [Running the Application](#running-the-application)
        * [Running with Docker (Recommended)](#running-with-docker-recommended)
        * [Cleaning Up Docker](#cleaning-up-docker)
        * [Running Locally (Optional)](#running-locally-optional)
    * [PWA Installation](#pwa-installation)
* [Configuration](#auto-configuration)
* [AI Models](#ai-models)
    * [Supported Model Providers](#support-for-major-ai-model-providers)
    * [Configuring Ollama Models](#selecting-and-configuring-ollama-models)
    * [Using OpenAI](#switching-to-openai)
    * [OpenAI-Compatible Servers](#switching-to-openai-compatible-servers)
* [Tool Studio](#tool-studio)
    * [Built-in MCP Server](#built-in-mcp-server)
    * [Dynamic Tool Registration](#dynamic-tool-registration)
    * [JavaScript Runtime](#javascript-runtime)
    * [Low-code Tool Development Workflow](#low-code-tool-development-workflow)
    * [Pre-built Example Tools](#pre-built-example-tools)
    * [Using Tools in Agentic Chat](#using-tools-in-chat)
    * [Connecting External MCP Clients](#connect-external-mcp-clients)
* [MCP Playground](#mcp-server)
    * [Key Features](#key-features)
    * [Getting Started with MCP](#getting-started-with-mcp)
* [Vector Database](#vector-database)
    * [Supported Vector Databases](#support-for-major-vector-database-providers)
    * [Vector Database Playground Features](#key-features-1)
* [Agentic Chat](#agentic-chat)
    * [Two Integrated Paradigms](#two-integrated-paradigms)
        * [RAG: Chain-based Workflow](#1-rag-knowledge-via-chain-workflow)
        * [MCP: Agentic Reasoning](#2-mcp-actions-via-agentic-reasoning)
    * [Workflow Integration](#workflow-integration)
    * [Model Requirements for Agentic Reasoning](#️-requirement