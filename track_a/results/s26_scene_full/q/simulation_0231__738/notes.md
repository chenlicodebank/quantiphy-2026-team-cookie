# Q738 – length of the teacher's table (m)

Prior: black cat speed = 0.714 m/s. fps 24 = question_fps (no re-timing). Camera static, wall facing the camera.

## Cat pixel speed (scene/tracks/cat.csv, checked)
Cat walks steadily left→right on the desk top, f0–f49, whole body visible.
- torso_cx: net 433.5 px / 49 frames → 212.3 px/s; linear fit 213.9 (1st half 215.5, 2nd half 212.5)
- cx_dark 214.9–216.0, cx_mask 214.2–215.7, cx_bbox 212.6–216.5
→ 214 px/s (±1 %). Scale = 0.714 / 214 = 3.34 mm/px **at the cat's depth**.

## Desk pixel length at the cat's depth (desk.py, edges2.py, edges3.py)
The desk top is seen in perspective: the near edge is longer than the rear edge. Measured on f0 (right end clear) and f49 (left end clear):
- right side edge of top: sub-pixel line x = -0.692·y + 1304.9 (residual ≤1 px); rear-right corner ≈ (797, 733.5), front-right ≈ (775.5, 765)
- left side edge (staircase artefacts in the row profile): rear-left corner ≈ (186, 733.5), front-left ≈ (70, 765)
- the two side lines converge at ≈ (939, 529), close to the image centre, so the camera looks straight at the wall.
- Pixel length vs row (linear for a horizontal plane): 611 px at the rear edge (733.5), 706 at the front (765).
- Cat's walking line: near paws touch at y ≈ 742.5, far paws at ≈ 735 → centre line ≈ 738.5 ± 1.5.
  Desk length on that row = 626–633 px (different edge fits) → **629 px**.

## Answer
629 px × 3.336 mm/px = **2.10 m**.

Check: the rear-edge length (611 px) and front-edge length (706 px) would give 2.04 m and 2.36 m. The cat walks close to the rear edge, so the result sits near the low end, and its uncertainty is about ±1.5 % from the row choice and the edge fit.
Cat torso 146 px → 0.49 m. That is a realistic cat, which confirms the scale is sensible.
Confidence: moderate-high (±3 %).
