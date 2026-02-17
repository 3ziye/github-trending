# Unofficial App Store Connect CLI

<p align="center">
  <a href="https://github.com/rudrankriyam/App-Store-Connect-CLI/releases/latest"><img src="https://img.shields.io/github/v/release/rudrankriyam/App-Store-Connect-CLI?style=for-the-badge&color=blue" alt="Latest Release"></a>
  <a href="https://github.com/rudrankriyam/App-Store-Connect-CLI/stargazers"><img src="https://img.shields.io/github/stars/rudrankriyam/App-Store-Connect-CLI?style=for-the-badge" alt="GitHub Stars"></a>
  <img src="https://img.shields.io/badge/Go-1.26+-00ADD8?style=for-the-badge&logo=go" alt="Go Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Homebrew-compatible-blue?style=for-the-badge" alt="Homebrew">
  <img src="https://img.shields.io/github/downloads/rudrankriyam/App-Store-Connect-CLI/total?style=for-the-badge&color=green" alt="Downloads">
</p>

A **fast**, **lightweight**, and **scriptable** CLI for the [App Store Connect API](https://developer.apple.com/app-store-connect/api/). Automate your iOS, macOS, tvOS, and visionOS app workflows from your terminal, IDE, or CI/CD pipeline. A modern **fastlane alternative** built as a single Go binary.

### Features

- **TestFlight** -- manage builds, beta groups, testers, feedback, and crash reports
- **App Store submissions** -- versions, localizations, screenshots, review submissions, and phased releases
- **Builds** -- upload IPAs/PKGs, expire old builds, manage build metadata
- **Signing** -- certificates, provisioning profiles, bundle IDs, and capabilities
- **Subscriptions & IAP** -- create and manage subscriptions, in-app purchases, offer codes, and pricing
- **Analytics & Sales** -- download sales reports, analytics data, and finance reports
- **Xcode Cloud** -- trigger workflows, monitor build runs, download artifacts
- **Notarization** -- submit, poll, and retrieve logs for macOS notarization
- **Game Center** -- achievements, leaderboards, leaderboard sets, and localizations
- **Screenshots & Previews** -- upload, frame, and manage App Store media assets
- **Webhooks** -- create and manage App Store Connect webhooks
- **Agent-friendly** -- JSON-first output, explicit flags, no interactive prompts, clean exit codes

## Why ASC?

| Problem | Solution |
|---------|----------|
| Manual App Store Connect work | Automate everything from CLI |
| Slow, heavy tooling | Single Go binary, instant startup |
| Poor scripting support | JSON output, explicit flags, clean exit codes |

## Table of Contents

- [Features](#features)
- [Why ASC?](#why-asc)
- [Quick Start](#quick-start)
  - [Install](#install)
  - [Authenticate](#authenticate)
- [Commands](#commands)
  - [Scripting Tips](#scripting-tips)
  - [TestFlight](#testflight)
  - [Beta Groups](#beta-groups)
  - [Beta Testers](#beta-testers)
  - [Devices](#devices)
  - [App Store](#app-store)
  - [App Tags](#app-tags)
  - [App Events](#app-events)
  - [Alternative Distribution](#alternative-distribution)
  - [Analytics & Sales](#analytics--sales)
  - [Finance Reports](#finance-reports)
  - [Sandbox Testers](#sandbox-testers)
  - [Xcode Cloud](#xcode-cloud)
  - [Notarization](#notarization)
  - [Game Center](#game-center)
  - [Signing](#signing)
  - [Certificates](#certificates)
  - [Profiles](#profiles)
  - [Bundle IDs](#bundle-ids)
  - [Subscriptions](#subscriptions)
  - [In-App Purchases](#in-app-purchases)
  - [Performance](#performance)
  - [Webhooks](#webhooks)
  - [Publish (End-to-End Workflows)](#publish-end-to-end-workflows)
  - [App Clips](#app-clips)
  - [Encryption](#encryption)
  - [Screenshots & Video Previews](#screenshots--video-previews)
  - [Background Assets](#background-assets)
  - [Routing Coverage](#routing-coverage)
  - [Notify](#notify)
  - [Apps & Builds](#apps--builds)
- [App Setup](#app-setup)
  - [Categories](#categories)
  - [Offer Codes (Subscriptions)](#offer-codes-subscriptions)
  - [Versions](#versions)
  - [App Info](#app-info)
  - [Pre-Release Versions](#pre-release-versions)
  - [Localizations](#localizations)
  - [Build Localizations](#build-localizations)
  - [Migrate (Fastlane Compatibility)](#migrate-fastlane-compatibility)
  - [Validate (Pre-Submission)](#validate-pre-submission)
  - [Submit](#submit)
  - [Utilities](#utilities)
  - [Output Formats](#output-formats)
  - [Authentication](#authentication)
- [Design Philosophy](#design-philosophy)
  - [Explicit Over Cryptic](#explicit-over-cryptic)
  - [JSON-First Output](#json-first-output)
  - [No Interactive Prompts](#no-interactive-prompts)
- [Installation](#installation)
- [Documentation](#documentation)
- [How to test in <10 minutes](#how-to-test-in-10-minutes)
- [Security](#security)
- [ASC Skills](#asc-skills)
- [Wall of Apps](#wall-of-apps)
- [Acknowledgements](#acknowledgements)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
- [Star History](#star-history)

## Quick Start

### Install

```bash
# Via Homebrew (recommende