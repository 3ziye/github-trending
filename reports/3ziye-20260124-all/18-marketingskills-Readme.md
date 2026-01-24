# Marketing Skills for Claude Code

A collection of AI agent skills focused on marketing tasks. Built for technical marketers and founders who want Claude Code (or similar AI coding assistants) to help with conversion optimization, copywriting, SEO, analytics, and growth engineering.

Built by [Corey Haines](https://corey.co?ref=marketingskills). Need hands-on help? Check out [Conversion Factory](https://conversionfactory.co?ref=marketingskills) — Corey's agency for conversion optimization, landing pages, and growth strategy. Want to learn more about marketing? Subscribe to [Swipe Files](https://swipefiles.com?ref=marketingskills).

**Contributions welcome!** Found a way to improve a skill or have a new one to add? [Open a PR](#contributing).

## What are Skills?

Skills are markdown files that give AI agents specialized knowledge and workflows for specific tasks. When you add these to your project, Claude Code can recognize when you're working on a marketing task and apply the right frameworks and best practices.

## Available Skills

| Skill | Description | Triggers |
|-------|-------------|----------|
| [ab-test-setup](skills/ab-test-setup/) | Plan and implement A/B tests | "A/B test," "split test," "experiment" |
| [analytics-tracking](skills/analytics-tracking/) | Set up tracking and measurement | "tracking," "GA4," "GTM," "events" |
| [competitor-alternatives](skills/competitor-alternatives/) | Competitor comparison and alternative pages | "vs page," "alternative page," "[X] vs [Y]" |
| [copy-editing](skills/copy-editing/) | Edit and polish existing copy | "edit this copy," "review my copy," "copy sweep" |
| [copywriting](skills/copywriting/) | Write or improve marketing copy | "write copy," "rewrite," "headlines," "CTA copy" |
| [email-sequence](skills/email-sequence/) | Build email sequences and drip campaigns | "email sequence," "drip campaign," "nurture" |
| [form-cro](skills/form-cro/) | Optimize lead capture and contact forms | "form optimization," "lead form," "contact form" |
| [free-tool-strategy](skills/free-tool-strategy/) | Plan engineering-as-marketing tools | "free tool," "calculator," "lead gen tool" |
| [launch-strategy](skills/launch-strategy/) | Product launches and feature announcements | "launch," "Product Hunt," "feature release" |
| [marketing-ideas](skills/marketing-ideas/) | 140 SaaS marketing ideas and strategies | "marketing ideas," "growth ideas," "how to market" |
| [marketing-psychology](skills/marketing-psychology/) | 70+ mental models for marketing | "psychology," "mental models," "cognitive bias" |
| [onboarding-cro](skills/onboarding-cro/) | Improve user activation and onboarding | "onboarding," "activation," "first-run experience" |
| [page-cro](skills/page-cro/) | Conversion optimization for any marketing page | "optimize [page]," "CRO," "page isn't converting" |
| [paid-ads](skills/paid-ads/) | Create and optimize paid ad campaigns | "PPC," "Google Ads," "Meta ads," "paid media" |
| [paywall-upgrade-cro](skills/paywall-upgrade-cro/) | In-app paywalls and upgrade screens | "paywall," "upgrade screen," "feature gate" |
| [popup-cro](skills/popup-cro/) | Create/optimize popups and modals | "popup," "modal," "exit intent" |
| [pricing-strategy](skills/pricing-strategy/) | Design pricing, packaging, and monetization | "pricing," "tiers," "freemium," "willingness to pay" |
| [programmatic-seo](skills/programmatic-seo/) | Build SEO pages at scale | "programmatic SEO," "template pages," "pages at scale" |
| [referral-program](skills/referral-program/) | Design referral and affiliate programs | "referral," "affiliate," "word of mouth," "viral" |
| [schema-markup](skills/schema-markup/) | Add structured data and rich snippets | "schema," "JSON-LD," "structured data" |
| [seo-audit](skills/seo-audit/) | Audit technical and on-page SEO | "SEO audit," "technical SEO," "not ranking" |
| [signup-flow-cro](skills/signup-flow-cro/) | Optimize signup and registration flows | "signup optimization," "registration form" |
| [social-content](skills/social-content/) | Create and schedule social media content | "LinkedIn post," "Twitter thread," "social media" |

## Installation

### Option 1: CLI Install (Recommended)

Use [add-skill](https://github.com/vercel-labs/add-skill) to install skills directly:

```bash
# Install all skills
npx add-skill coreyhaines31/marketingskills

# Install specific skills
npx add-skill coreyhaines31/marketingskills --skill page-cro copywriting

# List available skills
npx add-skill coreyhaines31/marketingskills --list
```

This automatically installs to your `.claude/skills/` directory.

### Option 2: Claude Code Plugin

Install via Claude Code's built-in plugin system:

```bash
# Add the marketplace
/plugin marketplace add coreyhaines31/marketingskills

# Install all marketing skills
/plugin install marketing-skills
```

### Option 3: Clone and Copy

Clone the entire repo and copy the skills folder:

```bash
git clone https://github.com/coreyhaines31/market