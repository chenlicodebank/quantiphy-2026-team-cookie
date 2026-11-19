# simulation_0216_segmented — measurement record

**Scene:** 2D, segmentation video (Blender render, background replaced by white), 1920x1080, 24 fps, 50 frames
(t = frame/24, 0 to 2.042 s). The camera is static: frame-to-frame phase correlation of the static scene is
under 0.2 px. Side-on view. A black cat walks steadily from left to right along the floor, in front of a row of
furniture. Left to right the furniture is: a wooden bench, a TV console carrying a vase, a TV and a lamp, and a tall
leaning mirror. The cat is the only moving object. All units are image pixels (x to the right, y down) and seconds.
No metric scale is recorded.

## Files
- `scene.json`: inventory, camera, cat summary (positions, net displacement, per-frame x-step stats, pixel
  sizes), static objects and events.
- `tracks/cat.csv`: one row per frame, 0–49 (the cat is visible in every frame and never occluded or edge-clipped).
  Columns:
  - `cx, cy`: centroid of the full mask.
  - `area`: mask pixel count.
  - `bbox_x0..y1`, `bbox_cx, bbox_cy`: bounding box (tail tip to nose, ear/tail top to paws) and its centre.
  - `length_px, height_px`: bounding-box extents.
  - `torso_*`: box over the columns that hold ≥35 px of black fur. This is the body plus head, without the tail
    and thin legs. Its y-range can include legs.
  - `dark_cx, dark_cy`: centroid of the black fur inside those torso columns.
  - `edge_clipped`, `occluded`: 0 in every frame.
- `static_objects.json`: bounding box, width, height, centre and mask centroid of each piece of furniture. Measured
  on the per-pixel-maximum image over all frames, which removes the cat and its shadow.
- `scripts/`: `track_cat.py` (tracking), `static_objects.py` (furniture and camera check), `summarize.py` (stats),
  `probe_pixels.py` (colour checks).

## Method
The cat's fur is rendered pure black (0–35). Its shadow on the console front is brownish grey (50–100), so the two
can be told apart. Mask construction:
- Start from black pixels that differ from the max-background.
- Exclude "static dark" scenery: pixels that are black in more than 60% of frames, which is the console's black metal
  base. Re-insert it where the cat crosses that base, using vertical closing.
- Add the bright, low-saturation grey/tan paws, chest and muzzle components that touch the fur.

Overlays were checked by eye at frames 0, 14, 25, 30 and 42. The mask covers the body, tail, legs and paws, and does
not include the shadow.

## Reliability
- **Horizontal position:** good to about ±3 px per frame. The steps fluctuate with the gait: the `cx` step averages
  17.6 px/frame with an SD of 2.7. Use `dark_cx` or `cx` as the root/pelvis proxy; `bbox_cx` and `torso_cx` are
  noisier. The true rig origin is not visible. For speed questions, a centroid differenced over a few frames is
  safest. The walk is steady: the first-half and second-half mean steps are 17.9 and 17.8 px/frame. There is no
  vertical drift (`cy` changes by less than 2 px net).
- **Front of the head:** the grey muzzle is about the same colour as the console wood behind it. When the head is in
  front of the console (from about frame 8), `bbox_x1` can miss up to about 20 px of muzzle. The thin white matting
  halo around the cat sometimes adds a few px. Expect bbox length to be uncertain by about ±15 px.
- **Cat size:**
  - Bounding-box length (tail tip to nose): median 294.5 px, p10–p90 283–309. The tail pose changes this.
  - Body length without the tail (dark columns): about 260 px.
  - Bounding-box height (tail/ear top to paws): median 219 px.
  - Body top is at y ≈ 880 and paws at y ≈ 1021, so shoulder or back height is about 140 px (rough).
  - Apparent size does not trend over time, which fits a planar (2D) walk.
- **Furniture:** boxes are accurate to ±2 px.
  - Bench: 466 × 213 px.
  - TV console: 772 × 212 px.
  - TV: 399 × 230 px.
  - Vase: 102 × 216 px.
  - Lamp: 206 × 287 px. The shade is 206 px wide.
  - Mirror: 266 × 578 px. It leans, so its frame is slightly skewed.
  - The furniture stands slightly behind the cat's walking line: furniture feet are at y ≈ 988–991, the cat's paws
    at about 1021.
- **Events:**
  - No start or stop: the cat is already walking at frame 0 and still walking at frame 49.
  - Its nose passes the left end of the console at about frame 8.
  - Its tail tip clears that end at frame 25.
  - There are no bounces, impacts or direction changes.
