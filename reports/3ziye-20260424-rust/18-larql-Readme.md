# LARQL

The model IS the database. Query neural network weights like a graph database. No GPU required.

LARQL decompiles transformer models into a queryable format called a **vindex** (vector index), then provides **LQL** (Lazarus Query Language) to browse, edit, and recompile the model's knowledge.

```sql
larql> USE "gemma3-4b.vindex";
Using: gemma3-4b.vindex (34 layers, 348.2K features, relations: 512 types)

larql> DESCRIBE "France";
France
  Edges (L14-27):
    capital     → Paris              1436.9  L27  (probe)
    language    → French               35.2  L24  (probe)
    continent   → Europe               14.4  L25  (probe)
    borders     → Spain                13.3  L18  (probe)

larql> INSERT INTO EDGES (entity, relation, target)
   ...   VALUES ("John Coyle", "lives-in", "Colchester");
Inserted 1 edge. Feature F8821@L26 allocated.

larql> INFER "The capital of France is" TOP 3;
  1. Paris                (97.91%)
  2. the                  (0.42%)
  3. a                    (0.31%)
```

## Quick Start

```bash
# Build
cargo build --release

# Pull a pre-built vindex from HuggingFace
larql pull hf://chrishayuk/gemma-3-4b-it-vindex

# List what's cached
larql list

# Run it — one-shot or chat
larql run gemma-3-4b-it-vindex "The capital of France is"
larql run gemma-3-4b-it-vindex          # drops into chat mode

# Or extract locally — inference-ready at f16 by default
larql extract google/gemma-3-4b-it -o gemma3-4b.vindex
larql run gemma3-4b.vindex "Einstein is known for"
```

`larql extract` defaults to `--level inference` (full local forward
pass) stored at f16. No flags needed for the common case.

<details>
<summary>Extract tiers and options</summary>

```bash
# Browse-only — gate KNN + embeddings, no forward pass (~3 GB for 4B)
larql extract google/gemma-3-4b-it -o gemma3-4b.vindex --level browse

# Attention-only — client-side slice for `run --ffn URL` (Act 2 demo)
larql extract google/gemma-3-4b-it -o gemma3-4b.attn.vindex --level attention

# Inference (default) — full local forward pass
larql extract google/gemma-3-4b-it -o gemma3-4b.vindex
larql extract google/gemma-3-4b-it -o gemma3-4b.vindex --level inference

# All — +lm_head +COMPILE extras (largest)
larql extract google/gemma-3-4b-it -o gemma3-4b.vindex --level all

# Q4_K/Q6_K inline (Ollama-compatible, smallest disk footprint)
larql extract google/gemma-3-4b-it -o gemma3-4b.vindex --quant q4k

# Maximum size reduction on Q4K — drop gate_vectors.bin, rebuild from
# interleaved_q4k.bin at load (~1.6 s cost on 4B, ~12 s on 31B)
larql extract google/gemma-3-4b-it -o gemma3-4b.vindex \
  --quant q4k --drop-gate-vectors

# Uniform Q4_K on FFN — gate + up + down all Q4_K (default stores
# down as Q6_K). ~30 MB/layer smaller, ~1.5–1.7× faster decode down
# matmul. Adds ~1.5 % softmax drift; top-1 / top-5 preserved.
larql extract google/gemma-4-31b-it -o gemma4-31b.vindex \
  --quant q4k --down-q4k

# Opt out of f16 (rarely wanted — doubles file sizes)
larql extract google/gemma-3-4b-it -o gemma3-4b.vindex --f32

# Convert from GGUF instead of extracting from safetensors
larql convert gguf-to-vindex model.gguf -o model.vindex
```

`extract-index` is kept as a backwards-compatible alias of `extract`.

</details>

### Serve it over HTTP + gRPC

```bash
larql serve gemma3-4b.vindex --port 8080
```

### Run attention locally, FFN on another machine

```bash
# Extract once, then carve deployment slices with `larql slice`.
# Either --preset or --parts a,b,c works; `--dry-run` previews.
larql extract google/gemma-4-31b-it -o gemma4-31b.vindex --quant q4k

# Client slice (7.4 GB for 31B Q4_K — attn + embed + norms + tokenizer)
larql slice gemma4-31b.vindex --preset client -o gemma4-31b.client.vindex

# Server slice (27 GB — gate + interleaved FFN + down_meta, no attention)
larql slice gemma4-31b.vindex --preset server -o gemma4-31b.server.vindex

# Server (holds the FFN half):
larql serve gemma4-31b.server.vindex --port 8080 --ffn-only

# Client (laptop — runs attention locally, FFN over HTTP):
larql run gemma4-31b.client.vindex --ffn http://server.local:8080 \
  "The capital of France is"
```

Other presets: `browse` (DESCRIBE/WALK only, no forward pass), `router`
(MoE router only, ADR-0003), `all` (full clone). See `larql slice --help`
for the explicit part list.

**3-tier topology (ADR-0008).** When laptop RAM matters, split the
embedding table out to its own server:

```bash
# Attention-only client (no embed, no FFN — ~310 MB on 4B, 10× smaller than `client`)
larql slice gemma3-4b.vindex --preset attn -o gemma3-4b.attn.vindex

# Embed server slice (embed + tokenizer; paired with ADR-0008 embed-server)
larql slice gemma3-4b.vindex --preset embed -o gemma3-4b.embed.vindex
```

The 3-tier client + embed server + FFN server split unlocks the
"laptop in ~1 GB" version of the dense-remote topology for small
models. Full rationale in
[`docs/adr/0007-vindex-distribution.md`](docs/adr/0007-vindex-distribution.md)
and [`docs/adr/0008-embed-server.md`](d