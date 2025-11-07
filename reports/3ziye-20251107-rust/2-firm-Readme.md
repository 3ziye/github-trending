# Firm: Business-as-code
A text-based work management system for technologists.

![Firm CLI demo](media/demo.gif)

## Why?
Modern businesses are natively digital, but lack a unified view. Your data is scattered across SaaS tools you don't control, so you piece together answers by jumping between platforms.

Your business is a graph: customers link to projects, projects link to tasks, people link to organizations. Firm lets you define these relationships in plain text files (you own!).

Version controlled, locally stored and structured as code with the Firm DSL. This structured representation of your work, *business-as-code*, makes your business readable to yourself and to the robots that help you run it.

### Features
- **Everything in one place:** Organizations, contacts, projects, and how they relate.
- **Own your data:** Plain text files and tooling that runs on your machine.
- **Open data model:** Tailor to your business with custom schemas.
- **Automate anything:** Search, report, integrate, whatever. It's just code.
- **AI-ready:** LLMs can read, write, and query your business structure.

## Getting started
Firm operates on a "workspace": a directory containing all your `.firm` DSL files. The Firm CLI processes every file in this workspace to build a unified, queryable graph of your business.

The first step is to add an entity to your workspace. You can do this either by using the CLI or by writing the DSL yourself.

### Add entities with the CLI
Use `firm add` to interactively generate new entities. Out of the box, Firm supports a set of pre-built entity schemas for org mapping, customer relations and work management. The CLI will prompt you for the necessary info and generate corresponding DSL.

```bash
$ firm add
```
```
Adding new entity

> Type: organization
> ID: megacorp
> Name: Megacorp Ltd.
> Email: mega@corp.com
> Urls: ["corp.com"]

Writing generated DSL to file my_workspace/generated/organization.firm
```

### Write DSL manually
Alternatively, you can create a `.firm` file and write the DSL yourself.

```firm
organization megacorp {
  name = "Megacorp Ltd."
  email = "mega@corp.com"
  urls = ["corp.com"]
}
```

Both of these methods achieve the same result: a new entity defined in your Firm workspace.

### Querying the workspace
Once you have entities in your workspace, you can query them using the CLI.

#### Listing entities
Use `firm list` to see all entities of a specific type.

```bash
$ firm list task
```
```
Found 7 entities with type 'task'

ID: task.design_homepage
Name: Design new homepage
Is completed: false
Assignee ref: person.jane_doe

...
```

#### Getting an entity
To view the full details of a single entity, use `firm get` followed by the entity's type and ID.

```bash
$ firm get person john_doe
```
```
Found 'person' entity with ID 'john_doe'

ID: person.john_doe
Name: John Doe
Email: john@doe.com
```

#### Exploring relationships
The power of Firm lies in its ability to travel a graph of your business. Use `firm related` to explore connections to/from any entity.

```bash
$ firm related contact john_doe
```
```
Found 1 relationships for 'contact' entity with ID 'john_doe'

ID: interaction.megacorp_intro
Type: Call
Subject: Initial discussion about Project X
Interaction date: 2025-09-30 09:45:00 +02:00
Initiator ref: person.jane_smith
Primary contact ref: contact.john_doe
```

## Installation
The Firm CLI is available to download via [Github Releases](https://github.com/42futures/firm/releases/). Install scripts are provided to make the process easy.

### Linux and macOS

```bash
curl -fsSL https://raw.githubusercontent.com/42futures/firm/main/install.sh | sudo bash
```

If you don't feel confident running it with `sudo`, you can:

1. **Download the release**
   - Go to [Github Releases](https://github.com/42futures/firm/releases/)
   - Download the appropriate archive for your operating system and architecture. You can run `uname -m` in your terminal if you're not sure which one to pick.

2. **Extract the archive**
```bash
tar -xzf firm-[OS]-[ARCH].tar.gz
```

3. **Navigate to the extracted directory**
```bash
cd firm-[OS]-[ARCH]
```

4. **Run the application**

**Option A:** Run from current directory
```bash
./firm
```

**Option B:** Install globally (recommended)
```bash
# Make executable (if needed)
chmod +x firm

# Move to system PATH
sudo mv firm /usr/local/bin/

# Now you can run firm from anywhere
firm
```

### Windows
```bash
irm https://raw.githubusercontent.com/42futures/firm/main/install.ps1 | iex
```

## Using Firm as a library
Beyond the CLI, you can integrate Firm's core logic directly into your own software using the `firm_core` and `firm_lang` Rust packages. This allows you to build more powerful automations and integrations on top of Firm.

First, add the Firm crates to your `Cargo.toml`:

```toml
[dependencies]
firm_core = { git = "https://github.com/42futures/firm.git" }
firm_lang = { git = "https://github.com/42futures/firm.git" }
```

You can then l