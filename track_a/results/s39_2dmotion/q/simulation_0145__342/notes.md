# q_342: acceleration of the rocket at t = 1 s (m/s^2)

Prior: the rocket is 2.9 m long. 2D render at 24 fps; question_fps is also 24, so t = 1 s is frame 24. The rocket flies in
a straight line at 39 deg up-left (the axis from scene/ was checked: perpendicular offset of the mask is under 0.1 px
in frames 15-24). The camera is static.

## Scale: rocket length in px (blur-free)
- Each frame has about 0.8 frame of motion blur, so every raw extent is too long by about 0.8 x v.
  - SAM 3 masks (frames 14/16/18/20): 228 / 237 / 245 / 252 px. These include the blur smear. My own blurred extents
    agree (3-10% threshold: 240-250 px at f18), so SAM and my mask match as *blurred* extents.
  - The 50%-of-plateau ends used in scene/ give 202 px. That is too short: the nose is a long ogive taper, so its 50%
    point sits well behind the tip.
- `blurfit.py` fits a forward model to the along-axis profiles of the nose (frames 8-21) and tail (frames 14-24): a
  static end shape (nose taper about 39 px; tail with a light nozzle) convolved with a box of length sigma x v.
  - Result: sigma = 0.82, tip-to-tail L = 214.8 px (sd 0.6 over frames 15-21).
  - With sigma fixed at 0.5-0.9: L = 219-212 px. The fit is worse at 0.5.
  - Used L = 215 px, so the scale is 2.9 / 215 = 0.01349 m/px.
- I read "length" as the rocket's own long axis. If it meant the world-AABB horizontal extent of the tilted rocket
  (about 178 px), the scale would be 0.0163 m/px and the answer about 14.5 m/s^2.

## Acceleration at frame 24 (px/frame^2)
- Speeds (px/frame) come from sub-pixel matching along the axis between consecutive frames:
  - Nose region, frames 7-21 (`nosexc.py`).
  - Tail region, frames 15-24, with a fitted gain (`xcorr3.py`): 6 variants (diff/gray images, 3 windows).
- The speed rises from about 27 (f9) through 47.9 (f16) and 56.6 (f20) to about 62.9 (f24).
- The acceleration is not constant: it is about 3.0 px/f^2 in frames 8-14 and about 2.0 in frames 14-21. This is
  consistent with Blender's default Bezier ease (smoothstep), where the speed is a parabola.
- Fitting v = k (f - f0)(f1 - f) gives f0 of about 1 (matches launch onset, when the truck starts rocking at frame
  2) and f1 of about 62-78.
  - a(24) = v(24) - v(23) = 1.44-1.63 px/f^2 depending on the fit window. A free quadratic gives the same.
  - (`final_fit.py`, `vfit.py`)
- Adopted a = 1.55 px/f^2 = 893 px/s^2, which gives 893 x 0.01349 = **12.0 m/s^2**.

## Second-route checks and disagreements
- **Tail edges** (50% crossing on the max-channel diff, `measure.py`; forward-model tail, `accel2.py`):
  - Frames 16-21 agree with the matching to within about 1 px/frame.
  - Frames 22-24 give flat speeds of about 60, against 62-63 from the matching. That would mean a(24) of about 1.0 or
    less.
  - The gray-image edge crossing (`tailcheck.py`) instead agrees with the matching (62-63.5). So I trusted the
    gain-fitted matching, which uses many more pixels.
- **A constant-acceleration fit** over frames 16-24 gives 2.0 px/f^2, which is 15.5 m/s^2. It is rejected because
  early frames clearly accelerate faster.
- Plausible range: 1.0-2.0 px/f^2, i.e. 7.8-15.5 m/s^2. Best estimate 12.0. Confidence moderate: the main
  uncertainty is the local slope of the speed at f24, with the rocket half out of frame.
