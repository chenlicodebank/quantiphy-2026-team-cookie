# Q48: width of the white car (m)

The scene is a 2D top-down view at 24 fps (fps = question_fps, so no re-timing). The "white car" is the white van at x≈833.

## Scale from the prior (bicycle speed 5.33 m/s)
- The cyclist's centroid moves at constant velocity. A linear fit of cy over frames 2–71 (scene/tracks/cyclist.csv)
  gives 8.916 px/frame, which is 213.98 px/s.
- Scale = 5.33 / 213.98 = 0.02491 m/px.
- Sanity check: the bike is about 64 px long, which gives 1.6 m. That is plausible.

## Van width (measure.py, measure2.py)
I measured the per-row horizontal extent of the van at frames 20, 30, 40 and 50, against a background of asphalt grey.
- Body: the threshold-25 median is 86 px, and the half-max edges of the mean profile give 84.4–86.5 px. I take about
  85.5 px, which is **2.13 m**.
- Including the side mirrors (rows about 67 px behind the front): about 91–98 px, roughly 95 px, which is **2.37 m**.
- The scene record's bbox width of about 101 px also includes a soft shadow fringe. At a low threshold the body
  rows alone read 98 px, so I did not use 101 px.

## Answer
I answer **2.2 m**. The convention (width = wheel-to-wheel body width) points to 2.13 m. A world bounding box that
includes the mirrors would give about 2.37 m. I chose 2.2 m, leaning toward the body width, so the answer is within
about 3–7 % of both readings.

The second route was repeating the measurement on four separate frames: the body width was consistent within ±1 px
(84.4–86.5 px).

Confidence: moderate. The main uncertainty is whether the mirrors count, about ±10 %.
