# Q1536 – width of the blue car (light-blue canopy cart), metres

Answer: **0.96 m** (the front-to-back horizontal extent across the cart, i.e. along the camera depth axis, since the cart drives parallel to the image plane).
File fps = question fps = 24.

## Scale (3D pinhole)
- Principal point ≈ (960, 539.3) (vanishing point of the garage axis, from scene/). Camera looks horizontally.
- Yellow tyre: radial edge fits (rays.py) at frames 12 and 21 give a pixel diameter of ≈193.5 px (top 690.5–691, bottom 884; the arch hides the sides). The left-front hub is at (1652, 788) at frame 12 (t=0.5 s).
  Solving 11.38 m = |origin| with the origin 0.1 m behind the outer sidewall gives f ≈ 2762 px (HFOV 38°); with no offset, 2787. Script: solve.py.
- Blue cart tyre: at frame 38 the rear hub is at x≈955, almost on the optical axis, so the horizontal silhouette is unbiased. Its diameter is 36.75+36.25 = **73.0 px**, so the near tyre outer face is at Z_t = f·0.369/73 = **13.96 m**.
- Check: the ground-contact rows (car 884.25, cart 818.5) with camera height 1.36 m from the yellow car give a cart depth of 13.47 m, 3.5 % lower. This route does not use the cart prior, so I kept the tyre-prior value and used this one only as a bracket.

## Width (frame 0, cart front face visible at x≈1600–1710)
The cart is right of centre and drives left, so its front face is seen obliquely. For two points with the same world X, the depth ratio is Z_far/Z_near = (x_near−cx)/(x_far−cx).
- Wheels: the near front tyre's outer face has its leftmost point at 1634.5 (hub 1671, r 36.5); the far tyre's leftmost point is at 1598.5. Ratio 1.0564, so the outer-to-outer track is 0.787 m and the cart centre plane is at Zc ≈ 13.96+0.39 = 14.35 m.
- Roof front face: the far silhouette is at 1658.5 and the orange LED strip ends are at 1664.5 and 1701.5 (sharp). Taking the strip as centred, the roof half-width ratio is 722.5/698.5 = 1.0344. This predicts the near roof edge at 1708.2, and the observed shading edge is at 1707 ✓.
  Roof width = 0.0688·Zc = **0.99 m**.
- Hood front face: far silhouette 1617.5, near shading edge 1662.5. Width/Zc = 0.066, so **0.95 m**.
- The body overhangs the tyres by ~10 cm per side. The side-view offsets at frame 38 (tyre front → hood front 25 px) and the far-tyre/far-hood geometry independently give ~10 cm on the far side.
- Frames 1–3 give the same edge geometry (faceedges.py).

## Result and uncertainty
- Tyre-prior scale: roof 0.99, hood 0.95, mean ≈ 0.97 m. Ground-contact scale: ≈ 0.93 m.
- Answer **0.96 m**.
- Main uncertainties:
  - The near/far edges of rounded body corners: ±1 px moves the result by ~2 %.
  - The 3.5 % disagreement between the tyre-prior scale and the floor-contact scale.
  - Whether the roof or the hood is the widest part.
- Estimated error ±6 %. The alternative assumption that the body is flush with the tyres gives 0.89 m (unlikely, since the far side shows the overhang).
