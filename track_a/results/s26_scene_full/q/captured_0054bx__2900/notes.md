# Q2900: distance between the orange ball and the soccer ball at 1.0 s (frame 24)

The orange ball is the basketball. The file and the question both run at 24 fps, so 1.0 s is frame 24. The camera is f = 0.5959 x 1280 = 762.75 px, with its centre at (640, 360).

## Orange ball at f24
- Circle fit in measure.py: centre (537.6, 385.8), d = 61.6 px, which matches the scene record.
- The given depth is 1.81 m, so P_o = (-0.241, 0.061, 1.793) m.
- Caveat: this depth does not fit the ball's apparent size. At 1.81 m, 62 px is only 0.15 m, but at f12 the given 2.24 m with 77 px gives 0.227 m. The reference uses the given depth, so I do too.

## Soccer ball at f24
The ball is still held, so the hand hides part of its right side. Its visible bounding box is x 893-944, y 574-640. The vertical extent of 66 px matches the full diameter, so the left, top and bottom edges are real.
- **Centre:** about (926, 607), with the diameter taken as about 67 px. The RANSAC circle in the record gives (926, 607). Extrapolating back from f25-27 gives (920, 604).
- **Depth:** there is no depth for f24, so I scaled the given f48 depth (3.254 m) by the ball's apparent size. In the record the f48 diameter is 47.2 px (diam_px), 44.2 px (fit) or 45.1 px (equivalent from area). At f26-28 the same measures are about 69.5, 66.6 and 67.2 px, and the ball is roughly the same size from f24 to f28. This gives a depth of 2.16-2.21 m, and I used 2.17 m.
- **Size check:** at f48, 3.254 m and 45 px give a ball of 0.19-0.20 m, which is plausible for a soccer ball.

## Result
- **Distance:** |P_s - P_o| = 1.135 m with centre (926, 607) and depth 2.17 m.
- **Sensitivity:** across centres (920-927, 604-607) and depths 2.12-2.22 m the distance is 1.09-1.16 m (run measure.py).
- **Answer:** 1.13 m.
- **Second route:** the depth from fit_d (2.16 m) and the depth from area-equivalent diameter (2.18 m) both give 1.13 m.

## Confidence
Moderate, about ±5%. The main uncertainties are the soccer ball's depth at f24, which is not given, and the size inconsistency in the orange ball's given depth.
