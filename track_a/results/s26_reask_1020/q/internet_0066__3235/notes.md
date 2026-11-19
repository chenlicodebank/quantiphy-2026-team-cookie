# Q3235: displacement of the ball between 1.70 s and 1.80 s

- Time base: question_fps = 30, which matches the file. 1.70 s is frame 51 and 1.80 s is frame 54.
- Scene: a top-down hand-held view of a gym floor. A basketball rolls right to left at about 90 px/frame. Its shadow stays attached and no bounce or fall is visible.
- The prior (g = 9.8 m/s^2) describes motion the clip never shows. There is no vertical free fall, and the measured pixel acceleration is about 0, so the prior gives no usable scale.
- Scale: taken instead from a regulation size-7 basketball, diameter 0.239 m. Its pixel diameter is 256 px (the blur-free vertical extent, median over frames 53–69, range 250–261). That gives 9.34e-4 m/px.
- Positions: the camera-stabilised centres from scene/tracks/ball.csv. I checked them on crops of frames 51 and 54:
  - Frame 51 is cut by the right edge (centre = visible left edge + 128). Its left edge sits at about x = 1714, so cx ≈ 1842.
  - In frame 54 the ball spans about x 1448–1700, so cx ≈ 1575.
- Displacement in pixels:
  - Direct, frame 51 to 54: 267.0 px.
  - Quadratic fit over frames 50–70: 271.8 px.
  - Constant-velocity fit: 3 × 89.9 = 269.8 px.
  - I used about 270 px.
- Answer: 270 × 0.239 / 256 ≈ **0.252 m**. The direct value gives 0.249 m; with a size-6 ball (0.232 m) it would be 0.242–0.246 m.
- Sanity check: the rolling speed comes out at 2.5 m/s, which is plausible.
- Confidence: moderate. The main uncertainty is the ball size (size 7 vs 6, about 3%) and the blur on the edge-cut frame 51.
