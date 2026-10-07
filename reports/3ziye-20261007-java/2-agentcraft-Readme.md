<div align="center">

# AgentCraft

**A team of Claude agents doing real work on your code, inside a Minecraft studio you can walk around in.**

*Powered by Claude*

[![License: MIT](https://img.shields.io/badge/license-MIT-c9a227)](LICENSE)
[![Minecraft 26.3](https://img.shields.io/badge/Minecraft-26.3-8fa98b)](https://www.minecraft.net)
[![Fabric](https://img.shields.io/badge/mod%20loader-Fabric-d97757)](https://fabricmc.net)
[![Claude Agent SDK](https://img.shields.io/badge/agents-Claude%20Agent%20SDK-2fa3a0)](https://code.claude.com/docs/en/agent-sdk/overview)
[![Tests](https://img.shields.io/badge/tests-487%20passing-3b2a20)](foreman/test)

<img src="docs/img/readme/hero.jpg" alt="The AgentCraft HQ at golden hour" width="100%">

</div>

<br>

Multi-agent coding usually means a wall of terminal text. AgentCraft turns it into a place.

You type a goal. A lead agent reads your repo, writes a plan and pins tasks to a wall. Workers walk to
their desks, sit down and start coding in their own git worktrees while their monitors stream every
file they read and every line they change. When a call is genuinely yours, an agent walks over to
you with a question. When work is ready, you review the real diff and press **Merge**. Nothing
touches your branch without that click, and nothing is ever pushed.

Close the game and the agents keep working. Open it again and the studio catches up.

<br>

## How a goal plays out

<table>
<tr>
<td width="50%" valign="top">

**1. You give a goal.** Press <kbd>`</kbd> and type it. `@juniper` messages a specific agent, with
Tab completion.

<img src="docs/img/readme/console.jpg" alt="The command console with agent autocomplete">

</td>
<td width="50%" valign="top">

**2. The lead plans.** Marlow splits the goal into tasks with dependencies. They land on the Task
Wall, and the plan goes into the shared library.

<img src="docs/img/readme/task-wall.jpg" alt="The Task Wall kanban">

</td>
</tr>
<tr>
<td width="50%" valign="top">

**3. The team builds.** Each worker codes in its own worktree. Monitors stream the live log: tool
calls, test runs, red and green diffs.

<img src="docs/img/readme/desk.jpg" alt="Juniper coding at her desk with a live monitor">

</td>
<td width="50%" valign="top">

**4. They come to you.** A clay <kbd>!</kbd> appears, the bell rings, the agent walks to the
podium. Press <kbd>J</kbd> to answer.

<img src="docs/img/readme/podium.jpg" alt="Marlow waiting at the decision podium">

</td>
</tr>
<tr>
<td width="50%" valign="top">

**5. You review and merge.** A real code review screen: file list, line numbers, collapsed context,
the worker's summary and the reviewer's notes.

<img src="docs/img/readme/diff.jpg" alt="The merge review screen with a real diff">

</td>
<td width="50%" valign="top">

**6. Memory stays shared.** The lead's plan, decisions and repo conventions live in a library every
agent reads, and you can too.

<img src="docs/img/readme/library.jpg" alt="The memory library">

</td>
</tr>
</table>

<br>

## Meet the team

<img src="docs/img/readme/cast.jpg" alt="The six AgentCraft agents" width="100%">

Six hand-pixelled characters, each with their own silhouette and colour. **Marlow** leads: he plans,
splits work and reviews. **Juniper, Kit, Wren, Rowan and Tove** build. They walk the studio with
real pathfinding, sit at their desks while they type, show what they are doing with small particles
and nameplates, talk in speech bubbles, and come find you when they need a decision.

<br>

## The studio

<table>
<tr>
<td width="50%"><img src="docs/img/readme/atrium.jpg" alt="The goal atrium"></td>
<td width="50%"><img src="docs/img/readme/studio.jpg" alt="The studio floor"></td>
</tr>
<tr>
<td><b>The Goal Atrium.</b> Progress ring, task counts, and how many decisions need you.</td>
<td><b>The studio floor.</b> Desks, status lamps, the library and the lounge.</td>
</tr>
</table>

<img src="docs/img/readme/night.jpg" alt="The HQ at night" width="100%">

Everything is information you can read at a glance. Far away, the lamps and the cupola beacon tell
you who is working, who is stuck and who is waiting on you. Closer, nameplates and cards tell you
what. Up close, monitors and screens tell you exactly how.

<br>

## Proven with real agents

This is not a mockup. These screenshots come from a real run with Claude agents on a sample repo,
driven entirely through the game: a goal typed into the console, questions and permission prompts
answered in game, merges reviewed in the diff screen, including a merge conflict sent back to the
worker and resolved. The game was restarted mid run and the Foreman was taken offline and brought
back. Six features landed in the repo with its tests passing.

<table>
<tr>
<td width="33%"><img src="docs/img/readme/real-decision.jpg" alt="A real question from the lead agent"></td>
<td width="33%"><img src="docs/img/readme/real-monitor.jpg" alt="A real agent's monitor streaming its work"></td>
<td width="33%"><img src="docs/img/readme/re