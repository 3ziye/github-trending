<p align="center">
  <img src="icon.png" alt="Aether Icon" width="256" height="256">
</p>

https://github.com/user-attachments/assets/d0571670-e98f-4717-834c-34d6a2ec53f1

# Aether

A visual theming application for Omarchy. Create beautiful desktop themes through real-time color manipulation, wallpaper integration, and template-based theme generation.

## Key Features

- **Intelligent Color Extraction** - Advanced ImageMagick-based algorithm with automatic image classification (monochrome, low-diversity, chromatic)
- **Smart Palette Generation** - Adaptive strategies ensure readability and preserve image aesthetics
- **Image Filter Editor** - Apply blur, exposure, vignette, grain, and 12 presets before color extraction
- **Wallpaper Browsing** - Integrated wallhaven.cc browser, local wallpaper manager, and favorites system
- **Color Presets** - 10 popular themes: Dracula, Nord, Gruvbox, Tokyo Night, Catppuccin, and more
- **Advanced Color Tools** - Harmony generator, gradients, and adjustment sliders (vibrance, contrast, temperature)
- **Color Lock System** - Protect specific colors while experimenting with adjustments
- **Blueprint System** - Save and share themes as JSON files
- **Neovim Themes** - 37 LazyVim-compatible themes with preset matching
- **Shader Manager** - 80+ GLSL screen shaders for hyprshade (color grading, effects, era vibes)
- **Accessibility Checker** - Real-time WCAG contrast ratio validation
- **Customizable UI** - Live theme reload and CSS variable system
- **Multi-App Support** - Hyprland, Waybar, Kitty, Alacritty, btop, Mako, and 15+ more applications

## Requirements

- GJS (GNOME JavaScript bindings)
- GTK 4
- Libadwaita 1
- libsoup3 - HTTP client library for wallhaven API
- **ImageMagick** - Intelligent color extraction and image filter processing
- **hyprshade** - Screen shader manager (optional, for shader effects)
- **Omarchy** - Distro

## Installation

1. Install system dependencies:
```bash
sudo pacman -S gjs gtk4 libadwaita libsoup3 imagemagick
```

2. Clone the repository:
```bash
git clone https://github.com/bjarneo/aether.git
cd aether
```

3. Run Aether:
```bash
./aether
```

To open with a specific wallpaper:
```bash
./aether --wallpaper /path/to/image.png
# or short form
./aether -w /path/to/image.png
```

4. (Optional) Install desktop entry:
```bash
cp li.oever.aether.desktop ~/.local/share/applications/
```

Or install via AUR:
```bash
yay -S aether
# or
paru -S aether
```

## Usage

### Command Line Options

```bash
./aether [OPTIONS]

Options:
  -h, --help              Show help message
  -w, --wallpaper=FILE    Path to wallpaper image to load on startup
```

Example:
```bash
./aether --wallpaper ~/Pictures/wallpaper.jpg
```

### Basic Workflow

1. **Create a palette:**
   - Upload a wallpaper and extract colors with intelligent ImageMagick algorithm
   - (Optional) Edit wallpaper with filters before extraction
   - Browse wallhaven.cc, local wallpapers, or favorites
   - Choose from 10 color presets
   - Generate color harmonies or gradients

2. **Customize colors:**
   - Adjust individual colors with the color picker
   - Use sliders: vibrance, contrast, brightness, hue, temperature
   - Lock colors to protect them from slider adjustments

3. **Apply theme:**
   - Click "Apply Theme" button
   - Aether processes templates and writes to `~/.config/omarchy/themes/aether/`
   - Runs `omarchy-theme-set aether` to apply across all configured applications

Changes apply instantly via live reload.

### Screen Shaders

Aether includes many GLSL screen shaders for hyprshade. Shaders are automatically installed to `~/.config/hypr/shaders/` when you run Aether. Use the Shader Manager in the Settings sidebar to toggle effects, or bind them directly in your Hyprland config.

**Shader Location:** `~/.config/hypr/shaders/`

Add your own `.glsl` files to this directory and they will automatically appear in the Shader Manager list. For GLSL shader tutorials, see [The Book of Shaders](https://thebookofshaders.com/), [Shadertoy](https://www.shadertoy.com/), or [LearnOpenGL - Shaders](https://learnopengl.com/Getting-started/Shaders).

**Manual Binding Example:**
```conf
# In ~/.config/hypr/hyprland.conf
bind = $mainMod, F1, exec, hyprshade toggle grayscale
bind = $mainMod, F2, exec, hyprshade toggle retro-glow
bind = $mainMod, F3, exec, hyprshade off
```

**Shader Categories:**
- Color corrections (grayscale, sepia, duotone, tritone)
- Temperature adjustments (warm-tone, cool-tone, amber, blue-light-reduce)
- Saturation effects (saturate, desaturate, color-pop, pastel)
- Era vibes (40s, 50s, 60s, 70s, 80s, 90s, 00s)
- Artistic looks (golden-hour, cyberpunk-neon, vintage-film, faded-memory)
- Nature themes (forest-green, ocean, arctic-blue, desert-sand, autumn-leaves)
- Accessibility (protanopia, deuteranopia, tritanopia, high-contrast)

### Color Extraction Algorithm

Aether uses an advanced ImageMagick-based extraction system that:

- **Automatically classifies images** as monoc