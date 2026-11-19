# Q2556: ping-pong ball velocity at t = 1.4 s (cm/s)

Time base: question_fps = file fps = 24, so t = 1.4 s is frame round(33.6) = 34. The timestamps are uniform (pts.py), so no frames were dropped.
Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360). Prior: D = 40 mm. depth_info: 0.738 m at frame 34, 1.457 m at frame 22.

## What happens around frame 34
After bounce 2 (frame 25) the ball makes low hops and rolls toward the camera and to the left across the table. It is at the front edge at frame 35 and falling in front of the table at frames 36–37. Frame 34 is sharp vertically but blurred horizontally. Its vertical extent is about 40 px, which agrees with the 41.4 px implied by 0.738 m (763 x 0.04 / 0.738).

## Route 1: table-plane back-projection (plane_vel.py, tablecheck.py)
- The plane normal comes from the vanishing points of the table-top trapezoid. The corners were checked on frame 46.
- A plane through the ball centres is anchored at the frame-34 3D centre (0.738 m along the frame-34 ray).
- The implied table top is 0.52 x 0.61 m, a rectangle (plausible), with the front edge at Z ≈ 0.665 m. That matches the ball reaching the edge at frame 35.
- The plane distances agree with the measured ball sizes at frames 30–34 (for example frame 30: 35 px measured vs 34.3 px predicted; frame 33: 38 vs 38.1).
- Linear fit of the 3D centres:
  - frames 30–35: 97.7 cm/s, vector (-28, +2, -94) cm/s
  - frames 31–35: 96.6 cm/s
  - chord 30→35: 101.5 cm/s
  - forward difference 34→35: 101 cm/s
- The single-frame differences are noisy (centroid v jitter ±2 px).

## Route 2: depth from apparent size (flux.py, route_size.py)
- The integrated brightness excess over the ball-free background is conserved under motion blur. Its square root gives the pixel diameter, calibrated to 41.35 px at frame 34.
- Distances for frames 29–35: 0.91, 0.875, 0.82, 0.86, 0.80, 0.738, 0.65. These agree with the plane to within about 4% for frames 29–34. Frame 35 is biased close, because the ball overlaps the darker front face of the table.
- Linear fits of the 3D centres:
  - frames 29–34: 86 cm/s
  - frames 29–35: 102 cm/s
  - frames 30–35: 107 cm/s

## Rejected
- Using frame 25 as an on-table anchor (route2.py, 117–122 cm/s) is invalid. The size there (about 34 px, 0.87–0.9 m) shows the ball was off the plane (hopping), not at the plane depth of 1.13 m.
- Frames 36–37 (falling past the edge, heavy blur) are not used. The size there is inflated by the dark background.
- The depth_info value at t = 0.9 s (1.457 m) conflicts with the ball's apparent size at frame 22 (about 37 px, so about 0.81 m). It was not used.

## Answer
Velocity (speed) at frame 34 ≈ **100 cm/s**: about 94 cm/s toward the camera, 28 cm/s to the left and a small vertical part. Both routes give 97–107 cm/s over the 5–6 frame windows ending at 35.
Confidence: moderate, about ±10–15%. The main uncertainty is the depth rate, and how the reference smoothed velocity near the table edge.
