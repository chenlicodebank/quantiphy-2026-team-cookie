# q_3108 – height of the walking person (m); prior g = 9.8 m/s^2

Time base: file fps 30 = question_fps 30. The 30 fps result also gives a plausible basketball size (below).

## Scale from gravity (g.py)
I fitted a quadratic to the ball's vertical centre (scene/tracks/ball.csv) during free flight, frames 35–60
(release to just before the bounce at frame 61).
- Raw y: 3727 px/s^2. Camera-compensated y (bg0): 3711. Window 38–58: 3694–3708. Halves: 3813 and 3729.
  Mean second difference: about 3720.
- I adopted a = 3720 px/s^2, so scale = 9.8/3720 = 2.634e-3 m/px.
- Sanity check: ball diameter 94 px x scale = 0.248 m (a real basketball is 0.23–0.24 m). The ball also
  bounces at the same floor row (y ~870) as the walker's feet, so they are at about the same depth.

## Person height in pixels
From scene/tracks/person.csv, cap top to floor contact, frames 73–108. I spot-checked frame 90 on screen.
- The value changes with gait: minimum ~685 px (frames 77–79), maximum ~715 px (frames 91–93), 711 px at
  frame 90.
- Representative value is ~700 px (mean over the frames).

## Answer
- 700 px x 2.634e-3 = **1.84 m**.
- Range from gait: 1.80 (min) to 1.88 (max).
- Includes the cap and the shoes.

Confidence: moderate. The g scale is solid (about ±2 %). The main uncertainty is which gait frame the
annotators measured (±2 %).
