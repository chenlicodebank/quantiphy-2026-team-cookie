# q_675 — speed of the vacuum cleaner at t = 0.5 s

The file and the question both run at 24 fps, so t = 0.5 s is frame 12. The speed is the backward difference between frames 11 and 12.
This is a 2D render from a top-down camera. The only moving object is the white round robot vacuum, and it is also the prior's object (diameter = 0.438 m).

## Position (motion)
- `measure.py`: threshold gray > 190, then the largest component near the robot, then a robust circle fit to its contour. Centres are (1613.06, 410.06) at frame 11 and (1601.11, 407.89) at frame 12, so the step is **12.15 px**. The overlay is `frames/my_f12.png`: the circle sits on the bright top.
- The scene record (`scene/tracks/robot_vacuum.csv`) gives a frame 11→12 step of **12.17 px**, which agrees within 0.2 %. Its neighbouring steps (11.29, 12.17, 13.33) show a smooth acceleration of about 1 px/frame², with no event near frame 12.
- SAM 3 (box-prompted "white disc", k = 0, score 0.97) gives mask centroids (1612.2, 410.5) → (1600.5, 408.3), a step of 11.9 px (2 % lower). The SAM mask includes the soft shadow and the lit side rim, so its centroid is slightly biased. I used the circle-fit centres.

## Scale (diameter in pixels)
- `profile.py` reads intensity profiles through the centre at frame 12 and at frame 75 (stationary, nearer the image centre). I took the edge at the mid level between floor (~120) and disc (~199), i.e. level 160:
  - frame 12: vertical 120.0 px. Horizontal is 123.4 px, but the left side has a gradual ramp: the cylinder's side wall is visible through perspective, because the robot is 640 px right of the image centre. I excluded that axis.
  - frame 75: horizontal 120.0 px, vertical 119.0 px.
  - So the diameter is **120 px (±1)**.
- The disagreements are over 3 %, so I looked at the zoomed frame (`frames/f12.png`, `frames/my_f12.png`) to decide:
  - The record's circle fit (117.8 px) and my gray > 190 fit (117.1 px) put the edge at a high threshold, so they sit about 1 px inside the antialiased rim. That makes them about 2 % small.
  - SAM's extents (130 × 127 px) include the dark contact shadow and the side rim, so they are about 7 % too large.
  - The mid-level edge (120 px) matches the visible rim on the zoomed frame.
- The scale is 0.438 / 120 = 3.65e-3 m/px.

## Answer
The speed is 12.16 px/frame × 24 fps × 0.438 / 120 m/px = **1.065 m/s**.

## Checks
- **Second route:** with the record's 117.8 px circle diameter the result would be 1.085 m/s (+1.9 %). With the SAM centroid step it would be 1.04 m/s.
- **Perspective:** the top face and the origin height differ in scale by less than 1 %, judging from the about 6 px side band at 640 px off-centre.

Confidence: high, within about 2 %.
