# q 883 – height of the plant (m)

2D simulation: a potted succulent falls straight down in a plane facing the camera. The prior (a = 9.8 m/s^2 before 0.5 s) sets one m/px scale.

Time base: the file is 24 fps but question_fps = 30. As instructed, every frame-to-time conversion uses 30 fps.

## Acceleration (px)
- Bottom edge y1 of the pot, frames 0–14 (scene record, checked with my own strip-profile tracker in measure.py).
  Quadratic fits give 7.00 (frames 0–14), 7.12 (3–14) and 7.14 (5–14) px/frame^2. My sub-pixel tracker gives
  7.04 (0–14) and 6.92 (5–14). Best value: 7.05 ± 0.1 px/frame^2.
- At 30 fps: 7.05 x 900 = 6345 px/s^2, so the scale is 9.8 / 6345 = 1.545e-3 m/px.

## Height (px)
- Frame 0 is the cleanest frame (dark wall): bbox rows 26–92 = 67 px (scene record). The half-max row profile in
  height.py gives 67–68 px over frames 0–2. I used 67 px.
- Height = 67 x 1.545e-3 = 0.1035 m.

## Checks
- At this scale the console table is 1021 px = 1.58 m long and the outdoor AC unit is 505 px = 0.78 m wide. Both are
  realistic sizes. If the file's 24 fps were used instead, they would come out at 2.5 m and 1.2 m, which are
  implausible, so the 30 fps time base agrees with the scene.
- A plant about 10 cm tall in a pot about 7 cm wide (47 px) is plausible.
- The uncertainty from the acceleration fit (±1.5%) and the pixel height (±1 px) is about ±3%.

Answer: 0.104 m.
