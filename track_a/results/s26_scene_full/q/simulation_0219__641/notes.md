# q_641: length of the big robot (blue tracked drill tank)

Prior: the tank moves at 5.924 m/s. fps = question_fps = 24, so no re-timing. No depth_info.

## Method (`length_calc.py`, using scene/tracks/tank_drill_robot.csv, checked on frames 12 and 30)
The video is labelled 2D, but it has clear perspective. The tank's parts move at different pixel speeds: drill tip
54.02 px/frame, near-side rear edge 51.04, far-side rear about 45.5. Its apparent length also grows from 614 to 705 px.
The tank only translates, so every point moves at the same 5.924 m/s. That gives each point its own scale,
k = Z/f = v / (fps * pixel speed), and its world x = (u - cx) * k.
Length = X(drill tip) - X(rearmost point). The drill tip is the rightmost point (the claws stop well short of it).
The rearmost point is the near-side track rear while the tank is left of the image centre, and the far-side rear end
once it is right of the centre.

- Route 1, frames 9-19 (near-side rear, linear fit residual 0.7 px, slope 51.04): L = 3.026 m with cx = 960
  (3.010 to 3.042 for cx = 900 to 1020). The value is constant over these frames.
- Route 2, frames 28-48 (far-side rear, slope 45.65, noisier): L = 3.01 m (2.98 to 3.01 depending on the window).
- For reference, a naive single scale from the body speed (51.8 px/frame) times the apparent length gives
  2.95 m at frame 12 and 3.28 m at frame 30. This varies with perspective, so I did not use it.

I checked the leftmost extent by eye on frame 12: the track rear is at about x = 183, against 180 in the record.

**Answer: 3.02 m.** Confidence: good (about ±3%). The main uncertainties are the principal point and the
rear-edge pixel positions.
