# Q1104: length of the eagle (m). Answer: 0.90 m

The file is 25 fps and question_fps is 24. All times use 24 fps: t=1 s is frame 24 and t=2 s is frame 48.

## Scale (fit_f.py)
- Fitted a straight-line, constant-velocity 3D path for the eagle, P(i) = P0 + V·i, under a pinhole camera with cx = cy = 480.
- The fit used the pixel centroid track from scene/tracks/bird.csv (bad and occluded frames removed) and three constraints:
  - |P(24)| = 116.0475 m and |P(48)| = 108.2756 m;
  - |V| × 24 = 11.84 m/s.
- Result: **f = 3401 px** (horizontal FOV 16.1°). The fit reproduces both distances to within 0.04 m and the speed exactly.
  The pixel residual is 2.4 px in u.
- Direction of flight: V/frame = (0.360, 0.006, −0.337), so the eagle flies right and toward the camera, about 43° out of the
  image plane.
- Checks of this scale:
  - Boat at about 103 m: hull 263 px → about 8 m long; mast top to hull bottom 314 px → about 9.5 m. Both are realistic.
  - The raised wing (wings-up frames 23–25 and 48–50) is about 31 px tall at 116 m, so about 1.05 m half-span. This is a
    vertical extent, so it does not depend on the bird's heading.
  - Horizontal wing extent at mid-stroke is 1.35–1.5 m projected (widths.py). Divided by the foreshortening for wings
    perpendicular to the flight direction (0.68), that gives a **wingspan of about 2.0–2.2 m**, a real bald-eagle size.
    The two routes agree, which confirms both the scale and that the bird faces its direction of flight (the white head
    also sits to the right of the wing roots, as this heading predicts).

## Length
The bird is seen almost head-on: its body points 47° from the line of sight, so its length is shortened by a factor of
0.73 in the image and only covers about 18–21 px.
- **Direct measurement** (mask.py, wings-up frames where the body base is visible): the body runs from the tail side to
  the white head over 18 px at frame 24 (116 m) and 21 px at frame 48 (108 m). Projected that is 0.61–0.67 m; divided by
  0.73 it gives **L ≈ 0.84–0.92 m**.
- **Proportion check:** a bald eagle's length is about 0.43 × its wingspan, so 2.1 m × 0.43 ≈ 0.9 m.

Answer: 0.90 m.

Confidence: moderate. The scale is solid (two consistent routes), but the body is heavily foreshortened, only about 20 px
long, and partly hidden by the wings, so the length is good to perhaps ±10–15 %.
