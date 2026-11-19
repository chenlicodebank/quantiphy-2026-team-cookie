# Q451 – length of the truck (m)

Prior: truck acceleration = 10.757 m/s^2. 2D side-view simulation, static camera, 30 fps (file fps = question_fps, no re-timing).

## Pixel acceleration
- track.py: four foreground-masked templates from the chassis/wheel band (y 740-900) at frame 42, matched horizontally
  in each frame with sub-pixel parabola refinement. Quadratic fits x(t):
  piece0 1849, piece1 1835, piece2 1823, piece3 1829 px/s^2 (residuals 0.15-0.6 px); chained mean 1831 px/s^2.
- Scene record track (independent tracker), quadratic fits: 1845 (frames 14-57), 1833 (20-50), 1837 (36-50),
  1830 (14-35), 1859 (30-54). Vertex of all fits at t ~ 0 (starts from rest), so uniformly accelerated.
- Adopted a = 1835 px/s^2 (spread about ±0.7 %).
- Scale = 10.757 / 1835 = 0.005862 m/px.

## Pixel length (frame 42, truck centred, least perspective)
- length.py: foreground mask (|frame − empty frame 59| > 18). The left end is the tail-lift tip at x ≈ 192-198
  (row 720). The right end is the mirror/railing at x ≈ 1703 (row 585). Full side length ≈ 1509 px. The scene record gives 1507.
- Full length = 1509 × 0.005862 = **8.85 m** (world AABB, including the tail lift and mirror).
- Other readings: box rear to cab bumper is 1368 px → 8.02 m. Tail-lift tip to cab nose is 1487 px → 8.72 m.
  The answer uses the AABB reading, which includes everything.

## Check
The two independent trackers agree on the acceleration to within 1 %. The mask edges agree with the record's
length to within 4 px. Confidence: good on the scale; the main uncertainty is which extent the reference length uses.
