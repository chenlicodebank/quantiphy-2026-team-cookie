# Q1675 — length of the eagle (m)

The file is 25 fps; question_fps is 24. All times use 24 fps (t=1 s -> frame 24, t=2 s -> frame 48), following the frame column of scene/tracks/bird.csv.

## Scale (focal.py, dir.py)
- Eagle positions at frames 24 and 48 come from the mask centroid (scene track, checked on crops), back-projected with the given depths 116.0475 and 108.2756 m and the principal point at the image centre (480, 480).
- I solved for the focal length f so that the 3D chord over 24 frames equals 11.84 m (the prior speed 11.84 m/s x 1 s). This gives f = 3392 px. Other frame pairs one flap cycle apart (23/47, 25/49, 22/46) give 3330–3416, so I used **f ≈ 3380 px** (horizontal field of view about 16°).
- Motion direction in camera coordinates: (0.73, 0.02, -0.68). The eagle flies right and toward the camera, about 43° from the image plane.
  - The body axis projects onto image x with a factor of 0.755.
  - The wing axis (horizontal, perpendicular to the body) projects with a factor of 0.656.
- Depth at other frames is interpolated linearly from the two given values.

## Length (extent.py)
- At 960 px the eagle is only 22–54 px wide, so the head and tail cannot be picked out directly.
- At full upstroke (frames 23–25) the wings are near vertical, so the horizontal extent is set by the body, beak to tail. The extent at the 50% darkness level is 22 px at depth 116.0 m, which is 0.755 m projected. Dividing by the 0.755 foreshortening factor gives **L ≈ 1.00 m**.
- Other narrow poses give upper bounds:
  - frame 6 (wings edge-on): 0.83 m projected, so L ≤ 1.10 m;
  - frames 48–50: the V is visibly more open, so the wings add width.

## Second route: wingspan and proportions
- With the wings spread (frames 58–61) the horizontal extent is 1.60–1.63 m projected. Dividing by the 0.656 wing factor gives a wingspan of about 2.45 m.
- That makes the length-to-wingspan ratio 0.41, which matches real eagles (about 0.40–0.45). An eagle 1.0 m long with a 2.4 m wingspan is realistic, so the real-world scale is consistent.

## Answer
1.0 m. Confidence is moderate, about ±15%. The main uncertainty is that the body is barely resolved: the length comes from the minimum upstroke extent and an assumed foreshortening, with the body axis taken along the flight direction.
