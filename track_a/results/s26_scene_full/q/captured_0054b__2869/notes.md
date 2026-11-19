# q_2869: orange ball (basketball) diameter, cm

The file and the question both run at 24 fps. The orange ball is the "basketball" in scene/. It rolls up-left, away from the camera, from frame 10 on.

## Method (lab method card)
- f = 0.5959 × 1280 = 762.8 px, principal point (640, 360).
- `measure.py` fits an HSV orange mask, takes its convex hull and fits an ellipse and a circle for frames 10–30. The fit overlay at frame 12 (`frames/fit12.png`) traces the ball outline well.
- Frame 12 (t = 0.5 s, depth 2.24 m): minor axis 76.1 px, bbox 74 × 78, equal-area diameter 76.9. By eye the overlay is about 75 px wide. The smooth size trend over frames 13–17 gives about 74.5–75 at frame 12. I used 75.5 px.
- Diameter = 2.24 × 75.5 / 762.8 = **0.222 m**. A tangential off-axis correction (f_eff = sqrt(f² + ρ²)) gives 0.216 m.
- Answer: **22.0 cm**.

## Checks / caveats
- The depth at t = 1.0 s (1.81 m) cannot be right for this ball. At frame 24 the ball measures 62 px, which would give a 14.8 cm diameter. The ball also shrinks on screen from 75 to 62 px between t = 0.5 and 1.0 s, so it is moving away: its distance grows by about 19% rather than falling. I did not use that value.
- The other depths given at t = 1.0 s check out. The white ball (1.235 m, about 41 px, blurred) gives 6.6 cm and the yellow/green ball (1.331 m, about 42 px) gives 7.3 cm. Both are plausible small balls, so the camera model holds.
- Velocity-prior route: I built the 3D trajectory in units of D from the apparent sizes and matched it to 2.21 m/s at frame 12. The result swings with the smoothing window (0.06–0.27 m), because frame 11→12 is a skipped camera capture and frames 10–11 are occluded by the hand. The steady chords give D ≈ 0.21 (frames 12–13) and 0.27 (frames 12–16), which roughly brackets 0.22. This route is too noisy to use as the answer.
- Confidence: moderate-high, about ±5%. A real basketball would be 22–24 cm.
