# Q2883: soccer ball velocity at 0.5 s (frame 12 at 24 fps; the file is also 24 fps)

## What the video shows
- At frame 12 the soccer ball is still **held**: the thrower's hands are masked out and hide most of it. You can see this in frames/view.png, made by view.py.
- The throw only starts later:
  - wind-up toward the camera at about frames 17–22 (apparent diameter grows from 54 px to about 61 px);
  - release at about 23–25;
  - then flight away from the camera.

## Measurements
- edges2.py and edges3.py measure the unoccluded top and right edges of the ball for frames 0–24. These edges stay at the same place, within the ±1–2 px noise, from frame 0 through frame 17:
  - top edge at about 583–588 px;
  - right edge at about 929–933 px.
- So the ball is nearly at rest at frame 12. The only small drift is a lift of about 4–5 px between frames 9 and 12 and back by frame 14, which is roughly 1.5 px per frame.
- **Scale:**
  - The depth of 3.254 m at t = 2.0 s and the 51.9 px diameter at frame 48 give a ball diameter of 0.221 m (a size-5 soccer ball).
  - While held, the diameter is 54 px, so z is about 3.13 m and each pixel is about 4.1 mm.
- **Speed:** 1.5 px per frame × 4.1 mm × 24 fps is about 0.15 m/s. Measuring the centre shift from the edges gives 0.17 m/s over frames 9→12 and 0.14 m/s over 12→14.
- If the reference used noisy clicks smoothed over 5 frames, its noise alone would also come to about 0.1–0.15 m/s.

## Check of the conventions with the prior (prior_check.py)
- Basketball: the depth of 2.24 m at frame 12 and the 75.8 px diameter give D = 0.2225 m.
- The forward differences over frames 12–18 give 1.7–2.45 m/s, and the 5-frame chord gives 2.04 m/s. The prior is 2.21 m/s, so the pipeline is consistent.

## Answer
0.15 m/s. Confidence is low: the true value is close to zero, so a small absolute difference is a large relative error.
