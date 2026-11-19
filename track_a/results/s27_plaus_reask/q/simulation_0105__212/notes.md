# q_212 – height of the teacup with the plate (m)

2D Blender scene, static camera, 24 fps (file and question fps are the same). Prior: gravity = 9.8 m/s^2, which sets the scale through the falling sugar cube.

## Scale (measure.py)
- I fitted a quadratic to the cube centroid y (scene/tracks/cube.csv, frames 22–45, t = frame/24).
  The acceleration is 682.4 px/s^2 (rms residual 0.12 px).
- Split-half check: frames 22–33 give 682.0 and frames 34–45 give 682.8, so the fall is uniformly accelerated.
- A hand linear regression of the per-frame steps gives 1.185 px/frame^2, which is 682.6 px/s^2.
- Scale = 9.8 / 682.4 = 0.014362 m/px.

## Height
- In frames 0, 5, 12 and 20, the cup and saucer mask (|grey − 155| > 6, 12 or 25) spans rows 974–1073 at every threshold.
- The bbox is 100 px. The edge rows 974 and 1073 are partly covered (anti-aliasing), so the edge-to-edge height is about 99.5 px.
- Height = 99.5 × 0.014362 = 1.429 m (with the full 100 px bbox it is 1.436 m). **Answer: 1.43 m**
- The scene is scaled: the cube is about 0.37 m and the cup about 1.4 m. The prior is gravity, which holds whatever the size of the scene, so a giant-size setup is allowed here.

Confidence: high. The pixel height is within ±1 px (about 1%) and the acceleration fit is better than 0.5%.
