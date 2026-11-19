# q_478 — diameter of Callisto model (m)

Prior: Callisto speed = 0.627 m/s. 2D scene (all moons in one plane facing the camera), file fps = question fps = 30.

## Scale
- Callisto track (scene/tracks/callisto.csv, frames 0–99, checked on frames): uniform circular motion,
  R = 414.1 px, ω = 8.43 °/s → 60.9 px/s; mean of per-frame backward-difference speeds = 61.09 px/s
  (path length / 99 frames identical).
- Scale = 0.627 / 61.09 = 0.010264 m/px.

## Callisto pixel diameter (re-measured, scripts in this folder)
- `fit_disc.py`: forward-model fit (antialiased disc + linear shading + Gaussian blur + sky), green channel
  (the red orbit line passing behind the moon has little green), 20 frames: **11.00 ± 0.25 px**.
- `edge_size.py`: radial profiles in 36 directions, 34 frames: half-level 10.74 ± 0.22 px, steepest edge 10.85 ± 0.35 px.
- scene record half-max radial profile: 11.1 px; `measure_size.py` 50 % mask eq. diameter 11.6 (slightly inflated
  by the orbit line in gray), flux/peak eq. diameter 11.1.
- Adopted 10.95 px (spread 10.7–11.1).

## Answer
D = 10.95 px × 0.010264 m/px = **0.112 m**.
Second route: half-level edge (10.74 px) → 0.110 m; disc fit (11.00 px) → 0.113 m. Confidence: moderate
(±3–5 % from edge definition of a ~11 px blurred disc; the scale is accurate to <0.5 %).
