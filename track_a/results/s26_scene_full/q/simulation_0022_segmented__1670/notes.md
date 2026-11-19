# q_1670 — length of the rock (m); prior: boat length = 10 m; depth: boat 148.745 m (t=1), 146.973 m (t=2)

File fps 25, question_fps 24 (frame = round(t*24)). The rock is the static pale island (x 31–557, y 529–655).

## Measurements (scripts in this folder)
- `perframe.py`: masked least-squares fit (sx, sy, rotation, tx, ty) of the frame-50 boat into every frame.
  The boat approaches (sy 0.988 -> 1.011), and its centroid row (y=622.5) shifts by ty = (sy-1)*30.0 px.
  `horizon_fit.py`: the fixed row is y_h = 592.5. Frames 2–35 give 592.3 and frames 36–74 give 593.2, so this is
  the camera-height (horizon) row for a boat moving on a horizontal plane. No roll: the keel is level and the rotation is < 0.1 deg.
- Focal length: the boat is 289 px long at ~146.5 m depth, so f ≈ 289*146.5/10 ≈ 4280 px (12.8° hFOV). A depth-rate check
  (depth_info Δd = 1.77 m/s against the sy growth of 0.9%/s) gives f ≈ 3500–4300. The answer depends only weakly on f.
- `boatbottom.py`: at frame 50 the keel bottom is at y≈678 (flat), the rudder at 687, and Z_boat ≈ 146.5 m
  (d at t=50/24 = 146.83 m, less the lateral and vertical offsets).
- `rockprof.py`: the rock's bottom silhouette is a straight line (a planar base or water cut), y = 627 at x≈31–45 and
  655 at x=557.

## Geometry
For points on the same horizontal plane, (y − y_h) ∝ 1/Z. The plane is at the boat's keel, which is 85.5 px below the horizon at Z = 146.5 m.
- Rock left end: 34.5 px below the horizon, so Z = 363 m and X = (31−480)/4280*363 = −38 m.
- Rock right tip: 62.5 px below the horizon, so Z = 200 m and X = +3.6 m.
- Horizontal end-to-end length = sqrt(162.6² + 41.7²) ≈ 168 m. The rock is a long, low island seen nearly
  end-on: its vanishing direction is about 14° off the optical axis, and its peak is about 7 m high.

## Variants / confidence
- If the plane is at the rudder bottom (687): ≈ 186 m. If it is at the red/dark paint line (~662): ≈ 136 m.
- If the rock were at the boat's depth (no ground-plane reasoning), the pixel ratio gives 527/289*10 ≈ 18 m. This would need the
  rock's base to float 1–2 m above the keel plane and be tilted 3°, so I rejected it.
- The answer is very sensitive to the horizon: ±2 px gives about ±6%. Overall confidence is low to moderate. Answer: 168 m.
