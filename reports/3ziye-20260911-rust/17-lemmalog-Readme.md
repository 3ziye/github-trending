# Lemmalog

A Datalog engine for LLM agent memory. This repo contains the engine
(Rust crate, MCP server, REPL, agent skill) plus the design document
([`datalog-context-engine-design.md`](datalog-context-engine-design.md),
with an honest status log of what shipped).

The thesis: **an agent's memory should be a deductive database** — the
agent builds a *verifiable model of what it knows* and mechanically
reasons over how that knowledge changes, rather than "remembering
better" than a vector store. Base facts
are asserted at the ingestion boundary (LLM extraction); rules derive
closures, temporal projections, contradiction candidates, and relevance
diffusion; every fact carries provenance back to its source episodes; and
each conversation turn updates derived views incrementally instead of
re-deriving them (or worse, re-reasoning them in-context).

## What's implemented

| Design element | Status |
|---|---|
| Runtime-parsed, stratified Datalog (interpreter, not proc-macro) | ✅ |
| Negation-as-absence with negative-cycle rejection | ✅ |
| Seminaive fixpoint with per-epoch delta maintenance | ✅ |
| Bi-temporal facts via `valid_from`/`valid_to`/`asserted_at` columns + `now()` | ✅ |
| Semiring annotations: confidence (product t-norm) × provenance (set union) | ✅ |
| Annotation merge on re-derivation (max conf, union prov, deduped supports) | ✅ |
| `why()` proof trees with cycle protection | ✅ |
| Additive arithmetic in comparisons (`D = Dm + 1`) with linear solving | ✅ |
| Scoped negative deltas: retraction recomputes only transitive dependents | ✅ |
| `ask()` — read-only datalog query surface for agents | ✅ |
| Magic-sets demand evaluation (`ask_deep`): point queries without full fixpoint | ✅ |
| Per-position secondary indexes; row-id lookups; WAM-style trail backtracking | ✅ |
| Epoch change-log: `changes_from/since` + "new in memory" context section | ✅ |
| Hybrid retrieval (`context_for_query`): BM25 + entity/graph boosting, budget-aware | ✅ |
| Extraction boundary: `Extractor` trait, memoized `MockExtractor` + `LlmExtractor` | ✅ |
| Deterministic update policy: ADD / UPDATE / NOOP / escalate | ✅ |
| Positional `ContextAssembler` (distilled top, verbatim provenance bottom, budget) | ✅ |
| `AgentMemory` facade: observe → policy → maintain → ask/ask_deep/context/why | ✅ |
| Persistence: snapshot save/load (episodes + EDB facts + rules; derived rebuilt) | ✅ |
| Semantic side index: `Embedder` trait, `HashEmbedder`, `seed_mentions` + `near` diffusion | ✅ |
| DRed-lite scoped recompute: supersession rebuilds only what actually changed | ✅ |
| Synthetic eval harness (`scenario::run_eval`): accuracy/token/latency vs. ground truth | ✅ |
| Aggregation: `count`/`min`/`max`/`sum` head args with group-by fold + value-change propagation | ✅ |
| Entity resolution: star-shaped aliasing, directional canonical views, conflict escalation | ✅ |
| MCP server (`--features mcp`): the engine as tools for Claude Code / Kimi CLI | ✅ |
| Rule registry: versioned batches, agent install/uninstall, backfill on change | ✅ |
| Hypotheticals: `what_if` lookahead with byte-identical store restore | ✅ |
| Streaming change feed: `Added`/`Retracted`/`Cleared` events for projections | ✅ |
| Indexed read paths: `query`/`ask` select buckets (point lookups ~100µs at 4M facts) | ✅ |
| Differential testing: 450 random programs vs a naive fixpoint oracle + parser fuzzing | ✅ |
| REPL: `cargo run --bin lemmalog` (rule / + / ? / ?? / why / run / dump / batches) | ✅ |
| Leapfrog triejoins (worst-case-optimal joins), DBSP streaming deltas | 🚧 future phases |

## Entity resolution (canonicalization)

The LLM proposes star-shaped `alias(Local, Canonical)` edges; Datalog
derives the closure; canonical views project facts read-side only
(`src/canonical.rs`):

```prolog
alias(Acme_Corp, Acme).                       % LLM-proposed, confidence-tagged
same_as(X, Y) :- alias(X, Y).                 % symmetric-transitive closure
same_as(X, Z) :- same_as(X, Y), same_as(Y, Z).
maps_to(X, X) :- entity(X), !aliased(X).      % directional projection:
maps_to(L, C) :- alias(L, C).                 %  exactly one canonical spelling
current_canon(S, R, O) :- current(S, R, O), maps_to(S, S2), maps_to(O, O2).
```

Safety properties (all tested): topology violations — a local with two
canonicals, or a name both local and canonical — derive `alias_conflict`
facts instead of merging identities; confidence propagates through the
closure (weak two-hop merges are visibly low-confidence); retracting an
alias edge collapses the closure and every downstream view in the same
epoch. A similarity-gated LLM reconciliation pass
(`canonical::reconcile::reconcile_entities`) offers only
embedding-similar name pairs to the model.

Building this surfaced and fixed two long-lived engine bugs: the scoped
recompute never processed same-stratum dependents (latent stale-fact
bug), fixed by SCC-condensation stratification plus a recompute
fixpoint; and the invalidation pass ran before lower strata w