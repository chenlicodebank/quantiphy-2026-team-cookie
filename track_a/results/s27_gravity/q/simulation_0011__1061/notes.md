# q1061: width between the two widest eaves of the house (simulation_0011)

The file and the question both run at 24 fps.

## What was measured
- The eave tips are the lower ends of the front gable's barge boards, read from zoomed crops (frames/leave.png,
  frames/reave.png, frames/house.png). Left tip x ≈ 1032 (y≈1095), right tip x ≈ 1622 (y≈1075). Width ≈ **590 px**
  (±15 px). Both tips lie in the facade plane.
- The falling "nest" is the black fuzzy object at the left tree. Its depth is 17.27/17.25 m at t = 0/1 s, so it is
  still at rest at t = 1. I tracked it (fall.py, fall2.py, fall3.py, strip.py). It is a soft body: it tumbles,
  stretches and flattens, and part of its path is occluded or motion-blurred. The parabola fits give
  a ≈ 1.4–3.0 px/frame² depending on the window, ≈ 2 px/frame² typical, so f = a·Z/(g/24²) ≈ 2000 px.

## Scale: the gravity route fails the plausibility check
With f ≈ 2000 the door (195 px) would be about 5.5 m tall, the barrels (90 px) 2.7 m, the cart wheel (172 px at
33.2 m) 2.8 m and the nest 1 m. Everything comes out about 2.5x too large. The fall is also visibly not a clean
free fall: velocity stalls around frames 43–46 and the body deforms. So the gravity prior gives no usable scale
here. Following the rule, the scale comes from standard objects in the facade plane instead:
- door leaf 195 px ↔ ~2.0 m gives 97.5 px/m
- doorway 205 px ↔ ~2.1 m gives 98 px/m
- barrels 90 px ↔ ~0.9 m gives 100 px/m (they stand slightly in front of the wall)
- I used about 97 px/m at the facade.

## Consistency check with depth_info (an independent route)
- Ground plane: the nest landing contact is at v≈1577 with Z≈17.3 m and the cart wheel contact at v≈1435 with
  Z≈33.2 m. These give a horizon at v≈1278, and the house base (v=1365) then sits at Z≈59.5 m. That fits a house
  origin at 63.6 m if the house centre is about 4 m behind the facade.
- With s = 97 px/m at 59.5 m, f ≈ 5770 px. That gives a cart wheel of about 1.0 m, a nest of 0.35 m, a bird
  wingspan of about 1.0 m, a trunk of 0.25 m and a camera height of about 0.9 m. All are realistic, which supports
  the real-scale reading.
- Eave width = 590 · 59.5 / 5770 ≈ 6.1 m. The front wall comes out at 4.7 m wide and the apex at 4.9 m high.

## Answer
590 px / 97 px/m ≈ **6.1 m**.

Confidence: moderate, about ±10%. The scale rests on assumed door and barrel sizes, and the eave tips are soft in
the image. If the gravity scale were taken literally the answer would be about 2.4x larger (≈ 14.6 m), but that
reading makes every object implausibly large, so I rejected it.
