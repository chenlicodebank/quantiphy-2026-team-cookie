# q_1356 — average speed of the walking pedestrian, beginning to end (m/s)

Answer: **1.18 m/s**

File fps = question_fps = 24. Frames 0 and 1 are identical in the video, so motion runs from frame 1 to frame 71.

## Method
- I used the pedestrian track from scene/tracks/pedestrian.csv: the bbox centre (`ref`) and the head top (`top`). I checked
  the frames by eye: it is the man in the white T-shirt on the right sidewalk, and he is never occluded.
- Anchor (exact scale): depth_info gives the camera-to-pelvis distance at t=0.58 s (frame 14) = 21.677 m and at
  t=1.58 s (frame 38) = 22.7825 m. Back-projecting the pixel points with these depths gives a 3D displacement of
  **1.19–1.21 m over 24 frames**. This barely depends on the focal length (f=800–1400 px: 1.188–1.220) or on which
  body point is used, because the motion is mostly a change in depth. So the speed over 0.58–1.58 s is about 1.20 m/s.
- Full clip: I intersected the rays with a horizontal plane (horizon y=-47 px from scene.json; the plane height comes
  from the two given depths) to get the 3D path for frames 1–71. With head top + 50 px and f=1000, the given depths are
  reproduced exactly (21.677 and 22.783 m).
  - Average speed over the whole clip relative to the 14–38 window: 0.967 (head-top track) and 0.960 (bbox-centre
    track). Head-top track: 1→71 net = 1.163 m/s, linear fit 1.176 m/s, quadratic-fit mean 1.176 m/s.
  - Net-displacement estimate: ≈1.20 × 0.963 ≈ 1.165 m/s.
  - A mean of per-frame speeds (the benchmark convention) adds about 1–2 % for the pelvis's sideways sway and vertical
    bob in a walk cycle. Averaging over 71 instead of 70 frames (counting the duplicated first frame) would take
    about 1.4 % off. These roughly cancel, so the answer is about 1.17–1.18 m/s.

## Focal-length checks (calib.py)
- Ground-plane consistency of the four objects between frames 14 and 38 is a weak constraint on f (roughly 1000–1400).
- The white-car prior (a = 4 m/s², from rest at frame 1, so 4.15 m between frames 14 and 38) points to f ≈ 1350.
- The answer depends weakly on f: within ±5 % over this range.

## Confidence
Moderate to high. The answer is about ±5 %, and the main uncertainty is how the speed is averaged over frames outside
the 14–38 anchored window.

Scripts: calib.py, ped.py, ped2.py.
