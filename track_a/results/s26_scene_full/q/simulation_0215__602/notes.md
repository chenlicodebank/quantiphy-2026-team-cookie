# q602 — width of the TV stand (m)

Scene: a 2D top-down render. The prior's "black cat" is the only animal, the black pet that walks right along y≈359
(scene/ calls it a dog). The TV stand is the dark console against the top wall (x 709 to ~1150+, with a vase on the
left end and a lamp on the right end).

## Scale (from the prior: speed = 0.94 m/s)
I fitted the track in scene/tracks/dog.csv again (measure.py). The linear slope is 10.991 px/frame for torso_cx,
10.997 for mask_cx and 10.995 for nose_x. Mean per-frame dx is 11.02 for nose and mask. The speed is steady with no
acceleration, so I used 10.995 px/frame × 24 = 263.9 px/s.
Scale = 0.94 / 263.9 = 0.003562 m/px.

## TV stand width (front-to-back depth = vertical image extent in a top view)
- The front edge is a sharp step at y = 292 in every column from x=820 to x=1090 (measure.py). The front edge is
  the bottom edge in the image.
- The back edge is where the console's left-end contrast with the carpet starts. It starts at y ≈ 169 (edges.py:
  the carpet−console difference jumps from about 6 to about 30 between y=167 and y=170). I cross-checked this by eye
  in a zoomed crop.
- Extent = 292.5 − 169 ≈ 123.5 px (±3). Width = 123.5 × 0.003562 ≈ 0.44 m.
- For reference, the length (the long side, partly hidden under the lamp) is at least 437 px, which is at least 1.56 m.

## Checks
- Scale check: the pet is 191 px long, which gives 0.68 m. That is plausible for a cat or small dog. A TV stand
  0.44 m deep and over 1.5 m long is also plausible.
- Every reference point on the pet gives the same speed to within 0.1%.
- Caveat: the console top is raised above the floor, so under perspective it may look a few percent larger. This is
  ignored, following the single-scale 2D convention.

Answer: 0.44 m. Confidence: good (about ±5%).
