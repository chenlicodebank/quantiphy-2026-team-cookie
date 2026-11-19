# q1087 – length of the bench seat (atrium), simulation_0017

The file runs at 33.039 fps and the question at 33.0 fps. I used frame numbers and 33.0 fps throughout.

## What the scene is
The image is rolled 90° (world up = image +x). Viewed upright (`rot.py` → frames/upright_60.png), it shows an atrium:
- in the foreground, a long bench: a dark seat slab with 4 grey cushions, on X-shaped legs and a base plinth;
- behind it, a person walking left to right in the upright view;
- a sculpture on a pedestal, and art panels on stands in front of the back wall.

The scene/ record calls this a "sofa / living room". It is the bench. The camera is horizontal and static: the wall
grid is frontal and uniform.

## Camera (fit_person.py)
- Person pelvis track (scene/tracks/human.csv, frames 5–100): it moves 7.54 px/frame along image y, while image x
  stays constant.
- Model: the person walks at constant Z with lateral offset Z·(y−540)/f. I fit it to d(t=0)=5.424 m, d(t=1)=4.886 m
  and the 1.3 m/s speed.
- Result: Z = 4.65 m, f ≈ 892 px.
- Checks:
  - Fitting to the depths alone predicts a speed of 1.297 m/s (the prior is 1.3).
  - The pelvis track and the head track agree within 1 %.
  - Person height = 1.82–1.84 m.
- Camera height from the person's soles (x≈355 at Z 4.65): 0.965 m.

## Bench measurements (profile2.py, frame 100, with sub-pixel thresholds)
- The front corners of the seat slab are its farthest-reaching points: image y 11.6 → 1059.1, so **L_px = 1047.5 px**.
  The slab is centred on the image, so it lies parallel to the image plane.
- Cushions: front-top edge at x = 327.5, back-top edge at x = 381.5. This gives Z_back/Z_front = 1.341, so the
  seat depth is about 0.34·Z_front.
- The origin is taken as the centre of the bounding box. The sculpture/pedestal depths (5.962 vs 5.963 m) are only
  consistent with centre origins, not bottom origins.
- Solving centre distance = 2.267 m (solve_bench.py) gives:
  - Z_front = 1.84 m, bench depth ≈ 0.63 m, cushion top ≈ 0.53 m above the floor;
  - **length = 1047.5 × 1.842 / 892 = 2.16 m**.

## Checks and sensitivity
- The plinth's floor-contact line (x≈108) gives Z = 1.99 m. That puts the plinth just behind the seat front, which
  is consistent: the seat overhangs.
- If the bench depth is 0.50 m instead, the length is 2.24 m. If it is 0.75 m, the length is 2.09 m.
- Using the origin depth directly for the front corners would give 2.53 m. That is wrong, because the corners are
  closer to the camera than the origin.
- The given "freestanding art display panel" distance (4.223 m) does not match the visible panels. Those stand near
  the back wall, roughly 12 m away by floor contact, and the person passes in front of them. I did not use it.

Confidence: moderate, about ±4 %. The main uncertainty is the bench depth used to place the front edge.
