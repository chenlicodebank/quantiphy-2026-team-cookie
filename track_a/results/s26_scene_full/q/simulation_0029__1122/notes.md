# Q1122: boat speed at t = 1.0 s (m/s)

Time base: question_fps = 24, so t=1 s is frame 24 and t=2 s is frame 48. The file's rate is 25 fps, but I used the frame index only.
The camera is static (scene record). The principal point is taken as the image centre (480, 480).

## Method (script: solve.py)
- Eagle pixel centre: scene/tracks/bird.csv cx_interp/cy_interp. Frame 24 = (235.6, 521.8), frame 48 = (409.7, 527.8).
- Boat pixel centre: hull_bbox_cx/cy. Frame 24 = (483.5, 646.5), frame 48 = (421.5, 648.0).
- Back-projection: P = d * (u-cx, v-cy, f)/|(u-cx, v-cy, f)|, with the depth_info distances.
- Focal length: I solved for the f that makes the eagle's 3D displacement between t=1 and t=2 equal to 12 m (prior 12 m/s, steady flight).
  The result is f ≈ 2646 px (HFOV ≈ 20.6°). Raw centres and local linear fits (±2, ±4 frames) give 2644-2648.
- Boat speed: the boat moves at constant velocity (steady pixel step, smooth growth in size), so its speed is the 3D chord from t=1 to t=2 over 1 s.
  The result is 4.11-4.12 m/s. About 2.70 m of it is radial approach (depth 133.96 → 131.26) and about 3.1 m is lateral.

## Checks
- Eagle steadiness: on frames 0-24, with depth extrapolated linearly, the lateral 9.75 m and radial 7.45 m give about 12.3 m/s. This is consistent with a constant 12 m/s, so the f estimate holds.
- Boat consistency: the hull length grows 164 → 168 px (+2.4%) while the depth drops by 2.0%, which fits the given depths.
- Size sanity at this f: the boat is about 8.3 m long and the eagle wingspan is about 1 m. Both are plausible.

Answer: 4.12 m/s. Confidence: moderate-high, ±5%. The main uncertainty is whether the eagle flies at exactly constant velocity.
