# KisakCOD VR

KisakCOD VR is a single-player OpenXR VR conversion for the original 2007
Windows release of Call of Duty 4: Modern Warfare. It adds stereoscopic
rendering, 6DoF headset tracking, motion-controller weapon aiming, physical
scope support, VR HUD placement, and campaign-specific compatibility fixes.

This project is based on [KisakCOD](https://github.com/SwagSoftware/KisakCOD).
It contains no Call of Duty game data and requires a legitimately installed
copy of the original game.

- [Download the current beta from GitHub](https://github.com/jplakon/CallOfDuty4_VR/releases)
- [Read supporter updates on Patreon](https://www.patreon.com/c/J_Play)

## Current status

The current public beta is `v0.10.0-beta.14`.

Beta.14 fixes the remaining stereo-menu and legacy-crosshair defects, adds
a full-FOV Pimax Crystal Light scope layout, routes Safehouse and Heat
air-support targeting through the right controller, makes the Configurator
fully resizable, and adds a guarded guided installer beside the portable ZIP.
Existing LocalAppData profiles and Controller Input V4 bindings remain
unchanged during an update.

### Beta.14 fixes

- Keeps Mission Select artwork and text in the same eye-local geometry, centers
  Quit Game and Quit Mission dialogs in both eyes, and suppresses COD4's legacy
  flat crosshair in VR even when an older profile has `cg_drawCrosshair 1`.
- Adds the recommended Pimax Crystal Light Full FOV preset: the runtime's
  uncropped `4312x5102` recommendation at output scale `0.80` becomes two
  `3450x4082` eyes plus the 1024-pixel scope panel in a `7924x4082` packed
  surface. The older `7684x3128` / `1.00` cropped preset remains available;
  Quest modes are unchanged.
- Makes the Safehouse and Heat air-support ray, target marker, and strike
  placement follow the tracked right controller. It keeps the normal right
  glove stable and suppresses broken canned arms; the handheld device model is
  still invisible, which is cosmetic rather than a targeting blocker.
- Requests a true `1160x750` Configurator client area and adds resize,
  maximize, restore, and a minimum tracking size so rightmost and bottom
  controls cannot be clipped by Windows/DPI non-client metrics.
- Adds guided Windows Setup as the recommended download while retaining the
  portable ZIP. Setup finds Steam libraries, accepts manual Browse, validates a
  classic COD4 layout before writing, and never guesses how to rearrange an
  unsupported Microsoft/Xbox raw layout.
- Gives install/update/repair a stable identity, backs up and SHA-256-verifies
  every pre-existing managed file, restores those originals on uninstall, and
  preserves COD4 data, saves, and `%LOCALAPPDATA%\KisakCOD-VR` settings.
- Builds Setup and ZIP from one deterministic case-insensitive allowlisted
  payload with matching SHA-256 sidecars. Publishing fixes include Inno
  preprocessor line-break handling, literal `/DName=Value` definitions, Inno
  6/7 close-app compatibility, and escaped smoke-test AppIds.
- Preserves native Windows Setup switches under Git Bash, validates their exact
  JSON argument transport, and waits for Inno's second uninstall phase to write
  `Log closed.` before checking restoration. The final R8 lifecycle test passed
  incomplete-layout rejection, install, repair, uninstall, exact sentinel
  restoration, and game-data retention.
- Retains all 142 settings checks plus the installer-builder suite and focused
  source contracts. Real Pimax Full FOV and Bog mounted-gun headset confirmation
  are still requested from testers.

### Beta.13 fixes retained

- Uses one canonical HUD transform for the real compass ticker/objectives and
  their editor rectangle, and corrects normal-notification bounds so saved
  layouts and live artwork stay aligned.
- Samples frontend and pause menus once into the centered headset view while
  keeping controller cursor hit testing in eye-local coordinates. The normal
  COD4 crosshair now defaults to Off only for new or reset profiles.
- Uses the DXGI 1.1 factory/adapter interfaces required by the SteamVR OpenXR
  D3D11 interoperability path while retaining adapter-LUID and sync-texture
  guards.
- Adds a `7684x3128` Pimax Crystal Light layout: two `3330x3128` eyes plus the
  existing 1024-pixel physical-scope panel. Quest Native and Performance modes
  are unchanged.
- Selects Pimax's 32-bit OpenXR manifest only when Pimax is the active runtime,
  preserves an explicit `XR_RUNTIME_JSON`, and adds a Pimax-only grip-pose
  fallback plus magazine/support/grenade interaction ownership guards.
- Drives mounted-machine-gun `tag_aim` and `tag_aim_animated` from the tracked
  right-controller ray, clamped by COD4's replicated mechanical pitch/yaw
  limits. HMD look remains independent and the fixed scoped Barrett keeps its
  HMD-centered path.
- Retains all 142 configurator settings checks. The new source/runtime contracts
  pass; real Pimax Crystal Light and Bog mounted-gun headset confirmation are
  still requested fro