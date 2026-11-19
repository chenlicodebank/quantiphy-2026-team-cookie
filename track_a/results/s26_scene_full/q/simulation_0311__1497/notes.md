# q_1497 – acceleration of the car at t = 1.0 s (frame 24, question_fps = file fps = 24)

Answer: **0.96 m/s^2**

## Camera
- Static camera, principal point assumed at image centre (1280, 720).
- Vertical vanishing point from the centrelines of three poles, fitted row by row (`poles.py`): near pole x = -0.0628y + 2039.8,
  left pole x = 0.0851y + 237.0, middle pole x = 0.0115y + 1124.1. Their pairwise intersections are (1274, 12192), (1266, 12332)
  and (1263, 12052), so VP ≈ (1268, 12190) and roll ≈ 0.
- Ground-plane constraint: the car's origin stays at a constant height. Its rays at frames 24 and 48, scaled by the given depths
  (17.8278 m and 23.1989 m), must sit at the same height below the camera, which fixes the pitch for each f. Requiring
  that the pitch also reproduces the vertical VP gives **f ≈ 3612 px** (HFOV ≈ 39°), pitch 17.5°, and camera height 7.4 m above
  the origin plane (`motion3d.py`, `final.py`).
- Checks on f:
  - The car's rear width at frame 48 (~341 px) gives about 1.97 m, which matches a LaFerrari (1.99 m).
  - Apparent car height (~180 px at frame 48) is consistent with H = 1.15 m.
  - The rear-face to deck ratio on the car implies a ~19° view, consistent with the 17.5° pitch.

## Motion
- I tracked the car frame by frame with LK features on the car mask (pole band excluded), using a forward-backward check
  and a RANSAC similarity fit (`track.py`). Chaining these fits propagates a reference point (the silhouette centroid at
  frame 48, (1162, 792)) to frames 9-71. On frames 12-71 the propagated points stay on the same physical spots (fuel-cap
  ring, tail light; `frames/pts.png`).
- I back-projected each frame's point onto the origin plane and took per-frame 3D speeds (backward difference × 24).
  They rise linearly from ~5.3 to ~8.0 m/s, so the motion is uniformly accelerated.
- Linear fit of speed vs t over frames 10-71: a = 0.964, v(0) = 5.06 m/s. A quadratic fit to path length gives 0.946.
- Sensitivity:
  - Reference pixel moved ±40-80 px: 0.93-1.00.
  - Vertical VP y between 11900 and 12500: 0.954-0.974.
  - Fit windows 10-40 / 20-50 / 29-71 / 40-71: 0.95 / 0.89 / 0.98 / 1.06.
- The displacement from frame 24 to 48 is 6.52 m.

## Second route and why the routes disagree
- The scene record's silhouette centroid (frames 29-71) and bbox corner, put through the same camera, give a ≈ 0.61-0.65
  (`check2.py`).
- This route is biased. The ray's angle below horizontal falls from ~23° to ~15° as the car recedes, so more of the rear
  face and less of the roof is visible. The silhouette centroid and the extreme points therefore slide toward the car's rear
  and lag the true motion.
- The LK-tracked physical points do not drift (verified visually), so I use the LK route.
- Scene record note: the scene record's centroid/bbox tracks shouldn't be used for accelerations.
- Frames 0 and 1 are identical. The 3D speed does not start from 0: extrapolated v(0) ≈ 5 m/s.

Confidence: moderate-good, about ±8% (mainly f / reference-point choice and per-frame noise).
