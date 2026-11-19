# Q148: length of the big bird (bald eagle), in metres

2D scene. The scale comes from the prior: the small bird (crow) flies at 11 m/s. File fps = question fps = 24.

## Measurements (measure.py: background-median mask, threshold 15)
- Crow speed: the rightmost (beak) x position goes 1277, 1355, 1434, 1512, 1591, 1669, 1747, 1825, 1904 over frames 2-10.
  That is (1904-1277)/8 = 78.4 px/frame. Frames 1-10 give 78.3. Cross-correlating the column profiles of
  consecutive frames gives a mean of 78.1. The record's centroid dx (78.4) and body_cx dx agree.
  Using 78.4 px/frame x 24 = 1882 px/s, the scale is 11/1882 = 0.005846 m/px.
- Eagle length, beak to tail, on the static frame 0: mask x 668-817, so 150 px (149 in moving frames). Taking
  149.5 px x 0.005846 gives **0.874 m**. The answer is 0.875 m.

## Checks
- Using 149 px or 150 px gives 0.871 to 0.877 m. A crow speed of 78.1 instead of 78.4 px/frame gives 0.878 m.
- Plausibility: a real bald eagle is 0.7-1.0 m long, so 0.875 m fits. The small bird comes out at 92 px = 0.54 m,
  which is large for a crow but realistic for a raven.
- Confidence: high, about ±2%.
