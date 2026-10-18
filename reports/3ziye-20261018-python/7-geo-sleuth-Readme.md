<div align="center">

# 🧭 geo-sleuth

**An agent skill that finds where a photo was taken — and shows its work.**

<p align="center">
  <a href="README.md"><img alt="English" src="https://img.shields.io/badge/English-1f6feb?style=flat-square"></a>
  <a href="README.zh-CN.md"><img alt="Simplified Chinese" src="https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-dbeafe?style=flat-square"></a>
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
  <a href="https://www.python.org/downloads/"><img alt="Python 3.10+" src="https://img.shields.io/badge/python-3.10%2B-blue.svg"></a>
  <a href="https://agentskills.io"><img alt="Agent Skill: SKILL.md" src="https://img.shields.io/badge/Agent%20Skill-SKILL.md-8A2BE2.svg"></a>
  <a href="CONTRIBUTING.md"><img alt="PRs welcome" src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg"></a>
  <a href="https://github.com/Oldcircle/geo-sleuth/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/Oldcircle/geo-sleuth?style=social"></a>
</p>

<p align="center">
  <b>Works with</b><br>
  <a href="https://code.claude.com/docs/en/skills"><img alt="Claude Code" src="https://img.shields.io/badge/Claude%20Code-D97757?style=for-the-badge&logo=claude&logoColor=white"></a>
  <a href="https://developers.openai.com/codex/skills"><img alt="Codex" src="https://img.shields.io/badge/Codex-000000?style=for-the-badge"></a>
  <a href="https://cursor.com/docs/skills"><img alt="Cursor" src="https://img.shields.io/badge/Cursor-000000?style=for-the-badge&logo=cursor&logoColor=white"></a>
  <a href="https://geminicli.com/docs/cli/skills/"><img alt="Gemini CLI" src="https://img.shields.io/badge/Gemini%20CLI-1A73E8?style=for-the-badge&logo=googlegemini&logoColor=white"></a>
  <a href="https://opencode.ai/docs/skills/"><img alt="OpenCode" src="https://img.shields.io/badge/OpenCode-211E1E?style=for-the-badge&logo=opencode&logoColor=white"></a>
  <a href="https://docs.github.com/en/copilot/concepts/agents/about-agent-skills"><img alt="GitHub Copilot" src="https://img.shields.io/badge/GitHub%20Copilot-000000?style=for-the-badge&logo=githubcopilot&logoColor=white"></a>
  <br><sub>…and any other agent that reads <code>SKILL.md</code> and runs shell commands.</sub>
</p>

<img src="docs/hero.gif" width="880" alt="From one photo to a camera position: the photo, the region scan, the skyline overlays, the evidence image">

*No text. No plates. No landmarks. One bridge, one mountain. Located to within 2 m.*

</div>

---

## Quick start

```bash
npx skills add Oldcircle/geo-sleuth
```

Pick your agents when prompted. Then hand your agent a photo and say:

> find where this photo was taken

On first use, ask the agent to run `doctor.py` from the installed skill’s `scripts/` folder and address any failed checks (see [Requirements and setup](#requirements-and-setup)). That is the whole interface. The agent reads `SKILL.md`, runs the scripts, and comes back with the camera position, the direction it was facing and a satellite evidence image. Prefer to copy the folder yourself? See [Installation](#installation).

## Why geo-sleuth

- **One photo, one sentence.** Give your agent a photo and say *find where this photo was taken*. You get back the camera position, the direction it was facing, and a satellite evidence image.
- **It works when there is nothing to read.** No sign, no plate, no landmark: OpenStreetMap geometry, elevation data, satellite tiles and street view carry the search on their own.
- **Geometry instead of guesswork.** Pier spacing becomes a distance ruler, shadows become a bearing, a ridge line becomes a fingerprint that elevation data can be matched against.
- **Every claim points at a file.** A conclusion has to name the command that ran in the session and the file it produced. Population and fame are not evidence.
- **Scripts rank, the model judges.** Twenty single-purpose scripts search, score and sort; the model only picks among the top few.
- **One skill, every agent.** A standard Agent Skill — `SKILL.md` plus plain Python scripts — so the same folder runs in Claude Code, Codex, Cursor, Gemini CLI, OpenCode and GitHub Copilot.
- **Answers carry an error radius.** Coordinates ± radius, the camera heading, an evidence image and a graded confidence.

## Cases

None of these photos had GPS data. Each case lists what the skill read from the photo, how it narrowed the search, and how far the result landed from the confirmed camera position.

Each case is a record of one run by one model. The skill tells the agent how to work; what to query, how to filter and how many top results to check are the model's own decisions, so a different model or different decisions may not reach the same result. Under each case, *Reproduction conditions and checkpoints* lists the input, the hint, the key parameters and what each stage should still cover, so you can find the step where your own run diverg