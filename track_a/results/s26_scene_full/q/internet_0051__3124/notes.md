# q_3124 — height of the person riding the scooter (m)

Prior: average speed of the rider = 2.07 m/s. Internet video, 30 fps (file and question_fps agree), planar convention:
one scale = 2.07 m/s / pixel speed.

## Pixel speed
From scene/tracks/rider_scooter.csv (bbox centre, slow pan removed): cx_bg 1414.5 -> 551.5 over 49 frames
= 17.61 px/frame = 528.4 px/s, nearly constant (first/last 10 frames 17.55 / 17.85).
Scale = 2.07 / 528.4 = 0.003918 m/px.
Alternatives: raw image coords (no pan correction) 849 px -> 519.8 px/s; template matching 854 px -> 522.9 px/s.

## Pixel height of the person (cap top to shoe soles on the deck)
Read on 3x crops with 10 px ticks (crops.py, frames/c0, c24, c49):
frame 0: 554 -> 852 = 298 px; frame 24: 557 -> 852 = 295 px; frame 49: 553 -> 853 = 300 px. Mean ~298 px
(scene record: ~300 px; rider+scooter to wheel bottom 322 px).

## Answer
298 px x 0.003918 = 1.167 m -> **1.17 m**.
Second route: template-matching / raw-coordinate speed gives 1.18-1.19 m; including the scooter (322 px) would give 1.26 m
(not the person's height). Sanity: 1.17 m is short for an adult (scooter wheel ~45 px suggests a larger scale), so the
prior speed seems low in real-world terms, but the prior is exact by convention and sets the scale. Confidence moderate.
