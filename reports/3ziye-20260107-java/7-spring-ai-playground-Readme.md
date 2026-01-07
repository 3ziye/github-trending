# Spring AI Playground

**Spring AI Playground is a self-hosted web UI platform for building low-code tools and dynamically exposing them via built-in MCP server for AI agents.**

Unlike most AI playgrounds that focus solely on prompt testing and chat visualization, it bridges the gap between **static AI conversations** and **real-world actions** by enabling you to create executable tools that AI agents can use.

It brings together **Large Language Models (LLMs)**, **Retrieval-Augmented Generation (RAG)**, and **low-code tool development** in a single environment. Tools created in the **Tool Studio** are dynamically evaluated and loaded at runtime, then automatically made available as **Model Context Protocol (MCP) tools**. This makes them instantly available to MCP-compatible clients without restarting or redeploying.

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

## Project Scope & Positioning

Spring AI Playground is intentionally built as a **tool-first reference environment** for exploring, validating, and operationalizing Spring AI features in a reproducible way.
> **Note:** This project is intentionally opinionated and scope-limited in its early stages.
> It focuses on providing a stable, reproducible reference runtime for tool execution and MCP integration,
> rather than evolving into a feature-complete agent platform at this time.

**Current focus (what this project prioritizes):**
- Providing a UI-driven reference runtime that demonstrates how Spring AI features compose in practice.
- Testing and validating tool execution flows and RAG integration.
- Promoting validated tools to **standalone, deployment-ready MCP servers**
  that can be independently run and reused by multiple AI clients and agent runtimes.

**Important note:** While this Playground is not a full-fledged agent orchestration product today, it is explicitly designed as the **foundation** for building interoperable tool-first agents in the future. Validated tools and MCP-hosted runtimes created here are intended to be reusable by different AI systems and agent frameworks.

## Contributing & Scope

**Please read before opening issues or submitting contributions.**

### Current scope (what we accept):
- ✅ Bug reports and reproducible issues
- ✅ Documentation improvements and usage examples

### Out of scope (for now):
- ❌ Broad feature requests that expand the project's scope (we will not accept general feature requests at this stage)
- ❌ Experimental model integrations not officially supported by Spring AI
- ❌ High-level agent orchestration layers (Agent builders are a planned future layer built on top of validated tools)

### Reporting issues

Before opening an issue, please check:
- Use the Bug Report template for reproducible failures.
- For documentation fixes or improvements, please submit a documentation PR.
- General feature requests are out of scope at this stage — please read the Project Scope above.

We triage issues regularly; issues outside the scope may be closed with guidance on where to best contribute.

If you believe you have a contribution that fits the current scope, submit a PR or a targeted issue. For larger proposals, please open a sho