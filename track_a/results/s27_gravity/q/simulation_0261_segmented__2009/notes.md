# q2009 - speed of the mug at t=0.625 s
- 2D video, 24 fps (file fps = question_fps = 24). t=0.625 s -> frame 15. Mug is in free fall over frames 0-18; it hits the floor between f18 and f19.
- Scale from the prior (a = 9.8 m/s^2): I fitted a quadratic to the mug centre y (scene/tracks/mug.csv, cy_bbox and cy_mask) over frames 0-18.
  Pixel acceleration = 8.81-8.85 px/frame^2 (rms 0.4-0.6 px), so scale = 9.8/(a_px*24^2) = 0.001924-0.001931 m/px.
- Speed (benchmark convention, one-frame backward difference): (y15 - y14)*24*scale = 129.5 px * 24 * 0.001924 = 5.97-5.99 m/s.
  From the fitted parabola, the backward difference is 5.96-5.98 m/s. Second-route check: free fall from rest at t0 = -0.1 frame gives g*(14.5+0.1)/24 = 5.96 m/s. All three agree.
- The top and bottom edges give 5.90-6.10 m/s (noisier because of the mug's apparent tilt wobble).
- Answer: 5.97 m/s. Confidence: high (about 2 pct).
- fit.py does the fits.
