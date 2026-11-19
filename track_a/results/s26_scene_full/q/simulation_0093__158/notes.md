# Q158: speed of the plane at 0.5 s (m/s)

The video is a 2D simulation at 24 fps. question_fps is also 24, so t = 0.5 s is frame 12. The prior is car length = 5.67 m.

## Measurements (measure.py, step2.py)
- **Car pixel length at frame 12:** 92 px with thresholds 12–30, 90 px with threshold 50, and 91.2 px from the half-max subpixel edges. Frame 0, where the car is nearest the image centre and perspective has the least effect, gives 91–92 px. I used 91.5 px, which gives a scale of 5.67 / 91.5 = 0.06197 m/px.
- **Plane motion:** the plane moves at constant velocity, measured by cross-correlating the whole plane between frames.
  - Frames 2→18: 40.40 px/frame
  - Frames 6→18: 40.37 px/frame
  - Frames 2→11: 40.28 px/frame
  - Frames 11→12 alone: 40.75 px/frame. This single step is about 1% off because of frame-level jitter.
  - The scene record's ref_x gives a mean of 40.36 px/frame.
  - I used 40.4 px/frame.
- **Speed:** 40.4 × 24 × 0.06197 = **60.1 m/s**. The single 11→12 step would give 60.6 m/s.

## Checks
- Scale check: the plane's 608 px length × 0.06197 = 37.7 m, which matches a real A320 (37.6 m). This confirms the plane and the car are at the same depth, so one scale applies to both.
- The car's speed comes out at 20.13 × 24 × 0.062 = 30 m/s, which is plausible.

## Confidence
The main uncertainty is the car's pixel length (91–92.5 px), which puts the answer between about 59.4 and 60.6 m/s. Confidence is about ±2%.
