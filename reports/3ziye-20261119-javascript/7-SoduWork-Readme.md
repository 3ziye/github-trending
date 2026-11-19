**English** · [简体中文](README.zh-CN.md)

> **中文文档入口：[文档目录](docs/README.zh-CN.md) · [安装与启动](docs/getting-started.md) · [开发指南](docs/development.md)**

<div align="center">

<img src="client/build/icons/256x256.png" alt="SoduWork" width="96" />

# SoduWork

## The AI-native engine for teams and their agents

**A chat ends with an answer. A SoduWork request ends when the person who asked signs off.**

**Multi-harness · Multi-agent · Self-hosted**

Works with Pi · OpenCode · DeepSeek Harness · Qwen Code · Kimi Code · Codex Harness · Codex

```sh
git clone https://github.com/mdiri-ai/SoduWork
cd SoduWork
```

| Platform | Start command |
| --- | --- |
| macOS / Linux | `sh start.sh --desktop` |
| Windows PowerShell | `.\start.cmd --desktop` |
| Windows Command Prompt | `start.cmd --desktop` |

[Website](https://soduwork.ai) | [Live demo](https://soduwork.ai) | [Documentation](docs/README.md) | [Docs website](https://dev.soduwork.ai) | [Releases](https://github.com/mdiri-ai/SoduWork/releases) | [Discord](https://discord.gg/AXYNrAYHy)

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/mdiri-ai/SoduWork)](https://github.com/mdiri-ai/SoduWork/releases)
[![Platforms](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](#quick-start)
[![Discord](https://img.shields.io/badge/chat-Discord-5865F2.svg)](https://discord.gg/AXYNrAYHy)

</div>

---

## What SoduWork can do for you

| | |
| --- | --- |
| **One harness does the work, another reviews it** | Pick Pi to do the work. OpenCode, on a different model, reviews it against the acceptance criteria. If the review fails, the work goes back with the reasons. |
| **Hand a request to a colleague's agent** | People and AI work together: you file a request, AI writes the acceptance criteria, and you assign it to yourself or a colleague. The assignee's agent does the work and reviews it, and a person signs off. Everyone on the request can see who did what. |
| **Turn one person's know-how into a team asset** | When you and AI get a task right, save the chat as a plugin. After review, anyone on the team can use it and contribute improvements, with access granted as needed. |

## Core ideas

<table>
<tr>
<td width="33%" valign="top">

**🔀 Smart dispatch**

**The right agent and model for each job.**

- Pick a harness for each step and switch mid-conversation
- Routine steps on cheap or local models, strong models where it matters
- Long tasks go to your own cloud runner

</td>
<td width="33%" valign="top">

**🛡️ Built-in governance**

**Your organization decides which AI does what, and where.**

- Plugins are reviewed before they are shared, granted to teams or people, and can be revoked
- Roles, usage, cost and an audit log
- Self-hosted

</td>
<td width="33%" valign="top">

**✅ Verified delivery**

**Set the bar first. Done means the requester signed off.**

- Every request carries its acceptance criteria
- A separate AI review checks each one
- A person makes the final call

</td>
</tr>
</table>

## Quick start

> SoduWork is in public beta. Try it and tell us what you think, and evaluate it before using it in production.

You need Python 3.12+, Node.js 22.19+ and Git.

From the cloned repository, run `sh start.sh --desktop` on macOS/Linux, `.\start.cmd --desktop` in Windows PowerShell, or `start.cmd --desktop` in Command Prompt.

The first run installs dependencies, then starts the Hub, the admin console and the desktop client on this computer. Set a password for the `admin` account (12–128 characters) when asked. Then add a model provider under **Model catalog** in the admin console, start a chat in the client and try a small task. Pi is built in.

### Already added an API key? Start here

1. **Add a chat model as well.** Under **Capabilities → Model catalog**, find the service you connected, choose **Add model**, enter the provider's exact model ID, select **Chat model**, and save. Saving a service credential alone does not create a selectable model.
2. **Open the desktop client and sign in to the same Hub.** Use `--desktop` when starting from source. The browser admin console configures the service; check that **Connection** on the desktop sign-in screen points to that same Hub.
3. **Choose New conversation, Pi, and the model you added.** Pi uses the SoduWork model catalog. Codex uses its own account and needs its own sign-in; it does not automatically use this API key.
4. **Try a small task.** For example: “Turn these fictional meeting notes into an action table with owner and due date. Mark missing information as unconfirmed: Alex will organize the requirements by Friday; Sam will check the quotation.” Check the returned table against the notes.
5. **Create a requirement when you need assignment and acceptance.** Describe the goal, inputs and acceptance criteria, open **Arrange execution**, choose an Agent and model, and inspect the delivery before accepting i