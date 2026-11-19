# Q1907 – diameter of the truck's tire (m)

Prior: speed of the box = 0.094 m/s. 2D side view, static camera, 120 fps (file fps = question_fps; no re-timing).

## Scale from the box speed
- The cardboard box (on the cargo-body roof) moves straight up at a CONSTANT speed. Its top edge, measured sub-pixel
  in every frame over 60 columns (top.py → top_track.csv), gives a linear fit of 0.1581 px/frame = 18.97 px/s
  (rms 0.33 px). The speed is the same in 80-frame windows (19.6, 18.8, 17.9, 19.3, 19.3 px/s). A quadratic fit gives
  19.04 → 18.90 px/s, so there is essentially no acceleration.
- The cargo body underneath speeds up (7.7 → 29 px/s, fit.py), and its roof edge hides more and more of the box bottom.
  That is why the box's apparent height shrinks by ~6 px and why the record's box ref_y and bottom edge look as if
  they speed up. The box width stays at 408 px (no scale change). The scene record's box centre therefore mixes in the
  body motion. The box itself (a linear, constant-speed animation, matching a single prior speed value) is the top edge.
- Scale = 0.094 / 18.97 = 4.956e-3 m/px.

## Tire diameter in px (wheel2.py, wheel3.py; frame 200, wheels are static)
- I fitted circles to the tire silhouette against the white background on the lower arc (angles 13-70 deg from the
  bottom on both sides, leaving out the flattened contact patch):
  rear 163.5 px, front 167.2 px (rms 0.6-0.7 px).
- Radii along rays from the hub centre: rear about 83.5 (D about 167); front left/right average about 82 (D about 164).
- Scene record: 168 / 163. I adopted D = 165.5 ± 2 px.

## Answer
D = 165.5 px × 4.956e-3 m/px = 0.820 m (rear only: 0.81-0.83; front: 0.81-0.83).

## Checks / alternatives
- If "speed of the box" meant the cargo body's mean speed (20.2 px/s), the answer would be 0.77 m. If it meant the
  body's end speed (28.7 px/s), it would be 0.54 m. The constant-speed box top is the only motion that matches a
  single fixed speed, so I use it.
- Sanity check: at this scale the truck is about 8.5 m long (1716 px) and the tire about 0.82 m. Both are plausible
  for a catering truck.

Confidence: moderate-high on the measurement (±2%). The main risk is how the prior's speed is defined.
