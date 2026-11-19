# q744 – black cat length incl. tail (m)

Prior: cat speed = 0.714 m/s. 2D scene (cat walks parallel to the frontal wall, static camera), fps 24 = question_fps.

Scale (measure.py): linear fits of the cat's horizontal position against frame number in scene/tracks/cat.csv
give torso_cx 213.9, torso_x0 214.3, torso_x1 213.6, cx_dark 216.0, cx_mask 215.7, cx_bbox 212.6 px/s.
I used 214.5 px/s, so the scale is 0.714 / 214.5 = 3.33e-3 m/px. Motion is almost purely horizontal (±3 px bob).

Length (world AABB extent along the walking direction, tail included): this is the horizontal bbox width of the
cat's silhouette.
- Record bbox_x1 - bbox_x0: median 184, mean 187 px (range 177–211; it changes with the stride).
- My own check (measure2.py: median-background difference, components near the torso, mask drawn in
  frames/mask_30.png): median 183, mean 186.8 px. The two agree.
The tail is held upright and curves back only a little, so the bbox runs from the hind paw/tail to the front paw.
I used ~186 px × 3.33e-3 = 0.62 m (0.61 from the median, 0.70 at the widest stride).

Confidence: medium. The scale is solid (to about 1%). The main uncertainty is which length convention the
reference used: the animated AABB, which changes with the gait, versus a rest pose with the tail extended,
which would be longer.
