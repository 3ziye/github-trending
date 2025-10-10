# Blogr

[![Rust](https://img.shields.io/badge/rust-1.70%2B-orange.svg)](https://www.rust-lang.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Pages](https://img.shields.io/badge/deploy-GitHub%20Pages-blue.svg)](https://pages.github.com/)

A fast, lightweight static site generator built in Rust for creating and managing blogs. Write in Markdown, preview with a built-in terminal editor, and deploy to GitHub Pages with a single command.

## Features

**Two Site Types**
- **Blog Mode**: Traditional blog with posts, archives, tags, and RSS feeds
- **Personal Mode**: Portfolio/personal website without blog functionality
- Single command initialization for either type
- Theme-specific optimizations for each mode

**Content Creation**
- Write posts in Markdown with YAML frontmatter
- Built-in terminal editor with live preview
- Draft and published post management
- Tag-based organization
- Automatic slug generation

**Site Generation**
- Fast static site builds
- Multiple themes: 7 built-in themes for blogs and personal sites
  - Blog: Minimal Retro, Obsidian, Terminal Candy
  - Personal: Dark Minimal, Musashi, Slate Portfolio, Typewriter (NEW)
- Full-text search with MiniSearch integration
- Syntax highlighting for code blocks
- RSS/Atom feeds (blog mode)
- SEO-friendly output

**Development**
- Live reload development server
- Interactive configuration editor
- Project validation and cleanup tools
- Comprehensive CLI commands

**Deployment**
- One-command GitHub Pages deployment
- Custom domain support with CNAME generation
- Automatic git branch management
- Deployment status checking

**Newsletter System** (optional)
- Email subscription collection via IMAP
- Interactive subscriber approval interface
- Newsletter creation from blog posts or custom content
- SMTP integration for reliable email delivery
- Import/export from popular services (Mailchimp, ConvertKit, etc.)
- REST API for external integrations
- Extensible plugin system

## Installation

**Requirements**
- Rust 1.70+
- Git (for deployment)
- GitHub account (for GitHub Pages deployment)

**Install from source:**
```bash
git clone https://github.com/bahdotsh/blogr.git
cd blogr
cargo install --path blogr-cli
```

**Install from crates.io:**
```bash
cargo install blogr-cli
```

## Quick Start

**1. Create a new blog or personal website**
```bash
# For a traditional blog
blogr init my-blog
cd my-blog

# For a personal website (no blog posts)
blogr init --personal my-portfolio
cd my-portfolio
```

**2. Set up GitHub token** (for deployment)
```bash
export GITHUB_TOKEN=your_github_token
```
Get a token at: https://github.com/settings/tokens (needs `repo` and `workflow` scopes)

**3. Create your first post**
```bash
blogr new "Hello World"
```

**4. Choose a theme (optional)**
```bash
# Use default Minimal Retro theme, or switch to Obsidian
blogr theme set obsidian              # For Obsidian community themes
curl -o static/obsidian.css https://raw.githubusercontent.com/kepano/obsidian-minimal/HEAD/obsidian.css
```

**5. Preview your blog**
```bash
blogr serve
# Opens http://localhost:3000
```

**6. Deploy to GitHub Pages**
```bash
blogr deploy
```

## Commands

**Project Management**
```bash
blogr init [NAME]           # Create new blog
blogr init --personal [NAME] # Create personal website (no blog)
  --github-username USER    # Set GitHub username
  --github-repo REPO        # Set repository name
  --no-github               # Skip GitHub setup

blogr project info          # Show project details
blogr project check         # Validate project
blogr project clean         # Clean build files
```

**Content Management**
```bash
blogr new "Post Title"      # Create new post
  --draft                   # Save as draft
  --tags "rust,web"         # Add tags

blogr list                  # List all posts
  --drafts                  # Show only drafts
  --tag rust                # Filter by tag

blogr edit my-post-slug     # Edit existing post
blogr delete my-post-slug   # Delete post
```

**Development**
```bash
blogr serve                 # Start dev server
  --port 8080               # Custom port
  --open                    # Open browser

blogr build                 # Build static site
  --drafts                  # Include drafts
```

**Deployment**
```bash
blogr deploy                # Deploy to GitHub Pages
  --message "Update"        # Custom commit message
```

**Configuration**
```bash
blogr config edit          # Interactive config editor
blogr config get blog.title # Get config value
blogr config set blog.title "My Blog" # Set config value

# Domain setup
blogr config domain set example.com     # Set custom domain
blogr config domain list                # List domains
```

**Newsletter** (optional)
```bash
# Subscriber management
blogr newsletter fetch-subscribers      # Fetch from email inbox
blogr newsletter approve                 # Launch approval UI
blogr newsletter list    