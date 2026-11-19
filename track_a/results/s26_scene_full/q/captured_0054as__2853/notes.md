# q_2853: distance orange ball (basketball) to soccer ball at t = 1.0 s (frame 24)

File fps = question_fps = 24, so t = 1.0 s is frame 24. Lab camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).

## Identities
- The orange ball is the basketball. Its depth is given at frames 12 (2.3557 m) and 24 (1.8100 m).
- The "white ball" (3.0735 m) and the "green ball" (3.0390 m) are the two small balls just thrown by the standing
  person at frame 24 (the grey/white ball and the yellow-green tennis ball). They are about 18 px across, which is
  about 7 cm at 3 m. They are not the soccer ball, so **the soccer ball's depth is not given** and has to be estimated.

## Measurements
- Basketball circle fits use a background-difference mask (frame 0 as background) and an iterative least-squares
  circle (`ballfit2.py`). The colour-only mask in `ballfit.py` missed the dark lower half.
  - Frame 12: centre (343.4, 607.0), diameter 77.9 px. At 2.3557 m that is 0.241 m, a regulation basketball.
  - Frame 24: centre (585.1, 680.6), diameter 93.9 px (the ball is cut by the bottom edge). At 1.81 m that is
    0.223 m; the fit is probably low because of the cut.
  - Basketball position at frame 24 = (-0.120, 0.700, 1.665) m.
- Soccer ball at frame 24: the hand is releasing it and there is slight blur. Its centre is about (152, 605) and
  its diameter is about 66 px (horizontal width at rest is 65–68 px; read from zoomed grid crops).

## Soccer ball depth (`geom.py`)
1. **Floor plane.** The basketball rolls on the floor, so its centre stays on a plane. That plane passes through the
   two given 3D centres, assuming no camera roll: pitch 2.5 deg, centre height 0.77 m below the camera.
   - Check: the plane-predicted basketball distances in frames 11–21 match the size-based distances
     (0.241 m ball) to within about 3%.
   - Check: the velocity near 0.5 s is 2.1–2.3 m/s over windows that include the frame 11→12 jump (a dropped
     frame), in line with the 2.21 m/s prior.
   - The soccer ball centre ray meets the plane, raised by about 1 cm for the smaller radius, at **2.64 m**. That
     implies a soccer diameter of 0.228 m.
   - Separation from the basketball: **1.342 m**.
2. **Size.** Assuming a size-5 soccer ball of 0.22 m and 66 px gives D = 2.54 m and a separation of **1.269 m**. If
   the depth scale were the one implied by frame 24 (k = 170), it would be 2.36 m and 1.137 m. This is less likely,
   because frames 11–21 support the frame-12 scale.

## Answer
The two consistent routes give D_soccer ≈ 2.54–2.64 m. Taking about 2.60 m gives a separation of **1.31 m**.

Confidence: moderate, about ±7%. The main uncertainty is the soccer ball's depth, which is not given.
