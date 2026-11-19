# q_2547 — speed of the white (ping-pong) ball at t = 1.5 s, in cm/s

The file is 24 fps and question_fps is 24, so t = 1.5 s is frame 36. The lab camera has f = 0.5959 × 1280 = 763 px and principal point (640, 360).
depth_info: the ping-pong ball is 1.353 m away at t = 1.5 s (the tennis ball is 1.183 m away; that matches the 6.7 cm prior with its 43 px diameter at f36, so the focal length is consistent).

## Measurement (measure.py → meas.npy; velocity.py)
- White-ball mask: V > 165, S < 52, R−B > 4. These thresholds exclude the bluish background and the brown reflection on the table, which the scene/ mask partly leaked into. The centre comes from a least-squares circle fit to the upper 75 % of the contour, for frames 34–48.
- Image motion after f36 is steady: about 5.8 px/frame to the right and about 1.9 px/frame down. The apparent diameter grows from about 26–27 px (f36) to about 32 px (f48), so the ball is rolling toward the camera.
- The depth per frame isn't given, so I estimated it two independent ways:
  1. **Apparent size:** a linear fit of 1/diameter over f36–48, with Z ∝ 1/diameter.
  2. **Table-plane geometry:** Z ∝ 1/(v_centre − v_horizon), with the horizon at y = 340–351 (from the vanishing point of the table edges).
- 3D points are back-projections ((u−cx)/f, (v−cy)/f, 1)·Z, scaled so the distance at f36 is 1.353 m.

## Results (speed, cm/s)
| depth route | linear fit f36–41 | mean forward diff f36–40 | centred 5-frame smoothing (covers the 35→36 jump) |
|---|---|---|---|
| diameter fit | 53.2 | 53.6 | 58.3 |
| horizon y=340 / 345 / 351 | 47.2 / 49.3 / 52.1 | 51 / 53 / 56 | ~100 (raw per-frame depth jump) |

The two depth routes agree on the true speed: about 50–53 cm/s. Its components are about 0.155 m/s sideways and 0.47–0.51 m/s toward the camera.

## Dropped frame
A frame was dropped between f35 and f36: both balls move about twice their normal step there. A reference made with 5-frame centred smoothing would include that gap. If the motion is uniform, that inflates the speed by about 6/5, to roughly 60–62 cm/s.

**Answer: 56 cm/s.** This sits between the true speed (about 51) and the inflated value (about 61), within about 10 % of both.

Confidence: moderate. The toward-camera component dominates the speed, and depth can only be inferred from image cues.
