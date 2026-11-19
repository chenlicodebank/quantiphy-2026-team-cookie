# q_2015 — acceleration of the blue car (the light-blue cart) at t = 1 s

The file and the question both run at 24 fps, so t = 1 s is frame 24. The convention is a = speed(24) − speed(23) = x24 − 2·x23 + x22, in px/frame², then × 24².

## Tracking (all in code)
- `edges.py` finds two features on the cart in every frame, to sub-pixel accuracy:
  - the left (front) edge of the roof, in rows 516–526;
  - the right tip of the rear post, in rows 492–501.
  
  These are the only parts of the cart above the yellow car while it hides the cart (frames 8–31).
- `tyres_lib.py` and `fit2.py` fit circles to the lower silhouette arc of each cart tyre in frames 32–41, when the cart is fully visible. They give the hub tracks and the tyre diameter.
- The motion matches a Blender two-keyframe Bezier ease, x = x0 − D·(3s² − 2s³) with s = (i − i0)/T.
  - The post track alone (frames 15–41) gives i0 = 0.5, T = 57.9, rms 0.29 px, and a24 = 0.513 px/f².
  - With i0 = 0 and T = 59/60 fixed:
    - hub midpoint: a24 = 0.505 and 0.521;
    - post: a24 = 0.500 and 0.521.
  - The roof edge in frames 0–25 gives 0.48–0.50. On the right side it is biased by the oblique view.
- **Check by a second route, with no ease model:** a local cubic fit to the post track over windows of 15–21 frames centred on frame 24 gives a24 = 0.509, 0.518 and 0.520 px/f².
  - Quadratic fits give about 0.41. They return the window-mean acceleration (frame 24) rather than the backward-difference value centred at frame 23, so they are consistent.
- **Chosen value:** a24 = 0.51 px/frame².

## Scale
- The cart's tyre diameter is 75.2 px: the median of 20 circle fits over frames 32–41, with a standard deviation of 0.9.
- The prior gives 0.369 m, so the scale is 0.004907 m/px at the depth of the near-side wheels.
- Every point of a rigid body moving in translation has the same velocity. The post tip and the hubs move at the same pixel speed: the fitted D is 1338.5 vs 1339.5 px, so the post is effectively at hub depth and the tyre scale applies directly.
- Yellow-car cross-check: its tyre measures 182.5 px, and with 11.38 m and 0.764 m that gives f ≈ 2718 px. The cart's near-side wheels are then about 13.3 m from the camera, which is plausible. The answer itself does not use this.

## Answer
a = 0.51 × 576 × 0.004907 = **1.44 m/s²**. The rate of 0.50–0.52 px/f² gives a range of 1.41–1.47.

**Confidence:** moderate to good. The main risk is whether the animation really is a smooth ease curve.
