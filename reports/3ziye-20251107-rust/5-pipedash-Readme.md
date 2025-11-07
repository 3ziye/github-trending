<div align="center">
  <br>
  <img src="./app-icon.png" width="102px" alt="Pipedash Logo" />
  <h1>Pipedash</h1>
  <p>A desktop app for managing CI/CD pipelines from multiple providers </p>

</div>

<p align="center">
<div align="center">
<img src="./public/pipedashbg.png" alt="Pipedash Screenshot" style="box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3); border-radius: 8px;"/>
</div>
</p>

> **[WIP]** This is an work-in-progress project. It works for basic use cases but hasn't been thoroughly tested. Things might break, APIs might change, and there are probably bugs. Tested primarily on macOS – not sure if it works properly on Linux and Windows due to webview differences.

## About

Pipedash aggregates CI/CD pipelines from multiple providers into a single desktop interface. Instead of switching between GitHub Actions, GitLab CI, Buildkite, Jenkins, and Tekton dashboards, view everything in one place.

Built with Tauri, Rust, React, and TypeScript.

## Why

Most development teams use multiple CI/CD platforms over time. Open source projects often use GitHub Actions, internal services might run on GitLab CI or Buildkite, Kubernetes-native workloads use Tekton, and there's usually some Jenkins instance handling legacy systems. Checking everything means opening multiple tabs and manually refreshing.

This tool pulls pipeline data from different providers and shows it together.

## Supported Providers

- GitHub Actions
- GitLab CI
- Buildkite
- Jenkins
- Tekton CD

The plugin architecture allows adding more providers.

## What It Does

The app polls configured providers and displays pipelines organized by repository and workflow. Background refresh runs every X seconds (configurable per provider). When pipeline status changes, the UI updates automatically.

Main capabilities:
- View pipeline status across multiple providers
- Browse run history with commit info and execution times
- Trigger workflows with parameters dynamically loaded from each provider
- Re-run previous executions with the same parameters
- Cancel running builds
- Multiple instances of the same provider type

When triggering or re-running a workflow, the app fetches available parameters directly from the provider plugin (workflow inputs for GitHub Actions, pipeline variables for GitLab CI, build parameters for Jenkins and Buildkite, etc.) and displays them in a form.

**Privacy First**

Everything runs locally on the machine. The app only connects to configured CI/CD providers – no analytics, telemetry, or third-party services. Pipeline data is stored in a local SQLite database and API tokens are encrypted in the system keyring.

## Installation

Download the latest release for your platform from the [releases page](https://github.com/hcavarsan/pipedash/releases).

Available for macOS, Windows, and Linux.

## Setup

Launch the app and add a provider via the sidebar. Each provider needs an API token:

**GitHub Actions**: Personal Access Token with `repo` and `workflow` scopes. Optionally set a custom base URL for GitHub Enterprise.

**GitLab CI**: Personal Access Token with `api` scope. Supports both GitLab.com and self-hosted instances.

**Buildkite**: API Access Token with read permissions and the organization slug.

**Jenkins**: API token, username, and server URL.

**Tekton CD**: Kubernetes config file path and context. Automatically detects namespaces with Tekton pipelines.

After adding a provider, the app validates credentials and fetches available repositories. Select which ones to monitor and save. Pipelines will appear in the main view and refresh automatically.

## How It Works

**Store**

Provider configurations are stored in a local SQLite database. Tokens are kept separate in the system keyring.

Each provider has its own refresh interval (default: 30 seconds), adjustable based on API rate limits.



**Plugin System**

Each CI/CD provider is implemented as a plugin that exposes a common interface. The core application doesn't know the specifics of how GitHub Actions, GitLab CI, Buildkite, Jenkins, or Tekton work—it just calls standard methods like `fetch_pipelines()` or `trigger_pipeline()` and the plugin handles the details.

Plugins are compiled into the application at build time, not loaded dynamically at runtime. This keeps things simpler and avoids the security concerns of runtime plugin loading.

When the app starts, it loads cached pipeline data from SQLite immediately. In the background, a refresh loop polls each provider's API and updates the cache when changes are detected. The frontend listens for events and re-renders when new data arrives.

## Adding Providers

To add support for a new CI/CD platform, create a new crate in `crates/pipedash-plugin-{name}/` and implement the `Plugin` trait from `pipedash-plugin-api`. The trait defines methods for fetching pipelines, validating credentials, triggering builds, and retrieving run history.

Each plugin should follow this structure:
- `schema.rs` - Table and column definitions speci