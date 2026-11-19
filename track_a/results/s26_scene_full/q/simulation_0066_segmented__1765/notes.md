# q_1765: length of the white car (the white van), in metres

**Answer: 5.78 m.** Plausible range is about 5.70–5.86 m.

The file and the question both use 24 fps. Frame i is at t = i/24. The white car is the white van (`scene/tracks/van.csv`). It is the only white vehicle that moves.

## Scale: from the prior (a = 4 m/s²)
- The camera is static. The van moves in pure translation along a straight line, so every point on it moves along an image ray from one focus of expansion (FOE).
- I tracked 231 KLT features on the van (`track_feats.py`) and fitted the model x_k(t) = e + A_k / (1 − s(t)/z_k), with s(t) = ½·4·(t − t0)². The fit is `fit_foe3.py`.
  - z_k is the distance (in metres along the path) that feature k still has to travel before it reaches the camera's image plane. It needs no focal length.
- Fit results: e = (620.5, 78.4) px and t0 = −0.038 s. Residual is 0.54 px median over 174 features.
  - `t0_profile.py`: t0 stays at −0.038 for fit windows ending at frames 50, 60 and 72.
  - A free-v0 model gives the same s(t), with v0 = 0.15 m/s.
- Check that needs no focal length (wheelbase):
  - Both wheel hubs and the FOE are collinear in the image.
  - The front hub reaches the rear hub's frame-71 image position (1458, 705) at frame ≈ 63.3. So WB = s(71) − s(63.3) ≈ 3.64 m.
  - The feature model predicts ≈ 3.72 m from the image-distance ratio of the two hubs and the rear-wheel feature z. They agree within the timing uncertainty, so the kinematic scale holds.

## Focal length
- Mirror-image pairs on the front (left/right windshield corners) must line up across the van's direction of travel. The top corners give f ≈ 923 px and the bottom corners give f ≈ 1088 px (`sym_f.py`).
- With f ≈ 1000, the taxi origin computed from its depth_info stays at constant height (0.00 m change). It sits about 0.26 m below the van's lower-bumper feature, which fits vehicle origins at ground level (`heights.py`). The cyclist also stays at constant height.
- I used f ≈ 1000–1050 px (horizontal FOV ≈ 92–94°).
- The van's own depths (23.589 m at frame 14, 19.990 m at frame 38) agree in absolute value with the reconstruction to 1–2% when the origin is at the van's centre and on the ground. Their ratio, however, implies a 3.60 m depth change against about 3.95 m predicted, and no f or origin position fits both depths exactly (`origin_solve.py`).
  - I treated this as a limitation of the depth data, not of the scale. The images reject a later t0 strongly (the fit error doubles).
  - If the scale were taken from the depths instead, the length would be about 1.5% shorter (≈ 5.71 m).

## Length (bounding-box extent along the direction of travel)
- **Route 1: van-frame reconstruction** (`vanframe.py`, `sideplane.py`).
  - Front reference: the lower-bumper centre features 126/173.
  - Rear end: van-mask pixels in frames 68–71, intersected with the van's near-side plane. At low height (the rear bumper end) this gives 5.83 m at f=1000, 5.79 m at f=1050 and 5.76 m at f=1100.
  - `rear_check.png` overlays the grid on the rear silhouette as a visual check.
- **Route 2: same-line check, no f needed for the main part** (`sameline.py`).
  - Feature 150 (the near front corner under the headlight) and the rear silhouette lie on the same FOE line.
  - Their separation along the path is 5.47–5.52 m over frames 66–71 (mean ≈ 5.48 m).
  - Feature 150 is 0.27–0.30 m behind the bumper centre (f = 1000–1100). That gives L ≈ 5.76–5.78 m.
- The bumper face may protrude 0–5 cm beyond the tracked bumper features. With that, the final answer is **5.78 m**.

**Confidence:** fairly good, about ±3%.
- The main uncertainties are f (≈ ±1.5%) and t0 / the depth inconsistency (≈ ±1.5%).
- I assumed the van's world bounding box is aligned with its heading.
