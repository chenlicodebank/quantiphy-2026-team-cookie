# simulation_0262 – measurement record (pixels, seconds)

2D simulation, 1080x1920 portrait, 24 fps, 50 frames (0–49, t = frame/24). Pixel y points down.

## Scene
- **cup**: the only object. A disposable coffee cup with a red body, a tan sleeve band and a light grey lid. It enters through
  the top edge at frame 2 already falling, falls straight down at x ≈ 576 with no visible rotation, and lands upright on the
  floor between frames 18 and 19. It then squashes (f19), stretches (f20–22, top ~14 px higher, bottom still on
  the floor), settles (f23) and is at rest from f24 to f49.
- **floor / backdrop**: a plain beige seamless backdrop. A faint floor seam sits at y ≈ 1534. There are no markings or other props.
- **cup shadow**: a soft grey contact shadow under the cup from about f17. It is excluded from the cup extents.
- **Camera**: static (background diff between f0 and f49 averages 0.25/255). Per-frame shift is 0.

## Files
- `scene.json`: inventory, events, rest pose and sizes, and the cup's bottom/top edge y per fall frame.
- `tracks/cup.csv` (main track, from `scripts/track2.py`), one row per frame 0–49 (`visible=0` for f0–1):
  - `cx, cy`: centre of the full-cup bbox. This is the reference point standing in for the object origin.
  - `x0 y0 x1 y1`: full bbox (lid top to cup bottom, lid rim included). `width_px` and `height_px` are its extents.
  - `body_*`: the saturated red/tan body only (bottom edge, left/right, centroid). `lid_h_px` is the lid band height.
  - `clipped_top=1`: cup cut off by the top image edge (f2–5). For those frames the centre and height are not the cup's;
    use `body_bottom` instead.
  - There is no occlusion at any frame (single object), so no separate occlusion flag is needed beyond `clipped_top`.
- `tracks/cup_raw.csv`: first-pass mask, plain diff > 30 against f0. It misses part of the lid and **includes the floor
  shadow** after landing. It is kept only for comparison; do not use it.
- `scripts/`: `track.py` (raw), `track2.py` (final), `crops.py` / `crops2.py` (visual checks), `background.py` (seam,
  camera stability, overlay).

## Method and reliability
- Background = frame 0 (empty). Body = HSV saturation > 90. Lid = diff > 14 vs f0 in the rows directly above the body,
  within the body's x-range ±12 px. The overlays (frames/overlay.png, frames/land.png) were checked by eye. The boxes fit
  the cup from lid top to red bottom, with the shadow excluded.
- **Most reliable fall measure: `body_bottom`** (the red bottom has a sharp edge against the beige background). It is
  ±1 px, and it is also valid for f2–5. Per-frame bottom increments are 29, 39, 50, 62, 71, 83, 94, 105, 116, 127, 136,
  152, 162, 174, 185, 196 px (f2→f18). They grow roughly linearly, which is consistent with constant acceleration
  (not fitted here). The f18→f19 step (65 px) is cut short by the impact.
- `cy` during the fall has a few px of bias. The bbox height changes with viewing angle (173 px at f6 down to 150 px at
  f15–18, because the underside ellipse shows high in the frame). The origin is best taken as the midpoint of a fixed
  rest height: origin_y ≈ body_bottom − 72 when airborne. cx is stable at 575–577 throughout.
- **Size for scale**: at rest the cup is 144 px tall including the lid (bottom 1847, lid top 1704), 96 px wide at the lid
  rim, and 87 px wide on the body just under the lid (the cup tapers). The lid band is about 18 px. Width is the most
  view-independent measure. In flight the maximum width is 94–97 px, which agrees with the rest value, so the cup stays at one depth.
  If a question's prior is the cup's height, use the rest height 144 px. In-flight heights are inflated by perspective.
- Ambiguities: (1) The lid is close to the background colour. Its top edge is ±2 px, and the mask fills it in from
  the frame difference. (2) The squash/stretch at f19–22 makes the bbox height there not rigid. (3) The release
  instant is not in the video: the cup is already moving when it appears at f2.
