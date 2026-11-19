# q76 – speed of the walking person at 1.0 s (m/s)

Prior: bike length = 1.7 m. No depth_info. question_fps = file fps = 24, so t = 1.0 s is frame 24, and the speed is the
backward difference between frames 23 and 24.

## Measurements (scripts: measure.py, feet.py, answer.py)
- Bike tip-to-tip length (cyan columns, measure.py): 415-417 px at x≈1570-1670, 413 at x≈1520, 407-409 on the left side.
  SAM3 "bicycle": box width 414.2 px (f6), 411.1 px (f20), compared with mine at 415 / 409: they agree within 1%.
  Local length near the walker's ground position (x≈1520): **413 px**, so 1.7/413 m/px in the bike plane.
- Walker pixel displacement 23→24 (upper body, pelvis proxy):
  head blob centroid 14.28, darkness-weighted head 14.27, head+shoulder template match 14.06, SAM3 "white t-shirt"
  centroid 14.0 (1579.3→1565.3). SAM3 clean head mask (f24, k2) centroid 1574.0 vs mine 1574.4. Mean **14.15 px/frame**.
  The scene record's head_x gives 14.2, which agrees with mine.
  The SAM3 whole-body ("walking person") centroid moves only 11.5 px. That mask includes the swinging leg and arm, so its
  centroid does not follow the pelvis, and I did not use it. The SAM3 "hair" mask at f23 also picked up part of an arm
  (it is 98 px wide; I checked the overlay), so I rejected it too.
- The head speed swings between 12.4 and 16.9 px/frame over the 17-frame step cycle. Frame 24 sits near the mean
  (14.5 px/frame over frames 3-40), so a phase error between the head and the pelvis matters little here.

## Perspective (top-down camera, objects at different heights)
Head and feet show clear parallax. At the same gait phase one cycle apart (frames 9/43, 26/60, 17/51), the head-to-shoe
offset shrinks as the walker approaches the image centre. The slope (h_head−h_shoe)/(H−h_shoe) ≈ 0.086 (individual
values 0.075-0.096), so with a head of ≈1.68 m the camera height is H ≈ 18.7 m. As a check, the head-vs-shirt parallax
slope of 0.019 implies a head-to-shoulder height difference of ≈0.33 m, which is plausible.
Head-plane metres per pixel = bike-plane value × (H−1.68)/(H−0.45) = 0.932. This factor is not sensitive to the
assumed heights: it stays between 0.926 and 0.942 across the range of slopes.

## Result
- Single scale (bike plane): 14.15 × 24 × 1.7/413 = 1.398 m/s.
- With the perspective correction to the head/torso plane: **1.30 m/s**. This is the answer, since the reference is the
  pelvis world speed.
- Second route: the SAM3 shirt centroid alone gives 14.0 px → 1.29 m/s, and the template match gives 1.30 m/s.

Confidence: moderate-high, about ±5%. The main uncertainties are how closely the head/torso proxy follows the
pelvis within the step cycle, and the perspective correction (±1%).
