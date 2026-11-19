# Q851: speed of the soccer ball at t = 0.5 s

- This is a 2D clip at 24 fps. question_fps is also 24, so t = 0.5 s is frame 12. The camera is static and the ball rolls horizontally at y ≈ 382.5.
- **Scale.** The prior gives the diameter as 0.344 m. The ball's pixel diameter is 66 px, measured vertically because motion blur widens it horizontally to about 71 px.
  - I checked this on frame 12 with column profiles (`measure2.py`) and an upscaled crop (`frames/c12.png`). The top limb is at about 350 and the bottom limb at about 415–416. The limb positions at offsets of ±10 and ±20 px fit a radius of about 33–34 px.
  - The scale is 0.344/66 = 5.212e-3 m/px.
- **Motion.** I used the cx track from scene/tracks/ball.csv, which follows the left limb and is calibrated with an ellipse.
  - The raw step from frame 11 to 12 is 55.5 px.
  - A quadratic fit over frames 5–23 gives a step of 55.13 px at frame 12.
- **Speed.** 55.13 px/frame × 24 × 5.212e-3 = 6.90 m/s. The raw step gives 6.94 m/s.
- **Second route.** I took the midpoints of the thresholded horizontal extent against the background (`measure.py`) for frames 10–14. Their slope is 54.65 px/frame, which gives 6.84 m/s. This agrees within 1%.
- **Confidence.** The main uncertainty is the pixel diameter (66 ± 1.5 px), about ±2%. Answer: 6.90 m/s.
