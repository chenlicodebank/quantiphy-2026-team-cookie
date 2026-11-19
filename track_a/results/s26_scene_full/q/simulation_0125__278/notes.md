# Q278 — height of the potted plant (m)

2D Blender render, 24 fps (file fps = question_fps, no retiming). Prior: man's speed = 1.22 m/s. Static camera.

## Scale (from prior)
Man's pelvis track (scene/tracks/man.csv, checked with speed.py): endpoint 363.5→750.0 px over 70 frames = 5.53 px/frame;
linear fit 5.58 px/frame; centroid fit 5.59; mean per-frame step of smoothed pelvis 5.67 (includes residual noise).
Adopted 5.58 px/frame = 133.9 px/s → 1.22 / 133.9 = 0.00911 m/px.

## Plant pixel height (plant.py, plant2.py, plant3.py; frame 70, man far away)
- Top: highest leaf tip, G−R greenness crosses background level at y ≈ 713–714 (x ≈ 326–334).
- Bottom: the pot's dark legs end on the deck at y ≈ 867–868 (luminance column profiles; bright lit floor strip below).
- Height = 867.5 − 713.5 ≈ 154 px (±2 px).

## Answer
154 px × 0.00911 m/px = 1.40 m (range 1.38–1.42 m for the pixel-speed choices 5.67–5.53 px/frame).

## Check
Man's pixel height is 215–223 px → 1.96–2.03 m at this scale; plant/man ratio 154/219 = 0.70, so the plant is ~1.4 m
under the same scale. The man reads a bit tall, which would come from the prior speed being a 3D per-frame pelvis speed
(bobbing adds to the path), so the true scale may be a few % smaller; the plant
stands slightly behind the man's walking line (its base is ~7 px higher in the image), a small perspective effect also ignored per the 2D convention.
Confidence: moderate-high (±5%).
