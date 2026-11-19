# Q392 – length of the police car (van), prior: bike speed 5.52 m/s

fps = question_fps = 24, so no re-timing. Camera is static. Both objects move left to right, parallel to the image plane, so the 2D scale method applies.

- Cyclist pixel speed: I fitted a line to scene/tracks/cyclist.csv ref_x over f6–79 (fit.py). Result: 21.024 px/frame, residual std 0.43 px.
  Scale = 5.52 / 24 / 21.024 = 0.010940 m/px.
- Van side-view length: 438 px. I checked it on frame 66 with a grid crop (frames/f66.png): rear about x 752, front about x 1185, which gives about 433–438 px.
- Single-scale (2D convention) length: 438 × 0.010940 = **4.79 m**.
- Perspective check: the van's tyres touch the ground at y 743 and the cyclist's at y 738, with the horizon at about y 598. So the cyclist is
  about 145/140 = 3.6 % farther away, and the van's own m/px is about 3.5 % smaller, which gives 4.63 m.
- Answer: 4.71 m, between the two readings, so it is within about 2 % of either.
- Sanity checks: cyclist wheel 66 px gives 0.72 m (realistic). Van wheel 68 px gives about 0.72 m. A 4.6–4.8 m van is plausible.
- Second route: the van's pixel speed is 27.01 px/frame, which is 7.1 m/s at the single scale. That is consistent and plausible.

Confidence: moderate-high (±4 %).
