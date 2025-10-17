<div align="center">
  <img width="300" alt="Chroma's logo in ASCII rainbow" src="https://github.com/user-attachments/assets/871f6c7b-8b7c-486d-8cae-41ec13ed2d02" />

🌈 A Rust-based, ASCII art shader audio visualizer for your terminal!

  <img src="https://github.com/user-attachments/assets/b71074f2-3e77-4fb9-a8ef-30288a3690c4" width="550" />

</div>

## ⭐ Features

- 🎨 **GPU-accelerated shaders** using wgpu (compute shaders)
- 🖼️ **ASCII art rendering** with ANSI color support
- ⚙️ **Highly configurable parameters** via config file
- 💾 **Save/Load configurations** with automatic deduping via hashing
- 🔄 **Live config reloading** for real-time parameter adjustment
- 🎵 **Audio visualization** driven by system audio input
- 📊 **FFT-based audio analysis** for reactive visual effects

## ✨ Demos & screenshots

🔊 Make sure you turn on sound on the videos!

<img width="2474" height="1248" alt="chroma-themes" src="https://github.com/user-attachments/assets/0f43781d-4276-4d5f-8247-a932df43372e" />

<img width="1958" height="1103" alt="chroma-config" src="https://github.com/user-attachments/assets/96dae99e-2e93-470a-b44f-40c0a09f098a" />

[chroma.webm](https://github.com/user-attachments/assets/9e821a20-8394-445c-9542-91e294225e63)

[chroma-demo-long.webm](https://github.com/user-attachments/assets/3ae02009-b9a5-4003-93b3-8120db869447)

## 🔗 Install

### Arch Linux

```bash
# With an AUR helper: yay
yay -S chroma-visualizer-git

# With an AUR helper: paru
paru -S chroma-visualizer-git

# Or manually:
git clone https://aur.archlinux.org/chroma-visualizer-git.git
cd chroma-visualizer-git
makepkg -si

# If you're lazy:
git clone https://aur.archlinux.org/chroma-visualizer-git.git \
  && cd chroma-visualizer-git \
  && makepkg -si
```

### Other distros

...More packaging coming soon!...

Meanwhile you can build from source below:

### From source (manual)

```bash
# Clone the git repo and enter it:
git clone https://github.com/yuri-xyz/chroma.git
cd chroma

# Make sure you have the `alsa-lib` & `pipewire` packages installed,
# the exact package names may vary depending on your distro.

# Pick one:
cargo build --release                    # visuals only
cargo build --release --features audio   # with audio reactivity (recommended)

# Install the built bin so that you can run it with `chroma`:
sudo install -Dm755 target/release/chroma /usr/local/bin/chroma
```

## ℹ️ Usage

```bash
# Run with default settings
chroma

# Load a saved configuration
chroma --config config_a3f8c2d9e1b5.toml

# Or using the short form
chroma -c config_a3f8c2d9e1b5.toml

# View help for all arguments and settings
chroma --help
```

## 🕹️ Controls

- `Q` or `Esc` - Quit application
- `R` - **Randomize parameters** ⭐ (Discover new effects!)
- `S` - **Save configuration** 💾 (Creates `config_<hash>.toml` in current directory)
- `P`/`O` - **Cycle palettes** 🎨 (16 different character sets!)
- `↑`/`↓` - Adjust frequency
- `→`/`←` - Adjust speed
- `+`/`-` - Adjust amplitude
- `[`/`]` - Adjust scale

See [CONTROLS.md](./notes/CONTROLS.md) and [PALETTES.md](./notes/PALETTES.md) for more details.

## 🎨 Configuration & Ricing

Chroma is designed to be highly configurable and CLI-friendly, so it feels natural alongside your other terminal tools. There are multiple ways to configure the effects and visuals:

**Config files**: Load preset configurations from TOML files. You can find [example preset configs in the `examples` directory](./examples):

```
chroma -c examples/0.toml
```

**Live reloading**: Edit your config file while chroma is running and see changes applied instantly! This makes it easy to tweak parameters and visualize your adjustments in real time.

**CLI parameters**: Most parameters can be set via command-line arguments. Run `chroma --help` to see all available options.

> [!TIP]
> You can combine config files with CLI parameters—CLI args take precedence. This is perfect when you have a favorite base config but want to tweak specific values on the fly or in a script.

> [!TIP]
> Use `--random` or `-r` to randomize any parameters that haven't been explicitly set by your config file or CLI args. Great for adding variety to each run!

If you're feeling brave, you can even create your own custom shader patterns and load them like this: `chroma --custom-shader my_shader.wgsl`. Take a look at [`examples/custom_shader.wgsl`](./examples/custom_shader.wgsl) as a beginner template.

## 📦 Dependencies

- Runtime
  - vulkan-icd-loader
  - A Vulkan driver: one of `vulkan-intel`, `vulkan-radeon`, or `nvidia-utils`
  - Terminal with ANSI color support
- Optional (audio feature)
  - pipewire (recommended) or alsa-lib
- Build
  - rust, cargo, git

## 🏗️ Contributing

All contributions welcome! If you have some cool ideas, found some bugs, or would like to improve the project anyhow, feel free to create an issue and then a corresponding PR :)

Here's some tips to making good contributions:

- ✅ Create a corresponding issue with a reasonable explanation.
- ✅ K