<div align="center">
  <p><strong>CN <a href="./README.zh-CN.md">中文</a> | US English</strong></p>
  <h1>Ops Mind Agent</h1>
  <p><strong>A production-oriented AI agent application for intelligent operations workflows</strong></p>
  <p>Streaming Chat · AI Ops · RAG · Skills · Multi-User Session Management</p>
  <p>Product-facing UI: <strong>Xiaowei Assistant</strong></p>
</div>

## Overview

`Ops Mind Agent` is a production-oriented agent system built for intelligent operations scenarios rather than a thin chat wrapper around an LLM. It combines conversational interaction, alert analysis, document retrieval, public web search, session persistence, and multi-user access control into a single deployable engineering baseline.

The project is designed to look and behave like a real product: users can sign in, continue prior conversations, trigger an `AI Ops` workflow from a dedicated entry point, upload knowledge documents, and ask follow-up questions against both internal and public sources.

## Product Value

This project is aimed at teams that need more than a playground demo. It provides a practical baseline for building an AI-powered operations assistant with clear product shape and extensible engineering foundations.

It is especially useful when you need to combine:

- conversational assistance for day-to-day operations work
- structured alert interpretation and report generation
- internal knowledge retrieval with vector search
- public web search for time-sensitive questions
- user isolation, session continuity, and deployable runtime support

## Key Capabilities

| Capability | Description |
| --- | --- |
| Streaming Conversation | Supports standard chat and `SSE`-based streaming output for a more responsive user experience |
| AI Ops Workflow | `/api/ai_ops` streams analysis progress and operations reports instead of returning a single static response |
| Context-Aware Sessions | Supports recent sessions, full message history retrieval, and contextual follow-up interactions |
| Knowledge-Augmented QA | Uploads Markdown/TXT files, chunks them, indexes them into Milvus, and uses retrieval for grounded answers |
| Skills-Based Extension | Integrates official Spring AI `Skills` with built-in `web-search` capability for public internet search |
| Authentication & Isolation | Supports registration, login, captcha, JWT authentication, and user-level session isolation |
| Persistent Data Layer | Persists users, sessions, and messages in MySQL, with Redis for high-frequency state and cache support |
| Deployment Flexibility | Supports both local development mode and server-side containerized deployment |

## Production-Oriented Design

Many LLM demos stop at a single chat box. This project goes further in several important ways:

- It has a user system instead of anonymous one-off usage
- It preserves session continuity rather than treating every question as isolated
- It provides a dedicated `AI Ops` path for alert analysis and operations reporting
- It combines RAG and Skills instead of depending on model memory alone
- It supports both engineering experimentation and actual deployment workflows

This makes the project suitable not only for demos, but also as a serious starting point for an internal operations assistant.

## Product Surface

### Xiaowei Assistant

The main product-facing interface is **Xiaowei Assistant**, designed for natural language interaction. It is suitable for routine operations Q&A, contextual troubleshooting, knowledge lookup, and continued follow-up conversations.

### AI Ops Entry

The floating `AI Ops` button provides a dedicated workflow-oriented entry point for alert analysis. Instead of acting like generic chat, it focuses on structured operational reasoning, report generation, and flowing the result back into the same session context.

### Knowledge and Search Layer

The project combines two complementary augmentation paths:

- Internal knowledge: RAG retrieval from `aiops-docs` and uploaded documents
- External knowledge: public internet search powered by the `web-search` Skill

This gives the assistant both enterprise memory and external freshness.

## Product Features

### Conversation Assistant

- normal chat and streaming chat modes
- contextual follow-up questions in the same session
- recent conversations list and full message retrieval
- natural continuation after `AI Ops` execution

### AI Ops Analysis

- dedicated entry separate from general chat
- streaming operational reasoning output
- alert-oriented analysis flow
- final report generation and session integration

### Knowledge-Augmented Experience

- upload `txt` and `md` files
- automatic file persistence and overwrite by original filename
- automatic vector indexing after upload
- Milvus-backed semantic retrieval for grounded responses

### Public Search Capability

- built-in `web-search` Skill
- designed for latest, current, recent, and public information lookups
- supports time-sensitive search handling and