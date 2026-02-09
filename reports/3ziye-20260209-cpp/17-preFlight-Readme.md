<p align="center">
  <img src="resources/icons/preFlight.png" alt="preFlight logo" width="600">
</p>

# preFlight

**The Engineer's Slicer**

preFlight is an advanced 3D printing slicer built for precision and performance. Building on the Slic3r legacy as a spiritual successor to PrusaSlicer, it offers exclusive features and a comprehensive under-the-hood overhaul, bringing the entire dependency stack up to modern standards. Given this massive modernization, preFlight has evolved beyond the constraints of the original codebase, making upstream merging irrelevant.

## oozeBot

Based in Georgia, USA, oozeBot is a small but ambitious team currently preparing for the take-off of our Elevate line of 3D printers. preFlight is the cornerstone of the ecosystem we are building - a genuinely new option in the 3D printing space designed to benefit all makers, regardless of the hardware they use.

## Donate

While preFlight is open-source and free for everyone, your support helps us maintain the infrastructure, fund R&D, and keep our team in orbit. If you find value in our tools, consider contributing to the mission.

[Support the preFlight Mission (via Stripe)](https://donate.stripe.com/eVqfZbgoVf9y1c1aXe63K00)

## Requirements

**Windows only** at this time. Linux and macOS support coming soon.

**Required:** [Microsoft Visual C++ Redistributable (x64)](https://aka.ms/vs/17/release/vc_redist.x64.exe) - Install this first if preFlight won't launch.

## Security & Authenticity

To ensure the integrity of your installation and protect yourself, please following these security guidelines:

* **Official Downloads:** Only download preFlight binaries directly from our [GitHub Releases](https://github.com/oozebot/preFlight/releases) page. We do not distribute preFlight through third-party mirror sites.
* **Verified Signature:** All official Windows binaries are digitally signed by **oozeBot, LLC** using an **Organization Validation (OV) Code Signing Certificate**. 
* **Verification:** Before running the installer, right-click the file, select **Properties**, and navigate to the **Digital Signatures** tab. Ensure the "Name of signer" is explicitly listed as **oozeBot, LLC**.
* **Safety First:** If you receive a "Windows protected your PC" (SmartScreen) warning on a file that is *not* signed by oozeBot, LLC, do not proceed with the installation and [report the issue](https://github.com/oozebot/preFlight/issues) immediately.

## Why preFlight?

| What You Get | The Difference |
|--------------|----------------|
| **Athena Perimeter Generator** | Independent overlap control no other slicer offers |
| **Interlocking Perimeters** | Enhanced Z-bonding without added cost or complexity |
| **True 64-bit Architecture** | No coordinate overflow, no silent failures |
| **High Precision** | Clipper2 compiled with 10-decimal high precision |
| **In-Memory Processing** | No temp files, ~50% less RAM usage |
| **Modern Stack** | C++20, Clipper2, Boost 1.90, CGAL 6.1, OpenCASCADE 7.9, Eigen 5.0 |

---

## Flagship Features

### Athena Perimeter Generator

In Greek mythology, Athena defeated Arachne not through greater complexity, but through discipline and precision. We named our perimeter generator after her for the same reason.

**Why Athena Exists**

We forked Arachne to modernize it in several ways. Athena uses **fixed extrusion width** instead of variable and **independent overlap control** between perimeters. Arachne calculates overlap automatically. Athena lets you specify exactly how much perimeters overlap. It even enables negative overlap for creating gaps between perimeters.

#### Unique Controls

| Setting | What It Controls | Range |
|---------|------------------|-------|
| `Ext. perimeter/perimeter overlap` | Gap between external wall and first internal wall | -100% to +100% |
| `Perimeter/perimeter overlap` | Gap between all internal perimeters | -100% to +80% |
| `Perimeter compression` | How aggressively perimeters narrow in tight areas | |

- **Positive overlap**: Perimeters merge into each other (stronger bonding)
- **Zero overlap**: Perimeters just touch
- **Negative overlap**: Gap between perimeters (useful for flexible or soft materials)

#### Additional Characteristics

- Fixed extrusion widths with variation absorbed in spacing, not width
- Predictable wall shell thickness
- Full thin wall support

**When to Use Athena:** You need control over how perimeters bond, want consistent external perimeter width, or are tuning for strength/flex behavior.

**When to Use Arachne:** You prefer automatic overlap calculation or don't care about perimeter spacing.

### Interlocking Perimeters

A novel approach to layer bonding using **spacing variation and compression bonding** - fundamentally different from "brick layers".

**How it works:**
- Alternates perimeter spacing between layers (X/Y axis manipulation)
- Over-extrusion compresses material into horizontal gaps
- Creates diagonal bonding surfaces as material compresses into 