# q_280 — width of the house (m)

Prior: speed of the person = 1.22 m/s. 2D video (frontal facade, the man walks parallel to it), 24 fps (file fps = question_fps).
I used one metres-per-pixel scale taken from the man's pixel speed.

## Man's pixel speed (speed.py, scene/tracks/man.csv, frames 0-70)
- pelvis_x_smooth: line-fit slope 5.577 px/frame, endpoints / mean step 5.526
- centroid_x: 5.587 (fit) / 5.481 (endpoints); raw pelvis 5.578 / 5.521
- Adopted: 5.55 px/frame = 133.2 px/s, so the scale is 1.22 / 133.2 = 0.00916 m/px

## House width in pixels (edges.py, frame 0, strongest intensity edge against the grey mountain)
- Left outer edge x = 150.5 on every row from y=420 to y=880
- Right outer edge x = 922.5 on rows 420, 700 and 800 (rows 500 and 600 picked an inner edge at 890; ignored)
- Width = 772-773 px, which matches the scene record (~775 px)

## Answer
773 px x 0.00916 m/px = 7.08 m (horizontal extent across the facade, black outer frame included).

## Check and confidence
- Using the endpoint speed (5.53 px/frame) instead gives 7.10 m; using the fit slope (5.58) gives 7.04 m.
- At this scale the man is about 220 px x 0.00916 = 2.0 m tall. That is a bit tall, so the speed prior may not match a
  realistic body size, or the man (walking on the recessed porch) is slightly farther away than the facade front.
  Perspective looks weak (the recess side walls are only about 10 px wide), so I kept a single scale as the 2D
  convention says.
- The deck/platform below the house extends wider than the facade; it was not counted as part of the house.
- Confidence: moderate (within about 5-10%).
