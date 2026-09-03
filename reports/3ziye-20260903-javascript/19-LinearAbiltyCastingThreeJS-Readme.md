# Elemental Sandbox

A skillshot VFX sandbox built with **Three.js**, **Vite** and hand-written **GLSL**.

Five abilities and two ways to aim them. Four are **line casts**: press the key to arm, a
League-of-Legends style arrow appears on the ground and swings with the mouse, click to fire. The
fifth is a **far cast**: the arrow is replaced by a circle with a deliberately thick boundary that
follows the cursor and answers the only question a ground-targeted AoE has to answer before you
commit — how much space is this going to take.

**Q — Frost Lance.** A fracture front races out along the line while a field of ice crystals
tears up out of the floor behind it — small and dense at your feet, opening into a wall of blades
at the far end, with a cluster thrown up around the impact point.

**E — Storm Lance.** A bolt leaves the caster's hand and a bundle of lightning filaments is drawn
out behind the strike front, holds while it gutters and re-strikes, then blows out. Sparks come
off it the whole way, the floor underneath takes a branching electric burn and a dark scorch, and
the far end gets a shell of ionised air.

**R — Cinder Fall.** A burning rock is lobbed downrange on an arc, trailing a raymarched wake of
burning gas and heating up the whole way: the lava seams splitting its surface prise wider and
brighter as it comes in. It detonates on arrival, throws its own shattered chunks across the floor, and tears the
ground open into a network of molten cracks that keep glowing while the crater burns out.

**F — Nova Beam.** The caster winds a ball of light up in both hands, pulling motes in out of the
air, then lets a column of it out along the line — white-hot core, cyan sheath, gold ribbons
spiralling around it and shock discs racing down it. It *holds* there, burning into the floor and
throwing spray back up the beam, before collapsing to a thread and blinking out. The only cast in
the sandbox that is still happening a second after it landed.

**V — Voltaic Snare.** The far cast. A leash of current is whipped out across the floor, and where
it lands the ring snaps open past its own radius and pulls back onto it: a violet column tears up
out of the middle, tendrils crawl outward to the boundary, arcs run around the rim and the whole
disc burns. It holds there re-striking and hauling the air up into the pillar, then collapses to a
thread. The circle you measured out before the click is exactly the circle you get.

Everything you can see is generated. There are no textures, no sprite sheets and no meshes on
disk except the character: the crystals are procedural geometry, the bolt is a strip of ribbon
placed entirely by a vertex shader, the meteor is an icosphere cratered and sliced by fracture
planes on the CPU, the beam is a parametric tube drawn three times at three radii, the snare's
whole cage is that same ribbon strip threaded along four different parametric paths, the arrow, the
targeting circle, the rime, the burns and the molten cracks are signed-distance and noise shaders,
and the mist, sparks, chips and glitter are GPU particles.

**Every parameter is a live slider** — 938 of them — and they stay live while the simulation is
paused. That is the point of the project: freeze a frame mid-eruption, mid-strike or mid-burn with
**P**, then reshape the silhouette, the palette and the timing against a still image.

References for the look: `icecast.jpg`, `thundercast.jpg`, `superbeam.jpg` and
`electricalboost.jpg`.

---

## Quick start

```bash
npm install
```

```bash
npm run dev
```

Then open the URL Vite prints (default <http://127.0.0.1:5173>).

```bash
npm run build
```

```bash
npm run preview
```

### Assets

Six binary assets are served from `public/` and loaded automatically at boot:

| File | Purpose |
| --- | --- |
| `public/models/Idle.fbx` | Rigged character **and** its idle animation clip |
| `public/models/diffuse.png` | The character's colour map |
| `public/models/cast1.fbx` | Cast animation |
| `public/models/cast2.fbx` | Cast animation |
| `public/models/cast3.fbx` | Cast animation — the default for Frost Lance, Root Snare and Glacier Crown |
| `public/hdri/spruit_sunrise.hdr` | HDR probe used for image-based lighting and crystal reflections |

All four FBX files are Mixamo exports of the same rig, each carrying a skinned mesh plus one
animation stack. The character comes from the idle file; the cast files are loaded for their clip
alone, and the duplicate rig that arrives with each one is released the moment its `AnimationClip`
has been taken. Clips bind to the skeleton by bone name, which is the whole reason an animation
authored in another file plays here without retargeting.

The rig ships no material, so `diffuse.png` is loaded beside it and assigned as the colour map when
the imported materials are converted to PBR — an FBX that *does* carry an embedded texture keeps its
own, since that map is authored against its own UVs.

Every ability picks the clip it throws — `castAnim` in its s