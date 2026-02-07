# GitHub Copilot CLI SDKs

![GitHub Copilot SDK](./assets/RepoHeader_01.png)

[![NPM Downloads](https://img.shields.io/npm/dm/%40github%2Fcopilot-sdk?label=npm)](https://www.npmjs.com/package/@github/copilot-sdk)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/github-copilot-sdk?label=PyPI)](https://pypi.org/project/github-copilot-sdk/)
[![NuGet Downloads](https://img.shields.io/nuget/dt/GitHub.Copilot.SDK?label=NuGet)](https://www.nuget.org/packages/GitHub.Copilot.SDK)

Agents for every app.

Embed Copilot's agentic workflows in your application—now available in Technical preview as a programmable SDK for Python, TypeScript, Go, and .NET.

The GitHub Copilot SDK exposes the same engine behind Copilot CLI: a production-tested agent runtime you can invoke programmatically. No need to build your own orchestration—you define agent behavior, Copilot handles planning, tool invocation, file edits, and more.

## Available SDKs

| SDK                      | Location                                          | Installation                              |
| ------------------------ | ------------------------------------------------- | ----------------------------------------- |
| **Node.js / TypeScript** | [`cookbook/nodejs/`](https://github.com/github/awesome-copilot/blob/main/cookbook/copilot-sdk/nodejs/README.md) | `npm install @github/copilot-sdk`         |
| **Python**               | [`cookbook/python/`](https://github.com/github/awesome-copilot/blob/main/cookbook/copilot-sdk/python/README.md) | `pip install github-copilot-sdk`          |
| **Go**                   | [`cookbook/go/`](https://github.com/github/awesome-copilot/blob/main/cookbook/copilot-sdk/go/README.md)         | `go get github.com/github/copilot-sdk/go` |
| **.NET**                 | [`cookbook/dotnet/`](https://github.com/github/awesome-copilot/blob/main/cookbook/copilot-sdk/dotnet/README.md) | `dotnet add package GitHub.Copilot.SDK`   |

See the individual SDK READMEs for installation, usage examples, and API reference.

## Getting Started

For a complete walkthrough, see the **[Getting Started Guide](./docs/getting-started.md)**.

Quick steps:

1. **Install the Copilot CLI:**

   Follow the [Copilot CLI installation guide](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-cli) to install the CLI, or ensure `copilot` is available in your PATH.

2. **Install your preferred SDK** using the commands above.

3. **See the SDK README** for usage examples and API documentation.

## Architecture

All SDKs communicate with the Copilot CLI server via JSON-RPC:

```
Your Application
       ↓
  SDK Client
       ↓ JSON-RPC
  Copilot CLI (server mode)
```

The SDK manages the CLI process lifecycle automatically. You can also connect to an external CLI server—see the [Getting Started Guide](./docs/getting-started.md#connecting-to-an-external-cli-server) for details on running the CLI in server mode.

## FAQ

### Do I need a GitHub Copilot subscription to use the SDK?

Yes, a GitHub Copilot subscription is required to use the GitHub Copilot SDK, **unless you are using BYOK (Bring Your Own Key)**. With BYOK, you can use the SDK without GitHub authentication by configuring your own API keys from supported LLM providers. For standard usage (non-BYOK), refer to the [GitHub Copilot pricing page](https://github.com/features/copilot#pricing), which includes a free tier with limited usage.

### How does billing work for SDK usage?

Billing for the GitHub Copilot SDK is based on the same model as the Copilot CLI, with each prompt being counted towards your premium request quota. For more information on premium requests, see [Requests in GitHub Copilot](https://docs.github.com/en/copilot/concepts/billing/copilot-requests).

### Does it support BYOK (Bring Your Own Key)?

Yes, the GitHub Copilot SDK supports BYOK (Bring Your Own Key). You can configure the SDK to use your own API keys from supported LLM providers (e.g. OpenAI, Azure AI Foundry, Anthropic) to access models through those providers. See the **[BYOK documentation](./docs/auth/byok.md)** for setup instructions and examples.

**Note:** BYOK uses key-based authentication only. Microsoft Entra ID (Azure AD), managed identities, and third-party identity providers are not supported.

### What authentication methods are supported?

The SDK supports multiple authentication methods:
- **GitHub signed-in user** - Uses stored OAuth credentials from `copilot` CLI login
- **OAuth GitHub App** - Pass user tokens from your GitHub OAuth app
- **Environment variables** - `COPILOT_GITHUB_TOKEN`, `GH_TOKEN`, `GITHUB_TOKEN`
- **BYOK** - Use your own API keys (no GitHub auth required)

See the **[Authentication documentation](./docs/auth/index.md)** for details on each method.

### Do I need to install the Copilot CLI separately?

Yes, the Copilot CLI must be installed separately. The SDKs communicate with the Copilot CLI in server mode to provide agent capabilities.

### What tools are enabled by default?

