# 📝 NoteDiscovery

> Your Self-Hosted Knowledge Base

## What is NoteDiscovery?

NoteDiscovery is a **lightweight, self-hosted note-taking application** that puts you in complete control of your knowledge base. Write, organize, and discover your notes with a beautiful, modern interface—all running on your own server.

![Note Discovery](docs/screenshot.jpg)

## 🎯 Who is it for?

- **Privacy-conscious users** who want complete control over their data
- **Developers** who prefer markdown and local file storage
- **Knowledge workers** building a personal wiki or second brain
- **Teams** looking for a self-hosted alternative to commercial apps
- **Anyone** who values simplicity, speed, and ownership

## ✨ Why NoteDiscovery?

### vs. Commercial Apps (Notion, Evernote, Obsidian Sync)

| Feature | NoteDiscovery | Commercial Apps |
|---------|---------------|-----------------|
| **Cost** | 100% Free | $xxx/month/year |
| **Privacy** | Your server, your data | Their servers, their terms |
| **Speed** | Lightning fast | Depends on internet |
| **Offline** | Always works | Limited or requires sync |
| **Customization** | Full control | Limited options |
| **No Lock-in** | Plain markdown files | Proprietary formats |

### Key Benefits

- 🔒 **Total Privacy** - Your notes never leave your server
- 🔐 **Optional Authentication** - Simple password protection for self-hosted deployments
- 💰 **Zero Cost** - No subscriptions, no hidden fees
- 🚀 **Fast & Lightweight** - Instant search and navigation
- 🎨 **Beautiful Themes** - Multiple themes, easy to customize
- 🔌 **Extensible** - Plugin system for custom features
- 📱 **Responsive** - Works on desktop, tablet, and mobile
- 📂 **Simple Storage** - Plain markdown files in folders
- 🧮 **Math Support** - LaTeX/MathJax for beautiful equations
- 📄 **HTML Export** - Share notes as standalone HTML files

## 🚀 Quick Start

### Running from GitHub Container Registry (Easiest & Recommended)

Use the pre-built image directly from GHCR - no building required!

> **💡 Tip**: Always use `ghcr.io/gamosoft/notediscovery:latest` to get the newest features and fixes.

> **📁 Important - Volume Mapping**: The container needs local folders/files to work:
> - **Required**: `data` folder - **Your personal notes** will be stored here (create an empty folder)
> - **Required**: `themes` folder with theme `.css` files (at least a single theme must exist)
> - **Required**: `plugins` folder (can be empty for basic functionality)
> - **Required**: `config.yaml` file (needed for the app to run)
> - **Optional**: `documentation` folder - If you cloned the repo, mount this to view app docs inside NoteDiscovery
> 
> **Setup Options:**
> 
> 1. **Minimal** (quick test - download just the essentials):
>    ```bash
>    # Linux/macOS
>    mkdir -p data plugins themes  # data/ is for YOUR notes
>    curl -O https://raw.githubusercontent.com/gamosoft/notediscovery/main/config.yaml
>    # Download at least light and dark themes
>    curl -o themes/light.css https://raw.githubusercontent.com/gamosoft/notediscovery/main/themes/light.css
>    curl -o themes/dark.css https://raw.githubusercontent.com/gamosoft/notediscovery/main/themes/dark.css
>    ```
>    
>    ```powershell
>    # Windows PowerShell
>    mkdir data, plugins, themes -Force  # data\ is for YOUR notes
>    Invoke-WebRequest -Uri https://raw.githubusercontent.com/gamosoft/notediscovery/main/config.yaml -OutFile config.yaml
>    # Download at least light and dark themes
>    Invoke-WebRequest -Uri https://raw.githubusercontent.com/gamosoft/notediscovery/main/themes/light.css -OutFile themes/light.css
>    Invoke-WebRequest -Uri https://raw.githubusercontent.com/gamosoft/notediscovery/main/themes/dark.css -OutFile themes/dark.css
>    ```
> 
> 2. **Full Setup** (recommended - includes all themes, plugins, and documentation):
>    ```bash
>    git clone https://github.com/gamosoft/notediscovery.git
>    cd notediscovery
>    # The data/ folder is empty - for your personal notes
>    # The documentation/ folder has app docs you can optionally mount
>    ```

> **🔐 Security Note**: Authentication is **disabled by default** with password `admin`. For testing/local use, this is fine. If exposing to a network, **change the password immediately** - see [AUTHENTICATION.md](documentation/AUTHENTICATION.md) for instructions on how to enable it.

**Option 1: Docker Compose (Recommended)**

> 💡 **Multi-Architecture Support**: Docker images are available for both `x86_64` and `ARM64` (Raspberry Pi, Apple Silicon, etc.)

```bash
# Download the docker-compose file
curl -O https://raw.githubusercontent.com/gamosoft/notediscovery/main/docker-compose.ghcr.yml

# Or if you cloned the repo, just use it directly
docker-compose -f docker-compose.ghcr.yml up -d

# Access at http://localhost:8000
# Login with default password: admin

# View logs
docker-compose -f docker-compose.ghcr.yml logs -f

# Stop the application
docker-compose -f docker-compose.ghcr.yml down
```

**Option 2: Dock