# q_604 — diameter of the vase (m)

Prior: speed of the black cat = 0.94 m/s. No depth_info. fps 24 (file) = question_fps 24, so frame = round(t·24).

Scene: a 2D top-down render with a static camera. The only moving animal is the black cat; scene/ calls it a "dog".
It walks steadily in +x, and the white vase sits on the left end of the TV console.

## Scale (from the prior)
- The cat track (scene/tracks/dog.csv) covers the right animal in all frames 0–49. Linear-fit slopes are
  nose_x 10.995, mask_cx 10.997 and torso_cx 10.991 px/frame, with no acceleration. So the speed is
  10.995 × 24 = 263.9 px/s (measure.py).
- Scale = 0.94 / 263.9 = 0.003562 m/px.

## Vase pixel diameter
- vase_edges.py averages 8 frames (the vase is static) and takes 72 radial profiles from the vase centre. The edge is
  the sub-pixel half-level crossing between the white rim and the dark console. A circle fit to these edges gives a
  diameter of **72.35 px** (residual std 0.5 px), with x extent 71.9 and y extent 73.0. The overlay is in
  frames/vase_fit.png.
- Second route (measure.py): threshold masks at grey 130 give a 72×72 px box and an equal-area diameter of 71.2 px.
  Half-max crossings on the centre row and column give about 72.2 and 73.6 px. This matches scene.json (71 ± 3 px).

## Answer
72.35 px × 0.003562 m/px = **0.258 m**

Sanity checks: the cat is about 0.68 m nose to tail and the room floor is about 5.5 m wide, so the scale is plausible.
Perspective: the vase is on the console, so it is a little closer to the camera than the cat's plane. But the
console and bench show no visible side faces, so the perspective effect is small. Following the 2D convention, I
used a single planar scale. Confidence: good (about ±3% from the pixel measurements); any perspective effect would
make the true vase slightly smaller.
