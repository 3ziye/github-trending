# zhizhi-agent-runtime

<p align="center">
  <img src="zhizhi-logo.png" alt="Zhizhi agent runtime" width="720">
</p>

[![Go Reference](https://pkg.go.dev/badge/github.com/cocoyes/zhizhi-agent-runtime.svg)](https://pkg.go.dev/github.com/cocoyes/zhizhi-agent-runtime)
[![Go Report Card](https://goreportcard.com/badge/github.com/cocoyes/zhizhi-agent-runtime)](https://goreportcard.com/report/github.com/cocoyes/zhizhi-agent-runtime)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

[中文文档](README.zh-CN.md)

[Architecture and package boundaries](docs/architecture.md)

Production-grade Go runtime for agents that plan, act, recover, and remain auditable.

Version 1.0.7 adds a realtime duplex speech API, kept separate from ordinary
LLM calls, plus a function-calling Doubao adapter. See
[Doubao realtime speech](docs/doubao-realtime-speech.md).

Zhizhi is a model-agnostic execution layer for real applications. It turns ordinary Go functions into validated tools, builds dependency-safe plans, handles conditional branches and bounded replanning, and makes side effects explicit.

## What You Get

- Typed tools with generated JSON schemas and runtime input/output validation
- Chat, streaming, capability routing, and model-planned complex tasks
- Dependency graphs, parallel batches, conditions, and evidence bindings
- Bounded replanning after required-step failures
- Retries, fallback, deadlines, budgets, and concurrency limits
- Guards, confirmation gates, action receipts, and side-effect safety
- MCP integration with allow-lists and trust-boundary controls
- JSONL traces, evidence, warnings, and execution statistics

The lifecycle is explicit:

```text
request -> route -> plan -> execute -> observe evidence -> replan -> answer
```

## Requirements

- Go 1.25 or newer
- An OpenAI-compatible Chat Completions endpoint

The built-in adapter calls `{LLM_BASE_URL}/chat/completions`. It accepts standard
Chat Completions responses and Responses-style text responses (`output_text` or
`output[].content[].text`). Internal tool IDs may contain dots; they are normalized
only on the provider wire format.

Hybrid reasoning models such as DeepSeek and Doubao can be configured explicitly:

```go
model := openaicompat.New(openaicompat.Config{
    BaseURL:         os.Getenv("LLM_BASE_URL"),
    APIKey:          os.Getenv("LLM_API_KEY"),
    Model:           os.Getenv("LLM_MODEL"),
    Thinking:        openaicompat.ThinkingEnabled, // or ThinkingDisabled / ThinkingAuto
    ReasoningEffort: "high",
})
```

The adapter sends `thinking: {"type":"..."}` and, when explicitly configured, the top-level `reasoning_effort` field. When thinking mode is combined with tool calls, returned `reasoning_content` is automatically preserved in same-turn continuation requests. If omitted, `thinking` defaults to `ThinkingDisabled`, while `reasoning_effort` is not sent and remains under caller/provider control. Supported values still depend on the provider and model version. Example 10 also reads `LLM_THINKING` and `LLM_REASONING_EFFORT`.

Enable detailed JSONL when diagnosing plans or tool arguments:

```go
zhizhi.WithObserver(observe.NewJSONL(os.Stdout, observe.WithDetails()))
```

Detailed mode records planner/replanner model requests, raw responses and repair attempts, actual per-step inputs/outputs/errors, the final patch, and final-composer requests/responses. It may contain user or business data, so it is disabled by default; example 10 enables it explicitly.

The runtime no longer hand-parses structured model output: `jsonrepair-go` extracts and repairs non-standard JSON, `mapstructure/v2` handles common weak scalar drift, and `go-openapi/jsonpointer` resolves RFC 6901 evidence paths. Repaired syntax must still pass plan, JSON Schema, and patch-application validation before execution.

The planner and replanner follow Eino's structured-output pattern on their primary path: derive JSON Schema from the Go result type, bind Plan or Patch as the only synthetic output tool, force `tool_choice`, and consume only that tool's arguments. Plain JSON text remains a compatibility path for models that do not advertise tool calling; domain tools are catalog metadata and cannot execute during planning.

## Install

```bash
go get github.com/cocoyes/zhizhi-agent-runtime
```

## Quickstart

```go
package main

import (
    "context"
    "fmt"
    "log"
    "os"

    zhizhi "github.com/cocoyes/zhizhi-agent-runtime"
    "github.com/cocoyes/zhizhi-agent-runtime/adapter/model/openaicompat"
)

func main() {
    model := openaicompat.New(openaicompat.Config{
        BaseURL: os.Getenv("LLM_BASE_URL"),
        APIKey:  os.Getenv("LLM_API_KEY"),
        Model:   os.Getenv("LLM_MODEL"),
    })
    agent, err := zhizhi.New(zhizhi.WithModel(model))
    if err != nil { log.Fatal(err) }
    defer agent.Close(context.Background())

    response, err := agent.Run(context.Background(), zhizhi.Request{
        Input: "Summarize the latest support request",
    })
