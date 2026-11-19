# q_1327 – average speed of the walking pedestrian, 1.0–2.0 s (m/s)

The file fps (24) is the same as question_fps (24). The window is frames 24–48. This is a 3D Blender scene with a static camera.

## Focal length (main uncertainty)
- **Vertical poles (poles.py, poles_cfg.txt):** I fitted the centre lines of the near double lamp, the far-centre lamp, the near-right
  traffic-light pole and the far-left traffic-light pole on frame 0. They meet at a vertical vanishing point near (1084, ~6900),
  which agrees with the principal point x = 1080. The road vanishing point (curb fits in curbs.py: y between -197 and -229,
  record value -208) gives the horizon. Then f^2 = (y_v - 540)(540 - y_h), so **f ≈ 2160 px**
  (the four poles give 2189, 2096, 2154 and 2179; hfov about 53°).
- **Checks from depth_info (heights.py):** at f ≈ 2100–2200 the pedestrian's pelvis keeps a constant height between
  t = 0.58 s and 1.58 s, and their displacement is perpendicular to the road (they walk along the cross-street sidewalk).
  The cyclist's height is also constant for f ≥ 1500.
- **Prior (white car a = 4 m/s^2), route2.py:** I took the van's motion shape along the road projectively from the rear-bottom
  row and the vanishing point, and its metric length from the two given depths. This gives a = 4.0 at f ≈ 1400 and
  a ≈ 3.78 at f = 2160. The method is weakly sensitive to f: a reference point on the van roof instead of the rear-bottom
  changes it by 5%, and the bbox-centre route in focal.py gives 3.46 at f = 2000. I treat it as consistent to within about 6%.
  f = 1400 would make the pedestrian walk at about 1.9 m/s and conflicts with the pole and height checks.

## Pedestrian speed (ped_speed.py)
- The pelvis proxy from the record is the mask-centroid x and y = bbox_y0 + 0.47 h. I back-projected it with the given depths at
  frames 14 and 38 to set the pelvis height. For every frame I intersected the ray with that horizontal plane.
  This reproduces the given depths: 25.37 vs 25.357 and 25.91 vs 25.92.
- The image motion is steady at about 4.3 px/frame (104 px/s over frames 24–48, the same as the clip mean).
- At f = 2160:
  - net displacement from 1.0 to 2.0 s: 1.240 m/s
  - linear fit over frames 6–66: 1.22 m/s
  - the mean of the raw per-frame speeds (1.44) is inflated by ±2 px jitter in y and is not used.
- A real pelvis adds some vertical bob and side sway, which raises the mean per-frame speed by about 1%.
- **Answer: 1.24 m/s.**
- Sensitivity: about 1/f. The pole estimates (2096–2189) give a range of 1.22–1.28.

## Confidence
Moderate to good. The focal length comes from the pole and horizon geometry and is backed by two depth_info consistency checks.
The car-acceleration prior agrees to within about 6% (weak test).
