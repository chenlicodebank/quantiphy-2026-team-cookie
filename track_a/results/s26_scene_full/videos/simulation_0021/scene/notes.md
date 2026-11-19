# simulation_0021 — measurement record

3D Blender render, 1080x1080, 89 frames at 29.996629 fps (t = frame/fps). All values are image pixels
(x right, y down) and seconds. No metric scale is assumed anywhere.

## Scene
A static camera looks straight at a white-painted brick building wall. In front of the wall: a wet sidewalk
with a black street lamp (x ~155-236) and a white fire hydrant with rust spots (x ~60-140), then a curb, a wet road
and a white lane line. **One moving object: a man** (navy jacket, white shirt, grey trousers, blank face) who
walks left to right (+x) through the whole clip, **behind** the hydrant and then **behind** the lamp post. He is
already walking at frame 0 and still walking at frame 88; he never stops or turns.

## Files
- `scene.json`: inventory (every object with description, pixel extents, visible frames), camera, ground-line
  rows, events.
- `tracks/man.csv`: one row per frame 0-88. Columns:
  - `ref_x_best, ref_y_best`: **the reference point to use (pelvis estimate)**.
  - `ref_source`: `pelvis_row` (measured directly; only frames 81-88 are fully clear) or `head+offset`.
  - `ref_x_pelvis_est`: raw mean mask x on the hip rows. Biased whenever the hydrant/lamp hides part of the hips.
  - `ref_y_pelvis_est`: head_top_y + 116.
  - `head_cx`: raw head-centre x. `head_cx_filled`: same, interpolated where the pole covers the head.
  - `head_top_y`, `sole_y`, `bbox_x0..y1`, `height_px`, `width_px`, `mask_area`.
  - `occluded`, `occluder`: the bbox overlaps the lamp or hydrant (a loose test).
  - `pelvis_row_occluded`, `head_occluded`.
- `scripts/`:
  - `bg_and_camera.py`: median background and camera-shift check.
  - `track_person_final.py`: segmentation and the CSV.
  - `check_ref.py`: overlay check.
  - `static_measure.py`, `static_probe.py`: static objects.
  - `feet_probe.py`: sole/reflection probe.
  - `track_person.py`: first draft.

## Method
- **Camera**: phase correlation of the wall against frame 0 gives a shift of at most 0.01 px. The camera is
  static, so the background shift is 0 in every frame.
- **Man**: subtract a per-pixel median background (every 3rd frame), threshold at 28, apply morphology, and keep
  pixels within 90 px of the median x. Below the feet, the mask is cut at the narrowest row between the feet and
  their mirror reflection on the wet pavement (search band y 855-882).
  - Overlays (`frames/man_check.png`, `frames/ref_check.png`) confirm the mask covers the full man except the
    parts hidden by the props.
- **Pelvis**: x is the mean mask x on rows ref_y±4. Where the hip row is not clear, x = head_cx_filled + an
  (pelvis − head) offset interpolated from the clear frames. That offset is a stable −4.0 to −5.0 px over frames
  81-88; it is held constant for earlier frames.
  - y = head top + 116 px (0.53 of the ~219 px body height). The head top is a cleaner signal than the sole.
- **Static objects**: measured on the median background (lower half) and on frame 88 (upper half). The hydrant was
  read by hand from zoomed crops, ±3 px.

## Key numbers (px)
- **Man position**: best pelvis x goes from 83.7 (f0) to 252.2 (f88), net +168.5 px. y ≈ 766-770 (gait bob
  ±2). Head top y 650-654 the whole time.
- **Man size**:
  - Standing height ≈ 218 ±5 (head top to sole line ~866-872).
  - Max height while walking ≈ 219 (head top 650); min ≈ 214 (head top 654).
  - bbox width 41 (legs together) to 116 (full stride).
  - Torso width ≈ 45.
- **Apparent size is constant**: he walks parallel to the image plane at constant depth, so a single px scale
  applies along his path.
- **Gait**:
  - Legs together at frames ≈ 0, 14, 28, 44, 57, 73, 88, i.e. a step every ~14.6 frames (≈0.49 s).
  - Widest stride at frames ≈ 8, 22, 36, 50, 65, 80.
  - Pace is not perfectly uniform: head x moves ~1.7 px/frame over f0-50 and ~2.6 px/frame over f76-88.
    Fit your own motion if needed.
- **Lamp post**: bbox x 155-236, y 328-894. Height 566. Pole width 12 at x ≈ 191. Lantern 82 wide x 72 tall.
  Base ≈ 53 wide (x 162-215).
- **Fire hydrant**: bbox x 60-140, y 753-890. Height 137. Width 80 including nozzles; body ≈ 43.
- **Lower windows**: 117 × 205 px (left, x 254-370) and 117 × 204 px (right, x 708-824), both y ≈ 189-393. Two
  upper windows are cut off by the top edge.
- **Graffiti "NEOM."**: x 614-939, y 604-791, 326 × 188 px.
- **Ground rows (y)**: wall base 806, grass/sidewalk edge 826, man's contact line ≈868, prop bases 892, curb top
  907, road edge 945, lane line 957. The horizon is not visible; it is ≈540 if the camera is level with a centred
  principal point.

## Reliability and ambiguities
- **Camera static**: certain.
- **Man's x track**: good to ~±2 px in frames 76-88. Elsewhere it is ±3-5 px, because it relies on the head plus
  an offset assumed constant.
  - Frames 0-40: the hydrant hides the lower body and part of the hips.
  - Frames 45-80: the lamp base and pole hide parts of the body; the pole covers the head ~f56-62. head_cx raw is
    biased low there, so use head_cx_filled.
  - Raw `ref_x_pelvis_est` jumps in f9-12 and f58-63 because of this occlusion; do not use it in those frames.
- **sole_y / height_px per frame**: noisy (±8). The reflection on the wet ground merges with the shoes. Prefer
  head_top_y for vertical motion and ~218 px for height.
- **Pelvis y**: a body-proportion estimate, not a joint detection. Absolute ±5 px; relative bob is reliable.
- **Reflections**: the man, lamp and graffiti are reflected on the wet sidewalk. These are not objects.
- **Distinguishing objects**: only one person, one lamp and one hydrant are present, so there are no
  similar-object confusions. Motion blur is negligible.
