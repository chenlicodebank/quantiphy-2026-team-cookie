# q_209 – diameter of the grey truncated cone on the charging post

2D scene, fps 24 = question_fps (no re-timing). Object: the light-grey frustum-shaped disc directly under the phone
(above the dark band of the lift head). It is light grey (~186-191 RGB) vs the dark band (~40-60).

## Scale (prior: lifting speed 0.2 m/s)
Phone/head rise at constant speed from frame 1 to 27: top_y 954.98 -> 332.07 = 622.9 px / 26 frames
= 23.96 px/frame = 575.0 px/s (scene/tracks/phone.csv; per-frame steps 23.9-24.1). Independent check with my own
measure.py: disc side top row 657 (frame 15) -> 370 (frame 28, at rest since 27) = 287 px / 12 frames = 23.9 px/frame.
Scale = 0.2 / 575.0 = 3.478e-4 m/px.

## Diameter (measure.py, background-difference mask, sub-pixel edge coverage, frames 15, 28, 30)
- Sloped (cone) part rows 360-368 widen from ~294 to 316 px; vertical part rows 371-387: 315.7-316.7 px, max 316.7
  (x 801-1117). Same values in frames 15, 28, 30.
- Max (base) diameter = 316.6 px -> 0.1101 m.
- Alternative reading (top/smaller diameter of the visible slope, ~294 px; partly hidden by phone) -> 0.102 m.
  Answer uses the largest diameter.

Answer: 0.110 m. Confidence: moderate-high on scale (±0.5%); main uncertainty is which diameter is meant.
