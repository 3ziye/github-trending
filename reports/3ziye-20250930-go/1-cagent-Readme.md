# 🤖 `cagent` 🤖

> A powerful, easy to use, customizable multi-agent runtime that orchestrates AI agents with
> specialized capabilities and tools, and the interactions between agents.

![cagent in action](docs/assets/cagent-run.gif)

## ✨ What is `cagent`? ✨

`cagent` lets you create and run intelligent AI agents, where each agent has
specialized knowledge, tools, and capabilities.

Think of it as allowing you to quickly build, share and run a team of virtual experts that
collaborate to solve complex problems for you.

And it's dead easy to use!

⚠️ Note: `cagent` is in active development, **breaking changes are to be expected** ⚠️

### Your First Agent

Example [basic_agent.yaml](/examples/basic_agent.yaml):

Creating agents with cagent is very simple. They are described in a short yaml file, like this one:

```yaml
agents:
  root:
    model: openai/gpt-5-mini
    description: A helpful AI assistant
    instruction: |
      You are a knowledgeable assistant that helps users with various tasks.
      Be helpful, accurate, and concise in your responses.
```

Run it in a terminal with `cagent run basic_agent.yaml`.

Many more examples can be found [here](/examples/README.md)!

### Improving an agent with MCP tools

`cagent` supports MCP servers, enabling agents to use a wide variety of external tools and services.

It supports three transport types: `stdio`, `http` and `sse`.

Giving an agent access to tools via MCP is a quick way to greatly improve its capabilities, the quality of its results and its general useful-ness.

Get started quickly with the [Docker MCP Toolkit](https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/) and [catalog](https://docs.docker.com/ai/mcp-catalog-and-toolkit/catalog/)

Here, we're giving the same basic agent from the example above access to a **containerized** `duckduckgo` mcp server and it's tools by using Docker's MCP Gateway:

```yaml
version: "2"

agents:
  root:
    model: openai/gpt-5-mini
    description: A helpful AI assistant
    instruction: |
      You are a knowledgeable assistant that helps users with various tasks.
      Be helpful, accurate, and concise in your responses.
    toolsets:
      - type: mcp
        ref: docker:duckduckgo # stdio transport
```

When using a containerized server via the Docker MCP gateway, you can configure any required settings/secrets/authentication using the [Docker MCP Toolkit](https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/#example-use-the-github-official-mcp-server) in Docker Desktop.

Aside from the containerized MCP severs the Docker MCP Gateway provides, any standard MCP server can be used with cagent!

Here's an example similar to the above but adding `read_file` and `write_file` tools from the `rust-mcp-filesystem` MCP server:

```yaml
version: "2"

agents:
  root:
    model: openai/gpt-5-mini
    description: A helpful AI assistant
    instruction: |
      You are a knowledgeable assistant that helps users with various tasks.
      Be helpful, accurate, and concise in your responses. Write your search results to disk.
    toolsets:
      - type: mcp
        ref: docker:duckduckgo
      - type: mcp
        command: rust-mcp-filesystem # installed with `cargo install rust-mcp-filesystem`
        args: ["--allow-write", "."]
        tools: ["read_file", "write_file"] # Optional: specific tools only
        env:
          - "RUST_LOG=debug"
```

See [the USAGE docs](./docs/USAGE.md#tool-configuration) for more detailed information and examples

### 🎯 Key Features

- **🏗️ Multi-agent architecture** - Create specialized agents for different domains.
- **🔧 Rich tool ecosystem** - Agents can use external tools and APIs via the MCP protocol.
- **🔄 Smart delegation** - Agents can automatically route tasks to the most suitable specialist.
- **📝 YAML configuration** - Declarative model and agent configuration.
- **💭 Advanced reasoning** - Built-in "think", "todo" and "memory" tools for complex problem-solving.
- **🌐 Multiple AI providers** - Support for OpenAI, Anthropic, Gemini and [Docker Model Runner](https://docs.docker.com/ai/model-runner/).

## 🚀 Quick Start 🚀

### Installation

[Prebuilt binaries](https://github.com/docker/cagent/releases) for Windows, macOS and Linux can be found on the releases page of the [project's GitHub repository](https://github.com/docker/cagent/releases)

Once you've downloaded the appropriate binary for your platform, you may need to give it executable permissions.
On macOS and Linux, this is done with the following command:

```sh
# linux amd64 build example
chmod +x /path/to/downloads/cagent-linux-amd64
```

You can then rename the binary to `cagent` and configure your `PATH` to be able to find it (configuration varies by platform).

### **Set your API keys**

Based on the models you configure your agents to use, you will need to set the corresponding provider API key accordingly,
all theses keys are optional, you will likely need at least one of these, though:

```bash
# For OpenAI