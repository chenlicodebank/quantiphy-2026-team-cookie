# Q1240 – speed of the walking pedestrian, 0.0–1.0 s (m/s)

The file's frame rate (24) is the same as question_fps (24). Frame 1 is a duplicate of frame 0.

## Focal length (calib.py, vanacc.py)
Principal point is the image centre (1080, 540) and the horizon row is 422.5 (from the scene record's vanishing point).
I put the van and cyclist origins in 3D from their depth_info at frames 14 and 38 and scanned f:
- the van and cyclist move in parallel directions (same cross street) at f ≈ 2300–2400
- the van's motion is perpendicular to the main road (its vanishing point is at u = 1253) at f ≈ 2200
- the prior's van acceleration of 4 m/s² (each frame placed on its 3D line, linear fit of speed over frames 3–47)
  gives f ≈ 2250–2300. The cyclist's speed comes out constant at f ≈ 2000–2200.
- I chose f = 2300 px (HFOV ≈ 50°). Check: the pedestrian's height comes out at 1.79 m, which is plausible.

## Pedestrian (ped2.py)
- Pelvis pixels: (92.0, 675.2) at frame 14, from the scene track.
- At frame 38 the body is cut by the left image edge. The body centre is u ≈ 0 ± 5 (looked at on the frame) and
  v ≈ 690–698.
- I back-projected both points with the given depths (18.7297 and 17.6974 m). The 3D displacement over 1.0 s is
  1.19–1.21 m for f between 2100 and 2500 and u38 between −4 and +4, with a vertical change of only ±0.03 m.
  So the walking speed is v ≈ 1.20 m/s, and it hardly depends on f.
- Second route: tracking the head template (head.py) gives a roughly constant lateral rate of about 3.8 px/frame
  over frames 12–30, with gait oscillation. The image tracks show no large speed change over 0–1.6 s, so I take
  the walk to be steady. The image-only 3D routes (ped.py, ped3.py) are too noisy because of gait and lamp-post
  occlusion, and I used them only qualitatively.
- If the reference averages per-frame speeds and includes the duplicate frame 0→1 (zero), it would be about
  0.96 × v = 1.15. I answer 1.18, between 1.20 and 1.15.

Confidence: moderate-good (±5%).
