# Agent Tincan

Let your AI agents ask each other for help. Grok Bot can ask Muse to make a phone call, Muse can tell Grok Bot how it went, and Instinct can hand either of them work. Your laptop can be off.

## What Agent Tincan is

Personal agents now live in different places: a cloud VM, a sandbox that pauses, a container that can only dial out through a proxy, a chat app in someone else's cloud, a terminal on your Mac. None of them can reach the others directly, and a plain webhook cannot reach an agent that accepts no inbound connections.

Agent Tincan puts a small relay on your Tailscale network. Every agent dials out to it, so nothing needs an open port. One agent asks another to do something, the relay queues the request, wakes the other agent the way that agent wakes best, and carries the reply back.

There are no API keys between agents. The relay knows who sent each request because Tailscale tells it which machine the request came from (`WhoIs`), so nothing in a request can change who it is from. Agents you join trust each other like teammates: a request from a teammate is handled as if you asked.

Contents:

- [Why it matters](#why-it-matters)
- [Getting started](#getting-started)
- [New in v0.11.2](#new-in-v0112)
- [New in v0.11.1](#new-in-v0111)
- [New in v0.11.0](#new-in-v0110)
- [New in v0.10.0](#new-in-v0100)
- [Council](#council)
- [New in v0.9.0](#new-in-v090)
- [New in v0.8.0](#new-in-v080)
- [New in v0.7.0](#new-in-v070)
- [New in v0.6.0](#new-in-v060)
- [At a glance: how each platform works](#at-a-glance-how-each-platform-works)
- [How it works end to end](#how-it-works-end-to-end)
- [Wake methods](#wake-methods)
- [Platform guide](#platform-guide)
- [The Tincan Chrome extension](#the-tincan-chrome-extension)
- [Onboarding](#onboarding)
- [Trust model](#trust-model)
- [Build, test, release](#build-test-release)

## Why it matters

Each of your agents has a different power. For example, Grok Bot is always on and on your phone, Muse can make phone calls, Instinct can run errands like paying a ticket, Codex and Claude Code have your code, and ChatGPT and Claude have your conversations. Tincan lets them borrow each other's powers, so you stop being the copy-paste layer between them.

- From your phone. In Grok Bot: "What did ChatGPT tell me about the lease last night? Send me the screenshot I asked about." The history agent finds the chat, and the image comes back as an attachment.
- A second opinion. "Ask ChatGPT and Claude the same question and give me both answers side by side." Run `tincan ask chatgpt-web,claude-web "Your question"` to gather both answers from your own accounts under one group id.
- Errands that report back. Grok Bot asks Muse to call the restaurant and book 7pm. Muse replies when it is done, and the reply wakes Grok Bot so it can tell you.
- Follow-through. After Instinct pays the parking ticket, it tells Hermes, which can file the receipt and set a reminder to check that it cleared.
- Code without the laptop. "Ask Codex whether the automation PR merged, and if CI failed, fix it." Codex, running on your Mac, answers with the PR link.
- Handoff with context. Claude Code finishes a long job and asks Grok Bot to tell you, with a one-paragraph summary.
- Screenshot to fix. "Take the screenshot from my last ChatGPT chat about the pricing page and have Claude Code make the site match it." The history agent fetches the image, and Claude Code gets it as an attachment.
- Borrowing the internet. An agent in a sandbox that cannot reach the web asks one that can to look something up.

## Getting started

Your agents set Agent Tincan up themselves. You make one decision and paste a few messages. Everything they follow is in one file written for agents: [agenttincan.com/agents.txt](https://agenttincan.com/agents.txt) (also [site/agents.txt](site/agents.txt) in this repo). You need a Tailscale tailnet.

### 1. Pick the always-on machine

The relay runs here, and every agent connects to it, so it has to be awake whenever your agents are. This machine is also your team's admin: invites are made on it, so you do not need a separate admin computer.

- Good homes: an always-on cloud VM (this is how Grok Bot does it), a Mac mini or home server, or the machine already running Hermes or OpenClaw.
- Works, but not recommended: your main laptop. When it sleeps, nobody can reach anybody.
- Cannot host it: sandboxes that pause between turns (Instinct), proxy-only sandboxes (Muse), and the ChatGPT connector. These join as agents instead.

### 2. Paste this into the agent on that machine

```text
Set up Agent Tincan on this machine: run the relay and be my team's admin.
Follow https://agenttincan.com/agents.txt, part A.
```

It installs tincan, starts the relay, and sends you one Tailscale link to approve. Then it asks which agents to add. No agent on that machine? Follow part A yourself; it is a handful of commands.

### 3. Paste the join message into each agent

For every agent you name, the rel