# Q1883: acceleration of the astronaut at t = 0.5 s (m/s^2)

Time base: the file and the question are both 24 fps, so t = 0.5 s is frame 12. acc(12) = (speed(12) - speed(11)) x 24.

## Scale
- Focal length: the prior height is 2.2 m and depth_info gives 18.147 m at t = 1 s (f24). bbox_h at f24 is 380 px, in a
  legs-nearly-together pose. f = 380 x 18.147 / 2.2 = 3134 px (horizontal FOV about 40 deg).
- Depth at f12: two size proxies, both anchored at f24.
  - Backpack vertical extent (rigid): 168 px at f6-16 against about 171 px at f24, giving Z12 = 18.4 m.
  - bbox_h: 343 px against 380 px, giving Z12 = 20.1 m. This proxy is pose-affected.
  The backpack height stays at 168 +/- 1 px from f0 to f22, so the depth is about constant around f12.

## Position
- I used torso-rigid silhouette landmarks rather than the record's heuristic pelvis, which arm pixels contaminate.
  The landmarks are the buttock rear edge just below the backpack, the backpack rear edge, and the backpack-bottom row
  (scripts: profile.py, bp.py, butt.py, bpack.py).
- Image motion from f1 to f14: x step is a constant 9.5-10 px/frame. y step falls smoothly from 8 to 1 px/frame (the
  path curves). The torso shows no gait oscillation.
- At f14 to f15 the x step jumps abruptly to 20 px/frame and then to 30. The limb-pose change rate does not jump
  (posechange.py), so the clip is not re-timed. No foot is ever planted (the camera may track, or the feet slide).
  This does not affect f11-12.

## Result (final.py)
- Fitted quadratic x(t), y(t) over f2-14, f4-14 and f6-14, with Z = 18.4 or 20.1 m, with and without the depth trend:
  - speed about 1.46-1.67 m/s at f11 and f12;
  - acc12 between -0.03 and -0.28 m/s^2, typically about -0.25.
- The scalar speed is nearly constant, decreasing slightly as the image path turns.
- Raw per-frame differences are dominated by noise: 1 px of noise is about 3.7 m/s^2.

## Second route
- The raw centroid and the record's pelvis with the depth held constant give a trend of -0.1 to -0.8 m/s^2 (f6-14
  and f2-14 fits) and about 0 per-frame for the centroid.
- Both routes agree that the speed is nearly constant, with |acc| below 1 m/s^2.

The answer must be positive, so I give the magnitude: 0.25 m/s^2.

**Confidence: low.** The true value is near zero, so the relative error could be large. The camera may move (no
static reference is visible), which makes the fixed-camera assumption uncertain.
