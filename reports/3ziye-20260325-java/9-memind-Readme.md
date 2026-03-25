<p align="center">
  <h1 align="center">Memind Memory</h1>
</p>

<p align="center">
  <strong>Self-evolving cognitive memory for AI agents — not just storage, but understanding.</strong>
</p>

<p align="center">
  <a href="./README.md"><img src="https://img.shields.io/badge/English-Click-yellow" alt="English"></a>
  <a href="./README_zh.md"><img src="https://img.shields.io/badge/简体中文-点击查看-orange" alt="简体中文"></a>
  <a href="https://github.com/openmemind/memind"><img src="https://img.shields.io/github/stars/openmemind-ai/memind?style=social" alt="GitHub Stars"></a>
</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Java-21-blue" alt="Java 21"></a>
  <a href="#"><img src="https://img.shields.io/badge/Spring%20Boot-4.0-brightgreen" alt="Spring Boot 4.0"></a>
  <a href="#"><img src="https://img.shields.io/badge/Spring%20AI-2.0-green" alt="Spring AI 2.0"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-orange" alt="License"></a>
  <a href="#"><img src="https://img.shields.io/badge/Maven%20Central-coming%20soon-lightgrey" alt="Maven Central"></a>
</p>

---

memind is a **hierarchical cognitive memory system** for AI agents, built natively in Java. It goes beyond simple key-value memory — memind automatically extracts, organizes, and evolves knowledge from conversations into a structured **Insight Tree**, enabling agents to truly understand and remember.

It tackles the core problems of agent memory: **flat, unstructured storage** (memories are isolated facts with no relationships) and **no knowledge evolution** (memories never grow or consolidate).

---

## Why memind?

| Traditional Memory Systems | memind |
|---------------------------|--------|
| 🗄️ Flat key-value storage | 🌳 Hierarchical Insight Tree (Leaf → Branch → Root) |
| 📝 Store raw facts only | 🧠 Self-evolving cognition — items are analyzed into multi-level insights |
| 🔍 Single-level retrieval | 🎯 Multi-granularity retrieval (detail → summary → profile) |
| 💰 Requires expensive models | 🏆 SOTA performance with gpt-4o-mini |
| 🔧 Manual memory management | ⚡ Fully automatic extraction pipeline |

---

## Highlights

### 🌳 Insight Tree — Hierarchical Knowledge, Not Flat Storage

The Insight Tree is memind's core innovation. Unlike traditional memory systems that store isolated facts, memind **progressively distills knowledge** through three tiers — each tier sees patterns the previous one cannot:

| Tier | Input | What it produces |
|------|-------|-----------------|
| 🍃 **Leaf** | Grouped memory items | Insights within a single semantic group |
| 🌿 **Branch** | Multiple leaves | Cross-group patterns within one dimension |
| 🌳 **Root** | Multiple branches | Cross-dimensional insights invisible at lower levels |

**Example — understanding a user named Li Wei through conversations:**

> 🍃 **Leaf** (from career_background group):
> "Li Wei has 8 years of backend experience — 3 years at Alibaba, then led an 8-person team at a fintech company, designing a core trading system with Java 17 + Spring Cloud + Kafka."
>
> 🌿 **Branch** (integrating career + education + certifications):
> "Li Wei is a senior backend architect with deep distributed systems expertise, combining Zhejiang University CS training, large-scale Alibaba experience, and hands-on fintech system design — a well-rounded technical profile with both depth and breadth."
>
> 🌳 **Root** (cross-dimensional — identity × preferences × behavior):
> "Li Wei's preference for functional programming and high code quality (80% test coverage), combined with conservative tech adoption (requires 2+ years production validation), reveals a personality oriented toward long-term code maintainability over rapid innovation — suggesting recommendations should emphasize stability and proven patterns over cutting-edge tools."

Each tier reveals something the previous one couldn't see. Leaves know facts. Branches see patterns. Roots understand the person.

### 🏆 SOTA with Lightweight Model

Achieved **86.88% overall** on the LoCoMo benchmark using only **gpt-4o-mini** — a lightweight, cost-effective model. This proves that intelligent memory architecture matters more than brute-force model power.

### ☕ Java-Native — First SOTA Memory for the Java Ecosystem

The first Java-based AI memory system to achieve SOTA-level performance. Built with **Spring Boot 4.0** and **Spring AI 2.0**, memind integrates naturally into Java/Kotlin enterprise stacks with a one-line Maven dependency.

---

## Architecture

memind processes conversations through a multi-stage pipeline, from raw dialogue to structured knowledge:

![Architecture](docs/images/mermaid-architecture.png)

### Two-Scope Memory

memind maintains separate memory scopes for comprehensive agent cognition:

| Scope | Categories | Purpose |
|-------|-----------|---------|
| **USER** | Profile, Behavior, Event | User identity, preferences, relationships, experiences |
| **AGENT** | Tool, Procedural | Tool usage pa