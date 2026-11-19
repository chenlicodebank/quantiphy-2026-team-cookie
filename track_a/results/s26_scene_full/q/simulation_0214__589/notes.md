# Q589 — width of the TV stand (m)

Prior: black cat speed = 0.94 m/s. No depth_info. fps = question_fps = 24.

## Scene
Top-down Blender render with a static camera. The TV stand is the dark low console along the top wall. Its left end is at x ≈ 710. Its right end is under the lamp shade, at x ≈ 1265. Its back edge is at y ≈ 168–169 (the wall shadow above it is lighter, ~76 grey, against ~57 on the cabinet top). Its front edge is at y ≈ 292.5 (a sharp step to the carpet, ~68 → 110).
Following the naming rule, "width" of a TV stand = its front-to-back depth. In this view that is the vertical image extent.

## Measurements (measure.py, profile.py; frame 0)
- Column intensity profiles at x = 740–1100 put the front edge at y = 292–293 in every column and the back edge at y ≈ 168–169 (clearest at x = 740 and 800).
  The depth is ≈ 124 px (±3).
  The automatic mask top of 150 in scene.json includes the wall shadow, so it was not used.
- The length is ≈ 555 px (710 → ~1265), for a sanity check only.
- Black cat pixel speed (scene/tracks/black_cat.csv): (last − first)/49 frames gives 10.97 px/frame from body_cx and 10.98 from bbox_x1 (head front). A linear fit gives 10.94 and 10.98.
  Speed ≈ 10.96 px/frame × 24 = 263 px/s.
- Scale = 0.94 / 263 = 3.574e-3 m/px (a single 2D scale).

## Answer
Width = 124 px × 3.574e-3 = **0.443 m**. As a sanity check, the length comes out at 555 px ≈ 1.98 m, so the stand is about 2.0 m × 0.44 m, which is plausible for a TV console.

## Second route / checks
- Scale from the head-front edge (bbox_x1) instead of the body centroid differs by less than 0.2%.
- The cat's tracked width (~41 px) gives ≈ 0.15 m, which is plausible for a cat.

## Caveats
This is a perspective camera, and the cabinet top sits above the floor while the cat walks on it. This may magnify the cabinet a few percent relative to the cat's scale.
A slightly lighter band at y ≈ 244–292 might be the visible front face, which would make the true top depth smaller. The two effects partly cancel, and the camera height cannot be recovered reliably, so a single 2D scale was used, as the 2D convention specifies.
Confidence: moderate (±10%).
