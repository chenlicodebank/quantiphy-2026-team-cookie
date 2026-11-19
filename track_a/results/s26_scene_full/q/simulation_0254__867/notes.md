# q_867 — acceleration of the tennis ball at t = 0.5 s (prior: diameter 0.17 m)

**Answer: 6.17 m/s²**

Time base: fps = question_fps = 24, so no re-timing was needed.

## Situation
- At t = 0.5 s (frame 12) the ball is still above the top of the frame. It enters at frame 18 and rolls down a straight ramp until frame 47. The acceleration at 0.5 s is therefore the ramp's constant acceleration.
- In 3D the speed extrapolates to zero at t ≈ −0.02 s, so the ball was released from rest at t ≈ 0 and was on the same ramp at 0.5 s.

## Key finding: perspective, not a planar scene
- With a single scale, the pixel acceleration falls along the ramp from about 806 to 616 px/s² (first half vs second half).
- A projective constant-acceleration line model, `u = A + s/(1+Cs)` with `s = v0 t + a t²/2` (models.py), fits the path to 0.20 px rms. A planar constant-acceleration fit leaves 1.75 px rms.
- The model's implied depth ratio from frame 19 to 47 is 1.080. Two independent checks agree with it:
  - the ball's pixel diameter shrinks by 1.06–1.09 over the same frames (diam_rgb.py, diam_grad.py, diam_blue.py);
  - the line's vanishing point, about (14170, 13483), matches the intersection of the two ramp-strip edges, about (14790, 14090).
- So the ball recedes from the camera while it accelerates uniformly. A velocity-damping model fits about as well (0.22 px rms), but it does not account for the measured shrink in diameter.

## Measurements
- **Ball diameter (depth-only, referred to frame 19):** 25.0 px.
  - Taken from the steepest blue-channel gradient on 144 rays, using frames 35–39 near the image centre, where off-axis elongation is negligible. Each frame is multiplied by the kinematic depth factor.
  - RGB half-level gives 25.15 px. Blue half-to-core gives 24.3 px, which is biased low by the darker limb.
- **3D reconstruction (world3d.py):** `Z_i = f·0.17/D19·zf_i`, with `X, Y = (u − c)·Z/f` and the principal point at the image centre.
  - Speed rises linearly and both halves agree within 0.1%.
  - a = 6.08 / 6.13 / 6.17 / 6.22 m/s² for f = 1500 / 2000 / 2667 / 3500 px, after rescaling to D19 = 25.0.
  - The weak dependence on f is expected: the depth term (proportional to f) and the off-axis lever (proportional to 1/f) cancel to first order.
  - f itself is weakly constrained. The off-axis shape of the ball favours f ≳ 2000 px, and I used 2667 px (a 50 mm lens on a 36 mm sensor).

## Second route: scale check with gravity
- The free-flight hop after the floor impact (frames 49–54) gives 1347 px/s². At the floor diameter of about 23.1 px that is 9.9 m/s², close to g = 9.81.
- This confirms that the prior-based scale is consistent with the scene's physics.

## For comparison
- Naive single-scale planar estimates give 5.0–5.6 m/s². They are biased low because of the perspective recession.

## Confidence
- The main uncertainty is the edge definition of the pixel diameter, about ±2%, plus about ±1% from f.
- Estimated accuracy: about ±3%.
