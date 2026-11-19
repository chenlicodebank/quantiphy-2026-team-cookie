# q_1989 — length of the brown horse (m)

Prior: speed of the brown horse = 0.874 m/s. 2D side-view scene, static camera, fps 24 (file and question agree).

Object: the "brown horse" is the larger grey-brown middle horse (scene record `brown_horse`); the left one is chestnut/red.
Checked on frame 0 (frames/f0.png).

Scale (measure.py, from scene/tracks/brown_horse.csv):
- pixel speed: mean one-frame torso step 5.937 px/frame; linear fit of torso x 5.940; centroid net 5.942; bbox
  x0 and x1 net 5.939 px/frame -> all agree, 5.94 px/frame = 142.5 px/s (constant walking speed).
- scale = 0.874 / 142.5 = 0.00613 m/px.

Length: horizontal bbox extent of the mask (side view, nose to tail), frames 0-49: median 229 px, mean 229.6,
range 223-241 (gait). 229 px x 0.00613 = 1.405 m; mean -> 1.408 m.

Second route: same ratio via bbox-edge motion (x0/x1 5.939 px/frame) gives identical 1.405 m.
Answer 1.41 m. Confidence: moderate-high; main uncertainty is gait-dependent silhouette length (±4 %) and whether
the reference AABB includes tail/head pose differently.
