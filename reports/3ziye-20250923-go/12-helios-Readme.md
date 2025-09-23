# Helios - Fast Version Control for AI Agents

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/good-night-oppie/helios?style=for-the-badge)](https://github.com/good-night-oppie/helios/releases/latest)
[![GitHub Downloads](https://img.shields.io/github/downloads/good-night-oppie/helios/total?style=for-the-badge&color=brightgreen)](https://github.com/good-night-oppie/helios/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg?style=for-the-badge)](LICENSE)
[![Go Version](https://img.shields.io/badge/go-1.22+-00ADD8?style=for-the-badge&logo=go)](https://golang.org/)

[![Platform Support](https://img.shields.io/badge/platforms-Linux%20|%20macOS%20|%20Windows-success?style=for-the-badge)](https://github.com/good-night-oppie/helios/releases)
[![Architecture](https://img.shields.io/badge/arch-AMD64%20|%20ARM64-blue?style=for-the-badge)](https://github.com/good-night-oppie/helios/releases)
[![Ask DeepWiki](https://img.shields.io/badge/deepwiki-indexed-purple?style=for-the-badge)](https://deepwiki.com/good-night-oppie/helios)
[![README_ZH](https://img.shields.io/badge/中文文档-README__ZH.md-red?style=for-the-badge)](README_ZH.md)

**H**ybrid / **E**fficient / **L**ayered / **I**ncremental **O**bject **S**tate (Engine)

## Problems Helios Solves

**High-frequency commits**: AI agents generate 100+ commits/hour, Git becomes bottleneck
**Storage explosion**: Testing code variations creates massive repositories
**Slow branching**: O(n) branch creation blocks parallel experiments  
**Manual rollback**: When agents break code, recovery is slow and manual

## Quick Start

```bash
# Install
curl -sSL https://raw.githubusercontent.com/good-night-oppie/helios/master/scripts/install.sh | sh

# Use with existing project
cd my-project
echo "print('hello')" > test.py
helios commit --work .  # Fast commit of current directory
```

## How It Works

**Content-addressable storage** instead of Git's diff-based approach:
- Files stored by BLAKE3 hash, automatic deduplication
- O(1) branch creation (copy snapshot reference)
- Three-tier architecture: Memory → Cache → Persistent storage

## Quick Start: 5 Minutes to Faster AI Development

```bash
# Install Helios
curl -sSL https://raw.githubusercontent.com/good-night-oppie/helios/master/scripts/install.sh | sh

# Basic usage (v0.0.1 commands)
cd your-ai-project/

# Commit current working directory
helios commit --work .

# View statistics
helios stats

# Restore to a specific snapshot
helios restore --id <snapshotID>

# Compare snapshots
helios diff --from <id1> --to <id2>

# Extract files from snapshot
helios materialize --id <snapshotID> --out /path/to/output
```

## Real AI Coding Agent Use Cases

**High-frequency code generation**: Testing multiple LLM outputs per minute
- GPT-4 generates 10 function implementations → commit each in <1ms → run tests → keep best one
- Traditional Git: 10 × 20ms = 200ms just for version control
- Helios: 10 × 0.2ms = 2ms for version control

**Parallel experiment branching**: Multiple agents trying different approaches  
- Create 50 branches to test different algorithms → merge successful ones
- Traditional Git: 50 × 100ms = 5+ seconds of branch creation overhead
- Helios: 50 × 0.07ms = 3.5ms for all branches

**Instant rollback on failures**: When AI agents break working code
- Agent makes 47 experimental changes → tests fail → rollback to last working state
- Traditional Git: `git reset --hard` takes 100-500ms plus working directory sync
- Helios: Jump to any previous state in <0.1ms

## How It Works (Technical Overview)

### Why Helios Is Faster

**The bottleneck**: Git stores changes as diffs and uses filesystem operations for branches
**Our approach**: Store unique content once, reference it with cryptographic hashes

```
Traditional Git                    Helios Content-Addressable
├── commit1/                      ├── content/
│   ├── file1.py (full content)   │   ├── abc123... → "def func1():"
│   └── file2.py (full content)   │   ├── def456... → "def func2():"  
├── commit2/                      │   └── ghi789... → "def func3():"
│   ├── file1.py (diff)           └── snapshots/
│   └── file2.py (diff)               ├── commit1 → [abc123, def456]
└── commit3/                          └── commit2 → [abc123, ghi789]
    ├── file1.py (diff)
    └── file2.py (diff)
```

**Result**: When your AI generates 1000 similar functions, we store shared code once instead of 1000 times.

### Three-Layer Performance Architecture

```
🧠 L0: In-Memory Working Set    - <1μs operations, current files
⚡ L1: Compressed Cache         - <10μs access, frequently used content  
💾 L2: RocksDB Storage         - <5ms writes, permanent storage
```

**Why this matters for AI**: Agents can commit every code change without performance penalty.

### Performance: When It Matters

**Operations per second your AI can achieve:**

| Task | Git Limit | Helios | Real Impact |
|------|-----------|---------|-------------|
| Code commit