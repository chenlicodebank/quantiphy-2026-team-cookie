# simulation_0101: measurement record (2D, simulation, 24 fps, 73 frames, 1920x1080)

All values are in pixels (x to the right, y down, origin at the top-left) and seconds (t = frame/24).
No metric scale is assumed.

## Scene
A static camera shows a side-on cut-away view of the sea:
- grey sky, with the horizon/sea line at y≈565;
- a grey-blue surface band between y 565 and 672, where a red fishing boat floats;
- a uniform bright-blue underwater region from y=673 down, where a shark swims.

Both objects move LEFT, horizontally only. In 2D one m/px scale applies to the whole scene, taken from the
prior object. Nothing in the image suggests the boat and the shark are at different depths, but this cannot be
checked from the image.

## Files
- `scene.json`: inventory, extents, reference points, layout lines, events and camera.
- `tracks/boat.csv` and `tracks/shark.csv`: one row per frame (0-72).
  - Columns: frame, t; the mask bbox (x_min, x_max, y_min, y_max, bbox_cx, bbox_cy, length_px, height_px);
    area_px; the mask centroid; `ref_x`, `ref_y` (the reference point to use); `occluded` (always 0).
  - Boat only: `bow_x`/`bow_y` (leftmost hull point, rows 330-640); hull_x_min/max; clipped_right; clipped_top.
  - Shark only: `nose_x`/`nose_y` and `tail_x`/`tail_y` (leftmost and rightmost mask points); clipped_right.
- `scripts/`:
  - `measure.py`: segmentation and track writer.
  - `analyze.py`: per-frame displacement check.
  - `boat_parts.py`: boat part extents.
  - `check_start.py`: comparison of frame 0 and frame 1.
  - `explore.py`, `debug_mask.py`: exploration.
  - `bg.jpg` in `scene/` is the composite clean background.

## Method
- **Background:** frame 0 for x<1300 and frame 72 for x≥1300, so neither object is in it. The camera is static:
  clean strips differ by ≤7 levels.
- **Boat mask:** max-channel difference >30 above y=673, then a 3x3 open and a 25x5 vertical close (this keeps the
  thin mast attached).
- **Shark mask:** difference >22 below y=676, then a 3x3 open and a 1-px dilation.
- **Checks:** masks and boxes were drawn on frames 0, 12, …, 72 and inspected. They cover the full boat, including
  mast, railings and rudder, and the full shark.

## Boat (red fishing boat "AH805", bow pointing left)
- **Clipping:** the right side is cut by the image edge until frame 25. The full boat is visible from frame 26.
  The mast runs off the top of the frame in every frame, so `y_min=0` is clipping and the full height is NOT
  measurable.
- **Length:** bow tip to stern is **858 px** (856-860 px over frames 26-72). This is the most reliable size.
- **Heights:** keel ≈ y 645, cabin roof y 237, bow gunwale y 352.
  - The mask `y_max=672` includes the boat's water reflection (y 648-672). Use 645 as the keel.
- **Parts at frame 72:** cabin x 493-673; mast x 595-605; rear railings x 768-1065; rudder x ≈1028-1062.
- **Reference point:** use `ref_x = bow_x + 428.5`. This is the centre of the full extent and stays valid while
  the boat is clipped. `bbox_cx` is wrong for frames 0-25 because of the clipping. `ref_y` is a constant 441.
  - The boat is rigid and only translates, so any point gives the same displacement.
  - The true Blender origin is unknown (horizontally probably near mid-hull).
- **Motion:** `bow_x` is 1496 at frames 0 and 1, then falls by 17-18 px every frame to 227 at frame 72. The steps
  are uniform: a linear fit leaves 2 px rms, which is integer-edge jitter.
- **Reliability:** about ±1 px per frame on bow_x.

## Shark (grey and white, underwater, facing left)
- **Visibility:** visible and unoccluded in all frames.
- **Size:** mask length is **268 px** (266-274 px). The snout is rendered semi-transparent and the mask misses
  about 5-9 px of the nose tip, so the true nose-to-tail-tip length is about 275 px. Height (dorsal tip to pectoral
  fin tip) is about 108 px.
- **Reference point:** use `ref = bbox centre`. The centroid is about 23 px further left (head-heavy). The centroid
  is the smoothest per-frame signal; the bbox edges jitter by about ±2 px because of the tail.
- **Vertical position:** centroid y = 905.4 ± 0.2, constant (no vertical motion).
- **Motion:** stationary over frames 0-1, then accelerates left. Per-frame dx of the centroid is about -7.6 at
  frames 1-2 and grows smoothly to about -17 to -19 at frames 70-72. A quadratic fits x(t) to 1 px rms. The
  per-frame steps of nose and bbox are noisier (±2 px).
- **Swimming animation:** a small tail/fin wiggle.

## Events
- Frames 0 and 1 are identical (both objects at rest); the first motion is between frames 1 and 2 (t = 0.083 s).
- The boat's stern enters the frame at frame 26 (t = 1.083 s).
- Both objects are still moving at the last frame (72, t = 3.0 s).
- There are no contacts, bounces or direction changes. The bow is always left of the shark's nose.

## Ambiguities
- **Boat height:** the mast top is out of frame, so neither the full height nor the true vertical bbox centre of
  the boat is measurable.
- **Shark nose:** the semi-transparent snout makes the nose edge uncertain by about 5-9 px. A soft lighting halo
  around the shark was excluded by the threshold choice.
- **Boat reflection:** the reflection below the waterline is not part of the boat.
- **Motion blur:** none significant.
