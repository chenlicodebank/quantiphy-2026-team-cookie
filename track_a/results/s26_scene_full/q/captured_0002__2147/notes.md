# q_2147 – length of the slope (cm)

The video file and the question both run at 24 fps.

Correction to scene/: the "white board" is the slope. The ball rolls down its face during frames 28-35 and does
not fall in front of it. It shows faintly on the white surface in frames 32-35, then reaches the table at frame 36.

## Method (measure.py)
- f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- I made a white mask of the board at frame 12. Its outline is the polygon (654,291) (560,299) (563,423) (665,415).
  Down the central columns, the top edge is at y 294 and the bottom edge at y 421.
- Endpoints: top-edge midpoint back-projected at the far-end depth 1.8150 m, and bottom-edge midpoint back-projected
  at the near-end depth 1.6715 m. The ball's depth decreases as it rolls down (1.779 -> 1.736), so the low end is
  the near one.
- Length = 3D distance between the two endpoints:
  - central column mask (610,294)-(614,421): 32.26 cm
  - polygon midpoints: 31.68 cm
  - left edge: 31.54 cm
  - right edge: 31.75 cm
- Answer: 32.0 cm (spread about +-0.4 cm).

## Checks
- The ball's 3D displacement from frame 24 (depth 1.779 m) to frame 31 (depth 1.736 m) is parallel to the slope
  axis (cos = 0.999), which confirms the endpoint assignment and the geometry.
- I projected the ball track onto the slope line and fitted a quadratic over frames 29-35. It gives an
  acceleration of 4.12 m/s^2, against the prior's 4.05 (1.7 pct off), so the metric scale is confirmed.
- The ball covers about 0.31-0.38 m along the slope by frames 35-36, which agrees with a slope of about 32 cm.

Confidence: high (expected error under 3 pct).
