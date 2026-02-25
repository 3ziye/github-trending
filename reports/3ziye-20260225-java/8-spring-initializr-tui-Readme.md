# Spring Initializr TUI

[![Release Native Binaries](https://github.com/danvega/spring-initializr-tui/actions/workflows/release.yml/badge.svg)](https://github.com/danvega/spring-initializr-tui/actions/workflows/release.yml)

An interactive terminal UI for scaffolding Spring Boot projects, powered by the [start.spring.io](https://start.spring.io) API. Built with [TamboUI](https://tamboui.dev), a declarative Java TUI framework.

I had an idea to improve my personal workflow for scaffolding Spring Boot projects, so I made a [video](https://youtu.be/J9C2MiQTIYs) about it. This is the code that goes along with that video.

## Table of Contents

- [Screenshots](#screenshots)
- [Features](#features)
- [Supported Platforms](#supported-platforms)
- [Requirements](#requirements)
- [Build & Run](#build--run)
- [Setting Up Shell Access](#setting-up-shell-access)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Themes](#themes)
- [Open in Terminal](#open-in-terminal)
- [Post-Generate Hook](#post-generate-hook)
- [About TamboUI](#about-tamboui)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)
- [License](#license)

## Screenshots

### Splash Screen
The app launches with a Spring-styled ASCII art logo and a progress bar while it fetches metadata from the start.spring.io API.
![Splash Screen](screenshots/splash_screen.png)

### Main Screen
The main configuration form lets you set your project type, language, Spring Boot version, group, artifact, description, packaging, Java version, and more. Below the form is a searchable, categorized dependency picker where you can browse and toggle dependencies.
![Main Screen](screenshots/main_screen.png)

### Explore Build Files
Preview your generated build file before downloading. Switch between `pom.xml`, `build.gradle`, and `build.gradle.kts` with syntax-highlighted content and line numbers. Your current project settings are displayed at the top for reference.
![Explore](screenshots/explore.png)

### Generate & Open in IDE
After generation, the project is extracted to your chosen directory. The app auto-detects installed IDEs (IntelliJ IDEA, VS Code, etc.) and lets you open the project directly, open in your terminal, generate another, or quit.
![Generate](screenshots/generate.png)

### Help
A quick-reference help overlay showing all keyboard shortcuts organized by screen — Main Screen, Explore Screen, and Generate Screen.
![Help](screenshots/help.png)

## Features

- Configure Spring Boot projects entirely from your terminal (group, artifact, Boot version, Java version, packaging, language)
- Search and select dependencies with a categorized picker and fuzzy search
- Filter dependencies by category and surface recently used dependencies
- Explore generated build files with syntax highlighting before downloading
- Switch between `pom.xml`, `build.gradle`, and `build.gradle.kts` previews
- Generate and extract projects to the current working directory
- Auto-detect and launch IDEs (IntelliJ IDEA, VS Code, Cursor, Eclipse, NetBeans)
- "Open in Terminal" option prints the project path and a ready-to-copy `cd` command
- Cross-platform support (macOS, Linux, Windows)
- Remembers your preferences between sessions

## Supported Platforms

- macOS (aarch64)
- Linux (x86_64)
- Windows (x86_64)

## Requirements

- **JDK 25** (LTS)
- **Maven 3.9+**
- **GraalVM 25** (optional, for native image)

## Build & Run

### JVM

```bash
mvn compile exec:java
```

### JAR

```bash
mvn package -DskipTests
java --enable-preview -jar target/spring-initializr-tui-0.1.1.jar
```

### Native Image (GraalVM)

Compile to a standalone native binary for instant startup:

```bash
mvn clean -Pnative package -DskipTests
./target/spring-initializr-tui
```

> Requires GraalVM 25 as your `JAVA_HOME`. If using SDKMAN: `sdk use java 25.0.2-graalce`

## Setting Up Shell Access

For quick access from any directory, set up an alias or add the binary to your PATH.

### macOS / Linux

Add an alias to `~/.zshrc` or `~/.bashrc`:

```bash
alias spring='/path/to/spring-initializr-tui'
```

Then reload your shell:

```bash
source ~/.zshrc
```

### Windows

Add the directory containing `spring-initializr-tui.exe` to your PATH, or create a doskey alias:

```cmd
doskey spring="C:\path\to\spring-initializr-tui.exe" $*
```

To make it permanent, add the binary's directory to your system PATH via **Settings > System > About > Advanced system settings > Environment Variables**, or use PowerShell:

```powershell
$binDir = "C:\path\to"
$path = [Environment]::GetEnvironmentVariable("Path", "User")
[Environment]::SetEnvironmentVariable("Path", "$path;$binDir", "User")
```

### Usage

Once configured, create a new project from anywhere:

```bash
mkdir my-project && cd my-project
spring
```

The generated project will be extracted into the current working directory.

## Keyboard Shortcuts

### Main Screen

| Key | Action |
|---|---|
| `Tab` / `Shift+Tab` | Navigate between fields |
| `Left` / `R