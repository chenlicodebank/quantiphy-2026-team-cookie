# q_2360 — diameter of the white jar (cm)

File fps = question_fps = 24, so t=0.60 s -> frame 14 (the release frame, jar just leaving the near person's hand).
Camera: lab card, f = 0.5959*1280 = 763 px, principal point (640,360). Depth at frame 14: jar 1.9735 m.

## Object
The "white object" in scene/ is the jar: a short white cylinder with a lid. Frames 4-5 (held, nearly still) show it
clearly: the lid ellipse is ~33.5 px across its major axis, and the jar's height is visibly smaller than its diameter.

## Measurement (rows.py, profile2.py)
Rotated profiles perpendicular to the motion direction (motion blur only stretches along the motion), score =
min-RGB minus the local background, edge at 40 % of the bright plateau, one row every 2 px along the motion:
- frame 13: 30-32 px (clean rows)
- frame 14 (stated time): 33.0-33.8 px on the rows clear of the hand (s = 0..+14)
- frame 15: 27 px, frame 16: 29.5 px, frame 17: ~31 px (the jar tumbles, so the width changes a little)
Lowering the threshold to 50 % takes about 1 px off.

Main route: D = 1.9735 x 33 / 763 = 8.5 cm (8.3 cm with a 32 px width at the 50 % edge).

## Second route: 3D ballistic fit (ballistic.py, plus a fit with gravity's direction fixed)
Fitted the jar's free flight (frames 15-26, skipping 18-19 where it crosses the toy): g = 9.8 m/s^2, gravity's
direction from the vertical vanishing point in scene/, |P(14)| = 1.9735 m. Residuals rms 3.6 px (gravity direction
free) and 5.8 px overall with it fixed, but at most ~4.6 px for the jar. With it fixed, the catch distance comes out
~3.1 m, which fits the far person at 3.24 m.
Fitted distances: 15: 2.01-2.03, 16: 2.06-2.09, 17: 2.13-2.15 m.
Sizes from these: f15 7.1, f16 8.0-8.1, f17 8.6-8.7 cm; frame 13 (depth ~1.93) gives 8.0 cm.
Mean of frames 13, 14, 16 and 17 is about 8.3 cm. Frame 15 (7.1 cm) is likely a moment of tumbling where the
narrower height-side extent faces across the motion.

Sanity check: the lid ellipse at frame 4 is ~33.5 px, the same as frame 14, so the jar would have to be at a similar
distance then. That is plausible but could not be checked (no depth is given at frame 4).

## Answer
8.4 cm (main route 8.3-8.5, the other frames 8.0-8.7). Confidence moderate (about ±8 %): the main
uncertainties are the edge threshold on a blurred, partly shaded object and tumbling.
