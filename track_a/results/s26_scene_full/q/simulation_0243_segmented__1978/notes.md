# q_1978 – length of the deer (m)

Video: 2D side view, static camera, 30 fps (file and question both 30 fps). Prior: deer speed = 1.277 m/s.

## Scale (from prior)
Fits of horizontal position against frame over all 75 frames (scene/tracks/animal.csv, re-checked):
torso_cx 6.55, muzzle tip 6.51, centroid 6.45 px/frame. Using ≈6.52 px/frame = 195.6 px/s gives
scale = 1.277 / 195.6 = 0.00653 m/px. Vertical drift is negligible, and the speed is constant (the quadratic term is about 0).

## Length (horizontal extent of the bounding box)
- The mask bbox width changes with the tail swing and the gait: 412 px at frame 0, median 481, max 508.
  I checked frame 29 on a gridded crop: the tail tuft is at x≈240 and the muzzle at x≈745, so 505 px.
- Body without the tail (rump to muzzle): ≈344 px.
- Readings: frame-0 bbox 412 px → 2.69 m; median animated bbox 481 px → 3.14 m; body without tail 344 px → 2.25 m.
- Answer: 430 px × 0.00653 = 2.81 m. It sits between the frame-0 bbox and the median animated bbox, because the
  frame at which the reference took the world bbox is unknown.

## Check
The second route uses the muzzle-tip track alone for the speed (6.51 px/frame). This changes the scale by less than 1%.
Confidence: moderate. The main uncertainty is which pose and frame defines the bbox (±15%).
