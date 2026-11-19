# q_1930 — lampshade diameter (simulation_0216_segmented)

Time base: file fps = question_fps = 24, used throughout.

## Scale from prior (cat speed 0.94 m/s)
- Cat x-track (scene/tracks/cat.csv, checked with measure.py): linear-fit slope 17.65 px/frame for cx,
  17.80 for dark_cx, 17.66 for bbox_x0 and 17.46 for bbox_x1. Mean ≈ 17.7 px/frame, so 424.6 px/s.
  The walk is steady with no vertical drift.
- Scale at the cat's depth: 0.94 / 424.6 = 2.214 mm/px.

## Lampshade
- measure.py checks each row for non-white pixels at frames 0 and 49. The shade is a pleated cone, and its widest
  row (bottom rim, y ≈ 600–605) is 1240–1448. That gives 209 px including about 1–2 px of anti-aliasing,
  so I took 207 px. The scene record gives 206 px.
- Single 2D scale: 207 × 2.214 mm = 0.458 m.

## Perspective check
The cat walks in front of the console. Its paws are at y ≈ 1021, while the furniture feet are at y ≈ 990. The bench
top is seen slightly from above. A rough horizon estimate (from the bench top versus floor foreshortening) puts the
horizon near y ≈ 450, so the lamp is about 5–7% farther away than the cat. The fully corrected value is
≈ 0.48–0.49 m. The video is treated as 2D, where the convention is one scale, but there is mild perspective. I
answered with a compromise value of 0.47 m, which is within about 3–4% of either route.

Sanity check at the same scale: TV 399 px ≈ 0.88 m wide (a 40" TV) and lamp height 287 px ≈ 0.64 m. Both are plausible.

Confidence: moderate-high (±6%).
