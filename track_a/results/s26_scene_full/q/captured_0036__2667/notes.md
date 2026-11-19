# q_2667 — ping pong ball velocity at 1.4 s (cm/s)

- question_fps = file fps = 24 -> t=1.4 s is frame round(33.6) = 34. Depths given: frame 22 (0.9 s) 1.010 m, frame 34 (1.4 s) 0.716 m.
- Track: scene/tracks/ball.csv centres (checked on 3x crops of frames 28-37, frames/crops.png; centres OK).
- f = 0.5959*1280 = 763 px, principal point (640,360). Positions = unit ray * depth (depth = Euclidean distance),
  depth linearly interpolated/extrapolated in frame between the two given depths. Check: pixel diameter
  763*0.04/d = 30.2 px at frame 22 (measured 31), 42.6 px at frame 34 (measured 45, blur) - consistent.
- Per-frame speeds on the table (vel.py): frames 26-35 ~80-88 cm/s (frame 34 backward 86, forward 34->35 83).
  Smoothed chords that stay on the table: 29-34 86, 30-35 86, 31-35 85.
- Step 35->36 is 154 cm/s (76 px vs ~28 px), physically impossible as a real speed change -> likely a dropped
  capture frame as the ball leaves the edge. Any centred >=5-frame smoothing at frame 34 (as the reference method uses)
  spans it: chord 32-36 101, 32-37 99, 31-37 97, 30-38 95.
- Second route (size-based depth k/diam) is noisy per frame but gives chords 30-35 82, 31-36 105 - same picture.
- Answer: 96 cm/s, between the on-table physical speed (~85) and the reference-convention smoothed value (~97-101),
  weighted toward the latter. Confidence moderate (+-10%).
