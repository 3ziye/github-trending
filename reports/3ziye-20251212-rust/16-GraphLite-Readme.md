# GraphLite

**A graph database as simple as SQLite for embedded processes**

GraphLite is a fast, light-weight and portable embedded graph database that brings the power of the new **ISO GQL (Graph Query Language)** standard to the simplicity of SQLite.<p> 
GraphLite uses a single binary and is an ideal solution for applications requiring graph database capabilities without the complexity of client-server architectures.

## Features

- **ISO GQL Standard** - Full implementation of ISO GQL query language based on grammar optimized from [OpenGQL](https://github.com/opengql/grammar/tree/main) project
- **Pattern Matching** - Powerful MATCH clauses for graph traversal
- **ACID Transactions** - Full transaction support with isolation levels
- **Embedded Storage** - Sled-based embedded database (no server needed)
- **Type System** - Strong typing with validation and inference
- **Query Optimization** - Cost-based query optimization
- **Pure Rust** - Memory-safe implementation in Rust

## Prerequisites

Before building GraphLite, you need to install Rust and a C compiler/linker.

<details>
<summary><b>macOS</b></summary>

```bash
# Install Xcode Command Line Tools (C compiler, linker)
xcode-select --install

# Install Rust via rustup
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Restart terminal or run:
source $HOME/.cargo/env

# Verify installation
rustc --version
cargo --version
```
</details>

<details>
<summary><b>Linux (Ubuntu/Debian)</b></summary>

```bash
# Install build essentials
sudo apt-get update
sudo apt-get install build-essential

# Install Rust via rustup
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Restart terminal or run:
source $HOME/.cargo/env

# Verify installation
rustc --version
cargo --version
```
</details>

<details>
<summary><b>Linux (Fedora/RHEL)</b></summary>

```bash
# Install development tools
sudo dnf groupinstall "Development Tools"

# Install Rust via rustup
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Restart terminal or run:
source $HOME/.cargo/env

# Verify installation
rustc --version
cargo --version
```
</details>

## Getting Started

Get up and running with GraphLite in 3 simple steps:

### Step 1: Installation

**Choose your installation method:**

#### Option A: Use as a Crate (Recommended for Rust Applications)

Add GraphLite to your Rust project - no cloning or building required:

```bash
# For application development (SDK - recommended)
cargo add graphlite-rust-sdk

# For advanced/low-level usage
cargo add graphlite
```

**See:** **[Using GraphLite as a Crate](docs/Using%20GraphLite%20as%20a%20Crate.md)** for complete integration guide.

#### Option B: Use Docker (Easiest for Quick Start)

Run GraphLite instantly with Docker - no installation required:

```bash
# Initialize database
docker run -it -v $(pwd)/mydb:/data ghcr.io/graphlite-ai/graphlite:latest \
  graphlite install --path /data/mydb --admin-user admin --admin-password secret

# Start interactive GQL shell
docker run -it -v $(pwd)/mydb:/data \
  -e GRAPHLITE_DB_PATH=/data/mydb \
  -e GRAPHLITE_USER=admin \
  -e GRAPHLITE_PASSWORD=secret \
  ghcr.io/graphlite-ai/graphlite:latest
```

**See:** **[Docker Guide](docs/Docker.md)** for complete Docker setup including multi-architecture builds and Docker Compose.

#### Option C: Install CLI from crates.io

Install the GraphLite CLI tool directly from crates.io:

```bash
cargo install gql-cli
```

After installation, the `graphlite` binary will be available in your PATH.

#### Option D: Clone and Build (For Development/Contributing)

```bash
# Clone the repository
git clone https://github.com/GraphLite-AI/GraphLite.git
cd GraphLite

# Build the project
./scripts/build_all.sh --release
```

After building, the binary will be available at `target/release/graphlite`.

<details>
<summary><b>Custom Build Options</b></summary>

```bash
# Development build (faster compilation, slower runtime)
./scripts/build_all.sh

# Build and run tests
./scripts/build_all.sh --release --test

# Clean build (useful when dependencies change)
./scripts/build_all.sh --clean --release

# View all options
./scripts/build_all.sh --help
```
</details>

<details>
<summary><b>Advanced: Manual Build with Cargo</b></summary>

If you prefer to build manually without the script:

1. Build in `release` mode for production-use:
    ```bash
    cargo build --release
    ```

2. Build in `debug` mode for development:

    ```bash
    cargo build
    ```
</details>

### Step 2: Initialize Database (For CLI Usage)

**Note:** If you're using GraphLite as a crate in your application, skip to **[Using GraphLite as a Crate](docs/Using%20GraphLite%20as%20a%20Crate.md)** instead.

```bash
# If you installed via 'cargo install gql-cli' (Option B)
graphlite install --path ./my_db --admin-user admin --admin-password secret

# If you built from source (Option C)
./target/release/graphlite install --path ./my_db --admin-user admin --admin-password secret
``