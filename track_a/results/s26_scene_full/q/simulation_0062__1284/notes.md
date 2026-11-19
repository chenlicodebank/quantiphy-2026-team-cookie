# Q1284 – length of the turning yellow car (taxi)

File fps 24 = question_fps 24, so frame = round(t*24). The taxi depth is given at t=0.58 s, which is f14.

## Focal length (focal.py)
- The white van moves at constant image size and constant y, so it stays at a constant depth Z.
- Its two given depths (30.065 m at f14, 29.307 m at f38) and its centre pixels (u=516.4 at f14, u=860.0 at f38) solved
  d = Z*sqrt(1+((u-cx)^2+(v-cy)^2)/f^2) for both unknowns: **f = 2256 px, Z_van = 29.16 m**. The answer hardly
  depends on the origin's v (f moves by about 1 px).
- Check against the prior: a quadratic fit to the van's x track gives 307.2 px/s^2, and 307.2 * Z/f = **3.97 m/s^2**
  against the prior's 4 (0.7 % off). So f is confirmed.

## Taxi extent (crops.py, 4x crops of f8–f14)
- Over f10–f14 the front bumper (888.75 → 938) and the rear (trunk 416 → 465.5) both move about 12.3 px/frame.
  The extent stays constant, so in these frames the car is still side-on (yaw ≈ 0) at constant depth.
- **f14:** rear bumper extreme u = 453.5 (the trunk lid edge is 12 px further right), front bumper extreme u = 938.
  The record's bbox_x0 = 439 at f12–15 is wrong: it is stuck and interpolated. At f10 the record's x0 = 416 is the
  trunk lid; the bumper there is hidden behind the litter bin.
- **3-D box model (box_f14.py):** the car is left of the optical axis, so the leftmost point is the rear corner on the
  near side and the rightmost point is the front corner on the far side.
  - Equations: u_L = cx + f(Xc-L/2)/(Zc-W/2), u_R = cx + f(Xc+L/2)/(Zc+W/2), and Xc^2+Y^2+Zc^2 = 24.855^2.
  - Result: Zc = 24.50 m, Xc = -4.07 m, **L = 4.92 m (W=2.0) to 4.96 m (W=1.8)**. A yaw of 2° gives +0.03 m.
    A focal-length error of ±25 px gives ∓1 %. A bumper-pixel error of ±3 px gives ±0.7 %.
- If you ignore the depth spread (extent 484.5 px at the centre depth), you get 5.26 m. The near-side/far-side
  geometry matters, so the box model is the one to use.

## Second-route checks
- **Ground plane:** the van and cyclist tyre lines give a camera height h ≈ 0.95 m. The taxi's near rear tyre bottom
  at f14 is at y = 629.5, which gives Z = 23.95 m at the near-side tyre, so about 24.7 m at the centre. That agrees
  with the depth-derived 24.50 m to within 1 %.
- **f10:** the extent there (inferred bumper 404 to 888.75, 484.75 px) matches f14, which supports the yaw ≈ 0 reading.
- **Width:** the head-on width at f71 (310 px including mirrors, depth from the ground line) gives W ≈ 1.8–1.9 m.
  I used W ≈ 1.85.

## Answer
L ≈ **4.95 m**. Confidence: moderate-high, about ±3 %.
