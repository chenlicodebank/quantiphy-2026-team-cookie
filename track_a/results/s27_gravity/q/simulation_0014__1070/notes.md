# q1070 – maximum height of the cart above the ground (m)

File fps = question_fps = 24. The cart is static; its maximum height above the ground is the top of its bounding box, which is the top
corner of the tilted box at the back end. The wheel and shafts rest on the ground.

## Pixel measurement (frame 72, zoomed crop frames/cart.png, 20 px grid)
- Top of the cart box at y ≈ 1018; wheel/ground contact at y ≈ 1247–1248, so the height is **≈ 230 px** (the scene record gives 231 px and I agree).
- Cart depth (given) is 27.562 m. With the cart ~380 px right of and ~150 px below the image centre, the off-axis correction is < 0.5 %.

## Focal length
1. Gravity route (fit.py): I fitted a parabola to the nest's back-projected vertical position over frames 26/30/34/38–48. Depth was
   taken from the given 5.630 m at t = 1 s, and the landing depth (≈ 4.5 m) from the ground-plane relation between the cart and the barn.
   To get a = 9.8 m/s² this needs f ≈ 1600–1700 px. That f would make the cart 3.9 m tall, its wheel 3.2 m, the barn door ~7 m and the
   nest 0.75 m wide. All of these are implausible by far more than 40 %. The nest is a soft body sliding and sagging off a branch, and its
   pixel acceleration is only about 1/3–1/4 of free fall at a realistic scale. So the clip's motion does not give a usable 9.8 m/s² scale.
   It looks damped or slowed by about 2x.
2. Standard-object route (used): each object gives a focal length, and they agree:
   - the cart wheel (192 px at ~27.5 m, assumed 1.0–1.3 m): f ≈ 4100–5300;
   - the barn door opening (228 px at ~51 m for the front wall, assumed 2.2–2.5 m): f ≈ 4650–5300;
   - the barrels (95 px, assumed ~0.9 m): f ≈ 5400;
   - the nest (219 px at 5.66 m, assumed ~0.25–0.3 m): f ≈ 4100–5000.
   I took **f ≈ 4800 px** (horizontal field of view ≈ 23°).

## Answer
Height = 230.5 px × 27.46 m (forward depth) / 4800 ≈ **1.32 m**. The plausible range of f gives 1.1–1.45 m.
As a check, the same f makes the wheel 1.1 m and the nest 0.26 m, both realistic.
Confidence: moderate. The scale comes from standard object sizes, not from the gravity prior, because the prior's motion route gives an
unrealistic scene.
