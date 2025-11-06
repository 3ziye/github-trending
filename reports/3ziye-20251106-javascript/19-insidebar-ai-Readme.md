# insidebar.ai

> Your AI command center: ChatGPT, Claude, Gemini, Google AI, Grok, and DeepSeek—all in one sidebar

![Version](https://img.shields.io/badge/version-1.6.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Languages](https://img.shields.io/badge/languages-10-brightgreen.svg)

**Quick access to multiple AI assistants without switching tabs.** Open the sidebar, choose your AI, and start chatting. All your AI conversations in one place, with your existing logins.

![insidebar.ai in action](Screenshots/1280x800_insidebar-ai-grok-opened.png)

---

## Quick Navigation

- [Features](#features)
- [Installation](#installation)
  - [Chrome Web Store (Recommended)](#chrome-web-store-recommended)
  - [Manual Installation (Advanced)](#manual-installation-advanced)
- [Supported AI Providers](#supported-ai-providers)
- [How to Use](#how-to-use)
- [Screenshots](#screenshots)
- [Privacy & Security](#privacy--security)
- [Troubleshooting](#troubleshooting)
- [Support & Contributing](#support--contributing)

---

## Features

### 🤖 6 AI Providers in One Sidebar

ChatGPT, Claude, Gemini, Google AI Mode, Grok, and DeepSeek — all accessible with one click. No more juggling tabs.

Switch between providers using the tabs at the bottom of the sidebar. Each session persists, so you can return to any conversation right where you left off.

### 📚 Prompt Library

Save, organize, and reuse your best prompts across any AI provider.

- **50+ Curated Prompts**: Import a starter library covering coding, writing, analysis, and more
- **Categories & Tags**: Organize prompts for easy discovery
- **Variables Support**: Create dynamic templates with placeholders
- **Search & Filter**: Find prompts instantly by keyword or favorite status
- **Import/Export**: Share prompt libraries or back up your collection

![Prompt Library](Screenshots/1280x800_insidebar-ai-insert-prompt-to-context.png)

### 💬 Chat History

Save important conversations from any AI provider. Never lose a valuable discussion.

- **Universal Saving**: Works with ChatGPT, Claude, Gemini, Grok, and DeepSeek
- **Full Markdown Rendering**: Conversations display beautifully with code highlighting
- **Search & Filter**: Find conversations by provider or content
- **Original Links**: Access the original conversation URL anytime

![Chat History](Screenshots/1280x800_insidebar-ai-chat-history.png)

### ⌨️ Powerful Keyboard Shortcuts

- **`Cmd/Ctrl+Shift+E`**: Open sidebar instantly
- **`Cmd/Ctrl+Shift+P`**: Access prompt library
- **Customizable Enter Behavior**: Configure Enter vs Shift+Enter for each AI provider
  - Choose from presets: Default, Swapped, Slack-style, Discord-style, or create your own

### 🎨 Your Preferences, Your Way

**Source URL Control** (New in v1.6.0)
Choose where URLs appear when sending selected text or page content:
- At the end (after content)
- At the beginning (before content)
- Don't include URL (save tokens)

**Theme Customization**
Auto-detect system theme or set Light/Dark mode manually

**Language Support**
Available in 10 languages: English, Chinese (Simplified & Traditional), Japanese, Korean, Spanish, French, German, Italian, and Russian

**Provider Management**
Enable only the AI providers you use. Set your default provider.

![Settings](Screenshots/1280x800_insidebar-ai-settings.png)

### 🔒 Privacy First

- **No API keys required**—uses your existing browser logins
- **All data stays local** in your browser's storage
- **Zero tracking, zero analytics**—we don't collect anything
- **Fully open source**—review the code before installing

---

## Installation

Choose your installation method:

### Chrome Web Store (Recommended)

**One-click installation. Automatic updates. No developer mode needed.**

1. Visit the [Chrome Web Store page](https://chromewebstore.google.com/detail/insidebarai/jhlfjcmiemebjjnbdoddhoohbdjnfece)
2. Click **"Add to Chrome"**
3. Click **"Add Extension"** in the popup
4. Done! Click the extension icon or press `Cmd/Ctrl+Shift+E`

**Also works on Microsoft Edge:** Install from Chrome Web Store using Edge browser.

---

### Manual Installation (Advanced)

**For developers or users who prefer manual control.**

Perfect if you want to:
- Review the source code before installing
- Install a development or unreleased version
- Avoid automatic updates
- Have full control over when to update

<details>
<summary><b>Click to expand: Manual installation instructions</b></summary>

#### Chrome Installation

1. **Download** the latest release from [GitHub Releases](https://github.com/xiaolai/insidebar-ai/releases) or click **Code → Download ZIP** on the main repository page
2. **Extract** the ZIP file to a permanent location (don't delete this folder after installation)
3. **Open Chrome** and navigate to `chrome://extensions/`
4. **Enable** "Developer mode" using the toggle in the top right corner
5. **Click** "Load unpacked" button
6. **Select** the extracted folder containing `manifest.json`
7. **Don