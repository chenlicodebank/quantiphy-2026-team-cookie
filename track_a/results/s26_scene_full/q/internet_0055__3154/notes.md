# q_3154 – DO NOT ENTER sign height above ground

Prior: average speed of the "person riding scooter" = 1.95 m/s. The only person in the clip is the woman crossing
right to left (scene/tracks/pedestrian.csv); she is taken as the prior's object. fps = question_fps = 30.

## Scale (speed.py)
Mean pixel speed over frames 0-74 for different reference points: bbox centre 248.5 px/s, head top 242-246, centroid
242-245 (stabilised 245-252). Taken as ~247 px/s -> scale = 1.95 / 247 = 0.00790 m/px (one planar scale, annotator convention).

## Sign (pole.py + zoomed frames sign.png, base2.png)
Panel bottom edge y ≈ 289-292 (frame 0-30, panel ~144-290). The pole's base is hidden by bushes; the pole is clearly
visible down to y ≈ 585-590, ground at base estimated ≈ 590-605. Sign bottom to ground ≈ 297-310 px.
Distance = ~297 px x 0.0079 = 2.35 m (range 2.33-2.45 depending on the hidden base point).
Alternative reading (sign centre y≈217 to ground): ~3.0 m – not used; "distance of the sign to the ground" read as bottom edge.

## Check
Real-world: MUTCD minimum sign bottom height 7 ft (2.13 m) – consistent. Note the pedestrian is nearer to the camera than
the sign, so the planar scale is only the annotators' convention.
Confidence: moderate (hidden pole base, reference-point choice ±3%).
