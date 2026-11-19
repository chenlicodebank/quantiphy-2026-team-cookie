# Q3178: ball-to-floor distance at t = 1.40 s (frame 42, 30 fps; the file and the question both use 30 fps)

## Scale from the gravity prior (fit.py)
- I fitted a parabola to the ball centre's y (scene/tracks/ball.csv, free flight from frame 23 to 63):
  - Raw coordinates: 2000 px/s².
  - Stabilised coordinates: 2001 px/s².
  - Rising part only (frames 23-42): 2008 px/s². Falling part only (frames 42-63): 1920 px/s².
  - Median second difference: about 1970 px/s².
- I used 2000 px/s². Scale = 9.8 / 2000 = 0.00490 m/px.
- Sanity check with this scale: the ball's 50.4 px diameter gives 0.247 m (a real basketball is about 0.24 m). The
  player's 344 px standing height gives 1.69 m. Both are plausible.

## Positions at frame 42 (the apex)
- Ball centre: raw y = 30.3 px. Ball radius: about 25.5 px, so the ball's bottom is at y ≈ 55.8 px.
- Floor under the ball: the ball is directly above the player, at her depth. Her shoe soles are at y ≈ 890-892, read on
  the 3x zoom `frames/feet42.png`; the person track gives 892.5. I used 891 px.
- Ball centre to floor: 861 px × 0.0049 = 4.22 m.
- Ball bottom to floor (the gap): 835 px × 0.0049 = 4.09 m.

## Answer
4.15 m, the midpoint of the two readings, which is within 1.6 % of each.

## Uncertainty
- The g fit varies by about ±2 % (rising part against falling part).
- The floor line is ±3 px.
- Confidence is moderate to high.
