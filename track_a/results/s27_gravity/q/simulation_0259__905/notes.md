# q_905 — height of the mug (simulation_0259, 2D)

File fps = question_fps = 30.

## Scale from the prior (red cup falls at 9.8 m/s^2 before 0.5 s)
`measure.py` fits a quadratic to the cup track (scene/tracks/cup.csv, free fall frames 0–14; first impact at frame 15 = 0.5 s):
- centre (bbox cy / centroid): 6.94–6.96 px/frame^2 = 6248–6266 px/s^2
- top_y: 7.03 px/frame^2 = 6323 px/s^2; bottom_y 6170–6210 (underside ellipse shrinks during the fall)
The origin is the centre, so I use 6260 px/s^2 -> 9.8 / 6260 = 1.566e-3 m/px.
The cup width stays 42–43 px for the whole fall, so its depth (and the scale) is constant.

## Mug pixel height
Column profiles through the mug body in frame 39 (x = 1235–1255): top edge at y ≈ 816.6 (blue wall -> cream),
bottom at y ≈ 871.0 (dark contact shadow line on the table). Height ≈ 54.3 px (scene.json record: 54 px, agrees).
The mug stands on the table with its contact line at the same y (871) as the cup's resting contact line, so it is at the same
depth as the cup — same scale.

## Answer
54.3 px x 1.566e-3 m/px = 0.085 m.
Second check: with the top_y acceleration (6323 px/s^2) it is 0.084 m. Sanity: the cup is then 6.7 cm wide and 10.2 cm tall, and
the mug 8.5 cm tall (body 45 px = 7.0 cm wide), both realistic sizes.
Confidence: good (about ±3 %).
