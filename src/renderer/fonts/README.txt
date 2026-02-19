NocCraft.ttf

This is a small pixel-style TrueType font generated locally for the UI.
It is NOT the official Minecraft font.

Implementation note:
- The glyph shapes are rasterized and pixelated from an open system font
  (DejaVu Sans / DejaVu Sans Bold) to provide Cyrillic coverage.
- The resulting font is named "NocCraft" to avoid any trademarked names.

If you want to replace it with another font:
- Put your .ttf into this folder
- Update @font-face in src/renderer/styles.css
