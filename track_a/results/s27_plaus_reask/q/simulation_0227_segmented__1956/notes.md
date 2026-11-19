# q_1956 — width of the beach chair (m)

Prior: black cat speed = 1.041 m/s. No depth_info. question_fps = 24 = file fps.

## Scale
- Cat centroid track (scene/tracks/cat.csv, checked on frames): linear fit x(frame) slope 5.465 px/frame; nose
  (bbox_x1) slope 5.463 px/frame -> 131.1 px/s. The raw mean of per-frame path lengths is 5.63, but that is
  inflated by mask noise. Scale at the cat's depth = 1.041 / 131.1 = 0.00794 m/px.

## Chair width
- The six loungers face the camera foot-end first, so width (the shorter horizontal extent, across the chair) is
  their horizontal pixel extent. Measured with chairs.py / legs.py on the median background:
  - front-left: 764-946 = 183 px (seat front = outer edges of the legs)
  - front-middle: legs 1005-1189 = 185 px (seat 1000-1188 includes a little of the side)
  - front-right: front legs 1249-1431 = 183 px
  -> 183 px at the chairs' front face (front legs reach the ground at y = 901).
- Perspective: the front-right chair's back legs are at 1226 and 1392 (167 px). This fits the vanishing toward
  x = 960 with a ratio of 0.913, and the front-left and front-middle back legs match the same ratio. The back legs
  reach the ground at y ≈ 872, so the ground horizon is at y ≈ 569. The cat's feet are at y ≈ 920, so the cat is
  about 5.7 % nearer than the chair fronts -> scale at the chair front = 0.00794 x 1.057 = 0.00839 m/px.
- Width = 183 x 0.00839 = 1.54 m (perspective-corrected); plain 2D single scale: 183 x 0.00794 = 1.45 m.
- Answer 1.52 m. It leans toward the corrected value but is shaded down a little, because the origin's per-frame
  speed may be a bit above the fitted pixel speed, and the back-leg ground contact could be cut off in the
  segmentation.

## Plausibility
- 1.5 m is wide for a single sun lounger (typically 0.6-0.8 m), but every in-scene check gives this scale: at
  0.008 m/px the seat is about 0.40 m high (51 px) and the cat is about 0.69 m from nose to rump. Relative to the
  cat, the chair is about 2.1x the cat's body length. The chairs are wide relative to their own seat height (183 vs
  51 px), so the chair model itself is wide. The prior is the only metric scale, so I kept it.
- Confidence: moderate (±5 % from scale and perspective). The main risk is a scaled scene or a different reading of
  "width".
