Camera-drift-corrected bowl track: mean per-frame displacement over frames 26-40 (t=1.0-1.6 s at question_fps=25) = 6.982 px/frame -> 174.5 px/s. Scale from the cleanest full fork (SAM mask, 175.0 px = 20.3 cm) = 1.160 mm/px, giving 0.2025 m/s. Independent SAM bowl track agrees after removing the ~0.85 px/frame camera drift (~174 px/s).

Final message:
Answer submitted: **0.2025 m/s** (question 3023).

Method summary:
- **Time base:** question_fps = 25 → t=1.0 s is frame 25, t=1.6 s is frame 40; averaged the per-frame displacements 25→26 … 39→40.
- **Motion:** used the camera-drift-corrected tomato-bowl track (drift ≈ 0.85 px/frame downward, measured by phase correlation and ECC in `scene/`). Mean displacement = 6.982 px/frame → 174.5 px/s. An independent SAM 3 bowl track gave 194.9 px/s raw; subtracting the same drift gives ~174 px/s, confirming the result.
- **Scale:** SAM 3 fork masks inspected; the least-foreshortened full fork (frame 46, lying on the plate) measures 175.0 px for the 20.3 cm prior → 1.160 mm/px. Cross-check: dinner plates then measure ~28.8 cm, plausible; the view is essentially orthographic.
- **Answer:** 174.5 px/s × 1.160 mm/px ≈ **0.202 m/s**.
