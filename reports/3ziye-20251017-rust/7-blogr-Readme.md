# Blogr

[![Rust](https://img.shields.io/badge/rust-1.70%2B-orange.svg)](https://www.rust-lang.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Pages](https://img.shields.io/badge/deploy-GitHub%20Pages-blue.svg)](https://pages.github.com/)

A fast, lightweight static site generator built in Rust for creating and managing blogs. Write in Markdown, preview with a built-in terminal editor, and deploy to GitHub Pages with a single command.

![Blogr Demo](demo.gif)

## Quick Start

**Get up and running in 5 minutes:**

```bash
# 1. Install Blogr
cargo install blogr-cli

# 2. Create your blog
blogr init my-blog
cd my-blog

# 3. Create your first post
blogr new "Hello World"

# 4. Preview your blog
blogr serve
# Opens http://localhost:3000

# 5. Deploy to GitHub Pages
export GITHUB_TOKEN=your_github_token
blogr deploy
```

**For a personal website instead of a blog:**
```bash
blogr init --personal my-portfolio
```

## Installation

**Requirements:**
- Rust 1.70+ ([Install Rust](https://rustup.rs/))
- Git (for deployment)
- GitHub account (for GitHub Pages deployment)

**Install from crates.io (recommended):**
```bash
cargo install blogr-cli
```

**Install from source:**
```bash
git clone https://github.com/bahdotsh/blogr.git
cd blogr
cargo install --path blogr-cli
```

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

## Documentation

For detailed information about specific features, see the following documentation:

- **[Commands Reference](docs/COMMANDS.md)** - Complete CLI command reference
- **[Configuration Guide](docs/CONFIGURATION.md)** - All configuration options
- **[Themes Guide](docs/THEMES.md)** - Available themes and customization
- **[Newsletter System](docs/NEWSLETTER.md)** - Email newsletter setup and usage
- **[Search Feature](docs/SEARCH.md)** - Full-text search configuration
- **[Terminal Editor](docs/TERMINAL_EDITOR.md)** - Built-in editor usage

## Basic Commands

**Project Management**
```bash
blogr init my-blog                    # Create new blog
blogr init --personal my-portfolio   # Create personal website
blogr project info                    # Show project details
```

**Content Management**
```bash
blogr new "My Post Title"             # Create new post
blogr list                            # List all posts
blogr edit my-post-slug               # Edit existing post
```

**Development & Deployment**
```bash
blogr serve                           # Start dev server
blogr build                           # Build static site
blogr deploy                          # Deploy to GitHub Pages
```

**Configuration**
```bash
blogr config edit                     # Interactive config editor
blogr theme set minimal-retro         # Switch theme
```

## Project Structure

When you create a new blog, Blogr generates this structure:

```
my-blog/
├── blogr.toml              # Configuration file
├── posts/                  # Markdown posts
│   ├── welcome.md          # Sample post
│   └── about.md            # About page
├── static/                 # Static files (images, CSS, JS)
│   ├── images/
│   ├── css/
│   └── js/
└── .github/workflows/      # GitHub Actions (auto-generated)
    └── deploy.yml
```

**Key files:**
- `blogr.toml` - Your site configuration
- `posts/` - All your blog posts in Markdown
- `static/` - Images, custom CSS, and JavaScript files
- `.github/workflows/` - Automatic deployment setup

## Configuration

Edit `blogr.toml` to configure your site. Use `blogr config edit` for an interactive editor.

**Basic Configuration:**
```toml
[blog]
title = "My Blog"
author = "Your Name"
descripti