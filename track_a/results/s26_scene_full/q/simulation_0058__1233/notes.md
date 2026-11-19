# q_1233 – speed of the yellow car (taxi) at t = 2.5 s  → **4.1 m/s**

The file and the question both run at 24 fps, so t = 2.5 s is frame 60. The answer is the backward difference between frames 59 and 60.
The camera is static. The principal point is assumed at (1080, 540) and the horizon at row 422.5 (main-road vanishing point), which gives a pitch of about 3.0°.

## Focal length (calib.py, geom.py)
- Van (white car), prior a = 4 m/s². I back-projected its centre at frames 14 and 38 using the given ranges (31.07 m and 29.92 m), which defines its 3D line of motion.
  For every frame I took the van's rear-edge pixel track, found the closest point on that line, fitted s(t) with a quadratic and solved for 2·c2 = 4.
  This gives f = 2237 px (box-width centre) or 2183 px (constant-length centre), with sub-windows giving 2130–2230. The fit residual rms is 0.02 m.
- Independent check: if the cross street is orthogonal to the main road, its far-curb slope of 0.007 implies f ≈ 2100. I used f = 2210.

## Camera height (height.py)
- I back-projected the origin with its given range and dropped it vertically onto the ground-contact ray. This gives a camera height H of:
  - cyclist (tyre contact directly under the origin): 2.81 m at frame 14 and 2.79 m at frame 38;
  - pedestrian (feet): 2.83 m.
- The van and taxi give 2.9–3.1 m, but that is expected: their contact rows are the near-side or front wheels, which are closer to the camera than the origin.
- I used H = 2.80 m (cyclist mean at f = 2210). For each f, H is re-derived from the cyclist. Because H·f stays nearly constant, the speed is almost independent of f: 4.0841 m/s at f = 2130 and 4.0840 m/s at f = 2290.

## Taxi speed
Route A (speedA.py, checks.py):
- Method: I intersected the tyre-contact point (record's `ground_y` and `bottom_center_x`) with the ground plane in frames 46–71. The car is on a straight path along the main road there: the heading is −4.2° in camera X, against −4.5° for the road direction from the vanishing point. The depth rate is constant, so the speed is constant.
- Fitting quadratics in X and Z and taking the frame 59→60 difference gives 4.09 m/s (frames 46–71), 4.12 (50–71), 4.14 (44–66) and 4.14 (52–68).
- The raw per-frame speeds near frame 60 are 4.3, 4.2 and 4.0 m/s.

Route C (scaleB.py) – check on a second rigid point: I template-tracked the front face (plate, grille, headlights) from frame 60.
- The plate's image row expands by (v − vh) ratio 1.3085 between frames 46 and 71. That is what Route A's contact depths predict for a point about 0.9 m ahead of the front-tyre contact (1.310), so the depth rate is confirmed.
- The template's *scale* ratio (1.330, which would give 4.4–4.5 m/s) is biased: the template's own image rows contradict it, and so does the ground row. The likely cause is the changing oblique view (the right side of the car grows visible from perspective as the car comes closer, off-axis). I rejected the scale estimate for that reason.

Sanity check: the chord between the taxi origins at frames 14 and 38 (from the given ranges) is 4.0 m in 1 s, while the car turns. That is consistent with a cruising speed of about 4.1–4.3 m/s.

## Confidence
Moderate to good, about ±5%. The main uncertainty is H (±1%, set by the cyclist and pedestrian origin assumptions), plus the bbox-based ground point and integer `ground_y`.
Rejected readings: bbox height (4.4–4.6) mixes the depths of the roof sign and the front contact, and bbox width (8+) grows because the side of the car comes into view.
