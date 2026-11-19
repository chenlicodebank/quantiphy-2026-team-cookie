# q 2081 – basketball velocity at t = 0 s

- 2D internet clip (near top-down drone view, camera drift <1 px over frames 0-4). The fps values 30 and 29.9 differ by 0.3%, which doesn't matter here; I used 30.
- Scale: prior "inner court width" = lane (key) width = 4.88 m (16 ft). The bottom lane width between line centres, measured in code on frame 0 at rows 2950-3680 (look.py), is 633-641.5 px, so I used 640 px (outer edges ≈ 650 px, inner ≈ 628 px).
  Scale = 4.88/640 = 0.007625 m/px.
- Ball: scene/tracks/ball.csv (NCC, bgref). I checked frames 0 and 1 visually (frames/b0.png, b1.png): ball centre ≈ (1100,3537) → (1103,3531), which agrees with the track.
- Image speed per frame: 7.74, 7.47, 7.41, 8.54 ... px.
  Forward difference frame 0→1: 7.74 px/frame × 30 = 232 px/s → **1.77 m/s**.
- Second route: a quadratic fit over frames 0-3, 0-5 and 0-7 gives v(0) = 1.78, 1.69 and 1.65 m/s; linear means give 1.72-1.83 m/s.
- Answer: 1.75 m/s, between the forward difference and the smoothed values. Uncertainty ±5% (from the lane-width line convention and the ball centre at frame 0, which overlaps the rim).
