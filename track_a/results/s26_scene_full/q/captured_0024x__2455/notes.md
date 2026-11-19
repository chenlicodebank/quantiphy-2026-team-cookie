# q_2455 — velocity of the book at t = 1.2 s (cm/s)

File fps = question fps = 24, so t = 1.2 s is frame 29. f = 0.5959 x 1280 = 763 px, principal point (640, 360).

## Track
I used the book centre from scene/tracks/book.csv (two versions: the full-mask centroid and the
cover-only centroid). I checked both by overlaying them on frames 24–33 (frames/strip.png); they sit
on the book. Frame 29 is the moment the book's front edge reaches the table at the bottom of the
ramp. From frame 30 it tips over and slides on the table, slowing down.

## 3D (measure.py)
- I back-projected P24 with depth 1.0685 m and P29 with depth 0.9770 m (from depth_info). The
  distance between them is 0.161 m (0.160 m with the cover centroid), so the average speed over
  frames 24–29 is 0.77 m/s.
- The book slides along a straight ramp, so for frames 18–31 I took each pixel ray's closest point
  to the 3D line P24–P29 to get its position.
- Per-frame backward-difference speeds (m/s), frames 24–31: 0.64, 0.64, 0.71, 0.79, 0.85, 0.88, 0.60, 0.43
  (cover centroid: 0.53, 0.67, 0.68, 0.85, 0.86, 0.78, 0.65, 0.65).
- A quadratic fit over frames 20–29 on the ramp gives a = 1.8–2.0 m/s² (the prior says 2.8) and
  v(frame 29) = 0.95–0.99 m/s.
- Smoothing that is centred on frame 29 mixes in the slowdown after the impact and gives 0.69–0.76 m/s.

## Routes and choice
- Speed just before contact (backward difference at 28–29): 0.78–0.88 m/s.
- Fit extrapolation: 0.95–0.99 m/s.
- Uniform acceleration with the prior's a = 2.8 plus the 0.161 m distance anchored by the given
  depths: v29 = 1.06 m/s.
- Centred 5-frame window across the impact: about 0.72 m/s.

I answer 0.90 m/s = **90 cm/s**, the middle of the routes that stay on the ramp. Confidence is
moderate: the true value most likely lies between 0.75 and 1.05 m/s. The spread comes from frame 29
being the impact frame and from which smoothing window the reference used.
