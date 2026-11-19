# Q1462 — height of the forklift (m)

The file and the question both run at 24 fps. The scene has a static camera, a forklift and a red car moving away towards the upper left.

## Method
- Prior: the forklift accelerates at 2 m/s² from rest, so s(t) = t². The track starts at frame ≈0: the free fit gives k0 = -0.15…0.1 frames, and frames 0 and 1 differ by only 1.7 mm. With k0 = 0, the displacement from t=1 to t=2 is 3.0 m.
- Focal length:
  - Route 1 (fit_clean.py): a joint fit of the trajectory (straight line, s = ((k-k0)/24)², pinned at t=1 by depth 16.795 m, with |P(48)| constrained to 19.098 m) and of a 3D box (L, W, H, plus an origin offset). The box is aligned with the motion direction, and "up" is perpendicular to the motion direction with no camera roll; a free roll came out at ≈ -1°. The fit uses the visible-mask bounding-box sides in frames 13-45/50, where the forklift is fully visible and not touched by the car. From frame ~55 the car contaminates the top of the forklift mask, so those frames are excluded. The fit gives f ≈ 3300-3320 px (hfov ≈ 42°), with rms ≈ 0.6 px on every side.
  - Route 2 (check2.py): the two-point focal length from the reference points at t=1 and t=2, the two depths and the 3.0 m displacement gives f = 3329 px, which agrees with route 1.
- Box result (k0=0 or free): H = 2.32-2.34 m, L ≈ 3.63 m (including the forks), W ≈ 0.98 m. The vertical origin offset comes out ≈ 0.03 m, which fits an origin at the box centre.
- Sensitivity: if the start were at k0 = 1, f would be ≈ 3480 and H ≈ 2.20, but that fit has a worse rms and an implausible origin offset (0.2 m up, -0.29 m lateral). Fixing f at 3300, 3400 or 3500 gives H = 2.34, 2.26 or 2.18.

## Answer
H ≈ 2.33 m. Confidence: moderate-good (±4%).
