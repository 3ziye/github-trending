# Hallucination Risk Calculator & Prompt Re-engineering Toolkit (OpenAI-only)

**Post-hoc calibration without retraining** for large language models. This toolkit turns a raw prompt into:  
1) a **bounded hallucination risk** using the Expectation-level Decompression Law (EDFL), and  
2) a **decision** to **ANSWER** or **REFUSE** under a target SLA, with transparent math (nats).

It supports two deployment modes:

- **Evidence-based:** prompts include *evidence/context*; rolling priors are built by erasing that evidence.
- **Closed-book:** prompts have *no evidence*; rolling priors are built by semantic masking of entities/numbers/titles.

All scoring relies **only** on the OpenAI Chat Completions API. No retraining required.

---

## Table of Contents
- [Install & Setup](#install--setup)
- [Core Mathematical Framework](#core-mathematical-framework)
- [Understanding System Behavior](#understanding-system-behavior)
- [Two Ways to Build Rolling Priors](#two-ways-to-build-rolling-priors)
- [API Surface](#api-surface)
- [Calibration & Validation](#calibration--validation)
- [Practical Considerations](#practical-considerations)
- [Project Layout](#project-layout)
- [Deployment Options](#deployment-options)

---

## Install & Setup

```bash
pip install --upgrade openai
export OPENAI_API_KEY=sk-...
```

> The module uses `openai>=1.0.0` and the Chat Completions API (e.g., `gpt-4o`, `gpt-4o-mini`).

---

## Core Mathematical Framework

### The EDFL Principle

Let the binary event $\mathcal{A}$ be the thing you want to guarantee (e.g., **Answer** in decision mode, or **Correct** for factual accuracy).  
Build an ensemble of **content-weakened prompts** (the *rolling priors*) $\{S_k\}_{k=1}^m$. For the realized label $y$, estimate:

- **Information budget:**  
  $$\bar{\Delta} = \tfrac{1}{m}\sum_k \mathrm{clip}_+(\log P(y) - \log S_k(y), B)$$
  (one-sided clipping; default $B=12$ nats to prevent outliers while maintaining conservative bounds).

- **Prior masses:** $q_k = S_k(\mathcal{A})$, with:
  - $\bar{q}=\tfrac{1}{m}\sum_k q_k$ (average prior for EDFL bound)
  - $q_{\text{lo}}=\min_k q_k$ (worst-case prior for SLA gating)

By EDFL, the achievable reliability is bounded by:  
$$\bar{\Delta} \ge \mathrm{KL}(\mathrm{Ber}(p) \| \mathrm{Ber}(\bar{q})) \Rightarrow p\le p_{\max}(\bar{\Delta},\bar{q})$$

Thus the **hallucination risk** (error) is bounded by $\overline{\mathrm{RoH}} \le 1 - p_{\max}$.

### Decision Rule (SLA Gating)

For target hallucination rate $h^*$:
- **Bits-to-Trust:** $\mathrm{B2T} = \mathrm{KL}(\mathrm{Ber}(1-h^*) \| \mathrm{Ber}(q_{\text{lo}}))$
- **Information Sufficiency Ratio:** $\mathrm{ISR} = \bar{\Delta}/\mathrm{B2T}$
- **ANSWER** iff $\mathrm{ISR}\ge 1$ *and* $\bar{\Delta} \ge \mathrm{B2T} + \text{margin}$ (default `margin≈0.2` nats)

> **Why two priors?** The gate uses **worst-case** $q_{\text{lo}}$ for strict SLA compliance. The RoH bound uses **average** $\bar{q}$ per EDFL theory. This dual approach ensures conservative safety while providing realistic risk bounds.

---

## Understanding System Behavior

### Expected Behavioral Patterns

The toolkit exhibits different behaviors across query types, which is **mathematically consistent** with the framework:

#### Simple Arithmetic Queries
**Observation:** May abstain despite apparent simplicity  
**Explanation:**
- Models often attempt answers even with masked numbers (pattern recognition)
- This yields **low information lift** $\bar{\Delta} \approx 0$ between full prompt and skeletons
- Despite potentially low EDFL risk bound, worst-case prior gate triggers **abstention** (ISR < 1)

#### Named-Entity Factoids
**Observation:** Generally answered with confidence  
**Explanation:**
- Masking entities/dates substantially reduces answer propensity in skeletons
- Restoring these yields **large** $\bar{\Delta}$ that clears B2T threshold
- System **answers** with tight EDFL risk bound

**This is not a bug but a feature**: The framework prioritizes safety through worst-case guarantees while providing realistic average-case bounds.

### Mitigation Strategies

1. **Switch Event Measurement**
   - Use **Correct/Incorrect** instead of Answer/Refuse for factual QA
   - Skeletons without key information rarely yield correct results → large $\bar{\Delta}$

2. **Enhance Skeleton Weakening**
   - Implement mask-aware decision head that refuses on redaction tokens
   - Ensures skeletons have strictly lower "Answer" mass than full prompt

3. **Calibration Adjustments**
   - Relax $h^*$ slightly (e.g., 0.10 instead of 0.05) for higher answer rates
   - Reduce margin for less conservative gating
   - Increase sampling ($n=7-10$) for stability

4. **Provide Evidence**
   - Adding compact, relevant evidence increases $\bar{\Delta}$ while preserving bounds

---

## Two Ways to Build Rolling Priors

### 1) Evidence-based (when you have context)

- **Prompt** contains a field like `Evidence:` (or JSON keys)
- **Skeletons** erase the evidence content but preserve st