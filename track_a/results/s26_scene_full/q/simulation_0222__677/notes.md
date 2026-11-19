# q677 speed of robot vacuum at t=1 s (2D overhead render)
- fps 24 (file = question_fps). t=1 s -> frame 24; speed = |p24-p23| x 24 x scale.
- Position: record circle-fit centre (scene/tracks): step 23->24 = 20.21 px. Independent check (measure.py,
  mid-level threshold 160/180, centroid & ellipse centre): 20.25 / 20.21 px. Neighbouring steps 20.1-20.5 (smooth motion).
- Scale: disc diameter 0.438 m = ~118.3 px (circle fit 117.9, threshold-180 equiv diam 119.4, ellipse axes 117.5/119.4).
  -> 0.003702 m/px. Robot and its motion are on the floor, so one scale holds.
- Speed = 20.22 x 24 x 0.438/118.3 = 1.797 m/s. Diameter uncertainty about 1%; the step is good to 0.2%.
- Confidence: high (about 2%).
