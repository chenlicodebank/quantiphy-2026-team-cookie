# q_2758: velocity of the white ball (the white toy) at t = 1.5 s, in cm/s

- t = 1.5 s is frame 36 (question_fps 24 = the file's fps). The "ball" is the white oblong toy, the only moving object.
- Lab camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).
- Depth: 0.7045 m at frame 36 and 0.627 m at frame 48. I interpolated linearly in between and extrapolated the same line
  to frames 34-35, which gives about -6.5 mm per frame (about 15.5 cm/s toward the camera).
- Centroids come from scene/tracks/white_toy.csv. I checked frames 33-36 on 4x crops (view2.py, frames/seq2.png):
  - Frames 34 and 35 are partly behind the card tent, but the recorded centres (658, 436) and (693, 398) agree with the visible toy to within a few px.
  - Frame 33 is hidden and was not used.
- Each centre was back-projected along its ray to the depth given (vel.py).
- Pixel motion around frame 36 is irregular:
  - 35→36 is 73 px, about twice the 36→37 step (32 px). The toy jumps from the tent top to above the cup rim in one frame, perhaps a dropped capture frame.
  - From 36 to 40 it moves a steady 33-37 px/frame horizontally.
  - The apex of this arc is near frame 36.
- Estimates of the speed at frame 36 (vel.py, vel2.py), in cm/s:
  - 5-frame vector-smoothed forward difference, (p39 - p34)/5: 85.8
  - (p40 - p35)/5: 85.9
  - (p41 - p36)/5: 88.6
  - Centred (p38 - p34)/4: 95.3
  - Quadratic fits over frames 34-38, 34-39 and 34-40: 98
  - Mean of the scalar forward speeds over d34..d38: 110 (pushed up by the 35→36 jump)
  - Single 36→37 step: 70
- Answer: 92 cm/s, the middle of the 86-98 cluster of smoothed estimates.
- Confidence: moderate, about ±12%. The spread comes from the irregular 35→36 step and from not knowing the exact
  smoothing the reference used.
