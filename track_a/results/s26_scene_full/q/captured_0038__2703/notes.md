# Q2703: displacement of the white ball between 0.9 s and 1.4 s (cm)

Lab video. The file and the question are both 24 fps. t = 0.9 s is frame 22 and t = 1.4 s is frame 34. Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).

## Positions
- Ball centres come from scene/tracks/ball.csv (cx_best, cy_best). I checked them on zoomed crops (frames/c22.png, c34.png) and they sit on the ball.
  - Frame 22: (527.6, 497.7)
  - Frame 34: (725.0, 505.9)
- Frame 34 depth is given as 0.716 m, so P34 = (0.0779, 0.1337, 0.6991) m.
- Scale check: the credit card (the dark card with the yellow label) is about 98 px long at 0.6867 m, which gives 8.82 cm against the true 8.56 cm (+3 %). The ball's 38 px vertical size gives a diameter of 3.6 cm, which is plausible.

## Depth at frame 22 (not given)
- **Route A, ball centre on a plane parallel to the table** (disp.py): I intersected the frame-22 ray with the plane through P34.
  - Level camera: depth 0.761 m, displacement 19.16 cm.
  - Camera pitched down 4–6°: 18.7–18.8 cm. This pitch is suggested by the card's foreshortening (about 18 px tall for 54 mm, which means about 17° elevation against the level ray's 13°). It also brings the ball radius implied by the card and ball heights closer to the measured 1.8 cm.
  - ±1° of roll moves the result by about ±0.5 cm.
- **Route B, the ball's apparent size** (size.py): its width (which includes the same motion blur at a near-constant speed) grows from about 41.8 px at x≈528 to about 43.4 px at x≈725. After removing about 4 px of blur, the ratio is about 1.04, so depth0 ≈ 0.745 m and the displacement is 18.7 cm. The top-to-shadow distance gives a ratio of 1.026, so 0.735 m and 18.4 cm.
- If both frames were at the same depth, the displacement would be 18.08 cm (lower bound).

## Answer
18.7 cm (spread of the routes: 18.4–19.2). Confidence is moderate: the main uncertainty is the depth at frame 22 (±2 %), which moves the answer by about ±0.5 cm. Frames 22–34 do not include the probable dropped frame (between frames 35 and 36), and the displacement is the straight-line distance, so it is unaffected.
