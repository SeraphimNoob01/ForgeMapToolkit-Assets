# ForgeMapToolkit Assets

A curated collection of assets for use with **ForgeMapToolkit** — a Supreme Commander: Forged Alliance map-making tool.

This repository contains:
- **Skybox presets** — ready-to-use `.scmskybox` files with preview images
- **Unit preview images** — PNG thumbnails for all factions including Nomads
- **Prop preview images** — PNG thumbnails for environment props
- **Nomads _unit.bp files** — containing unit information for the Unit-Library

---

## Usage

These assets are loaded automatically by ForgeMapToolkit at scan time.  
No manual installation is required.

### Folder Structure

```
skyboxes/
  <Category>/
    <SkyboxName>/
      <SkyboxName>.scmskybox
      prev/
        1.png
        2.png
        3.png
      assets/           # custom skyboxes only
        <name>.dds
        <name>_glow.dds

nomads/
  <UnitID>/
    <UnitID>_unit.bp

units/
  <UnitID>.png

props/
  <PropName>_albedo.png
```

---

## License

All skybox presets in this repository are licensed under  
**Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.

You may use, share, and adapt them freely for **non-commercial purposes**, provided you give appropriate credit to **Seraphim-Noob** and keep the copyright block intact.

> Unit blueprints sourced from the Nomads mod are the property of their respective authors and are included here solely for tool integration purposes.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on submitting skyboxes, previews, or bug reports.

---

## Credits

Created and maintained by **Seraphim-Noob**.  
Built for use with [ForgeMapToolkit](https://github.com/SeraphimNoob01/ForgeMapToolkit).
