

![Logo of eilmeldung](docs/images/logo.png) 
  

![Screenshot of eilmeldung](docs/images/hero-shot.jpg) 

*eilmeldung* is a *TUI RSS reader* based on the awesome [news-flash](https://gitlab.com/news-flash/news_flash) library.  
- *fast* in every aspect: non-blocking terminal user interface, (neo)vim-inspired keybindings, instant start-up and no clutter
- *stands* on the shoulder of *giants*: based on the news-flash library, *eilmeldung* supports many RSS providers, is efficient and reliable
- *powerful* and yet *easy to use out-of-the-box*: sane defaults which work for most, and yet configurable to meet anyones requirements, from keybindings to colors, from displayed content to RSS provider
- read news like a pro: filter and search news with a easy-to-learn powerful *query language*, activate *zen mode* to focus on the article content and nothing else

*eilmeldung* is German for *breaking news*

---

## Table of Contents

- [Showreel](#showreel)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Quick Reference](#quick-reference)
- [Documentation](#documentation)
- [FAQ](#faq)
- [Credits](#credits)
- [Contributing](#contributing)

---

# Showreel

https://github.com/user-attachments/assets/a8a1dc60-0705-4521-a88d-3520923d2891

This video demonstrates
- basic (vim-like) navigation and reading
- *zen* mode: just show content
- creating new tags and tagging a article
- *filtering* and *searching* article list by using a article queries
- *tagging* multiple articles by using an article query

---

# Installation 

**Quick install:**

- **Homebrew**: `brew tap christo-auer/eilmeldung  https://github.com/christo-auer/eilmeldung && brew install eilmeldung`
- **Arch (AUR)**: `paru -S eilmeldung` or `yay -S eilmeldung`
- **Cargo**: `cargo install --locked --git https://github.com/christo-auer/eilmeldung` (you need to install [build dependencies](docs/installation.md) first!)

**Important**: You need a [Nerd Font](https://github.com/ryanoasis/nerd-fonts) compatible font/terminal for icons to display correctly!

For detailed installation instructions including Nix/Home Manager setup, see **[Installation Guide](docs/installation.md)**.

---

# Quick Start

1. **Install** eilmeldung (see above)
2. **Run** `eilmeldung` - you'll be guided through the initial setup
3. **Choose a provider** (select "Local" if you're new to RSS)
4. **Add feeds** with `c f` or import an OPML file with `:importopml path/to/file.opml`
5. **Sync** your feeds with `s`
6. **Start reading!** Use `j`/`k` to navigate up/down, `h`/`l` to navigate between panels, `o` to open articles in the browser, `z` to enjoy "zen mode"

Press `?` anytime to see all available commands!

For a comprehensive getting started guide, see **[Getting Started](docs/getting-started.md)**.

---

# Quick Reference

Here some key bindings to get you started.

| Key       | Action                                          |
| -----     | --------                                        |
| `?`       | Show all key bindings (search with `/`!)        |
| `s`       | Sync all feeds                                  |
| `j` / `k` | Move down / up                                  |
| `h` / `l` | Move between panels (left/right)                |
| `o`       | Open article in browser, mark as read, jump to next unread |
| `r` / `u` | Mark as read / unread                           |
| `m` / `v` | Mark (star) / unmark article                    |
| `/`       | Search articles                                 |
| `:`       | Open command line                               |
| `q`       | Quit                                            |

**Tip:** Press `?` anytime to see all available commands, and use `/` in the help dialog to search!

---

# Documentation

Complete documentation is available in the `docs/` directory:

- **[Getting Started Guide](docs/getting-started.md)** - Setup and first steps
- **[Installation Guide](docs/installation.md)** - Detailed installation instructions
- **[Key Bindings Reference](docs/keybindings.md)** - Complete keybinding reference
- **[Commands Reference](docs/commands.md)** - All available commands
- **[Article Queries](docs/queries.md)** - Powerful search and filter syntax
- **[Configuration Guide](docs/configuration.md)** - Customize appearance and behavior
- **[Command Line Arguments](docs/cli_args.md)** - Available CLI options
- **[FAQ](docs/faq.md)** - Frequently asked questions

---

# FAQ

### Which providers are supported?

See [news_flash_gtk for all supported providers](https://gitlab.com/news-flash/news_flash_gtk). Note: inoreader is currently **NOT** directly supported.

### Does eilmeldung support smart folders?

Yes! Use queries in your feed list configuration. Example:

```toml
feed_list = [
  'query: "Important Today" #important unread today',
  'query: "Read Later" #readlater unread',
  "feeds",
]
```

### Can I customize keybindings and colors?

Absolutely! Everything is customizable via the [configuration file](docs/config