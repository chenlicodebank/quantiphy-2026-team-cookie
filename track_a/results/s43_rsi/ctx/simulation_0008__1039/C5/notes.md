3D pinhole reconstruction: boat moves parallel to the image plane (constant apparent length), so its two given depths (7.452 m at t=0, 6.655 m at t=1) plus its pixel x positions give f=955 px and z_boat=5.72 m; the prior boat height 0.75 m (131 px silhouette) fixes the boat origin 0.375 m above the water. Pitch 1.49 deg from the pier platform's trapezoid (180/115 px) and camera height 1.43 m from the boat's waterline. The pier's outer (near) edge, anchored by the pier's given 11.579 m depth and the measured waterline at the posts (v=676), lies at z=8.52 m, 0.38 m above the water. Boat at t=3 s (frame 72 at question_fps=24, constant velocity extrapolation) is at (0.237, 0.910, 5.718) m; pier outer end at (0.045, 0.829, 8.516) m -> 2.81 m. Second route (pier origin at platform centre, no waterline measurement) gives z_outer=9.0 m -> 3.0 m, so 2.8 +- 0.3 m.

Final message:
I've completed the measurement and submitted the answer.

**Summary of the method:**

1. **Camera calibration (3D pinhole):** The boat's apparent length is constant, so it moves parallel to the image plane. Its two given depths (7.452 m at t=0, 6.655 m at t=1) combined with its pixel x positions give focal length f ≈ 955 px and boat depth z ≈ 5.72 m. The prior boat height (0.75 m ↔ 131 px silhouette) confirms the scale to 4%.

2. **Camera pose:** Pitch (1.49°) from the pier platform's trapezoid (near edge 180 px wide, far edge 115 px), camera height 1.43 m above the lake from the boat's waterline.

3. **Pier outer end:** The pier's given 11.579 m depth back-projects to the platform's centre; the waterline at the pier (v≈676, found from the reflection symmetry of the posts and platform front face) anchors the outer edge at z = 8.52 m, 0.38 m above the water.

4. **Boat at t=3 s:** Extrapolated at constant velocity to frame 72 (question_fps = 24) → (0.237, 0.910, 5.718) m.

**Answer: 2.8 m** (distance dominated by the ~2.8 m depth separation; second independent route gives 3.0 m).
