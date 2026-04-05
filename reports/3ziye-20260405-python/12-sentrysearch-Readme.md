# SentrySearch

Semantic search over video footage. Type what you're looking for, get a trimmed clip back.

[OpenClaw Skill](https://clawhub.ai/ssrajadh/natural-language-video-search)

[<video src="https://github.com/ssrajadh/sentrysearch/raw/main/docs/demo.mp4" controls width="100%"></video>](https://github.com/user-attachments/assets/baf98fad-080b-48e1-97f5-a2db2cbd53f5)

## How it works

SentrySearch splits your videos into overlapping chunks, embeds each chunk as video using either Google's Gemini Embedding API or a local Qwen3-VL model, and stores the vectors in a local ChromaDB database. When you search, your text query is embedded into the same vector space and matched against the stored video embeddings. The top match is automatically trimmed from the original file and saved as a clip.

## Getting Started

1. Install [uv](https://docs.astral.sh/uv/) (if you don't have it):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh    # macOS/Linux
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"  # Windows
```

2. Clone and install:

```bash
git clone https://github.com/ssrajadh/sentrysearch.git
cd sentrysearch
uv tool install .
```

3. Set up your API key (or [use a local model instead](#local-backend-no-api-key-needed)):

```bash
sentrysearch init
```

This prompts for your Gemini API key, writes it to `.env`, and validates it with a test embedding.

4. Index your footage:

```bash
sentrysearch index /path/to/footage
```

5. Search:

```bash
sentrysearch search "red truck running a stop sign"
```

ffmpeg is required for video chunking and trimming. If you don't have it system-wide, the bundled `imageio-ffmpeg` is used automatically.

> **Manual setup:** If you prefer not to use `sentrysearch init`, you can copy `.env.example` to `.env` and add your key from [aistudio.google.com/apikey](https://aistudio.google.com/apikey) manually.

## Usage

### Init

```bash
$ sentrysearch init
Enter your Gemini API key (get one at https://aistudio.google.com/apikey): ****
Validating API key...
Setup complete. You're ready to go — run `sentrysearch index <directory>` to get started.
```

If a key is already configured, you'll be asked whether to overwrite it.

> **Tip:** Set a spending limit at [aistudio.google.com/billing](https://aistudio.google.com/billing) to prevent accidental overspending.

### Index footage

```bash
$ sentrysearch index /path/to/video/footage
Indexing file 1/3: front_2024-01-15_14-30.mp4 [chunk 1/4]
Indexing file 1/3: front_2024-01-15_14-30.mp4 [chunk 2/4]
...
Indexed 12 new chunks from 3 files. Total: 12 chunks from 3 files.
```

Options:

- `--chunk-duration 30` — seconds per chunk
- `--overlap 5` — overlap between chunks
- `--no-preprocess` — skip downscaling/frame rate reduction (send raw chunks)
- `--target-resolution 480` — target height in pixels for preprocessing
- `--target-fps 5` — target frame rate for preprocessing
- `--no-skip-still` — embed all chunks, even ones with no visual change
- `--backend local` — use a local model instead of Gemini ([details below](#local-backend-no-api-key-needed))

### Search

```bash
$ sentrysearch search "red truck running a stop sign"
  #1 [0.87] front_2024-01-15_14-30.mp4 @ 02:15-02:45
  #2 [0.74] left_2024-01-15_14-30.mp4 @ 02:10-02:40
  #3 [0.61] front_2024-01-20_09-15.mp4 @ 00:30-01:00

Saved clip: ./match_front_2024-01-15_14-30_02m15s-02m45s.mp4
```

If the best result's similarity score is below the confidence threshold (default 0.41), you'll be prompted before trimming:

```
No confident match found (best score: 0.28). Show results anyway? [y/N]:
```

With `--no-trim`, low-confidence results are shown with a note instead of a prompt.

Options: `--results N`, `--output-dir DIR`, `--no-trim` to skip auto-trimming, `--threshold 0.5` to adjust the confidence cutoff, `--save-top N` to save the top N clips instead of just the best match. Backend and model are auto-detected from the index — pass `--backend` or `--model` only to override.

### Local Backend (no API key needed)

Index and search using a local Qwen3-VL-Embedding model instead of the Gemini API. Free, private, and runs entirely on your machine. For the best search quality, use the Gemini backend — the local 8B model is a solid alternative when you need offline/private search, and the 2B model is a fallback when hardware can't support 8B.

The model is **auto-detected from your hardware** — qwen8b for NVIDIA GPUs and Macs with 24 GB+ RAM, qwen2b for smaller Macs and CPU-only systems. You can override with `--model qwen2b` or `--model qwen8b`. Pick an install based on your hardware:

| Hardware | Install command | Auto-detected model | Notes |
|---|---|---|---|
| **Apple Silicon, 24 GB+ RAM** | `uv tool install ".[local]"` | qwen8b | Full float16 via MPS |
| **Apple Silicon, 16 GB RAM** | `uv tool install ".[local]"` | qwen2b | 8B won't fit; 2B uses ~6 GB |
| **Apple Silicon, 8 GB RAM** | `uv tool install ".[local]"` | qwen2b | Tight — may swap under load; Gemini API recommend