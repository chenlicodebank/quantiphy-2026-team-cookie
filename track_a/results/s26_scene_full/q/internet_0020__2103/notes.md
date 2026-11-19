# Q2103 – velocity of the picked bottle at 0.50 s (cm/s)

## Scale
Prior: bottle height = 11.7 cm. On frame 0 (sharp, at rest) the full bottle, from the top of the metal neck (y≈1183) to the base (y≈1820), is 637 px. I checked this on zoomed crops (`frames/f0top.png`, `frames/f0base.png`); the base is uncertain by about ±15 px.
Scale = 11.7 / 637 = 0.01837 cm/px.
(If the 11.7 cm were only the glass body, 453 px, the answer would be about 97 cm/s. I rejected this: "height of the bottle" is read as the whole bottle.)

## Time base
The file is 19.5946 fps (an odd rate, 725/37); question_fps is 25. The clip looks re-timed, so I used the original 25 fps footage rate. t = 0.5 s → frame 12.5 → frame 12 (forward difference to frame 13). Both rates give plausible hand speeds, so this choice is the main risk. Under the file rate, the answer at frame 10 would be about 44 cm/s.

## Motion measurement
I took differences against frame 18 (the bottle is gone there), with camera drift compensated (`diffzoom.py`, `frames/dz1.png`, `frames/dz2.png`). I read the lowest end of the bottle's blur streak on each frame:
8:1475, 9:1385, 10:1255, 11:1145, 12:1000, 13:865, 14:700, 15:550, 16:350 (image y).
- Per-frame steps: 90, 130, 110, 145, 135, 165, 150, 200. A linear trend gives about 147 px/frame vertical at frames 12→13.
- Sideways drift of the centre is about 25 px/frame, and camera drift adds about 1.7 px/frame.
- Combined: about 150 px/frame.

## Second route
The centre track in scene/tracks/bottle.csv (midpoint of neck top and base) gives these frame-to-frame steps: 10→11 159, 11→12 150, 12→13 144 and 13→14 165 px/frame, averaging about 155. This agrees with the streak route.

## Answer
v ≈ 150–152 px/frame × 25 fps × 0.01837 cm/px ≈ 69 cm/s.

Confidence: moderate. The measurement is good to about ±7%. The main uncertainties are the fps choice and which part of the bottle the 11.7 cm prior refers to.
