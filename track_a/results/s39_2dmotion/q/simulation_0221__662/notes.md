# q_662: acceleration of the vacuum cleaner at t = 1 s (m/s^2)

Prior: the vacuum's diameter is 0.438 m. The video is a 2D top-down render. The file and question_fps are both 24, so t = 1 s is frame 24.
By the convention, a = (speed(24) - speed(23)) x fps, where speed(i) = |p(i) - p(i-1)| x fps.

## Scale
- The vacuum's diameter at frames 22-25: the record's circle fit gives 121.3-121.8 px. My Otsu threshold gives a bbox of 122 x 120 px and an
  area-equivalent diameter of 120.0-120.5 px. On a 4x zoomed crop (frames/f24_zoom.png) the edges are at x 1332-1451 and y 319-439, about 120 px.
  I used D = 121 px, so the scale is 0.438 / 121 = 3.62e-3 m/px.
- The SAM 3 mask (box prompt, frame 24) has a centroid of (1391.8, 377.3). This matches my centroid of (1391.85, 377.89) and the record's
  (1391.35, 378.09) to within 0.8 px. However, its extents are 133 x 142 px (area-equivalent diameter 132 px). That is about 9% larger than
  the other measurements. On the zoomed frame and the overlay (frames/seg_01_f24.jpg) the SAM outline is jagged, with a bump on top: it
  includes the soft shadow and halo around the disc. The disc itself is about 120-122 px, so the SAM extents were not used.
  (A text prompt with "robot vacuum cleaner" returned no instances.)

## Acceleration (pixels)
I used three independent position routes: the scene record's circle fit, my Otsu-threshold centroid (my_track.py, route A) and subpixel
template matching between consecutive frames (route B).
- Raw one-frame ds at frame 24 is noisy: 0.122 (record), 0.204 (A) and 0.174 (B) px/frame^2. Position noise of about 0.3 px dominates.
- I fitted quadratic and cubic polynomials to each speed series over windows within frames 10-32, before the sunlit patch and the kink at
  frame 39 (fit_routes.py and accel_fit.py). These give ds(24) = 0.205-0.23 px/frame^2 in every case. The mean of the three routes over
  frames 12-32 gives 0.209 (quadratic) and 0.222 (cubic).
- Polynomial fits to the positions (accel_fit.py) give a median of 0.208.
- Adopted value: ds = 0.21 px/frame^2, so a = 0.21 x 24^2 = 121 px/s^2.
- Context: the speed rises from 0 at frame 0 to a peak of about 20.5 px/frame near frame 26, so at frame 24 the vacuum is still accelerating
  slightly.

## Answer
a = 121 px/s^2 x 3.62e-3 m/px = **0.438 m/s^2**. Over the range of fits (0.20-0.22 px/frame^2) this is 0.42-0.46 m/s^2.
Confidence: moderate. The acceleration is small near the speed peak, so the answer depends on the smoothing (about ±7%).
