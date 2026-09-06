# Qwen3.8-27B on one RTX 3090

![Stock vLLM against this repo, same card, same prompts](docs/media/demo.gif)

Serving setup for [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) on a
single 24 GB consumer GPU with vLLM — 150k token context and an OpenAI-compatible
API with key auth, in two ready-made modes.

## Quick start

The image is prebuilt and pushed to
[ghcr.io](https://github.com/syv-ai/qwen38-27b-rtx3090/pkgs/container/qwen38-27b-rtx3090)
on every commit — the build applies all `patches/` and runs `verify.sh` as its
gate, so `latest` is always the current stack. The first start pulls it (9.5 GB),
downloads and requantizes the model (~20 GB, once, into `./models`), and serves
on port 18020. Pick a mode — one GPU serves one at a time:

```bash
git clone https://github.com/syv-ai/qwen38-27b-rtx3090 && cd qwen38-27b-rtx3090

docker compose --profile single up -d    # one or a few people chatting
docker compose --profile batch  up -d    # API backend, many concurrent requests
```

| | `--profile batch` → [batch/](batch/) | `--profile single` → [single-user/](single-user/) |
|---|---|---|
| for | API backends, pipelines, many concurrent requests | one or a few people chatting |
| aggregate, 64 concurrent (128 in / 512 out) | **~1,035 tok/s** steady-state decode, 948 end-to-end (~1,222 / 1,042 with all layers int8) | n/a (8 slots) |
| single-stream (C1) decode rate, realistic prompts | 46 tok/s | MTP: **121** tok/s at default sampling, **120** greedy (`CTX=fast`, 64k; 96 / 102 with `CTX=long`, 150k). DFlash2 (`SPEC=dflash2`): **127** default, **130** greedy |
| reproducing its own context (quoting a document, applying an edit) | 46 tok/s | **381 tok/s** at 25k context — 15.0 tokens per verify step, drafted straight from the prompt (`SPEC=dflash2` + `DFLASH_TOKENS=15`) |
| trick | 16-bit recurrent state + int8 tensor-core GEMMs | MTP speculation with 4 cheap drafts, a draft vocabulary that covers what the model says, calibrated int4 lm_head/drafter, split-KV verify attention; optionally native vLLM 0.28.0 DFlash2 (7 drafts in one pass, int4-requantized) with a verify block the context fills |
<sub>Single-stream numbers re-measured 2026-08-22 on current main with
`bash bench/run_benchmarks.sh single` — `vllm bench serve`, the 8 prompts in
`bench/prompts_real.jsonl`, 1024 output tokens, C1, decode rate taken as
`C / mean TPOT`. Quote them against that harness: a client with a different output
length is not measuring the same thing, and mixing the two is how
[#3](https://github.com/syv-ai/qwen38-27b-rtx3090/issues/3) got confusing.</sub>

> Version note: this branch pins vLLM 0.28.0; the throughput and quality tables are
> retained as reference baselines while the v0.28.0 GPU matrix is being re-measured.

Both modes share one install — the mode is just which launch script you run.
Speculation wins below ~8 concurrent users on short prompts, plain batching above;
on long independent sessions the crossover is much earlier, because a speculating
request reserves recurrent-state pages the pool has few of — the concurrency
paragraph under "DFlash2 at 240k" has the measurement. Numbers are `vllm bench serve` on an
RTX 3090 at a 250 W power limit. If the card is yours alone, the fastest
configuration is three environment variables away:
[If you are the only user](#if-you-are-the-only-user-do-this).

Prefill is a separate budget from either: ~1,810 tok/s at 1k inputs in batch
mode, and in single-user mode ~1,440 tok/s stock or **~1,850-1,940 with
`INT8_ACT=int8`** (1,423 at 51k in), measured on the seeded benchmark protocol
([full matrix](batch/README.md#prefill); older published prefill rows came
from an unseeded harness that let the prefix cache contaminate the numbers,
and are not comparable). How each number was won:
[docs/optimizations.md](docs/optimizations.md).

The server listens on `0.0.0.0` and is unauthenticated unless you give it a key.
For anything past your own machine, add one first — everything reads it from
`.env` or `api_key.txt`, and nothing needs it otherwise:

```bash
echo "VLLM_API_KEY=$(openssl rand -hex 24)" > .env
```

No compose, no clone — plain Docker runs the same image with one command and
prepares the model itself on the first boot (into a named volume, so it
survives container replacement):

```bash
docker run -d --name qwen --gpus all --ipc=host -p 18020:18020 \
  -v qwen-models:/app/models -v qwen-cache:/cache \
  --restart unless-stopped ghcr.io/syv-ai/qwen38-27b-rtx3090:latest
```

`batch` after the image name is the other mode, and the knobs compose reads
from `.env` become `-e` flags (`-e VLLM_API_KEY=...`, `-e SPEC=dflash2`, ...) —
[docs/docker.md](docs/docker.md#plain-docker-no-compose) has the mapping.

Or by hand in a venv (same steps: model download, requantization, vLLM
patches, `verify.sh`) — see [Setup](#setup).

### If you are the only user, do this

The command above starts the conservative default — MTP speculation, 8 request
slots, 64k context, 120 tok/s greedy a