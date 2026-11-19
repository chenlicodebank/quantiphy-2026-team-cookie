# Q881 – acceleration of the tennis ball at t = 1 s (m/s^2)

2D simulation, fps 24 (file and question agree), t = 1 s -> frame 24. Single ball moving left->right along y ≈ 364 px,
static camera, decelerating smoothly (no bounce). Prior: diameter 0.17 m.

## Tracking (measure.py, own re-track)
Lab b* > median+12 mask, b*-weighted centroid; frames 6–39 fully visible (5 and 40 cut by edges, excluded).
Matches scene/tracks/ball.csv.

## Acceleration in px (fit.py)
Quadratic fit x(t), centroid: frames 6–39 −220.5 px/s², 6–22 −223.4, 17–31 −219.4, 22–39 −213.4, 12–36 −220.9;
cubic fits evaluated at 1 s: −219…−221. Linear fit of per-frame speed vs time: −218.8 px/s².
=> constant deceleration ≈ −220 px/s² (raw single-frame difference at f24 is −200, noisy; ±0.5 px jitter).

## Scale (diam.py, prof.py)
Mask bbox 35–36 px (inclusive, counts partially covered edge pixels). Sub-pixel half-max crossings of the Lab
colour-distance profile along the horizontal diameter: 34.7, 35.1, 35.1 px (frames 12, 20, 30). The vertical profile is
spoiled by the shadow above the ball. Using D = 35.0 px -> 0.17/35 = 4.86e-3 m/px.

## Answer
|a| = 220 × 0.17 / 35.0 ≈ 1.07 m/s² (deceleration; reported as a magnitude). If D = 36 px (bbox), it would be 1.04.
Second route (fitting speed against time) gives −218.8 px/s², which converts to 1.06 m/s². Confidence: about ±4 %,
and the diameter in pixels is the main uncertainty.
