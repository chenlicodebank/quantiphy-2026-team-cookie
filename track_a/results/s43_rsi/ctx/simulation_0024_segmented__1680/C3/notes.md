# q_1680 — length of the rock

Method: the scale comes from the prior (boat speed 4 m/s). The boat moves 6.44 px/frame, from a linear fit of ref_x, hull_cx and centroid_x over frames >= 3 in scene/tracks/boat.csv. At question_fps 24 that is 4/24 = 0.1667 m per frame, so 0.02588 m/px. The file itself is 25 fps.

Depth: the boat's camera distance changes only 90.11 -> 90.44 m between t=1 s and t=2 s, so its motion is nearly parallel to the image plane and one scale applies.

Rock: the bbox width is 634 px (x 326-959). The right tip touches the image edge, so this may be truncated by a few px. 634 x 0.02588 = 16.4 m. I assumed the rock is at about the boat's depth, because no depth is given for it.

Sanity check: the boat hull is about 396 px, which is 10.2 m, plausible for a fishing boat. I did not run a separate second measurement route.

Confidence: moderate to low. The rock's depth is unknown, and its edge may be clipped.
