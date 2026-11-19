# q3088: distance between the two bottles (cm)

Prior: the rolling cylinder's velocity is 107.3 cm/s. I used the internet-video convention: one planar scale = prior / pixel speed.

## Time base
The file runs at 30.013 fps and question_fps is 30. That difference is negligible, so I used 30 fps.

## Cylinder pixel speed (speed.py, from scene/tracks/cylinder.csv, stabilised centroid)
I used frames 4-30, where the cylinder is fully in view.
- Mean of the per-frame displacements: 61.3 px/frame.
- Net displacement over frames 4-30: 61.2 px/frame.
- Leading edge (bbox_x0): 59.5 px/frame.
- Frames 12-24 (around the bottles): 59.1 px/frame. Frames 16-24: 60.0 px/frame.

I took 60.5 px/frame, which is 1815 px/s, giving a scale of 107.3 / 1815 = 0.0591 cm/px.

## Bottle positions (bottles.py, frame 44, the clean background; also gridded crop frames/bottles.png)
- Tea bottle centre: x ≈ 717-718. The cap centre is at about 712.
- Green bottle centre: x ≈ 958-959.
- Centre-to-centre: 239-243 px. static_objects.json gives 241 px (959 - 718). I used 241 px.
- Both bottles stand on the same contact line (y ≈ 717-721), so the separation is horizontal.

## Answer
241 px × 0.0591 cm/px = **14.25 cm**, centre to centre.

The other reading is the edge-to-edge gap: 98 px (tea x1 787 to green x0 885), which is 5.8 cm. I did not use it, because "distance between" objects is taken to mean between their centres.

## Checks and confidence
- A scale from the frames 16-24 speed alone (60.0 px/frame) gives 14.4 cm.
- A scale from the mean per-frame speed (61.3 px/frame) gives 14.1 cm.
- Sanity check: the tea bottle's width is 138 px, which is 8.2 cm, and the cylinder's diameter is about 185 px, which is 10.9 cm. Both are plausible.
- The bottles sit farther from the camera than the cylinder, so the real distance is somewhat larger. The annotators' convention ignores this.

Confidence: moderate. The main uncertainty is which pixel speed the annotators used for the prior (±3%) and the centre-versus-gap reading.
