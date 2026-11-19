# q562 cat height incl. tail
2D scene, single scale from the speed prior 0.94 m/s. fps 24 (file = question).
- Cat pixel speed: linear fit of x vs t across 4 reference points (mask centroid, torso centre, nose, rear) = 426.8 px/s
  (per-frame mean of the centroid's speed = 432.0 px/s, inflated by gait wobble). Scale = 0.002203 m/px.
- Height (tail tip to paws) from scene/tracks bbox, checked on a zoomed frame 0 (tail tip y~812, paws y~1031):
  212-226 px, median 220 px.
- Height = 220 x 0.002203 = 0.485 m. With the max bbox it would be 0.498 m; with the per-frame speed, 0.479 m.
Confidence: moderate-good (~5%); the main uncertainty is which frame or pose the reference AABB used.
