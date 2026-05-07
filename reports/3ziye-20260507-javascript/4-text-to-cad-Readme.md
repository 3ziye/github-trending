<div align="center">

<img src=".assets/text-to-cad-demo.gif" alt="Demo of the text-to-cad harness generating and previewing CAD geometry" width="100%">

<br>

# ⚙ Open Source Text to CAD Harness ⚙

An open source harness for generating 3D models with your favorite coding agent

[Demo project](https://text-to-cad.earthtojake.com)

[![GitHub stars](https://img.shields.io/github/stars/earthtojake/text-to-cad?style=for-the-badge&logo=github&label=Stars)](https://github.com/earthtojake/text-to-cad/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/earthtojake/text-to-cad?style=for-the-badge&logo=github&label=Forks)](https://github.com/earthtojake/text-to-cad/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)
[![Follow @soft_servo](https://img.shields.io/badge/Follow-%40soft__servo-000000?style=for-the-badge&logo=x)](https://x.com/soft_servo)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](.agents/skills/cad/requirements.txt)
[![build123d](https://img.shields.io/badge/build123d-CAD-00A676?style=for-the-badge)](https://github.com/gumyr/build123d)
[![OCP](https://img.shields.io/badge/OCP-OpenCascade-2F80ED?style=for-the-badge)](.agents/skills/cad/requirements.txt)
[![STEP](https://img.shields.io/badge/STEP-Export-4A5568?style=for-the-badge)](.agents/skills/cad/SKILL.md)
[![STL](https://img.shields.io/badge/STL-Export-4A5568?style=for-the-badge)](.agents/skills/cad/SKILL.md)
[![3MF](https://img.shields.io/badge/3MF-Export-4A5568?style=for-the-badge)](.agents/skills/cad/SKILL.md)
[![URDF](https://img.shields.io/badge/URDF-Robots-6B46C1?style=for-the-badge)](.agents/skills/urdf/SKILL.md)
[![Robot Motion](https://img.shields.io/badge/Robot%20Motion-IK%20%2B%20Planning-6B46C1?style=for-the-badge)](.agents/skills/robot-motion/SKILL.md)
[![Node.js](https://img.shields.io/badge/Node.js-CAD%20Explorer-339933?style=for-the-badge&logo=node.js&logoColor=white)](.agents/skills/cad/explorer/package.json)
[![React](https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react&logoColor=111111)](.agents/skills/cad/explorer/package.json)
[![Vite](https://img.shields.io/badge/Vite-7-646CFF?style=for-the-badge&logo=vite&logoColor=white)](.agents/skills/cad/explorer/package.json)

</div>

## ✨ Features

- **Generate** - Create source-controlled CAD models with coding agents like Codex and Claude Code.
- **Export** - Produce STEP, STL, 3MF, DXF, GLB, topology data, and URDF robot descriptions.
- **Browse** - Inspect generated geometry in CAD Explorer.
- **Reference** - Copy stable `@cad[...]` references so agents can make precise follow-up edits.
- **Review** - Render quick review images for fast checks during an iteration loop.
- **Reproduce** - Edit source files first, then regenerate explicit targets.
- **Local** - Run the harness and CAD Explorer locally with no backend to host.

## 🧰 Bundled Skills

This harness vendors file-targeted skills for CAD, robot-description, robot-motion, and manufacturing-preflight work. Use the bundled copies here for local CAD projects, or use the dedicated repositories when installing the skills outside this harness.

- **CAD Skill** - STEP, STL, 3MF, DXF, GLB/topology, render images, and `@cad[...]` geometry references. [Bundled skill](.agents/skills/cad/SKILL.md) · [Standalone repo](https://github.com/earthtojake/cad-skill)
- **URDF Skill** - Generated URDF XML, robot links, joints, limits, validation, and mesh references. [Bundled skill](.agents/skills/urdf/SKILL.md) · [Standalone repo](https://github.com/earthtojake/urdf-skill)
- **Robot Motion Skill** - ROS 2/MoveIt setup, CAD Explorer motion artifacts, inverse kinematics, path planning, and motion-server testing for existing URDFs. [Bundled skill](.agents/skills/robot-motion/SKILL.md)

Skills live canonically under `.agents/skills` for Codex. Claude Code compatibility is provided by per-skill symlinks in `.claude/skills`.

## 📸 Screenshots

<table>
  <tr>
    <td width="33%">
      <a href="./.assets/text-to-cad-demo.gif">
        <img src="./.assets/text-to-cad-demo.gif" alt="CAD skill demo showing generated geometry in CAD Explorer" width="100%">
      </a>
      <a href="./.agents/skills/cad/SKILL.md"><strong>CAD</strong></a>
    </td>
    <td width="33%">
      <a href="./.assets/urdf-demo.gif">
        <img src="./.assets/urdf-demo.gif" alt="URDF skill demo showing robot description output in CAD Explorer" width="100%">
      </a>
      <a href="./.agents/skills/urdf/SKILL.md"><strong>URDF</strong></a>
    </td>
    <td width="33%">
      <a href="./.assets/robot-motion-demo.gif">
        <img src="./.assets/robot-motion-demo.gif" alt="Robot Motion skill demo showing inverse kinematics in CAD Explorer" width="100%">
      </a>
      <a href="./.agents/skills/robot-motion/SKILL.md"><strong>Robot Motion</strong></a>
    </td>
  </tr>
</table>

## 🔁 Workflow

1. **Describe** - Tell your agent a