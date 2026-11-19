# simulation_0298 – measurement record

**Scene.** A 2D Blender render, 1920x1080 px, 24.005263 fps, 73 frames (t = frame/fps). The camera looks straight down at a uniform purple plane (RGB ~164,88,194). There are no markings or static objects. The only object is a **fire-rescue truck** seen from above. Its white cab, with "FIRE-RESCUE" on the roof and a red light bar, is at the front (left). Behind it are the dark chassis, a dark-blue flat bed with red trim and a red crane fitting, and magenta tail lights at the rear (right). The truck drives straight left along y ≈ 539.5 px, cab first. It enters the left image edge at frame 48 and the last sliver disappears after frame 68, so frames 69–72 are empty. The camera is static. A blank background cannot show any pan, but there is no reason to suspect one.

## Files
- `scene.json`: inventory, sizes, events, camera and perspective notes.
- `tracks/truck.csv`: one row per frame. Columns:
  - `ref_x, ref_y`: reference point (see below).
  - `ref_source`: how the reference point was obtained.
  - `x0 y0 x1 y1`: mask bbox. x0 is the front (left) edge and x1 the rear (right) edge.
  - `length_px`: front-to-rear extent, only while fully visible.
  - `visible_length_px`: extent of the visible part.
  - `width_incl_mirrors_px`: full vertical bbox extent.
  - `body_width_px`: vertical mask extent in the column 130 px in front of the rear edge (mid-bed, no mirrors).
  - `cab_width_px`: vertical mask extent in the column 70 px behind the front edge.
  - `front_edge_x, rear_edge_x, mask_cx, mask_cy, area_px`.
  - `truncated_by_frame_edge`, `occluded`: the truck is never occluded by another object.
- `tracks/truck_raw.csv`: raw segmentation output.
- `scripts/`:
  - `measure.py`: background difference, threshold 25, 3x3 open, connected components.
  - `finalize.py`: builds the final track.
  - `overlay.py`: draws the mask and bbox for visual checking.
  - `background.py`: camera and background check.

## How measured / reliability
- **Segmentation.** The truck is segmented by colour difference from the flat background. Overlays at frames 0, 24, 47, 52 and 60 show the outline matching the whole truck, including mirrors and the rear hooks. There is no shadow and no visible motion blur. Edges are accurate to about ±1 px.
- **Reference point (vehicle root).** The origin is not visible.
  - Frames 0–47: ref = bbox centre. The mask centroid sits 2–12 px behind it because the mass is uneven.
  - Frames 48–68 (front out of frame): ref = rear edge x1 minus the offset (x1 − bbox centre), predicted from a quadratic fit in x1 over frames 0–47. The fit's residual std is 0.5 px. Extrapolated points carry about ±2 px of extra uncertainty, and the step at 47→48 is −24.4 px against a typical −26.5.
  - `rear_edge_x` is an independent track measured in every visible frame (0–68).
- **Motion.** Per-frame displacement is near constant:
  - bbox centre: 1511.5 → 274.0 px over frames 0–47, mean 26.33 px/frame;
  - rear edge: about 26.3 px/frame over frames 0–68;
  - front edge: 1232 → 2 over frames 0–47.
  - There is no visible acceleration, direction change, bounce or contact. The truck is already moving at frame 0, so the start of motion is not visible. Single-frame steps quantise to 0.5 px (std ≈ 0.5 px); use multi-frame fits for speeds.
- **Sizes.**
  - Length along the motion axis: **534 px** when centred in the image (frames 23–32, the best top-view value). It is 560 px at frame 0 (right side) and 545 px at frame 47 (left side). This is perspective: the tall truck's sides become visible off-centre.
  - Body width without mirrors: **160 px** (157 at the far right).
  - Cab width: 160 px. The 175 px reading at frame 0 is from the mirror arms.
  - Width with mirrors: 184–191 px.
  - Height cannot be observed from the top-down view.
  - If a question's size prior is the truck length, scale with 534 px (centred view). The spread from 534 to 560 px (about 5%) shows the uncertainty.
- **Ambiguities.**
  - The vehicle root may be at the rear axle rather than the bbox centre. That shifts positions by a constant but leaves speeds and accelerations unchanged.
  - Perspective makes edge-based speeds differ by about 1% (front 26.17, centre 26.33, rear 26.49 px/frame over frames 0–47).
