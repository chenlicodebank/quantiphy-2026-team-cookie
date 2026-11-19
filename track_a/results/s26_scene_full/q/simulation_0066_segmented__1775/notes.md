# q1775 — length of the green car (simulation_0066_segmented)

Prior: white car (van) acceleration = 4 m/s². Depths at t=0.58 s (frame 14) and 1.58 s (frame 38) for the human, the yellow car, the white car and the bike. File fps = question fps = 24.
The green car is the parked teal sedan, upper right. It is static: bbox x 1441–1625, y 334–414 on frame 0. It is seen from the front-left at about 43° to the line of sight.

## Camera (pinhole, principal point at image centre)
- **Back-projection:** each object is back-projected with its given depths at frames 14 and 38.
  - Van: smoothed mask centroid.
  - Pedestrian: the record's centroid is biased at frame 14 because the leg is detached and the mask is truncated (bh 71 instead of ~90). I used the head top y0 + 46 px as the pelvis, with x from a linear fit of cx (`joint3.py`).
- **Focal length f**, from three routes:
  1. Van ⟂ pedestrian ground plane with zero camera roll: f ≈ 935 (±100; 1 px of pedestrian error moves f by ~65).
  2. Van motion: positions are the centroid ray intersected with the van-origin plane (`vanplane.py`), or the line through P14 and P38 (`focal2.py`). A quadratic fit gives a = 4 at f ≈ 900–1050, depending on the frame window, with start time t0 ≈ 0.
  3. Street-grid check: the green car's axis is perpendicular to the van path (86–90°) and parallel to the pedestrian path at f = 900–1000 (`angles.py`).

  Adopted f ≈ 960 ± 50 px. The camera tilt is ~28° down.
- **Ground plane:** the pedestrian's feet (bbox bottom, frames 8–65) below the pelvis give a pelvis height of ~0.93 m, so the camera is ~7.4 m above the ground. Checks: van origin height ≈ 0.8 m; pedestrian walking speed ≈ 1.15 m/s.

## Green car (`carlen2.py`, overlay `drawbox.py` → frames/box.png)
- **Car axis and wheelbase:** the wheel contact points, front-left (1514, 413) and rear-left (1593, 397), are intersected with the ground. Wheelbase ≈ 2.40 m and the car is ~22.6 m away.
- **Rear end:** the rightmost silhouette edge (x = 1625, the rear-left corner) is intersected with the car's left side plane.
- **Front end:** the front-left corner (orange indicator / corner edge at x ≈ 1499 ± 3) is intersected with the same plane.
- **Length vs focal length:** L = 3.98 (f=850), 3.87 (900), 3.82 (920), 3.76 (950), 3.67 (1000) m. An inset of 0.05–0.10 m changes L by < 0.02 m. A ±3 px corner pick changes it by ±0.09 m.
- **Width:** from the front-right corner, ≈ 1.65 m (sanity check).
- **Result:** at f ≈ 960, L ≈ 3.74 m. I added ~0.05 m because the centres of the front and rear bumpers protrude slightly beyond the corner points used. Answer: **3.8 m**.

## Confidence
Moderate. The focal length is the main uncertainty (±5% in f gives ±5% in L), followed by the corner picks. Expected error is about 5–8%.
The car's beltline looks slightly flatter than the modelled axis lines. I attribute this to the car model's styling; the wheel-contact yaw is consistent with the street grid.
