# Q1335 — length of the turning yellow car (taxi), simulation_0066

Answer: **5.62 m** (bumper to bumper; the car's own long axis).

File fps = question fps = 24, so frame = round(t*24). t=0.58 s -> f14 and t=1.58 s -> f38. Static camera, 2160x1080, 3D scene.

## Focal length (principal point assumed at the image centre)
- `vp2.py`: curb edges fitted with guided edge detection on scene/bg.png (rms < 0.5 px; overlay in frames/lines.png).
  Road A vanishing point = (620.5, 77.5) (two line pairs agree within 1 px). Road B vanishing point = (3100, 82).
  If the roads are perpendicular, **f = 846 px** (HFOV about 104 deg, slightly above the stated range).
- Check with the prior, which `vanacc2.py` reproduces at f = 846:
  - The white van is still until about f6 in pixels, which is consistent with starting from rest at t=0 (radial motion is barely visible).
  - Displacement f14->f38 from the depths + rays: 4.25 m. Predicted for a = 4 from rest at t=0: 4.33 m.
  - Speeds at f14/f38: 2.32/6.40 m/s (predicted 2.33/6.33).
  - Acceleration fitted with t0 = 0: 4.09 m/s^2.
  - Taken together, the prior supports f in about 780–920.
- Ground normal from the two vanishing points. The pedestrian (pelvis depth + feet pixels, `ground.py`) gives a pelvis height of
  0.92 m (stature ≈ 1.73 m, realistic) and a camera height of 7.0 m above the ground.

## Route 1 — the taxi's depth_info (`taxi3d.py`)
- Taxi masks: frame minus bg, with shadows removed (`taximask.py`; overlays checked at f38 and f60).
- Taxi centroid rays at f14/f38 are scaled to the given depths, and the taxi is tracked on a plane parallel to the ground.
  Its heading per frame comes from that track.
- The silhouette tips along the projected heading are intersected with the car's vertical centre plane.
- L depends on the view angle phi, because corners inflate it when the view is oblique. The minimum is at side-on view, f52–55 (phi 0–7°):
  **5.71–5.74 m** with the average origin plane. Using the f38 plane, which suits side views better (the f14 front-view
  centroid sits ≈0.2 m low), gives ≈5.63 m.

## Route 2 — ground plane from the pedestrian plus wheel contacts (`route2.py`, `route2b.py`)
- Near-side tyre contacts were read from 3x crops: f52 (484,606),(700,556.5) and f38 (678,550),(837,499).
  Wheelbase 3.06 / 2.95 m.
- The vertical centre plane is offset from the near-side contact line by half the track (0.7–1.0 m). The f52 tips intersected with it give
  L = 5.56–5.68 (5.62 at 0.85).
- Consistency: with a centre origin about 0.7 m above the ground, this ground geometry reproduces the taxi's given f38 depth
  (16.549) to within 0.5% (scale 0.995–1.003). A ground-level origin would be 2–3% off. Scale-corrected L ≈ 5.59–5.62.

## Result and confidence
The routes give 5.59–5.72; the answer is 5.62 m. As a sanity check, a Ford Crown Victoria is 5.39 m with a 2.91 m wheelbase.
The measured wheelbase of about 3.0 m implies a model scale of about 1.03, which predicts about 5.55–5.65 m. The main uncertainty is f (about ±5%).
Under the alternative reading of length as the world-axis bounding box of a rotated car, the value would be larger, but the car is
not axis-aligned while turning, so I used the car's own length.
