# q_3217 – gap between the ball's bottom and the floor at 3.5 s (frame 105)

Time base: the file and the question both use 30 fps, so 3.5 s = frame 105. A gravity fit at 30 fps gives a ball diameter of 0.235 m, which is a plausible basketball size.

## Scale from the gravity prior
- I fitted parabolas to the ball centre `cy` from `scene/tracks/ball.csv`, after checking the track on frames (script: fit.py).
  - Flight 1 (frames 81–113): 3539 px/s².
  - Flight 2 (frames 116–143): 3531 px/s².
  - With camera drift removed (`cy_bg`): 3546 and 3558 px/s².
  - I used 3540 px/s².
- Scale: 9.8 / 3540 = 0.002768 m/px.

## Pixel gap at frame 105
- The ball centre is at cy = 448.0. Its radius is about 42.5 px (sharp-edge diameter 85 px). That puts the bottom at about 490.5; the mask bbox gives y1 = 488, and the zoomed frame shows about 490.
- Floor level is the height of the ball's bottom where it touches the floor. The ball lands in front of the baseboard at frame 114.
  - On the zoomed frame 114, the bottom of the blurred ball is at about 1050–1055.
  - The two free-flight parabolas intersect at a centre height of 1016. Adding r gives 1058.
  - I used 1053.
- Gap: 1053 − 490.5 ≈ 563 px, which gives 563 × 0.002768 = **1.56 m**.

## Checks
- Second route: scaling by the ball itself (85 px for a 0.24 m basketball) gives 0.00282 m/px and a gap of 1.59 m. This agrees within 2 %.
- Other reading: if "floor" meant the floor/baseboard line at y ≈ 1015, the gap would be 525 px, or 1.45 m. I rejected this because the ball touches the floor in front of the wall, at about y ≈ 1053.

Confidence: moderate to good, about ±5 %. Most of the uncertainty is in the pixel level of the floor contact.
