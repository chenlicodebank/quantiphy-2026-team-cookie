# q_1960 — speed of the swimming ring (flamingo float) at t = 0.5 s

Prior: the black cat's speed is 1.041 m/s. No depth_info. fps = question_fps = 24, so t = 0.5 s is frame 12.

## Pixel speeds
- **Cat** (scene/tracks/cat.csv): it walks at a steady pace. A linear fit over frames 0–49 gives 5.465 px/frame
  for the centroid, 5.463 for the nose edge (bbox x1) and 5.439 for the tail edge (x0). I used 5.465 px/frame.
- **Float**: I re-measured it with my own background-difference mask (measure.py). It agrees with the record, and
  both bbox edges match. The one-frame backward difference p(12) − p(11) is 9.3 for the record centroid, 9.48 for
  my lower-body centroid, 9.0 for x0 and 10.0 for x1. Local quadratic and cubic fits (half-widths 3–8 frames,
  evaluated as p(12) − p(11)) give 9.34–9.66 px/frame. I used **9.48 px/frame**. The ring accelerates smoothly
  here, with no impact nearby.
- With one 2D scale (equal depths): v = 9.48 / 5.465 × 1.041 = **1.81 m/s**.

## Depth correction (perspective)
The scene has clear perspective: identical lounge chairs in the back row look 142.5 px tall and those in the
front row 166.5 px tall. The objects stand on a common ground plane, and the float sits much lower in the image
than the cat, so it is nearer the camera.
- **Horizon** from the chairs (bgchairs.py, legs.py):
  - Back row: top 713.5, front-leg bottom 856. Front row: top 734, front-leg bottom 900.5. This gives yh ≈ 592.
  - The seat-edge and leg-bottom pair (823/856 against 861/900.5) gives yh ≈ 593.
  - The record's rounded heights give yh ≈ 575.
  - I used yh ≈ 590 ± 15.
- **Ground rows**: the cat's paws are at y ≈ 917. The float's front-bottom edge is at 1018 at frame 12, and the
  centre of its footprint is about 9 px higher (ring viewed at a shallow angle), so y ≈ 1009 ± 4.
- **Depth ratio** Z_float / Z_cat = (917 − yh) / (1009 − yh) = 0.78. Across the horizon and footprint
  uncertainties it ranges from 0.77 to 0.79.
- Corrected speed: 1.81 × 0.78 = 1.41 m/s. I answered **1.42 m/s**, a little above that. If the float rests on
  water below the deck level rather than on the deck, the ratio would be closer to 1.

## Check / confidence
- The float speed agrees across four reference points (two centroids and both edges) and several fit windows,
  to within ±2%. The cat speed agrees across centroid, nose and tail to within 0.5%.
- The main uncertainty is the depth correction. Without it the answer would be 1.81 m/s, so the two cases differ
  by about 22%. I applied it because Blender ground truth is 3D and the chair rows show clear perspective with the
  objects on the ground. Confidence is moderate.
