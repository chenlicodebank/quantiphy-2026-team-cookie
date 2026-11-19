# Q1236 – length of the turning yellow car (taxi)

Answer: **5.0 m**. The file and question_fps are both 24.

## Scale: focal length
Principal point (1080,540). The horizon is at row 422.5 and the main-road vanishing point is at (1253,422.5), both from scene/_vp.json. Together they give the ground normal and the road directions for any f.
- The prior is the white van's acceleration, 4 m/s². The van origin line comes from the given depths at t=0.58 and 1.58 (frames 14 and 38). Each frame's box is projected onto that line, and a quadratic is fitted to s(t).
  - Box-centre version: f = 2232–2237 (accel.py, accel2.py).
  - Rear-edge version: f = 2172–2206.
  - 3D van box model with silhouette corners, using only frames where both edges were measured: f = 2167 (vanmodel.py). The residuals are about 1 cm, so the acceleration is uniform.
- Check without the prior: at f ≈ 2200–2230 the van's 3D path from the two depths runs parallel to the cross street, within 0.1–0.5°. That cross-street direction is perpendicular to the main-road vanishing direction. The cyclist's path gives f ≈ 2000–2200, and the curb-slope vanishing point gives about 2100 (this one is very sensitive).
- Adopted f = 2195 ± 40 px, which is a horizontal field of view of about 53°.

## Taxi pixel extent
I measured the extent of the yellow paint mask in code (extent.py, overlay at frames/ext14.png). Bumper to bumper it is 467 px, constant over frames 0–17. At frame 14 it spans 384 to 851 px.
- Correction to the record: the scene track has x0 = 367 at frame 14, but the true rear bumper is at 384. The track's left edge was contaminated by the van's wheel.
- The car's heading comes from the near-side tyre contact rows, mapped through the ground homography (contacts.py, route2.py). It is 13° toward the camera at frame 14 and 1.4° at frame 3.

## Length
I modelled the car as a 3D box with W/L = 0.37 and the bumper band at 0.05–0.12 L. The model's left and right silhouette extremes were fitted to the measured pixel extremes (boxmodel.py, route2.py).
- **Route 1 (frame 14):** origin on the ray at the given depth 25.704 m. L = 4.94–4.98 m for heading 10.5–14°.
- **Route 2:** camera height H = 2.84 m, calibrated from frame 14. Then at frame 3 (nearly pure side view) the ground plane gives depth 27.1 m and L = 5.05 m.
- **Check at frame 38:** the ground-plane model predicts a taxi depth of 21.8–22.1 m against the given 22.29 m, which agrees to 1–2%.
- **Sensitivity:**
  - f ±40 px changes L by ∓1.8%.
  - W/L of 0.33 or 0.41 changes L by +1.7% / −1.7%.
  - Origin height has a negligible effect.

Confidence: moderate-good, about ±4%.
