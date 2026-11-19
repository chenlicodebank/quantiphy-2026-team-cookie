# simulation_0256 – measurement record

2D simulation, 1920x1080, 24 fps, 41 frames (t = frame/24). One object: a small yellow-green tennis-style ball
moving left -> right horizontally across a plain beige backdrop. Camera static.

## Files
- `scene.json` – inventory, camera, ball size, events.
- `tracks/ball.csv` – per frame: frame, time, visible, centroid (cx, cy, px, b*-weighted subpixel), bbox
  (x0,y0,x1,y1,w,h inclusive), mask area, equivalent diameter, major/minor mask extents, height, major-axis angle,
  `occluded_or_cut` (1 = cut by image edge: frames 5 and 40). Frames 0-4: not visible.
- `tracks/camera_bgshift.csv` – background phase-correlation shift vs frame 0 (all < 0.11 px => static).
- `scripts/track_ball.py` (tracking + overlays), `scripts/check_size.py` (threshold sensitivity, entry check).

## Method
Ball mask = Lab b* channel more than 12 above the frame median (ball is the only yellow thing), largest component.
Overlays (frames/ov_*.png) checked: contour hugs the ball; the dark soft shadow above/up-left of it is excluded.

## Key numbers (px)
- Ball diameter ≈ 36 px (bbox w = h = 36 median, ±1). Equivalent-area diameter 34.7 (mask misses a few dark rim
  pixels); thresholds 6/20 give 37-38 / ~30, so 36 ± 1 is the best estimate. Size constant over time → constant depth.
- Path: cy constant 363.3–364.2; cx 51.4 (f6) → 1868.4 (f39). Per-frame dx decreases smoothly from ~60.8 (f6→7)
  to ~49.4 (f38→39): steady deceleration (~ -0.35 px/frame per frame). No bounce/direction change.
- Edge frames: f5 only right sliver (x 0–7) visible, centre ≈ -10.5 by edge+radius; f40 left part (x 1900–1919),
  centre ≈ 1917.5. The CSV centroids for these two frames are of the visible part only — do not use them as centres.
- Events: enters f5 (0.208 s), fully visible f6–f39, exiting f40 (1.667 s, last frame).

## Reliability
Centroids good to ~0.3 px (per-frame dx jitter ~±0.5 px; use differences over several frames for smoother values).
2D scene, single plane: one metres-per-pixel scale from the prior (e.g. ball diameter 36 px). No ambiguity about
object identity (only one object).
