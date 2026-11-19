# Q390 – width of the road the bike crosses (simulation_0166)

Reading: the cyclist rides left to right along a cross street and so crosses the main street, which recedes toward
the camera's vanishing point. "Width" here means the main street's curb-to-curb width, measured horizontally
along the bike's line.
fps = question_fps = 24, so no retiming.

## Scale (prior: bike speed 5.52 m/s)
- Cyclist track (scene/tracks/cyclist.csv, template matching, camera static): linear fit over f6–79 gives 21.024 px/frame,
  i.e. 504.6 px/s. Scale = 5.52 / 504.6 = 0.010940 m/px at the bike's depth (tyre contact row y = 738).
- Sanity check: cyclist height 163 px gives 1.78 m, and van length 438 px gives 4.8 m. Both are plausible.

## Road edges (hough.py, frame 5; the background is static)
- Canny + HoughLinesP below y = 760. Left curb bottom (road edge): line through (616,760), slope dx/dy = -1.568.
  Right curb bottom: line through (1505,760), slope +2.44. Lane centre lines meet these at a vanishing point of about
  (960, 538), which checks out.
- The bike is inside the intersection, so I extrapolated the main-street curb lines to the bike's ground row y = 738:
  x_L = 650.5, x_R = 1451.3, giving **800.8 px**.
- Width = 800.8 × 0.010940 = **8.76 m**.

## Checks and sensitivity
- Ground row ±2 px: 8.67–8.85 m. Using the van's ground row (743): 8.98 m.
- Inner edges of the painted edge stripes (not curbs): 752.6 px, or 8.23 m. This is the lower bound if the answer
  counts only the area between the lines.
- Confidence: moderate. The geometry is solid. The main uncertainties are curb versus asphalt edge and which depth
  row to use (±3 %).
