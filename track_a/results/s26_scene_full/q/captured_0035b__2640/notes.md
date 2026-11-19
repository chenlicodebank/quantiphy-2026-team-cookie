# q_2640: basketball velocity at t = 0.9 s (cm/s)

- Time: t = 0.9 s at question_fps 24 -> frame round(21.6) = 22. File fps is also 24.
- Track: the basketball centres from scene/tracks/basketball.csv (circle fits, about ±1.5 px). Checked visually at frame 22 (frames/f22.png): the centre is at about (666, 400), and the track gives (667.1, 398.5).
- Camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).
- Depth: 2.7777 m at 0.9 s for the basketball. The two entries at 1.4 s are both labelled "soccer_ball". The pixel sizes decide which is which. The soccer ball's diameter goes from 52.5 px to 54.8 px (frames 22 to 34), so its range ratio is about 0.96, which matches 2.373/2.477. The basketball's goes from 60.9 px to 67.0 px, which matches 2.602/2.7777 = 0.94; the other reading would give a ratio of 0.85 (or 1.05 for the soccer ball). So the basketball is at 2.602 m at 1.4 s.
- Check of the depths: f x 0.232 / 2.7777 = 63.7 px expected against 60.9 measured, and 68.0 expected at frame 34 against 67.0 measured. Both are consistent to within about 4 %.
- Method: each centre is back-projected with a range that is linear in time between the given depths (range converted to Z along the ray). The velocity is a linear fit of the 3D position over frames 19-25 / 20-24. It does not cross the dropped frame at 35/36, and the contact with the soccer ball starts at frame 24 without changing the basketball's path.
  - Model A (given depths): vel = (-101.5, 63.3, -34.7) cm/s, speed **124.5 cm/s** (frames 19-25) and 128.0 (frames 20-24). The mean of the forward differences over frames 20-24 is 124.7.
- Second routes:
  - Model B, depth from inverse pixel diameter: 120-122 cm/s.
  - Model C, constant depth: 120-123 cm/s.
- Answer: 125 cm/s. Confidence: good, about ±5 %.
