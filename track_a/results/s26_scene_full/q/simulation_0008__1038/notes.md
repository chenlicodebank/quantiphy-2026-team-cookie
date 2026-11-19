# Q1038 – length of the pier (jetty), shore-side edge to water-side edge

The pier points almost straight at the camera: the deck's centre line runs x 552→555 and vanishes near x≈545, close to cx = 540.
So its length is a depth difference: L = Z_back − Z_front. The camera is static, and frame 0 is used.

## Measurements (frame 0; scripts vprof.py, blobs.py, edges.py, overlay.py)
- Deck top, water-side (front) edge: v = 629.3. Below it is a bright bevel at 628, a dark gap at 630, and the front face from 630 to 644.5.
- Deck top, shore-side (back) edge: v = 588.5, where the grass turns into wood (saturation step in vprof.py).
- Horizon / vanishing row of the deck plane, vh = 530.8 ± 2. This comes from the dark post/beam ends that sit in pairs at three positions along the deck. Their pixel separation w is proportional to (v − vh):
  - back pair: 103.4 px at v 595.9
  - front pair: 146.7 px at v 623.1
  - middle pair: predicted 123.5 px, measured about 124
  
  A rough fit of the deck side lines gives vh 529–532, which agrees.
- Water line at the front legs: v = 675.5, the mirror midpoint of the front face (645↔706) and the deck edge (629↔722).

## Route 1 (main): deck plane + pier-origin depth
On a horizontal plane Z ∝ 1/(v − vh), so r = Z_b/Z_f = (629.3−530.8)/(588.5−530.8) = 1.707.
The pier origin is taken as the box centre, Z_c = (Z_f+Z_b)/2. From 11.579 m, after removing the small vertical offset (camera about 1 m above the origin) and lateral offset, Z_c ≈ 11.52 m.
This gives Z_f = 8.51 m, Z_b = 14.53 m and **L = 6.02 m**. This route does not depend on the focal length.
Sensitivity: vh ±2 px → L 5.8–6.2; an edge row ±1 px → ±0.2 m.

## Route 2 (check): boat waterline
- Focal length from the two boat depths (constant Z, since the boat's apparent size is constant; origin at the box centre): f ≈ 975–1000 px and Z_boat ≈ 5.80–5.86 m. Both t = 1 s frames (23 at 22.8 fps, 24 at 24 fps) were tried; the difference is small.
- The camera height is shared by the boat and the pier: Z_f = Z_bw·(757 − vh)/(675.5 − vh).
- If the boat's near-side waterline lies about 0.4 m in front of its origin (a waterline beam of about 0.8–1 m), solving jointly gives vh ≈ 531, r ≈ 1.71 and L ≈ 6.0 m. This matches route 1.
- Over plausible half-beams of 0.25–0.65 m, L spans 5.7–6.5 m.

## Caveats
- The deck's side edges are stepped: it is made of three plank sections with rounded ends. Because of that, the width ratio of the deck's outline (178 / ~110 px → r ≈ 1.62, L ≈ 5.5 m) is less reliable than the post pairs and the vertical rows.
- The boat prior (0.75 m ↔ ~127 px for a centre origin, while 133–142 px are visible above the water) is slightly inconsistent. This only affects route 2.
- Time base: only the t = 1 s boat depth uses time. Frames 23 and 24 give f 976 vs 1003, which hardly changes anything.

Answer: **6.0 m**. Confidence: moderate (±5–8 %).
