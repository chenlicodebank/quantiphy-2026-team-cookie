# Q379: speed of the ball at t = 2 s

- 2D side view, static camera. fps = question_fps = 24, so t = 2 s is frame 48.
- Scale comes from the prior (ball diameter 0.21 m). The fitted diameter near frame 48 is 80.5–81.4 px
  (scene track: frames 40–60 give 80.2–81.8 px). My own background-difference chord measurement gives 81 px at frame 47.
  I used D = 81.0 px, so the scale is 0.21/81.0 = 2.593e-3 m/px.
- Ball centre x (scene track): 598.42 (frame 46), 622.76 (47), 647.34 (48), 671.78 (49), 696.20 (50).
  The backward step at frame 48 is 24.58 px. The mean of the four steps around it (frames 46→50) is 24.45 px/frame.
- Second route (measure.py): an independent background-difference mask, using the median mid-point of the left and right edges
  over rows 612–667. It gives steps of 24.5 px for 47→48, 48→49 and 49→50, and (744 − 551)/8 = 24.1 px/frame across frames 44–52.
- Speed = 24.45 px/frame × 24 fps × 2.593e-3 m/px = 1.52 m/s. If D = 81.5 px, the result is 1.51 m/s.
- Confidence: good, about ±3%.
