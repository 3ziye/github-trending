# Smaug 🐉

Archive your Twitter/X bookmarks (and/or optionally, likes) to markdown. Automatically.

*Like a dragon hoarding treasure, Smaug collects the valuable things you bookmark and like.*

## Contents

- [Quick Start](#quick-start-5-minutes)
- [Getting Twitter Credentials](#getting-twitter-credentials)
- [What It Does](#what-it-does)
- [Running](#running)
- [Categories](#categories)
- [Automation](#automation)
- [Output](#output)
- [Configuration](#configuration)
- [Claude Code Integration](#claude-code-integration)
- [Troubleshooting](#troubleshooting)
- [Credits](#credits)

```
  🔥  🔥  🔥  🔥  🔥  🔥  🔥  🔥  🔥  🔥  🔥  🔥
       _____ __  __   _   _   _  ____
      / ____|  \/  | / \ | | | |/ ___|
      \___ \| |\/| |/ _ \| | | | |  _
       ___) | |  | / ___ \ |_| | |_| |
      |____/|_|  |_/_/  \_\___/ \____|

   🐉 The dragon stirs... treasures to hoard!
```

## Quick Start (5 minutes)

```bash
# 1. Install bird CLI (Twitter API wrapper)
# See https://github.com/steipete/bird for installation

# 2. Clone and install Smaug
git clone https://github.com/alexknowshtml/smaug
cd smaug
npm install

# 3. Run the setup wizard
npx smaug setup

# 4. Run the full job (fetch + process with Claude)
npx smaug run
```

The setup wizard will:
- Create required directories
- Guide you through getting Twitter credentials
- Create your config file

## Manually Getting Twitter Credentials

Smaug uses the bird CLI which needs your Twitter session cookies.

If you don't want to use the wizard to make it easy, you can manually put your session info into the config.

1. Copy the example config:
   ```bash
   cp smaug.config.example.json smaug.config.json
   ```
2. Open Twitter/X in your browser
3. Open Developer Tools → Application → Cookies
4. Find and copy these values:
   - `auth_token`
   - `ct0`
5. Add them to your `smaug.config.json`:

```json
{
  "twitter": {
    "authToken": "your_auth_token_here",
    "ct0": "your_ct0_here"
  }
}
```

> **Note:** `smaug.config.json` is gitignored to prevent accidentally committing credentials. The example file is tracked instead.

## What Smaug Actually Does

1. **Fetches bookmarks** from Twitter/X using the bird CLI (can also fetch likes, or both)
2. **Expands t.co links** to reveal actual URLs
3. **Extracts content** from linked pages (GitHub repos, articles, quote tweets)
4. **Invokes Claude Code** to analyze and categorize each tweet
5. **Saves to markdown** organized by date with rich context
6. **Files to knowledge library** - GitHub repos to `knowledge/tools/`, articles to `knowledge/articles/`

## Running Manually

```bash
# Full job (fetch + process with Claude)
npx smaug run

# Fetch from bookmarks (default)
npx smaug fetch 20

# Fetch ALL bookmarks (paginated - requires bird CLI from git)
npx smaug fetch --all
npx smaug fetch --all --max-pages 5  # Limit to 5 pages

# Fetch from likes instead
npx smaug fetch --source likes

# Fetch from both bookmarks AND likes
npx smaug fetch --source both

# Process already-fetched tweets
npx smaug process

# Force re-process (ignore duplicates)
npx smaug process --force

# Check what's pending
node -e "console.log(require('./.state/pending-bookmarks.json').count)"
```

### Fetching All Bookmarks

By default, Twitter's API returns ~50-70 bookmarks per request. To fetch more, use the `--all` flag which enables pagination:

```bash
npx smaug fetch --all              # Fetch all (up to 10 pages)
npx smaug fetch --all --max-pages 20  # Fetch up to 20 pages
```

**Note:** This requires bird CLI built from git (not the npm release). See [Troubleshooting](#troubleshooting) for installation instructions.

**Cost warning:** Processing large bookmark backlogs can consume significant Claude tokens. Each bookmark with content-heavy links (long articles, GitHub READMEs, etc.) adds to the context. Process in batches to control costs:

```bash
npx smaug run --limit 50 -t    # Process 50 at a time with token tracking
```

Use the `-t` flag to monitor usage. See [Token Usage Tracking](#token-usage-tracking) for cost estimates by model.

## Categories

Categories define how different bookmark types are handled. Smaug comes with sensible defaults, but you can customize them in `smaug.config.json`.

### Default Categories

| Category | Matches | Action | Destination |
|----------|---------|--------|-------------|
| **article** | blogs, news sites, papers, medium.com, substack, etc | file | `./knowledge/articles/` |
| **github** | github.com | file | `./knowledge/tools/` |
| **tweet** | (fallback) | capture | bookmarks.md only |

🔜 _Note: Transcription coming soon for podcasts, videos, etc but feel free to edit your own and submit back suggestions!_

### Actions

- **file**: Create a separate markdown file with rich metadata
- **capture**: Add to bookmarks.md only (no separate file)
- **transcribe**: Flag for future transcription *(auto-transcription coming soon! PRs welcome)*

### Custom Categories

Add your own categories in `smaug.config.json`:

```json
{
  "c