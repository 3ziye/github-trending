# Spring AI Agent Utils

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Maven Central](https://img.shields.io/maven-central/v/org.springaicommunity/spring-ai-agent-utils.svg?label=Maven%20Central)](https://central.sonatype.com/artifact/org.springaicommunity/spring-ai-agent-utils)
[![Java Version](https://img.shields.io/badge/Java-17%2B-orange)](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html)


A [Spring AI](https://docs.spring.io/spring-ai/reference/2.0-SNAPSHOT/index.html) library that brings [Claude Code](https://code.claude.com/docs/en/settings#tools-available-to-claude)-inspired tools and agent skills to your AI applications.

## Overview

<img style="display: block; margin: auto;" align="left" src="./spring-ai-agent-utils/docs/spring-ai-agent-utils-logo.png" width="250" />

Spring AI Agent Utils reimplements core Claude Code capabilities as Spring AI tools, enabling sophisticated agentic workflows with file operations, shell execution, web access, task management, and extensible agent skills.

This project demonstrates how to reverse-engineer and reimplement Claude Code's powerful features within the Spring AI ecosystem, making them available to Java developers building AI agents.

## Project Structure

```
spring-ai-agent-utils/
├── spring-ai-agent-utils/          # Agent Utils Core library
│   ├── src/                        # Agent Tool Utils implementation
│   ├── docs/                       # Agent Tool documentation
│   └── README.md                   # Detailed library documentation
│
└── examples/
    ├── code-agent-demo/            # Full-featured AI coding assistant
    ├── ask-user-question-demo/     # Interactive question-answer demo
    ├── skills-demo/                # Focused skills system demo
    ├── subagent-demo/              # Markdown-defined local sub-agents
    └── subagent-a2a-demo/          # A2A protocol remote sub-agents
```

## Agentic Utils

These are the agent tools needed to implement any agentic behavior

#### Core Tools

- **[AgentEnvironment](spring-ai-agent-utils/docs/AgentEnvironment.md)** - Dynamic agent context utility that provides runtime environment information and git repository status to system prompts
- **[FileSystemTools](spring-ai-agent-utils/docs/FileSystemTools.md)** - Read, write, and edit files with precise control
- **[ShellTools](spring-ai-agent-utils/docs/ShellTools.md)** - Execute shell commands with timeout control, background process management, and regex output filtering
- **[GrepTool](spring-ai-agent-utils/docs/GrepTool.md)** - Pure Java grep implementation for code search with regex, glob filtering, and multiple output modes
- **[GlobTool](spring-ai-agent-utils/docs/GlobTool.md)** - Fast file pattern matching tool for finding files by name patterns with glob syntax
- **[SmartWebFetchTool](spring-ai-agent-utils/docs/SmartWebFetchTool.md)** - AI-powered web content summarization with caching
- **[BraveWebSearchTool](spring-ai-agent-utils/docs/BraveWebSearchTool.md)** - Web search with domain filtering

#### User feedback

- **[AskUserQuestionTool](spring-ai-agent-utils/docs/AskUserQuestionTool.md)** - Ask users clarifying questions with multiple-choice options during agent execution

#### Agent Skills

- **[SkillsTool](spring-ai-agent-utils/docs/SkillsTool.md)** - Extend AI agent capabilities with reusable, composable knowledge modules defined in Markdown with YAML front-matter

#### Task orchestration & multi-agent

- **[TodoWriteTool](spring-ai-agent-utils/docs/TodoWriteTool.md)** - Structured task management with state tracking
- **[TaskTools](spring-ai-agent-utils/docs/TaskTools.md)** - Extensible sub-agent system for delegating complex tasks to specialized agents with multi-model routing and pluggable backends

While these tools can be used standalone, truly agentic behavior emerges when they are combined. SkillsTool naturally pairs with FileSystemTools and ShellTools to execute domain-specific workflows. BraveWebSearchTool and SmartWebFetchTool provide your AI application with access to real-world information. TaskTools orchestrates complex operations by delegating to specialized sub-agents, each equipped with a tailored subset of these tools.

### Detailed documentation

- **[Agent Utils Library Documentation](spring-ai-agent-utils/README.md)** - Complete API reference, tool capabilities, and skills development guide
- **[Example Applications](#examples)** - Working demos showcasing different use cases


## Quick Start

**1. Add dependency:**

```xml
<dependency>
    <groupId>org.springaicommunity</groupId>
    <artifactId>spring-ai-agent-utils</artifactId>
    <version>0.4.2</version>
</dependency>
```

_Check the latest version:_ [![](https://img.shields.io/maven-central/v/org.springaicommunity/spring-ai-agent-utils.svg?label=Maven%20Central)](https://central.sonatype.com/artifact/org.springaicommunity/spring-ai-agent-utils)

> **Note:*