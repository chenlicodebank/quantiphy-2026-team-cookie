# q_2234: ball diameter (cm), captured_0014

The file runs at 24 fps and question_fps is also 24, so frame = round(t*24). t=0.6 is frame 14.

## Method (lab method card)
- f = 0.5959 * 1280 = 763 px, and the diameter = depth * pixel width / f.
- I used the horizontal pixel width because the ball rolls toward the camera, which shows up as image-vertical motion. That motion blur stretches the vertical extent but leaves the horizontal extent alone.
- widths.py takes half-maximum (mid-level between the ball and the white board) left/right edge crossings per row and keeps the widest chords (mean of the top 5 rows):
  frame 12: 27.1 px, 13: 27.2, 14: 27.0, 15: 26.2, 16: 26.8. The mean is 26.9 px, and I used ~26.8 px at frame 14.
- I checked this visually on a 10x crop of frame 14 (frames/z14.png). The ball spans x ≈ 535–561, which is about 26 px.
- At depth 1.7288 m (t=0.6): D = 1.7288 * 26.8 / 763 = 6.07 cm.

## Second route
- Frames 4–11: the ball is held or just released near the top of the board. The edges were read from row profiles
  (widths_top.py), where the SAM-edit dark rim marks the boundary. The width is about 25.5–27 px, roughly 26.5 px.
- At depth 1.818 m (the t=0 depth): 1.818 * 26.5 / 763 = 6.31 cm.
- The two routes differ by about 4%. The held-ball edge is less clean: the hand is close, the rim artefact may sit slightly outside
  the ball, and the background is blurred. So I weight the t=0.6 measurement more heavily.
- Note that the ball's pixel width barely changes between frame 4 and frame 16, although the depths imply a 5% change, which is about 1.3 px. That is within the
  measurement noise.

## Answer
6.1 cm (route range 6.07–6.31). Confidence: moderate-good, about ±5%.
The scene record's "about 26 px" diameter agrees with these measurements.
