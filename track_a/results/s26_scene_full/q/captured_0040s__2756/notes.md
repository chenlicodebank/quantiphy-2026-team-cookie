# q_2756 – velocity of the white ball at 1.4 s (cm/s)

Time base: question_fps = file fps = 24, so t = 1.4 s → frame round(33.6) = **34**. That is just after the
first bounce, which happens at frame 33 (an image-y minimum).

## Track
I used the scene/ ball centres (scene/tracks/ball.csv). I checked frames 32–37 in zoomed crops (zoom.py, crops.py,
frames/*.png) and the centres agree within a few px. In frames 32 and 34–35 parts of the ball are hidden by the
SAM2-composited tape/card tent. The composite order is not reliable for depth. There is frame-timing jitter: the
step from frame 35 to 36 is 60 px, against 31–36 px for the steps that follow.

## Depth / scale (method card: f = 0.5959·1280 = 762.8 px, principal point (640, 360))
- depth_info: radial distance 0.7045 m at frame 36 and 0.627 m at frame 48. Converted to camera z: 0.697 and 0.507.
- Ball width_minor × z_cam gives K = 27.3 at frame 36 and 27.7 at frame 48. These agree, so the ball size is
  consistent with the given depths (D ≈ 3.6–4 cm). A size-based linear z(t) fit gives a slope of −0.0072 m/frame.
- Depth models for frame 34: z_cam is 0.728 when extrapolated linearly from the frame 36–48 trend, and 0.711 from
  the size-based slope anchored at frame 36.
- Sanity check: a ballistic fit of flight 2 (frames 34–40, X and Z linear, Y quadratic) gives g ≈ 10.1–10.6 m/s²,
  so the metric scale is right.

## Velocity at frame 34 (scripts vel.py and smooth.py), in cm/s
| route | lin36_48 depth | size-fit depth |
|---|---|---|
| raw forward difference 34→35 | 128 | 121 |
| 5-frame centred mean of the velocity vector (spans the bounce, so the vertical part cancels) | 109 | 102 |
| 5-frame mean of scalar speed | 138 | 131 |
| ballistic fit of flight 2, speed at frame 34 / 34.5 | 150 / 132 | 148 / 130 |

All routes fall between 100 and 150 cm/s. The spread comes from two things: the bounce sits right inside the
required ≥5-frame smoothing window, and the frames are unevenly spaced in time.

## Answer
**115 cm/s.** This is a compromise between the smoothed forward difference (about 105, the reference convention)
and the instantaneous post-bounce speed (about 125–145).

Confidence: low to moderate. The answer depends on how the reference smoothed velocity across the bounce.

Unresolved inconsistency: the bounce point's image y (about 483–500) would put the table contact at about 0.9 m
under a level-camera table model. Ball size and depth_info both say about 0.70 m. I followed depth_info.
