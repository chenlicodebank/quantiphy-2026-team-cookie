# Q1608 – height of the wooden bench (m)

The "wooden bench" is the reddish-brown slatted bench/side table on the right, which the scene record calls `side_table`.
File fps = question fps = 24.

## Focal length (focal.py)
The prior gives the cat's speed as 0.94 m/s, so it moves about 0.94 m over 24 frames. The cat's depths are 4.199 m at f0 and 4.481 m at f24.
I back-projected the cat's core centroid at f0 (408.5, 842.7) and f24 (869.4, 805.3), with the principal point at the image centre,
and solved for |P24 - P0| = 0.94 m. This gives f = 2156 px. Other reference points give: core f0 to an extrapolated f23 = 2158, centroid = 2147, bbox centre = 2099.
I used f ≈ 2150 px (HFOV about 48°).

## Bench pixel extents (bench.py, edges.py, slab.py, zoom*.py; median background of frames 30–49)
- Closest leg (front-left) foot bottom: y = 840.5 at x ≈ 1405. The rear-left foot is at y 826 and the right foot at y 821.5.
- Top slab: the back-edge silhouette is at y ≈ 652.5. In the overhang columns at both ends, the slab spans 658.4–665.6
  (left end) and 655.5–663.3 (right end). So the front-top edge is at about 658.4 at the left end and 656 at the right end.
  Above the front-left leg (x 1405) it is about 657.7. The slab's front face is about 7 px thick, and below it is the apron.
- Pixel height at the closest leg: 840.5 − 657.7 ≈ 183 px.

## Scale and height
The closest leg is 5.69 m from the camera. At the leg pixel, Z/f = d/|ray| = 5.69/2209 ≈ 0.00257 m/px.
H = 182.8 × 0.00257 − 0.0016 = 0.468 m. The 0.0016 m term corrects for the top front edge being about 3 cm behind the foot,
because the legs splay: the top is about 0.22 m deep while the feet span about 0.28 m front to back.

## Checks
- Floor and camera height: the camera height above the floor, with no pitch, is 0.772 m from the leg foot (5.69 m),
  0.789 m from the mirror's bottom centre (6.407 m, pixel about (1500, 815)), and 0.78–0.785 m from the cat's paws at f0 and f24.
  These agree, so the pitch is about 0°.
- Second route: the top height from the floor model, Hc − (v_top − cy)·Z_top/f = 0.772 − 0.303 = 0.469 m.
- Sensitivity: if the front-top edge were read as y 664 (the bottom of the slab face) instead of the top, H would be 0.453 m.
  Each 2.5 % change in f moves H by about 2 %.

Answer: 0.468 m (likely within about ±3 %).
