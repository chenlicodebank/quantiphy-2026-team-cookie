# q_576 — lampshade diameter (simulation_0213)

Question: diameter of the table lamp's shade (m). Prior: black cat speed = 0.94 m/s. No depth_info. fps = question_fps = 24.

## Scale from the cat (prior)
- The cat walks at a steady pace, parallel to the image plane. Linear fits over its visible frames (scene/tracks/cat.csv, checked in measure.py):
  - nose bbox_x1: 17.76 px/frame (rms 0.7 px)
  - fit_bbox_cx: 17.71 px/frame
  - centroid: 17.81 px/frame
  - I use 17.74 px/frame = 425.8 px/s, so k_cat = 0.94 / 425.8 = 2.208 mm/px in the cat's lane.

## Lampshade pixel width (measure.py, vert.py)
- The shade is a white pleated cone, faint against the grey wall. I found its edges at the half level between shade and wall, row by row, at frame 48.
- The widest row is y≈602, at the bottom rim: edges at 1409.2 and 1622.5, so W = 213.3 px. The scene record gives 216, which agrees.
- The shade centre is at x = 1515.9. The lamp-base centre line is at x = 1515.3–1515.7 over y 630–770. Verticals stay vertical, so the camera is level to within about 1° and I put the horizon at y≈540.

## Depth correction (the scene is called 2D, but the lamp is clearly behind the cat)
- The cat's paws touch the floor at y≈1008–1020. Its body-centre lane is about y = 1015.
- The table top runs from y=782 (back edge) to y=806 (front edge). The legs' feet are at y=965 (back) and y=993 (front).
- I assumed the top overhangs the legs equally front and back. Then the top's middle (y=794) sits over floor y=979, and a horizontal plane at table-top height maps to the floor as (y−540) = 0.579·(y_floor−540).
- The lamp base touches the table at y≈790. Its centre is about 3.5 px further back (the foot is a circle seen nearly edge-on), at y≈786.5. That puts the lamp's floor line at y≈966.
- Depth ratio Z_lamp / Z_cat = (1015−540) / (966−540) = 1.115. Over plausible inputs it ranges from 1.09 to 1.14; it barely depends on the horizon (±10 px changes it by under 0.5%).

## Off-axis correction (focal length)
- The lamp is 556 px right of the image centre. A horizontal circle seen off-axis looks wider by sec α, where α = atan(556/f).
- I estimated f from how much horizontal circles sag in the image (half minor axis ≈ a·(y−y_h)/sqrt(f²+dx²)):
  - shade bottom rim (rim.py): sag 4.5 px → f ≈ 1400 (1150–1650 depending on the horizon)
  - edge of the vase's blue band (vase_bands3.py): sag ≈ 3.2 px → f ≈ 1900–2050
  - vase foot: too noisy to use (f 1500–4400)
- I take f ≈ 1600 ± 300, giving cos α ≈ 0.944 (range 0.92–0.96).

## Result
D = W × k_cat × (Z_lamp/Z_cat) × cos α = 213.3 × 2.208e-3 × 1.115 × 0.944 ≈ **0.496 m**

## Checks and confidence
- With a single flat scale and no corrections, D would be 0.471 m. With the depth correction only, it would be 0.525 m.
- The scale is consistent with the rest of the scene:
  - lamp height 289 px → about 0.71 m
  - camera height ≈ 1.05 m
  - table top height ≈ 0.44 m
- Main uncertainties: the focal length (±2–3% on the answer) and the lamp's depth on the table (±2.5%). Expected error is about 4–5%.
