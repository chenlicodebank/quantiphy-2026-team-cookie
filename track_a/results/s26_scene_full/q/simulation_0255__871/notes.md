# q_871 – speed of the tennis ball at t = 0.5 s

2D render, 24 fps (file fps = question_fps = 24, so no re-timing). t = 0.5 s → frame 12. Static camera, single ball
rolling right along y ≈ 562.6 px with steady deceleration of about −0.266 px/frame².

## Scale (prior: diameter = 0.17 m)
- `diam_speed.py` finds sub-pixel half-level edge crossings (between the background and the ball interior) on
  the rows around the centre and takes the widest chord. Width is 23.9 px at frame 12, 23.7 px as the median over
  all frames, and 23.5 px over frames 8–28. The diameter is taken as 23.7 px. The recorded value of 24.5 px came
  from the background-difference mask, which includes blur and the contact shadow.
- That gives 0.17 / 23.7 = 0.007173 m/px.

## Pixel speed at frame 12
- Edge-centre track (mine): dx(12) = 41.08 px. Quadratic fit gives 41.10. Mean of dx over frames 10–14 is 41.09.
- Recorded chroma centroid: the raw dx is 40.35 because of noise. Its quadratic fit gives 41.07, which agrees
  with the edge-centre track.
- That gives 41.08 px/frame × 24 = 985.9 px/s.

## Answer
985.9 px/s × 0.007173 m/px = **7.07 m/s**.

The two tracks (edge centre and chroma centroid, both fitted) agree to 0.1%. The main uncertainty is the diameter.
If it is 23.5–24.5 px, the speed is 6.84–7.13 m/s. Confidence is good, within about 3%.
