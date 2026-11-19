# Q2108 — saucer diameter (mm), prior: mouse width = 57 mm

Static top-down camera; both objects are static on the desk, so timing/fps doesn't matter. Measured on frame 35 (saucer fully
uncovered; at frame 0 the sleeve covers part of it).

- Mouse (white Magic-Mouse style, tilted −17.5°): width = short-axis extent.
  - Threshold mask minAreaRect: 102.5 x 198 px (frames 0 and 35 agree; frame 20 gives 100.6).
  - Gradient-edge cross-sections perpendicular to the long axis (radial.py): 101–104 px, max over the body ≈ 103.5.
  - Used 103 px → scale = 57/103 = 0.5534 mm/px.
- Saucer: radial gradient-edge scan from the centre (2° steps) + robust least-squares circle fit, 131 points,
  residual std 1.1 px → diameter 250.8 px, centre (1291.5, 1123.7). Overlay in frames/radial.png.
  Second route: white-mask hull ellipse 249.9 x 251.8 px, bbox 251 x 249 (measure.py). Record in scene/ gave ~250. All agree.
- Diameter = 250.8 x 0.5534 = 138.8 mm (range ~137–141 for mouse width 101.5–104 px).

Single planar scale, no perspective correction (annotator convention). Confidence: good (~3%).
