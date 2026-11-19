# q_731 — paper airplane speed at t = 1.25 s

The video and the question both run at 24 fps, so t = 1.25 s is frame 30. The speed is |p(30) − p(29)| × 24.
Prior: the chalkboard is 5 m long. This is a 2D scene, so one metres-per-pixel scale comes from the chalkboard.

## Scale (board.py, measure.py, SAM)
- Outer edges of the chalkboard including its wooden frame, from intensity profiles in frame 30: x ≈ 320.5 to ≈ 1690.5,
  so **≈1369 px** wide. The scene record gives 320–1692 (1372 px). The SAM "chalkboard" mask box spans 324.2–1690.3
  (1366 px). All three agree within 0.5 %.
- The inner green writing surface is 341.5–1670.5, so 1328 px wide (3 % smaller).
- I take the board object to be the whole board including its frame: 5 m / 1369 px = 0.003652 m/px.

## Plane displacement from frame 29 to 30
| method | step (px) |
|---|---|
| own background-difference mask: centroid | 61.4 |
| own mask: midpoint of the main-axis extent | 62.2 |
| own mask: bbox centre | 62.3 |
| SAM mask centroid (1412.0,399.2 → 1470.0,417.8) | 60.9 |
| SAM bbox centre | 61.2 |
| scene track ref point | 62.8 |

- Neighbouring steps from my own midpoint: 65.2, 63.7, 61.8, **62.2**, 59.5, 58.6. These fall smoothly as the plane
  slows, and a trend fit gives ≈61.5 at frame 30.
- I use **61.8 px/frame**, with an uncertainty of about ±1 px.
- My mask and the SAM mask differ by less than 3 % in both length (140.3 vs 141.3 px) and centre, so no conflict needed
  resolving. The overlay is in frames/plane30_mask.png.

## Result
61.8 px × 24 fps × 0.003652 m/px = **5.42 m/s**.

- Second route: the SAM centroid step (60.9 px) gives 5.34 m/s, and the scene track's step gives 5.50 m/s.
- If the "length" meant only the green surface (1328 px), the answer would be 5.58 m/s.

Confidence: good, about ±3 %. The main doubt is whether the board's length includes its frame.
