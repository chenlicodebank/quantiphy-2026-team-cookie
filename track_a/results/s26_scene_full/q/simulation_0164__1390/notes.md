# q1390 – height of the bowling pin (m)

Prior: ball diameter 0.21 m. depth_info: ball at t=0.5 s (frame 12 at 24 fps; file is also 24 fps) is 9.391 m from the camera.

## Method (geom.py, pinprof.py)
- Ball apparent diameter at frame 12 = 82.04 px (linear fit of frames 7-17 diam_fit from scene/tracks/ball.csv).
  Focal length f = d·Z/D with a small off-axis correction = 3610 px (HFOV 29.8°). The fitted ball depths
  reproduce 9.38 m at frame 12.
- Horizon y = 205 (vanishing point from scene record) gives the camera pitch (5.3° down). Ball-centre height
  relative to the camera stays constant along the path (-1.12 to -1.145 m, frames 8-37), so the ground plane is
  ≈1.23 m below the camera.
- Pin pixel extents measured from column intensity profiles on frame 0 (pins static): the rightmost pin
  (x=1597, clear against the dark backdrop) has its top at y≈483.5 and its base contact line at y≈586 (102.5 px);
  the pin at x=1558 gives the same values.
- Base ray intersected with the ground plane (distance ≈11.85 m), and the top ray with the vertical line through
  the base → H = 0.332 m (±0.5 px on each end gives 0.329-0.335; ground at -1.235 m gives 0.3345).

## Second route
Ball at impact (frame 37): diameter 64.4 px, depth 11.95 m, bottom at y≈587 (same ground line as the pin bases).
H = 102.5/64.4 × 0.21 × (11.85/11.95) = 0.331 m. The simple ratio without the depth correction gives 0.333 m.

Answer 0.333 m. Confidence: good (±2%). This is smaller than a real pin (0.38 m), which is expected because
the scene is not at real-world scale.
