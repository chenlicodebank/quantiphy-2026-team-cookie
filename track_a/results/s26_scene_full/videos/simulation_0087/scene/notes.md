# simulation_0087: measurement record (pixels, seconds)

Video: 1920x1080, 24 fps, 54 frames (t = frame/24, frame 0 = t 0). Simulation, 2D: a top-down view of a flat, featureless grey ground (RGB ~140).
Image axes: x to the right, y downward, in px.

## Files
- `scene.json`: inventory, pixel sizes, events, camera and lane separation.
- `tracks/cyclist.csv`, `tracks/car.csv`: one row per frame (0-53). Columns:
  - frame, time.
  - Mask bbox: x0, x1, y0, y1, plus bbox_cx/cy.
  - Mask centroid: mask_cx/cy, and area_px.
  - Mask extents: len_x (along the motion axis) and wid_y (across it).
  - truncated / trunc_side: object cut by the image edge.
  - ref_x, ref_y: **the reference point to use** (origin proxy). ref_source says how it was obtained.
  - occluded: always 0.
  - Cyclist only: rider_cx/cy and rider_x0..y1, the dark torso blob.
- `scripts/`:
  - `track.py`: segmentation and tracking. Threshold |grey-140| > 38 or chroma > 25, then close, keep the main components, fill holes. Cyclist band is y 300-540, car band is y 540-1000.
  - `finalize.py`: reference-point columns and scene.json.
  - `diffs.py`: per-frame edge steps.
  - `crops.py`, `probe.py`: checks.

## Objects
1. **cyclist**: a rider on a bicycle (dark clothes, teal bike accents), upper lane, centre y ≈ 429. Moves +x (right).
   - Bike length tip to tip: median **171 px** (173 → 169 over the clip). Width across: 49 px (shoulders/handlebar).
   - Steady speed of about **21.1 px/frame** (edge steps are 21-22 every frame), already at full speed in the first moving frame (1→2).
   - y wobbles between 426 and 430.
   - Truncated at the left edge in frames 0-6. In frames 0-1 only the front wheel tip shows, so ref_x there = front tip − 171/2.
   - Reference point = bbox centre, which is roughly the saddle/pelvis. The torso-blob centroid (rider_cx) sits 10-20 px behind it. Pick one consistently.
2. **car**: a white/silver angular pickup (Cybertruck-like), lower lane, centre y ≈ 688.5. Front (light hood) faces left; the dark bed is at the right. Moves −x (left).
   - Length bumper to bumper: median **583 px** (589 at f37 down to 577 at f53; ±6 px from edge blur).
   - Width: **214 px** body only, **250 px** including the side mirrors (mirror y 564-813, body y 579-792).
   - Starts at rest: front edge at x = 1787 in frames 0-1. It then speeds up smoothly. Front-edge step per frame is ≈ −1 at f2, −14 at f20, −23 at f35 and −37 at f53, roughly uniform acceleration of ≈ 0.7 px/frame².
   - Cut by the right edge in frames 0-36. For those frames ref_x = front edge x0 + 583/2 (extrapolated). From f37 to f53, ref_x = bbox centre.
   - Root assumed at the bbox centre. A rear-axle root would shift ref_x by a constant, which does not change speeds.
   - Front wheel arches ≈ x 850-960 and rear ≈ x 1200-1310 at f53.
3. **ground**: uniform grey, no markings or static props. **Shadows**: soft, around both objects, excluded from the masks.

## Events
- Frames 0 and 1 are identical: a held first frame, and motion starts between frames 1 and 2.
- f2: the cyclist is moving and the car starts creeping.
- f7: the cyclist is fully in view.
- f14-15: the car's mirrors enter.
- f37: the car is fully in view.
- f47: the x-ranges of the two objects first overlap. They pass each other in separate lanes (Δy between centres = 259.5 px), with no contact.
- At f53 the centres have not yet crossed (car 1101, cyclist 1072).

## Camera
Static top-down view with no zoom. Both objects keep a constant pixel size, and the cyclist's speed is perfectly constant. The background has no texture, so there are no features to measure a shift against.

This is a 2D scene, so one metres-per-pixel scale applies to both objects (same ground plane, same depth).

## Reliability and ambiguities
- Edges are good to ±1-2 px and the cyclist ref_x to ±1 px.
- The car's ref_x is less certain:
  - For frames 0-36 it depends on the assumed length of 583 px (±6 px).
  - Fully visible bbox centres scatter about ±2 px because the length varies.
- For per-frame car speed, the front edge x0 is the cleanest signal in every frame (the same rigid offset from the centre).
- Mask lengths can include 1-3 px of motion blur at high car speed.
