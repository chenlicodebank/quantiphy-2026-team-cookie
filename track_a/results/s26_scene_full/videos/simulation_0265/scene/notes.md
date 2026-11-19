# simulation_0265 — measurement record (pixels, seconds)

Video: 2D simulation (Blender), 2560x1440, 24 fps, 72 frames (t = frame/24, frame 0 at t = 0).

## Scene content
- **vehicle** (the only object): a dark grey/black futuristic car seen from directly above. Its nose points LEFT
  (-x), it has blade-like fins at the nose and four dark diamond-shaped wheel pods at the rear (right-hand) corners.
  It drives straight LEFT along image row y ≈ 720, starting from rest.
- Background: plain uniform light grey (~RGB 193). No ground markings, no other objects, no horizon. Nothing static
  to measure.
- Camera: static (the background stays at a constant level). The scene is a top-down 2D plane, so there is no
  perspective and a single m/px scale applies. Height is not visible.

## Files
- `scene.json`: inventory, sizes, events and camera.
- `tracks/vehicle.csv`: one row per frame (0–71). Columns:
  - `ref_x, ref_y`: the reference point (estimate of the vehicle origin = centre of the full bounding box).
  - `ref_method`: how `ref_x` was found (see below).
  - `nose_x` (left edge) and `tail_x` (right edge of the rear pods). Blank when that edge is outside the frame.
  - `bbox_*`, `length_px_visible`, `length_px_full`, `width_px`, mask area and centroid, truncation flag,
    occlusion flag (never occluded).
- `tracks/vehicle_raw.csv`: raw segmentation output (track.py).
- `scripts/`: track.py (segmentation |grey−193.5|>10 plus morphology), parts.py (part extents), blurcheck.py and
  crops.py (stretch investigation), final.py (builds the csv and json), probe.py.

## Key numbers
- Visible frames 0–66. Fully inside the frame only in frames 7–50.
  - Frames 0–6: about 20 px of the rear tip is cut off by the right edge.
  - The nose reaches x = 0 at frame 51. The last sliver is in frame 66, and frames 67–71 are empty.
- Width (across the motion, y): **515 px** (rows 462/463–976/977), constant throughout. This is the most reliable size.
- Length (along the motion, x, full bounding box from nose to rear pods):
  - **1012–1013 px** while slow (frames 7–9).
  - It grows steadily with speed: 1033 at frame 30, 1071 at frame 50 (+6 %).
  - The nose-to-body-tail distance on the centre row grows the same way: 997 → 1015 → 1047 px.
  - The edges are sharp, so this is not ordinary motion blur. The rendered model really stretches along x
    (shape and lighting change). The quadratic fit is L(f) = 1011.66 + 0.0249 f + 0.02339 f² (max residual 1.1 px),
    and is used for the truncated frames.
  - For the vehicle's own length, use the at-rest value of about **1012 px**. Frame 0 is clipped; the fit gives 1011.7.
- Motion: at rest in frames 0–1 (the two frames are identical). Motion starts at frame 1 (t = 0.042 s).
  - Direction: straight −x. The y drift is under 1 px.
  - The per-frame step grows nearly linearly, by about +1.2 px/frame each frame (nose steps: 2 px at frame 2,
    ~30 at frame 24, ~60 at frame 50; rear steps ~76 px at frame 65). This looks like constant acceleration.
  - No bounce, impact, stop or direction change.
- Reference-point centre crossings: ref_x ≈ 1110 at frame 40. It crosses the image centre x = 1280 between
  frames 36 and 37, and reaches x = 0 between frames 58 and 59.

## Reference point and reliability
- Frames 7–50: ref_x = centre of the full mask bounding box (±0.5 px). The origin is assumed to be the bounding-box
  centre. The mask centroid sits about 15–20 px further back (more mass at the rear) and is given as an alternative.
- Frames 0–6: ref_x = nose_x + (L_fit − 1)/2. Frames 51–66: ref_x = tail_x − (L_fit − 1)/2. These depend on the
  length fit, so allow about ±2–5 px, more by frame 60–66 where the length is extrapolated. The extrapolated centre
  has negative x (it is off-screen).
- The nose and tail edges are sharp (±1 px) and give a centre-independent alternative for speeds. The stretch makes
  the nose move faster than the tail: the rate of stretch is ~1–2.5 px/frame against steps of 30–75 px/frame.
  A per-frame step (backward difference) measured from the centre is about the mean of the nose and tail steps.
- Masks were checked visually on overlays at frames 3, 10, 30, 40 and 58: they cover the whole vehicle including the
  pods and fins. There are no shadows and no occlusion.
