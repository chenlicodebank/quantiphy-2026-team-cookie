# Q1350 — length of the white car (the white cargo van), in metres

Answer: **5.88 m**

The file's frame rate and question_fps are both 24 fps. The "white car" is the white van (scene/tracks/van.csv). It drives
in a straight line toward the upper-left road.

## Scale from the prior (a = 4 m/s²)
- I ran KLT tracking on van features, frames 15–71 (`track.py 15 71`) and frames 3–45 (`track.py 3 45`), with a
  forward–backward check.
- All of the van's rigid-feature tracks are straight lines through one vanishing point, V = (119.3, -43.4). V lies on
  the horizon (y ≈ -45), so the van translates horizontally along a fixed direction u.
- For a point translating along u, the image distance to V is δ = c/z. So 1/δ_k(t) = A_k + B_k·s(t), where s(t) is
  shared by all tracks. A robust rank-1 factorisation (`joint.py`) recovers s(t) up to an affine map. The second
  singular value is 0.3 % of the first.
- s(t) is an exact quadratic: rms 2 mm, and a cubic fit gives an acceleration of 4.02 → 3.98. Setting s'' = 4 m/s²
  fixes the metric scale. The vertex is at t ≈ -0.045 s.
- Depth of every tracked point: z_k = (u_z / B_k) / δ_k, with u = K⁻¹(V, 1).

## Focal length (it has only a weak effect on the length)
- Vanishing points of the two perpendicular roads: f ≈ 1100–1107 px. The scene's vertical vanishing point gives ≈ 1100.
- The pedestrian's depth_info (pelvis, with the feet on the vertical through it) gives a camera height that matches the
  van-derived camera height at f ≈ 1120–1200 (`camh.py`).
- I used f = 1100. Over f = 1000–1200 the wheelbase does not change (3.759 m) and the bumper-corner offsets change by
  under 1 cm.

## Length = rear overhang + wheelbase + front overhang (f = 1100)
- **Wheelbase:** rim centres were fitted as ellipses (`rims.py`) at frames 24 and 48. Each hub depth comes from its
  δ ratio over the known s(48) − s(24) (`hubs.py`).
  - Wheelbase = 3.759 m (lateral and vertical mismatch < 3 mm).
  - Hub height = 0.37 m above ground, which matches the tyre radius.
  - The predicted front hub at frame 14 lands on the observed rim centre (1162, 740) to within 0.5 cm.
- **Rear overhang:** the rear-bumper features on the rear face are 1.20–1.24 m behind the rear hub (from the tracked
  cloud). The body's rear corner is 1.0 m behind it.
- **Front overhang:** the front face is never visible (the camera sees the van from behind-left and above).
  - The front bumper's near corner (frame 14: (1112, 668); frame 30: (975, 570)), intersected with the hub plane, is
    0.72–0.77 m ahead of the front hub. Allowing the corner to sit 5–8 cm inboard gives 0.80–0.87 m.
  - The hood front edge, seen as a silhouette across the width (`hood.py`), is nearly perpendicular to u, curved by
    about 0.1 m from centre to corner. So the bumper centre probably sits a further ~0.05–0.1 m forward.
  - Estimate: 0.87 ± 0.07 m.
- **Total:** L ≈ 1.22 + 3.76 + 0.87 ≈ 5.85 m.
  - Lower bound: the directly tracked extent (rear bumper to the furthest visible front point) is 5.55–5.71 m.
  - Plausible range: 5.75–5.95 m.

## Checks
- **depth_info:** with the origin at the van's bottom centre (vehicle root on the ground), the reconstruction gives
  camera distances of 10.64 / 13.08 m at frames 14 / 38 for f = 1100, and 10.46 / 12.80 m for f = 1050. The given
  values are 10.624 / 12.810. So the prior's scale and the depth scale agree within about 2 %. A box-centre origin
  fits worse.
- **Real-world sanity:** a Chevy Express 155" scaled to the measured wheelbase (3.76 / 3.94) would be about 5.92 m
  long. Its length/wheelbase ratio of 1.57 matches the measured 1.56.
- **Final:** 5.88 m. Most of the uncertainty is the hidden front bumper, ±0.1 m (about 2 %).

## Notes on the scene record
- The record's van bbox is clipped by the image edges in frames 0–14, as it states.
- The bbox centre is not the origin's projection, so I used it only to restrict masks.
- The answer relies only on frame indices; no times from scene/ are used.

Scripts: track.py, fit.py, joint.py, cloud.py, box.py, solve.py, run_koff.py, scale.py, camh.py, rims.py, hubs.py,
corner.py, hood.py, origin_check.py, crop.py.
