# Q1123: height of the person (m). Answer: 1.8 m (low-to-medium confidence, about ±10 %)

The file runs at 25 fps and the question at 24 fps. Depths are taken at frames 24 and 48 (t = 1 s and 2 s), and the
person's speed per frame is 1.3/24 m.

## Measurements (scene/tracks, checked on frames)
- Person: head-to-foot box height has a median of 77 px over frames 0–74 (±3 px from the gait; about 78 early and
  about 76.6 late, so the apparent size does not grow). Pelvis moves −1.20 px/frame in x and +0.57 px/frame in y
  (feet +0.56).
- The person's camera distance is 139.95 → 139.98 m and barely changes, although the body walks down-left. So the
  origin is roughly static, and its distance is used only as the body depth (about 140 m).
- Boat: hull-box centre (fitted over ±6 frames) goes (229, 763) → (141, 722) between frames 24 and 48. Depth goes
  130.35 → 133.74 m, and the template scale ratio (0.974) matches that depth ratio. If the boat stays at a constant
  height, this gives the camera pitch θ(f) for each focal length f (solve.py).
- Eagle: with the same θ(f) it is also level (Δz < 0.05 m for every f), so the two constraints agree but they are
  degenerate: they do not fix f.

## Focal length / scale routes
1. Speed prior (flat ground, boat-derived pitch): the person walks mostly toward the camera (radial component about
   1.17–1.2 of the 1.3 m/s), so the lateral share, and with it f, is ill-conditioned. This gives f ≈ 7200–8300 and
   H ≈ 1.33–1.53 m. A beach slope of only 3° moves this to f ≈ 4500 and H ≈ 2.5 m, so this route is unreliable. It
   is used only as a weak bound.
2. Eagle wingspan (eagle_vs_person.py): uses the maximum PCA span of the flat-wing frames, projected with the eagle's
   3D heading (about 59° off the image x axis). The ratio H / eagle span is about 0.92 for all f:
   f = 6000 gives span 2.00 m and H 1.85 m; f = 6500 gives 1.81 m and 1.70 m; f = 5500 gives 2.23 m and 2.03 m.
3. Cliff-column vanishing point (columns.py): too noisy to use (f·cotθ ≈ 4×10^4 ± 100 %, which would mean f ≈ 8000).
4. Plausibility check: an adult of about 1.8 m needs f ≈ 6100, which also gives a realistic eagle (about 2 m) and a
   boat of about 7 m.

## Answer
Depth 140 m × 77 px / (f cos e), with f ≈ 6000–6300 taken from the eagle span and the standard-size check. The box
height while walking is about 2 % below standing height. Result: about 1.8 m.

The scale could not be pinned by the speed prior alone because the geometry is ill-conditioned. It rests mainly on
the eagle's wingspan and a plausible adult height.
