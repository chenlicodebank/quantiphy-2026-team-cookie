# q_2619 – soccer ball velocity at t = 1.6 s (cm/s)

File fps = question fps = 24 → t = 1.6 s is frame 38 (t = 0.6 s is frame 14). Camera: f = 0.5959 × 1280 = 762.8 px,
principal point (640, 360), camera static (scene/camera_shift.csv).

## depth_info label
The depth_info lists two "soccer_ball" distances at t = 1.6 s (3.052 and 2.412). The 2.412 value must be the
basketball: the basketball's 71.5 px diameter at frame 38 gives 0.232 × 763 / 71.5 ≈ 2.5 m, the soccer ball sits
higher in the image (farther away), and 2.758 → 3.052 matches the soccer ball rolling back toward person A.
So: soccer f14 = 2.758, f38 = 3.052; basketball f14 = 2.270, f38 = 2.412.

## Method (measure.py, check.py)
- Soccer ball centres for frames 26–46: the scene track (RANSAC circle), checked against my own re-measure (convex
  hull of the white pixels: centroid and enclosing circle). They agree to about 1 px. Frame 38 overlay checked
  visually (frames/f38.png): the centre is about (499, 348).
- Depth at the other frames: both balls roll on the floor, so their centres lie on planes parallel to the floor.
  I took the 4 back-projected depth_info points (2 soccer, 2 basketball) and solved for the plane normal plus one
  offset per ball (4 equations, 4 unknowns; exact solution). Result: camera pitch about 36°, soccer-centre plane
  1.742 m from the camera, basketball-centre plane 1.691 m (offset difference 5 cm, roughly the difference in
  radii). Each soccer centre = its pixel ray intersected with the soccer plane. This reproduces 2.758 and 3.052
  exactly.
- Check of the plane: plane distance × the soccer ball's pixel hull width stays roughly constant at 130–141 over
  frames 22–46 with no trend (Z rises from 2.64 to 3.21 m while the width falls from 53 to 43 px). The ball's own
  apparent size therefore confirms the depth change the plane predicts.
- Velocity: a linear fit of the 3D centre over windows around frame 38. I start no earlier than frame 36 because of
  the suspected dropped frame between 35 and 36.
  - Fits on frames 36–40, 36–41, 36–42 and 37–41: 63.3, 62.0, 62.6 and 61.8 cm/s (track centres); 61.2, 61.6,
    61.6 and 60.9 cm/s (own centroids).
  - Mean per-frame speed over frames 37–41: 61.7 and 62.4 cm/s.
  - Raw one-frame differences: 54–82 cm/s (noisy).
  - The velocity splits into about 40.6 cm/s across the image (lateral, at constant depth) and about 0.49 m/s
    along the depth direction.

## Second route / caveats
- I also tried a plane normal taken from the basketball's diameter-based depths. It gives inconsistent soccer
  offsets (0.09 vs 0.30), so I rejected it: the basketball's pixel diameter barely changes, which contradicts its
  own depth_info values.
- Depth rate taken only from the soccer ball's pixel size over frames 30–46: dZ/dt ≈ 0.33 m/s, giving about
  52 cm/s. The size is quantised to whole pixels, so this is noisy. The longer-range size trend (frames 22–46)
  agrees with the plane model instead.
- Answer: 62 cm/s. Confidence moderate; the main uncertainty is the depth rate, so the answer could be 52–68 cm/s.
