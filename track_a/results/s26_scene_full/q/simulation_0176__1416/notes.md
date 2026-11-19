# q1416: height of the stone cliff (the big rock), simulation_0176

The file runs at 24 fps and question_fps is also 24, so t = 0.5 s is frame 12 and t = 1 s is frame 24.

## Focal length from the plane (prior + depth_info)
- Nose pixel positions come from a background-subtracted mask (`nose.py`; median background, threshold 18).
  The nose x is averaged over neighbouring frames to cut noise; the nose y is the tip row of the mask.
  - Frame 12: (1071, 155). Frame 24: (392, 177).
- The nose moves 153.582 × 0.5 = 76.79 m between the two frames (constant speed). The depths are 284.98 and 305.627 m.
  Solving |d2·r2 − d1·r1| = 76.79 with the principal point at (960, 540) gives **f = 2645 px** (horizontal FOV 39.9°) (`solve.py`).
  - Sensitivity: moving the nose x by ±5 px at both ends gives f = 2605–2685 (±1.5%). Moving y by 5 px has a negligible effect.
- Check (`check.py`): interpolating the 3D nose at constant velocity and projecting it at frames 16, 18, 20 and 28 lands
  within 5–9 px of the measured mask nose x0 in every frame. The bias is consistent, so the track is linear and the given data agree with each other.
  The plane's apparent length shrinks from 472 to 431 px between frames 12 and 24, which fits the depth increase.

## Rock
- Measured on frame 12 (`rock.py`), segmented against a per-row sky reference.
  - Top of the trees: y = 522.
  - Bare rock top (under the trees): y ≈ 600–620.
  - Base where the rock meets the sand: y ≈ 1020–1022 at the front right. It is ≈ 995 at the left part.
- Height = z · Δpx / f, where z = 296.35 m × cos(off-axis angle) ≈ 291–295 m:
  - Whole rock including the tree canopy (522 → 1020, 498 px): **54.8–55.5 m**.
  - Bare stone only (≈ 600 → 1020, 420 px): **46.2–46.7 m**.
- Ambiguity: it is unclear whether the object's bounding box includes the trees. The rock looks like a single vegetated
  island asset, which favours including the trees (≈ 55 m). I answered 53 m to hedge slightly toward the bare-stone reading.
- Perspective error: the treetop or base may sit a few metres off the origin's depth, worth ±10 px (≈ ±2%).

## Answer
53 m. Confidence is moderate: the scale is solid (±2%), and most of the uncertainty is whether the trees count.
