# Q1224 – height of the curb along the road (m)

File fps = question fps = 30. Static, level camera (verticals vertical → pitch ≈ 0); principal point assumed (540, 540).

## Which curb
Two curbs: the near curb (y 859-867) shows only its top surface; its vertical face points away from the camera.
The **far curb** (by the far sidewalk) shows its vertical face as a dark band. `curbcols.py` measures the edges
column by column (19 blocks of 40 px, frames 0 and 77, all agree to ±0.1 px):
- face top edge (below the lighter ~4 px curb-top strip at 694-698): y = 699.0
- face bottom: dark band ends at 714.5, with a 1 px bright line (base edge) at 715 → bottom ≈ 715.0
- Δv = 16.0 px (15.5 for the dark band only, 16.5 if the bright line is counted).

## Scale
- Car (`carfit.py`): centre_x over frames 28-77 fits a quadratic (rms 2 px), pixel accel −394.5 px/s² (median per-frame
  −391.5). Prior −2.86 m/s² → 0.00725 m/px at the car's depth. With depth 11.671 m at t=1 (u=−83) → f ≈ 1450-1470.
  Solving both car distances (t=0 extrapolated) without the prior → f ≈ 1505-1525 (implied accel −2.77, 3 % off).
  Used f = 1475 ± 35.
- Ground plane: level camera, Z = (h·f)/(v_ground − 540). Lamp (8.901 m, origin at centre) → Z 8.75, base 898 → h·f = 3131;
  hydrant (9.207 m) → Z 8.74, base 896 → 3111; man (8.313/8.189 m, both times consistent at Z ≈ 7.75) feet 942 → 3120;
  car near wheels at 865 → Z 9.6 ≈ car centre depth 10.6 − half width 1.0 (consistent). h·f = 3120 (h ≈ 2.12 m).
- Curb depth Z = 3120/(715 − 540) = 17.8 m.

## Result
H = Δv · Z / f = 16.0 × 17.83 / 1475 = **0.193 m** (= h·Δv/(v_b − c_y)).
Range: f 1450-1510 → 0.189-0.197; Δv 15.5-16.5 → 0.187-0.199; horizon ±10 px → ±3 %.
Second-route check: the camera height from the man alone (Z 7.76 at f 1460, feet 942 → h 2.14 m) gives
2.14 × 16/175 = 0.195 m, which agrees. Sanity check: the scene is about 1.2× real-world scale (lamp 4.6 m, man ~1.95 m),
so a ~0.15 m real curb fits. Confidence: moderate (about ±5 %).
