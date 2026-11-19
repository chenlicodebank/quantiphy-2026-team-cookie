# q2174 — basketball velocity at t = 1.2 s

The video and the question both run at 24 fps, so t = 1.2 s is frame round(28.8) = 29. That is the last falling frame before the first bounce: the record's lowest point is frame 30, and contact is about frame 29.5.

## Method (measure.py)
- I used the ball centres from scene/tracks/ball.csv (circle fit). I checked frames 21–30 against the record and they are consistent.
- Lab camera: f = 0.5959 × 1280 = 762.8 px, principal point (640, 360).
- 3D positions come from back-projecting each unit ray, scaled by the Euclidean camera distance. I estimated that distance two ways:
  (a) From the apparent ball diameter. The ball's diameter is 0.206–0.214 m, derived from the given depths at t = 1.0, 1.2 and 1.5 s; I used a mean of 0.210 m.
  (b) By interpolating linearly between the given distances 1.401 m (frame 24) and 1.564 m (frame 29).
- I fitted a quadratic, i.e. constant 3D acceleration, to frames 22–29 and to frames 23–29.
  - The fitted |a| is 9.2–9.7 m/s², which agrees with the prior of 9.8 m/s².
  - The fitted speed at frame 29 is 3.21–3.25 m/s, and at t = 1.2 s exactly it is about 3.18 m/s.
- Second route: raw frame-to-frame 3D speeds.
  - The backward differences at frames 28 and 29 are about 2.8 m/s (both depth estimates). They are slightly low, possibly because of motion blur or the onset of contact.
  - The forward difference from frame 29 to 30 is only about 1.4 m/s, because it runs into the impact.
- Third route, from the prior alone: release happens at about frame 20.5, giving v ≈ 9.8 × (1.208 − 0.854) ≈ 3.47 m/s. The fit puts the zero-speed time later, at about 0.88–0.90 s, so the release was probably gradual.

## Answer
I answered 3.1 m/s, a compromise between the fit value (3.2), the raw differences (2.8) and the free-fall value from release (3.45). Confidence is moderate: the result depends on how the reference smooths the velocity next to the impact.
