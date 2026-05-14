<div align="center">

<img src="assets/text-to-cad-demo.gif" alt="Demo of the CAD skill generating and previewing CAD geometry" width="100%">

<br>

# CAD Skills

A collection of agent skills for CAD, robotics and hardware design

[Docs](https://www.cadskills.xyz) | [Demo](https://demo.cadskills.xyz)

[![GitHub stars](https://img.shields.io/github/stars/earthtojake/text-to-cad?style=for-the-badge&logo=github&label=Stars)](https://github.com/earthtojake/text-to-cad/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/earthtojake/text-to-cad?style=for-the-badge&logo=github&label=Forks)](https://github.com/earthtojake/text-to-cad/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)
[![Follow @soft_servo](https://img.shields.io/badge/Follow-%40soft__servo-000000?style=for-the-badge&logo=x)](https://x.com/soft_servo)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](skills/cad/requirements.txt)
[![build123d](https://img.shields.io/badge/build123d-CAD-00A676?style=for-the-badge)](https://github.com/gumyr/build123d)
[![OCP](https://img.shields.io/badge/OCP-OpenCascade-2F80ED?style=for-the-badge)](skills/cad/requirements.txt)
[![STEP](https://img.shields.io/badge/STEP-Export-4A5568?style=for-the-badge)](skills/cad/SKILL.md)
[![STL](https://img.shields.io/badge/STL-Export-4A5568?style=for-the-badge)](skills/cad/SKILL.md)
[![3MF](https://img.shields.io/badge/3MF-Export-4A5568?style=for-the-badge)](skills/cad/SKILL.md)
[![URDF](https://img.shields.io/badge/URDF-Robots-6B46C1?style=for-the-badge)](skills/urdf/SKILL.md)
[![SDF](https://img.shields.io/badge/SDF-Simulation-6B46C1?style=for-the-badge)](skills/sdf/SKILL.md)
[![SRDF](https://img.shields.io/badge/SRDF-MoveIt2-6B46C1?style=for-the-badge)](skills/srdf/SKILL.md)

</div>

## ✨ Features

- **Generate** - Create source-controlled CAD models with coding agents like Codex and Claude Code.
- **Export** - Produce STEP, STL, 3MF, DXF, GLB, topology data, and URDF/SDF/SRDF robot descriptions.
- **Browse** - Inspect generated geometry, flat patterns, and robot-description files in CAD Explorer.
- **Source** - Find and download off-the-shelf STEP parts from the hosted step.parts catalog.
- **Reference** - Copy stable `@cad[...]` references so agents can make precise follow-up edits.
- **Review** - Render quick review images for fast checks during an iteration loop.
- **Reproduce** - Edit source files first, then regenerate explicit targets.
- **Local** - Run harness, skills and explorer locally with no backend to host.

## 🧰 Skills

- **CAD Skill** - STEP, STL, 3MF, DXF, GLB/topology, render images, and `@cad[...]` geometry references. [Bundled skill](skills/cad/SKILL.md) · [Standalone repo](https://github.com/earthtojake/cad-skill)
- **step.parts Skill** - Find, evaluate, and download common off-the-shelf STEP models from step.parts, including screws, nuts, washers, bearings, standoffs, electronics parts, motors, and connectors. [Bundled skill](skills/step-parts/SKILL.md)
- **CAD Explorer Skill** - Start or reuse CAD Explorer and return visual review links for generated `.step`, `.stp`, `.stl`, `.3mf`, `.dxf`, `.urdf`, `.srdf`, and `.sdf` files. [Bundled skill](skills/cad-explorer/SKILL.md)
- **URDF Skill** - Generated URDF XML, robot links, joints, limits, validation, mesh references, and CAD Explorer URDF visualization. [Bundled skill](skills/urdf/SKILL.md)
- **SDF Skill** - Generated SDFormat/SDF XML, simulator model/world structure, validation, mesh URIs, plugins, and simulator-specific metadata. [Bundled skill](skills/sdf/SKILL.md)
- **SRDF Skill** - MoveIt2 SRDF semantics, direct SRDF-to-URDF Explorer links, inverse kinematics, path planning, and optional MoveIt2-server testing for existing URDFs. [Bundled skill](skills/srdf/SKILL.md)
- **SendCutSend Skill** - SendCutSend.com-specific DXF and STEP/STP upload preflight reports using its ordering guide, catalog, and specs for selected materials, SKUs, services, and secondary operations. [Bundled skill](skills/sendcutsend/SKILL.md)

## 🧩 Harness

The `harness/` directory contains optional repo-level instruction files for larger CAD projects that will be edited by coding agents. These files keep project behavior predictable: edit sources before derived artifacts, regenerate explicit targets, avoid broad repo scans, treat CAD outputs as LFS-heavy, and keep reusable workflow details in the skills themselves.

To use the harness in another CAD project, copy `harness/AGENTS.md` and `harness/CLAUDE.md` into that project's root.

## 💻 Installation

Clone once for script installs, then choose your agent:

```bash
git clone https://github.com/earthtojake/text-to-cad.git
cd text-to-cad
```

### Codex

```bash
./scripts/codex-install.sh
```

Installs to `${CODEX_HOME:-$HOME/.codex}/skills`.

### Claude Code

```bash
./scripts/claude-install.sh
```

Installs to `${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills