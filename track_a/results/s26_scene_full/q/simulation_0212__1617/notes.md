# Q1617 — speed of the dog at t = 1 s (frame 24, question_fps = file fps = 24)

Answer: **1.0 m/s**

## Camera model
- Pinhole camera, principal point at the image centre, level (pitch ≈ 0). Evidence for pitch 0: with f ≈ 2100,
  a constant-height point gives K = Z·(v−cy) consistent at both given depths, within 1 % for the dog (951 vs 960)
  and 3 % for the cat. The camera height from the cat's feet (≈0.78–0.80 m) also matches the mirror-bottom floor point
  (6.407 m at row ≈805). The front table-leg foot gives 5.59 m against the given 5.69 m (−2 %).
- Focal length from the cat prior (catfit.py). The model is straight, level, constant-velocity motion with |V| = 0.94 m/s,
  |P(0)| = 4.199 m and |P(1 s)| = 4.481 m, fitted to the cat's core, centroid and bbox tracks over clear frames
  (0–23, plus 45–49).
  Result: **f ≈ 2100 px** (range 2054–2131; HFOV ≈ 49°). The plain displacement check |P24−P0| = 0.94 gives f ≈ 2150.

## Dog
- Tracked point: the record's torso-core centroid, with the mask centroid as an alternative. The record was checked on
  frames 0, 12 and 24: the dog is never occluded and the core lies on the body.
- Its height Y below the camera (≈0.455 m) was calibrated from the given distances at t = 0 (5.094 m) and t = 0.5 s
  (4.625 m). Between frames 0 and 12 the dog moves 0.51–0.52 m, an average of 1.03 m/s.
- A straight path through P0 and P12 does not fit: it predicts row 786 at frame 24, against the observed 760.
  The dog curves toward a more lateral heading.
- Route 1 (dogsmooth.py): Z(t) = K/(v−cy) for each frame, smoothed with polynomials over wide windows anchored at the
  two given depths, and X from u. The lateral velocity is robust at Vx ≈ −0.92 m/s. Vz at frame 24 is noisy
  (0.18–0.82 m/s), so the speed spans 0.92–1.27 m/s; median **1.00 m/s**, wide-window fits 0.94–1.02.
- Route 2 (dogjoint.py): a joint fit of a level ground path. Speed(t) and heading(t) are polynomials, P0 comes from
  the given distance, |P12| = 4.625 is a constraint, and the fit uses the u and v tracks over frames 0–32/36/40/44.
  Speed at frame 24: 0.92–1.12 m/s, median **0.96 m/s**. A constant-speed model fits about as well (u rms 4.1 vs
  3.7 px) and gives 1.02–1.06 m/s.
- Abandoned cues: ECC registration of the torso scale was unstable (the body deforms). Planted-paw detection was
  swamped by moving floor shadows.

## Confidence
The routes agree at 0.95–1.05 m/s. The main uncertainty is the depth rate at frame 24, which only the noisy row cue
constrains. Expected error is about ±8 %.
