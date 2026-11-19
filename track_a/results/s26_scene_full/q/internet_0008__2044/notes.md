# Q2044 — average speed of the sailboat (prior: sailboat length = 12 m)

Internet video, 960x540, 30 fps (file fps = question_fps = 30). Camera treated as static: the horizon stays at row 437 in every frame,
and the sea texture (-0.2 px/fr, waves) and the sun (+0.1 px/fr) drift in opposite directions, both small, so this is not a pan.

## Measurement (measure.py -> my_track.csv, mask overlays frames/mask_*.png)
I made my own dark-silhouette mask (pixels more than 25 below the row-wise background) on every frame, 0–528, and checked it on the overlays.
- Horizontal speed in px/frame from a linear fit (net displacement over 528 frames in brackets):
  - bbox left: 1.070 (564 px); bbox right: 1.080 (568 px)
  - my mask left: 1.072 (560 px); my mask right: 1.083 (570 px)
  - main mast: 1.073 (567.5 px); centroid: 1.077 (567 px)
  - Every reference point gives 1.07–1.08 px/frame, so I used 1.075 px/frame = 32.25 px/s.
  - The mean of the raw |per-frame differences| is 1.1–2.1 px/frame, but that is inflated by ±1–2 px mask jitter, so I did not use it.
    The motion is steady with no vertical component.
- Length in px (bowsprit to stern, along the motion): the median of my mask is 102 px (it grows from 100 to 106 px over the clip). The
  record's bbox median is 105 px. The hull alone is 101 px. I used L = 103.5 px.
- Scale: 12 / 103.5 = 0.1159 m/px.

## Answer
32.25 px/s x 0.1159 = **3.74 m/s**.

Second route: net displacement / time using the mast, 567.5 px / 17.6 s = 32.24 px/s, gives the same speed.
The sensitivity comes from the length: L = 102 px gives 3.79 m/s and L = 105 px gives 3.69 m/s.
Confidence: good, about ±3 %.
