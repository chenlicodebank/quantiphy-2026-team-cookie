# Q1563 – speed of the magnifying glass at t = 0.125 s (frame 3 at 24 fps; file fps also 24)

Method: the glass falls freely from frame 0 until it hits the desk at frame 11. The prior says its acceleration is 9.8 m/s².
Speed at frame 3 = |p3 - p2| x 24, which is the mean velocity between frames 2 and 3.

- I re-measured it with fit.py, using a difference mask against frame 29. Centroid y for frames 0-6 is 19.97, 26.08,
  43.22, 71.49, 110.27, 159.84, 219.47. The per-frame drops are 6.11, 17.14, 28.27, 38.78, 49.57 px. The second
  difference is about 11.0 px/frame² early on and falls later because of perspective as the glass moves away.
- Route 1 (pixel ratio, with the scale taken from the prior): speed = (d23 / a) x g / fps = 28.27 / 11.08 x 9.8 / 24
  = 1.042 m/s. With the bbox track (28 / 11) it is 1.039 m/s.
- Route 2 (release-time fit): a quadratic fit to frames 0-4 gives a release about 0.05 frames before frame 0 (d01 =
  6.1 px against 5.5 px for release exactly at frame 0). That matches Blender rigid-body semi-implicit Euler with 10
  substeps, where d_k = a(k + 0.55). This gives v = g x 2.55 / 24 = 1.041 m/s. A release from rest exactly at frame 0
  in closed form would give 1.021 m/s.
- Sideways drift is about 0.5 px/frame, which is negligible.

Answer: 1.04 m/s. Confidence: high, about ±2%.
