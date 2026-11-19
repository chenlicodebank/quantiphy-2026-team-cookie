# q_3155 – height of the Bicycle sign (m)

Prior: average speed of "the person riding scooter" = 1.95 m/s. The only moving person in the clip is the woman walking
right to left (no scooter is visible), so the prior is taken to refer to her. fps = question_fps = 30.

## Scale (annotator convention: one planar scale from the prior)
speed.py uses scene/tracks/pedestrian.csv for all 75 frames:
- bbox centre: net 248.7 px/s, mean per-frame path 250.7, smoothed path 249.0
- head top: net 242.3, smoothed path 244.9; stabilised centroid smoothed path 249.5
- Taken value: ~247 px/s, so scale = 1.95 / 247 = 0.00789 m/px. The routes span 242–251 px/s, about ±2%.
Camera drift is about 1% and was ignored, as in the annotators' convention.

## Sign
sign.py makes a yellow colour mask (outer rim component) on frames 0, 37 and 74. The diamond's outer vertical extent is
y 107–274 at frame 0 (167–168 px), with inner face 158 px. A zoomed grid view (frames/sign.png) reads 108–273, which
gives 166 px. The record's 166 px (scene.json) agrees. I used 166 px.

Height = 166 × 0.00789 = 1.31 m. Over the range of speed routes it is 1.29–1.34 m.

## Alternative readings
- Diamond plus the arrow plaque (y 108–325, 218 px): 1.72 m.
- Whole pole from the base on the island (~554 px): ~4.4 m.
I answered with the diamond itself, the "Bicycle sign". A real 30" bicycle warning diamond is about 1.07 m on the
diagonal, so 1.31 m is plausible: the sign is behind the walker, but the annotators applied one planar scale.

Confidence: moderate. The scale is solid to about 2%; the main risks are which object the prior means and which part
of the sign counts as "the sign".
