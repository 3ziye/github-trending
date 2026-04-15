<p align="center">
  <img src="./docs/images/memind-banner.png" alt="Memind banner">
</p>

<p align="center">
  <strong>Memory that thinks. Context that evolves.</strong>
</p>

<p align="center">
  <a href="#highlights">Highlights</a> ·
  <a href="#overview">Overview</a> ·
  <a href="#quick-start">Quick Start</a> ·
  <a href="#examples">Examples</a> ·
  <a href="#benchmark">Benchmark</a>
</p>

<p align="center">
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-orange" alt="License"></a>
  <a href="./README.md"><img src="https://img.shields.io/badge/English-Click-yellow" alt="English"></a>
  <a href="./README_zh.md"><img src="https://img.shields.io/badge/简体中文-点击查看-orange" alt="简体中文"></a>
  <a href="https://github.com/openmemind/memind"><img src="https://img.shields.io/github/stars/openmemind/memind?style=social" alt="GitHub Stars"></a>
</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/memind-0.1.0-0A7AFF" alt="memind 0.1.0"></a>
  <a href="#"><img src="https://img.shields.io/badge/Java-21-blue" alt="Java 21"></a>
  <a href="#"><img src="https://img.shields.io/badge/Spring%20Boot-4.0-brightgreen" alt="Spring Boot 4.0"></a>
  <a href="#"><img src="https://img.shields.io/badge/Spring%20AI-2.0-green" alt="Spring AI 2.0"></a>
</p>

---

<a id="highlights"></a>

## 🏆 Highlights

**Memind** achieves **state-of-the-art results across all three benchmarks**: LoCoMo, LongMemEval, and PersonaMem.

- ☕ **The first Java-native SOTA memory and context engine for AI agents:** built natively in Java, memind brings state-of-the-art long-memory performance into the Java ecosystem.
- 🚀 **Highest reported results across all three benchmarks:** achieved **86.88%** on **LoCoMo**, **84.20%** on **LongMemEval**, and **67.91%** on **PersonaMem** under aligned **MemOS / EverMemOS-style** evaluation.
- 📈 **Stronger than the strongest published baselines:** surpassed **EverMemOS** on **LoCoMo** and **LongMemEval**, and exceeded **MemOS** on **PersonaMem**.
- 🌳 **Insight Tree turns memory into structured understanding:** instead of flat fact storage, memind organizes memory into hierarchical knowledge that evolves over time. See [Insight Tree](#insight-tree).
- 🔬 **Full benchmark details:** see the [Benchmark](#benchmark) section for complete tables, category-level comparisons, context tokens, and evaluation protocol.

## Overview

### What is Memind?

Memind is a hierarchical cognitive memory and context engine for AI agents, built natively in Java.

Instead of treating memory as a flat collection of isolated facts, Memind continuously extracts, organizes, and evolves knowledge from conversations into a structured **Insight Tree**.

It tackles two core problems of agent memory: **flat, unstructured storage** (memories remain disconnected facts with no higher-level organization) and **no knowledge evolution** (memories accumulate, but never consolidate into deeper understanding).

The result is a long-term memory and context layer that helps agents retain context, build structured understanding over time, and recall knowledge at multiple levels of abstraction.

### Core Design

#### Insight Tree

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

#### Two-Scope Memory

memind maintains separate memory scopes for compr