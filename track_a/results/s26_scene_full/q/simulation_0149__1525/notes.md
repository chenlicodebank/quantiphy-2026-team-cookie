# q_1525: acceleration of the car at t = 1 s (frame 24 at 24 fps; the file is also 24 fps)

**Answer: 3.6 m/s²** (fitted value 3.595; range across the sensitivity runs 3.57–3.62)

## Camera geometry (frame 49, no car) — `geom.py`, `vp.py`
- The pillar edges are truly vertical (slopes of about 0.0003 px/px), so the camera has no pitch. The horizon at
  y≈829 (light-tube vanishing point (4026, 825)) therefore comes from a lens shift, and the principal point is
  taken as (960, 829).
- Focal length from two orthogonal vanishing points: the light tubes (family A) and the red pipes running across
  them (family B). Two clean pipe fits give f = 2368 and 2401–2415, so **f ≈ 2390 px**.
- Check: at frame 0 the right-front tyre is about 139 px tall at u≈67.5, which gives f ≈ 2416 from the given
  14.244 m. That agrees within 1%.

## The car's motion — `rims.py`, `line_fit.py`, `kin.py`
- I re-measured the near-side (right) wheel rims with ellipse fits (`rims.csv`, `rims75.csv`, overlay
  `frames/rims_sheet.png`). The hubs stay on the horizon, so the camera is at hub height.
- The rear hub retraces the front hub's image path about 7 frames later. The car is translating along a straight
  line without turning, so every point on it, including the origin, has the same speed.
- Model: a straight ground-parallel line through the frame-0 right-front hub, placed at range 14.244 m along the
  pixel ray (67.5, 829). The heading θ was fitted so that the front–rear hub separation along the line stays
  constant. Result: θ = 38.05°, wheelbase 2.885 m, constant to within **0.06%** over frames 20–30.
- Size check: the rim diameter implied by the model (h_px·Z/f) is 0.507–0.512 m in every frame from 20 to 38.
  That gives a tyre/rim ratio of about 1.50, which fits the measured tyre/rim pixel ratio of about 1.45–1.56.

## Kinematics — `fit_ease.py`
- Along-line position s(i) for frames 10–38: front hub, plus rear hub + wheelbase.
- It fits Blender's default two-key ease curve s = A·(3x² − 2x³), x = (i − i0)/T, with an rms of **0.75 mm**:
  A = 16.44 m, i0 = −0.03, T = 59.2 frames. The speed peaks at about 10.0 m/s near frame 30.
- Independent check: frame 0 was not used in the fit, yet the fit predicts s(0) = −0.01 m against 0 for the
  frame-0 hub. This confirms that the car starts on the line, so the metric scale from depth_info holds.
- The reference convention is acceleration = (speed(24) − speed(23))·24, with speed(i) = |s(i) − s(i−1)|·24.
  - From the ease fit: 3.595 m/s².
  - From a free cubic fit: also 3.595.
  - Speed at frame 24: 9.57 m/s.
- Sensitivity:
  - f between 2350 and 2430 → 3.57–3.62.
  - Frame-0 hub column between 66 and 69 → ±0.01.
- Second route: a linear fit to the per-frame speeds over frames 20–28 gives about 3.5 m/s². This window is
  centred slightly later, and the acceleration is falling there.

## Confidence
High that the value is about 3.6 m/s². The rigid-translation fit and the ease-curve fit are both very tight,
and frame 0 checks the scale independently. Main residual risk: the depth_info distance is to the tyre origin,
which I took as the hub centre.
