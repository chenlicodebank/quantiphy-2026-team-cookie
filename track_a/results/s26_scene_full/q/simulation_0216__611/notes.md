# q_611 — length of the wooden bench (m)

Prior: the black cat's speed is 0.94 m/s. No depth_info. fps = question_fps = 24, so no re-timing.

## Scale from the cat
- I checked the cat track (scene/tracks/cat.csv, `body_x_matched`) again. The mean of the per-frame 2D steps is
  17.74 px/frame, the net x is 17.73 px/frame, and the nose read by eye moves 870 px over 49 frames (17.76).
  So the speed is 425.8 px/s.
- That gives 452.8 px/m **at the cat's depth**. The cat's ground contact is at y ≈ 1015: the near-side paws are at
  1020 and the far-side paws at about 1010.

## Bench pixel length (bench_rows.py, bench_edges.py)
- I took sub-pixel half-saturation edges of the bench top's front edge (rows 796–806) on frames 20, 35 and 48,
  where the cat is clear: x = 23.7 → 476.9, which is **453.1 px**. The top is the widest part of the bench.
- The full image extent is 24 → 492 (468 px; scene.json says 467). But the rightmost pixel belongs to the back edge
  of the top, which is farther away. So the front edge is the right measure of the x-length.

## Perspective correction
- The bench stands farther back than the cat. Its front feet touch the floor at y ≈ 984–991 (mean 987.5) and its
  back feet at y ≈ 965.
- The x-separation of the front feet and the back feet gives a depth ratio of about 0.94. With the principal point
  at x ≈ 960, that puts the horizon at y_h ≈ 600 (±40).
- For lengths parallel to the image x-axis, the pixel scale on the floor is proportional to (y − y_h). So
  scale_front / scale_cat = (987.5 − y_h) / (1015 − y_h):
  - 0.934 at y_h = 600;
  - 0.942 at y_h = 540.
  - The ratio barely depends on y_h.
- Bench length = 453.1 / (452.8 × 0.934–0.942) = **1.062–1.071 m**.

## Second route / checks
- The plain 2D single-scale answer is 467 / 452.8 = 1.03 m, with no perspective correction. The corrected value is
  about 4% higher.
- The top's two receding ends are not fully consistent with one vanishing point. The bench may be yawed by a few
  degrees, or its slat ends may be shaped. Either way the AABB x-extent changes by only about 1–2%.
- Sanity check: cat nose-to-rump length is 245 px / 452.8 = 0.54 m, and a ~1.06 m slatted bench is plausible.

## Answer
**1.06 m**. It sits between the perspective-corrected value (≈1.066) and the flat 2D value (1.03), weighted
toward the corrected one. Confidence: moderate-high, about ±4%.
