# Q23 — walking speed of the person at t = 2.0 s (frame 60)

Prior: orange car acceleration = -2.86 m/s^2. Top-down camera, 30 fps (file fps = question_fps, so no re-timing). The camera is static.

## Scale (from the prior)
- I fitted a quadratic to the orange car's template-matched y track (scene/tracks/orange_car.csv, reliable frames; re-checked in `fit.py`):
  a = -311.0 (f15–90), -313.0 (f20+), -313.5 (f30+), -309.7 (f50+) px/s^2, with residuals of 0.15–0.4 px. I took 311.5 px/s^2.
- That gives a road-plane scale of 2.86 / 311.5 = 0.00918 m/px. Sanity check: the car comes out 556 px = 5.1 m long and 2.25 m wide.

## Person pixel speed near f60
- The scene record's jacket centroid is unreliable around f60: the head and shoulders are still at or past the bottom edge, and the shoes merge into the mask.
- `person_track.py`: my own navy-jacket mask with the lamp pole excluded. Linear and quadratic fits of the centroid over f55–75 and f52–90 give 1.80–1.92 px/frame.
- `tm_track.py` / `tm_fit.py`: sub-pixel template matching of the torso (templates taken from f70, f75 and f80).
  - The f75 and f80 templates give 1.63–1.81 px/frame at f60 (linear fits over f54–66 and quadratic/cubic fits over f54–90).
  - The f70 template matches poorly before f62 (score < 0.7, arm-swing phase) and gives 1.28. I treated it as an outlier.
  - The average over one stride (f54→80, 26 frames) is 1.67–1.70 px/frame.
- Adopted value: 1.72 px/frame = 51.6 px/s.
- The feet slide backward while planted (foot sliding in the animation), so stride length cannot be used. The speed comes from translation of the torso/root only.
- The speed rises later (about 2.4 px/frame over f80–90). This looks like gait oscillation or an ease-in, so I used the speed local to f60.

## Perspective correction (torso is above the road plane)
- From the lean of the person (head vs. feet radial distance from the image centre, about 1180 vs. 1074 px), D/(D-H) ≈ 1.10, so H/D ≈ 0.09.
- With the torso tracking point at about 0.72 H and the car origin at about 0.3 m: speed factor (D - h_torso)/(D - h_car) ≈ 0.95. The plausible range is 0.935–0.965.

## Result
v = 51.6 px/s × 0.00918 m/px × 0.949 ≈ 0.45 m/s.
Without the height correction it would be 0.47 m/s.

## Checks and confidence
- Three independent tracks (jacket centroid, two torso templates) and a stride-averaged estimate agree to within about ±6 % (1.63–1.92 px/frame).
- Moderate confidence. The main uncertainties:
  - per-frame gait oscillation of the pelvis, which the reference's one-frame difference would include;
  - the height correction, ±3 %.
