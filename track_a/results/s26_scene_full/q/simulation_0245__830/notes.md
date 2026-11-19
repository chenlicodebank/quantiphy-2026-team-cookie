# Q830: length of the rabbit (m)

Prior: the antelope (the large horned quadruped, called "creature" in scene/) moves at 1.277 m/s. The scene is 2D: both animals walk parallel to the image plane, the camera is static and their sizes stay constant. fps = question_fps = 30.

## Scale (measure.py)
- Creature horizontal pixel speed:
  - linear fit of the mask centroid over frames 0–74: 6.470 px/frame (residual sd 1.6 px);
  - torso_cx fit: 6.473 px/frame;
  - chords over 0–74, 5–69 and 10–60: 6.465, 6.466, 6.451 px/frame.
  - Result: 194.1 px/s, so the scale is 1.277 / 194.1 = 0.006579 m/px.
- Sanity check: creature torso 266 px = 1.75 m and height 427 px = 2.81 m (it includes the large horn). Both are plausible.

## Rabbit length
- Horizontal bbox extent from the scene/ masks over frames 0–64, where the rabbit is fully in frame: median 76 px, mean 77 px, range 68–98 px with the hop pose.
- Checked by eye on a zoomed crop of frame 6 (crouched pose): about 70 px, consistent with the record's 72.
- Length = 76 × 0.006579 = **0.50 m**. The pose range is 0.45–0.64 m.

## Confidence
The scale is solid (two reference points and several windows agree to within 0.3%). The main uncertainty is which pose or frame the reference's bounding box used. It is about ±10%.
