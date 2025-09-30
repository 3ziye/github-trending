## Blades
Blades is a multimodal AI Agent framework in Go, supporting custom models, tools, memory, middleware, and more. It is well-suited for multi-turn conversations, chain reasoning, and structured output.
> The name comes from the game God of War, set in Greek mythology, which tells the story of Kratos, who becomes a god of war and embarks on a divine slaughter. Blades are Kratos's iconic weapons.

## Architecture Design
Blades leverages the characteristics of Go to provide a flexible and efficient AI Agent solution. Its core lies in achieving high decoupling and extensibility through a unified interface and pluggable components. The overall architecture is as follows:
![architecture](./docs/images/architecture.png)

- **Go Idiomatic**: Built entirely in the Go way, the code style and user experience make Go developers feel at home.
- **Easy to Use**: Through concise code, define an AI Agent and quickly deliver requirements, making complex logic clear, easy to manage, and maintain.
- **Middleware Ecosystem**: Drawing inspiration from Kratos’s middleware design philosophy, features like Observability, Guardrails, and others can be easily integrated into the AI Agent.
- **Highly Extensible**: Through a unified interface and pluggable components, achieve high decoupling and extensibility, making it easy to integrate different LLM models and external tools.

## Core Concepts
The Blades framework achieves its powerful functionality and flexibility through a series of well-designed core components. These components work together to build the intelligent behavior of the Agent:

* **Agent (Intelligent Entity)**: The core unit that executes tasks, capable of invoking models and tools.
* **Prompt (Prompt Text)**: A templated text used to interact with LLMs, supporting dynamic variable substitution and complex context construction.
* **Chain (Chain)**: Links multiple Agents or other Chains to form complex workflows.
* **ModelProvider (Model)**: A pluggable LLM interface, allowing you to easily switch and integrate different language model services (such as OpenAI).
* **Tool (Tool)**: External capabilities that the Agent can use, such as calling APIs, querying databases, accessing file systems, etc.
* **Memory (Memory)**: Provides short-term or long-term memory capabilities for the Agent, enabling context-aware continuous conversations.
* **Middleware (Middleware)**: Similar to middleware in web frameworks, it can implement cross-cutting control over the Agent.

### Runner
`Runner` is the most core interface in the Blades framework, defining the basic behavior of all executable components. Its design aims to provide a unified execution paradigm, achieving **decoupling, standardization, and high composability** of various functional modules within the framework through the `Run` and `RunStream` methods. Components such as `Agent`, `Chain`, and `ModelProvider` all implement this interface, unifying their execution logic and allowing different components to be flexibly combined like LEGO bricks to build complex AI Agents.

```go
// Runner represents an entity that can process prompts and generate responses.
type Runner interface {
    // Run performs a synchronous, non-streaming operation, returning a complete Generation result.
    Run(context.Context, *Prompt, ...ModelOption) (*Generation, error)
    // RunStream performs an asynchronous, streaming operation, returning a Streamer for receiving Generation results step by step.
    RunStream(context.Context, *Prompt, ...ModelOption) (Streamer[*Generation], error)
}
```
![runner](docs/images/runner.png)

### ModelProvider
`ModelProvider` is the core abstraction layer in the `Blades` framework for interacting with underlying large language models (LLMs). Its design goal is to achieve **decoupling and extensibility** through a unified interface, separating the framework's core logic from the implementation details of specific models (such as OpenAI, DeepSeek, Gemini, etc.). It acts as an adapter, responsible for converting standardized requests within the framework into the format required by the native API of the model and converting the model's response back into the framework's standard format, thus allowing developers to easily switch and integrate different LLMs.

```go
type ModelProvider interface {
    // Generate performs a complete generation request and returns the result at once. Suitable for scenarios where real-time feedback is not needed.
    Generate(context.Context, *ModelRequest, ...ModelOption) (*ModelResponse, error)
    // NewStream initiates a streaming request. This method immediately returns a Streamer object, through which the caller can receive the generated content from the model step by step, suitable for building real-time, typewriter-effect conversation applications.
    NewStream(context.Context, *ModelRequest, ...ModelOption) (Streamer[*ModelResponse], error)
}
```
![ModelProvider](./docs/images/model.png)

### Agent
`Agent` is the core or