# Q96 — length of the black-and-white car (m)

2D top-down render, static camera, 24 fps (file and question agree). Prior: yellow car length = 5.67 m.

Method: one metres-per-pixel scale from the yellow car's pixel length along its motion (x extent).
- Record tracks (scene/tracks, read by measure.py): yellow length 270 px in all frames near the image centre
  (grows to 272-276 only at the left edge from perspective); black car 268-271 px near the centre
  (frames 4-48, x 826-1442), growing to 273-280 at the right edge.
- Visual check, frame 20 (frames/f20.png, gridded crop): yellow spans x ~537-807 (270 px), black ~915-1184 (269 px).
- Scale = 5.67 / 270 = 0.0210 m/px → black car = 269 x 0.0210 = 5.65 m.

Second route: comparing the cars at similar distances from the image centre (yellow frame 0 at x 862: 270 px;
black frames 16-24 at x 993-1105: 268-269 px) gives a ratio of 0.993-0.996 → 5.63-5.65 m.
My own background-difference test in measure.py did not give clean extents (moving-car ghosts in the median of 3
frames), so I discarded it and used the record's masks plus the visual check.

Answer: 5.65 m. Confidence high (±1%).
