# twitter-cli

[![CI](https://github.com/jackwener/twitter-cli/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/jackwener/twitter-cli/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/twitter-cli.svg)](https://pypi.org/project/twitter-cli/)
[![Python](https://img.shields.io/badge/python-%3E%3D3.10-blue.svg)](https://pypi.org/project/twitter-cli/)

A terminal-first CLI for Twitter/X: read timelines, bookmarks, and user profiles without API keys.

## More Tools

- [xiaohongshu-cli](https://github.com/jackwener/xiaohongshu-cli) — Xiaohongshu (小红书) CLI for notes and account workflows
- [bilibili-cli](https://github.com/jackwener/bilibili-cli) — Bilibili CLI for videos, users, search, and feeds
- [discord-cli](https://github.com/jackwener/discord-cli) — Discord CLI for local-first sync, search, and export
- [tg-cli](https://github.com/jackwener/tg-cli) — Telegram CLI for local-first sync, search, and export

[English](#english) | [中文](#中文)

## English

### Features

**Read:**
- Timeline: fetch `for-you` and `following` feeds
- Bookmarks: list saved tweets from your account
- Search: find tweets by keyword with Top/Latest/Photos/Videos tabs
- Tweet detail: view a tweet and its replies; use `show <N>` to open tweet #N from the last list output
- Article: fetch a Twitter Article and export it as Markdown
- List timeline: fetch tweets from a Twitter List
- User lookup: fetch user profile, tweets, likes, followers, and following
- `--full-text`: disable tweet text truncation in rich table output
- Structured output: export any data as YAML or JSON for scripting and AI agent integration
- Optional scoring filter: rank tweets by engagement weights
- Structured output contract: [SCHEMA.md](./SCHEMA.md)

> **AI Agent Tip:** Prefer `--yaml` for structured output unless a strict JSON parser is required. Non-TTY stdout defaults to YAML automatically. Use `--max` to limit results.

**Write:**
- Post: create new tweets and replies, with optional image attachments (up to 4)
- Quote: quote-tweet with optional images
- Delete: remove your own tweets
- Like / Unlike: manage tweet likes
- Retweet / Unretweet: manage retweets
- Bookmark: bookmark/unbookmark (`favorite/unfavorite` kept as compatibility aliases)
- Write commands also support explicit `--json` / `--yaml` output now

**Auth & Anti-Detection:**
- Cookie auth: use browser cookies or environment variables
- Full cookie forwarding: extracts ALL browser cookies for richer browser context
- TLS fingerprint impersonation: `curl_cffi` with dynamic Chrome version matching
- `x-client-transaction-id` header generation
- Request timing jitter to avoid pattern detection
- Write operation delays (1.5–4s random) to mitigate rate limits
- Proxy support via `TWITTER_PROXY` environment variable

### Installation

```bash
# Recommended: uv tool (fast, isolated)
uv tool install twitter-cli

# Alternative: pipx
pipx install twitter-cli
```

Upgrade to the latest version:

```bash
uv tool upgrade twitter-cli
# Or: pipx upgrade twitter-cli
```

> **Tip:** Upgrade regularly to avoid unexpected errors from outdated API handling.

Install from source:

```bash
git clone git@github.com:jackwener/twitter-cli.git
cd twitter-cli
uv sync
```

### Quick Start

```bash
# Fetch home timeline (For You)
twitter feed

# Fetch Following timeline
twitter feed -t following

# Enable ranking filter explicitly
twitter feed --filter
```

### Usage

```bash
# Feed
twitter feed --max 50
twitter feed --full-text
twitter feed --output tweets.json
twitter feed --input tweets.json
twitter feed --json                    # Structured stdout for scripts/agents

# Bookmarks
twitter bookmarks
twitter bookmarks --full-text
twitter bookmarks --max 30 --yaml

# Search
twitter search "Claude Code"
twitter search "AI agent" -t Latest --max 50
twitter search "AI agent" --full-text
twitter search "机器学习" --yaml
twitter search "python" --from elonmusk --lang en --since 2026-01-01
twitter search --from bbc --exclude retweets --has links
twitter search "topic" -o results.json         # Save to file
twitter search "trending" --filter              # Apply ranking filter

# Tweet detail (view tweet + replies)
twitter tweet 1234567890
twitter tweet 1234567890 --full-text
twitter tweet https://x.com/user/status/1234567890

# Open tweet by index from last list output
twitter show 2                         # Open tweet #2 from last feed/search
twitter show 2 --full-text             # Full text in reply table
twitter show 2 --json                  # Structured output

# Twitter Article
twitter article 1234567890
twitter article https://x.com/user/article/1234567890 --json
twitter article 1234567890 --markdown
twitter article 1234567890 --output article.md

# List timeline
twitter list 1539453138322673664
twitter list 1539453138322673664 --full-text

# User
twitter user elonmusk
twitter user-posts elonmusk --max 20
twitter user-posts elonmusk --full-text
twitter user-posts elonmusk -o tweets.json
twitter