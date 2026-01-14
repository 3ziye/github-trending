# Assistant Agent

[English](README.md) | [中文](README_zh.md)

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Java](https://img.shields.io/badge/Java-17%2B-orange.svg)](https://openjdk.org/)
[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.4-green.svg)](https://spring.io/projects/spring-boot)
[![Spring AI](https://img.shields.io/badge/Spring%20AI-1.1.0-blueviolet.svg)](https://spring.io/projects/spring-ai)
[![GraalVM](https://img.shields.io/badge/GraalVM-Polyglot-red.svg)](https://www.graalvm.org/)

## ✨ Technical Features

- 🚀 **Code-as-Action**: Agent generates and executes code to complete tasks, rather than just calling predefined tools
- 🔒 **Secure Sandbox**: AI-generated code runs safely in GraalVM polyglot sandbox with resource isolation
- 📊 **Multi-dimensional Evaluation**: Multi-layer intent recognition through Evaluation Graph, precisely guiding Agent behavior
- 🔄 **Dynamic Prompt Builder**: Dynamically inject context (experiences, knowledge, etc.) into prompts based on scenarios and evaluation results
- 🧠 **Experience Learning**: Automatically accumulates successful experiences to continuously improve performance on subsequent tasks
- ⚡ **Fast Response**: For familiar scenarios, skip LLM reasoning process and respond quickly based on experience

## 📖 Introduction

**Assistant Agent** is an enterprise-grade intelligent assistant framework built on [Spring AI Alibaba](https://github.com/alibaba/spring-ai-alibaba), adopting the Code-as-Action paradigm to orchestrate tools and complete tasks by generating and executing code. It's an intelligent assistant solution that **understands, acts, and learns**.

* <a href="https://java2ai.com/agents/assistantagent/quick-start" target="_blank">Documentation</a>
* <a href="https://java2ai.com/docs/overview" target="_blank">Spring AI Alibaba</a>

### What Can Assistant Agent Do?

Assistant Agent is a fully-featured intelligent assistant with the following core capabilities:

- 🔍 **Intelligent Q&A**: Supports unified retrieval architecture across multiple data sources (extensible via SPI for knowledge base, Web, etc.), providing accurate, traceable answers
- 🛠️ **Tool Invocation**: Supports MCP, HTTP API (OpenAPI) and other protocols, flexibly access massive tools, combine multiple tools to implement complex business workflows
- ⏰ **Proactive Service**: Supports scheduled tasks, delayed execution, event callbacks, letting the assistant proactively serve you
- 📬 **Multi-channel Delivery**: Built-in IDE reply, extensible to DingTalk, Feishu, WeCom, Webhook and other channels via SPI

### Why Choose Assistant Agent?

| Value | Description |
|-------|-------------|
| **Cost Reduction** | 24/7 intelligent customer service, significantly reducing manual support costs |
| **Quick Integration** | Business platforms can integrate with simple configuration, no extensive development required |
| **Flexible Customization** | Configure knowledge base, integrate enterprise tools, build your exclusive business assistant |
| **Continuous Optimization** | Automatically learns and accumulates experience, the assistant gets smarter with use |

### Use Cases

- **Intelligent Customer Service**: Connect to enterprise knowledge base, intelligently answer user inquiries
- **Operations Assistant**: Connect to monitoring and ticketing systems, automatically handle alerts, query status, execute operations
- **Business Assistant**: Connect to CRM, ERP and other business systems, assist employees in daily work


> 💡 The above are just typical scenario examples. By configuring knowledge base and integrating tools, Assistant Agent can adapt to more business scenarios. Feel free to explore.

![QA_comparison_en.png](images/QA_comparison_en.png)
![Tool_comparison_en.png](images/Tool_comparison_en.png)


### Overall Working Principle

Below is an end-to-end flow example of how Assistant Agent processes a complete request:

![workflow_en.png](images/workflow_en.png)

### Project Structure

```
AssistantAgent/
├── assistant-agent-common          # Common tools, enums, constants
├── assistant-agent-core            # Core engine: GraalVM executor, tool registry
├── assistant-agent-extensions      # Extension modules:
│   ├── dynamic/               #   - Dynamic tools (MCP, HTTP API)
│   ├── experience/            #   - Experience management and FastIntent configuration
│   ├── learning/              #   - Learning extraction and storage
│   ├── search/                #   - Unified search capability
│   ├── reply/                 #   - Multi-channel reply
│   ├── trigger/               #   - Trigger mechanism
│   └── evaluation/            #   - Evaluation integration
├── assistant-agent-prompt-builder  # Prompt dynamic assembly
├── assistant-agent-evaluation      # Evaluation engine
├── assistant-agent-autoconfigure   # Spring Boot auto-configuration
└── assistant-agent-start           # Startup module
```

## 🚀 Quick Start

### Prerequisites

- Java 1