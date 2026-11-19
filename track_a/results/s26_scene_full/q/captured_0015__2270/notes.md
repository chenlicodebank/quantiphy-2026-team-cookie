# q 2270 - velocity of the toy at 2.6 s (cm/s)

Prior: g = 9.8 m/s^2, no depth_info. File fps = question_fps = 24 -> t = 2.6 s is frame round(62.4) = 62.
Frame 62 comes 2 frames after the second catch (catch at ~60). The toy is in the hands and moving down
(motion blurred). Camera is static, and the video pts are regular (512/12288 s per frame).

## Scale from gravity (fit.py, track.py, fit2.py)
- I made my own background-difference masks (median background, threshold 28) for the free flights of both
  tosses and fitted y(t) = a t^2 + ... with t = frame/24.
- The top edge of the toy's head is the most rigid feature (rms 0.2-0.6 px):
  toss 2: frames 51-59 2879, 52-58 2949, 53-58 2962 px/s^2; toss 1: frames 15-22 2990, 16-22 3072, 17-22 3086.
  Bbox centre: 2685 (toss 2) and 3034 (toss 1). The mask centroid gives a lower 2540-2620 because the legs and
  tail swing and the toy rotates. Motion blur pushes the top-edge estimate slightly low, if anything.
- Chosen value: g = 3000 px/s^2 (+-3 %), so the scale is 9.8/3000 = 3.27 mm/px.
- Sanity check: the person is 507 px tall, which gives 1.66 m (the toy is slightly in front of her). That is
  plausible, while the centroid-based ~2550 would make her 1.95 m. The toy, at 103 px, comes out at ~34 cm.
  The implied depth is Z = 763 x 0.00327 = 2.5 m.

## Velocity at frame 62
Toy centres (scene/tracks/toy.csv best_cy, checked on zoomed crops frames/zoom_59_66.png; the bbox mid-points I
read by eye agree within a few px): 60: 261.8, 61: 285.8, 62: 308.3, 63: 324.6, 64: 340.1, 65: 346.9.
Vertical px/frame by estimator:
- central difference (63-61)/2 = 19.4
- (64-60)/4 = 19.6
- Savitzky-Golay window 5 = 19.5
- forward diffs averaged over 61-63 = 18.1
- forward diffs averaged over 60-64 = 17.0
I used 19.0 px/frame vertical. The horizontal component is ~ -2.5 px/frame, so the speed is 19.2 px/frame =
461 px/s, and 461 x 3.267 mm = 1.505 m/s = **150.5 cm/s**.

Second route: the core (dark fur) centroid track gives 304.9 at 62, with (63-61)/2 = 19.2 and (64-60)/4 = 19.1,
which agrees.

Confidence: moderate, about +-10 %. The main uncertainties are how the toy centre is defined while hands cover it,
the smoothing convention (17-19.6 px/frame), and the g fit (2950-3080).
