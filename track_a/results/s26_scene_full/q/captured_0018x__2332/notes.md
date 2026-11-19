# q_2332 — height of the right person (cm)

The right person is the near one (depth 2.002 m). The video and the question both use 24 fps.
Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).

## Problem
Her head top is at y = 102. This was measured in code over 13 frames, where the first 8 give 102, and the
values are consistent through the video. Her front foot is cut off by the bottom edge of the image at 719, so
the plain bbox (618 px, about 162 cm) is wrong. Her back foot's sole is at about y 672.

## Main route: floor row from the scene geometry
- The left person (depth 3.130) has her feet at y = 577. With a level camera, that puts the camera
  (577-360)*3.13/762.8 = 0.890 m above the floor. Her height comes out at 1.658 m, which is plausible.
- At the right person's depth of 2.002 m, the floor row is 360 + 762.8*0.890/2.002 = 699.3. This lies
  between her back-foot sole (672) and her cut front foot (>720), which is consistent.
- Height = (699.3 - 102) * 2.002 / 762.8 = **156.8 cm**.

## Checks (scripts: fall.py, height.py)
- The camera is level and cy is about 360. Fitting free fall with g = 9.8 (using the dropped capture frame at
  35→36 noted in the record) puts the tennis ball at Z ≈ 2.65 m. Its landing bottom row is 616, and the
  predicted floor row at 2.65 m is 360 + 763*0.89/2.65 = 616, an exact match. The soccer ball and box come out
  at Z ≈ 3.19 and 3.25 m and land at rows 577 and 602, near the left person's feet. This also fits a level camera.
- Head height route: her head top is 0.677 m above the camera axis. Adding the camera height of 0.890 m
  gives 1.567 m.
- Not used: top to the cut image bottom gives 162.2 cm, which is only a lower bound for her standing
  footprint and is biased by the front foot.

Confidence: moderate-high. The main uncertainties are about ±1-2 cm from the depth reference point and ±5 px
in the floor row.
