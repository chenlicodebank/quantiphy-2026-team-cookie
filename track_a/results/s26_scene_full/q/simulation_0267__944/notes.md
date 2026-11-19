# Q944 – speed of the spacecraft at 1.0 s (prior: acceleration at 1.0 s = 4 m/s^2)

fps = question_fps = 24, so no re-timing. 2D scene with a static camera. The "spacecraft" is the single flying car in scene/.

## Method (fit.py)
- Fitted a quadratic x(frame) to several independent tracks from scene/tracks/flying_car_final.csv: nose tip x0, tail tip x1,
  the nose/tail midpoint ref_x, and the whole-car template centre.
- Every track is described well by constant acceleration (rms 0.3-0.6 px, cubic term negligible). The parabola's vertex,
  where the velocity is zero, sits at frame 0.07-0.15 for every track. So the car starts from rest at t ≈ 0 and keeps
  accelerating uniformly.
- One m/px scale: speed / acceleration in pixel units has units of time, so the scale cancels.
  Speed(m/s) = 4 m/s^2 × (v_24 / a) / 24, where v_24 = x(24) − x(23) in px/frame (backward difference, per the convention)
  and a is in px/frame^2.

## Results
| track | a (px/f^2) | vertex frame | speed at 1.0 s (m/s) |
|---|---|---|---|
| nose 2-52 | -1.139 | 0.15 | 3.891 |
| nose 10-40 | -1.136 | 0.13 | 3.895 |
| tail 10-40 | -1.181 | 0.07 | 3.904 |
| ref midpoint 2-52 | -1.150 | -0.07 | 3.928 |
| template 2-60 | -1.188 | 0.15 | 3.892 |

The tail fit over 10-67 is excluded: the tail is clipped and blurred late in the clip (rms 8 px).

Second route: start the analytic motion exactly at rest at frame 0. The backward-difference speed at frame 24 is then
a × 23.5/24 = 3.917 m/s, which agrees with the fits.

Answer: 3.91 m/s. If the reference uses the instantaneous a·t instead, it would be 4.0 (2.3 % away). Confidence: high.
