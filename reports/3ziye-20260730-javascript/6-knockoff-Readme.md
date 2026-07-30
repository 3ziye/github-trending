![Knockoff: Amazon, without the knockoffs](store-assets/promo-og.png)

# Knockoff

**A browser extension that filters pseudo-brand junk out of Amazon.** Buy from
real, established brands, even when that means paying more.

Amazon is flooded with trademark-squat "brands" (SZHLUX, HORUSDY, LATTOOK,
DOZAWA...): random strings registered at the USPTO purely to unlock Amazon
Brand Registry, selling commodity goods with no company, no warranty, and no
reputation behind them. Knockoff detects those listings and hides, dims, or
labels them, right in the search results.

> [!NOTE]
> **This is a frozen public snapshot.** Active development has moved to a
> private repository, and future versions are no longer built in the open — so
> nothing here phones home. Loaded as-is, this build makes **zero calls to any
> Knockoff server**: it runs entirely on the brand lists bundled in the repo,
> and it won't receive further updates. For the maintained, auto-updating
> extension, install from the stores below. To run the fully local build
> yourself, see [Self-contained by default](#self-contained-by-default).

## Install

**[Add to Chrome](https://chromewebstore.google.com/detail/pjgickchbiikhdfpmecaabkphmofpdce)** from the Chrome Web Store, or
**[Add to Firefox](https://addons.mozilla.org/en-US/firefox/addon/knockoff-amazon-brand-filter/)** from Firefox Add-ons.

Or run the fully local build straight from this repo:

1. Clone this repo
2. Open `chrome://extensions`
3. Turn on **Developer mode** (top right)
4. Click **Load unpacked** and select the repo folder

Works on every Amazon marketplace, with no server behind it.

### Safari

Safari requires the extension to be wrapped in a native app. Open
[`safari/Knockoff/Knockoff.xcodeproj`](safari/Knockoff) in Xcode, run the
**Knockoff** scheme, then enable Knockoff in Safari → Settings →
Extensions. For unsigned local builds, first check "Allow unsigned
extensions" in Safari's Develop menu.

The Xcode project carries its own copy of the extension files; after
editing the extension, run [`scripts/sync-safari.sh`](scripts/sync-safari.sh)
to update it before rebuilding.

## Press

Some of the coverage since launch:

- [Fast Company](https://www.fastcompany.com/91570721/amazon-shopping-slop-viral-new-tool-filters-out-knockoff-brands)
- [Gizmodo](https://gizmodo.com/new-browser-extension-helps-you-dodge-amazons-sea-of-knock-off-products-2000783054)
- [404 Media](https://www.404media.co/knockoff-browser-extension-hides-sketchy-brands-on-amazon/)
- [PC Gamer](https://www.pcgamer.com/hardware/this-chrome-extension-hides-knockoff-brands-on-amazon-sorry-to-brands-like-wnpethome-eheyciga-yxy/)
- [Yahoo](https://tech.yahoo.com/apps/articles/chrome-extension-removes-unknown-brands-162002361.html)
- [Lifehacker](https://lifehacker.com/tech/knockoff-browser-extension-hides-shady-items-on-amazon)

## How it works

Everything runs locally in a content script. No accounts, no tracking, no
network requests of any kind. Each product tile's brand is
resolved through this pipeline (first match wins):

| # | Check | Verdict |
|---|-------|---------|
| 1 | Your allowlist | `allowed`, never filtered |
| 2 | Your blocklist | `blocked`, always filtered |
| 3 | Seed list of notorious pseudo-brands ([`data/flagged-brands.js`](data/flagged-brands.js)) | `flagged` |
| 4 | Established Chinese-owned brands ([`data/chinese-major.js`](data/chinese-major.js)) | `known`, or `flagged` if you enable that setting |
| 5 | ~5,000 established brands ([`data/known-brands.js`](data/known-brands.js) + the bundled community allowlist in [`data/community-brands.js`](data/community-brands.js)) | `known` |
| 6 | Name heuristics (see below) | `flagged` / `suspect` / `unknown` |
| - | No brand at the front of the title at all | `unbranded` |

### Name heuristics

Unknown brands are scored on the linguistic signature of trademark-squat
names: ALL-CAPS 5–9 character strings, vanishing vowel ratios,
unpronounceable consonant runs, un-English letter pairs, non-Latin
characters, random iNternal caPitalization. High scores are `flagged`,
mid scores `suspect`. The known-brands list always vetoes the heuristics:
plenty of real brands (ASICS, RYOBI, HOKA) would otherwise look suspicious.
Scoring lives in [`src/detector.js`](src/detector.js) and is deliberately
readable, and easy to tune for your own build.

### Filter levels

| Level | Filters |
|-------|---------|
| **Relaxed** | Known pseudo-brands + your blocklist |
| **Standard** (default) | + suspect-looking names + unbranded listings |
| **Strict** | + anything not on a known-brands list (allowlist-only) |

### Actions

Filtered items can be **hidden** (with a floating pill showing the count and
a one-click reveal), **dimmed** (fade + desaturate, restore on hover), or
just **labeled**. Every badge is clickable: trust the brand, block it, show
the item once, or report a misclassification.

Product detail pages get a verdict chip next to the brand byline. The page
is never hidden out