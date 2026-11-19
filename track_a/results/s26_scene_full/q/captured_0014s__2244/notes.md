# q_2244 — cookie diameter (cm)

Lab video, 1280x720, 24 fps (file fps = question_fps). f = 0.5959 x 1280 = 762.75 px, c = (640,360).
Cookie: chocolate-chip cookie standing upright against the front of the cup, its round face toward the camera
(appears as a near-circle, so the horizontal extent is the full diameter). Static all clip. Its centre is about (486,390).

## Pixel diameter (measure_cookie2.py / measure_cookie3.py; mean of frames 36-48, when the ball is out of frame)
- Horizontal profile (rows 386-396): the left edge against the white cup is at x ≈ 468.8 (half-way brightness step).
  The right edge, at the dark gap before the board, is at x ≈ 503. Width ≈ 34.2 px.
- Vertical profile (cols 481-491): the top is at y ≈ 373.7 (chroma step against the cup) and the bottom at
  y ≈ 406.5 (contact shadow). Height ≈ 33 px, so the face is slightly foreshortened by the downward view.
- 10x zoom read by eye: x 469.5-504, y 373.5-408, so about 34.5 x 34.5 px.
- I used a diameter of 34.2-34.5 px.
- scene.json gave "~34 x 36" (bbox 469-503 x 373-409), which is consistent.

## Scale
- Method card: D = 1.7355 m x 34.3 / 762.75 = 7.80 cm.
- Fronto-parallel pinhole using z rather than the ray distance: z = 1.7355 / sqrt(1 + (154/763)^2 + (30/763)^2)
  = 1.700 m, which gives D = 7.64 cm.
- Answer: 7.75 cm (between the two, leaning toward the method card).

## Sanity check
- The cup's 40 px width at 1.727 m gives 9.1 cm, a plausible tumbler.
- The ball's 28 px at 1.818 m gives 6.7 cm.
- So a cookie of about 7.8 cm is plausible.

Confidence: about ±4%.
