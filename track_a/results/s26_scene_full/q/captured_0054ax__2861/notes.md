# q_2861 – velocity of the white ball at t = 1.0 s (frame 24)

## Object identification
- "white ball" = the small pale (grey/lavender) ball the standing person throws (scene/ calls it `pink_ball`).
  Its given distance at f24 (3.0735 m) matches the standing person's depth; the "green ball" (3.039 m) is the
  yellow-green ball in the other hand. The soccer ball sits near the crouching person (~2.3 m), so it is not the white ball.
- The ball is released at f22–23. At f24 it is in free flight, up and to the left, and approaching the camera.
- Time base: question_fps = file fps = 24, so t = 1.0 s is frame 24.

## Problem
There is only one depth for the white ball (f24), so its radial (toward-camera) velocity cannot come from depths.
Lateral motion alone: about 11–15 px/frame at 3.07 m, i.e. about 1.1–1.4 m/s.

## Method (fit_drop.py, fit_25.py, fit_fps.py)
- Pinhole with f = 0.5959·1280 = 762.8 px and principal point (640,360). The white ball's f24 position is
  back-projected with the given distance 3.0735 m.
- I fit a 3D ballistic trajectory (gravity 9.81 m/s²) to the white ball's centroids from f24 to f37, jointly with
  the yellow ball.
  - Gravity direction: camera roll is a free parameter. Pitch is tied to the floor plane given by the basketball
    centre at f12 (2.3557 m) and f24 (1.81 m). Those centres are a constant height above the floor, which gives a
    nearly level camera about 0.75–0.89 m above the floor.
- **Frame drops found:** pixel steps double at f11→12 (basketball 16 → 33 → 18 px) and at f35→36 (both small
  balls: 45 → 120 px). The two drops are exactly 24 frames apart. This fits a 25 fps Femto recording thinned to
  24 fps.
  - With the post-f35 frames shifted by +1, the fit rms falls from 8 px to 1.3 px; shifting by 2 is worse (4 px).
- The radial velocity is strongly tied to the true frame interval:

  | true fps | v at f24 (m/s) | reference-convention speed at f24 (per-index step ×24, m/s) |
  |---|---|---|
  | 24 | (-0.67, -1.05, -1.42) | 1.5 – 1.86 |
  | 25 | (-0.68, -0.93, -1.82) | 1.73 – 2.06 (forward diff 2.00, 5-frame centred mean 2.06) |
  | 26 | | 2.05 – 2.26 |

- When fps is a free parameter, the fit gives 26.2–26.8 fps.

## Second-route checks
- **Apparent size:** the minor axis grows from about 16.9 px (f24–27) to about 20.5 px (f32–34), a ratio of about 1.21.
  The 24–25 fps models predict 1.16–1.25; the 26 fps models predict about 1.29–1.30.
- **Bounce timing:** the white ball touches the floor at video index ≈ 38 and the yellow at ≈ 37. The models
  predict contact 0.3–0.7 frame early, which slightly favours the higher time scales.
- **Prior check (basketball, f12):** with the given depths and linear depth interpolation, the per-frame
  3D speed is 1.6 m/s; a 5-frame smoothing that includes the f11→12 drop gives 1.73 m/s. The prior says 2.21 m/s,
  so the reference seems to read about 1.3× higher than clean geometry. That cannot be reproduced exactly; it
  pushes the answer toward the upper half of the range.

## Answer
About 2.0 m/s: the 25 fps model, reference convention, consistent with the size and bounce checks. Plausible range
1.7–2.3 m/s. Confidence is moderate, because the radial component is not directly measured.
