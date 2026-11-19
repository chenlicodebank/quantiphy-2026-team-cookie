# Q1238 – diameter of the bicycle wheel (m)

The file and the question both use 24 fps, so t = 0.58 s is frame 14 and t = 1.58 s is frame 38. The principal point is assumed at (1080, 540), and the horizon row is 422.5 (from scene/).

## Focal length (the prior: white car = the white van, a = 4 m/s^2)
- **Route A, acceleration curvature** (`focal_van.py`, `check_van.py`). The van's origin at frames 14 and 38 comes from the depths 31.070 m and 29.918 m along the box-centre rays, which defines the motion line. Each frame's rear-edge pixel (row 520, the cleanest feature) is intersected with the van's near side plane (half-width 1.0 m) to get s(t). A quadratic fit gives a = 4 at **f ≈ 2150–2155 px** (frames 4–66, 4–35 and 4–46 all agree). With half-width 0 the result is 2228, and frames 36–70 alone (noisier edges) give 2063. Speed is linear in time and starts near rest at t ≈ 0, which is consistent with constant acceleration.
- **Route B, motion perpendicular to the main road** (`focal_perp.py`, using the vanishing point (1253, 422.5)). The van gives f = 2222 and the cyclist gives f = 2008; the cyclist is weakly constrained.
- **Route C, displacement from rest at t0 ≈ 0** (`focal_disp.py`): f ≈ 2236–2270. This uses box-centre x values whose front edge is interpolated at frame 14, so it is less reliable.
- **Adopted: f = 2180 px** (range 2150–2225).

## Wheel pixel size
- `wheel.py` fits circles to the light tyre rings. Both wheels are clean in frames 20–40 (front) and 27–40 (rear), with a ring-centre radius of 24.4–24.8 px.
- `wheel_profile.py` measures the outer tyre silhouette (half-max crossing of radial profiles):
  - Frames 28–34: R = 25.14–25.36 px (mean 25.24), at bike depth 27.32 m (interpolated, frame 31).
  - Frames 36–40: R = 25.5–25.7 px, at depth about 27.06 m (frame 38; given value 27.1221).
- The R × Z products agree (689 and 694) because the radius grows as the bike gets closer. The mean R·Z_cam is about 692 px·m (off-axis cos ≈ 0.999).
- The wheel plane is nearly parallel to the image plane: the cross street is about 4.5° off, and the camera pitch is about 3°.

## Result
- Diameter = 2·R·Z / f = 1384 / f, which gives 0.642 at f = 2155, **0.635 at f = 2180** and 0.623 at f = 2222.
- **Answer: 0.635 m.**
- Second check: the rider plus bike is 138 px tall, which gives about 1.7 m, and the van works out to about 6.0 m long and 2.3 m high. These are plausible real-world scales.
- Confidence: moderate. The roughly ±2–3% uncertainty in the focal length dominates; the pixel size is good to about ±1%.
