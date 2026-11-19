# q_1068 – cart wheel diameter

The file and the question both run at 24 fps. The "nest" in depth_info is the black furry ball (`fur_ball`) in scene/.

## Wheel pixel size
I read the wheel on frame 72 from a zoomed grid crop (frames/wheel.png). It spans x ≈ 1337–1523 and y ≈ 1062–1240/1248, about 185–192 px across. The record gives 192 × 186. I use 188 ± 5 px.
The wheel centre is at (1431, 1153), 471 px off-axis, so the cart's forward depth is ≈ 27.562 / 1.004 ≈ 27.45 m.

## Scale: the gravity prior failed, so I used standard objects
- Gravity route (fit_fall.py): the nest's vertical pixel acceleration during the clear fall (frames 39–48) is only ~6 px/frame² (~3500 px/s²). If that were 9.8 m/s² free fall at a depth of ~5 m, then f ≈ 1200–1800 px. That focal length makes the barn door ~7–10 m tall, the barn eaves ~11–15 m, the nest ~0.8 m wide and the wheel ~3–4 m: implausible by far more than 40 pct.
  The nest also detaches gradually (it slides through the branch, frames 17–34) and is a soft body, probably with drag. Its fall time and acceleration are therefore not free fall, and the 3D parabola fit is degenerate. Conclusion: the gravity prior gives no usable scale here.
- Standard-object route: the house depth is 55.767 m to the house origin, so the barn front is at ≈ 52–53 m.
  - Door opening, 222 px, if 2.2 m tall: f ≈ 5300
  - Barrels, ~95 px, if 0.9 m tall: f ≈ 5500
  - Eave wall, 322 px, if ~3.2 m tall: f ≈ 5300
  - Front wall, 544 px, if ~5.5–6 m wide: f ≈ 5000

  I adopt f ≈ 5300 px (horizontal FOV ≈ 20°). Checks at this f: the nest is ≈ 220 × 5.66 / 5300 ≈ 0.24 m (realistic). Using the horizon from the ground contacts (v ≈ 1100, consistent with the far hill line), the camera height comes out ≈ 0.75 m.

## Answer
Diameter = 188 × 27.45 / 5300 ≈ 0.97 m. The f range 4850–5800 gives 0.89–1.06 m, a realistic cart wheel.
Confidence: moderate. The scale comes from the sizes of standard objects (door, barrels, barn), not from the gravity prior, which is inconsistent with a real-scale scene.
