# NanoJev — A nano replica of [Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)

**English** | [简体中文](README.zh-CN.md)

**A 0.6B parallel decision model: states and questions in, complete probability distributions out. Zero output-token decoding.**

> **New project: [JevHarness](https://github.com/TianyuCodings/JevHarness)** — Let an LLM build task-specific decision harnesses with [Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev), with optional refinement using rewards and execution traces. Includes an interactive Pokémon demo.

[Play ViZDoom](https://nanojev-dev.tianyuchen99.chatgpt.site/?autoplay=1) · [Maze & Snake](https://nanojev-dev.tianyuchen99.chatgpt.site/side-by-side?autoplay=1#maze) · [Model](https://huggingface.co/C-Tianyu/NanoJev) · [Dataset](https://huggingface.co/datasets/C-Tianyu/NanoJev-Data)

**Now playing ViZDoom:** one shared checkpoint handles Basic aiming and Predict Position's moving-target rocket shots, alongside Maze and Snake.

**4 tasks · 18,760 decision questions per data variant · 896 Predict Position expert episodes**

## What's new

**September 20, 2026 — One model, four games.**

- **ViZDoom Basic:** **128/128** test successes, compared with **56/128** for [Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev).
- **ViZDoom Predict Position:** **27/128** test successes, up from **11/128** before this round; the matched [Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) run also scores **11/128**. The policy learns when to turn, wait and fire at a moving target.
- **16,333 ViZDoom questions** within an **18,760-question** mixed-task dataset per target variant, spanning train, dev, calibration, test and OOD.
- **One model, four games:** the same step-400 checkpoint also completes the 50×50 maze in **225 attempts** and collects **30 food items** during a full 256-step Snake run.

## Three models, side by side

Real browser replays of **[Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev), NanoJev and Untuned Qwen**. These animations loop automatically; click either one to open its interactive player. All four demos use the same current NanoJev checkpoint. The interactive development site currently requires access; all recordings can also be played locally using the commands below.

### ViZDoom Basic · Aim, then fire

[![NanoJev eliminates the target with one shot while Jev and Untuned Qwen fail, shown side by side on the same game clock](assets/basic_unified_autoplay.gif)](https://nanojev-dev.tianyuchen99.chatgpt.site/?autoplay=1)

Move into position, line up the target, fire. NanoJev eliminates the target with **one shot in 1.40 s**; [Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) and Untuned Qwen each fire **19 shots** without an elimination before the deadline. The three panels share the same game clock and show original frames and action probabilities.

### Find the exit · 50×50 Maze

[![Jev, current NanoJev and Untuned Qwen explore the same 50×50 maze in the live three-panel viewer](assets/maze_unified_autoplay.gif)](https://nanojev-dev.tianyuchen99.chatgpt.site/side-by-side?autoplay=1#maze)

NanoJev reaches the exit in **225 attempts**, versus **2,738** for [Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) and **4,726** for Untuned Qwen. Each system combines local safety probabilities with the same exploration code and remembered open paths.

[Play Snake](https://nanojev-dev.tianyuchen99.chatgpt.site/side-by-side?autoplay=1#snake) · [Play Predict Position](https://nanojev-dev.tianyuchen99.chatgpt.site/predict-position?autoplay=1)

## What NanoJev does

- **Parallel decisions:** batch independent states, questions and candidate paths in one backbone forward.
- **Dynamic candidates:** Choice returns a distribution over 2–255 supplied candidates using a shared scoring head.
- **Boolean and ordered scores:** predict a proposition's probability, or a distribution and expectation over 2–10 ordered levels.
- **Direct probabilities:** rank, select or sample actions without generating answer tokens.
- **One small backbone:** Qwen3-0.6B with decision heads, reused across all four game tasks and a persistent inference service.

Each request supplies a **state**, a **question** and its **candidates**. The backbone encodes candidate paths; shared heads produce the requested probabilities. Choice uses set attention and a softmax, Boolean uses a sigmoid, and Score returns a probability-weighted level.

## Held-out gameplay

Successful episodes on the complete **274-case test set**, using the same observation interface, candidate actions and seeded epsilon-greedy controller across systems:

| Model | Maze | Snake | Basic | Predict Position |
|---|---:|---:|---:|---:|
| **NanoJev** | **4/10** | **8/8** | **128/128** | **27/128** |
| [Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) | 7/10 | 8/8 | 56/128 | 11/128 |
| Untuned Qwen3-0.6B | 2/10