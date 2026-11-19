# simulation_0272 – measurement record

2D simulation (Blender), 24 fps, 72 frames (t = 0 … 2.958 s), 2560×1440. Top-down view of snowy mountain terrain.
One moving object: a phoenix/peacock-like **bird** (green head/body/wings, red-orange eye-spot tail fan, long thin
green central tail shaft) flying toward image left along row y ≈ 715. Camera is static (phase-correlation shift
< 0.003 px over all frames). No shadow of the bird is visible. Nothing else moves.

## Files
- `scene.json` – inventory, key sizes, events, camera.
- `tracks/bird.csv` – one row per frame (0–71), columns:
  - `frame, time`
  - `cx, cy` – centroid of the full mask (biased toward the tail fan; jitters with wingbeats).
  - `bbox_cx, bbox_cy, x0, y0, x1, y1, bbox_w, bbox_h` – mask bounding box (bbox_w = beak-to-tail-tip length,
    bbox_h = vertical extent incl. tail fan).
  - `green_cx, green_cy` – centroid of all green mask pixels (body + wings; y jitters with wings).
  - **`body_cx, body_cy`** – centroid of green pixels within ±35 px of the beak row and ≤160 px behind the beak
    = body centre; **recommended proxy for the rig origin**.
  - `beak_x, beak_y` – leftmost mask pixel (beak tip); crispest horizontal position (≈ body_cx − 110 px).
  - `wing_y0, wing_y1, wing_span_px` – vertical mask extent over columns beak..beak+220 (wings only, no tail).
  - `area, axis_len, axis_wid, axis_angle_deg` – mask area and PCA-axis extents (axis flips to vertical when
    wings are spread; use bbox_w / wing_span_px instead).
  - `occluded` – always 0.
- `scripts/background.py` – camera-shift check; background plate = frame 71 for x ≥ 1150, frame 0 for x < 1150
  (a temporal median was contaminated because the bird hovers near x≈1500–1950 early).
- `scripts/track_bird.py` – segmentation: |frame − background| max-channel > 30, open 3×3, close 9×9, largest
  component + nearby pieces. Overlays (frames/ov/) were inspected at frames 9, 20, 40: the mask covers the whole bird
  incl. tail feathers and the thin tail shaft, nothing of the background.
- `scripts/probe.py` – initial saturation probe (not used for results).

## Key numbers (pixels)
- Body point: frame 0 (1595.5, 720.4) → frame 71 (542.8, 716.1); net ≈ 1053 px left. Vertical drift of body point
  only ±6 px (bobbing 708–721). Beak: 1487 → 432.
- Motion: frames 0 and 1 identical (at rest); motion starts at frame 2. Bird accelerates leftward with speed pulsing
  per wingbeat: beak step ~3–4 px/frame (frames 2–6), ~4–8 (7–25), ~14–20 (26–45), ~20–30 (46–71).
- Length beak→tail tip (bbox_w): median 436 px, range 420–456 (tail flexes).
- Wingspan (wing_span_px): max 618 (f71), 616 (f21), 613 (f46); min 118 (f13, f38, f39, f63 – wings raised/edge-on).
  Flap period ≈ 12.5 frames (maxima at ~10, 21, 35, 46, 60, 71).
- Apparent size constant over the clip (2D, plane parallel to image).

## Reliability / ambiguities
- Mask edges ±2 px (video compression). Body point ±3 px; beak_x ±1–2 px. Per-frame differences of body_cx are
  noisier than beak_x; for average speed / path length use either, for backward-difference speed at one frame
  consider beak_x or lightly smoothed body_cx.
- The true rig origin is not visible; body_cx/cy (body centre) is the best estimate. Full-mask centroid `cx` is
  shifted ~+100 px toward the tail and oscillates with flaps – do not use it as the origin.
- "Wingspan" in the image is the projected spread seen from above; at maxima the wings are near-flat, so max ≈ true
  span. Minima reflect raised wings, not folded ones.
- Static terrain has no well-defined objects with sizes (left grey cliff x≈0–900, right tan ridge x≈1950–2560).
