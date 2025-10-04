<p align="center">
  <img src="./logo/paper2agent_logo.png" alt="Paper2Agent Logo" width="600px" />
</p>

# Paper2Agent: Reimagining Papers As AI Agents

## 📖 Overview
`Paper2Agent` is a multi-agent AI system that automatically transforms research papers into interactive AI agents with minimal human input. Here are some [Demos](#-demos) of the Paper2Agent-generated agent.

## 🚀 Quick Start 

### Basic Usage
Automatically detects and runs all relevant tutorials from a research paper’s codebase.

> **⚠️ Prerequisites**: Complete the [installation & setup](#️-installation--setup) below before running Paper2Agent.
>
> **⏱️ Runtime & Cost**: Processing time varies from 30 minutes to 3+ hours based on codebase complexity. Estimated cost: ~$15 for complex repositories like AlphaGenome using Claude Sonnet 4 (one-time cost).

```bash
cd Paper2Agent

bash Paper2Agent.sh \
  --project_dir <PROJECT_DIR> \
  --github_url <GITHUB_URL>
```

### Advanced Usage

#### Targeted Tutorial Processing
Process only specific tutorials by title or URL:

```bash
bash Paper2Agent.sh \
  --project_dir <PROJECT_DIR> \
  --github_url <GITHUB_URL> \
  --tutorials <TUTORIALS_URL or TUTORIALS_TITLE>
```

#### Repository with API Key
For repositories requiring authentication:

```bash
bash Paper2Agent.sh \
  --project_dir <PROJECT_DIR> \
  --github_url <GITHUB_URL> \
  --api <API_KEY>
```

### Parameters

**Required:**
- `--project_dir <directory>`: Name of the project directory to create
  - Example: `TISSUE_Agent`
- `--github_url <url>`: GitHub repository URL to analyze
  - Example: `https://github.com/sunericd/TISSUE`

**Optional:**
- `--tutorials <filter>`: Filter tutorials by title or URL
  - Example: `"Preprocessing and clustering"` or tutorial URL
- `--api <key>`: API key for repositories requiring authentication
  - Example: `your_api_key_here`

### Examples

#### TISSUE Agent
Create an AI agent from the [TISSUE](https://github.com/sunericd/TISSUE) research paper codebase for uncertainty-calibrated single-cell spatial transcriptomics analysis:

```bash
bash Paper2Agent.sh \
  --project_dir TISSUE_Agent \
  --github_url https://github.com/sunericd/TISSUE
```

#### Scanpy Agent for Preprocessing and Clustering
Create an AI agent from the [Scanpy](https://github.com/scverse/scanpy) research paper codebase for single-cell analysis preprocessing and clustering:

```bash
# Filter by tutorial title
bash Paper2Agent.sh \
  --project_dir Scanpy_Agent \
  --github_url https://github.com/scverse/scanpy \
  --tutorials "Preprocessing and clustering"

# Filter by tutorial URL
bash Paper2Agent.sh \
  --project_dir Scanpy_Agent \
  --github_url https://github.com/scverse/scanpy \
  --tutorials "https://github.com/scverse/scanpy/blob/main/docs/tutorials/basics/clustering.ipynb"
```

#### AlphaGenome Agent
Create an AI agent from the [AlphaGenome](https://github.com/google-deepmind/alphagenome) research paper codebase for genomic data interpretation:

```bash
bash Paper2Agent.sh \
  --project_dir AlphaGenome_Agent \
  --github_url https://github.com/google-deepmind/alphagenome \
  --api <ALPHAGENOME_API_KEY>
```

## ⚙️ Installation & Setup

### Prerequisites
- **Python**: Version 3.10 or higher
- **Claude Code**: Install following instructions at [anthropic.com/claude-code](https://www.anthropic.com/claude-code)

### Installation Steps
1. **Clone the Paper2Agent Repository**
   ```bash
   git clone https://github.com/jmiao24/Paper2Agent.git
   cd Paper2Agent
   ```

2. **Install Python Dependencies**
   ```bash
   pip install fastmcp
   ```

3. **Install and Configure Claude Code**
   ```bash
   npm install -g @anthropic-ai/claude-code
   claude
   ```

## 🤖 How to Create a Paper Agent?
To streamline usage, we recommend creating Paper Agents by connecting Paper MCP servers to an AI coding agent, such as [Claude Code](https://www.anthropic.com/claude-code) or the [Google Gemini CLI](https://google-gemini.github.io/gemini-cli/) (it's free with a Google account!).
We are also actively developing our own base agent, which will be released soon.

### Automatic Launch
After pipeline completion, Claude Code will automatically open with your new MCP server loaded.

### Manual Launch with Local MCP Server
To restart your agent later:
```bash
cd <working_dir>
fastmcp install claude-code <project_dir>/src/<repo_name>_mcp.py \
--python <project_dir>/<repo_name>-env/bin/python
```

### Manual Launch with Remote MCP Server Hosted on Hugging Face
To create a paper agent in Claude Code with the Paper MCP server of interest, use the following script with your own working directory, MCP name, and server URL:
```bash
bash launch_remote_mcp.sh \
  --working_dir <working_dir> \
  --mcp_name <mcp_name> \
  --mcp_url <remote_mcp_url>
```

For example, to create an AlphaGenome Agent, run:
```bash
bash launch_remote_mcp.sh \
  --working_dir analysis_dir \
  --mcp_name alphagenome \
  --mcp_url https://Paper2Agent-alphagenome-mcp.hf.space
```

✅ You will now have an **AlphaGe