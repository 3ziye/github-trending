# 🤓 Orchestrator: A multi-agent AI coder. Reached #13 on Stanford's TerminalBench. Open sourced!

TL;DR:
- Over the weekend, quite unexpectedly, I made a multi-agent AI system that places slightly higher than Claude Code on Stanford's TerminalBench leaderboard (13th place).
- This AI system consists of an orchestration agent that dispatches multiple explorer and coder agents to do all the work.
- The orchestrator explicitly defines what knowledge artifacts subagents must return, then reuses and synthesises these artifacts across future tasks - creating compound intelligence where each action builds meaningfully on previous discoveries.

![Orchestrator with claude-sonnet-4 on standford's terminal bench](./readme_imgs/orchestrator-sonnet-4-stanford-terminal-bench-leaderboard.png)

## How the System Works

![System architecture overview](readme_imgs/orch_agent_sys_arch.png)

The orchestrator acts as the brain of the operation - it receives the user's task but never touches code directly. Instead, it:

1. **Analyses** the task and breaks it into focused subtasks
2. **Dispatches** explorer agents to understand the system
3. **Delegates** implementation work to coder agents with precise instructions
4. **Verifies** all changes through additional explorer agents
5. **Maintains** the context store with all discovered knowledge

The orchestrator's lack of direct code access forces proper delegation and verification patterns, leading to more strategic solutions.

For a full breakdown of this project's code structure, see [here](./PROJECT_STRUCTURE.md)


## 📈 Evaluation Results

### Performance on TerminalBench

[Terminal bench](https://www.tbench.ai/) is a brilliant benchmark created by Stanford and [Laude Institute](https://www.laude.org/) to quantify agents' ability to complete complex tasks in the terminal. My Orchestrator system achieved **13th place** on the leaderboard, demonstrating competitive performance against leading AI coding assistants.

I ran the Orchestrator evaluations with both Claude-4-Sonnet and also Qwen3-Coder-480B-A35B:

![Performance comparison chart](readme_imgs/perf_chart.png)
![Orchestrator with qwen-3-coder on standford's terminal bench](./readme_imgs/orchestrator-qwen-3-coder-stanford-terminal-bench-leaderboard.png)

This image shows Qwen-3-Coder performance on the benchmark. The screenshot towards the top of this README shows Sonnet-4 performance.

### Cost & Efficiency

One of the most striking results is the amount of tokens used by Sonnet-4 as opposed to Qwen3-Coder.

The below table shows the total tokens (input and output included) processed across the TerminalBench evaluation run (5 attempts at 80 tasks = 400 trajectories).

| Model | Success Rate | Total Evaluation Cost | Token Usage |
|-------|--------------|------------|-------------|
| **Claude Sonnet-4** | 37.0% | $263.56* | 93.2M tokens |
| **Qwen-3-Coder** | 19.7% | $217.83 | 14.7M tokens |

*Claude Sonnet-4 costs reflect heavy caching usage, reducing actual API costs


## 🤖 The Agents

While all agents use the same underlying LLM, each operates with its own context window, specialised system message, and distinct toolset. This creates functionally different agents optimised for their specific roles.

### 🎯 Orchestrator Agent
[System message](./src/agents/system_msgs/md_files/orchestrator_sys_msg_v0.1.md)
**Role:** Strategic coordinator and persistent intelligence layer  
**Capabilities:** Task decomposition, context management, subagent delegation  
**Tools:** Task creation, subagent launching, context store management  
**Restrictions:** Cannot read or modify code directly - operates purely at architectural level  

The orchestrator maintains the complete picture across all tasks, tracking discoveries and progress. It crafts precise task descriptions that explicitly specify what contexts subagents should return, ensuring focused and valuable information gathering.

**Trust Calibration Strategy:**  
The orchestrator employs adaptive delegation based on task complexity:
- **Low Complexity Tasks**: Grants extremely high autonomy to the coder agent for simple modifications and bug fixes
- **Medium/Large Tasks**: Maintains strong trust but uses iterative decomposition - breaking complex problems into atomic, verifiable steps
- **Verification Philosophy**: Uses explorer agents liberally to verify progress, especially when tasks involve critical functionality


### 🔍 Explorer Agent 
[System message](./src/agents/system_msgs/md_files/explorer_sys_msg_v0.1.md) 
**Role:** Read-only investigation and verification specialist  
**Capabilities:** System exploration, code analysis, test execution, verification  
**Tools:** File reading, search operations (grep/glob), bash commands, temporary script creation  
**Restrictions:** Cannot modify existing files - strictly read-only operations  

Explorers gather intelligence about the codebase, verify implementations, and discover system behaviors. They create knowledge artifacts that eliminat