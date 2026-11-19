# Q1345 — width of the purple car (m)

Prior: the white car (van) accelerates at 4 m/s². depth_info gives distances to the human, the taxi, the van and the bike at t=0.58 s (f14) and t=1.58 s (f38).
question_fps = file fps = 24. The purple car is a parked sedan (left foreground, cut off at the left edge) and is static.

## Camera calibration
- `lines.py` and `vp.py` use LSD line segments on scene/bg.png to find three vanishing points:
  road B (the car's axis) at (3148, 77), road A at (618, 84) and the vertical at (1110, 2134).
  Pairwise orthogonality gives f = 862, 861 and 822 px; the orthocentre gives f = 871 with the principal point at (1106, 567).
  **f = 850 px** (HFOV about 103°), with the principal point at the image centre. The ground normal comes from the two road vanishing points (`cam.py`).
- Camera height above the ground, H (`hped.py`, `hped2.py`): the pedestrian's pelvis is back-projected using its given depth
  (interpolated linearly for f30 and f66), and H is chosen so that the ground point under the feet lies vertically below the pelvis.
  Results: f38 6.75 / 6.76, f30 6.81, f66 6.77 → **H = 6.77 m**. The implied pelvis height is 0.83 m, which is plausible for a human about 1.75 m tall.
- Checks:
  - The purple car's near-side tyre contacts, intersected with the ground plane, give an axis parallel to road B within 0.03°.
    They give a wheelbase of 2.82 m, close to the Mercedes W116 the model resembles (2.865 m).
  - The van's ground-plane track, at the height fixed by its two depths (`vanacc.py`, `vanacc2.py`), gives an acceleration of about 4.1–4.5 m/s²
    (noisy, because the centroid is used as the reference). This is consistent with the 4 m/s² prior.
  - The bike's ground point fits H of about 7.1, if its origin is at ground level. Its origin height is unknown, so this is not used.

## Width measurement (`scan.py`, frame 5)
For each image column along the front fender and hood (x 456–558):
1. Find the near-side shoulder edge (the light top surface meeting the darker body side).
2. Back-project that point into the vertical plane through the near tyre-contact line. This gives its 3D position and its height, h ≈ 0.70–0.75 m.
3. Follow the image line toward road A's vanishing point (the horizontal direction across the car) to the far-side silhouette.
4. Intersect that ray with the plane at the same height. The lateral distance between the two points is the width.

Results:
- Mid-front fender and hood (x 456–504): 1.91–1.95, median about 1.92.
- Front taper (x 510–558): 1.72–1.88.
- Changing f between 820 and 870 (with H re-derived each time) changes the widths by less than 0.015 m.
- The body side is probably about 0.05 m outboard of the tyre contact line, which lowers the widths by about 0.015.
- Overlay: frames/scan.png.

The maximum body width is about **1.90 m**. The model resembles a W116, whose real width is 1.87 m, so this is a plausible sanity check.

## Second route / caveats
- Front-bumper chord (`purple.py`, `bumper.py`): 1.5–1.67 m. This route is unreliable: the camera views the front face at a grazing
  angle of about 13° (it is only about 2 m in front of the bumper plane), so the far end of the bumper is hidden or ambiguous.
  `predict.py` shows that a 1.9 m width projects the far front corner onto the observed hood corner at (572–582, 650).
- Mirrors do not visibly stick out beyond the far silhouette, so the answer is the body width.
- Confidence: moderate, about ±5%. The main uncertainty is H, which comes from the pedestrian route.
