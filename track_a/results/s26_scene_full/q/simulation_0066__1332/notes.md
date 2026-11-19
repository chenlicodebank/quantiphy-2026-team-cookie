# q_1332 — width of the white car (white Chevrolet-style van), simulation_0066

The file rate and question_fps are both 24. t=0.58 s maps to f14 and t=1.58 s to f38.
The white car is the `van` in scene/ (the white van with brown windows).

## Camera (scale-free geometry)
- Focal length from the static scene (`lines.py`, `vp.py`). I fitted line segments with LSD on scene/bg.png and computed
  vanishing points by least squares:
  - road B (left-right curbs): (3144, 74)
  - road A (receding curbs): (613, 100)
  - verticals (lamp and traffic-light poles): (1085, 2111)
  - The orthocentre of the three VPs is (1063–1070, 539–562), essentially the image centre. f = 828–872 px from the
    various pairings. **Used f = 845 px** (HFOV about 104°).
- Pose (`pose.py`): world X = road B, Y = road A, Z = up. The angle between the road directions is 91.1°, and the up axis is
  0.6° from the vertical VP, so the pose is consistent.
- Checks of f = 845:
  - The pedestrian's pelvis back-projected at the given depth lies at the same height in f14 and f38 (z = -5.71 both),
    0.98 m above the feet. That implies a human of about 1.85 m.
  - Van displacement f14→f38 from the two given depths is 4.25 m (f-dependent). The prior (a = 4 m/s² from rest at
    t ≈ 0) gives 4.17–4.33 m, which fits f = 800–880.
  - Van, cyclist and taxi f14→f38 displacements are horizontal; the van and cyclist move along −Y (road A).
- An acceleration fit to the centroid track alone is weakly sensitive to f and biased by the centroid proxy, so I did not
  use it for f.

## Body width (route 1: depth-anchored, f14 and f38)
- Front face from the left headlamp's outer edge (the front-left body corner) to the right body silhouette, measured
  along the road-B vanishing direction:
  - f14: (1038, 365) → (1114, 354.5)
  - f38: (1129, 427) → (1216, 412)
- Both pixels were back-projected onto the vertical plane Y = Y_front, where:
  - Y_front = Y_origin − (L/2 − 0.15)
  - Y_origin = sqrt(D² − X² − z²), with X = 8.4 m and z between the centroid height and the ground (−5.8 … −6.69)
  - L = 5.7–6.2 m
- Results: f14 W = 2.00–2.06 m; f38 W = 2.03–2.11 m. **Body width ≈ 2.05 m.**
- The recovered point heights (about 0.9–1.1 m above ground) are consistent with headlamp level.

## Mirror-to-mirror width (route 2: bounding-box width)
- Both door-mirror tips are visible at f50, f60 and f66. The line joining them points to the road-B VP, which confirms
  they are the left/right pair at the same height.
  - f50: (1189, 442) / (1310, 418)
  - f60: (1350, 548) / (1490, 508)
  - f66: (1522, 662) / (1680, 603)
- Scale in the same frame: the front-face width (2.05 m) fixes the front plane's Y. The mirror plane's offset d behind
  the front was solved from symmetry (mirror midpoint = body midpoint), giving d = 1.16–1.28 m. Mirror height is about
  1.5 m.
- Spans: f50 2.54 m, f60 2.42 m, f66 2.37 m. **Mean about 2.44 m; the sharper f60/f66 give 2.40 m.**

## Answer
- Sizes are defined as the world AABB, and the van drives along a world axis, so the AABB width includes the door
  mirrors. **Answer: 2.42 m.**
- The other reading (body only, "wheel to wheel") would be about 2.05 m.
- Confidence: moderate. The measurement is about ±4%; the main risk is whether the reference counts the mirrors.
- Note on the record in scene/: the late-frame centroid kinematics disagree with a = 4 from rest (the van appears further
  along than predicted after about f55). I did not rely on them.
