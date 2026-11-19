# q1138 – height of the curb (m)

Answer: **0.25 m** (curb face 35.5 ± 1.5 px at ≈0.0070 m/px; routes give 0.242–0.249 m).

File fps 30.005 vs question fps 30 (negligible; frame indices used, 30 fps for time).

## Scale (prior: orange car acceleration −2.86 m/s²)
- track2.py: masked (orange-pixel) matching of the car between consecutive frames → per-frame shift
  37.5 px (f1) → 12 px (f53), linear in frame (rms 0.34 px); fitspeed.py: −0.515 px/frame² = 463 px/s²
  (sub-windows 458–469). The record's front-bumper fit (347) is biased by blur; rear/axle tracks agreed (460/471).
  → s_side = 2.86/463.1 = 0.006176 m/px at the car's near side.
- Camera NOT level (record assumed level): LSD facade vertical segments converge to a VP 23,343 ± 570 px above
  the principal point (vp.py / model.py) → pitch up ≈3.9°, horizon ≈ row 646.
- Focal length: car d(t=0)=12.048, d(t=1)=10.432 with pixel positions (u0≈1485, u1≈544) → z_o/f ≈ 0.0063–0.0064,
  f ≈ 1577–1627 depending on origin u/v. Consistency of lamp/hydrant distances (12.325/12.565) with the car-based
  road/sidewalk planes is best at f ≈ 1570 (Z_curb from both routes 11.32 vs 11.35 m).

## Curb pixels (frame 0, joints.py, curbprof.py)
- Curb joints at x = 72, 361, 649, 936: slanted (horizontal sidewalk) above ~901, vertical from ~902 to ~935.
  Row profile: edge at 902 (sidewalk → curb face upper light band), 907/908 light→dark granite, bright/dark crease 937/938,
  then lighter gutter strip 939–945 (road plane), dark asphalt ≥ 947, lane line 956–960.
- Face: top ≈ 901.5, bottom ≈ 937 → 35.5 ± 1.5 px. (Record's "905–945" was corrected.)

## Height (model.py, full pitched pinhole)
- Route A (car → road plane via tyre contact v=982 → curb foot → vertical face): c = 0.242 m for 902→936.5 (34.5 px),
  nearly independent of f (0.240–0.243 for f 1450–1650).
- Route B (lamp/hydrant distance → sidewalk plane → curb top edge depth → face): 0.242–0.245 at f=1570.
- Check: camera height above road minus above sidewalk (no curb pixels used): 0.238 m at f=1570 (0.25 at f≈1590).
- Scaling to 35.5 px: ≈ 0.249 m → answer 0.25 m.

Confidence: moderate-high (±5%), dominated by the exact face edges (±1.5 px ≈ ±4%).
