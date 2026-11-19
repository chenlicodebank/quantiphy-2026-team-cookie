# Q1275: height of the traffic light (m)

The file runs at 24 fps and question_fps is 24, so t = 0.58 s is frame 14 and t = 1.58 s is frame 38.

## Correction to the scene record
The record puts the horizon at y≈535, which is wrong. Pairs of identical lamp posts give a consistent vanishing line:
- far-left lamp vs. lamp A: y = 479.5
- far-left lamp vs. lamp C: y = 481
- lamp C vs. lamp D (the row tops and bases intersect): y ≈ 479–485

I used **horizon y = 480**, with the principal point at (1080, 540). The camera is therefore pitched slightly down.

## Traffic lights (3 in view, same model)
| light | pole x | top y (sign tip) | base y | H_px | H_px / (base − 480) |
|---|---|---|---|---|---|
| right | 1593 | 328 | 663.5 | 335.5 | 1.825 |
| centre | 1025 | 382.5 | 597.5 | 215 | 1.830 |
| left (f38, taxi clear) | 744 | 352.5 | 638 | 285.5 | 1.81 |

All three give the same ratio, so they are the same height. Heights in metres are about 1.82 × the camera height, so it does not matter which light the question means.

## Scale
- **Focal length (trajectory fit, `trajfit.py`).** The van's 3D positions at f14 and f38 come from depth_info plus the pixel centre. I fitted a straight line with constant acceleration of 4 m/s² to its whole image track (cx, f2–71). Result: f = 2164 px, start at frame −1.1, rms 1.9 px.
  - Fixing f and freeing the acceleration gives a = 4.12 / 3.94 / 3.77 at f = 2100 / 2200 / 2300.
- **Camera height, route A (`height_cam.py`).** The feet of the pedestrian and the bicycle wheels are put at the horizontal distance of their depth-given origins. At f = 2164: h = 2.80 m (estimates range 2.74–2.82).
- **Camera height, route B.** This uses the van's ground-plane lateral displacement over f50→70, which must equal 2·(t70² − t50²) = 8.33 m. It needs neither depth nor f: h = 2.82 m with 5 px of shadow removed, 2.92 m without.
- **Consistency.** Route B's h, combined with route A's f·h product, gives f ≈ 2160, matching the trajectory fit.

## Result (`tl_height.py`)
The base is placed on the ground plane, and the top is taken at the same horizontal distance.
- Route A (f = 2164, h = 2.80): right 5.105 m, centre 5.112 m, left 5.046 m.
- Route B (h = 2.82): 5.146 / 5.154 / 5.088 m.
- Distance from the camera to the right light is about 34 m.

**Answer: 5.12 m.** Sensitivity: f ±3% changes H by about ±3% through route A, while route B is almost independent of f. Confidence is good, about ±4%.
