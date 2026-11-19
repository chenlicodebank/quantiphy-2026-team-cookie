# q_1681 – height of the rock (m)

Prior: boat speed is 4 m/s. Depth: boat 90.1103 m at t=1 s and 90.4360 m at t=2 s. question_fps = 24, but the file is 25 fps,
so I used frame indices: t=1 is frame 24 and t=2 is frame 48. The boat moves 4/24 m per frame, so it covers 4 m between
those two frames.

## Focal length (solve.py)
I fitted boat pixel tracks from scene/tracks/boat.csv linearly over frames 3–74 (-6.43 px/frame in x, about -0.3 px/frame in y).
Then I back-projected the boat's image positions at frames 24 and 48 using the given depths, with the principal point at the
image centre, and solved for f so that the 3D displacement is 4 m.
f = 3497 / 3503 / 3496 px using the bbox centre, mask centroid and keel point, so f ≈ 3499 px (HFOV ≈ 15.6°).
The direction of motion has a component away from the camera (+0.10). Assuming the boat moves horizontally, this gives a camera
pitch of 21.7–26.3° downward. This fits the deck being visible from above.

## Rock (rock.py, contour.py)
The rock is static. Its image extent is y 24–313 (290 px) and x 326–959 (truncated at the right edge). Its top is at (513, 24) and
its lowest edge point is at (692, 313).
- Route A (water-plane geometry): I put the water plane through the boat's keel and found the camera height to be about 38–44 m.
  The nearest waterline point of the rock is about 110–116 m from the camera, roughly 15–20 m behind the boat. I then took the
  rock's peak to be 5–12 m behind that nearest waterline point. The top ray at v=24 gives a height above the water of
  H = 6.2–8.5 m; for Rd ≈ 9 m and pitch 22–24°, H ≈ 7.1–7.5 m. If Rd = 0 (a vertical front face), H ≈ 9.6–9.8 m, which is an upper bound.
- Route B (simple pinhole at the boat's depth): 290 px × 90.3 m / 3499 px = 7.5 m.
Answer: 7.4 m.

Confidence: moderate. The rock's depth is not given and has to be inferred from the pitch, which is sensitive to the small
vertical drift. If the rock mesh extends below the water, its true bounding-box height would be larger than what is visible.
Rock width at its range is about 20 m or more (truncated), so the rock is wider than it is tall, which is consistent.
