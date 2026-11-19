# Q2786 — yoga ball diameter (cm)

- Lab video, 24 fps (file and question fps are the same). t = 1.0 s is frame 24. Depth to the yoga ball = 2.612 m.
- f = 0.5959 x 1280 = 762.8 px (lab method card).
- Apparent diameter at frame 24: the circle fit in scene/tracks/exercise_ball.csv gives 147.0 px. I checked it on a zoomed
  crop (frames/f24b.png) and with a row-wise gradient edge search (measure.py). The row medians are 142-150 px in frames
  22-26 and agree with the track (138 -> 158 px, smooth growth).
- Size = 2.612 x 147.0 / 762.8 = 0.503 m = 50.3 cm. Using exact sphere angular geometry with the off-axis position gives
  48.4 cm instead (-4%). I answer with the method-card convention.
- Second route (velcheck.py), which checks the depth convention against the prior: I back-projected the track with depth
  ∝ 1/diameter_px, scaled to 2.612 m at frame 24. The speed at 1.0 s comes out at 2.14-2.16 m/s, against the prior's 2.19
  m/s (~1.5% off). If 2.612 m were the distance to the front surface (centre ≈ 2.87 m), the speed would be 2.35 m/s (+7%).
  So 2.612 m is the centre distance, consistent with the 50 cm answer. Scaling slightly so the speed matches the prior
  exactly would give ~51 cm.
- Answer: 50.3 cm. Confidence: moderate-good (±4%, from motion blur on the rim and the off-axis stretch).
