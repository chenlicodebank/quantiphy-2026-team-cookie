# Q1255: speed of the bicycle (m/s)

The prior is that the white car (the white cargo van) accelerates at 4 m/s². The depth_info gives the van, bike, human and taxi depths at t=0.58 s (f14) and t=1.58 s (f38). The file fps and question_fps are both 24.

## Method (measure.py)
- Pixel tracks come from scene/tracks. Van: patch_cx plus the median bbox offset, with y = bbox centre. Bike: the cyclist's rider_cx (rigid with the bike), with y = bbox centre. I checked the identities on frame 38: the van is the white van behind the taxi, and the cyclist is at x~1233.
- Pinhole camera with the principal point at the image centre. For a trial focal length f:
  1. Back-project each object at f14 and f38 using its given depth. This gives two 3D points, and the line through them is the object's path.
  2. Intersect every frame's ray with that line to get 3D positions.
  3. Take per-frame speeds as the backward difference × 24.
- I solved for the f at which the slope of the van's speed over time equals 4 m/s². The result is f ≈ 2211 px (HFOV 52°). Changing the fit window (3-71, 10-60, 20-71) moves f by only 2190-2211.
- Check: at this f the van's speeds follow v = 4·n/24 starting from rest at frame 0 (6.00 m/s at f36, 11.83 m/s at f71). This independently reproduces the prior's constant-acceleration model. The van and bike path directions come out nearly parallel ((0.997, -0.007, -0.077) vs (0.996, -0.006, -0.093)), which fits both being on the same cross street.

## Result
- Bike per-frame speeds are constant, 5.2 ± 0.15 m/s (f2-71). The mean of the per-frame speeds is 5.213-5.26 m/s across the f-fits. The net displacement f1→f71 / time gives the same value, and using the bbox cx instead of rider_cx changes it by less than 0.001.
- Answer: **5.22 m/s**.
- Second route: the bike's speed depends on f only through Z/f, and the van's Z/f is fixed by the prior, so the answer is insensitive to f. Small differences in f window move it by under 1%.
- Confidence: high (about ±2%).
