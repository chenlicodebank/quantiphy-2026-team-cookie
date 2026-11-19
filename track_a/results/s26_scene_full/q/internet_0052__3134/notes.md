# q_3134 – wheel-to-wheel width of the scooter (m)

Prior: average speed of rider = 2.91 m/s. Internet video, 2D side view, 30 fps (file fps = question_fps, no re-timing).
Single planar scale from the prior, following the annotator convention.

## Pixel speed (prior object)
Scooter front-wheel leading edge (most reliable point; scene track, re-checked by wheels2.py which found the
front-wheel black run per frame: 1263 @f0 -> 468 @f43, 18.49 px/frame).
- raw pixels: 1262.0 -> 244.4 over frames 0-55 = 18.50 px/frame = 555 px/s
- stabilised (camera drift +9 px removed): 1027/55 = 18.67 px/frame = 560 px/s
Used 557 px/s (mean; the two differ by 0.9%). Scale = 2.91 / 557 = 0.005224 m/px.

## Wheel-to-wheel extent (wheels3.py)
Median of rows y 1008-1024, black threshold (<10): front wheel run (~39 px wide) and rear wheel run.
Frames 18-32 (rear wheel cleanly separated from the cast shadow, rear wheel ~39 px wide = front):
outer front-edge to rear-edge = 196-198 px; add ~1 px per edge for threshold blur -> ~199 px.
(The scene record's 203 px goes to the rear fender end, which sticks out past the wheel.)
Wheel centre-to-centre (wheelbase) ~ 158 px.

## Answer
Wheel-to-wheel (outer edges, along the motion direction, like bumper-to-bumper): 199 px x 0.005224 = **1.04 m**.
Alternative readings: wheelbase centre-to-centre 158 px -> 0.83 m; full length incl. fender 203 px -> 1.06 m.
Sanity: typical e-scooter length ~1.0-1.1 m. Second route: stabilised vs raw speed gives 1.034-1.043 m.
Confidence: moderate (the main uncertainty is which reading of "wheel-to-wheel" the annotators used).
