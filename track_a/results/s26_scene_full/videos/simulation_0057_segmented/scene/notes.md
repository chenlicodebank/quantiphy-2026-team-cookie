# simulation_0057_segmented — measurement record (pixels, seconds)

2D segmented Blender clip, 1080x1080, 30 fps, 91 frames (t = frame/30, 0–3.0 s). Top-down view onto a white
(segmented) background; image y increases downward. Camera static (props never move; no background texture).

## Objects
- **car** (only mover): orange sports car seen from above, long axis vertical, driving straight DOWN (+y) at
  x ≈ 350–356 px. Enters already moving through the top edge (partly out of frame frames 0–15, fully visible from
  frame 16), decelerates steadily the whole clip and is still moving (~3.7 px/frame) at frame 90. No stop, no contact.
  Size: length (y) ≈ **289 px** (median bbox_h, frames 40–90), body width (x) ≈ **115 px** (mask width is 117–121 px
  from frame ~55 on, because of a thin dark protrusion at the left side — mirror/shadow edge).
- **prop_upper**: static dark dumbbell/hammer-like prop (hexagonal head left, thin shaft, round knob right), nearly
  horizontal, left of the car path. bbox [177,432,263,476], bbox centre (220,454), centroid (214.5,455.5),
  main-axis length ≈ 90 px, width ≈ 43 px.
- **prop_lower**: same kind of prop, lower-left, diagonal (hex head bottom-left ~(197,980), knob top-right ~(252,910)).
  bbox [177,898,263,998], bbox centre (220,948), centroid (215.9,954.9), main-axis length ≈ 123 px, width ≈ 42 px.
  Distance between the two prop bbox centres = 494 px (vertical).

## Files
- `scene.json`: inventory, sizes, events, motion summary.
- `static.json`: prop masks' bbox/centroid/PCA extents (frame 0).
- `tracks/car.csv`: every frame 0–90: cx/cy of bbox and mask centroid, bbox x0,y0,x1,y1, bbox_w/h, area, PCA
  length/width/axis angle, touches_top, touches_static_mask, `cy_from_front` (= y1 − 144 px, a centre estimate valid
  while the rear is cut off), `cy_from_rear` (= y0 + 144), `occluded` (1 = partly outside frame, frames 0–15).
- `scripts/measure.py` (segmentation: non-white & saturation mask, props = frame-0 components, car = rest),
  `scripts/augment.py` (front/rear centre estimates, per-frame dy printout), `scripts/write_scene.py`.

## Motion (pixels)
Per-frame dy of the car: ~18 px/frame at frames 1–10 (front edge), ~16 at 17–20, ~14 at 30, ~12 at 42, ~10 at 52,
~9 at 60, ~7 at 70, ~5.5 at 80, ~3.7 at 88–90 — roughly linear decrease (≈ −0.16 px/frame² ≈ −144 px/s²; for
reference only, fit yourself). Centre y: ≈ −118 (est. from front edge y1 = 26) at frame 0, 375 at frame 30, 722 at frame 60,
906 at frame 90. Car centre passes prop_upper's y at frame 36 (t = 1.2 s); never reaches prop_lower's y (948).
x drifts slightly left (centroid 356 → 349 px).

## Reliability / ambiguities
- Origin for the car = bbox/mask centre (top-down view of a symmetric car; vehicle root assumed at its centre in xy).
  Frames 0–15: bbox centre is wrong (car cut by top edge) — use `cy_from_front`. Per-frame edge positions are
  integer-pixel: single-frame differences are noisy by ±1 px; the centroid column is smoother.
- Vertical motion blur in fast frames (16–30) inflates bbox_h to 293–301 px; blur is symmetric, so centres are fine;
  use 289 px as the car length. A size prior on the car length (bumper-to-bumper) ⇒ scale = prior / 289 px; on width
  ⇒ prior / 115 px.
- Props: identity unclear (dumbbell-like or hammer-like); both identical in style, distinguish by upper/lower.
