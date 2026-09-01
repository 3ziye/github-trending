![AOCI-CODE logo — AI-Oriented Cognition Infrastructure](assets/aoci-logo-en.jpg)

# AOCI-CODE

**AOCI-CODE is an indexing method that establishes global software-project cognition for AI Agents and provides a persistent, governable repository cognition map.**

🇺🇸 English | [🇨🇳 简体中文](README.zh-CN.md)

![Status](https://img.shields.io/badge/status-v0.1.0--rc7-orange)
![Runtime](https://img.shields.io/badge/runtime-local--first-blue)
![MCP](https://img.shields.io/badge/MCP-9%20tools-6f42c1)
![License](https://img.shields.io/badge/license-FSL--1.1--MIT-blue)

> [!IMPORTANT]
> AOCI-CODE v0.1.0-rc7 is the current release candidate. It is Fair Source/source-available software under FSL-1.1-MIT; see [LICENSE](LICENSE). Build from canonical source or use a signed package from the [v0.1.0-rc7 GitHub Release](https://github.com/aoci-spec/aoci-code/releases/tag/v0.1.0-rc7) after following the [release verification procedure](https://github.com/aoci-spec/aoci-code/blob/v0.1.0-rc7/docs/install.md#signed-github-release-packages).

## 🧠 What is AOCI?

**AOCI (AI-Oriented Cognition Infrastructure) is cognition infrastructure positioned between AI Agents and software systems.**

Large models handle reasoning, Agents handle planning and execution, and AOCI organizes code, configuration, tests, and database structures into continuously maintainable system cognition bound to the current system version, for Agents to read and understand before acting.

## 🗺️ What is AOCI-CODE?

AOCI-CODE originates from AOCI. Put simply, AOCI-CODE distills the information from source code, database structures, and other assets that materially affects how AI understands and modifies a system into a high-information-density, plain-text index combining symbols and semantics.

AOCI-CODE applies this method to projects through the `aoci` CLI and MCP Server.

When model context is limited, an AI Agent can read the index first, acquire most of the project’s key information in one pass, and then enter a specific development task. This reduces repeated searching and code re-learning while improving continuity across tasks and sessions.

- **The index is not a one-time summary**: it evolves with the system and remains in the project over the long term, where it can be diffed, reviewed, versioned, and rolled back with Git.
- **It records more than “where files are”**: AOCI-CODE also preserves object responsibilities, strong relationships, public contracts, transaction boundaries, compatibility constraints, and other information that is difficult to infer directly from code structure.
- **The index is portable**: the index is stored with the project and is not tied to a specific model, AI Agent, or individual session. When the index is aligned with the code version, different AI Agents and later sessions can read and reuse the same system cognition without rebuilding their understanding from scratch each time.
- **Code and databases can be understood together**: the model can build an independent table-level index for database tables. When Code Cognition and Database Cognition are delivered together, an AI Agent can understand the software system more completely.


Names in this document have the following roles: **AOCI** refers to the cognition paradigm and protocol, while **AOCI-CODE** refers to the project and the index itself that embody this method.

## ⚙️ How AOCI works

In the current Volume-first layout, AOCI-CODE organizes the index as governed, plain-text cognition assets stored with the project:

- **Root (`aoci.txt`)**: declares the composition and activation entry point of the current CognitionSet;
- **Meta (`aoci.meta.txt`)**: stores the tag dictionary, FRAS rules, and model-authoring constraints;
- **Code (`aoci.code.txt`)**: stores model-authored cognition for code and other repository assets;
- **Database (`aoci.database.txt`)**: stores optional table-level cognition when Database Cognition is enabled.

Root, Meta, and participating object Volumes together form the current Whole-Index. On top of these assets, the workflow has three stages:

1. **Establish governed cognition**: The model reads source code and accepted evidence, while AOCI-CODE governs Managed Scope and model-authored cognition for managed objects with the `index` role.
2. **Deliver cognition before action**: The Agent reads the Rules, live Guide, and current Whole-Index, then checks source and other evidence for the task at hand.
3. **Maintain cognition after verified change**: Once code and tests are stable, project Rules and the AOCI MCP workflow guide the Agent to update affected Entries and return formal cognition to `aligned`.

These plain-text cognition assets are stored with the project and can be versioned with Git. When cognition remains aligned with the current system version, different AI Agents and later sessions can read and reuse the same Whole-Index.

## 🚀 One-step setup

Give the following instruction to your AI Agent to download AOCI-CODE and integrate it; 