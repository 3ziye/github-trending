<div align="center">
<!-- <img alt="utcp code mode banner" src="https://github.com/user-attachments/assets/77723130-ecbc-4d1d-9e9b-20f978882699" width="80%" style="margin: 20px auto;"> -->

<h1 align="center">🤖 Code-Mode Library: First library for tool calls via code execution</h1>
<p align="center">
    <a href="https://github.com/universal-tool-calling-protocol">
        <img src="https://img.shields.io/github/followers/universal-tool-calling-protocol?label=Follow%20Org&logo=github" /></a>
    <a href="https://img.shields.io/npm/dt/@utcp/code-mode" title="PyPI Version">
        <img src="https://img.shields.io/npm/dt/@utcp/code-mode"/></a>
    <a href="https://github.com/universal-tool-calling-protocol/code-mode/blob/main/LICENSE" alt="License">
        <img src="https://img.shields.io/github/license/universal-tool-calling-protocol/code-mode" /></a>
 
  [![npm](https://img.shields.io/npm/v/@utcp/code-mode)](https://www.npmjs.com/package/@utcp/code-mode)
</p>
</div>

> Transform your AI agents from clunky tool callers into efficient code executors — in just 3 lines.

## Why This Changes Everything

LLMs excel at writing code but struggle with tool calls. Instead of exposing hundreds of tools directly, give them ONE tool that executes TypeScript code with access to your entire toolkit.

[Apple](https://machinelearning.apple.com/research/codeact), [Cloudflare](https://blog.cloudflare.com/code-mode/), and [Anthropic](https://www.anthropic.com/engineering/code-execution-with-mcp) say that Code-Mode is a more efficient way to approach tool calling compared to the traditional dump function information and then extract a JSON for function calling.

## Benchmarks

Independent [Python benchmark study](https://github.com/imran31415/codemode_python_benchmark) validates the performance claims with **$9,536/year cost savings** at 1,000 scenarios/day:

| Scenario Complexity | Traditional | Code Mode | **Improvement** |
|---------------------|-------------|-----------|----------------|
| **Simple (2-3 tools)** | 3 iterations | 1 execution | **67% faster** |
| **Medium (4-7 tools)** | 8 iterations | 1 execution | **75% faster** |
| **Complex (8+ tools)** | 16 iterations | 1 execution | **88% faster** |

### **Why Code Mode Dominates:**

   **Batching Advantage** - Single code block replaces multiple API calls  
   **Cognitive Efficiency** - LLMs excel at code generation vs. tool orchestration  
   **Computational Efficiency** - No context re-processing between operations

# Getting Started

[<img width="2606" height="1445" alt="Frame 4 (4)" src="https://github.com/user-attachments/assets/58ba26ab-6e77-459b-a59a-eeb60d711746" />
](https://www.youtube.com/watch?v=zsMjkPzmqhA)

## Get Started in 3 Lines

```typescript
import { CodeModeUtcpClient } from '@utcp/code-mode';

const client = await CodeModeUtcpClient.create();                    // 1. Initialize
await client.registerManual({ name: 'github', /* MCP config */ });  // 2. Add tools  
const { result } = await client.callToolChain(`/* TypeScript */`);   // 3. Execute code
```

That's it. Your AI agent can now execute complex workflows in a single request instead of dozens.

## What You Get

### **Progressive Tool Discovery**
```typescript
// Agent discovers tools dynamically, loads only what it needs
const tools = await client.searchTools('github pull request');
// Instead of 500 tool definitions → 3 relevant tools
```

### **Natural Code Execution**  
```typescript
const { result, logs } = await client.callToolChain(`
  // Chain multiple operations in one request
  const pr = await github.get_pull_request({ owner: 'microsoft', repo: 'vscode', pull_number: 1234 });
  const comments = await github.get_pull_request_comments({ owner: 'microsoft', repo: 'vscode', pull_number: 1234 });
  const reviews = await github.get_pull_request_reviews({ owner: 'microsoft', repo: 'vscode', pull_number: 1234 });
  
  // Process data efficiently in-sandbox
  return {
    title: pr.title,
    commentCount: comments.length,
    approvals: reviews.filter(r => r.state === 'APPROVED').length
  };
`);
// Single API call replaces 15+ traditional tool calls
```

### **Auto-Generated TypeScript Interfaces**
```typescript
namespace github {
  interface get_pull_requestInput {
    /** Repository owner */
    owner: string;
    /** Repository name */ 
    repo: string;
    /** Pull request number */
    pull_number: number;
  }
}
```

## Enterprise-Ready

- **Secure VM Sandboxing** – Node.js isolates prevent unauthorized access
- **Timeout Protection** – Configurable execution limits prevent runaway code  
- **Complete Observability** – Full console output capture and error handling
- **Zero External Dependencies** – Tools only accessible through registered UTCP/MCP servers
- **Runtime Introspection** – Dynamic interface discovery for adaptive workflows

If you're working at an enterprise, and need support, book a consultation [here](https://bevel.neetocal.com/meeting-with-ali).
## Universal Protocol