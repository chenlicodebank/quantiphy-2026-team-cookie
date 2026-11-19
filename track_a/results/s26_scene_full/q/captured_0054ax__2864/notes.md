# q2864 – distance orange ball (basketball) ↔ soccer ball at t = 1.0 s (frame 24)

Lab clip, 24 fps (file and question rates are the same), f = 0.5959·1280 = 762.8 px, principal point (640,360).
The orange ball is the basketball. The depth_info's "white"/"green" balls (about 3.04–3.07 m) are the two small
thrown balls: at that distance the soccer ball would have to be about 0.27 m across. So **the soccer ball's depth
is not given** and has to be estimated.

## Measurements (scripts: measure.py, soccer.py, answer.py)
- Basketball circle fits (orange-hue mask): f12 is at (343.9, 606.3) with diameter 75.1 px, so its real diameter is
  2.3557·75.1/762.8 = 0.232 m. At f24 the ball is cut by the bottom edge. The fit there is (585.4, 680.5) with diameter 91.4;
  with the diameter that 1.81 m implies (97.7 px), the centre would be at v = 683.7. Both were tried and they differ by less than 1 mm in the answer.
- Soccer ball: the scene record's circle of about 70 px included the hand. I re-fitted it on the lower outline against the
  green screen only (angles 15–175°, outliers removed). At f24 it is at (145.5, 608.8) with diameter 61.4 px; at rest
  (f0–22) the diameter is 60–62.5 px. The overlay is in frames/sbfit24.png.
- P_basket(1.0 s) = back-projection with the given 1.81 m = (-0.119, 0.70, 1.665) m.

## Soccer-ball depth: two routes
1. Floor plane: I fitted the plane of ball centres through the basketball's 3D centres at f12 and f24 (the given depths),
   assuming zero camera roll. The camera comes out about 0.78 m above the ball-centre plane (about 0.9 m above the floor) with
   about 3° of pitch. A cross-check gives the standing person (feet at y≈542) a depth of about 3.8 m and a height of about 1.7 m,
   which is plausible. The soccer-ball ray meets the plane lowered by (R_b − R_s) at 2.60 m, so the distance is **1.32–1.34 m**.
   This implies a soccer-ball diameter of 0.209 m, which is consistent with a real size-4/5 ball.
2. Assumed ball size: 0.205 / 0.215 / 0.22 m with 61.4 px gives a depth of 2.55 / 2.67 / 2.73 m and a distance of 1.28 / 1.37 / 1.42 m.

The two routes agree at a diameter of about 0.21 m. **Answer: 1.33 m.**

## Caveats
- The basketball depths in depth_info are a little inconsistent with its pixel size: the size implies 1.94 m at f24, not 1.81.
  The given values were used.
- The prior (2.21 m/s at 0.5 s) is not reproduced well: my smoothed speed is about 1.6–1.9 m/s, and the raw f11→f12
  step gives 3.0 m/s. The prior was not needed for the distance.

Confidence: moderate, roughly ±7%. The main uncertainty is the soccer ball's depth.
