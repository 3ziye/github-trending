<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./images/logo-lockup-dark.svg?v=2">
  <img src="./images/logo-lockup.svg?v=2" alt="Zilan 知澜" width="380">
</picture>

**Where knowledge converges into waves — bring every document to life**

Minimalist aesthetics × Deep parsing × Autonomous reasoning — an intelligent knowledge hub

</div>

<p align="center">
    <a href="./LICENSE">
        <img src="https://img.shields.io/badge/License-MIT-ffffff?labelColor=d4eaf7&color=2e6cc4" alt="License">
    </a>
    <a href="./CHANGELOG.md">
        <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-2e6cc4?labelColor=d4eaf7">
    </a>
    <a>
        <img alt="Deployment" src="https://img.shields.io/badge/Deployment-Private·Offline-333333?labelColor=f2f2f2">
    </a>
    <a>
        <img alt="Design Language" src="https://img.shields.io/badge/Design-Monochrome Minimal-333333?labelColor=f2f2f2">
    </a>
</p>

<p align="center">
| <b>English</b> | <a href="./README_CN.md"><b>简体中文</b></a> |
</p>

<p align="center">
  <h4 align="center">

  [Overview](#-overview) • [Highlights](#-highlights) • [Architecture](#-architecture) • [Feature Overview](#-feature-overview) • [Getting Started](#-getting-started) • [Docs](#-docs) • [Developer Guide](#-developer-guide)

  </h4>
</p>

# 💡 Zilan — Where Knowledge Converges: a Minimalist Knowledge Hub Unifying RAG, Agent Reasoning, and Auto-Wiki

## 📌 Overview

**Zilan (知澜)** is an LLM-powered knowledge management and intelligent Q&A platform with a minimalist product experience that unifies **RAG quick Q&A**, **ReAct agent reasoning**, and **auto-generated Wiki knowledge distillation**.

Zilan is a thorough re-imagination built on a battle-tested open-source knowledge framework, carrying product genes entirely its own:

- **🎨 A brand-new minimalist design language** — no clutter, no visual noise: a dark monochrome brand color (#333 family), large rounded corners, feather-light shadows, and pure solid backgrounds; one consistent visual system from the login page through chat streams to the settings center — quiet, restrained, and content-first
- **📄 A deep document parsing pipeline** — structured PDF table extraction, mathematical formula recognition, and dual-column layout awareness; **automatic routing** selects parsing engine intensity per document profile, low-scoring results are retried with heavier engines, and stubborn documents land in a human review queue
- **🕸️ GraphRAG-enhanced retrieval** — entity-relation storage on Neo4j; **community summaries + local subgraph retrieval** complement dense/sparse vector recall, widening coverage and explainability for complex multi-hop questions
- **🧠 Memory & knowledge distillation system** — a three-layer memory architecture: L1 working memory (current conversation), L2 short-term memory (vectorized summaries of recent conversations), L3 long-term memory (user profile + fact triples + to-dos); memories are extracted asynchronously after each session and injected into the system prompt scored by `semantic similarity × time decay × (1 + log(access count))`; long-term memory is further structured into **four semantic modules — Soul / User / Memory / Agent** (persona directives, user profile, memory stream, distilled skills), each with its own view on the **My Memory** page where users can view, edit, and delete everything the AI remembers — GDPR-compliant by design
- **🔐 An independent identity and protocol stack** — a fully self-owned namespace across branding, JWT audience (`aud=zilan`), webhook signature (`X-Zilan-Signature`), and embed SDK (`zilan-widget.js`) — zero upstream traces

On top of that, Zilan inherits engineering capabilities proven through large-scale production use: multi-source ingestion (Feishu / Notion / Yuque / RSS, and growing), 20+ LLM provider integrations, a dozen IM channels, website embed widgets, a 4-tier RBAC role matrix with workspace audit logs, AES-256-GCM credential encryption at rest, full-stack Langfuse observability plus a runtime task-queue governance dashboard, and a fully self-hostable modular architecture — LLMs, vector databases, and storage backends are all swappable, keeping data sovereignty entirely yours.

## ✨ Highlights

### 🎨 Minimalist Design Language · An Interface Built for Focus

| Principle | Details |
|-----------|---------|
| Dark monochrome brand | Brand color stays in the #333 family; interaction states shift luminance only — no flashy gradients, no saturated clashes |
| Large radii × light shadows | A global radius system (starting at 8/10/12px); cards and chat bubbles use feather-light or no shadows |
| Pure solid backgrounds | Pages return to solid colors (light #fafafa / dark #181818) — no textures, no decorative animations |
| Centered login | A single vertical focal point of brand mark + form; every login-irrelevant element removed |
| Symmetric chat bubbles | User-side dark, assistant-side light-gray symmetric rounded bubble