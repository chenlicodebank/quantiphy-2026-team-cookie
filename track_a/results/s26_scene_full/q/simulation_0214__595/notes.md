# q_595 — diameter of the white fur carpet (m)

Prior: black cat speed = 0.94 m/s. depth_info: none. fps = question_fps = 24.

## Scene
Top-down static perspective camera; floor plane faces camera. The round white fur rug is at left, partly under the sofa
(right ~1/4 occluded). The black cat walks at constant speed along +x on the same floor.

## Measurements (own scripts)
- `measure_cat.py`: black cat mask (gray<60, largest blob) in all 50 frames. Linear fit of x vs frame:
  centroid 10.962 px/frame, head front edge 10.975 px/frame (tail end 11.2, noisier). Per-frame centroid steps
  8.8–12.9 (gait noise), mean 10.96. Speed = 10.97 px/frame = 263.3 px/s.
  Scale = 0.94 / 263.3 = 0.003570 m/px. (Record said ~11.0 px/frame: agrees.)
- `rug_radial.py` + `rug_fit.py`: radial V-profiles from (425,634) every 3°, edge = midpoint between rug (~165)
  and carpet (~132) brightness. Circle fit on the edge not touching sofa: D = 473.0 px (all clear arcs),
  473.5 (excluding the side against the wall), 474.8 (top+bottom arcs only, rms 1.7 px); ellipse axes 465 x 477.
  Direct vertical profile at x=420: edges y≈392 and ≈873 → 481 (incl. fur fringe). Overlay: frames/rug_fit.png.
  Adopted D ≈ 475 px (soft fur fringe, ±5 px). Record's 476 px vertical extent agrees.

## Result
D = 475 × 0.003570 = 1.696 m on the floor-plane scale given by the cat.
Small perspective correction: the cat's silhouette (back, ~0.2 m above floor) is nearer to the camera than the rug
edge; the camera height is not known (walls' tops not visible; leaning frame suggests Z ≈ 10–20 m), giving a factor
~1.01–1.02. Applied ~1.5% → **1.72 m**.

## Check
Second route: front-edge speed (10.975 px/frame) and the vertical-profile diameter (481 px) give 1.71–1.72 m before
correction; circle fits give 1.69–1.70. All within ±2%.
Confidence: moderate-high (±3%); main uncertainty is the fur-edge definition and the unknown camera height.
