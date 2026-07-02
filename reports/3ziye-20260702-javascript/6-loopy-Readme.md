# Loop Library

Loop Library has two separate but related parts in this repository:

| Part | What it is | Where it lives |
| --- | --- | --- |
| **Loop Library website** | The public catalog where people and agents can browse published loops, read them, and copy their prompts. No installation is required. | [Live website](https://signals.forwardfuture.com/loop-library/) · all website code under [`loop-library/`](loop-library/) (shell in [`loop-library/site/`](loop-library/site/), database and rendering in [`loop-library/worker/`](loop-library/worker/)) |
| **Loopy skill** | An optional installable guide that helps an AI agent discover, find, audit, repair, craft, run, debrief, or prepare loops for publication. It uses the website's live catalog when recommending or publishing loops. | source in [`skills/loopy/`](skills/loopy/) |

The website is the library; Loopy is a companion way to work with it. You
can browse or give an agent the website without installing Loopy. Installing
Loopy adds the guided workflow, but it does not install or host the website.

Agents that do not have Loopy can use the published
[agent guide](https://signals.forwardfuture.com/loop-library/agents/),
[agent instructions](https://signals.forwardfuture.com/loop-library/llms.txt),
[JSON catalog](https://signals.forwardfuture.com/loop-library/catalog.json), or
[plain-text catalog](https://signals.forwardfuture.com/loop-library/catalog.txt)
directly.

Each published loop tells an agent what to do, how to check its work, what to
try next, and when to stop.

## What is a loop?

Most prompts ask an agent to do something once. A loop gives the agent a way to
learn from the result and take the next useful step.

For example, a one-shot prompt might say:

> Make this website faster.

A loop adds the feedback that makes the work repeatable:

> Find the slowest page, make one focused improvement, and measure it again.
> Keep the change only if it helps. Repeat until every page meets the target or
> another pass stops producing a meaningful improvement.

Think of a loop as a playbook with feedback built in. It is useful when the
first attempt probably will not be the final answer, such as fixing production
errors, improving test coverage, reviewing a product, or keeping documentation
current.

A good loop answers four simple questions:

- What is the agent trying to accomplish?
- How will it know whether the latest attempt worked?
- What should it do with what it learned?
- When should it finish or ask for help?

## Why loops are powerful

AI agents can move quickly, but an open-ended instruction like "keep improving
this" leaves too much room for guessing. A loop gives the work a clear finish
line and a consistent way to judge progress.

That makes the work easier to trust and easier to repeat. The agent can compare
results instead of relying on confidence, keep improvements instead of merely
making changes, and stop when it succeeds or stops making progress. The same
loop can also be reused by another person or agent without rebuilding the
workflow from scratch.

Loops are not permission for an agent to run forever. The best ones are
deliberately bounded. They include a real check, a clear stopping point, and a
moment to hand control back to a person when judgment or approval is needed.

## What Loopy does

Loopy gives your agent direct access to the ideas in the
library. You can use it to:

- Discover repeated work in a codebase, coding threads, or both and turn the
  strongest qualified candidate into a loop.
- Find a published loop that fits what you are trying to get done.
- Audit an existing loop for weak checks, unsafe actions, or unclear stopping
  behavior, then repair only the material problems.
- Adapt a useful loop to your tools, limits, and definition of success.
- Interview you about what you want to accomplish and what success looks like,
  then craft a new loop through a short, plain-language conversation.
- Run a loop in bounded passes and return a receipt with the actions, evidence,
  outcome, and stopping reason.
- Debrief completed runs and recommend the smallest evidence-backed
  improvement.
- Check a loop for catalog overlap, prepare a publication draft, and submit it
  only after you approve the exact preview.
- Turn the result into a compact prompt you can use right away.

Loopy checks the live catalog when it recommends a published loop. It does
not quietly start schedules, change production, publish content, or send
messages on your behalf. Those actions still require the normal permissions
and approvals.

## Install Loopy

You need Node.js and `npx`. Pick the platform you use:

| Platform | Install command |
| --- | --- |
| Codex | `npx skills add Forward-Future/loopy --skill loopy --agent codex -g -y` |
| Cursor | `npx skills add Forward-Future/loopy --skill loopy --agent cursor -g -y` |
| Claude Code | `npx skills add Forward-Future/loopy --skill loopy --agent claude-code -g -y` |

To install it for all three at on