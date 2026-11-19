# q_1919: speed of the box at t = 0.4 s

The video is a 2D segmentation clip at 120 fps, and question_fps is also 120. t = 0.4 s is frame 48. The box falls straight down onto the truck roof and hits it at about frame 61.

## Method
- Scale comes from the prior: the box's acceleration before 0.6 s is 9.8 m/s². I fitted a parabola to the box's vertical position over the free-fall frames to get its pixel acceleration a_px. Then m/px = 9.8 / a_px.
- Speed is the backward difference of the fitted curve at frame 48, (y48 − y47)·fps, converted with that scale.
- Positions:
  - `edges.py`: sub-pixel top edge of the silhouette (front-face top), averaged over columns 540-800. It is only visible from frame 24 on. I did not use the silhouette bottom because the underside strip shrinks with perspective.
  - scene/ track: center_y and face_bottom_left, at integer pixels. They cover frames 0-59 and include the clipped early frames.

## Results (`fit.py`)
| route | frames | a_px (px/s²) | v(0.4 s) (m/s) |
|---|---|---|---|
| scene center_y | 5-59 | 1955 | 3.90 |
| scene face_bottom | 0-59 | 1956 | 3.89 |
| top edge, sub-pixel | 24-59 | 1881 | 4.05 |
| top edge, sub-pixel | 30-59 | 1892 | 4.02 |

- The pixel speed at frame 48 is the same on every route: 776-778 px/s. Only the scale differs.
- The full-range fits are better conditioned and agree with the physics check. They put the start of the fall at frame ≈0, and the box is at rest over frames 0-4.
- Physics check: a box starting from rest at t = 0 at g has a backward-difference speed of 9.8 × 47.5/120 = 3.88 m/s, and an instantaneous speed of 3.92 m/s.
- Scale sanity check at 0.0050 m/px: the box is about 2.05 × 0.95 m and the truck about 8.6 m long, both plausible.

## Answer
3.90 m/s. Confidence is high, within about 3%.
