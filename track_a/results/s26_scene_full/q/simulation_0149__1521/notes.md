# q 1521 - width of the pillar with the collision-warning (yellow/black) markings

Answer: **0.975 m**. Time base: 24 fps (file rate = question_fps). Only static geometry is used, measured on frame 49 with the car gone.

## Which pillar
- The big foreground pillar on the right (x 1474-1709) has only hazard tape on its corners, so "the pillar with the
  collision warning markings" most likely means it. This is the main answer.
- The light pillar on the left (x 476-699, with the fire extinguisher and the 30 sign) also has striped corner
  guards. I use it as a second, independent check. Both pillars come out the same size within about 3 pct.

## Camera model (scripts: edges.py, bases_sub.py, corners.py, tire0.py)
- The pillar edges are exactly vertical in the image (edges.py: drift < 2 px over 600 px of height). So the camera
  has **no pitch**. The horizon y = 829 (from the tube vanishing point in scene/) therefore comes from a lens shift,
  which puts the principal point at (960, 829).
- Vanishing points on the horizon:
  - VP_A = 4050, from the ceiling tubes. The extinguisher pillar's lit face base gives 4107, which agrees.
  - VP_B = -938, from the foreground pillar's front-face base: sub-pixel fit, slope 0.04452 ± 0.0003.
  - Two perpendicular directions give f = sqrt(3090 x 1886) ≈ **2414 px**.
- Check against the prior plus depth_info: the right front tyre at frame 0 is the image-left wheel. Its rim is
  centred at (67, 829) and the tyre bottom is at about y 893-897. With f = 2414, the 14.244 m Euclidean distance
  gives Z = 13.36 m and a predicted tyre radius of 69 px. I measured about 65-68 px, which implies f ≈ 2250-2400.
  So f lies between 2300 and 2414, and the width hardly depends on it (see below).
- Camera height: the tyre centre sits on the horizon (rim centre y 829 at frame 0, hubs at y 826-834 in frames
  17-31), so h = tyre radius = 0.764 / 2 = **0.382 m** (± about 0.008 m). Floor point: Z = f h / (v - 829) and
  X = (u - 960) Z / f.

## Measurements (corners at 50 pct brightness transitions; base lines fitted with sub-pixel edges)
- Foreground pillar front face, B direction: x 1474.4 to 1708.7, base y 936.4 to 946.8.
  - Width **0.969 m** (f 2414) or 0.978 m (f 2300), with h = 0.382. Depth about 7.8 m.
  - The dark side face (A direction, x 1709 to about 1883 where the background reappears) gives about 1.0-1.02 m.
    That value is less certain.
- Extinguisher pillar: near corner x 552 (base y 894.2), far corners x 698.8 (A face) and x 475.5 (B face). Depth
  about 14 m.
  - A face: 1.006 m (f 2414) or 0.988 m (f 2300).
  - B face: 0.979 m (f 2414) or 1.046 m (f 2300). The B face is very sensitive to the corner position (±2 px gives
    ±4 pct).
- Sensitivity: h ± 0.008 m changes everything by about ±2 pct. f between 2300 and 2414 changes the foreground front
  face by less than 1 pct.

## Result and check
- Main route, foreground pillar front face: 0.97 m.
- Second route, the other pillar's two faces: about 0.98-1.01 m. The pillars look square, about 1 m on a side.
- Answer: 0.975 m, a slight weighting toward the clean foreground face measurement.
- Under any reading, the width (the face extent across the pillar, or the shorter horizontal extent) is about
  0.97-1.0 m.
- Confidence: about ±4 pct.
