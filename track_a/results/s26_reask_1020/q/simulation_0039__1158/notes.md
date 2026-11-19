# q1158 – eagle wingspan (simulation_0039)

Time base: file is 25 fps / 75 frames but frames 1, 26, 51 duplicate 0, 25, 50, so there are 72 unique frames
rendered at 24 fps (= question_fps). Unique index k = file frame minus the number of duplicates up to it;
t = k/24 (t=1 s -> file f25, t=2 s -> file f50).

## Scale (focal length) from the prior: boat speed 4 m/s (scale.py)
- Boat hull centroid (scene/tracks/boat.csv, hull_cx/cy) fitted linearly over unique frames 0–62 (before the
  bow gets cut by the edge): 8.33 px per unique frame. Stern x1 slope agrees (8.07 px/frame in x vs 8.02).
- 3D points = depth × unit ray((u-768)/f, (v-768)/f, 1) at t=1 s (177.2077 m) and t=2 s (177.9993 m). Solved
  |P2-P1| = 4 m -> **f = 9031 px** (HFOV 9.7°). Ignoring the ray direction (lateral = sqrt(4²-0.79²)) gives 9056 px.
- Checks on this scale: boat hull 495 px -> 9.7 m (plausible fishing boat); person width 28 px at 183 m -> 0.57 m;
  person walking ~2.08 px/unique frame -> ~1.0 m/s. All plausible.

## Wingspan (span.py)
- Bird mask per frame (dark threshold at 50 % / 65 % between bird and local background), max Feret
  (tip-to-tip) diameter of the convex hull. Frames 24–26 (merged with the person's shadow), 27, 61, 62 at 65 %
  threshold are segmentation outliers and ignored.
- Flap-cycle maxima: f6 ≈ 79 px, f33 ≈ 82 px, **f57 ≈ 89.4–90.2 px** (wings fully spread, checked on the overlay
  frames/span_57.png: line runs tip to tip; scene track main axis 90.65 px).
- Eagle depth at f57 (unique 54, t = 2.25 s): linear in the given values -> 176.56 m.
- Wingspan = 89.8 × 176.56 / 9031 = **1.75 m** (range 1.73–1.77 for 88.4–90.65 px).

## Second route / confidence
Naive-lateral focal (9056 px) gives 1.75 m as well. Value is a plausible eagle wingspan. The other flap peaks
(79–82 px -> 1.58–1.62 m) are smaller because the wings are less flat/spread there; the question asks for
fully spread wings, so the maximum is used. Main uncertainty: wing foreshortening / max-pose; ~±5 %.
