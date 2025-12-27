<p align="center">
  <img src="assets/favorites/logo_sqlit.png" alt="sqlit logo" width="180">
</p>

<h3 align="center">The lazygit of SQL databases</h3>

<p align="center">
  <em>Connect and query your database from your terminal in seconds.</em>
</p>

<p align="center">
  <a href="https://github.com/Maxteabag/sqlit/stargazers"><img src="https://img.shields.io/github/stars/Maxteabag/sqlit?style=flat&color=yellow" alt="GitHub Stars"></a>
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License">
</p>

<p align="center">
  <code>pipx install sqlit-tui</code>
</p>

<p align="center">
  <a href="https://www.buymeacoffee.com/PeterAdams"><img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=flat&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me a Coffee"></a>
</p>

---

### Connect
Supports all major databases: SQL Server, PostgreSQL, MySQL, SQLite, MariaDB, FirebirdSQL, Oracle, DuckDB, CockroachDB, ClickHouse, Snowflake, Supabase, CloudFlare D1, and Turso.

![Database Providers](demos/demo-providers.gif)

### Query
Syntax highlighting. History. Vim-style keybindings.

![Query History](demos/demo-history.gif)

### Results
Load millions of rows. Inspect data, filter by content, fuzzy search, no more squinting eyes looking for what you need!

![Filter results](demos/demo-filter/demo-filter.gif)

### Docker Discovery
Automatically finds running database containers. Press 'Enter' to connect, sqlit figures out the details for you.

![Docker Discovery](demos/demo-docker-picker.gif)

---

## Features

**Connection manager:** Save and switch connections without CLI args

**Just run `sqlit`:** No CLI config needed, pick a connection and go

**Multi-database support:** PostgreSQL, MySQL, SQLite, SQL Server, and 10+ more

**Docker integration:** Auto-detect running database containers

**SSH tunnels:** Connect to remote databases securely with password or key auth

**Secure credentials:** Passwords stored in your OS keyring

**Vim-style editing:** Modal editing for terminal purists

**Query history:** Searchable, per-connection history

**Filter results:** Fuzzy search through millions of rows

**Context-aware help:** Keybindings shown on screen

**Browse databases:** Tables, views, procedures, indexes, triggers, sequences

**Autocomplete:** Tables, columns, and procedures

**CLI mode:** Execute SQL from the command line

**Themes:** Rose Pine, Tokyo Night, Nord, Gruvbox

**Dependency wizard:** Auto-install missing drivers

---

## Motivation

Throughout my career, the undesputed truth was that SSMS was the only respectable way to access a database. It didn't matter that I wasn't a DBA, or that I didn't need complex performance graphs. I was expected to install a gigabyte-heavy behemoth that took ages to launch all for the mere purpose of running a few queries to update and view a couple of rows.

When I switched to Linux, I was suddenly unable to return to the devil I know, and I asked myself: _how do I access my data now?_

The popular answer was VS Code's SQL extension. But why should we developers launch a heavy Electron app designed for coding just to execute SQL?

I had recently grown fond of Terminal UI's for their speed and keybinding focus. I looked for SQL TUIs, but the options were sparse. The ones I found lacked the user-friendliness and immediate "pick-up-and-go" nature of tools I loved, like lazygit, and I shortly returning to vscode sql extension.

Something wasn't right. I asked myself, why is it that running SQL queries can't be enjoyable? So I created sqlit.

sqlit is for the developer who just wants to query their database with a user friendly UI without their RAM being eaten alive. It is a lightweight, beautiful, and keyboard-driven TUI designed to make accessing your data enjoyable, fast and easy like it should be-- all from inside your favorite terminal.

---

## Installation

| Method | Command |
| :----- | :------ |
| pipx *(recommended)* | `pipx install sqlit-tui` |
| uv | `uv tool install sqlit-tui` |
| pip | `pip install sqlit-tui` |

## Usage

```bash
sqlit
```

The keybindings are shown at the bottom of the screen.

### Try it without a database

Want to explore the UI without connecting to a real database? Run with mock data:

```bash
sqlit --mock=sqlite-demo
```

### CLI

```bash
# Run a query
sqlit query -c "MyConnection" -q "SELECT * FROM Users"

# Output as CSV or JSON
sqlit query -c "MyConnection" -q "SELECT * FROM Users" --format csv
sqlit query -c "MyConnection" -f "script.sql" --format json

# Create connections for different databases
sqlit connections add mssql --name "MySqlServer" --server "localhost" --auth-type sql
sqlit connections add postgresql --name "MyPostgres" --server "localhost" --username "user" --password "pass"
sqlit connections add mysql --name "MyMySQL" --server "localhost" --username "user" --password "pass"
sqlit connections add cockroachdb --name "M