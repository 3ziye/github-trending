<div align="center">
  <picture>
    <source srcset="figures/MiniMaxLogo-Dark.png" media="(prefers-color-scheme: dark)">
      <img src="figures/MiniMaxLogo-Light.png" width="60%" alt="MiniMax">
    </source>
  </picture>
</div>
<hr>

<div align="center" style="line-height: 1.4; font-size:16px; margin-top: 30px;">
  Join Our 
  <a href="https://github.com/MiniMax-AI/MiniMax-AI.github.io/blob/main/images/wechat-qrcode.jpeg" target="_blank" style="font-size:17px; margin: 2px;">
    💬 WeChat
  </a> | 
  <a href="https://discord.com/invite/hvvt8hAye6" target="_blank" style="font-size:17px; margin: 2px;">
    🧩 Discord
  </a> 
  community.
</div>
<div align="center" style="line-height: 1.2; font-size:16px;">
  <a href="https://agent.minimax.io/" target="_blank" style="display: inline-block; margin: 4px;">
    MiniMax Agent
  </a> | 
  <a href="https://platform.minimax.io/docs/guides/text-generation" target="_blank" style="display: inline-block; margin: 4px;">
    ⚡️ API (Now Free for a limited time!)
  </a> | 
  <a href="https://github.com/MiniMax-AI/MiniMax-MCP" style="display: inline-block; margin: 4px;">
    MCP
  </a> |
  <a href="https://www.minimax.io" target="_blank" style="display: inline-block; margin: 4px;">
    MiniMax Website
  </a> 
</div>
<div align="center" style="lline-height: 1.2; font-size:16px; margin-bottom: 30px;">
  <a href="https://huggingface.co/MiniMaxAI" target="_blank" style="margin: 2px;">
    🤗 Hugging Face 
  </a> | 
  <a href="https://github.com/MiniMax-AI/MiniMax-M2" target="_blank" style="margin: 2px;">
    🐙 GitHub
  </a> | 
  <a href="https://www.modelscope.cn/organization/MiniMax" target="_blank" style="margin: 2px;">
    🤖️ ModelScope
  </a> | 
  <a href="https://github.com/MiniMax-AI/MiniMax-M2/blob/main/LICENSE" style="margin: 2px;">
    📄 License: MIT
  </a>
</div>

# Meet MiniMax-M2

Today, we release and open source MiniMax-M2, a **Mini** model built for **Max** coding & agentic workflows.

**MiniMax-M2** redefines efficiency for agents. It's a compact, fast, and cost-effective MoE model (230 billion total parameters with 10 billion active parameters) built for elite performance in coding and agentic tasks, all while maintaining powerful general intelligence. With just 10 billion activated parameters, MiniMax-M2 provides the sophisticated, end-to-end tool use performance expected from today's leading models, but in a streamlined form factor that makes deployment and scaling easier than ever.

<p align="center">
  <img width="100%" src="figures/Bench.png">
</p>

---

## Highlights

**Superior Intelligence**. According to benchmarks from Artificial Analysis, MiniMax-M2 demonstrates highly competitive general intelligence across mathematics, science, instruction following, coding, and agentic tool use. **Its composite score ranks #1 among open-source models globally**.

**Advanced Coding**. Engineered for end-to-end developer workflows, MiniMax-M2 excels at multi-file edits, coding-run-fix loops, and test-validated repairs. Strong performance on Terminal-Bench and (Multi-)SWE-Bench–style tasks demonstrates practical effectiveness in terminals, IDEs, and CI across languages.

**Agent Performance**. MiniMax-M2 plans and executes complex, long-horizon toolchains across shell, browser, retrieval, and code runners. In BrowseComp-style evaluations, it consistently locates hard-to-surface sources, maintains evidence traceable, and gracefully recovers from flaky steps.

**Efficient Design**. With 10 billion activated parameters (230 billion in total), MiniMax-M2 delivers lower latency, lower cost, and higher throughput for interactive agents and batched sampling—perfectly aligned with the shift toward highly deployable models that still shine on coding and agentic tasks.

---

## Coding & Agentic Benchmarks

These comprehensive evaluations test real-world end-to-end coding and agentic tool use: editing real repos, executing commands, browsing the web, and delivering functional solutions. Performance on this suite correlates with day-to-day developer experience in terminals, IDEs, and CI.

| **Benchmark** | **MiniMax-M2** | **Claude Sonnet 4** | **Claude Sonnet 4.5** | **Gemini 2.5 Pro** | **GPT-5 (thinking)** | **GLM-4.6** | **Kimi K2 0905** | **DeepSeek-V3.2** |
|-----------|------------|-----------------|-------------------|-----------------|------------------|---------|---------------|----------------|
| **SWE-bench Verified** | 69.4 | 72.7 * | 77.2 * | 63.8 * | 74.9 * | 68 * | 69.2 * | 67.8 * |
| **Multi-SWE-Bench** | 36.2 | 35.7 * | 44.3 | / | / | 30 | 33.5 | 30.6 |
| **SWE-bench Multilingual** | 56.5 | 56.9 * | 68 | / | / | 53.8 | 55.9 * | 57.9 * |
| **Terminal-Bench** | 46.3 | 36.4 * | 50 * | 25.3 * | 43.8 * | 40.5 * | 44.5 * | 37.7 * |
| **ArtifactsBench** | 66.8 | 57.3* | 61.5 | 57.7* | 73* | 59.8 | 54.2 | 55.8 |
| **BrowseComp** | 44 | 12.2 | 19.6 | 9.9 | 54.9* | 45.1* | 14.1 | 40.1* |
| **BrowseComp-zh** | 48.5 | 29.1 | 40.8 | 32.2 | 65 | 49.5 | 28.8 | 47.9* |
| **GAIA (