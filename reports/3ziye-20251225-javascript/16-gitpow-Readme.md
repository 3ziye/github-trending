<img width="300" height="300" alt="image-Photoroom" src="https://github.com/user-attachments/assets/f25bdc63-c7dd-45d5-b166-e24d76a3e626" />
<img width="500" height="220" alt="image" src="https://github.com/user-attachments/assets/5dfd6463-5af7-405c-992d-d2e61d330936" />
<img width="1080" height="606" alt="image" src="https://github.com/user-attachments/assets/684bd3b6-0697-4b9b-8493-8e6604c551fc" />

# Why?

This is a passion project of mine where I wanted a cross-platform git client, which would tackle some of the pain-points of existing solutions. Namely, conditional strategies to handle larger repositories (i.e. Kubernetes, Linux kernel, etc.) More importantly, I wanted to implement certain ergonomics which I didn't find in other clients, such as: showing image previews to visualize what changed (if an image was replaced, for example), grouping commits by month/year, giving the user more customization over how they wished to see dates (human-readable, versus timestamps), or how many "commits ago" a file was introduced. As a fun challenge, I wanted to provide the user the option to visualize the repo as a vertical, or horizontal graph, which could be navigated (and zoomed in/out of) on a touch-screen. This is a work in progress, and I welcome any suggestions, or better yet - contributions to the project! 😊


## Prerequisites

### All Platforms

1. **Rust** (latest stable version)
   - Install from [rustup.rs](https://rustup.rs/)
   - Verify: `rustc --version`

2. **Node.js** (v18 or later)
   - Install from [nodejs.org](https://nodejs.org/)
   - Verify: `node --version`

3. **wasm-pack**
   - Install: `cargo install wasm-pack`
   - Verify: `wasm-pack --version`

4. **Tauri CLI**
   - Install: `cargo install tauri-cli`
   - Verify: `cargo tauri --version`


### Windows-Specific

- **Microsoft Visual C++ Build Tools** or **Visual Studio** with C++ support
  - Required for building native dependencies
  - Download from [Microsoft](https://visualstudio.microsoft.com/downloads/)

### Linux-Specific

**Note:** These are system-level dependencies required for Tauri applications on Linux. They cannot be bundled with the application and must be installed separately. This is standard practice for Linux GUI applications.

Install system dependencies:

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install -y \
    libwebkit2gtk-4.1-dev \
    build-essential \
    curl \
    wget \
    file \
    libssl-dev \
    libgtk-3-dev \
    libayatana-appindicator3-dev \
    librsvg2-dev \
    libsoup-3.0-dev \
    libjavascriptcoregtk-4.1-dev \
    xdg-utils \
    pkg-config
```

**Quick install script:**
```bash
# The test script can automatically install missing dependencies
./test-linux-build.sh
# When prompted, answer 'Y' to install dependencies
```

**Fedora:**
```bash
sudo dnf install webkit2gtk4.1-devel.x86_64 \
    openssl-devel \
    curl \
    wget \
    file \
    libappindicator-gtk3 \
    librsvg2-devel
```

**Arch Linux:**
```bash
sudo pacman -S webkit2gtk \
    base-devel \
    curl \
    wget \
    openssl \
    libappindicator \
    librsvg
```

### macOS-Specific

1. **Xcode Command Line Tools**
   ```bash
   xcode-select --install
   ```

2. **Homebrew** (recommended)
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

## Building Executables

### Step 1: Install Dependencies

```bash
# Install Node.js dependencies
npm install
```

### Step 2: Build WebAssembly Module

The graph visualization requires a WebAssembly module that must be built first:

**Windows:**
```cmd
cd graph-wasm
wasm-pack build --target web
cd ..
```

**Linux/macOS:**
```bash
cd graph-wasm
wasm-pack build --target web
cd ..
```

**Copy WASM files to static directory:**

**Windows:**
```cmd
if not exist "static\graph-wasm\pkg" mkdir "static\graph-wasm\pkg"
xcopy /Y /I "graph-wasm\pkg\*" "static\graph-wasm\pkg\"
```

**Linux/macOS:**
```bash
mkdir -p static/graph-wasm/pkg
cp -r graph-wasm/pkg/* static/graph-wasm/pkg/
```

### Step 3: Build Executables

#### Windows

**Development Build:**
```cmd
cargo tauri dev
```

**Release Build:**
```cmd
cargo tauri build
```

The executable will be located at:
```
src-tauri/target/release/gitpow.exe
```

**Installer:**
The installer will be created at:
```
src-tauri/target/release/bundle/msi/gitpow_0.1.0_x64_en-US.msi
```

#### Linux

**Quick Test (Recommended):**
```bash
# Use the automated test script
chmod +x test-linux-build.sh
./test-linux-build.sh
```

**Development Build:**
```bash
cargo tauri dev
```

**Release Build:**
```bash
cargo tauri build
```

The executable will be located at:
```
src-tauri/target/release/gitpow-tauri
```
(or `target/release/gitpow-tauri` if building from workspace root)

**Note:** The executable name is `gitpow-tauri` (matching the Cargo package name), not `gitpow`.

**See [LINUX-TEST-GUIDE.md](LINUX-TEST-GUIDE.md) for detailed Linux build instructions and troubleshooting.**

**AppImage:**
```
sr