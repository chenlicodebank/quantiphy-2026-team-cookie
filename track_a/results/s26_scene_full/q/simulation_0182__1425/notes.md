# q1425: speed of the box at t = 1 s (frame 24 at 24 fps)

The prior says the box's acceleration after 0.75 s is 2.338 m/s². Depths given: 9.522 m at frame 0 and 9.384 m at frame 12. The file is 24 fps, the same as question_fps.

## Motion
- The box falls from rest (frames 0–7) and lands on the inclined roller ramp at frame 8.
- It pivots onto the ramp (frames 8–13), then slides down-right and toward the camera with uniform acceleration (frames 13–39).
- I checked the scene/ record: its track covers the right object, but the centroid wobbles while the box rotates. So I re-tracked the box with frame-to-frame template matching of its core (`track_tm.py` → `tm_steps.csv`; correlation 0.98–0.998).

## Perspective: ramp vanishing point (`ramp_vp2.py`)
- I fitted the ramp's near-rail bottom edge (rms 0.7 px) and its far top edge (rms ~4–9 px, textured) on frame 0.
- They meet at VP = (-4227, -2407).
- Check: the box's own image path line passes through that VP (y = -2414 at the VP's x, vs -2407).
- For a point moving on a 3D line, 1/|x − VP| is affine in the true arc length. With uniform acceleration, 1/r is therefore quadratic in t, and v(1)/a = c1/(2·c2). This ratio does not depend on the scale (`fit_tm.py`).

## Route A (scale-free, uses the exact prior a)
- Template track: v(1)/a = 1.381. It stays at 1.380–1.385 for every fit window (13–35, 14–39, 18–39, 24–39 …).
- v(1) = 2.338 × 1.381 = 3.23.
- One-frame backward difference at frame 24: 3.23 − a/48 = **3.18**.
- Sensitivity: scaling the VP by ±15% changes the ratio to 1.47 / 1.32.
- The scene/ centroid track gives 1.26–1.39, which is noisier because of the box rotation.

## Route B (metric 3D)
- Focal length from the free fall, assuming g = 9.81 in scene units. The box drop gives 2140–2230 px/s² (depending on whether it is fitted as starting from rest), which means f ≈ 2030–2125 px at Z ≈ 9.33 m.
- I placed the box at 9.384 m along its pixel ray at frame 12 and slid it along the 3D line toward the VP direction (`metric3d.py`, `fit_tm.py`).
  - With the measured VP, the metric acceleration comes out at 2.39–2.49. That is 2–6% above the prior, a reasonable agreement.
  - Solving for the VP that makes a = 2.338 exactly gives VP x = −3530 to −3940, inside the edge-fit uncertainty (about −3800 to −4800). Then the backward-difference speed at frame 24 is 3.26–3.41 (`fit_tm_consistent.py`).

## Scale check
The box's frame-to-frame apparent scale grows about 1.13× from frame 16 to 35, against 1.11× predicted by the VP model. This is consistent, if noisy.

## Answer
The routes give 3.18 (A) and 3.26–3.33 (B, for f ≈ 2080–2125). Per-frame template steps show a small alternating jitter: the frame-24 step is about 2% below the smooth trend. If that jitter is real simulation motion, the raw speed would be slightly lower.

**Answer: 3.2 m/s.** I expect it to be within about 5%.
