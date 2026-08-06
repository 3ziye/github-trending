<p align="center">
  <img src="./public/assets/avatar.png" alt="Persona avatar" width="96" />
</p>

<h1 align="center">Persona</h1>

<p align="center">
  A realtime character presence for desktop voice experiences.
</p>

<p align="center" style="max-width: 700px; margin:0 auto; border-radius: 8px; overflow: hidden;">
<image src="./public/assets/demo.jpg" alt="Persona demo" width=700 />
</p>

Persona is a cross-platform desktop character that gives voice conversations
an expressive visual identity alongside your work.

## Platform support

| Platform    | Voice output listener            | Distribution               |
| ----------- | -------------------------------- | -------------------------- |
| Linux       | PipeWire playback-stream capture | AppImage and DEB           |
| Windows     | WASAPI process-loopback capture  | NSIS installer             |
| macOS 14.2+ | Core Audio process tap           | DMG and ZIP, arm64 and x64 |

Linux requires `pw-dump` and `pw-record` on `PATH`. Windows process-loopback
requires Windows 10 build 20348 or newer. macOS asks once for System Audio
Recording permission.

Each listener is scoped to an automatically detected or user-selected playback
process. Persona does not capture the microphone, save audio, produce speech,
transcribe content, or send audio over the network.

## Try Persona locally

Requirements:

- Node.js 24 or newer
- npm
- A desktop session with hardware-accelerated graphics

Persona includes a default character model plus idle and speaking motion. You
can replace the model or add more `.vrm` and `.vrma` files from Settings. Other
ignored media under `public/assets/` is not loaded unless declared in the
catalog.

To exercise the packaged-library path with the current ignored local test
media, copy the provided examples over the active published catalogs:

```bash
cp public/assets/library.json.example public/assets/library.json
cp public/assets/manifest.json.example public/assets/manifest.json
```

Both example files are directly usable and also document the complete catalog
format. Their media remains test-only: the example manifest deliberately keeps
distribution disabled and its license fields incomplete.

Packaged VRM files belong under `public/assets/models/`; packaged VRMA files
belong under `public/assets/animations/`. A catalog can declare multiple
packaged models. When `default_model_id` is `null`, Persona selects the first
model record as the packaged default.

```bash
npm install
npm run demo
```

`npm run demo` builds the current renderer and launches Persona with normal
automatic voice-output detection.

For a background launch:

```bash
npm start -- --background
```

## Customize Persona

Open **Settings…** from Persona's tray menu to manage the character library,
choose the voice audio source, and register MCP. You can preview installed
models and animation actions together, choose the default model, set the
character's initial size, and add your own `.vrm` and `.vrma` files.

Until a default model exists, Persona does not create the avatar window or
start its voice-output listener. The first imported model becomes the default
automatically.

Persona always provides **Idle** and **Speaking** action slots. They begin
without media, so the model keeps its normal pose until you add clips. Each
action can contain multiple `.vrma` files; uploads receive numbered names such
as `idle1`, `idle2`, `speaking1`, or `wave1`. Persona chooses a clip from the
action whenever that action runs.

Custom actions include a name, description, and trigger scenario. Persona adds
that metadata to its MCP animation tool so a connected agent can understand
what the action expresses and when to use it. Imported media and configuration
changes stay in Persona's local application data.

Packaged media is immutable. Editing or removing a packaged action creates a
user-level override without changing the installed application. **Reset
packaged actions** restores shipped metadata and visibility while leaving
user-created actions and uploaded clips untouched.

## Connect Persona to Codex

With Persona running, register its local MCP server:

```bash
codex mcp add persona --url http://127.0.0.1:47831/mcp
```

New Codex sessions can then ask Persona to play an installed animation, show or
hide its window, and report whether the local character and voice listener are
active. Persona remains a separate desktop application; the MCP connection
only exposes its own visual controls.

## Local voice apps

Persona does not run language models. To use it with a local model stack, open
**Settings → Voice** and select the running app or Linux playback stream that
produces assistant audio. Advanced users can supply a cross-platform process
pattern, while pipelines that already calculate output levels can use the
external-events mode. Any compatible MCP client can use the same animation
tools as Codex. See [Integrations](docs/INTEGRATIONS.md).

The window intentionally contains no contr