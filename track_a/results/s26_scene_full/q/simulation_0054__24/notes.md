# Q24: speed of the green car at 2.0 s (m/s)

- The "green car" is the car in the right lane. scene/ calls it black_car, but a zoomed crop at t=2.0 s (frames/g.png) shows it is dark green. It drives down the image at constant speed.
- The prior is the orange car's acceleration, −2.86 m/s². The video is a 2D top-down view with a static camera and both cars in one plane, so one m/px scale applies to both.
- Time base: fps is 30.003 and question_fps is 30.0. The difference is negligible: the result scales with 1/fps, so it changes by about 0.01%. t = 2.0 s is frame 60.

## Measurements (measure.py → edges.npy, fit.py, fit2.py)
- Mask = |frame − median background| > 40, then open and close. I took the largest component in each lane and recorded its bbox top and bottom y on every frame.
- **Orange car:** I fitted a quadratic to the bbox-centre y over frames 16–90 (full view).
  - Acceleration = −0.1808 px/frame², residual rms 0.5 px.
  - It is stable across windows: 25–90 gives −0.1812, 16–60 gives −0.1793, and 40–90 gives −0.1803. The 5-frame speeds fall linearly from 16.1 to 4.7 px/frame.
  - The single edges give −0.188 (top) and −0.173 (bottom). Motion blur stretches the mask early in the clip, and using the centre cancels most of that.
- **Scale:** 2.86 / (0.18075 × 30.003²) = 0.017578 m/px. Sanity check: the orange car's 293 px length is 5.15 m and the green car's 292 px is 5.13 m, which are plausible car lengths.
- **Green car:** a linear fit to the centre over frames 37–70 (full view) gives 22.436 px/frame. A quadratic term of about 0.01 px/f² means the speed is constant. The one-frame step at frame 60 is 22.5 px.
- **Speed:** 22.436 × 30.003 × 0.017578 = **11.83 m/s**.

## Second route
- Single-edge fits over wider windows: the top edge over frames 37–83 gives 22.32 px/f, and the bottom edge over frames 24–70 gives 22.33 px/f. Both give 11.78 m/s.
- The one-frame step at frame 60 (22.5 px) gives 11.87 m/s.
- The routes agree within 0.5%.

Confidence: high, about ±2%. The main uncertainty is the orange car's acceleration in px/frame² (about ±1%).
