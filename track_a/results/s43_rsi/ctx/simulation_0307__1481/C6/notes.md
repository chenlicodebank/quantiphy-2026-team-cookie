Focal length f=3346 px solved from the exact prior (22.16 m/s) plus the two given camera distances (102.6664 m at t=1, 121.8263 m at t=2) and the plane's image positions; velocity v=(-0.475,-0.281,0.834). Rigid-body triangulation of the SAM silhouettes at frames 0/24/48 (residuals 0.1-0.5 m) gives the plane's two principal 3D axes: 19.89 m at 84.7 deg to the velocity (wingspan) and 10.61 m at 40 deg to the velocity, projecting along the image motion direction (fuselage, nose to tail). The nose end coincides with the visible pitot probe (1535,770) and the tail end with the rear fin (1910,960); the two engine exhausts are separated along the projected wingspan direction, confirming the assignment. Second route: exact pinhole projection of the fuselage segment at frames 0/24/48 gives 10.6 m at all three frames. Answer: length (nose to tail) = 10.6 m (width/wingspan 19.9 m).

Final message:
I've completed the measurement and submitted the answer.

**Summary of method:**
1. **Focal length**: Solved `|p₂−p₁| = 22.16 m/s` using the two given camera distances (102.6664 m at t=1, 121.8263 m at t=2) and the plane's image positions → **f = 3346 px** (hfov 41.9°). Cross-checked against the scene's image-speed law, which implies an axial depth law reproducing the given depths to 1.5%.

2. **3D reconstruction**: Since the plane translates with constant velocity, each material point satisfies `X₀ + v(t−1)` lying on its image ray. Least-squares triangulation over frames 0/24/48 (SAM 3 masks, residuals 0.1–0.5 m) recovered the plane's two principal axes:
   - **19.89 m** at 84.7° to the velocity → wingspan
   - **10.61 m** at 40° to the velocity, projecting along the image motion → fuselage (nose to tail)

3. **Identification checks**: the reconstructed nose coincides with the visible pitot probe; the tail end with the rear fin; the two engine exhausts are separated along the projected wingspan direction (confirming the axis assignment).

**Answer: length = 10.6 m** (wingspan/width 19.9 m), verified by a second route (exact pinhole projection of the fuselage segment at three frames all giving 10.6 m).
