# Q334 – distance bird to roof at t = 1 s (frame 60)

2D simulation, 60 fps (file fps = question_fps, no re-timing). Static camera.

## Scale (prior: bird speed 9.146 m/s)
Bird ref point (eroded-mask centroid, scene/tracks/bird.csv, checked against frames) moves at a nearly constant
pixel speed: mean per-frame step 19.72 px (frames 17-99, outside the sun), 19.56-19.61 px/frame averaged over windows
centred on frame 60 (55-65, 50-70, 40-80). Per-frame jitter (wing beat) slightly inflates path length, so I use
19.6 px/frame = 1176 px/s -> 9.146 / 1176 = 0.007777 m/px.  (sp.py, roof.py)

## Positions at frame 60
- Bird: (993.2, 125.4) px.
- Roof (measured in roof.py on frame 60): shingles x 586-1406 / eave incl. fascia 576-1419, y 521 (ridge) to ~690
  (bottom of fascia board). Origin taken as bbox centre (997.5, 605.5).
- Pixel distance = hypot(4.3, 480.1) = 480.1 px -> 3.73 m.

## Checks / alternatives
- Using the 17-99 mean step 19.72 px/frame: 3.71 m.
- If the roof origin were at its eave/base (y ~690) instead of its centre: 564.6 px -> 4.39 m (not chosen).
Confidence: moderate; main uncertainty is the roof's origin location.
