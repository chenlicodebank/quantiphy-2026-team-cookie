# q_643: long side of a marked parking space (m)

Prior: big robot (blue tank) speed = 5.924 m/s, i.e. 0.24683 m per frame at 24 fps (file fps = question fps = 24).

## Scene geometry (frame 48, tank gone; `geom.py`)
- The parking strip runs along the back wall. The far white lane line is at y≈842.7 and the near one at y≈908.5.
  Two white divider stripes (x≈515-690 and 1610-1810) cross the strip and mark one stall.
- The divider edges, fitted per row, converge at a vanishing point of about (960, 551), which is about the principal
  point. So the dividers are perpendicular to the wall and the camera is level, looking squarely at it. The stall's
  long side is therefore along image x, and on the ground plane its pixel length is proportional to (y − y_horizon).
- Divider centreline to centreline: 1038.8 px at y=850 and 1219.3 px at y=902, so k = Δx/(y−yh) = 3.4715.
  Inner edges give k = 3.254 and outer edges k = 3.689. Each divider stripe is about 0.22 k-units wide.

## Scale (`track_near.py`)
- The tank translates purely in x (bottom row constant, linear tracks), so every rigid point has the same 3D speed,
  and the m/px at any depth is 0.24683 / (pixel speed of points at that depth).
- NCC tracking of the near-side track face over frames 9-32 gives: emblem 50.76, wheel 2 50.78, wheel 3 50.78,
  track-bottom strip 50.78 px/frame (residuals ≤ 0.5 px). At the near-track depth, 0.24683/50.77 = 0.0048618 m/px.
- The near track's ground contact (bottom silhouette) is at y ≈ 894.5 ± 1. At that row the stall measures
  k·(894.5 − 550.8) = 1193.2 px. Evaluating at this row makes the horizon estimate nearly irrelevant.

## Result
- Centreline to centreline: 1193.2 × 0.0048618 = **5.80 m** (the answer).
- Other readings: between the inner edges of the paint 5.44 m; between the outer edges 6.16 m.

## Checks
- The camera height comes out at h = 5.80/3.47 = 1.67 m. The divider paint is about 0.36 m wide.
- Assuming the lane lines have the same paint width, their image thickness (about 4.5 px far, 6.5 px near) gives a
  focal length of about 4100 px from each line, and the two agree. With that focal length:
  - the near track is about 20 m from the camera;
  - the tank is about 3.0 m long and 3.0 m high, and about 2.1 m wide (from the far-side speed of about 46 px/frame);
  - the stall is about 4.3 m deep, shorter than 5.8 m, which confirms that the side along the wall is the long side.
- Confidence: the scale is good to about 1%. The main uncertainty is the convention (centre vs inner/outer edges, ±6%).
