# Q563 – length of the wooden bench (m). Prior: speed of the black cat = 0.94 m/s. No depth_info.

Answer: **1.02 m**

## Time base
fps = question_fps = 24, so no re-timing.

## Scale from the prior
- Cat pixel speed: a linear fit of the mask centroid (scene/tracks/cat.csv, frames 0–49) gives 17.82 px/frame,
  which is 427.2 px/s. The bbox, torso and nose tracks agree within 0.3 %. The walk is steady and the camera is static.
- So 0.94 / 427.2 = 2.200 mm/px, horizontally, **at the cat's depth**.

## Why a single 2D scale is not enough
The render is a 3D scene with real perspective. The cat's paws touch the floor at y≈1023–1031, but the bench feet
are at y≈976 (back) and ≈1003.5 (front), so the bench is farther from the camera than the cat.
- Vanishing point (vp.py): I fitted lines to 11 slat grooves on the bench top, which run front-to-back. They meet at
  (951, 533). So the camera is level and not turned (the horizon is at the image centre).
- Depth is therefore ∝ 1/(y − 533) for floor points, and for any point u' = fX/Z, v' = f·Yh/Z, where Yh is the
  height below the camera.
- Camera height: h = (m/px at the cat) × (cat ground row − 533). The ground row under the cat's midline is ≈1026.5
  (near paws 1030, far paws ≈1023), giving h = 1.086 m.
- Height of the bench top below the camera, compared on the same depth line: top-back edge row 790 against back
  foot 976 gives 0.580; top-front edge row 808 against front foot 1003.5 gives 0.584. So Yh = 0.582 h.
  The back and front agree, which supports the model.
- Bench top ends, from colour-saturation edges on an average of 5 frames (bench2.py, redge.py), rows 800–806:
  - The right end is a clean depth line with X/Yh = 3.538 (x = 1899 → 1912).
  - The left end gives X/Yh = 1.921 (x = 1465 → 1472).
  - The front-right corner touches the frame edge at x=1919. That is why I used a depth-invariant ratio rather
    than a raw pixel span.
- L = (3.538 − 1.921) × 0.582 × 1.086 = **1.023 m** (solve.py).

## Checks
- Sensitivity (solve.py): moving the horizon by ±7 px (to 526 or 540, with VP x at 951 or 960) and the cat ground
  row from 1023 to 1030 keeps L between 1.015 and 1.031 m.
- Second route: scale the cat's mm/px by the depth ratio (cat ground v' = 493.5, bench mid-depth ground
  v' = 456.75, ratio 1.0805), giving 2.378 mm/px. The top span at mid-depth row 801 is 433.5 px, which gives 1.031 m.
- For reference, a naive single 2D scale gives 0.954 m. That underestimates the length because the bench is about
  8 % farther from the camera than the cat.
- The left end is ambiguous: the back-left corner at x=1455.5 on rows 790–799 would give X/Yh ≈ 1.96 and
  L ≈ 0.995 m.

Confidence: moderate to good, about ±3–4 %. The main remaining uncertainties are the exact bench ends (bevelled
corners) and the cat's ground row.

The scene record is fine for the cat. Its bench entry ("x 1455–1920, top length ~465 px") is a raw image extent
that mixes the back and front edges, and it does not account for the bench being farther away than the cat.
