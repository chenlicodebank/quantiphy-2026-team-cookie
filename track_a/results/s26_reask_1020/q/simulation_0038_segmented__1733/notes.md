# Q1733 — length of the rock (m)

File is 25 fps, question_fps = 24. Per-frame displacements are converted with 24 fps, as the reference answers do.

## Scale (from the person, prior 1.3 m/s, depth 179.1 m)
- Person image motion (pelvis, shirt and head-top fits all agree): 1.333 px/frame, almost straight down the
  image. 1.3/24 = 0.0542 m per frame.
- The given distance changes only 0.094 m/s, which is below the 0.1 m/s flag, so the origin is treated as
  static/root. The other reading (motion fully transverse, f = 4406) is rejected for two reasons:
  - The apparent body height swings 33–44 px with the gait, so the stride is foreshortened in the image's
    vertical direction. That means the person walks toward or away from the camera under an oblique view.
  - It would make the legs-together height only 1.38 m.
- Model (`human_geom.py`):
  - image speed = v·sin(d)/s
  - legs-together height (p10 ≈ 34.4 px) = H·cos(d) + a·sin(d), with H = 1.70–1.80 and a = 0.22–0.32 m
    (foot/body depth)
  - Result: depression d ≈ 57° (55–59), s ≈ 0.0341 m/px at the person, f ≈ 5230 px (5150–5330),
    HFOV ≈ 16.7°.
- Checks:
  - Arm-to-arm width 16 px → 0.55 m (including antialiasing).
  - Full-stride height 43 px → stride ≈ 0.65 m.
  - Head ≈ 5–6 px → 0.19 m.
  - All plausible.

## Rock (static, mask min(BGR) < 200, frame 30)
- Bounding box: 701 × 625 px, from (557, 17) to (1256, 642).
- With the camera above (pitch ≈ 56.7°, camera ≈ 152 m above the ground), I projected the silhouette onto
  horizontal planes z0 = 0–9 m (`rock_ground.py`). The rock is about 187–195 m from the camera.
  - Extent along the camera's horizontal x axis: 26.4 m (z0 = 0) to 24.9 m (z0 = 9). This holds within ±1 m
    over the f/d range.
  - Silhouette footprint: maximum caliper 33.2 → 31.2 m along a diagonal (about 52° in the ground frame).
    Minimum caliper ≈ 22 m. Depth extent 29 → 27 m.
  - The far silhouette is raised by the rock's height, so the true diagonal and depth extents are smaller,
    by about 0.5 × height (roughly 3–5 m for a 10–15 m tall boulder). That puts the true long footprint
    extent at about 28–29 m.
- Tried and discarded:
  - Half-ellipsoid silhouette fit (`rock_fit.py`): ill-conditioned, IoU only 0.9, axes inconsistent.
  - Mirrored near-contour (`rock_front.py`): the right extreme is not at the ground, which gives a nonsense
    44 m depth.

## Answer
The rock's length is its longer horizontal extent: 25.5 m along the camera axes, and about 29 m along the rock's
own long diagonal. World-axis orientation is unknown, so I answer **27.5 m** (plausible range 25–31 m).
Confidence: moderate. The main uncertainties are the rock's height and its orientation; the scale itself is
probably good to about 5%.
