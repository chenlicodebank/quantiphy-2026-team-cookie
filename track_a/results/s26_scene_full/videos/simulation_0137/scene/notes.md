# simulation_0137 — measurement notes

2D simulation (Blender), 1920x1080, 60 fps, 100 frames (t = frame/60, 0–1.65 s). Static camera.
Scene: a cabin on a grassy hill, a white sun on the left, sky with faint clouds, and **one moving object: a small
bird** that flies left to right across the sky above the house in an arc.

## Files
- `scene.json` – inventory (bird, house with its parts, sun, grass, sky), pixel extents, events, camera info.
- `tracks/bird.csv` – one row per frame 0–99. Columns:
  `frame, time, visible` (0 at frame 0: bird not yet in view),
  `ref_x, ref_y` = **reference point** (centroid of the 3x3-eroded mask ≈ body centre / origin),
  `centroid_x/y` (plain mask centroid), `wcentroid_x/y` (contrast-weighted centroid),
  `bbox_x0,y0,x1,y1` (inclusive), `bbox_cx/cy`, `bbox_w/h`, `area_px`,
  `main_axis_len`, `cross_axis_width` (mask extent along/across its principal axis), `main_axis_deg`,
  `occluded` (1 = touching the image edge, frames 1–3).
- `scripts/` – `track.py` builds the CSV; `summary.py` prints apex/size stats; `static.py` measures static objects and
  checks camera motion; `crops.py`, `overlay.py` draw checks (PNGs in `../frames/`, not part of the record).

## Method
Median background from every 5th frame; per-frame |frame − bg| (max over RGB) > 25, 3x3 closing, largest
component near the previous position. Checked visually on 4x crops (frames 1–99) and a full-path overlay: the boxes
hold the whole bird (beak, tail, both wings) and the ref point sits on the body.

## Bird – key numbers (pixels)
- Visible frames 1–99; partly outside the left edge in frames 1–3; fully visible 4–99.
- x increases every frame; the path rises to an apex at **frame 64** (ref_y ≈ 122.7 px; flat within ~1 px over
  frames 62–66, within ~3 px over 59–69) and then descends. Ends at ref ≈ (1729.2, 299.8) at frame 99.
- Per-frame displacement of the ref point: median 19.8 px, range 14–22 px (fully visible frames). Jitter from the wing
  beat moving the centroid is ~1–2 px per frame; smooth over a few frames before differentiating twice.
- Size: bbox width (≈ beak-to-tail length, the bird is seen side-on heading right) median 35.5 px, 34–40 px outside the
  sun frames; bbox height 16–35 px depending on wing position (wings flap ~every 5–9 frames); principal-axis length
  median 35 px, max 44.8 px. Apparent size does not trend over time → bird stays at about one depth (2D assumption fine).

## Static objects (pixels, from the median background)
- House overall bbox x 576–1419, y 520–958 (844 x 438). Roof 844 x 170 (eave width; ridge x ≈ 608–1380). Front wall
  x 610–1385, y 690–955 (776 x 265). Window incl. frame 285 x 151; door leaf 131 x 189 (with frame 161 x 203);
  mailbox ~42 x 40. Edges accurate to ~2–3 px.
- Sun disc: centre (133.9, 529.0), diameter ≈ 207 px.
- Ground line at house base y ≈ 955.

## Reliability / ambiguities
- Frames ~8–16 the bird is in front of the white sun: its pale belly/wing parts blend in, so the mask shrinks
  (bbox_w down to 21 px) and the ref point may be biased by a few px. Use sizes from other frames.
- Frames 1–3 truncated by the image edge – centre and size biased; do not use for size/speed.
- Wing flapping changes bbox_h and the mask centroid; the eroded-mask centroid (ref) is the most stable body point.
  centroid and bbox centre are alternative ref points (agree within ~1–2 px except while flapping).
- No metric scale is assumed; a question's prior (e.g. bird length or speed) gives one metres-per-pixel scale.
