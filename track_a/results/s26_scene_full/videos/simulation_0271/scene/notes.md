# simulation_0271 — measurement record

2D simulation, 24 fps, 72 frames (3.0 s), 2560x1440. Units: pixels, seconds; x to the right, y down. t = frame/24.

## Scene
- One object only: a **phoenix** (peacock-like bird; green/purple/dark wings, dark green spine, long orange
  peacock-eye tail feathers), seen top-down, head pointing **left**. It flaps and flies left across a plain grey
  (RGB ~194) background. No ground, props or markings. Camera static (no background texture; nothing indicates motion).
- 2D: one metres-per-pixel scale from whichever prior a question gives (size, speed or acceleration of the phoenix).

## Files
- `scene.json` — summary: inventory, key positions, extents, flap cycle, events.
- `tracks/phoenix.csv` — per frame 0-71: `ref_x, ref_y` (recommended reference point), `beak_x, beak_y`,
  `spine_y`, mask centroid, bbox (x0,y0,x1,y1) and centre, `length_x_px` (beak to tail tip, along the flight axis),
  `span_y_px` (vertical extent = wingspan when wings open), span above/below spine, area, part count,
  `touches_edge`, `occluded` (=1 when cut by the image edge: frames 70-71).
- `tracks/phoenix_body_shift.csv` — per-frame horizontal shift of a body template (columns beak+120..beak+450 px
  around the spine), with the beak dx for comparison and a cumulative body x.
- `scripts/` — `probe.py` (background stats), `track.py` (segmentation, overlays to frames/), `body_shift.py`,
  `merge_ref.py` (adds ref_x/ref_y).

## Method
- Mask = max|RGB−194| > 12, 5x5 close, components ≥ 200 px. Overlays (frames/ov_*.png) checked at frames
  0, 9, 14, 24, 38, 47, 62, 71: contour covers wings, body and tail feathers fully.
- Reference point: beak tip (leftmost mask pixel) x, and spine row (weighted row of the thin neck just behind the beak).
  Template matching of the body confirms the beak moves rigidly with the body (per-frame dx agree within ~1-3 px),
  so beak-tip differences = origin differences. The Blender origin is presumably at the body/wing root, a fixed
  offset (~200-270 px) behind the beak along the spine — irrelevant for displacement/speed/acceleration.
- Frames 70-71: beak off-screen; ref_x extrapolated with the body template shift (−37.7, −42.4 px) → −33.7, −76.1;
  ref_y from leftmost visible pixels. Less reliable (±3 px).

## Key numbers (px)
- ref_x: 1597 (f0) → 1408 (f24) → 838 (f48) → 4 (f69); y stays 719-729.5 (small bob with flapping).
- Motion: starts almost at rest (f0→f1 dx 0), accelerates leftwards with a speed ripple tied to the 25-frame
  flap cycle. Mean dx per frame: 8.2 (f1-25), 24.6 (f26-50), 40.7 (f51-69). Per-frame dx is noisy at ±1-3 px
  (pixel-quantised beak tip); smooth over a few frames if needed.
- Length (beak→tail tip): 690-746 px, median ~715 (tail pose changes it; faint thin tail filament may be partly
  outside the mask by a few px).
- Wingspan (vertical extent): max 1008 px (frames 21, 46, 71), min 374 px (frames 12, 37, 62); 429 at frame 0.
  Flap cycle period 25 frames (~1.04 s), two span peaks per cycle (~930 and 1008 px).

## Ambiguities / reliability
- Single object, no occlusion except image-edge cut at frames 70-71 (x extents invalid there; y extents fine).
- "Width" of the bird: in this top-down view the wingspan is the vertical (y) extent; length is horizontal (x).
- Motion blur negligible; feather tips are slightly translucent so extents are ±3 px.
- Speed ripples with the wing beat, so instantaneous speed at a chosen frame depends strongly on the frame.
