<div align="center">
  <img src="docs/images/Anima Logo.svg" alt="Anima logo" width="320" />
  <h1></h1>
  <p><strong>Make every hardware intelligent</strong></p>
  <p>An open-source Agent OS for hardware intelligence.</p>

  [English](./README.md) | [中文](./README.zh-CN.md)
  <br/><br/>

  [![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](./LICENSE)
  ![Python](https://img.shields.io/badge/Python-3.11--3.13-blue)
  ![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
  ![React](https://img.shields.io/badge/React-Dashboard-61DAFB?logo=react)
  ![LangGraph](https://img.shields.io/badge/LangGraph-Agent%20Brain-purple)
  ![MIoT](https://img.shields.io/badge/Xiaomi%20MIoT-Supported-orange)
</div>

<br/>

**Anima** is an open-source Agent OS for intelligent hardware. Its goal is not to build yet another device control panel, but to give home hardware perceptive, decision-making, learning, and extensible AI capabilities.

The name **Anima** comes from Latin and means "soul." It reflects the project's original idea: today's smart hardware already has sensors, connectivity, and actuation, but most devices still wait passively for commands. Anima connects these devices to a runnable intelligence center, so lights, air conditioners, humidifiers, air purifiers, speakers, and future devices can understand the environment, the user, and each other.

> Anima's vision: move every piece of hardware from a "connected device" to a collaborative intelligent agent.

<div align="center">
  <img src="docs/images/bedroom.svg" alt="Anima Dashboard Bedroom Design" width="100%" />
</div>

## What Is Anima

Anima can be understood as an intelligent hardware Agent Runtime running inside your local network:

- It discovers devices, maintains device state, and controls real hardware through adapters.
- It maintains long-term Memory and learns from explicit preferences and repeated behavior.
- It uses an LLM Brain to read the environment, user intent, historical memory, and skill knowledge, then plan actions.
- It packages domain knowledge for each device type as a Skill, so decisions are not just "on/off" but aligned with context, comfort, and safety boundaries.
- It provides a Dashboard, REST API, and CLI so you can observe, debug, control, and extend the whole system.

Anima currently supports Mi Home / MIoT devices. More hardware protocols will be added over time, and contributions from the open-source community are welcome.

---

## Why Anima

<div align="center">

![Zero config](https://img.shields.io/badge/Zero%20config-Auto%20discovery-0A7EA4?style=for-the-badge)
![AI skills](https://img.shields.io/badge/AI%20skills-Per%20device-1B5E20?style=for-the-badge)
![Memory system](https://img.shields.io/badge/Memory%20system-Learns%20your%20habits-B71C1C?style=for-the-badge)
![LLM brain](https://img.shields.io/badge/LLM%20Brain-OpenAI%20API%20compatible-4A148C?style=for-the-badge)
![Skill system](https://img.shields.io/badge/Skill%20system-Extensible-0D47A1?style=for-the-badge)
![Dashboard](https://img.shields.io/badge/Dashboard-Realtime%20visibility-6A1B9A?style=for-the-badge)

</div>

> [!TIP]
> Most smart-home systems ask, "What sensors do you need?" Anima asks, **"What do you have? I'll use it."** It discovers your devices automatically, loads domain knowledge for each device, and starts making intelligent decisions from day one.

<details>
<summary><strong>Q: Do I need to configure devices manually?</strong></summary>

**A:** No. Anima scans the local network through the corresponding adapter protocols. For Xiaomi / Mi Home devices, one QR login can automatically obtain device tokens without manually entering IP lists or extracting tokens.

</details>

<details>
<summary><strong>Q: Is it just a fancy switch controller?</strong></summary>

**A:** Far from it. Core device types have dedicated **Skills**: domain knowledge packages that include comfort models, occupancy awareness, cross-device coordination rules, and preference learning. Your humidifier understands seasonal adjustments and AC interaction; your lights can follow circadian lighting patterns.

</details>

<details>
<summary><strong>Q: How does it learn my preferences?</strong></summary>

**A:** Anima maintains a memory system with `preferences.md`, normalized learned profiles per device type, and extracted topic memories. The Brain incrementally extracts preferences from interaction history and evolves behavior over time.

</details>

<details>
<summary><strong>Q: Which LLM providers are supported?</strong></summary>

**A:** Any OpenAI-compatible API service, including OpenAI, DeepSeek, Doubao, Anthropic through a proxy, and local Ollama-compatible endpoints. Set `ANIMA_LLM_API_KEY`, and optionally `ANIMA_LLM_BASE_URL`.

</details>

---

## System Architecture

Anima's overall runtime flow is driven by user requests, device discovery, sensor updates, scheduled tasks, and device actions. After signals enter Anima Core