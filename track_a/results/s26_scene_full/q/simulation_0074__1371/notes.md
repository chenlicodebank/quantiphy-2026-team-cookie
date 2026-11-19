# q1371 – average speed of the bicycle (frames 0-71), simulation_0074

File fps = question_fps = 24, so frame = round(t*24): t=0.58 -> frame 14, t=1.58 -> frame 38.

## Focal length (vp.py)
- I fitted the road kerb edges in code (beige/grey transition plus RANSAC line fit, rms about 0.5-0.8 px):
  L1 y=0.24295x+54.87, L2 y=0.42606x+296.82 (road A); R1 y=-0.38522x+772.78, R2 y=-0.87654x+2096.36 (road B).
  The near-side kerbs L3 and R3 lie on the same lines as R1 and L1, which confirms the fits.
- Vanishing points: VA=(-1321,-266), VB=(2694,-265). The horizon is level (no roll).
- Assuming the two roads are perpendicular and the principal point is the image centre: f = sqrt(-(VA-c)·(VB-c)) = 1796 px.
- Check 1 (taxi_dir.py): at f=1796 the 3D displacements from depth_info (frames 14->38) put the pedestrian
  walking 1.5 deg off road A (along the sidewalk) and the cyclist at 90.1 deg (along road B). The vertical components
  are about 0 for both. At other f values these angles drift away.
- Check 2 (vanbox.py, rough): a 6 x 2.1 x 2.2 m box for the white van projected at f=1796 comes out about 10% larger
  than the van's mask bbox. A rounded van body is expected to fill less than its box, so this is consistent but only loosely.

## Bicycle speed (cyc_speed.py, cyc_fit.py)
- Depth route: P = d * unit ray(u,v) at frames 14 and 38 (d = 28.6001, 24.5118).
  |P38-P14| = 5.381 (centroid) / 5.360 (bbox centre) / 5.356 (bottom) m over 1.0 s. The result hardly depends on the reference point.
- Constancy check: I intersected the per-frame rays with the horizontal plane at the origin height, then fitted
  position against time. With the bottom point: v = 5.42 (frames 21-40), 5.51 (40-61), 5.43 (0-61), with acceleration
  about 0. The lateral scatter is 5 cm, so the cyclist rides a straight line at constant speed.
- Frames 62-71: the van hides the cyclist, and frames 0-20 come from a template track. Constant speed is assumed there.
- Average of the per-frame speeds ≈ 5.36-5.45 m/s. Answer: **5.4 m/s**.
- Sensitivity: f ±10% changes the answer by about ∓5%. Confidence: fairly good (±5%).
