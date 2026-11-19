# Q2293 — height of the left person (cm)

- The left person (light top, green cargo trousers, x≈340–430) is the farther person: distance_far_person_camera = 3.130 m.
  File fps = question fps = 24.
- Lab method: f = 0.5959 × 1280 = 763 px; height = depth × pixel extent / f.
- Pixel extent measured in code (measure.py) on frames 0, 10, 20 (she stands still, identical results):
  - head top (hair/background transition, row-min intensity drops 170→23): y ≈ 172.5
  - shoe soles: the nearer shoe's bottom edge y ≈ 577.5 (contrast falls 71→29 at 577/578); the farther shoe ≈ 567;
    the floor point under the body centre ≈ 572. scene/ record said 173 → 575 (402 px), consistent.
  - adopted extent ≈ 403 px (range 400–405).
- Height = 3.130 × 403 / 763 = 1.653 m → **165 cm** (range 164–166 cm for 400–405 px).
- Check: using the Z component of the depth instead (if depth were Euclidean, person 260 px off-axis, factor 1.057)
  would give 156 cm; the card's convention (depth used directly, as a depth-map Z value) gives 165 cm. A sanity
  check on the right person (depth 2.002 m, ≈617 px cap-to-sole) gives 162 cm with the same convention — both
  plausible adult heights, so the direct-depth convention is adopted.
- Confidence: moderate-high (±2 % on pixel extent; main uncertainty is the depth convention).
