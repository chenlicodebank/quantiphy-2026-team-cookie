# Q767: acceleration of the basketball at t = 1.5 s

- This is a 2D video with a static camera. fps = question_fps = 24, so t = 1.5 s is frame 36. That frame is in the ascent after the bounce at frame 24; the apex is at frame 49.
- Scale: the median circle-fit diameter is 74.66 px (from scene/tracks/ball.csv; the bbox gives 74.7-76). With the prior of 0.282 m, that is 3.777e-3 m/px.
- Main route (fit.py): a quadratic fit of cy(t) over the ascent gives 501.2 px/s² for frames 26-49, 501.1 for frames 28-44 and 498.7 for frames 30-42. That is **1.89 m/s²**, a constant deceleration (the speed falls, so the signed value is -1.89).
- Second route: the per-frame convention (backward-difference speed, then the difference of speed) at frame 36 gives -1.98 m/s². Neighbouring frames are noisy (-0.6 to -2.7) and average about -1.9. This agrees with the fit.
- The descent fit gives 2.05 m/s², about 8 % more than the ascent. It is not used, because t = 1.5 s is in the ascent.
- The scene is not at real-world scale (the acceleration is not 9.8 m/s²), which is expected for these renders.
- Answer: 1.89 m/s² (magnitude). Confidence: good, about ±3 %. The main uncertainty is the ±1 px in the diameter.
