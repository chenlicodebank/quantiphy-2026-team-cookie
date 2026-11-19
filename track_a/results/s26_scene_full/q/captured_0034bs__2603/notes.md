# q 2603 – total distance traveled by the left tennis ball (cm)

The file and the question both run at 24 fps, so the frame number is t x 24.

## Method (lab method card)
- Track: scene/tracks/tennis_ball_left.csv. I checked it with overlay.py (frames/overlay.png) on frames 24–48,
  including the occluded frames 33–48 behind the soccer ball. The 16 px-radius circles sit on the visible caps.
  My own re-track with an upper-arc fit (measure.py, retrack.json) was noisy near the collision, because the
  hue mask picked up the right ball and lost most of the ball when only a thin cap showed. I did not use it.
- Back-projection: f = 0.5959 x 1280 = 763 px, principal point (640, 360), Z = 0.706 m (the depth_info value
  for the left ball at t = 1.2 s), giving 0.926 mm/px. Path length = sum of the frame-to-frame 3D displacements.
- Motion: at rest for frames 0–23. The ball rolls right over frames 24–38, collides at frame 38, and then rolls
  slowly back left and up until frame 48.

## Results
- Raw record path, frames 24–48: 16.88 cm (frames 0–48 including the rest jitter: 17.50 cm).
- Split check: forward 24→38 = 14.76 cm, plus the backward part 38→48 = 1.88 cm after 5-frame smoothing
  (2.00 cm net), total 16.63 cm.
- Answer: 16.8 cm.

## Caveat
The apparent sizes (tennis ball about 32 px, soccer ball about 105 px) point to a real depth of about 1.6 m.
That is not consistent with 0.706 m, and the left ball also passes *behind* the soccer ball (0.894 m). I still
follow the stated convention, which back-projects with the given depth. Scaling instead by the prior
(6.7 cm / 32 px) would give about 38 cm.
Confidence: moderate. The geometry under the depth convention is solid (±3%); the main uncertainty is which
scale the reference used.
