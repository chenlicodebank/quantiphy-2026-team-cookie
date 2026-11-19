# q_3182 — height of the left billboard (cm)

Prior: g = 9.8 m/s^2. Internet video, 30 fps (file = question_fps). Treated as a 2D scene with one scale.

## Scale from the ball's fall (fit.py, fit2.py)
- Track: scene/tracks/ball.csv, cy_bg (camera-drift corrected), frames 66-97. Frames 77-80 (top clipped) are excluded.
- Quadratic fit over the whole flight: a = 4956 px/s^2 (4963 with the clipped frames; raw cy gives 4930; mask centroid gives 4931).
  The mean of the one-frame second differences is 5.54 px/frame^2, which is 4988 px/s^2.
- Rising half alone: 5327 px/s^2. Falling half alone: 4747. This is a systematic difference (perspective, residual camera roll or drag),
  so I used the whole-flight value, about 4950 px/s^2.
- Scale = 9.8 / 4950 = 1.98 mm/px. Sanity check: ball diameter of 121 px x 1.98 mm = 24 cm, which matches a basketball.

## Billboard pixel height (poster.py, poster2.py, zoomed crops frames/pt.png, frames/pb.png)
- Frame 0: the dark outer frame runs from y about 262 to 647 (386 px by intensity profile). A lighter band under it,
  the lower lip or shadow of the frame, reaches about 655. The scene record's box is 260-653, which is 394 px.
- Frames 40 and 85 give about 381-384 px with the same threshold (no zoom; the camera drifts).
- Value used: 390 px (range 386-394).

## Answer
390 px x 1.98 mm/px = 77.2 cm. The range is about 72.5-81 cm across the fit windows and edge choices.
Second route: the second-difference mean (4988 px/s^2) gives 76.6 cm.
Confidence: moderate (about ±5%).
