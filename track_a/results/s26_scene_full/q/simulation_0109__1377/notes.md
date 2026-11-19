# q1377: distance between the two cells at t = 1 s

Two identical red spheres (the "cells") rise and recede in a 3D Blender scene. The file runs at 24.008 fps, but the times here use question_fps = 24, so t = 1 s is frame 24 and t = 2 s is frame 48.
Tracks come from scene/tracks (circle-fit centres). **Frame 31 is corrupt in the record** (a halo switches on there, giving diameter 22 and 68 px with wrong centres), so I left it out of every fit.

## Scale / focal length (principal point 540, 540)
- **Route A (prior speed):** I back-projected the left sphere at f24 (Z = 22.0155) and f48 (Z = 24.0333). Assuming constant velocity, |X48 − X24| over 1 s should equal 4.7833 m/s. This gives f = 1499.7 px.
- **Route B (image trajectory only, no prior):** I modelled the left sphere as moving in a straight line at constant velocity through the two back-projected points, projected it into every frame 0–62, and fitted f. The best fit is f = 1504.3 px with 0.11 px rms residual, and the implied speed is 4.772 m/s, 0.24 % from the prior. So constant velocity holds and the two routes agree.
- Size-consistency route (circle diameters at f24 and f48 with an off-axis silhouette model): f ≈ 1626. I discarded it because it depends on sub-pixel diameter bias and is the least reliable.

## Right sphere depth at f24
- The diameters at f24 are equal (110.74 vs 110.71 px) and both spheres are near the image centre, so the depth is about the same.
- 3D constant-velocity line fit of the right sphere (image track plus size): Z = 22.00 m.
- Smoothed diameter ratio: Z = 22.06 m.

## Result
The 3D distance between the centres at f24 is:
- 3.008 m with f = 1500 and the line-fit depth;
- 3.012 m with f = 1500 and the ratio depth;
- 2.999–3.003 m with f = 1504.

**Answer: 3.007 m.** Confidence is high, with an estimated error of about 1 %. The main uncertainty is f (±0.3 %).
