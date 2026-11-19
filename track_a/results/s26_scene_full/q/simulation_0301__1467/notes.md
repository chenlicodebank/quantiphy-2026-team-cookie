# Q1467: height of the car (m). Answer: 1.08 m

Video: 3D Blender render, 2560x1440, 24 fps (file fps = question_fps = 24). Static camera.
Prior: forklift acceleration 2 m/s^2. depth_info: forklift 16.7953 m (t=1) and 19.0980 m (t=2); car 17.8278 m (t=1) and 23.1989 m (t=2).

## Camera (pinhole, principal point at the image centre)
- **Motion vanishing point (FOE)**: from LK feature tracks on the rigid forklift (pure translation; `foe.py`, `t0fit.py`),
  the FOE is at (-1155, -488) px (bootstrap sd about 7 px). The car's tracks give the same FOE, so the two paths are parallel.
  A track model p(t) - v ∝ 1/(1 + s(t)/w) with s = t^2 fits with rms 0.3-0.45 px. Free fit of the start time
  gives t0 = 0.000 s, so the forklift moves s = (a/2)t^2 = t^2 m from t = 0.
- **Focal length, route A (main)**: the two outer taillights of the car form a lateral (left/right symmetric) pair.
  Their image direction must point at the lateral vanishing point. With zero roll (confirmed by the forklift's edge
  vanishing-point fit), that point depends only on f. Frames 20-36 give **f = 3591 ± 20 px** (`latmulti.py`). The
  measured angle drifts from 159.9° to 165.0° across frames, yet f stays constant, which validates the model.
  HFOV = 39.2°, camera tilt = 18.6° down.
- **Focal length, route B (prior + depths)**: the forklift's metric 3D feature cloud comes from the s = t^2 m law (`cloud.py`).
  Asking the origin to satisfy |P1| = 16.7953 and |P1 + 3·fwd| = 19.0980 (the 3 m = a/2·(2²-1²) displacement) gives
  f = 3576 for an origin at ground level, centred laterally, and 0.34 of the cloud length from the rear (≈ body centre
  once the forks are excluded) (`solve2.py`). A mid-height origin cannot satisfy both depths. Agrees with A to 0.4%.
- An earlier rough edge-VP fit (3680-4100) was poorly conditioned: the mast and guard posts are tilted. It was not used.

## Car height
- Car feature cloud (LK tracks over frames 14-44 and 20-36, refs f24 and f27): depth per feature in units of the car's
  unknown a/2 (k). k comes from the car's two depths with a ground-level origin at the centre of the cloud:
  k ≈ 2.46-2.50, consistent between t = 1 and t = 2 to within 0.3%.
- Top: the highest features (99.7 pct of height along world-up) sit on the roof crest (checked on an overlay, `viscar.py`).
- Bottom: the visible car is **cut by the invisible ground plane**. The rear-left wheel's lower part ends on a straight
  line running toward the FOE (the intersection of the wheel plane with the ground). The rim (r = 0.10 k) and the tire
  outer edge (r ≈ 0.13 k ≈ 0.32 m) were fitted with 3D circles in the wheel plane about the hub (yellow logo).
  The tire bottom lies ≈ 0.055 m below the visible ground line (f24 and f27 agree).
- Height, roof crest to tire bottom (world-space box including the sunk part), at f = 3590 (`height3.py`):
  1.068 (cloud ref f27), 1.084 (dense cloud ref f24), 1.076 (cloud ref f24). **Mean 1.076 m.**
  Roof to the visible ground line: 0.98-1.01 m.
- If the car scale is set so that the car's ground matches the forklift's ground plane (forklift metric from the prior),
  k rises by about 0.9%, giving 1.085 m.
- f sensitivity: f = 3500 gives 1.09-1.10 m; f = 3680 gives 1.05-1.07 m.

## Answer
1.08 m (roof crest to bottom of the tires). Sanity check: a real LaFerrari is 1.116 m tall.

Caveats:
- The grey untextured slabs behind the rear bumper also reach the ground line. If they extend further below the
  ground, the true bounding-box bottom would be lower; this cannot be observed.
- If the reference used the visible above-ground height instead, it would be ≈ 1.00 m.

Confidence: moderate (about ±5%).

Note: the scene record's tracks were used only for rough boxes and masks. All geometry was re-measured here.
