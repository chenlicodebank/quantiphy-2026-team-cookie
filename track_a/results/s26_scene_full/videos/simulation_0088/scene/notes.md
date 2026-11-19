# simulation_0088 — measurement record (pixels, seconds)

2D Blender render, 1920x1080, 24 fps, 30 frames (t = frame/24). Static camera, plain uniform blue sky
(RGB 97,149,191), no ground, no static objects. Two birds seen from below fly straight right-to-left along the
same horizontal line:
- **eagle** – large bald-eagle-like raptor (dark wings/body, white head, pale beak, white fanned tail). Faster.
  Visible frames 0–15 (frame 15 cut by left edge).
- **crow** – smaller all-black bird. Slower. Visible frames 0–25 (frame 25 cut by left edge).

## Files
- `scene.json` – inventory, extents, events, camera, reference-point convention.
- `tracks/eagle.csv`, `tracks/crow.csv` – one row per visible frame: frame, t, cx_bbox/cy_bbox (bbox centre),
  cx_centroid/cy_centroid (mask centroid), head_tip_x/head_y (leftmost mask column and mean y of the 12 leftmost
  columns), tail_end_x/tail_y (same for rightmost columns), bbox x0,y0,x1,y1 (inclusive), length_px (horizontal
  extent = beak-to-tail, body axis is horizontal), wingspan_px (vertical extent = wingtip to wingtip), area_px,
  merged_with_other, cut_by_frame_edge, occluded.
- `scripts/probe.py` (component survey), `scripts/measure.py` (segmentation, tracks, overlays in frames/ov/).

## Method
Mask = sum|RGB − background| > 40; connected components; eagle = component wider than 110 px. Overlays (mask +
bbox + reference point) checked visually at frames 0, 6, 12: masks cover full bird incl. wingtips and tail; the
eagle's faint pale beak tip may be lost by ~1–3 px.

## Reference point (origin proxy)
Use **x = cx_bbox** (midpoint beak–tail; horizontal extent constant, so it moves rigidly with the body) and
**y = body line** (eagle ≈ 554.2, crow ≈ 552.4, constant). Both birds move purely horizontally, so the
tail_end_x (or head_tip_x) column gives equally clean per-frame displacement. Don't use cy_bbox/cy_centroid for
motion: wing flapping shifts them by ±10 px.

## Key numbers
- Eagle body length 138–140 px (mean ≈138.7); wingspan (projected, flapping) max 324 px (f6), min 175 px (f12).
- Crow body length 85–88 px (mean ≈86.6); wingspan max 164 px (f3/f12/f21), min 106 px (f24) (≈9-frame flap cycle).
- Per-frame steps: eagle 119–120 px/frame every frame f1→f14 (tail_end_x 1762→206, mean 119.69);
  crow 73–74 px/frame f1→f24 (tail_end_x 1826→141, mean 73.26). Steady, no direction change, no vertical motion.
- Eagle–crow horizontal gap grows ≈46.4 px/frame (from cx: f2 1573.5 vs 1710, ...).

## Events
f0 = f1 identical (no motion yet); motion starts f1→f2 already at steady step; f2 birds separate;
f15 eagle at left edge (last seen); f25 crow at left edge (last seen); f26–29 empty sky.

## Reliability / ambiguities
- Frames 0–1: birds overlap (eagle tail drawn over the crow's head). Split by columns: eagle = x ≤ 1762
  (right edge confirmed by the 119.7 px step to f2), crow = x ≥ 1740; crow's head is hidden, so crow x0=1750 and
  length 77 are truncated — true crow head ≈ x 1740 (tail end 1826 − 86), cx ≈ 1783. Eagle row f0–1 is reliable
  in x; its y extents are fine. Flagged merged/occluded.
- Frame 15 (eagle) and 25 (crow) cut by left edge: bbox/centre not valid there; use head/tail extrapolation.
- Wingspan is a projected, flapping value; "max/min wingspan during flight" = the max/min of wingspan_px over the
  fully visible frames (eagle f2–14, crow f2–24; including f0–1 for eagle: 183).
- Single depth plane (2D): one metres-per-pixel scale from the prior applies to both birds.
