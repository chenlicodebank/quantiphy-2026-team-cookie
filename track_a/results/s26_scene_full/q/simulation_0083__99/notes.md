# Q99 — distance yellow car ↔ black/white car at t = 2.0 s (frame 48 at 24 fps)

fps = question_fps = 24, so t = 2.0 s is frame 48. The clip is a 2D top-down view with a static camera; both cars lie in the same ground plane.

## Scale
- Prior: the yellow car is 5.67 m long.
- Its pixel length along the motion is 270 px near the image centre (frames 20–30; checked again in measure.py).
- Near the edge it reads 272 px because a little of the car's side shows. I used the centre value.
- Scale: 5.67 / 270 = 0.021 m/px.

## Positions at frame 48
I measured these with measure.py: median background, then a colour/brightness mask, then the bbox centre. The values match scene/tracks.

| Car | Centre x (px) | Centre y (px) |
|---|---|---|
| Yellow | 391.5 | ≈ 415.5 (lane) |
| Black/white | 1442.0 | ≈ 539.5 (lane) |

- dx = 1050.5 px and dy = 124 px.
- Edge perspective widens each bbox by about 1–2 px on the side away from the image centre. Correcting for that gives dx ≈ 1049 px.
- Distance ≈ 1056 px × 0.021 m/px = **22.18 m**. Without the correction it is 1057.8 px = 22.21 m.

## Second check (from the motion)
- At frame 0 the black car's centre is 78 px to the left of the yellow car's centre.
- Motion starts at frame 2, and the cars separate at 10 + 13.96 px per frame.
- After 47 steps: dx = −78 + 47 × 23.96 ≈ 1048 px. This agrees with the direct measurement to within 2 px.

## Confidence
High, about ±2%. The main uncertainty is where each vehicle's origin sits relative to its bbox centre.
