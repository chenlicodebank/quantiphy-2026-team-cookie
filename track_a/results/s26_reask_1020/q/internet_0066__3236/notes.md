# q3236: ball displacement 1.80 s to 1.90 s

- question_fps = file fps = 30, so the times are frame 54 and frame 57.
- The camera looks straight down at a gym floor, and the basketball rolls across it from right to left. The prior (g = 9.8 m/s^2) describes no motion seen in the clip because nothing falls, so it gives **no usable scale**. The scale comes instead from the ball, a regulation basketball with a diameter of 0.24 m. Its vertical pixel diameter, which has no motion blur, is 256 px (record median over frames 53-69). Scale = 0.24/256 = 9.375e-4 m/px.
- Pixel displacement from frame 54 to frame 57, using the ball centre from scene/tracks/ball.csv (cx_stab, cy_stab; the mask covers only the ball):
  - direct difference of the two frames: 280.5 px
  - quadratic fit over frames 53-69: 277.3 px
  - linear fit over frames 53-69: 271.1 px (90.4 px/frame)
  - adopted value: 276 px, giving **0.259 m** (range across the methods 0.254-0.263 m)
- Second route (measure.py): I made my own background-difference mask. It also picks up the soft shadow, which makes it about 350 px wide, so I did not use it for centres. The record's bbox edges give 267 px for the left edge and 291 px for the right edge, a mean of 279 px. This agrees with the adopted value.
- Plausibility check: 90 px/frame × 9.4e-4 × 30 ≈ 2.5 m/s, a reasonable speed for a rolled ball.
- Confidence: moderate. The main uncertainty is the scale assumption (a size 7 ball, 0.24 m). A size 6 ball would make the answer about 3% smaller.
