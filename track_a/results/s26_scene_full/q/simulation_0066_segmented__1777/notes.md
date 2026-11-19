# Q1777 — width of the purple car (m)

The purple sedan is static, in the lower-left foreground, side-on, and cut by the left edge. Its depth is not given, so I calibrated the full camera from the moving objects and then measured the car on the ground plane. The file rate and question_fps are both 24. Depth frames: t=0.58 → frame 14, t=1.58 → frame 38.

## Camera (calib.py, vanfit.py, roll0.py, purple.py)
- Pinhole model with the principal point at the image centre. Origins are the 3D points back-projected with depth_info: the van and cyclist use their mask centroids. The pedestrian pelvis was read on zoomed crops (f14 (437,430), f38 (367,438)), because the f14 mask is missing the legs.
- **Prior (white van, a = 4 m/s²).** The van's per-frame positions come from intersecting rays with its 3D line, fitted over frames 0–40 (the clean part). It starts from rest at t0 ≈ 0. The fit gives a = 4 at f ≈ 860 and a = 3.89 at f = 960; the acceleration depends only weakly on f.
- **Roll 0 (look-at camera).** Pitch is chosen so the motion is horizontal. The van and pedestrian motions agree at f ≈ 960 px, pitch 28.0°.
- **Camera height.** The ground point under the pedestrian pelvis (between the feet, f38) gives Hc ≈ 7.1 m. The pelvis is then 0.66 m above the ground and the van origin 0.71 / 0.70 m at both frames (consistent).
- **Independent check.** The purple car's axis, taken from its two near-wheel ground contacts, comes out exactly perpendicular (90.0°) to the van's road at f = 960 / pitch 28. That is what you expect for world-axis-aligned parked cars. The wheelbase is 2.87 m (plausible for a large classic sedan).

## Width (width.py)
- **Near side.** The near-side body plane is the vertical plane through the tyre ground contacts (rear (157,896.5), front (507,800)), moved δ = 0.05 m outward.
- **Shoulder height.** The near hood shoulder (hood-to-fender brightness edge, from prof2.py) at x = 460–500 is intersected with that plane, which puts it at h ≈ 0.73 m.
- **Far side.** The far hood shoulder is the top silhouette at the same longitudinal position and the same height.
- **Results:**
  - Width at the rear of the hood (x 460–500, widest): **1.79–1.80 m**.
  - It tapers to 1.72 / 1.65 toward the nose (x 520 / 540).
  - Sensitivity: f 860–1000 gives 1.77–1.80; f 1100 gives 1.73–1.78. δ from 0 to 0.15 changes the result by only ±0.02.
- **Second route (bumper.py).** The front chrome bumper's near and far ends are at the same height (0.48 m). They give 1.60 m. This is consistent with the taper measured at the very front, so it is a lower bound on the body width.

## Answer
The width is the AABB horizontal extent across the car, so I take the widest body section: **1.80 m**. Real-world sanity check: a classic large sedan (W126-like) is 1.82 m wide with a 2.9 m wheelbase.

Confidence: moderate. The likely error is about 5%. The main risks are mirrors (if the mesh has them, they would widen the AABB) and the focal-length / pitch calibration.
