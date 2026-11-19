# Q1511: distance from the man's foot to the left wall (m), simulation_0141

The file and the question both run at 24 fps, so no time-base conversion was needed. The camera is static and its optical axis runs along the corridor. The vanishing point is at (960, 539), and the horizon row is 536–539.

## Geometry (scripts: bg.py, wall.py, seams.py, tiles.py, answer.py)
- **Left wall–floor line** (wall.py): I fitted it to 109 of 111 edge points, with an rms error of 0.3 px: y = -0.2796 x + 807.6. The line passes through the vanishing point (960.6, 539), so it is a straight line on the floor parallel to the corridor.
- **Lateral positions:** for a floor point, lateral X = c · h_cam with c = (x-960)/(y-539). This gives:
  - wall: c = -3.574
  - planted foot, using the lowest sole point from the track (checked on zoomed frames): c = -0.573 (frame 0), -0.660 (frame 12), -0.579 (frame 24), -0.665 (frame 36), -0.538 (frame 48). The right foot is about 0.1 · h_cam closer to the image centre than the left foot.
  - So distance = (c_foot - c_wall) · h_cam = 3.00 · h_cam at t = 0. The mean over both feet is 2.97 · h_cam, so the man keeps a near-constant distance from the wall.
- **Floor tiles:**
  - The transverse seams are evenly spaced in 1/(y-539), with a step of 0.000249. This confirms the horizon row.
  - Longitudinal seams fall at c = -1.514, -0.808, -0.102, 0.604, 1.310, a constant step of 0.706.

## Scale
- **Depth along the corridor, K = f · h_cam:**
  - From the walking-speed prior: foot-contact rows step by 0.000357 in 1/(y-539) every 12 frames (0.5 s), giving K = 1.693 × 0.5 / 0.000357 = 2371.
  - The change in the given depths agrees: 0.88 m over the same 12 frames.
  - If the tiles are 0.6 m deep, K = 2410.
- **Absolute depths don't fit the floor geometry.** The stance foot at mid-stance puts the man at Z ≈ 4.7 m (frame 0) and ≈ 5.6 m (frame 12). The given depths (4.15 and 5.03) are about 0.55 m smaller at both times. The offset is constant, so the depths fix the depth scale (through their difference) but cannot fix the focal length. In fact the depths, the speed and the image together leave the focal length almost undetermined: the radial correction is only 1–2 %, which is below the noise.
- **Lateral scale (h_cam) therefore needs a size assumption:**
  - **Route 1, man's height.** The horizon crosses the man at a fixed fraction of his head-to-sole height: h_cam = 0.717 × H_walk, consistent across frames 0, 12, 24, 36 and 48. Taking an adult man about 1.78–1.80 m tall standing (H_walk ≈ 0.98 of that) gives h_cam = 1.25–1.27 m and f ≈ 1900 px (horizontal field of view about 54°). His 0.85 m steps at 1.7 m/s fit a man of this size.
  - **Route 2, floor tiles.** Tiles 0.6 m deep and 0.9 m wide (aspect 1.5) give f = 1890 and h_cam = 1.275. Route 1 independently predicts this aspect (1.49).
- **Result at t = 0 (planted foot):**
  - route 1: 3.75–3.80 m (H = 1.78–1.80); H = 1.75 gives 3.69 and H = 1.85 gives 3.90
  - route 2: 3.83 m

## Answer
**3.78 m** (planted foot at t = 0; the mean over both feet and the whole clip is about 3.74).

Confidence is moderate. The scale rests on the man's assumed height (or the tile aspect), giving roughly ±5 %. Which foot is meant adds about ±2 %. If someone trusted the absolute depths, the answer would come out about 4.1 m, but those depths contradict the floor geometry as described above.
