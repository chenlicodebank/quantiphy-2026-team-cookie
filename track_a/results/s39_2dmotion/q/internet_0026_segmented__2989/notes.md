# q_2989: average speed of the toy truck (cm/s)

Prior: total height of the sofa = 90 cm. **The sofa is not visible**: the background was replaced by white in this
segmented video, and SAM 3 "sofa" returns no instance on frame 10. So the prior's pixel height cannot be measured,
and the scale has to come from real-world references in the subject plane (low confidence).

Time base: question_fps = 30 (file 30.0003 fps, the difference is negligible). Frames 0-35 = 1.1667 s, 35 intervals.

## Motion (measure_speed.py)
- Truck track from scene/tracks/truck.csv. I checked it: the front bumper is never occluded. SAM truck masks at
  f10 (208x171 px) and f35 (205x168 px) agree with the record's 207-209 x 170 px to within 2%.
- The camera pans (hand-held) to follow the truck, and the content shifts about +40 (child) to +57 (man) px.
  Following the "measure against the background" rule, I used the record's stabilised front-bumper track:
  mean per-frame speed = 248.6 px/s (250.9 px/s using the centre with y). In the raw image it is 208.3 px/s.
- Duplicate frames (25->30 conversion) do not affect the mean of the per-frame speeds, because that is path / time.

## Scale (no sofa visible)
- Man's head (SAM 125 px vertical, ~128 px along the tilted axis; my grid reading 124 px, agrees) / 23.5 cm
  -> 0.184 cm/px. He is the closest to the camera (lowest floor contact, largest pan parallax).
- Child's head (SAM 82 px; my reading ~80) / ~17.5 cm -> 0.213 cm/px. The child is the farthest.
- The truck sits between them in depth -> ~0.195 cm/px. A sofa behind the people would give the annotators a slightly
  larger cm/px. I chose 0.205 cm/px, which puts the truck at about 42 x 35 cm (a plausible large toddler dump truck).

## Result
- 248.6 px/s x 0.205 = 51.0 cm/s (stabilised). Raw image: 42.7 cm/s. Truck-plane physical estimate: 293 px x 0.195 /
  1.1667 s = 49 cm/s.
- Answer: **50 cm/s**.
- Confidence: low-moderate. The scale is not from the prior's object, so it is uncertain by about ±20%.
