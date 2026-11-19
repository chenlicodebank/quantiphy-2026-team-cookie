# q_1434 — acceleration of the gift box at t = 0.2 s (frame 5 at 24 fps)

File fps = question fps = 24. At frame 5 the box is in free fall (frames 0–8, impact on the ramp between frames 8 and 9).
Track: scene/tracks/gift_box.csv body_cx/cy (checked: x is constant at 554 px, per-frame dy 1.89, 5.74, 9.71, 13.25,
17.27, 20.9, 24.4, 28.1 → constant 3.75 px/frame², starting from rest at frame 0). Hull area stays constant during
the fall, so depth is constant.

Scale (pinhole, cx,cy = image centre, depth_info d(0)=9.859 m, d(0.5 s = frame 12)=9.741 m), focal f unknown:
- Route A (prior): `slidefit.py` fits a straight-line constant-acceleration 3D slide starting at P(frame 12)
  (back-projected with d = 9.741) to image points of frames 10–38 (rms 0.3 px), for each f. The prior slide
  a = 3.18 m/s² gives f ≈ 2215 px. At that f the free-fall acceleration is ≈ 9.43 m/s² (linear fit of speeds, frames 1–8).
- Route B (physics check): Blender gravity of 9.81 needs f ≈ 2130 px. At that f the slide acceleration is 3.29
  (3.5 % above the prior). A fall of 0.551 m over 8 frames matches 0.5·g·t² = 0.545 m.
- The single-frame difference at frame 5 is noisy (+7 % above the trend), so I used the trend.

Answer: 9.7 m/s² (between route A's 9.43 and the gravity value 9.81, both within about 3 %). Confidence: good.
