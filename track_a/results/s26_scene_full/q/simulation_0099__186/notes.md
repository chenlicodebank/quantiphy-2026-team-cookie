# Q186: height of the shark (m). Prior: boat length = 10 m

- This is a 2D side view with a static camera, 24 fps (the file and the question use the same rate). I used one scale for the whole frame, taken from the boat.
- Boat length at frame 0, measured in code by background difference in measure.py: the stern is at x=227–231 and the bow tip at x=1087. That gives 857 px (853–861 depending on the threshold), which matches the scene record (851–860).
  Scale = 10 m / 857 px = 0.011669 m/px.
- Shark height is the vertical bounding box from the dorsal-fin tip to the pectoral-fin tip. In code, at frames 0–60 with threshold 60, it runs from y=852–853 to y=956–958, a height of 104–107 px. A 3x zoomed crop at frame 0 shows 852 to 957, so I used about 106 px. The scene record gives 107 px.
  At threshold 30 the mask picked up background noise at the top (y=833), and I rejected that result after looking at the crop.
- Height = 106 × 0.011669 = **1.237 m**. The range is 1.21–1.25 m.
- Sanity check: the shark is 274 px long, which comes to 3.2 m, a plausible ratio with a 1.24 m height that includes the fins.
- Confidence: good. The main uncertainty is about ±2 % from the edge definition.
