# simulation_0093 — measurement record (pixels, seconds)

2D simulation, 24 fps, 38 frames (t = frame/24, 0–1.5417 s), 1920×1080. Static camera; uniform dark-grey
background (RGB ≈ 80,81,88). No ground, horizon, markings or static objects.

## Objects
- **plane**: white Air China airliner (A320-type, red phoenix on the tail), side view, nose to the left, upper
  object. It moves left (−x) horizontally. Fully visible in frames 0–18; the nose is cut by the left border from frame 19; only
  a sliver remains at 34; out of frame from 35 on. Pixel size (frames 0–18): length nose→tail tip 606–612 px (frame 0: 612,
  median x1−x0 = 608), height fin top→engine bottom 181–182 px. bbox at frame 0: x 722–1333, y 370–550.
- **car**: small white angular pickup (Cybertruck-like), side view, below the plane. It moves right (+x) horizontally.
  It is visible and unoccluded in all 38 frames. Length 91 px at frame 0, slowly growing to 98 px at frame 37 (the perspective
  camera shows a bit more of the car as it moves off-centre). Height 30 px (y 605–634; the very light roof edge may
  be missed by ~1–2 px). bbox at frame 0: x 854–944.

## Motion (raw facts, no models)
- Frames 0 and 1 are identical: both objects are at rest. Motion starts between frames 1 and 2 (t = 0.0833 s).
- plane: per-frame step −40.0…−41.0 px, mean −40.36 px/frame. The tail-fin centroid steps are constant to ±0.5 px,
  so the velocity is constant and the plane does not accelerate. y is constant (ref y ≈ 459.5–460).
- car: per-frame step 19.5–21.0 px (bbox), 19.7–20.4 (column centroid), mean 20.13 px/frame. The velocity is constant and y is constant
  (ref y 619.5–621).
- At frame 0 the plane ref is 125.5 px right of and 159.5 px above the car ref (203 px apart).

## Files
- `scene.json`: inventory, sizes, events, camera, relations.
- `tracks/plane.csv`, `tracks/car.csv`: one row per frame with frame, time_s, ref_x, ref_y (the reference point),
  bbox x0,y0,x1,y1 (inclusive), mask centroid, length_px (x extent), height_px (y extent), mask area, visible,
  occluded_or_clipped, ref_method.
- `scripts/measure.py` (segmentation: max |RGB − bg| > 18, 3×3 opening, components ≥ 30 px, split at y = 580),
  `scripts/write_record.py` (CSVs), `scripts/check_steps.py` (step check from fin and column centroids),
  `scripts/check_overlay.py` (overlay check), `scripts/crops.py`, `scripts/probe.py`.

## Reference points and reliability
- car ref = bbox centre (±0.5 px). It is reliable, and the car's origin should be near the centre of its box.
- plane ref = tail-fin centroid + −260 px. The offset is fixed so the ref equals the bbox centre over frames 0–18. It
  is 1024.5 at frame 0, while the bbox centre there is 1027.5. Because the reference is rigid, it stays valid after the nose leaves the frame.
  Frames 33–34 are extrapolated (fin partly cut). The true Blender origin of the plane is unknown and is assumed to be the bbox centre.
  The y ref is the bbox mid-height (fin top to engine bottom), not the fuselage axis; the fuselage axis is about y ≈ 490.
- In clipped frames (19–34), the bbox, length and mask centroid describe only the visible part. Do not use them as
  the plane's position or size. The raw tail-tip x1 steps look smaller (~38.5 px) because the tip is thin and faint, which is an artifact.
  Use ref_x instead.
- I checked overlays of the masks, bboxes and refs on frames 0, 12, 25 and 32: the refs and boxes sit on the correct objects.
- Scale: one metres-per-pixel factor from whichever object's prior is given (e.g. plane length 608 px, car length
  ~91–98 px, plane speed 40.36 px/frame, car speed 20.13 px/frame). There is some perspective, because the car's apparent
  length changes by 7%. Prefer the frame the question refers to.
