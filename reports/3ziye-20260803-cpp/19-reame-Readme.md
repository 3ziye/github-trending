<p align="center">
  <img src="docs/figures/logo.svg" alt="Reame" width="300">
</p>

<p align="center">
  <a href="https://swellweb.github.io/reame/"><b>▶ Try the live demo</b></a> — a real Reame instance serving an LLM from a free Oracle ARM box, in your browser.
</p>

**A lean, fully-tested LLM inference server built on [llama.cpp](https://github.com/ggml-org/llama.cpp) — designed for the hardware you already have: shared vCPUs, free tiers, 2-core ARM boxes.**

> **Your local LLM re-reads the same text a thousand times.
> Reame reads it once.**

Reame is an inference server built for cheap CPU hardware first — not as a
fallback for missing GPUs. Its thesis is simple: **on a CPU, never compute the
same thing twice.**

![reame run demo: model catalog, one-line launch, streamed answer](docs/figures/demo.gif)

## What Reame is for

![The usual way sends every web page to a paid API — 2137 tokens, a bill that
grows with each user, pages leaving your machine. Stenografo strips the
navigation furniture down to 405 tokens in 211ms, Reame answers in 6.2s on four
free ARM cores, and all 13 critical facts still come out
right.](docs/figures/caso-uso.svg)

Reame is built for **narrow, repetitive AI workloads over your own data, on
hardware you already pay for** — the case where the answer lives in the
context you provide, not in the model's general knowledge. Reame's memory
makes request #100 cost a fraction of request #1, and the input pipeline
makes request #1 cheaper too.

**The headline number, measured on a €0 Oracle ARM box this week:** the same
question about the same customer page, answered by the same model —
**~6× faster time to first token** (40.5s → 6.2s on the box, 42.6s → 7.3s
through the public tunnel, so expect 5.9–6.5× depending on where you measure
from), and the score on a 20-question fact exam went from 19/20 to a perfect
**20/20 · 13/13 critical facts**. No new model, no
fine-tuning, no GPU. We just stopped handing the model 2137 tokens of prose
when 405 tokens of `label: value` say the same thing — and it turns out that
small models don't just read less that way, they read *better*.

Don't take our word for it — the page, the questions and the scorer are in
[`bench/`](bench/), and they run against any OpenAI-compatible server:

```bash
python3 bench/run_fact_exam.py --server http://127.0.0.1:8080 --model reame
```

The failures are published next to that number, including the two ideas we
built and killed the same day ([BENCHMARKS.md](docs/BENCHMARKS.md)).

| Use case | Why it fits | Suggested model |
|---|---|---|
| Document extraction & classification (RAG, invoices, tickets, scraping) | answers live in the context; prompts share prefixes → the disk cache pays | OLMoE 7B-A1B |
| Batch pipelines (tag 10k products overnight, meta descriptions, email triage) | repetitive by nature → Palimpsest drafts them; €0 per token, no rate limits | Qwen2.5 1.5B–3B |
| AI features inside a thin-margin SaaS | a €5 VPS instead of a metered API keeps unit economics alive | Qwen2.5 1.5B–7B |
| Privacy-bound work (legal, medical, public sector) | data never leaves your server — full sovereignty | OLMoE 7B-A1B |
| Private code autocomplete (Continue.dev + OpenAI-compatible API) | line-level completion is a narrow task; code never leaves the laptop | Qwen2.5-Coder 1.5B |
| Judgment on your data (SEO/content audits, review triage) — in batches | needs real reasoning: we measured smaller models inventing findings; the 9B audited a live page correctly in 73s on a laptop | Qwen3.5-9B |

**What Reame is NOT for**: a
general-purpose ChatGPT replacement (frontier reasoning and broad knowledge
need frontier parameter counts), agentic coding assistants, or creative
long-form writing at scale.

- 🗂️ **Persistent shared-prefix KV cache** — prompt prefixes are snapshotted to disk
  (zstd, checksummed, LRU-budgeted) and reused **across different prompts, restarts
  and processes**. A system prompt is paid for once, by the first user.
- 📜 **Palimpsest: the server remembers what it generated** — every completed
  generation feeds an on-disk n-gram archive; future requests draft from it
  at zero cost. Domain workloads repeat themselves — let them pay off.
- 🎭 **Il Suggeritore: grammar as a draft source** — constrained decoding uses
  structure to *forbid* tokens; Reame inverts it and uses structure to
  *propose* them. List numbering, bullets and format tokens are speculated
  for free on content nobody has ever generated before.
- 🔮 **Self-regulating speculative decoding** — a small draft model *or* zero-cost
  n-gram lookup proposes tokens; the target verifies them in one batched pass.
  Reame *measures* whether speculation pays on your hardware and switches it
  off by itself when it doesn't.
- 🏛️ **The Conclave: consensus as a quality knob** — `--best-of N` generates N
  candidate answers to the same prompt in one interleaved batch (one prefill,
  cloned into the others via KV copy; every weight read shared) and elects the
  w