# Rodney: Chrome automation from the command line

[![PyPI](https://img.shields.io/pypi/v/rodney.svg)](https://pypi.org/project/rodney/)
[![Changelog](https://img.shields.io/github/v/release/simonw/rodney?include_prereleases&label=changelog)](https://github.com/simonw/rodney/releases)
[![Tests](https://github.com/simonw/rodney/actions/workflows/test.yml/badge.svg)](https://github.com/simonw/rodney/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/rodney/blob/main/LICENSE)

A Go CLI tool that drives a persistent headless Chrome instance using the [rod](https://github.com/go-rod/rod) browser automation library. Each command connects to the same long-running Chrome process, making it easy to script multi-step browser interactions from shell scripts or interactive use.

## Architecture

```
rodney start          →  launches Chrome (headless, persists after CLI exits)
                          saves WebSocket debug URL to ~/.rodney/state.json

rodney connect H:P    →  connects to an existing Chrome on a remote debug port
                          saves WebSocket debug URL to ~/.rodney/state.json

rodney open URL       →  connects to running Chrome via WebSocket
                          navigates the active tab, disconnects

rodney js EXPR        →  connects, evaluates JS, prints result, disconnects

rodney stop           →  connects and shuts down Chrome, cleans up state
```

Each CLI invocation is a short-lived process. Chrome runs independently and tabs persist between commands.

## Building

```bash
go build -o rodney .
```

Requires:
- Go 1.21+
- Google Chrome or Chromium installed (or set `ROD_CHROME_BIN=/path/to/chrome`)

## Usage

### Start/stop the browser

```bash
rodney start              # Launch headless Chrome
rodney start --show       # Launch with visible browser window
rodney start --insecure   # Launch with TLS errors ignored (-k shorthand)
rodney connect host:9222  # Connect to existing Chrome on remote debug port
rodney status             # Show browser info and active page
rodney stop               # Shut down Chrome
```

### Navigate

```bash
rodney open https://example.com    # Navigate to URL
rodney open example.com            # http:// prefix added automatically
rodney back                        # Go back
rodney forward                     # Go forward
rodney reload                      # Reload page
rodney reload --hard               # Reload bypassing cache
rodney clear-cache                 # Clear the browser cache
```

### Extract information

```bash
rodney url                    # Print current URL
rodney title                  # Print page title
rodney text "h1"              # Print text content of element
rodney html "div.content"     # Print outer HTML of element
rodney html                   # Print full page HTML
rodney attr "a#link" href     # Print attribute value
rodney pdf output.pdf         # Save page as PDF
```

### Run JavaScript

```bash
rodney js document.title                        # Evaluate expression
rodney js "1 + 2"                               # Math
rodney js 'document.querySelector("h1").textContent'  # DOM queries
rodney js '[1,2,3].map(x => x * 2)'            # Returns pretty-printed JSON
rodney js 'document.querySelectorAll("a").length'     # Count elements
```

The expression is automatically wrapped in `() => { return (expr); }`.

### Interact with elements

```bash
rodney click "button#submit"       # Click element
rodney input "#search" "query"     # Type into input field
rodney clear "#search"             # Clear input field
rodney file "#upload" photo.png    # Set file on a file input
rodney file "#upload" -            # Set file from stdin
rodney download "a.pdf-link"       # Download href/src target to file
rodney download "a.pdf-link" -     # Download to stdout
rodney select "#dropdown" "value"  # Select dropdown by value
rodney submit "form#login"         # Submit a form
rodney hover ".menu-item"          # Hover over element
rodney focus "#email"              # Focus element
```

### Wait for conditions

```bash
rodney wait ".loaded"       # Wait for element to appear and be visible
rodney waitload             # Wait for page load event
rodney waitstable           # Wait for DOM to stop changing
rodney waitidle             # Wait for network to be idle
rodney sleep 2.5            # Sleep for N seconds
```

### Screenshots

```bash
rodney screenshot                         # Save as screenshot.png
rodney screenshot page.png                # Save to specific file
rodney screenshot -w 1280 -h 720 out.png  # Set viewport width/height
rodney screenshot-el ".chart" chart.png   # Screenshot specific element
```

### Manage tabs

```bash
rodney pages                    # List all tabs (* marks active)
rodney newpage https://...      # Open URL in new tab
rodney page 1                   # Switch to tab by index
rodney closepage 1              # Close tab by index
rodney clo