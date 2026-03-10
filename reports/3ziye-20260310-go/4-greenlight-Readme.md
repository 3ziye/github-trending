# greenlight

**Know before you submit.** Pre-submission compliance scanner for the Apple App Store.

Greenlight scans your app — source code, privacy manifests, IPA binaries, and App Store Connect metadata — against Apple's Review Guidelines, catching rejection risks before Apple does.

## Install

```bash
# Homebrew (macOS)
brew install revylai/tap/greenlight

# Go
go install github.com/RevylAI/greenlight/cmd/greenlight@latest

# Build from source
git clone https://github.com/RevylAI/greenlight.git
cd greenlight && make build
# Binary at: build/greenlight
```

## Quick Start

```bash
# Run EVERYTHING on your project — one command, zero uploads
greenlight preflight /path/to/your/project

# Include IPA for binary analysis
greenlight preflight . --ipa build.ipa
```

That's it. You get a full report in under a second.

## Commands

### `greenlight preflight [path]` — The one command to run

Runs all scanners in parallel. No account needed. Entirely offline.

```bash
greenlight preflight .                          # scan current directory
greenlight preflight ./my-app --ipa build.ipa   # with binary inspection
greenlight preflight . --format json            # JSON output for CI/CD
greenlight preflight . --output report.json     # write to file
```

**Scanners included:**

| Scanner | Checks |
|---------|--------|
| **metadata** | app.json / Info.plist: name, version, bundle ID format, icon, privacy policy URL, purpose strings |
| **codescan** | 30+ code patterns: private APIs, secrets, payment violations, missing ATT, social login, placeholders |
| **privacy** | PrivacyInfo.xcprivacy completeness, Required Reason APIs, tracking SDKs vs ATT implementation |
| **ipa** | Binary: Info.plist keys, launch storyboard, app icons, app size, framework privacy manifests |

### `greenlight codescan [path]` — Code pattern scan

```bash
greenlight codescan /path/to/project
```

Scans Swift, Objective-C, React Native, and Expo projects for:
- Private API usage (§2.5.1) — **CRITICAL**
- Hardcoded secrets/API keys (§1.6) — **CRITICAL**
- External payment for digital goods (§3.1.1) — **CRITICAL**
- Dynamic code execution (§2.5.2) — **CRITICAL**
- Cryptocurrency mining (§3.1.5) — **CRITICAL**
- Missing Sign in with Apple when using social login (§4.8)
- Missing Restore Purchases for IAP (§3.1.1)
- Missing ATT for ad/tracking SDKs (§5.1.2)
- Account creation without deletion option (§5.1.1)
- Placeholder content in strings (§2.1)
- References to competing platforms (§2.3)
- Hardcoded IPv4 addresses (§2.5)
- Insecure HTTP URLs (§1.6)
- Vague Info.plist purpose strings (§5.1.1)
- Expo config issues (§2.1)

### `greenlight privacy [path]` — Privacy manifest validator

```bash
greenlight privacy /path/to/project
```

Deep privacy compliance scan:
- PrivacyInfo.xcprivacy exists and is properly configured
- Required Reason APIs detected in code vs declared in manifest
- Tracking SDKs detected vs ATT implementation
- Cross-references everything automatically

### `greenlight ipa <path.ipa>` — Binary inspector

```bash
greenlight ipa /path/to/build.ipa
```

Inspects a built IPA for:
- PrivacyInfo.xcprivacy presence
- Info.plist completeness and purpose string quality
- App Transport Security configuration
- App icon presence and sizes
- Launch storyboard presence
- App size vs 200MB cellular download limit
- Embedded framework privacy manifests

### `greenlight scan --app-id <ID>` — App Store Connect checks

```bash
greenlight auth setup                    # one-time: configure API key
greenlight auth login                    # or: sign in with Apple ID
greenlight scan --app-id 6758967212     # run all tiers
```

API-based checks against your app in App Store Connect:
- Metadata completeness (descriptions, keywords, URLs)
- Screenshot verification for required device sizes
- Build processing status
- Age rating and encryption compliance
- Content analysis (platform references, placeholders)

### `greenlight guidelines` — Browse Apple's guidelines

```bash
greenlight guidelines list               # all sections
greenlight guidelines show 2.1           # specific guideline
greenlight guidelines search "privacy"   # full-text search
```

### Output formats

All scan commands support:

```bash
--format terminal   # colored terminal output (default)
--format json       # JSON for CI/CD pipelines
--output file.json  # write to file instead of stdout
```

## Claude Code Skill

Greenlight works as a Claude Code skill for AI-assisted compliance fixing. Claude runs the scan, reads the output, fixes every issue in your code, and re-runs until GREENLIT.

### Setup

Add the SKILL.md to your project's `.claude/` directory or install as a plugin:

```bash
# Copy skill file into your project
mkdir -p .claude/skills
cp /path/to/greenlight/SKILL.md .claude/skills/greenlight.md

# Or reference it in your CLAUDE.md
echo "See greenlight skill: /path/to/greenlight/SKILL.md" >> CLAUDE.md
```

Then tell Claude: *"Run greenlight preflight and fix everything unti