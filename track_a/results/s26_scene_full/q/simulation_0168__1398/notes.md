# q_1398 – diameter of the bike's wheel (simulation_0168)

Answer: **0.753 m** (outer tyre diameter, i.e. the wheel's bounding-box height).

File fps = question_fps = 24, so there is no time-base issue. The camera is static (per the scene/ record).

## Focal length (two independent routes)
1. **Orthogonal vanishing points of the building corner** (`vp.py`). Brick-course orientations were measured from
   structure-tensor patches on both faces of the building. Left face VP = (-2800, 495), right face VP = (2645, 537).
   This gives f = sqrt(-(u1-cx)(u2-cx) - (v1-cy)(v2-cy)) = 2517 px (bootstrap 2515-2568).
2. **Bike trajectory consistency** (`model.py`). P0 = 28.219 m x ray(hub midpoint at frame 0), with heading = the
   right-face VP direction (the bike rides parallel to that facade/road) and speed 5.52 m/s (prior) in a straight
   line. Results:
   - the model distance at t = 0.5 s is 25.556 m (given: 25.554 m);
   - the direct |P12 - P0| = 2.763 m (expected 5.52 x 0.5 = 2.76 m);
   - with a fitted half-wheelbase of 0.52 m, the model reprojects the measured front and rear hub centres at frames
     60 and 70 to an RMS of 0.7 px at f = 2530 (2.0 px at f = 2500, 2.7 px at f = 2560).

   Adopted f = 2530 px, principal point at the image centre.

## Wheel pixel size
- Rim ellipses were fitted ray-wise to the white rim edge (`ellfit.py`).
- Tyre outer top and bottom were read from vertical intensity profiles through the hub (`prof.py`) and from
  contrast-stretched zooms (`zoomc.py`).
- Tyre outer / rim vertical ratio = 1.14 (f70 rear 1.140, f70 front 1.137, f60 front 1.142, f79 rear 1.144).
- Outer vertical extents in px: f40 F 102.6, f50 F 115.5, f60 F 128.8, f60 R 123.6, f70 F 149.0, f70 R 139.8,
  f79 R 158.5.
- The vertical extent is used because it is insensitive to the wheel's yaw: the ellipse minor/major ratio is about
  0.35-0.5.

## Diameter
D = outer_px x Z_hub / f, with Z_hub (camera-axis depth of each hub) taken from the trajectory model.

- Per measurement: 0.751, 0.758, 0.748, 0.760, 0.753, 0.754, 0.747 m.
- Mean 0.753 m, spread ±0.7 %.
- Sensitivity: f ±30 px gives ±1.2 %; the tyre ratio ±0.02 gives ±1.7 %.
- If only the rim is meant, the answer would be about 0.66 m. I take "wheel" to mean the whole wheel including the
  tyre, as for a bounding box.

## Corrections to scene/
- scene.json has no focal length; it is estimated here.
- The automatic rim fit underestimates the rear rim at frame 79 (132.9 px fitted vs 138.5 px from the profile), so
  the profile value is used.

Confidence: fairly high (about ±3 %).
