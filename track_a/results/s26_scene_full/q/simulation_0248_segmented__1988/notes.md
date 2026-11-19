# q1988 — height of the brown horse (m)

2D side-view scene. The brown horse is the larger grey-brown horse in the middle. fps = question_fps = 24.
Scale comes from the prior (speed 0.874 m/s). Script: `measure.py`, which decodes the video itself and also reads the scene torso track.

- Brown horse speed: torso track per-frame mean 5.937 px/frame, linear-fit slope 5.940; the mask-centroid fit slope is 5.933.
  That is about 142.5 px/s, so the scale is 0.874 / 142.5 = 0.00613 m/px. Motion is steady, so every route gives the same speed.
- Height of the mask bbox (min RGB < 235, 4-connected) across all 50 frames ranges from 174 to 184 px. The median is 177.5 px and the mean 177.9 px.
- Height = 177.5 × 0.00613 = **1.09 m**. Using the max frame instead gives 1.13 m.

Second route: the scale from the centroid speed instead of the torso gives the same value within 0.1%.
Confidence: moderate-high. The main uncertainty is gait variation of the silhouette (±3%), and whether the
reference bbox is a rest pose or the animated one.
