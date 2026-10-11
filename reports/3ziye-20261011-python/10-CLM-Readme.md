<!-- markdownlint-disable MD001 MD041 -->
<p align="center">
  <picture>
    <img alt="CLM v0.1" src="assets/logo.png" width=45%>
  </picture>
</p>

<h3 align="center">
Contrastive Language Models
</h3>

<p align="center">
<i>A System One Model for Fast and Generalizable Decision-Making</i>
</p>

<p align="center">
| 📄 <a href="https://contrastive-lm.notion.site"><b>Blog</b></a> | 🗣️ <a href="https://discord.gg/5dAQEDJBs"><b>Discord</b></a> | 🤗 <a href="https://huggingface.co/Contrastive-LM"><b>Data &amp; Models</b></a> | 📚 <a href="#api-reference"><b>API Reference</b></a> | 🛠️ <a href="#fine-tuning-clm-on-your-own-data"><b>Fine-Tuning Tutorial</b></a> |
</p>

🔥 **Contrastive Language Models (CLMs)** are a new class of **System One
model** trained with a **contrastive learning** objective that connects
**states and actions**. This repo serves **CLM-8B** behind a
TypeSafe-compatible API.

- **CLM-8B** is pre-trained on **60M Nemotron Q&A pairs**, mid-trained on
  **30M synthetic hard negatives**, and post-trained on **1M agentic
  trajectories**.
- It performs on par with **Jev** across computer-use, gaming and tool-calling
  tasks with up to **9× lower latency**. With lightweight fine-tuning it sets a
  new SOTA as a verifier on agentic coding benchmarks: **Terminal-Bench 2.1
  (87.6%)** and **DeepSWE (81.6%)**.
- **States and actions are disaggregated**, so their embeddings are cached and
  reused independently, which makes training and serving cheap and blazing fast!

We invite the community to plug it into their own agents and benchmarks!

---

## Installation

```bash
pip install contrastive-lm
```

To install the latest from a clone:

```bash
pip install -e .
```

---

## Quickstart

### Serve

```bash
# 1. encoder (Qwen3-8B embeddings)
vllm serve Qwen/Qwen3-8B --served-model-name qwen3-8b --runner pooling --max-model-len 2048 --port 8090 &

# 2. CLM API on :8700 (downloads the 75 MB reference head on first run)
clm-serve
```

States longer than 2048 tokens are truncated. For longer states, raise both limits
together, e.g. `--max-model-len 8192` on `vllm serve` and `clm-serve --max-tokens 8192`
(needs more GPU memory).

### Ask typed questions about a state

```python
from clm import CLMClient, Choice, Noul, Score

client = CLMClient()                          # CLM_BASE_URL (default http://127.0.0.1:8700), CLM_API_KEY
r = client.system_one(
    state="Customer: my invoice was charged twice and nobody answers the phone!",
    questions={
        "urgency": Noul(instructions="Is this urgent?"),
        "department": Choice(instructions="Which team should handle this?",
                             criteria={"billing": "Charges, invoices, refunds",
                                       "technical": "Bugs and outages"}),
        "frustration": Score(instructions="How frustrated is the customer?",
                             criteria=["Calm", "Frustrated", "Very angry"]),
    },
)
print(r.answers["urgency"].noul)                # 0.41022     probability the statement is true
print(r.answers["department"].choice)           # billing
print(r.answers["department"].probabilities)    # {'billing': 0.93878, 'technical': 0.06122}
print(r.answers["frustration"].score)           # 1.98386     expected level, 0..2
print(r.usage.input_tokens, r.latency_ms)       # 38 58.1     (106 tokens on a cold cache: option texts are embedded once)
```

Questions may be `Noul` / `Choice` / `Score` objects or plain wire-format
dicts, so a request written for TypeSafe replays as
`client.system_one(state, questions)`.

### Rank candidates directly

`system_one` is built on one primitive: score a candidate against a state.
For free-form candidates (best-of-N answers, tool names, next moves) use the
in-process engine's `rank`:

```python
from clm import Engine

engine = Engine(emb_url="http://127.0.0.1:8090/v1/embeddings")     # reference head, downloaded if missing
engine.rank("What causes tides on Earth?",
            ["The Moon's gravitational pull.", "Photosynthesis in plants.", "Because the Earth is round."])
# [{'rank': 1, 'candidate': "The Moon's gravitational pull.", 'prob': 0.997}, ...]

engine.answer(state, questions)      # the same dict the HTTP endpoint returns, no server needed
```

---

## Playground

`clm-serve` also serves a web UI at `/` (`http://localhost:8700/` by default).
Write a state, add typed questions, and see CLM's answer distributions; every
request is also shown as JSON, `curl` and Python. A **Rank** tab ranks any
candidate set, and links are shareable.

<p align="center">
  <picture>
    <img alt="The CLM playground: a state on the left with three typed questions, their answer distributions on the right"
         src="assets/playground.png" width=100%>
  </picture>
  <br>
  <sub>Captured against a real <code>clm-serve</code> (<code>clm-latest</code>, Qwen3-8B encoder on one RTX 4090).</sub>
</p>

Remote server? `ssh -L 8700:localhost:8700 <host>`. API only: `clm-serve --no-ui`.

---

## Results

### Ze