<div align="center">
  <h1>📄 Production-Grade SLM-Powered OCR Course 📄</h1>
  <h3>Build a self-scaling, event-driven OCR pipeline on Kubernetes (AKS / GKE) with Qwen 3.5 + the GLM-OCR SDK</h3>
</div>

</br>

<p align="center">
    <img src="images/arch_overview.jpeg" alt="Architecture" width="700">
</p>

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Course Overview](#course-overview)
- [Who is this course for?](#who-is-this-course-for)
- [Course Breakdown: Week by Week](#course-breakdown-week-by-week)
- [Getting Started](#getting-started)
- [✨ Beyond Traditional OCR: The SLM Advantage](#-beyond-traditional-ocr-the-slm-advantage)
- [🧠 Pipeline Architecture: Deep Dive into Throughput \& Scaling](#-pipeline-architecture-deep-dive-into-throughput--scaling)
- [🔄 The Exact Document Workflow](#-the-exact-document-workflow)
- [🧩 Robustness: Why a Pre-layout Encoder Improves Fidelity](#-robustness-why-a-pre-layout-encoder-improves-fidelity)
- [📑 Technical Report: Document Handoff](#-technical-report-document-handoff)
- [🏛️ Formal Architecture Assessment: Production Robustness](#️-formal-architecture-assessment-production-robustness)
- [📈 Scaling Philosophy: Real-Time Workloads (Metric-Driven)](#-scaling-philosophy-real-time-workloads-metric-driven)
- [The tech stack](#the-tech-stack)
- [Contributors](#contributors)
- [License](#license)

## Course Overview

Most OCR tutorials stop at "call an API and get some text back." This isn't that.

Instead, we're building a **production-grade, self-scaling Visual Document Understanding pipeline**, deployed for real on Kubernetes (AKS or GKE), that goes far beyond flat text extraction: it reasons about charts, tables, and layout the way a human reader would — powered by a Small Language Model (**Qwen 3.5**) instead of a bloated frontier model.

By the end of this course, you'll have your own event-driven OCR system capable of:

* 🧠 Understanding documents, not just transcribing them — charts, tables, handwriting, and contextual reasoning via **Qwen 3.5 (4B)**
* ⚡ Serving generative OCR at **1.86 pages/second** with vLLM's continuous batching, PagedAttention, and Multi-Token Prediction (MTP)
* 🦀 Ingesting files through a high-concurrency **Rust (Axum) gateway**, decoupled from GPU inference via Redis
* 🔄 Running a **zero-copy, `/dev/shm`-based** document handoff between the layout encoder and the inference engine
* ☸️ Auto-scaling T4 (layout) and A100 (inference) node pools independently with **KEDA**, from zero to bursting load
* 🔒 Locking the whole pipeline behind an **Internal Load Balancer + Enterprise API Gateway** (Azure APIM / GCP API Gateway), with zero public exposure
* 🤖 Wrapping the pipeline as an **MCP server** for native use by AI agents, including Claude Code

Excited? Let's get started!

---

<table style="border-collapse: collapse; border: none;">
  <tr style="border: none;">
    <td width="20%" style="border: none;">
      <a href="https://theneuralmaze.substack.com/" aria-label="The Neural Maze">
        <img src="https://avatars.githubusercontent.com/u/151655127?s=400&u=2fff53e8c195ac155e5c8ee65c6ba683a72e655f&v=4" alt="The Neural Maze Logo" width="150"/>
      </a>
    </td>
    <td width="80%" style="border: none;">
      <div>
        <h2>📬 Stay Updated</h2>
        <p><b><a href="https://theneuralmaze.substack.com/">Join The Neural Maze</a></b> and learn to build AI Systems that actually work, from principles to production. Every Wednesday, directly to your inbox. Don't miss out!</p>
      </div>
    </td>
  </tr>
</table>

<p align="center">
  <a href="https://theneuralmaze.substack.com/">
    <img src="https://img.shields.io/static/v1?label&logo=substack&message=Subscribe%20Now&style=for-the-badge&color=black&scale=2" alt="Subscribe Now" height="40">
  </a>
</p>

---

## Who is this course for?

This course is for ML/AI Engineers and Platform Engineers who already know how to call an OCR API and want to know **what it takes to run one in production**: GPU node pools, autoscaling economics, network security, and the systems-design tradeoffs behind serving a generative model at throughput.

## Course Breakdown: Week by Week

We run this as a 6-week hands-on engineering cohort. The entire repository is open-source from day one — every week combines a deep-dive systems article with a step-by-step codebase walkthrough.

### 📅 Weekly Cadence
*   📘 **Weekly Production Article (Wednesday)**: Architectural deep dives, systems design math, and codebase explanations.
*   🎙️ **Live Office Hours (Friday)**: Live coding, cluster provisioning, load-testing, scaling demonstration, and Q&A.

| Week | Focus | Hands-on |
| :--- | :--- | :--- |
| ⛵ **1. Kubernetes for AI Systems** | Pods, Services, Node Pools, resource scheduling | Cluster setup on AKS/GKE, T4 & A100 node pools, GPU drivers/operators with proper security profiles and taints |
| 🧠 **2. SOTA OCR Approaches & VDU** | Single-stage end-to-end models vs. our two-stage layout-first pipeline |