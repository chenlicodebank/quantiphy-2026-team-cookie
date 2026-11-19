# q_854: speed of the soccer ball at t = 2 s (m/s)

**Answer: 5.2 m/s.**

## Setup
- This is a 2D Blender render at 24 fps (the file and question_fps agree), with 41 frames (0–40, so the clip ends at t = 1.667 s).
  t = 2 s is frame 48, which is past the end of the clip. By frame ~42 the ball would also have left the image on the right.
  The speed therefore has to come from extrapolating the measured motion.
- The prior gives the ball diameter as 0.344 m. The ball moves horizontally at constant depth: its apparent size stays the same and cy = 382.5 throughout.
  So one metres-per-pixel scale applies to the whole motion.

## Scale
- Vertical diameter, which motion blur does not affect: the top limb is at y ≈ 349.5, read from the column profiles where the shadow meets the ball.
  The bottom limb is at y ≈ 416–417, read from the bright rim and where the bottom stars end (frames 6, 12, 21, zoomed in zoom.py / vprof.py).
  That gives D ≈ 66.5 px; the scene record says 66 ± 1.5.
- The horizontal width is ≈ 70 px, both near the image edge and at the image centre. Because it does not change across the frame, the extra width is motion smear, not perspective, so I did not use it.
- Scale = 0.344 / 66.5 = 5.17e-3 m/px.

## Motion
- I used the x-track from scene/tracks/ball.csv (frames 5–40). My own ellipse fits to the lower half of the silhouette (edgefit.py) gave the same centres to within about 1.5 px.
- The per-frame step falls from about 57 px/frame to about 45 px/frame, so the ball slows smoothly. There is no bounce or contact.
- Fits used to extrapolate the step to frame 47→48 (fit.py):

| Model | RMS residual | Step at 47→48 | Speed |
|---|---|---|---|
| Exponential drag, k = 0.0076/frame | 1.06 px | 41.8 px/frame | 5.19 m/s |
| Cubic | 0.94 px | 42.8 px/frame | 5.31 m/s |
| Quadratic, all frames | 1.31 px | 41.0 px/frame | 5.09 m/s |
| Quadratic, frames 20–40 | — | 42.0 px/frame | 5.22 m/s |

- Between them, the models give 5.09–5.31 m/s. The deceleration shrinks over time, so the drag-like and late-window fits are the ones I preferred.
  Answer: 5.2 m/s.

## Confidence
- The answer is moderately uncertain:
  - The extrapolation model contributes about ±2–3%.
  - The pixel diameter contributes about ±1.5%.
  - The answer assumes the motion simply continues past the end of the clip.
