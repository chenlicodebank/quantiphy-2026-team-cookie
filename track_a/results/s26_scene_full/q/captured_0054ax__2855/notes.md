# Q2855 – orange ball (basketball) displacement 0.5 s → 1.0 s

File fps = question_fps = 24, so the frames are 12 and 24.
Lab camera: f = 0.5959·1280 = 762.8 px, principal point (640, 360).

Centres from scene/tracks/basketball.csv, checked by eye on zoomed crops (frames/f05.png, frames/f10.png):
- f12: circle-fit centre (343.7, 607.1), r 38.6 px. The ball is free and the whole ball is visible.
- f24: circle-fit centre (585.3, 681.1), r 46.5 px. The ball is cut by the bottom edge, so I used the circle fit.
  In the crop the sides are at x≈539–632 and the top at y≈633, which agrees.

Back-projection: the unit ray is scaled by depth_info, treating depth as the Euclidean distance to the centre.
- P(0.5) = (-0.817, 0.681, 2.102) m
- P(1.0) = (-0.119, 0.701, 1.665) m
- Displacement = **0.823 m**

Checks:
- Using the mask centroid instead of the circle centre gives 0.8225 m.
- The implied ball diameter is 0.239 m at f12 and 0.221 m at f24, which is plausible for a basketball.
- Prior: 2.21 m/s at 0.5 s. The average speed over the interval is 1.65 m/s, and the per-frame speed near f12
  ranges from about 1.7 to 2.5 m/s (there is a 31 px jump between f11 and f12). That is roughly consistent.

Confidence: high. The answer depends mainly on the two depths given in depth_info.
