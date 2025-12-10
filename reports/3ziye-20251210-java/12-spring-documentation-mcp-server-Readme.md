# Spring Documentation MCP Server
### (Current Version 1.4.2)
A comprehensive Spring Boot application that serves as a Model Context Protocol (MCP) Server, providing AI assistants with full-text searchable access to Spring ecosystem documentation via Server-Sent Events (SSE).

> Thanks to Dan Vega - https://github.com/danvega/sb4 providing Spring Boot 4 architecture examples - 
> flavors/architecture/danvega-sb4


## What is this?

This MCP server enables AI assistants (like Claude) to search, browse, and retrieve Spring Framework documentation, code examples, and API references. It includes:

- **MCP Server**: SSE-based protocol implementation using Spring AI
- **Documentation Sync**: Automated synchronization from spring.io and GitHub spring-projects repositories
- **Full-Text Search**: PostgreSQL-powered search across all Spring documentation
- **Web Management UI**: Thymeleaf-based interface for managing projects, versions, and documentation
- **Code Examples**: Searchable repository of Spring code snippets
- **Migration Recipes**: OpenRewrite-based migration knowledge for Spring Boot version upgrades
- **Language Evolution**: Java (8+) and Kotlin (1.6+) feature tracking with deprecations and code patterns
- **Flavors**: Company-specific guidelines, architecture patterns, compliance rules, and AI agent configurations
- **Flavor Groups**: Team-based access control with API key membership for secure guideline sharing
- **Boot Initializr**: Spring Initializr integration for dependency search, compatibility checks, and formatted snippets
- **Javadoc API Docs**: Crawled and indexed Javadoc documentation for Spring projects with full-text search

## Table of Contents

- [What is this?](#what-is-this)
- [Changelog](#changelog)
- [Quick Start](#quick-start)
- [API Key Authentication](#api-key-authentication)
- [Features](#features)
  - [Dashboard & Project Management](#dashboard--project-management)
  - [Documentation Management](#documentation-management)
  - [Code Examples](#code-examples)
  - [Migration Recipes](#migration-recipes)
  - [Language Evolution](#language-evolution)
  - [Flavors - Company Guidelines](#flavors---company-guidelines)
  - [Flavor Groups - Team Access Control](#flavor-groups---team-access-control)
  - [Boot Initializr Integration](#boot-initializr-integration)
  - [Javadoc API Documentation](#javadoc-api-documentation)
- [Using with Claude Code](#using-with-claude-code)
  - [Configuration](#mcp-configuration)
  - [Documentation Queries](#documentation-queries)
  - [Migration Planning](#migration-planning)
  - [Language Evolution Queries](#language-evolution-queries)
  - [Company Guidelines & Flavors](#company-guidelines--flavors)
  - [Boot Initializr Queries](#boot-initializr-queries)
  - [Javadoc API Queries](#javadoc-api-queries)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Resources](#resources)

## Changelog

> **Full changelog**: See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

### Recent Releases

| Version   | Date       | Highlights                                                   |
|-----------|------------|--------------------------------------------------------------|
| **1.4.2** | 2025-12-08 | Javadoc API documentation crawler and search (4 MCP tools)   |
| **1.4.1** | 2025-12-07 | GitHub docs keyword fix, configurable sync features          |
| **1.4.0** | 2025-12-06 | Boot Initializr integration, Caffeine caching (5 MCP tools)  |
| **1.3.4** | 2025-12-05 | Spring AI 1.1.1, CVE-2025-48924 security fix                 |
| **1.3.3** | 2025-12-04 | Flavor Groups with team-based access control (3 MCP tools)   |
| **1.3.2** | 2025-12-02 | YAML metadata headers for Flavors import/export, new example |
| **1.3.1** | 2025-12-01 | GitHub documentation scanner, enhanced code examples         |
| **1.3.0** | 2025-11-30 | Flavors feature (8 MCP tools)                                |
| **1.2.0** | 2025-11-29 | Language Evolution tracking (6 MCP tools)                    |
| **1.1.0** | 2025-11-28 | OpenRewrite migration recipes (7 MCP tools)                  |
| **1.0.2** | 2025-11-27 | Spring Boot 3.5.8, example app                               |
| **1.0.1** | 2025-11-26 | Initial release (10 MCP tools)                               |

**MCP Tools**: 10 (docs) + 7 (migration) + 6 (language) + 8 (flavors) + 3 (groups) + 5 (initializr) + 4 (javadocs) = **43 total**

## Quick Start

### Prerequisites

**IMPORTANT**: This project requires **Java 25** (LTS).

```bash
# Install Java 25 with SDKMAN (recommended)
curl -s "https://get.sdkman.io" | bash
sdk install java 25.0.1-tem
sdk use java 25.0.1-tem

# Verify
java -version  # Should show: openjdk version "25"
```

### 1. Start PostgreSQL Database
```bash
docker-compose up -d postgres
```

### 2. Build and Run
```bash
./gradlew clean build
java -jar build/libs/spring-boot-documentation-mcp-server-1.4.2.jar
```

Or usin