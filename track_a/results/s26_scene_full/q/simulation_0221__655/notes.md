# Q655: width of the floor mirror (m)

Prior: the vacuum's diameter is 0.438 m. There is no depth_info. The video is a top-down render (24 fps, and question_fps is also 24; time does not matter for this question).

## Object
The scene record has no "mirror". The floor mirror is the object it calls `chair_frame_top_right`: a thin light-wood
rectangular frame leaning against the top wall at x 1340-1613 px and y 85-221 px. The glass reflects the floor in front of it,
which is what you see inside the frame. Because of perspective, the top bar (high up, nearer the camera) looks
wider than the bottom bar on the floor. Its width is its horizontal extent across the face, which is the image x-extent of the frame.

## Measurements (frame 0, static; scripts crop.py, prof.py, legs.py, mirror.py, vac.py)
- Top bar, outer x-extent at y about 100: 1408.5 to 1612.5, so **204 px**. Taken from sub-pixel half-level crossings.
- Right leg, outer edge: a line fit over rows 106-212 gives a slope of about -0.85 px/row. The bottom-right outer corner on the floor is at **x about 1511**, y about 220.
- Bottom bar: it is visible only from x 1442 to 1510. The left leg is partly lit and partly in shade, so it shows up as broken pieces.
  Following the centreline of those pieces (slope -0.59) puts the bottom-left outer corner at x about 1342 (±5).
- Principal point: the lamp's top centre is offset from its rim centre by (+8, -10.5) px. That is radial from about (950-960, 540), so the principal point is at the image centre.
- Route A (bottom on the floor): 1511 - 1342 = **169 px**.
- Route B (top bar scaled down to the floor): k = (1612.5-960)/(1511-960) = 1.184, so 204/1.184 = **172 px**. If cx is wrong by ±50 px, this changes by only ±1.5%.
- I used 170.5 px for the width on the floor plane.

## Scale
- Vacuum diameter near the image centre (frames 35-50, track circle fit): 120.6 px. My own profiles of frames 36 and 40 give
  120.6 and 120.2 px. So 0.438/120.6 = 0.003632 m/px.
- The widest outline of the vacuum is about 5 cm above the floor. The camera is high (k = 1.18 for a mirror top at about 1.5+ m), so the
  correction to floor scale is about -0.5%. That gives 0.00361 m/px.

## Result
Width = 170.5 px x 0.00361 m/px = **0.62 m**. Route A gives 0.611 m and route B gives 0.622 m.
Confidence: moderate. The main uncertainty is where the bottom-left corner is (±3%). If you naively scale the top bar by the floor scale,
you get 0.74 m. That is wrong, because the top bar is raised.
