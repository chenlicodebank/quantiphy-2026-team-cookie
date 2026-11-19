# Q934 — width of the spacecraft (m)

Scene: 2D top-down render. One dark vehicle drives straight left (−x) from rest with constant acceleration. The file runs at 24 fps and question_fps is also 24, so there is no re-timing issue.

Scale from the prior (acceleration at 1.0 s = 4 m/s²):
- accel.py fits a quadratic to the reference-point track in scene/tracks/vehicle.csv (bbox centre, checked against the frame at t = 1.0 s).
  - ref_x, frames 7–50: a = 1.2048 px/frame² = 694.0 px/s² (max residual 0.7 px).
  - Frames 2–50: 693.8. Window 14–34 (around t = 1.0 s): 691.4.
  - The per-frame step grows steadily by about 1.2 px/frame, so the acceleration is constant and its value at 1.0 s equals the fitted value.
  - The nose (707) and tail (679) differ slightly because the model stretches along x. The centre is their mean and is used as the origin.
- Scale: 4 / 694 = 0.005764 m/px.

Width: the vehicle's shorter horizontal extent, across the motion (y), is 515 px (rows 462–976). It stays constant in every fully visible frame (514–516). The length is about 1012 px at rest.

Width = 515 × 0.005764 = 2.968 m, answered as 2.97 m.

Second route: using the local window around t = 1 s (691.4 px/s²) gives 2.98 m, and using the nose or tail tracks gives 2.91–3.04 m. These agree to within about 2%.

Other readings: the length would be about 5.83 m, but the question asks for width, which is the shorter extent.

Confidence: high (about ±2%).
