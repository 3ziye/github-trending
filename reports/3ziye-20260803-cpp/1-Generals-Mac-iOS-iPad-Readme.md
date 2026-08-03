# Command & Conquer Generals: Zero Hour — macOS, iOS & iPadOS

<img width="500" height="281" alt="IMG_3457_500" src="https://github.com/user-attachments/assets/aeaf6692-36e6-40c8-b9f8-8066d014ec4b" />

**Zero Hour running natively on Apple Silicon Macs, iPhone, and iPad** — campaign,
skirmish, and Generals Challenge, with touch controls built for RTS (tap-select,
drag-box, long-press deselect, two-finger scroll, pinch zoom). No emulation: this
is the real 2003 engine compiled for ARM64, rendering DirectX 8 →
[DXVK](https://github.com/doitsujin/dxvk) → Vulkan →
[MoltenVK](https://github.com/KhronosGroup/MoltenVK) → Metal.

Built on EA's GPL v3 source release, standing on a chain of community work —
[TheSuperHackers](https://github.com/TheSuperHackers/GeneralsGameCode),
[Fighter19's original Unix port](https://github.com/Fighter19/CnC_Generals_Zero_Hour), and
[fbraz3/GeneralsX](https://github.com/fbraz3/GeneralsX) — this fork adds the iOS/iPadOS
port and a set of engine fixes. See [Lineage & credits](#lineage--credits) for who built
what. The original GeneralsX README lives on the `upstream-main` branch.

**No game assets are included or distributed.** You need your own copy
([Steam](https://store.steampowered.com/app/2732960/), ~$5 on sale).

## What this port actually involved

"Porting" undersells how weird this journey was, so here's the honest shape of it.
The lineage below built the foundation: EA's source release, the community's
modernization, Fighter19's original Unix port, GeneralsX's macOS/Linux work.
What did *not* exist was any of this on iOS — and iOS is a hostile place for a
2003 Windows RTS:

- **The engine assumes a writable filesystem wherever it lives.** iOS apps live in a
  read-only, code-signed bundle. Every config write, cache, and save path had to be
  rerouted — and the working directory bootstrapped from the bundle itself.
- **The renderer speaks DirectX 8. The iPad speaks Metal.** In between: DXVK
  translating D3D8→Vulkan, MoltenVK translating Vulkan→Metal — and DXVK had never
  been built for iPhoneOS. That took a Meson cross-build and a patch to its Vulkan
  loader, because iOS confines `dlopen` to the app bundle ([`Patches/dxvk-ios.patch`](Patches/dxvk-ios.patch)).
- **iOS owns your process.** Open the app switcher and the OS seizes the Metal
  drawable *without backgrounding you* — draw one more frame and you're dead on
  resume. The whole render/sim loop learned to hold its breath.
- **An RTS needs a mouse.** SDL3 (from the lineage below) delivers raw touch events;
  the RTS semantics on top are new. Taps defer until the 2003 GUI has processed
  hover (or menu buttons never highlight), a drag has to decide "selection box or
  camera pan," long-press became right-click, and a cancelled touch must never
  ghost-click a rally point.
- **And then the bug hunts** — the best part. The minimap that rendered black
  because a 2003 texture-format fallback silently dropped the alpha channel. The
  EVA voice that went randomly mute because one zombie audio stream held a global
  "don't talk over speech" flag while chirping forever. Every one chased to root
  cause on a real device, fixed, and offered upstream.

**→ The war stories: [Porting Playbook §8 — the bug archaeology](docs/port/PORTING_PLAYBOOK.md#8-post-ship-bug-hunts-junejuly-2026--the-archaeology-section)**
**→ The complete engineering log: [docs/port/PORTING_PLAYBOOK.md](docs/port/PORTING_PLAYBOOK.md)**
**→ How to do this to another game: [docs/port/PORTING_PATTERNS.md](docs/port/PORTING_PATTERNS.md)**

Worth saying plainly: this was a **human + AI collaboration**. The engineering —
the C++, the cross-builds, the device debugging — was done by
[Claude Code](https://claude.com/claude-code) (Anthropic's Claude, Fable model),
directed and playtested by a human who described symptoms like *"the minimap is
black"* and *"I hear chirping"* and owned every decision. Neither half ships this
alone: one of us can't write C++, and the other can't hear the chirping.

## Quick start — macOS

Prerequisites (one time):

```sh
# Toolchain
xcode-select --install
brew install cmake ninja meson pkgconf
brew install --cask steamcmd

# vcpkg (full clone — a shallow clone breaks manifest baselines)
git clone https://github.com/microsoft/vcpkg ~/vcpkg && ~/vcpkg/bootstrap-vcpkg.sh
export VCPKG_ROOT=~/vcpkg          # add to your shell profile

# LunarG Vulkan SDK (NOT the Homebrew cask) — https://vulkan.lunarg.com/sdk/home
export VULKAN_SDK=$HOME/VulkanSDK/<version>/macOS   # add to your shell profile
```

Clone, build, get assets, play:

```sh
git clone https://github.com/ammaarreshi/Generals-Mac-iOS-iPad.git GeneralsX
cd GeneralsX
./scripts/build/macos/build-macos-zh.sh     # checks deps, configures, builds
./scripts/build/macos/deploy-macos-zh.sh    # creates ~/GeneralsX/GeneralsZH + run.sh
./scripts/get-assets.sh <your_steam_username>   # fetches game data you own
cd ~/GeneralsX/GeneralsZH && ./run.sh -win
```

## Quick start — iPhone / iPad

On 