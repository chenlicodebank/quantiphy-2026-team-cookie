# q_1995 — height of the rabbit (m)

Prior: brown horse speed 0.874 m/s. 2D side-view render, white background, fps 24 (= question_fps, no re-timing).
The scene record's "hamster" is the rabbit (small orange-brown animal with long ears, rightmost), confirmed on frame 12.

## Scale (measure.py)
Brown horse (largest component) moves at constant speed: centroid net 5.942 px/frame, bbox-centre 5.939, linear fit
5.933, torso template (scene record) 5.918. Use 5.935 px/frame = 142.4 px/s
-> 0.874 / 142.4 = 0.006137 m/px. Ground contacts of all animals are on the same row, so one scale holds for all of them.

## Rabbit height
Bbox height of the mask, frames 0–49: 29–39 px (it changes with the hop and ear pose). Median 35 (threshold 235) / 33.5
(threshold 200), mean 33.9. Taking 34.5 px gives 34.5 × 0.006137 = 0.212 m.

## Check
The scene record's independent tracks give the same values (horse torso 5.92 px/frame, rabbit median height 34.5 px),
which gives 0.211–0.212 m. At most this is +-10 % from the pose variation (29–39 px).
Confidence: moderate. The scale is solid; the main uncertainty is which pose the reference height uses.
