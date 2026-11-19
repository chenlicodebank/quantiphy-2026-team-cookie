2D static-camera clip. Scale from the prior (woman's height 1.63 m = head-to-toe body length ~700 px on SAM 3 masks/zoomed frames) = 0.00233 m/px. SAM 3 whole-swimmer track over frames 0-125 (t=frame/24, 5.20 s) gives a mild deceleration: quadratic fit ax=-7.6 px/s^2, and a quadratic+stroke-sinusoid fit -7.0 to -7.7 px/s^2; scalar-speed-slope route -4.3 to -7.6 px/s^2; independent head-reference fit -5.0 px/s^2. Adopted 7.0 px/s^2 -> 0.0163 m/s^2, reported 0.017 m/s^2.

Final message:
I measured the swimmer's deceleration in this static aerial 2D clip.

**Method:**
- **Scale:** The prior (woman's height = 1.63 m) corresponds to her head-to-toe body length in the image. Measured on SAM 3 masks and gridded zoomed frames across the clip: ~600–745 px (median ~670, max ~745; full extent including the extended arm 711–771 px). Adopted 700 px → **0.00233 m/px**.
- **Motion:** SAM 3 whole-swimmer track (82 samples, rms 12 px) over frames 0–125 (5.20 s at question_fps 24). Quadratic fit gives ax = −7.6 px/s²; a quadratic + stroke-cycle sinusoid fit gives −7.0 to −7.7 px/s²; the scalar-speed-slope route gives −4.3 to −7.6 px/s²; an independent head-reference fit gives −5.0 px/s². All routes agree on a mild deceleration.
- **Answer:** 7.0 px/s² × 0.00233 m/px ≈ **0.017 m/s²** (magnitude of the deceleration).

Notes written to `notes.md`; confidence moderate (scale good to ~8%, acceleration small and noisy, routes spanning 0.012–0.019 m/s²).
