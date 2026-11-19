# q 2878: orange ball displacement 0.5 s -> 1.0 s

- Orange ball = `basketball` track in scene/. Frames 12 (t=0.5) and 24 (t=1.0) at question_fps 24 (the file is also 24 fps). I confirmed both on frames: the ball is clean and unoccluded in each.
- Lab camera: f = 0.5959*1280 = 762.8 px, (cx, cy) = (640, 360).
- Centres (px): f12 (716.8, 534.6), f24 (537.9, 384.6) from the record. My own HSV orange mask in measure.py gives the same within 1-2 px: centroid (716.5, 536.3) / (537.9, 385.8).
- Back-projection: unit ray x depth_info distance (Euclidean camera distance) = 2.24 m at 0.5 s and 1.81 m at 1.0 s.
- Displacement = |P24 - P12| = **0.740 m**. The own-mask centroid gives 0.740 and the own min-enclosing circle 0.739.
- Variant: if the depth is read as the Z coordinate instead, the result is 0.781 m (+5.5 %). I used the Euclidean reading because that is how the task defines depth_info.
- Prior check: with depth interpolated linearly, the speed near 0.5 s is 1.8-2.7 m/s depending on the window (the release is at about frame 11 and a frame was probably dropped at 11->12). A 10-15 window gives 2.14, consistent with the prior of 2.21 m/s.
- Caveat: the apparent diameter shrinks from 76 to 60 px, which suggests the ball moves away from the camera, while depth_info says it gets closer. I followed depth_info, as the reference does.
- Confidence: good under the given depths (about ±2 %).
