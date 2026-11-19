2D scene, one m/px scale from the prior: the box slides down the 29-deg belt after landing at t~0.4 s; background-subtraction silhouette centroid (validated against a central-symmetry search, <=1 px) fitted over frames 13-29 gives a = 728 px/s^2 and v(0.75 s) = 586 px/s, v(1.5 s) = 1133 px/s. Scale = 2.338/728 = 0.003212 m/px (box 0.90 x 0.61 m, mu=0.30 on the incline - both plausible). Speed(1.5 s) = 1133 x 0.003212 = 3.64 m/s. Second route: sub-pixel template tracking of face patches (a=600 px/s^2, v(36)=1073 px/s) corrected for the measured rotation bias of the face point (+1.8 px/frame decaying to 0) gives a~710 and v(36)~1116 px/s, consistent.

Final message:
**Answer: 3.64 m/s** (question 438).

Method summary:
- **Scale**: 2D scene → one metres-per-pixel factor from the prior. The box lands on the belt at t≈0.4 s and then slides at constant acceleration; the sliding acceleration measured in pixels is 728 px/s², so scale = 2.338/728 = 0.003212 m/px. This makes the carton 0.90 × 0.61 m and the incline friction μ = 0.30 — both plausible.
- **Motion**: background-subtraction silhouette centroid (verified to be the projected box centre by a central-symmetry search, ≤1 px) fitted quadratically over the clean unoccluded frames 13–29: a = 728 px/s², v(0.75 s) = 586 px/s, v(1.5 s) = 1133 px/s.
- **Second route**: sub-pixel template tracking of face patches, corrected for the measured rotation bias of the face point, gives a ≈ 710 px/s² and v(36) ≈ 1116 px/s — consistent.
- Speed at t = 1.5 s (frame 36) = 1133 × 0.003212 ≈ **3.64 m/s**.
