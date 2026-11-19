# q747 – clock diameter (m)

2D scene: a static camera looks straight at the wall. The cat walks parallel to the wall, so one m/px scale comes from the prior (cat speed 0.714 m/s).
fps 24 = question_fps, so no re-timing.

- Cat speed in pixels: linear fits of x over frames 1–49 (scene/tracks/cat.csv) give torso_cx 214.0, torso_x0 214.3,
  torso_x1 213.7, cx_dark 216.0, cx_mask 215.7 and nose_x 213.6 px/s. The fits show no real acceleration. The net endpoint value is 212.3 px/s.
  Adopted value: 214.5 px/s, so the scale is 0.714/214.5 = 3.329e-3 m/px.
- Clock (clock.py, frame 24): a circle fitted to the half-max outer edge of the dark rim along 360 rays.
  Centre (1762.0, 292.6), diameter 113.5 px (horizontal 114.0, vertical 112.75). The scene record's 108 px horizontal value
  is a little small: a zoomed crop shows the rim spanning about 1706–1818 px.
- Diameter = 113.5 × 3.329e-3 = 0.378 m.
- Check: the cat's torso length of 146 px gives 0.49 m, which is plausible for a cat, and the clock size is plausible for a wall clock.
  Sensitivity: the speed spread of ±1.5 % and a rim-edge definition of ±2 px give about ±3 %.
- The cat stands on the desk, a little in front of the wall. Following the 2D convention, I ignored this depth difference.
Confidence: moderate–high.
