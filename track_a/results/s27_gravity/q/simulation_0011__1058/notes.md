# q_1058 — average speed of the bird (crow), 0.5 s to 1.0 s

The file and the question both run at 24 fps, so t = frame/24. The window covers frames 12 to 24. The answer is the
mean of the per-frame speeds at frames 12..24, which is 6.61 m/s. The 12→24 chord divided by 0.5 s gives 6.72.
**Answer: 6.6 m/s.**

## Objects
- bird = the crow (depth 46.654 m at t=0 and 43.970 m at t=1).
- nest = the black fuzzy object that falls off the branch of the left tree (17.27 m and 17.25 m). It carries the
  gravity prior. It is in free fall from about frame 30 and lands at frame 50.

## Focal length (principal point (960,977), checked: vertical lines have zero lean at x≈957)
1. Gravity: I fitted a full pinhole model of a vertical drop at g = 9.8 to the nest centroid (fall_fit.py), using
   several frame windows between 30 and 49 and two trackers. The result is f ≈ 1700–2080, median ≈ 1870 px. The
   implied start of the drop (velocity 0) is about frame 29, which matches the moment it leaves the branch.
2. Vanishing geometry: LSD on the house's vertical posts gives a vertical vanishing point at (957, −12100), so
   f·cotθ ≈ 13080 px and the camera is pitched up. The horizon comes from the convergence of the front-wall
   horizontals (y≈1261) and from the ground-plane depths (nest landing at 17.25 m against the cart at 33.2 m, which
   gives y≈1282). Together these give f² = 13080·(y_h − 977), so f ≈ 1925–2000 px.
   I used **f = 1920 px** (horizontal FOV ≈ 53°).

**Scale caveat.** With this f the house assets come out about 2.8× real size: the door is about 6 m, the barrels
about 2.7 m, the crow's wingspan about 2.8 m and the nest about 1 m. Taking f ≈ 5900 from "real" asset sizes would
contradict both the exact gravity prior (it would need about 5.8 px/frame² of image acceleration, but about 2 is
measured) and the perspective geometry of the house. Those two independent routes agree, so I treat the assets as
oversized models and kept f from physics and geometry.

## Bird trajectory
- My own tracker (track_bird.py) uses a median background, a mask of dark pixels and the core centroid from a distance
  transform. Frames 5–15 are unreliable because the bird passes against dark foliage and the eave post, so I left
  them out of the fit.
- 3D line from P0 = 46.654·ray(frame 0) to P24 = 43.970·ray(frame 24). Each frame's position is where its ray meets
  that line. The straight-line model fits: the apparent-size growth at the same flap phase (frames 24, 41, 58)
  matches the depth decrease the line implies.
- Fit of s(t): a cubic/smoothstep trend (a Bezier ease-in from about frame 0) plus a 17.1-frame wing-flap periodic
  term. This flap term is the mask centroid surging with wing pose. The origin speed comes from the trend.
- Trend speeds (f = 1920) rise from 1.5 m/s at frame 1 to 5.5 at frame 13, 7.3 at frame 21 and a peak of 8.7 near
  frame 37.
- Mean over frames 12..24: **6.61 m/s**. The chord gives 6.72.
- Sensitivity to f: f = 1850 gives 6.78, f = 2000 gives 6.42.

## Checks
- Same-phase chord speeds from raw s: 0→17 is 4.4 m/s, 17→34 is 7.7, 24→41 is 8.7 and 41→58 is 7.25. These fit
  the ease profile.
- A second route read head positions by eye on zoomed frames: x is 1127 at frame 12 and 1247 at frame 24. That gives
  about 6.4 m/s.
- If the flap surge were real origin motion, the answer would be about 6.2.

Confidence: moderate, about ±7%. The main uncertainty is f (±4%), followed by the trend over the occluded frames.
