# Best Practices for Creating Agent Skills

This guide explains how to write professional-grade skills for agents, validate them using LLMs, and maintain a lean context window.

This guide is a concentrated set of best practices for creating agent skills. If you're looking for a comprehensive documentation see [Claude's docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).

**To [evaluate if your skills do well](https://github.com/mgechev/skill-eval), check out the skills evaluation framework.**

## Structure of a skill

Every skill must follow this directory structure:

Plaintext

```
skill-name/
├── SKILL.md              # Required: Metadata + core instructions (<500 lines)
├── scripts/              # Executable code (Python/Bash) designed as tiny CLIs
├── references/           # Supplementary context (schemas, cheatsheets) 
└── assets/               # Templates or static files used in output
```

* **SKILL.md:** Acts as the "brain." Use it for navigation and high-level procedures.  
* **References:** Link directly from SKILL.md. Keep them **one level deep** only.  
* **Scripts:** Use for fragile/repetitive operations where variation is a bug. **Do not bundle library code here**;

## Optimize the frontmatter for discoverability

The `name` and `description` in the frontmatter of your `SKILL.md` are the only fields that the agent sees before triggering a skill. If they are not optimized for discoverability and specific enough, your skill is invisible.

* **Adhere to Strict Naming:** The name field must be 1-64 characters, contain only lowercase letters, numbers, and hyphens (no consecutive hyphens), and **must exactly match the parent directory name** (e.g., name: `angular-testing` must live in `angular-testing/SKILL.md`).  
* **Write Trigger-Optimized Descriptions:** (Max 1,024 characters). This is the only metadata the agent sees for routing. Describe the capability in the third person and include "negative triggers."  
  * **Bad:** "React skills." (Too vague).
  * **Good:** "Creates and builds React components using Tailwind CSS. Use when the user wants to update component styles or UI logic. Don't use it for Vue, Svelte, or vanilla CSS projects."

## Progressive disclosure and resource management

Maintain a pristine context window by loading information only when needed. **SKILL.md** is the "brain" for high-level logic; offload details to subdirectories.

* **Keep SKILL.md Lean:** Limit the main file to **\<500 lines**. Use it for navigation and primary procedures.  
* **Use Flat Subdirectories:** Move bulky context to standard folders. Keep files exactly **one level deep** (e.g., `references/schema.md`, not `references/db/v1/schema.md`).  
  * `references/`: API docs, cheatsheets, domain logic.  
  * `scripts/`: Executable code for deterministic tasks.  
  * `assets/`: Output templates, JSON schemas, images.  
* **Just-in-Time (JiT) Loading:** Explicitly instruct the agent when to read a file. It will not see these resources until you direct it to (e.g., *"See `references/auth-flow.md` for specific error codes"*).  
* **Explicit Pathing:** Always use **relative paths** with forward slashes (`/`), regardless of the OS.

Skills are for agents, not humans. To keep the context window lean and avoid unnecessary token consumption. **Do not create:**

* **Documentation files:** `README.md`, `CHANGELOG.md`, or `INSTALLATION_GUIDE.md`.  
* **Redundant logic:** If the agent already handles a task reliably without help, delete the instruction.  
* **Library code:** Skills should reference existing tools or contain tiny, single-purpose scripts. Long-lived library code belongs in standard repo CLI directories.

## Use specific procedural instructions instead of prose

Create instructions for LLMs instead of humans.

* **Use Step-by-Step Numbering:** Define the workflow as a strict chronological sequence. If there is a decision tree, map it out clearly (e.g., *"Step 2: If you need source maps run `ng build --source-map`. Otherwise, skip to Step 3."*).  
* **Provide Concrete Templates:** Agents pattern-match exceptionally well. Instead of spending paragraphs describing how a JSON output should look, place a template in the assets/ folder and instruct the agent to copy its structure.  
* **Write in the Third-Person Imperative:** Frame instructions as direct commands to the agent (e.g., *"Extract the text..."* rather than *"I will extract..."* or *"You should extract..."*).

Be specific and consistent in the way you reference concepts in your skill files.

* **Use identical terminology:** Pick a single term to refer to a specific concept.  
* **Specificity**: Use the most specific terminology that’s native to the domain that you describe. For example, in Angular use the concept “template” instead of “html”, “markup”, or “view”.

## Bundle deterministic scripts for repetitive operations

Don't ask the LLM to write complex parsing logic or boilerplate code from scratch every time it r