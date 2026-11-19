# Q1226 – height of the person (simulation_0055)

The file and the question both run at 30 fps, so frame = t × 30. The video is a 3D Blender render with a static, level camera. I assumed the principal point is at the image centre (540, 540).

## Answer: 1.79 m (the man's head-top-to-sole height, taken at its maximum while walking ≈ rest standing height)

## Pixel height (`height.py`, `feetview.py`)
- Head top: the first row where the frame differs from bg.png inside the head columns. It is 572–573 at the highest
  point of the gait (mid-stance) and 573–579 over the walk cycle.
- Sole of the planted shoe is at y ≈ 947. I checked this by eye on 4× crops of frames 20 and 45. The record's
  feet_y values of 941 and 953 are noisy, partly from shadows and the cracks between paving slabs.
- Height: 375 px at its maximum (947 − 573 + 1), about 372 px median over the walk. Rest height is the maximum, 375 px.

## Focal length (three routes)
- The man is at constant depth: his planted-foot row and head width stay constant.
  Z_man = d / sqrt(1 + r²/f²), where r is the pelvis offset from the image centre.
- **Route A, man's two distances** (8.313 m at t=0, 8.189 m at t=1). Over one gait cycle he moves 89–90 px, from
  pelvis x ≈ 1068–1071 to 979–981 (y ≈ 748). Solving for f gives **≈ 1615 px**, with a spread of about ±5%.
- **Car track correction.** The record's edge-based car centre is biased. The rear and front silhouette edges drift
  by up to 20 px against the wheels, apparently from perspective on the bumpers, and this made the deceleration look
  non-constant. I re-tracked the car by its wheel centres (`wheels.py`, `wheels2.py`): the dark tyre extent in rows
  780–860, with the midpoint averaged over 4 thresholds. The wheelbase stays constant at 480.2 px. The rear wheel
  covers frames 46–75 and the front wheel frames 39–51. Their combined centre track fits a constant deceleration of
  **≈ 450 px/s²** with an rms of 0.5 px; frame windows give 432–472.
- **Route C, prior acceleration plus the car's t=1 distance**: sqrt(f² + r30²) = 11.671 × a_px / 2.86. This gives
  **f ≈ 1655–1700**.
- **Route B, car distances at t=0 and t=1** (16.059 and 11.671 m), with frame 0 extrapolated from the
  constant-acceleration fit: **f ≈ 1633–1651**.
- B and C give the same f (≈ 1613) when a_px = 430, which also matches route A. The best fit, a_px = 450, gives
  B 1651 and C 1698.
- **Adopted f ≈ 1650 px.** That puts Z_man at 7.855 m, the same from both of the man's distances, and Z_car at
  ≈ 10.75 m; the latter reproduces d(t=0) = 16.05 m.

## Result
H = 375 px × 7.855 / 1650 = **1.785 m ≈ 1.79 m**. Other readings:
- Median walking height (372 px): 1.77 m.
- Range over f = 1615–1700: 1.74–1.82 m.

## Checks
- Car height comes out at 219 px × ~10.3 m / 1650 ≈ 1.37 m and car length at ~4.6 m. These fit a sports sedan
  (the car looks like a Kia Stinger: 1.40 m × 4.83 m).
- A man of 1.79 m is plausible.

## Confidence
Moderate. The answer is about ±4%, driven mostly by the uncertainty in f. The lamp-post and hydrant distances were
not used: their origins are unknown, and a flat-ground model with the horizon at row 540 did not reproduce them well.
