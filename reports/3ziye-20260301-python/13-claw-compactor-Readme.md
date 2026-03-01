# Claw Compactor
![Claw Compactor Banner](assets/banner.png)

[![Build](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/aeromomo/claw-compactor) [![Release](https://img.shields.io/github/v/release/aeromomo/claw-compactor?color=blue)](https://github.com/aeromomo/claw-compactor/releases) [![Tests](https://img.shields.io/badge/tests-800%20passed-brightgreen)](https://github.com/aeromomo/claw-compactor) [![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://python.org) [![License](https://img.shields.io/badge/license-MIT-purple)](LICENSE) [![OpenClaw](https://img.shields.io/badge/OpenClaw-skill-orange)](https://openclaw.ai)

*"Cut your tokens. Keep your facts."*

**Cut your AI agent's token spend in half.** One command compresses your entire workspace — memory files, session transcripts, sub-agent context — using 5 layered compression techniques. Deterministic. Mostly lossless. No LLM required.

## Features
- **5 compression layers** working in sequence for maximum savings
- **Zero LLM cost** — all compression is rule-based and deterministic
- **Lossless roundtrip** for dictionary, RLE, and rule-based compression
- **~97% savings** on session transcripts via observation extraction
- **Tiered summaries** (L0/L1/L2) for progressive context loading
- **CJK-aware** — full Chinese/Japanese/Korean support
- **One command** (`full`) runs everything in optimal order

## 5 Compression Layers
| 1 | Rule engine | Dedup lines, strip markdown filler, merge sections | 4-8% | |
| 2 | Dictionary encoding | Auto-learned codebook, `$XX` substitution | 4-5% | |
| 3 | Observation compression | Session JSONL → structured summaries | ~97% | * |
| 4 | RLE patterns | Path shorthand (`$WS`), IP prefix, enum compaction | 1-2% | |
| 5 | Compressed Context Protocol | ultra/medium/light abbreviation | 20-60% | * |

\*Lossy techniques preserve all facts and decisions; only verbose formatting is removed.

## Quick Start
```bash
git clone https://github.com/aeromomo/claw-compactor.git
cd claw-compactor

# See how much you'd save (non-destructive)
python3 scripts/mem_compress.py /path/to/workspace benchmark

# Compress everything
python3 scripts/mem_compress.py /path/to/workspace full
```

**Requirements:** Python 3.9+. Optional: `pip install tiktoken` for exact token counts (falls back to heuristic).

## Architecture
┌─────────────────────────────────────────────────────────────┐
│ mem_compress.py │
│ (unified entry point) │
└──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬────┘
 │ │ │ │ │ │ │ │
 ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼
 estimate compress dict dedup observe tiers audit optimize
 └──────┴──────┴──┬───┴──────┴──────┴──────┴──────┘
 ▼
 ┌────────────────┐
 │ lib/ │
 │ tokens.py │ ← tiktoken or heuristic
 │ markdown.py │ ← section parsing
 │ dedup.py │ ← shingle hashing
 │ dictionary.py │ ← codebook compression
 │ rle.py │ ← path/IP/enum encoding
 │ tokenizer_ │
 │ optimizer.py │ ← format optimization
 │ config.py │ ← JSON config
 │ exceptions.py │ ← error types
 └────────────────┘

## Commands
All commands: `python3 scripts/mem_compress.py <workspace> <command> [options]`

`full`, Description=Complete pipeline (all steps in order), Typical Savings=50%+ combined
`benchmark`, Description=Dry-run performance report, Typical Savings=—
`compress`, Description=Rule-based compression, Typical Savings=4-8%
`dict`, Description=Dictionary encoding with auto-codebook, Typical Savings=4-5%
`observe`, Description=Session transcript → observations, Typical Savings=~97%
`tiers`, Description=Generate L0/L1/L2 summaries, Typical Savings=88-95% on sub-agent loads
`dedup`, Description=Cross-file duplicate detection, Typical Savings=varies
`estimate`, Description=Token count report, Typical Savings=—
`audit`, Description=Workspace health check, Typical Savings=—
`optimize`, Description=Tokenizer-level format fixes, Typical Savings=1-3%

### Global Options
- `--json` — Machine-readable JSON output
- `--dry-run` — Preview changes without writing
- `--since YYYY-MM-DD` — Filter sessions by date
- `--auto-merge` — Auto-merge duplicates (dedup)

## Real-World Savings
Session transcripts (observe), Typical Savings=**~97%**, Notes=Megabytes of JSONL → concise observation MD
Verbose/new workspace, Typical Savings=**50-70%**, Notes=First run on unoptimized workspace
Regular maintenance, Typical Savings=**10-20%**, Notes=Weekly runs on active workspace
Already-optimized, Typical Savings=**3-12%**, Notes=Diminishing returns — workspace is clean

## cacheRetention — Complementary Optimization
Before compression runs, enable **prompt caching** for a 90% discount on cached tokens:

```json
{
 "agents": {
 "defaults": {
 "models": {
 "anthropic/claude-opus-4-6": {
 "params": {
 "cacheRetention": "long"
 }

Compression reduces token count, caching reduces cost-per-token. Together: 50% compression + 90% cache discount = **95% effective cost reduction**.

## Heartbeat Automation
Run weekly or on heartbeat:

```markdown

## Memory Maintenance 