# Q1864: speed of the astronaut at t = 3 s (m/s)

Prior: the astronaut is 2.2 m tall. 2D video at 24 fps (the file and question_fps are the same), so t = 3 s is frame 72.

## Scale
- At f0 the astronaut stands upright (axis about 87-94°). My threshold mask (min RGB < 225) gives a bbox of 43 x 90 px (y 477-566). The SAM 3 "astronaut" mask at f0 gives vert_px 90 and length_px 91.0, so the two agree (<1 pct).
- Scale = 2.2 / 90 = 0.02444 m/px.

## Speed at frame 72 (measure.py, compare_sam.py)
- The astronaut rises and slows towards a stop at about f78. The rotation (~0.3°/frame) is negligible for the pelvis-vs-centroid offset.
- My mask centroid: the raw backward step f71->f72 is 1.70 px. A quadratic fit over f67-77, evaluated at 71.5, gives 1.67 px/frame. With a darkness-weighted centroid: raw 1.64, fit 1.67.
- SAM 3 track (second route): step f71->72 is 1.61 px; a quadratic fit at 71.5 gives 1.66 px/frame. This agrees with my centroid to within about 2 pct.
- Speed = 1.67 px/frame x 24 x 0.02444 = 0.98 m/s (the routes range from 0.96 to 1.00).

## Answer
0.98 m/s. Confidence is good, about ±4 pct; the main uncertainty is frame-to-frame centroid jitter.
