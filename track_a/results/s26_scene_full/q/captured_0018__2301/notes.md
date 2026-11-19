# q2301 — shoe length of the left person (cm)

The left person is the farther one (light top, green cargo trousers, white Samba-style shoes with three black stripes).
depth_info: distance_far_person_camera = 3.130 m. The camera is the lab Orbbec: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
The file and the question both run at 24 fps. The person stands still, so I averaged frames 0, 10, 20 and 48.

## Pixel measurement (edges.py, shoe_mask.py, frames/shoe_0.png)
- I measured the near shoe (the right foot, lateral side facing the camera). The far shoe's heel is hidden.
- The heel back is the half-intensity edge against the floor on rows 558-563: x ≈ 347.8-348.4.
- The toe front is the edge on rows 566-569: x ≈ 396.6-398.5; I take ≈ 398.5 (±1).
- Horizontal extent: Δu ≈ 50.5 px (±1.5).
- Orientation: the floor contacts are heel ≈ (350, 571.5) and toe ≈ (397, 574.5), and the lowest point of the lateral sole is 577.5 at x ≈ 380.
  With the horizon at y ≈ 342 and a camera height of ~0.85 m, these give a toe-towards-camera angle φ ≈ 10-15°.
  So the shoe is close to parallel to the image plane. The far shoe's medial sole edge is flat in the image, which agrees.

## Scale
- Card method: 3.13 m x 50.5 / 762.8 = 20.7 cm (horizontal image extent).
- Foreshortening at φ ≈ 12° with rounded ends (width ~8.5 cm): L ≈ (20.7 - 8.5)/cos12° + 8.5 ≈ 21.0 cm.
  A rectangle model would give 19.4 cm, and using the z-depth 2.97 m instead of the Euclidean 3.13 m would give about 5% less.
- Final answer: 21.2 cm. I nudged it slightly up because real adult shoes are usually 23 cm or longer.

## Checks and confidence
- Sanity check: the person's height of 402 px at this depth is about 1.56-1.65 m, and the head width is about 15.6 cm, so the scale is plausible.
- Inconsistency: the floor geometry does not quite agree with the given depths.
  The soccer ball (2.8 m) lands higher in the image than the left person's feet, which would put the feet nearer than 2.8 m.
  So the depth of the feet is uncertain by about ±8%.
- Confidence: moderate. The expected error is about ±10%, driven by the foot's depth and its angle φ.
