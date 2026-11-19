3D pinhole: depth_info gives radial speed 1.1153 m/s; with prior speed 1.29 m/s the tangential speed is 0.648 m/s. Rigid torso template tracking gives 430 px image displacement between t=1 and t=2, solving |P2-P1|=1.29 gives f=3804 px (cross-check from per-frame torso pixel speeds: 3820/3983 px; apparent-size ratio 0.82-0.86 matches the depth ratio 0.824). Nose-to-tail-tip length measured on the least-foreshortened frame (frame 0, body/tail extended): 646 px at z0=4.34 m (from wingspan ratio) -> 646*4.34/3900 = 0.72 m; horizontal-body 3D reconstruction gives 0.70-0.74 m for a 30-40 deg camera pitch.

Final message:
I measured the dragon's body length as **0.72 m**.

Method summary:
- **Focal length**: from the depth_info radial speed (5.2108→6.3261 m over 1 s = 1.1153 m/s) and the 1.29 m/s speed prior, the tangential speed is 0.648 m/s. Tracking the rigid torso (not the wing-beat-noisy silhouette centroid) gave a 430 px image displacement between t=1 and t=2, which solves to f ≈ 3800 px (confirmed independently by per-frame torso pixel speeds → 3820/3983 px, and by the apparent-size ratio 0.82–0.86 matching the depth ratio 0.824).
- **Body length**: nose-to-tail-tip measured on frame 0, where the body/tail are least foreshortened (646 px), at z₀ = 4.34 m (from the wingspan ratio to the known-depth frame). Same-depth back-projection gives 0.72 m; a horizontal-body 3D reconstruction gives 0.70–0.74 m for a plausible 30–40° camera pitch. Other frames give only 0.44–0.53 m because the tail hangs toward the camera there.
