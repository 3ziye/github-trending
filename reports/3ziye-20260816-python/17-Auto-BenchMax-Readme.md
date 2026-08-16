<div align="center">

[English](README.md) | [中文](README_zh.md)

# 🚀 Auto-BenchMax

**One click to automatically build benchmark-targeted data and reach up to 2× the base model's score.**

<img src="aseets/results.png" alt="Auto-BenchMax results: one iteration of skill-synthesized data more than doubles the base model's score on Tau2-bench (telecom) and MCP-Atlas" width="820">

</div>

---

## 💡 Motivation

> Some say this is *"the darkest hour for domestic models"* and that *"winter is coming"* — that the industry has been dragged into a vicious cycle of building for investors and benchmark numbers, while real technical progress gets left behind.
>
> 有人说这是"国模最黑暗的时代"、"凛冬将至"，行业被拖入了面向投资人和 benchmark 数字开发的死循环，真正的技术积累反而被搁置了。

I don't fully agree with this. But I also know that many practitioners really are trapped in the daily grind of chasing benchmark scores, leaving them little energy for work that truly matters. This is harmful — both to individual growth and to the overall progress of domestic models.

To make this easy for the community to use and reproduce, this project open-sources:

- **Pipeline** — the data-construction pipeline
- **Training code** — scripts to reproduce the runs
- **Environment** — adapted from the MCP-Atlas benchmark pipeline
- **Data** — generated within that environment

With a single click, you can reproduce a run that scores **2× higher than the base model** on **MCP-Atlas** — a benchmark that companies like OpenAI and Anthropic follow closely.

> The data released here comes from the **first iteration**. Using the provided training scripts, it reaches a score of **40.4** (up from a **19.1** baseline). A single iteration already more than doubles the base model's score, and further iterations can push past **50**. The evaluation set is the **MCP-Atlas public set**.

---

## 🛠️ Synthesize Data for Your Own Benchmark

### **It's as simple as one sentence:**

If you use an agent (e.g. Claude Code) that supports skills, the easiest way is a **single sentence**: point it at your evaluation entry point and let the skill drive the whole pipeline. For example:

> My eval launch command is `<your eval command>`. Read this skill and synthesize training data for this benchmark.

The reproduction above uses our released data. To generate **same-distribution data for your own tool-use / agentic benchmark**, use the skill under [`skills/tool-use-data-synthesis/`](skills/tool-use-data-synthesis/) (see [`SKILL.md`](skills/tool-use-data-synthesis/SKILL.md)).

The skill picks one of two synthesis paradigms based on how your benchmark scores — **Paradigm A** for LLM-judged benchmarks and **Paradigm B** for rule-based ones:

<div align="center">
<img src="aseets/paradigm-a.png" alt="Paradigm A: Execute-then-Extract — Generate, Execute, Extract, Filter" width="380">
<img src="aseets/paradigm-b.png" alt="Paradigm B: Construct-then-Verify — Construct, Verify, Phrase, Roll" width="380">
</div>

The skill will read your evaluator to determine the scoring mechanism (rule-based vs. LLM-judged), pick the right synthesis paradigm, align to your benchmark's structural distribution, roll out real trajectories, and emit training data — following the methodology in `SKILL.md`.

---

## 📂 Repository Layout

```
Auto-BenchMax/
├── skills/
│   └── tool-use-data-synthesis/   # the core skill: methodology + references that drive the whole data-synthesis pipeline
├── codes/
│   ├── axolotl/                   # training code, adapted from axolotl; our configs live in benchmax_configs/ and launch scripts in benchmax_scripts/
│   └── mcp-atlas/                 # the evaluation environment — the MCP-Atlas benchmark adapted to run our pipeline end-to-end
├── datas/
│   └── benchmax_sft_iter1.jsonl   # first-iteration SFT data (1312 tool-use samples), ready to train on
└── aseets/                        # figures used in this README
```

**A note on `codes/mcp-atlas/`:** it is adapted from Scale AI's [MCP-Atlas](https://scale.com/leaderboard/mcp_atlas) benchmark. We wired our pipeline into it so that trajectory roll-out, evaluation, and scoring all run within the same environment used to produce the results above.

---

## 🔁 Reproduce Our Results

The released data and training scripts let you reproduce the first-iteration run end-to-end.

### 1. Get the code and set up axolotl

The training code lives under [`codes/axolotl/`](codes/axolotl/), adapted from [axolotl](https://github.com/axolotl-ai-cloud/axolotl). Set up its environment (a `.venv` under `codes/axolotl/`) by following the axolotl install guide: https://github.com/axolotl-ai-cloud/axolotl#
### 2. Training data

The first-iteration SFT data is already in this repo:

```
datas/benchmax_sft_iter1.jsonl        # 1312 tool-use SFT samples (first iteration)
```

Each line is a chat sample with `messages` and `tools` fields — the exact payload format the model was trained on.

### 3. Point the config at your model

Open [`codes/axolotl/benchmax_configs/qwen3_exp0.yaml`