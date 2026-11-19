# Q371: speed of the shark at t = 1.5 s (m/s)

Prior: the turtle's acceleration is 2.639 m/s^2. depth_info: none. The video is 2D: both animals swim leftward at constant y and the camera is static, so I used one metres-per-pixel scale for both animals.
fps = question_fps = 24, so t = 1.5 s is frame 36.

## Method
- `track_ff.py`: frame-to-frame template matching on high-pass, contrast-normalised grey images with a sub-pixel peak. It measures the per-frame displacement (step) directly, so no chaining of templates is needed.
  The patches follow the scene/ ref tracks: turtle carapace (ref-120..ref+130, y 490-575); shark front body (ref-450..ref, y 40-240); and an independent shark mid-body/dorsal patch.
- `fit_steps.py`: linear fit of step against frame (constant acceleration).
  - Turtle, frames 10-47: a = 0.927 px/frame^2 (sub-windows give 0.905-0.939). Residual rms 0.5 px. Extrapolating the fit, the step is zero at frame ~0.4, so the turtle starts from rest at frame 0.
  - Shark, frames 1-38: a = 2.53 px/frame^2. The fitted step at frame 36 is 89.1-89.5 px (directly measured: 89.6; mid-body patch: 89.6).
- Scale: 2.639 / (0.927 × 24²) = 0.00494 m/px.
- Shark speed at frame 36 (one-frame backward difference): 89.4 px × 24 × 0.00494 = **10.6 m/s**.

## Checks
- Second route, using the mid-body patch: 10.64 m/s. The mean of the steps over frames 34-38 gives 10.59.
- I also fitted quadratics to the ref_x positions in the scene/ record: turtle a = 0.94 and shark step@36 = 87.8, which gives about 10.3. That record's chained templates are noisier (±3-5 px per frame), so I prefer the frame-to-frame result.
- The main uncertainty is the turtle's pixel acceleration (about ±2 %).

Confidence: good (about ±3 %).
