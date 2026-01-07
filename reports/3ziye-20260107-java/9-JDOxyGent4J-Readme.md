[English](./README.md) | [中文](./README_zh.md)

<p align="center">
  <a href="https://github.com/jd-opensource/JDOxyGent4J/pulls">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome">
  </a>
  <a href="https://github.com/jd-opensource/JDOxyGent4J/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="license"/>
  </a>
  <a href="https://search.maven.org/search?q=g:com.jd.oxygent%20AND%20a:JDOxyGent4J">
    <img src="https://img.shields.io/badge/maven_central-JDOxyGentJ1.0.0-blue" alt="maven"/>
  </a>
  <a href="https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html">
    <img src="https://img.shields.io/badge/Java-17-orange?logo=openjdk" alt="jdk17"/>
  </a>
</p>

![Banner](docs/images/images_banner.jpg)

<h2 align="center">An advanced Java framework that enables developers to quickly build production-grade intelligent systems.</h2>

<div align="center">

**🌐 Official Website:** [OxyGent](http://oxygent.jd.com) | **📚 Open Source:** [Python Version](https://github.com/jd-opensource/OxyGent) | [Java Version](https://github.com/jd-opensource/JDOxyGent4J)

</div>

## 🔍 1. Project Overview

OxyGent is an open-source multi-agent framework that unifies Agent/LLM/Tool as composable Oxy components, providing transparent end-to-end pipelines with orchestration capabilities, supporting continuous evolution and unlimited expansion in production environments.

JDOxyGent4J shares the same philosophy as the Python version and is deeply optimized for the Java ecosystem: native type safety and compile-time validation, seamless Spring Boot integration, enterprise-grade concurrency and stability, and developer-friendly APIs for Java developers.

JDOxyGent4J has been validated and applied in multiple real-world business scenarios, proving its stability and scalability in production environments.

---

## ⚡ 2. Core Features

⚙️ **Deep Java Ecosystem Integration**
- Seamlessly integrates with Spring Boot and Java EE standards, providing a type-safe intelligent agent development experience. Supports rapid definition of agent behavior through annotations and configuration files, leveraging Java ecosystem's mature toolchain and dependency injection mechanisms to accelerate enterprise AI application development.

🛡️ **Enterprise-Grade Reliability Assurance**
- Inherits Java platform's security model and exception handling mechanisms, ensuring stable operation of agent systems in production environments. Provides complete access control, audit logs, and observability support, meeting enterprise application security and compliance requirements.

⚡ **High-Performance Concurrent Processing**
- Based on Java's concurrent programming model, enabling efficient asynchronous execution of agent tasks. Supports large-scale concurrent agent execution, with non-blocking IO for inter-agent communication, showing significant performance improvements over the Python version in concurrency tests.

🔄 **Flexible Configuration and Extensible Storage**
- Provides unified infrastructure abstraction layer and flexible configuration system, supporting user-defined extensions for various storage implementations (databases, caches, vector libraries, etc.). Through configuration-driven architecture design, easily adapts to local development, cloud deployment, and enterprise runtime environments, achieving hot-pluggable storage layer and seamless migration.


---

## 🗂️ 3. Project Structure

```
JDOxyGent4J/
├── oxygent-core/                  # Core: Agent/LLM/Tool/MAS with examples
│   └── src/main/java/com/jd/oxygent/core/
│       ├── Config.java            # Global configuration
│       ├── Mas.java               # Multi-Agent System (MAS) core
│       ├── MasFactoryBean.java    # Spring integration and space management
│       ├── oxygent/oxy/           # Component implementations
│       │   ├── agents/            # Chat/ReAct/Workflow/RAG/SSE/Parallel etc.
│       │   ├── llms/              # HttpLlm, OpenAiLlm etc.
│       │   ├── function_tools/    # FunctionHub, FunctionTool
│       │   └── mcp/               # StdioMCPClient, SSEMCPClient
│       ├── oxygent/schemas/       # Request/Response/Memory/Context/Exception/Observation
│       ├── oxygent/infra/         # Database, RAG, multimodal abstraction
│       ├── oxygent/samples/       # Sample code and servers
│       ├── tools/                 # Preset tools and example tools
│       └── utils/                 # Common utility classes
├── oxygent-infra/                # Infrastructure implementation
├── oxygent-starter-core/          # Spring Boot Starter (auto-configuration)
├── oxygent-studio/                # Web examples and demo UI
├── docs/                          # Documentation (Chinese in docs/docs_zh)
└── cache_dir/                     # Local cache directory
```

## 🚀 4. Quick Start

> 💡 **Quick Start Recommendations**:
> - Read [docs/](docs/docs_zh/README.md) for compl