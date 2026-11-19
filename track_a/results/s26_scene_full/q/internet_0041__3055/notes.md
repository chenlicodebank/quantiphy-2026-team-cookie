# Q3055: average speed of the middle duck (cm/s). Prior: size of the middle duck = 66 cm

## Method
I used the 2D internet convention: one scale = 66 cm / the duck's pixel length (bill to tail tip, along its motion direction).

## Time base
The file runs at 23.979 fps and the question at 24. The two differ by 0.09 %, which does not matter here. I used 24.

## Duck length in pixels
- From zoomed grid reads: frame 0 gives 2282 to 2413 = 131 px. Frame 25 gives about 2198 to 2334 = about 135 px. Frame 50 gives
  2110 to 2247 = about 137 px.
- The GrabCut masks in scene/ give a median of 127 px. They cut off the pale tail tip.
- My own colour mask (measure.py) leaked into the pale water, so I rejected it.
- Value used: about 132 px, so the scale is 0.50 cm/px.

## Motion
The camera is almost static. Its drift is under 1 px in x and up to 6 px in y. I subtracted it.
- Route 1: template matching of the body, with sub-pixel peaks (measure.py, tmpl_track.csv). The mean per-frame
  displacement is 3.46 px/frame raw and 3.35 px/frame with 5-frame smoothing. Net displacement over 51 frames gives 3.41 px/frame.
- Route 2: mask centroid from scene/. This gives 3.52 px/frame raw, and net displacement gives 3.44 px/frame.
- Value used: 3.44 px/frame x 24 = 82.6 px/s.

## Answer
82.6 px/s x 66 / 132 = 41.3 cm/s. I report 41.5.
- If the length is 127 px, the answer is 44.7. If it is 135 px, the answer is 40.4.

## Confidence
Moderate. The main uncertainty is the pixel length of the duck, about ±4 %.
