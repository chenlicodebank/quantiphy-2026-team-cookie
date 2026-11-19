# Q897 – height of the red cup (m)

2D scene, file fps = question fps = 30. Prior: the cup falls at 9.8 m/s^2 before 0.5 s (free fall over frames 0–14, impact at frame 15).

## Scale (fit.py)
I fit quadratics to the cup's vertical track (scene/tracks/cup.csv), frames 0–14:
- top_y (lid rim, a fixed 3D point, the cleanest edge): a = 6300–6327 px/s^2
- bbox centre / centroid: 6215–6266 px/s^2 (lowered slightly because the visible underside ellipse shrinks)
- bottom_y: 6130–6210 px/s^2 (most affected by the ellipse)
I adopted a ≈ 6290 px/s^2, which gives a scale of 9.8 / 6290 = 1.558e-3 m/px.

## Pixel height (hmeas.py, crops frames_rest.png, frames_14.png)
- The silhouette is 74 px tall at the top of the frame because the underside is seen from below. It shrinks to 64–65 px near camera height (frames 13–14).
- At rest (frames 20–39) it is 65–66 px, measured from the lid top at y 806–807 to the contact line at y 871. The glow on the table below is excluded.
- Adopted true height: 65 px (±1).

## Answer
65 × 1.558e-3 = 0.101 m. That is a realistic size for a paper coffee cup.

Check: the width is 42.5 px, or 0.066 m across the lid rim, which is also realistic. Taking the extreme acceleration routes (6200 vs 6320) and heights (64 vs 66) gives 0.099–0.104 m.
Confidence: high (about ±3%).
