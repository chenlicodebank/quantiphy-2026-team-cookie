# q_2434 – velocity of the book at t = 1.0 s (cm/s)

The file and the question both run at 24 fps. t = 1.0 s is frame 24, while the notebook slides down the ramp (frames 19–29).

## Method
- Camera: f = 0.5959 × 1280 = 762.8 px, principal point (640, 360).
- 3D anchors: I back-projected the book centre with the given depths: frame 24 at d = 1.0685 m and frame 29 (t = 1.2 s)
  at d = 0.977 m. These two points are 15.8 cm apart. The book slides in a straight line on a flat ramp, so I took the
  line through these two points as its 3D path. For every other frame, the position is the point on that line closest
  to the camera ray through the tracked pixel centre. This reproduces both given depths exactly.
- Velocity: I fitted a quadratic s(t) along the path over windows from frames 20–28 to 22–26 (light smoothing), and
  also took the mean of the 5 forward differences centred on frame 24.

## Routes
1. scene/ full-mask centroid: quadratic v(1.0) = 61–66 cm/s, v(frame 24.5) = 65–69; mean of the 5 forward
   differences = 67.6.
2. scene/ cover-only centroid: v(1.0) = 57–59 cm/s, v(24.5) = 62–63.
3. My own template-matching track (tmatch.py; subpixel, chained from frame 24): v(1.0) = 53–54 cm/s,
   v(24.5) = 57–59; mean of the 5 forward differences = 59.1.

The measured acceleration is about 1.9–2.3 m/s², a little below the prior's 2.8. Check against the prior: starting from
rest at about frame 18.5 with a = 2.8 m/s², v(24) = 2.8 × 5.5 / 24 = 64 cm/s. This agrees with the routes above.

## Answer
About 62 cm/s, between the centroid routes and the template route and close to the prior-based check.

Confidence: moderate, about ±10 %. Depth falls quickly along the path, so it makes up much of the 3D speed. The answer
therefore depends on the depth_info values at 1.0 s and 1.2 s and on the centre found at frame 29 (the ramp foot).
