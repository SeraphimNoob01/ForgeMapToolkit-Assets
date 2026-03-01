# Contributing to ForgeMapToolkit Assets

Thank you for your interest in contributing! This document explains how to submit assets and report issues.

---

## What You Can Contribute

- **Skybox presets** — new `.scmskybox` files with preview images
- **Bug reports** — broken previews, wrong folder structure, loading errors

---

## Submitting a Skybox

### Folder Structure

Place your skybox in the correct category folder:

```
skyboxes/
  <Category>/           # e.g. Earth, Desert, Space, Custom
    <SkyboxName>/
      <SkyboxName>.scmskybox
      prev/
        1.png           # Required — shown as card thumbnail
        2.png           # Optional — additional previews
        3.png           # Optional
      assets/           # Custom skyboxes only
        <name>.dds
        <name>_glow.dds
```

### Requirements

- The `.scmskybox` file must be valid JSON
- The copyright block must be present at the top of the file (see below)
- Preview images must be in `prev/`, named `1.png`, `2.png`, `3.png`
- Preview images should be **1920×1080** or **1280×720**, PNG
- Skybox name should be descriptive (e.g. `Arctic_Twilight`, not `test1`)

### Copyright Block

Every `.scmskybox` file must include this comment at the top:

```
    "_copyright": [
        "============================================================",
        " ForgeMapToolkit Assets — Skybox Preset",
        " Copyright (c) 2026 Seraphim-Noob",
        "============================================================",
        "",
        " LICENSE: Creative Commons Attribution-NonCommercial 4.0",
        "          International (CC BY-NC 4.0)",
        "",
        " You are free to:",
        "   - Share  — copy and redistribute this file in any medium",
        "   - Adapt  — remix, transform, and build upon this material",
        "",
        " Under the following terms:",
        "   - NonCommercial — You may not use this material for",
        "                     commercial purposes.",
        "   - No additional restrictions — You may not apply legal",
        "                     terms or technological measures that",
        "                     legally restrict others from doing",
        "                     anything the license permits.",
        "",
        " This copyright block must remain intact in all copies",
        " and derivative works.",
        "",
        " Full license text: https://creativecommons.org/licenses/by-nc/4.0/",
        " Repository:        https://github.com/SeraphimNoob01/ForgeMapToolkit-Assets",
        "============================================================"
    ],
```


## Pull Request Checklist

Before opening a PR, confirm:

- [ ] Files are in the correct folder with the correct structure
- [ ] `.scmskybox` files contain the copyright block
- [ ] Preview images are included in `prev/`
- [ ] No copyrighted third-party assets included without permission
- [ ] PR title clearly describes what is being added

---

## Reporting Issues

Use the **Bug Report** issue template for:
- Missing or broken preview images
- Skyboxes not loading in ForgeMapToolkit
- Incorrect folder structure
- Report only bugs related to the ForgeMapToolKit-Assets repository, not issues originating from the ForgeMapToolkit itself.

Use the **Asset Request** template to request new skyboxes or previews.

---

## Code of Conduct

Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before participating.
