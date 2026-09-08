# Vomit

Vomit converts Claude's token vomit into English by piping it through a local LLM. It's fully local (no telemetry) and has no external dependencies.

Vomit hooks into Claude Code, rewriting all its output within the Claude Code terminal UI.

Disclaimer:

* The local LLM can only see what Claude tries to communicate (no access to any actions or files), so it can hallucinate a bit
* This is totally vibe-coded, only tested on Mac
* It's pretty slow

## Install

```sh
# Install the binary to your GOPATH
go install github.com/zachahn/vomit@latest

# Setup connection details to your LLM
vomit init

# Instructions on how to replace Claude's output via hooks
vomit scrub -claude
```

## Usage

In addition, there's a non-invasive mode if you want to run Vomit on the side. _(This is deprecated.)_

* `vomit list`. List Claude session identifiers
* `vomit tail [<session_identifier>]`. Translate Claude's tokens for the specified session, or follow the latest one
* `vomit help`. See for more commands

This should work with:

* [Llama.app]
* [Ollama]
* [Apfel] (Super convenient if you have MacOS 26+, but not very good.)
* Anything that uses the OpenAI API?

If you don't have a local LLM set up already, I think I recommend using [Llama.app], and downloading [GPT-OSS 20B](https://llama.app/models/gpt-oss) through it. Run the `init` subcommand after you set this up.


## Tips

* You can press `ctrl-o` within Claude Code to get Claude's original output.

## License

GNU GPLv3

[Llama.app]: https://github.com/ggml-org/Llama-macOS
[Ollama]: https://github.com/ollama/ollama
[Apfel]: https://github.com/Arthur-Ficial/apfel
[AgentsView]: https://www.agentsview.io
