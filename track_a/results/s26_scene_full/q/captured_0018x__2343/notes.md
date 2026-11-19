# q_2343 — velocity of the pineapple toy (yellow plush) at 3.4 s, in cm/s

## Problem
The clip has only 49 frames at 24 fps (0–2.04 s; file fps = question_fps = 24). The asked time, 3.4 s, would be
frame 82, which does not exist. The question's time most likely refers to the uncut recording, but the offset of
this clip within it is unknown. So the answer is a best guess at the toy's speed during its free fall, the event
the question (gravity prior) is about.

## Measurement
- Object: yellow_plush ("pineapple toy": yellow body with green leaves), held by the near person, so I used
  Z = 2.002 m (near_person depth). f = 0.5959 x 1280 = 763 px, principal point (640, 360).
- I used the track from scene/tracks/yellow_plush.csv (bbox centres). Release is at frame 27/28 and floor impact at frame 36. The jump from
  frame 35 to 36 is a dropped frame plus the impact, so I left it out.
- A parabola fitted to Y(frame) over frames 29–35 gives an acceleration of 8.7 m/s^2, which is consistent with the
  9.8 m/s^2 prior (a check on the scale).
- Fitted vertical speed: frame 29 is 163 cm/s, 31 is 236, 32 is 272, 33 is 309, 35 is 382. Raw backward
  differences agree to within about 10 %.
- After impact (frames 37 onward), the speed is 20–130 cm/s while the toy tumbles.

## Answer
270 cm/s, the mid-fall speed (frame 32). The fall speeds range from about 130 to 400 cm/s.
Confidence: low, because the asked time is outside the provided clip.
