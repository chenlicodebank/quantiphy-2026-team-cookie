# Q2043: average speed of the black car (m/s); prior: lane width = 3.66 m

- **Object.** The only dark car is the one the scene record calls `blue_car` (very dark metallic blue). It drives up the left lane
  and is visible in frames 0–133. The white car is the other one.
- **Scale (lane.py).** Asphalt edges come from a saturation half-level crossing, and the dashed centre line from a
  brightness peak. I measured 35 row bands × 3 frames (15, 200, 280). Road width is 82 px (median); centre minus left
  edge is 41.6 px and right edge minus centre is 40.2 px. Lane width = **40.9 px**, so the scale is 3.66 / 40.9 = 0.0895 m/px.
  (The scene record's "71 px road" was too narrow.)
  Sanity check: at this scale the car would be 74 px × 0.0895 = 6.6 m long. The real lane is clearly narrower than 3.66 m,
  but the benchmark uses one scale taken from the prior, so I follow that. If someone instead took the whole road
  (82 px) as "lane width", the answer would be about 15.9 m/s.
- **Pixel speed.** The scene track (speed.py) gives 11.86 px/frame raw and 11.81 stabilised (mean per-frame speed,
  frames 0–127; the camera is almost static). As an independent check (check.py), I detected the blue-body blob myself on
  frames 0–125: 11.86–11.90 px/frame (about 11.4 early, then about 12.0). I used **11.85 px/frame**.
- **Time base.** The file is 29.94 fps and the question says 30. The difference is 0.2 %, so I used 30.
  11.85 × 30 = 355.5 px/s.
- **Answer.** 355.5 × 0.0895 = **31.8 m/s**.
- **Confidence.** The pixel speed is good to about 1 %, and the lane pixel width (38–42 px, depending on where the edge
  is taken) to about 4 %. The main risk is how the annotators read "lane".
