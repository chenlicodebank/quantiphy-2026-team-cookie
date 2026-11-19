# q2728 — white ball velocity at t=1.0 s (cm/s)

t=1.0 s → frame 24 (question_fps 24 = file fps). Lab camera f = 0.5959·1280 = 762.8 px, principal point (640,360).
Ball track: scene/tracks/ball.csv (circle-fit centres and diameters, frames 19-40, ±0.5 px), checked for consistency.

## Key facts
- Motion is almost purely toward the camera. The image offset from the principal point r_img and the ball diameter D scale
  together (r/D ≈ 5.2 constant), so lateral X,Y ≈ constant and depth ∝ 1/r_img ∝ 1/D.
- 1/r_img clearly curves in time (quadratic rms 0.053 vs linear 0.127), which means the ball slows down as it rolls.
- Relative approach rate at frame 24, -(dZ/dt)/Z: 0.75-0.78 /s from the 1/r_img quadratic fits, 0.73 from a local ±3-frame slope,
  and 0.69-0.70 from the noisier 1/D fits.
- Anchor: distance 1.014 m at frame 24. The models predict z(35)/z(24) ≈ 0.71-0.73, which matches the given 0.737/1.014 = 0.727.
  The given t=1.5 depth lines up best with frame 35, which fits the dropped frame between 35 and 36.

## Result
Full 3D back-projection with depth ∝ 1/r_img (quadratic), anchored at 1.014 m:
- forward difference at frame 24: 78.0 cm/s
- mean forward difference over frames 22-26: 78.1 cm/s
- linear fit over ±2-3 frames: 79.9 cm/s

Second route (depth ∝ 1/D, quadratic): 70.6-71.8 cm/s.
Simple linear-in-time depth between the two given depths: 57 cm/s. This is rejected because the image data show deceleration.

Answer: **77 cm/s**. Confidence is moderate (±10%). It depends on the depth-time model.
Scripts: vel.py, vel2.py, curv.py.
