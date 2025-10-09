# Claudesidian: Claude Code + Obsidian Starter Kit

Turn your Obsidian vault into an AI-powered second brain using Claude Code.

## What is this?

This is a pre-configured Obsidian vault structure designed to work seamlessly
with Claude Code, enabling you to:

- Use AI as a thinking partner, not just a writing assistant
- Organize knowledge using the PARA method
- Maintain version control with Git
- Access your vault from anywhere (including mobile)

## Quick Start

### 1. Get the Starter Kit

**Option A: Clone with Git**

```bash
# Clone with your preferred folder name (replace 'my-vault' with any name you like)
git clone https://github.com/heyitsnoah/claudesidian.git my-vault
cd my-vault

# Examples:
# git clone https://github.com/heyitsnoah/claudesidian.git obsidian-notes
# git clone https://github.com/heyitsnoah/claudesidian.git knowledge-base
# git clone https://github.com/heyitsnoah/claudesidian.git second-brain
```

**Option B: Download ZIP (no Git required)**

1. Click "Code" → "Download ZIP" on GitHub
2. Extract to your desired location
3. Open the folder in Claude Code

### 2. Run the Setup Wizard

```bash
# Start Claude Code in the directory
claude

# Run the interactive setup wizard (in Claude Code)
/init-bootstrap
```

This will:

- Install dependencies automatically
- Disconnect from the original claudesidian repository
- **Intelligently analyze** your existing vault structure and patterns
- **Import your existing Obsidian vault** safely to OLD_VAULT/ (if you have one)
- **Research your public work** for personalized context (with your permission)
- Ask you about your workflow preferences
- Create a personalized CLAUDE.md configuration
- Set up your folder structure
- Optionally configure Gemini Vision for image/video analysis
- Optionally configure Firecrawl for web research
- Initialize Git for version control

### 3. Open in Obsidian (Optional but Recommended)

- Download [Obsidian](https://obsidian.md)
- Open vault from the claudesidian folder
- This gives you a visual interface alongside Claude Code

### 4. Your First Session

Tell Claude Code:

```
I'm starting a new project about [topic].
I'm in thinking mode, not writing mode.
Please search my vault for any relevant existing notes,
then help me explore this topic by asking questions.
```

Or use one of the pre-configured commands (in Claude Code):

```
/thinking-partner   # For collaborative exploration
/daily-review       # For end-of-day reflection
/research-assistant # For deep dives into topics
```

## Folder Structure

```
claudesidian/
├── 00_Inbox/           # Temporary capture point for new ideas
├── 01_Projects/        # Active, time-bound initiatives
├── 02_Areas/           # Ongoing responsibilities
├── 03_Resources/       # Reference materials and knowledge base
├── 04_Archive/         # Completed projects and inactive items
├── 05_Attachments/     # Images, PDFs, and other files
├── 06_Metadata/        # Vault configuration and templates
│   ├── Reference/      # Documentation and guides
│   └── Templates/      # Reusable note templates
└── .scripts/           # Helper scripts for automation
```

## Key Concepts

### Thinking Mode vs Writing Mode

**Thinking Mode** (Research & Exploration):

- Claude asks questions to understand your goals
- Searches existing notes for relevant content
- Helps make connections between ideas
- Maintains a log of insights and progress

**Writing Mode** (Content Creation):

- Generates drafts based on your research
- Helps structure and edit content
- Creates final deliverables

### The PARA Method

**Projects**: Have a deadline and specific outcome

- Example: "Q4 2025 Marketing Strategy"
- Create a folder in `01_Projects/`

**Areas**: Ongoing without an end date

- Example: "Health", "Finances", "Team Management"
- Lives in `02_Areas/`

**Resources**: Topics of ongoing interest

- Example: "AI Research", "Writing Tips"
- Store in `03_Resources/`

**Archive**: Inactive items

- Completed projects with their outputs
- Old notes no longer relevant

## Claude Code Commands

Pre-configured AI assistants ready to use:

- `thinking-partner` - Explore ideas through questions
- `inbox-processor` - Organize your captures
- `research-assistant` - Deep dive into topics
- `daily-review` - End of day reflection
- `weekly-synthesis` - Find patterns in your week
- `create-command` - Build new custom commands
- `de-ai-ify` - Remove AI writing patterns from text
- `upgrade` - Update to the latest claudesidian version
- `init-bootstrap` - Re-run the setup wizard
- `install-claudesidian-command` - Install shell command to launch vault from
  anywhere

Run with: `/[command-name]` in Claude Code

### Staying Updated with `/upgrade`

Claudesidian automatically checks for updates when you start Claude Code and
will remind you to run `/upgrade` when new features are available.

The upgrade command intelligently merges new features while preserving your
customizations:

```bash
# Preview what would be updated (recom