# simulation_0105 – measurement notes

**Scene**: 2D Blender render, 1080x1080, 24 fps, 47 frames (t = frame/24). Plain uniform grey background, static camera.
A white cup (handle on the left) stands on a white saucer at the bottom centre. A small white cube (sugar cube)
falls straight down from above the top edge at x ≈ 539.5 px, appears at frame 21, and drops into the cup between
frames 45 and 46. Nothing else moves. No ground line, horizon or markings.

## Files
- `scene.json` – inventory, static extents, events, camera.
- `tracks/cube.csv` – cube per frame 21–45: frame, time, centroid (cx, cy) px, bbox (x0,y0,x1,y1 inclusive),
  width_px, height_px, area_px, occluded (1 = clipped by image top, frame 21 only).
- `scripts/track.py` (cube tracking: |grey − background| > 25 threshold above y = 960, largest blob, centroid),
  `scripts/static.py` (cup/saucer extents, overlay check), `scripts/views.py` (zoomed crops).

## Measurements and reliability
- **Cube** size: 26 px wide × ~26–27 px tall bbox (includes ~1 px anti-alias; solid core ~25 px). Constant size
  (2D scene, no depth change). Centroid precision ~±0.3 px in frames 22–45. Frame 21 is clipped at the top edge:
  its centroid (y = 5.5) is biased; true centre ≈ bbox_y1 − 13 ≈ −2 px. Use frames 22–45 for motion.
  x is constant (539.4–539.6) → purely vertical motion. Per-frame y step grows ~27 px (22→23) to ~53 px (44→45),
  i.e. steady acceleration (free fall); the release is above the frame and not visible.
- **Cup** (from frame 0, where the contrast is best): rim y = 974, rim x 478–611 (134 px), width incl. handle
  469–611 (143 px), height rim → saucer ≈ 79 px (974–1052). Edges ±1–2 px (cup shading is close to the background
  grey in later frames).
- **Saucer**: x 451–636 (186 px), y 1052–1073 (≈22 px tall).
- Distance cube centre → cup rim at frame 45: 974 − 945.2 = 28.8 px (cube bottom 16 px above rim).

## Events
- f21 (0.875 s) cube enters the view at the top; f22 (0.917 s) first fully visible; f45 (1.875 s) last visible;
  f46 (1.917 s) cube inside the cup (hidden), small disturbance at the rim → impact/entry between f45 and f46.

## Ambiguities
- Frames 0–1 render the cup semi-transparent (inner cavity visible), opaque from frame 2; geometry unchanged.
- Cube has a darker grey spot in its centre (texture/shading), not a separate object. No shadows, negligible blur.
