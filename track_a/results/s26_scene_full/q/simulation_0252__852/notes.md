# Q852: speed of the soccer ball at t = 1 s

- This is a 2D render with a static camera. fps = question_fps = 24, so t = 1 s is frame 24, and the speed is the step from frame 23 to frame 24 times 24.
- **Scale.** The prior gives the diameter as 0.344 m, and the ball is 66 px across, so the scale is 0.344/66 = 5.212e-3 m/px.
  - I checked the 66 px in `rim.py` (frames/rim24.png): a circle of r = 33 px drawn on a contrast-stretched frame 24 sits on the rim.
  - The vertical extents of the star patches on frame 10 (y 350 to 416) agree.
  - The horizontal width of about 72–76 px is widened by motion blur, so I did not use it.
- **Motion.** I used `scene/tracks/ball.csv`, the left-limb ellipse tracker (cx; the scene record lists it as accurate to ±1.5 px).
  - The raw step from frame 23 to 24 is 50.2 px.
  - Polynomial fits over several windows (`speed.py`) give 49.8–50.2 px/frame.
  - Speed = 50.2 × 5.212e-3 × 24 = **6.28 m/s**.
- **Second route.** I tracked the ball myself with background difference and the midpoint of the equator-row limbs (`measure.py`). It gives 50.7–50.8 px/frame, or 6.35 m/s. That is 1% higher, probably because the shadow pushes the right limb outward.
- **Confidence.** High, about ±3%. The main uncertainty is the pixel diameter (66 ± 1.5 px).
