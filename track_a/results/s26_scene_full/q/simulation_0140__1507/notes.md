# Q1507 – bird speed at t = 1.0 s (frame 24 at 24 fps; file fps = question fps = 24)

## Scale (focal length)
- Prior: window frame width = 1.48 m. Central-facade windows next to the neon sign measure about 130 px across
  the outer dark frame (row band y 420–500: window 1 x≈840–970, window 2 x≈1023–1153; `winprof.py`).
- The windows are on the same backdrop as the sign, so they are at the sign's depth: sign distance 34.5 m, which
  gives Z ≈ 34.4 m (the sign is only slightly off-axis).
- f = 130 × 34.4 / 1.48 ≈ 3022 px (horizontal FOV ≈ 35°). The principal point is taken at the image centre.

## Bird 3D
- I back-projected the mask centroids from scene/tracks/bird.csv (checked on frame 24; the box sits on the bird)
  with the given distances: Z(0) = 24.46 m and Z(0.5 s) = 24.34 m.
- So almost all of the drop in distance comes from the bird moving toward the optical axis. The depth Z itself
  changes only about −0.24 m/s.
- I extrapolated Z linearly to frames 23–24 (Z ≈ 24.2 m). Holding Z constant changes the result by less than 1%.
- I smoothed the pixel positions with a local quadratic over ±6 frames (wingbeats make the centroid jitter).

## Result
- Speed at frame 24 = |P24 − P23| × 24 ≈ 3.42–3.46 m/s.
- Checks with other choices:
  - Raw one-frame difference: 3.61 m/s.
  - Smoothing over ±3 frames: 3.53 m/s; over ±8 frames: 3.40 m/s.
  - Mean of raw per-frame speeds over frames 20–28: 3.42 m/s.
- Sensitivity: ±4% in f gives ∓4% in the speed.

**Answer: 3.45 m/s.**

## Confidence
Medium. The main risk is the assumption that the windows lie at the sign's depth of 34.5 m. If they were instead at
the bird's take-off depth of about 25 m, the speed would be about 4.7 m/s.
