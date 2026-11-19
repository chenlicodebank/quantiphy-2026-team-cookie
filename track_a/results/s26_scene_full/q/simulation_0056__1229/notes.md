# q1229: average speed of the green car, 0-1 s

- The green car is `dark_car` in scene/ (a dark green vintage coupe). I used question_fps = 30, so t=0 is frame 0 and t=1 is frame 30. The file's rate is 29.9936 fps, which makes no difference here.
- I checked the frame 0 and frame 30 crops. The box readings are good: f0 x 1248-1420, roof 1040, wheel bottom 1137; f30 x 1524-1893, roof 1062, wheel bottom 1240.
- Origin pixel: the box centre, (1334, 1088.5) at f0 and (1708.5, 1151) at f30.
- 3D position: P = D x unit ray((u-1024)/f, (v-1024)/f, 1), using the given D = 28.684 m (t=0) and 17.388 m (t=1).
- Average speed is the mean of the per-frame speeds over frames 1-30, which equals the path length over frames 0-30 divided by 1 s.
  - For the path, Z per frame comes from the car's apparent height (Z = a/h + b, pinned to both given depths).
  - Pixel positions get a light 3-frame smoothing before back-projection.

## Focal length (the main uncertainty)
- Purely geometric checks could not pin f:
  - The ground plane, hydrant, lamps and the man give inconsistent results.
  - The horizon from the road vanishing point (y=1050) does not agree with the green car's wheel contacts.
- I used real-size references instead (the scene's assets look real-scale):
  - Man, 1.75-1.80 m tall at 858 px with pelvis D 4.786: f ≈ 2110-2180.
  - Orange car, mirror width about 2.1 m: f ≈ 1650-1810.
  - Green car height, about 1.3 m: f ≈ 1970.
- Chosen value: f = 1950 (horizontal field of view ≈ 55°).

## Results
| f | chord f0→f30 (m) | path (m) |
|---|---|---|
| 1600 | 12.27 | 12.38 |
| 1800 | 12.10 | 12.20 |
| 1950 | 12.00 | 12.08 |
| 2100 | 11.92 | 11.99 |
| 2300 | 11.83 | 11.89 |

- Answer: **12.08 m/s**.
- Second route: the straight-line chord gives 12.00, within 0.7%, so the path is only slightly curved.
- Confidence: about ±3% if f is between 1700 and 2300. If the scene were not at real scale and f were about 1000, the answer would be about 13.4 (+11%).
- The orange car's acceleration prior can't give f, because its motion is almost all along the line of sight.
