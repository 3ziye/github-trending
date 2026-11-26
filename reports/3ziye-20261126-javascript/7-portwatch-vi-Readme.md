# PortWatch VI

**Does GTA VI run on PC yet?** A static GitHub Pages site that tracks every serious community effort to recompile, emulate or port the leaked Xbox Series build of GTA VI to PC. All efforts are scored on one ladder, and a scout refreshes the data every 3 hours.

- One headline progress bar shows the closest effort, with the top projects pinned to it.
- A live countdown runs to the missing executable's expected drop.
- A leaderboard card per effort shows its own bar, milestone ladder, groundwork breakdown, what works and what's blocking.
- Further sections cover the watchlist of early projects, a toolkit of asset tools, the scout's inbox of new candidates, and fake-download warnings.

No game files, keys or executables are hosted or linked, ever.

## Deploy on GitHub Pages

1. Create a new GitHub repository and push this folder to its `main` branch.
2. In the repo, open **Settings → Pages** and set **Source** to **GitHub Actions**.
3. Open **Settings → Actions → General** and make sure workflows are allowed.
4. Open **Actions → Scout → Run workflow** to run the first scout. It commits fresh data and deploys the site.

Each deploy also runs `scripts/build-site.mjs`, which turns `data/tracker.json` into pages search engines can read: one page per news story (`news/<id>.html`), a news archive, an RSS feed (`news/feed.xml`) and `sitemap.xml`. It then pings [IndexNow](https://www.indexnow.org/) (Bing, Yandex and others; no account needed) with the URLs that changed since the last deploy. For Google, add the site in Search Console and submit `sitemap.xml`.

From then on, `Scout` runs every 3 hours (00:17, 03:17, 06:17 … UTC) on GitHub's servers, so no computer of yours needs to be on. Any push to `main` redeploys the site through `Deploy site`. To change the frequency, edit the `cron` line in `.github/workflows/scout.yml`. For example, `17 6 * * *` runs it once a day. GitHub can delay scheduled runs by a few minutes when it's busy.

## What the scout does (`scripts/scout.mjs`)

1. **Refreshes** every tracked repo: stars, forks, issues, last push, commits in the last 7 days, and whether it's gone (404, or 451 for a DMCA block). It also hashes each README to notice changes.
2. **Spots claims.** If a README newly says GTA VI boots, reaches the menu or runs at some FPS, the card shows an "unverified claim" banner and the change feed records it.
3. **Discovers** new repos from GitHub and GitLab searches (`scout.queries` in `data/tracker.json`), Hacker News, Bluesky, Mastodon, Lemmy and 4chan, plus Reddit and X when keys are set, by pulling GitHub links out of posts. It also gathers **headlines** from the Google News and Bing News feeds, keeping only stories about the leak, ports, takedowns, scams or official news. And it **watches GitHub's public DMCA log** for new Take-Two or Rockstar notices, flagging any tracked project they name. On 4chan it uses the free read-only API, at one request per second. It opens only /v/ threads that mention GTA VI together with port terms (recomp, emulator, leak, executable, GitHub…), plus /vg/'s /gtag/ and /emugen/ generals. Change the boards with `scout.chan.boards`. Nothing from 4chan is shown on the site except, indirectly, repo names that pass every filter.
4. **Filters out spam** such as clone networks, download lures and "PC installer" repos. Their names are counted under *There is no download*, never linked.
5. **Filters out copies.** Re-uploads of tracked projects are flagged when they reuse a tracked project's name or have a README that is 60% or more identical, renamed copies included. Original fan games and repos without a real README are skipped too. Candidates already waiting are re-checked every run.
6. **Scores substance** from code language, size, technical depth, status tables, tests and commit activity. Repos with real code go to **New candidates**, shown as plain text and not linked until reviewed. Thin or off-topic ones are remembered and skipped.
7. **Writes news** (needs `ANTHROPIC_API_KEY`). Claude searches the web for takedowns, bans, confirmed leaks, legal news, scams and official announcements, then writes up to two short original articles. It runs at most every 11 hours, not on every 3-hourly scout run, to keep costs down. A source is kept only if it came up in Claude's own search. Each article's image is the source's preview image, credited and linked back; it falls back to a generated cover.
8. **Records** a change feed, the day's leader score for the sparkline, and a run summary.

### Optional secrets (Settings → Secrets and variables → Actions)

| Secret | What it enables |
|---|---|
| `ANTHROPIC_API_KEY` | **Claude review.** When a tracked README changes, or a new candidate shows up, Claude (`claude-opus-5-5`) reads the README and recent commits and re-scores the effort. It also promotes or rejects candidates automatically. Guardrails clamp the output: a GTA VI milestone only counts if Claude quotes text that really appears in the repo, and