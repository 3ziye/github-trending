# Fly Brain Minecraft

[![build](https://github.com/blendi-remade/fly-brain-minecraft/actions/workflows/build.yml/badge.svg)](https://github.com/blendi-remade/fly-brain-minecraft/actions/workflows/build.yml)
[![code: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE)
[![data: CC BY 4.0](https://img.shields.io/badge/data-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

A Fabric mod for Minecraft 1.21.1 that runs the complete male fruit fly nervous system inside a fly mob.

The connectome is the male *Drosophila melanogaster* central nervous system released by Janelia, Google Research and
the Cambridge connectomics group (neuPrint `male-cns:v1.0`, Berg et al., *Cell*, September 2026): 176,422 neurons and
6.29 million connections of five or more synapses, carrying 90 of the dataset's 125 million synapses. Every neuron is
simulated as a leaky integrate-and-fire unit following Shiu et al. (*Nature* 2024). The Minecraft world drives the fly's
real sensory neurons (photoreceptors, olfactory and gustatory receptor neurons, Johnston's organ, bristles), and the
activity of its real descending and motor neurons is decoded into what the mob does. Each fly runs its own brain on its
own thread, in real time.

![Brain view (B) on the left, neuroscope (H) on the right, a fly in flight with its identity tag](docs/media/hud-brainview-neuroscope.png)

## What you see

Two HUD panels show the brain at work:

- **B, the brain view.** A live map of the whole nervous system (optic lobes top left and right, central brain between
  them, nerve cord below). Neurons light up at their real soma positions as they fire and fade over about 300 ms. Below
  the map: spikes per region for the current tick and a spikes-per-tick history.
- **H, the neuroscope.** The readout: decoded motor channels (forward, yaw, back, stop, land, flight, feed, groom, song),
  firing rates of the key populations (MN9, the giant fibre DNp01, DNa02 left and right, MDN, aDN1/2, LC4, LPLC2, Kenyon
  cells, projection neurons and more), a spike raster, and the retina as the fly sees it.

Every fly gets a persistent number, an identity colour and a matching name tag (`Fly-1 ♂`). The same colour heads both
panels and draws a rotating ring above the fly whose brain you are watching, so with several flies it is always clear
which brain is which.

You can also put the brain into the world: `/flybrain build` places the 141,781 neurons with a reconstructed soma as a
walk-through structure of stained glass coloured by region, and the linked fly's spiking neurons flash as sea lanterns.

![The connectome built out of blocks: brain on the left, nerve cord on the right](docs/media/flybrain-build.png)

## What the fly does

| Behaviour | Trigger in game | Pathway in the connectome | Origin |
|---|---|---|---|
| Feeds (proboscis extension) | Touching cake, honey, berries, fruit, sugar; a player offering food by right-click | sugar GRNs (`LB3b`, `LB3c`, `PhG1a-c`, `LgLG3`) to G2N-1 and Fudog to the MN9 proboscis motor neuron | emergent |
| Rejects bitter food | Spider eye, poisonous potato, pufferfish, rotten flesh | bitter GRNs (`LB1a-d`) to Scapula, MN9 silenced even with sugar present | emergent |
| Escape jump and takeoff | Something approaching fast (a player sprinting at it, a falling block, another mob) | LC4 and LPLC2 looming detectors to the giant fibre DNp01 to the TTMn jump muscle motor neuron | decision emergent, looming drive hand-built |
| Grooms | Rain, dust, collisions | Johnston's organ and head bristles to aDN1/aDN2 and the head grooming descending neurons | emergent |
| Walks, turns, halts | Whatever the brain does with its inputs | DNp09 and the BDN walking neurons, DNa02 right minus left, MDN (backward), bluebell and brake (halt) | readout emergent, gains hand-built |
| Walks toward food | Nearby odor sources | the antennal lobe saturates in this model and gives no reliable steering signal, so a reflex layer takes over while the brain is quiet; the HUD shows `[REFLEX]` when it does | hand-built |
| Flies and lands | Escape jump or takeoff neurons | DNg02 wing power and takeoff neurons enter flight, DNp07/DNp10 land | state machine hand-built |
| Courtship song hooks (males) | Another fly seen, smelled or tapped | pC1/P1 to the pIP10 song neuron, one wing extended | wired, not yet demonstrated |

The point of the project is to be honest about that last column. What comes out of the wiring diagram and what is
scaffolding is spelled out in [docs/REFERENCE.md](docs/REFERENCE.md) and [docs/VALIDATION.md](docs/VALIDATION.md).

## Quick start

Requirements: Minecraft 1.21.1, Fabric Loader 0.17.3 or newer, Fabric API for 1.21.1, Java 21 or newer. A machine with
8 or more cores keeps one fly in real time; more flies share the cores (`maxBrains`, default 4).

Install: put `fruitfly-connectome-<version>.jar` and the Fabric API jar into `.minecraft/mods/`. The 23 MB connectome is
inside the jar, nothing is downloaded at runtime. To