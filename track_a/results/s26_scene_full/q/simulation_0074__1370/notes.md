# Q1370 – length of the purple car (m)

Prior: white car (the van) length = 6 m. depth_info for human, taxi (yellow car), van (white car) and bike at
frames 14 and 38 (t = 0.58 s and 1.58 s, at question_fps = 24, which is also the file's rate). The purple car is the parked dark-purple
sedan (static, frame 0 used; unoccluded). It is a 3D scene with a static camera.

## Camera calibration (no assumed size)
- `lines.py`: RANSAC/SVD fits of the four straight kerb edges of each road (Canny edges in bands). Each road's
  two kerbs are collinear across the junction, so there are 2 clean lines per direction.
  VP_A = (-1312, -264), VP_B = (2683, -256). The roads are perpendicular, so f^2 = -(vA-c)·(vB-c), giving **f = 1787 px**
  (HFOV 62°). Camera pitch is ~24° down (`calib.py`).
- Independent check (`poles.py`, `vz2.py`): the vertical VP from 6 poles is (1078, 4552). Combined with the horizon or with
  either VP it gives f = 1788 / 1791 / 1794 px, so the calibration is confirmed. (The right signal pole and the short far-centre pole fit poorly and were left out.)

## Metric scale = camera height H above the ground
- Depth route: the van at frame 14 (mid-wheelbase ground point) needs H ≈ 9.55 (origin at ground) to 9.65 (origin
  ~1 m up) to reproduce 31.28 m. The taxi at frame 38 gives H ≈ 9.48–9.55. The pedestrian (feet on the ground, pelvis vertically
  above, |pelvis| = depth; `ped_h.py`) gives 9.72 (f14) and 9.52 (f38). Best value: H ≈ 9.58 ± 0.1.
- Prior route (van = 6 m, `veh_len.py`, `probe.py`): at H = 9.5 the van measures 5.78 m from the front-bumper centre
  to the rear corner on the visible side. The rear bumper adds ≈0.1–0.2 m, giving ≈5.9–6.0 m, so H ≈ 9.5–9.66. This agrees.
  Its wheelbase is 3.67 m, which also fits a 6 m Express-style van.

## Purple car
- Its long axis is parallel to road A: the line through its wheel contacts is within 0.7° of A.
- Visible-side plane is from the wheel ground contacts (452,365) and (558,401.5).
- Rear near corner (408,325) and front near bumper corner (576,380) are intersected with that plane. They come out at
  heights 0.45 m and 0.49 m, which is plausible for bumpers. The front-bumper points across the face all give the same
  L (22.6 m), so the bumper centre does not protrude.
- Length at H = 9.5 is 4.67 m (4.64 m if the body side is 0.1 m outboard of the tyre contacts). Scaled to H = 9.58,
  that is ≈4.68–4.71 m. With the bumper-height plane method instead: 4.56–4.62 at h = 0.45–0.5 (corner heights are known, so the side-plane value is preferred).
- Second route (ratio to the van measured the same way): 4.67 / 5.93 × 6 ≈ 4.72 m.
- Sanity check: the model looks like a Mercedes W123, which is 4.725 m long in reality.

Answer: **4.70 m**. Estimated uncertainty is about ±3% (from the corner pixels ±1.5 px and H ±1%).
