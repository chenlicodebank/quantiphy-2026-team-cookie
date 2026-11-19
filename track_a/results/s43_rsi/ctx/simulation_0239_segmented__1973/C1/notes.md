# q_1973: width of the house (m). Prior: brown horse speed = 0.874 m/s

## View
The camera looks straight down (the animals are seen from above with no legs showing). The house appears only as its roof: a main gable
roof with its ridge running along image y at x≈1018, and a cross-gable band across the middle (x 618-1423). The camera is static and
fps = question_fps = 24.

## Measurements (house.py, scene tracks)
- House mask at frame 10. Gable-end eave corners are at y≈97 (top, mean of 99/95) and y≈715 (bottom, mean of 714/716). The ridge ends
  are at y=25 and y=744. Radial perspective check: the ridge/eave magnification is s = 719/618 = 1.163, which puts the nadir at y≈538, the
  image centre. So the camera is top-down, and the ridge is closer to the camera than the eaves by a factor of 1.163.
- Footprint in eave-level pixels: y extent 618 px; x extent 699 px (main block x 662-1361). The ends of the cross band
  (618/1423) are at ridge height and match x 662-1361 at eave level after the same s. So length = x (699 px) and **width = y (618 px)**.
- Horse pixel speed: the mask centroid averaged over whole gait cycles. Frames 0→40 give 2.665 px/frame and frames 8→48 give 2.63. The
  bbox nose edge slope is 2.648, so I used 2.64 px/frame = 63.4 px/s. Frame 49 is a reset artifact and is excluded. This gives a scale of
  0.874/63.4 = 0.01379 m/px at the depth of the horse's back.

## Scale and depth correction
Naive single 2D scale: 618 × 0.01379 = 8.52 m. The eaves are higher than the horse's back, so they are closer to the camera and need a
smaller m/px. The roof geometry gives tan(pitch) = f/2488. With f ≈ 2000-2700 px (a pitch of about 40-47°, Blender's default 50 mm lens
is 2667 px), D_horse = 0.01379·f ≈ 28-37 m. With eave height minus horse-back height ≈ 1-1.5 m, the eave/horse depth ratio is ≈ 0.95-0.97,
so W ≈ 8.1-8.3 m. The full plausible range is 7.9-8.5 m.

## Check
Horse length: 148 px × 0.01379 = 2.04 m, which is a realistic horse, so the scene is roughly at real-world scale. The house footprint
is 8.2 × 9.3 m with a ridge about 5 m above the eaves, which is plausible.

Answer: **8.2 m** (the length reading, x extent, would be ≈ 9.3 m). Confidence: moderate. The main uncertainty is the depth difference
between the horse and the eaves (±4%).
