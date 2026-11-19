# q_612: height of the wooden bench (m)

Prior: the black cat's speed is 0.94 m/s. No depth_info. fps = question_fps = 24, so no re-timing.

## Scale from the cat
- Cat walking speed, from scene/tracks/cat.csv, re-fitted in `speed.py`: matched upper body 17.735 px/frame
  (first half 17.78, second half 17.75). Torso centroid gives 17.87 and the nose by eye 17.76.
  I used 17.75 px/frame = 426 px/s.
- s = 0.94 / 426 = 0.002207 m/px at the cat's depth. The camera is static and the cat's body length stays
  constant, so its motion is in a plane parallel to the image.

## Bench pixel geometry (frame 48; `prof.py`, `legs.py`, `crop.py`)
- Top surface: back edge at y = 779.5 and front edge at y ≈ 798, with the slat front face below that.
- Feet: the front legs end at y = 992 and the back legs at y = 966.
- So the bench spans 194 px in its front plane and 186.5 px in its back plane.
- The bench is clearly farther away than the cat. Its feet are at y 966–992, while the cat's paws touch down at
  y ≈ 1019–1020 on the near side and ≈ 1010–1013 on the far side. I took the cat's midline ground at y ≈ 1016.
  Because of this depth difference, the cat's scale has to be corrected for perspective.

## Perspective correction
- Horizon: the TV-stand cabinet's right side edge is vertical to dx/dy = 0.0004 (`vert.py`, rms 0.05 px), and it
  lies 463 px from the image centre. That means the camera has essentially no pitch, so the horizon is at
  y_h ≈ 540, the image centre.
- For a level camera, ground y − y_h is proportional to 1/Z. The bench's real height is
  s · (y_cat_ground − y_h) · (bench px height) / (y_bench_foot − y_h):
  - front plane: 194 · 476 / 452 = 204.3 px-equivalent
  - back plane: 186.5 · 476 / 426 = 208.4 px-equivalent
  - mean: 206.3 → 206.3 × 0.002207 = **0.455 m**
- Sensitivity: moving y_h by ±40 px changes the result by about ±1%. Without any perspective correction
  (212 px full box × s) the answer would be 0.468 m, about 3% higher.

## Check
- The front and back planes are two independent routes (different feet and top edges, different depths). They
  give 0.451 m and 0.460 m.
- A typical bench or side table is about 0.45 m high, which makes the answer plausible.

Confidence: good, about ±3%.
