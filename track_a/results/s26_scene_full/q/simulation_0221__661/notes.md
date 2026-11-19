# q_661: speed of the vacuum cleaner at t = 1 s

- The scene is 2D: a top-down view with a static camera. fps = question_fps = 24, so t = 1 s is frame 24. Speed = |p24 - p23| x 24.
- **Pixel step from frame 23 to 24:**
  - scene record (circle fit to the rim): 20.24 px.
  - my own template match of the vacuum crop between frames 23 and 24, with subpixel peak: 20.26 px.
  - Hough circles (integer centres, noisy): 21.0 px. The steps from neighbouring frames are about 20.1-20.5 px, so the motion is smooth.
  - Used: 20.25 px per frame, which is 486 px/s.
- **Diameter in pixels (prior 0.438 m):**
  - Measured from half-level edge crossings of intensity profiles through the centre (`diam.py`).
  - Vertical extent: 120.1 px at frames 24, 75 and 79.
  - Horizontal extent at rest (frames 75 and 79): 120.95 px. At frame 24 it is 122.2 px, widened by motion blur along x.
  - The record's circle fit gives 121.5 px at frame 24, and 122.9 px near the dock where perspective shows the side wall.
  - Used: 120.8 px (±0.7). Scale = 0.438 / 120.8 = 3.626e-3 m/px.
- **Speed:** 20.25 x 24 x 3.626e-3 = **1.762 m/s**. With the record's 121.5 px diameter it would be 1.752 m/s.
- **Second route:** the template-match step and the record's circle-fit step agree within 0.1%. The diameter choice leaves about 1% uncertainty.
- **Confidence:** high, about ±2%.
