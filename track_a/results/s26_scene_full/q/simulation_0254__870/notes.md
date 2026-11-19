# q_870: acceleration of the tennis ball at t = 1.75 s (frame 42)

**Answer: 6.29 m/s²** (uncertainty about ±4%, mostly from the ball's pixel diameter)

## Inputs and time base
- The prior is the ball diameter, 0.17 m. No depth_info is given.
- fps and question_fps are both 24, so t = 1.75 s is frame 42.
- At frame 42 the ball is on the straight ramp. Frames 20-47 are the clean ramp segment; frame 48 is the floor impact.

## Key finding: perspective
- The pixel acceleration is not constant along the ramp. A linear fit of the per-frame pixel speed gives about 800 px/s² over frames 20-33 and about 600 px/s² over frames 36-47. A plain quadratic fits the path with 1.5 px rms.
- The ramp recedes from the camera. A model of constant acceleration along a 3D line, seen through a pinhole camera, fits the path almost perfectly:
  - Model: p(t) = A + B/(1 + b1·t + b2·t²), where p is the position along the image line (`fit3d.py`).
  - Fit residual: 0.22 px rms, the same as the 0.25 px scatter perpendicular to the path.
- Independent check (`check.py`): the dark ramp strip on frame 0 narrows from 69.13 px at x = 355 to 64.49 px at x = 1355, a ratio of 0.9329. The model predicts a depth ratio between frames 20 and 47 of 0.9323. The two agree, so the ball's real acceleration is constant and the falling pixel acceleration is a perspective effect.
- The measured ball diameter also shrinks along the path, from about 23.5 to about 22.3 px. This agrees with the model within noise.

## Metric conversion
- Metric positions come from the ball diameter at each frame: X = (x − cx)·0.17/D and Y = (y − cy)·0.17/D, with the principal point at the image centre, and Z = f·0.17/D. D(t) is taken from the depth model, scaled to the measured diameters.
- With the model, the 3D speed differences are constant across frames.
- Sensitivity:
  - Focal length: 6.42 (f = 1500 px) to 6.46 (f = 2700 px) at D(42) = 22.27 px.
  - Principal point shifted by ±100 px: ±0.025.
- Ball diameter at frame 42, depth-normalised and averaged over frames 21-47:
  - Chroma soft area with interior normalisation: 21.6 px. This is biased low by limb darkening.
  - Rim-normalised chroma coverage: 23.0 px.
  - Uncorrected soft area, through the model: 22.3 px.
  - Luma edge: about 23.5 px. Ball and background have similar luma, so this is less reliable.
  - The record's hue mask: about 23.1 px.
  - **Adopted value: 22.8 ± 0.5 px.**
- Result: a = 6.44 × 22.27/22.8 = **6.29 m/s²**.

## Second route and checks
- A purely local 2D estimate gives 4.56 m/s²: the pixel acceleration over frames 38-46 (604 px/s²) divided by the diameter (22.5 px), times 0.17. It is low because it ignores the term caused by the ball receding while moving fast. The strip-taper check shows that term is real.
- Physics sanity check: g·sin(44°) = 6.84 for frictionless sliding, and 5/7 of that is 4.89 for rolling. The answer of 6.3 is close to the frictionless case, which is plausible.
- **Confidence:** moderate. The scale (ball diameter, about ±3%) is the main uncertainty.
