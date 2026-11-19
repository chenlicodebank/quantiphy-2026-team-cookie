# q1611: height of the table lamp (simulation_0212, 3D render, 24 fps; file rate = question rate)

Answer: **0.69 m**

## Lamp in pixels (lamp.py, frame 49, static object)
- Shade top edge at y ≈ 398.5–399 (row profile), base bottom at y ≈ 661 (dark contact line 660–662, then the table top).
  That gives 262 px (the record said 398–660, which agrees). Lamp axis is at x ≈ 1369.

## Focal length (focal.py): from the prior (cat speed 0.94 m/s) and the cat's depths
- Cat core centroid at f0 (408.5, 842.7) with d = 4.199 m and at f24 (869.4, 805.3) with d = 4.481 m. Back-projected
  with principal point (960, 540), |P24 − P0| = 0.94 m (1 s × 0.94) when **f ≈ 2150 px** (mask centroid 2148,
  f23-extrapolated 2152, bbox centre 2100–2110). That is a horizontal FOV of ≈ 48°.

## Lamp depth (floorfit.py, lamp3d.py)
- Floor plane: I fitted the camera pitch and height to the cat paws (f0), the dog's front paws (f0) (each put in the
  animal's vertical path plane), the mirror bottom centre (6.407 m, pixel (1517, 817)) and the closest bench-leg
  floor contact (1408, 841) at the leg origin's depth (5.69 m). Result: pitch ≈ +0.44°, camera height ≈ 0.735, all
  seven floor points agree to within ±2 cm. The front-left leg's floor contact comes out at a distance of 5.72 (the
  leg origin is 5.69), which is consistent.
- Rear-left leg (1331, 827) and right leg (1626, 822) were put on the floor. The lamp column (x = 1369) meets the
  table's front-back midline at the left end (midpoint of the two left legs) at camera z = 5.70 (distance 5.81 m).
  This value is insensitive to f and to the pitch model: an earlier floor-only model with pitch 1.7° also gave
  z = 5.707.
- The lamp's base is 0.46 above the floor. The table is about 0.79 long and 0.32 front to back, which is plausible.

## Height
- World-vertical extent between rows 399 and 661 on the vertical through the lamp foot: 0.695 m at f = 2150
  (0.710 at 2100, 0.680 at 2200).
- Rim correction: the camera (height 0.735) is below the shade top (about 1.15) and above the base (0.46), so the
  image top and bottom are the near edges of the rims. Correcting for this removes about 3 px, giving
  259.5/262 × 0.695 ≈ **0.688 m**.

## Checks
- Simple route: 262 px × z 5.70 / f 2150 = 0.695, which matches the full 3D route.
- Floor consistency across independent references (paws of both animals, mirror and leg) holds to within 2 cm.
- The main uncertainty is f (±2–3 %, from the choice of the cat's reference point). Lamp placement off the midline
  by ±5 cm changes the result by < 1 %.
- Confidence: moderate to good, about ±4 %.
