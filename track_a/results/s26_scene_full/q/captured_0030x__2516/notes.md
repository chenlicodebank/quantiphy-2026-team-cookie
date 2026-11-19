# q_2516 – speed of the red ball at t = 0.2 s (cm/s)

t = 0.2 s → frame round(0.2·24) = 5 (file fps = question fps = 24). Lab clip, f = 0.5959·1280 = 762.8 px, c = (640, 360).

## Data
- Ball centres: scene/tracks/ball.csv (upper-arc circle fit; bbox centre for blurred frames 0-2). I checked frame 5
  zoomed: ball spans about x 424-490, y 445-505, centre ≈ (457, 476), and the record has (457.5, 478.1). OK.
  My own colour mask (remeasure.py) picks up the orange glow, not the dark ball, from frame 5 on, so I kept the record.
- depth_info: frames 5, 10, 14, 19 → 0.8715, 1.166, 1.372, 1.315 m.

## Method (plane.py, speed.py, hybrid.py)
The four given-depth back-projected points lie on one plane: residuals are ≤ 4 mm, the normal is almost the camera's y
axis (~1° pitch), and the plane is 13.9 cm below the camera. The ball moves on the tabletop, so for every frame I
intersected its centre ray with this plane to get its 3D position, which gives depth for frames that have no depth_info.
- Route A (pure plane): speed at frame 5 = 166-202 cm/s depending on the smoothing (quadratic fit over 5/7 frames:
  189/177; mean forward speed over frames 3-7: 188; 5-frame moving average then forward difference: 183).
- Route A' (plane distances rescaled to match the given depths exactly, scale interpolated between frames 5 and 10):
  quadratic fit over 5/7 frames: 175/162; mean forward speed over frames 3-7: 172-177; central difference (X7−X3)/4: 174-180.
  The camera-frame velocity at frame 5 is about (−116, −3, +140) cm/s, mostly away from the camera. The given depths alone
  give an average radial rate of 141 cm/s over frames 5-10.
- Route B (depth from apparent size, corrected for diameter inflation): noisy, 148-222 cm/s. Used only as a sanity check.
- Second check (loop.py): a circle fit to the in-plane path gives radius 0.30 m and period 26.2 frames, so a uniform
  speed of 174 cm/s. The smoothed per-frame speed around frame 5 is 172-183 cm/s.

## Answer
175 cm/s. Confidence: moderate, about ±10 %. The main uncertainty is how the depth varies between the given times
and how the reference was smoothed.
