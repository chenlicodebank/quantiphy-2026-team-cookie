# q 3234 – ball velocity at 2.20 s

- Clip: top-down hand-held view of a gym floor; a basketball rolls right→left (frames 49–72). File fps = question_fps = 30, so t=2.20 s → frame 66.
- Prior (gravity 9.8 m/s²) describes no motion shown in the clip: the ball rolls on the floor with no fall or bounce, and its apparent diameter stays constant. So the scale comes from the regulation basketball instead: diameter 0.24 m = 256 px (median vertical, blur-free extent over frames 53–69) → 0.000938 m/px.
- Pixel track: scene/tracks/ball.csv cx_stab/cy_stab (camera-drift-removed). I checked the frame at 2.2 s by eye; the ball is fully in view with centre ≈ (481, 440).
- Velocity at frame 66 (script vel.py): forward difference 2.49 m/s, backward 2.45, central 2.47; a linear fit over frames 62–69 gives 2.50, 60–69 gives 2.51, 53–69 gives 2.54. The ball slows slightly.
- Answer 2.49 m/s.
- Cross-check of the scale: the court line is ≈50 px wide, and a standard line is 5.08 cm, which gives 0.00102 m/px at floor level. The ball's centre plane is 0.12 m higher, so it should look ~8% larger. That matches a camera height of ~1.6 m, which is plausible, so the two scales agree. Using the floor scale would give ~2.7 m/s.
- Confidence: moderate (±5–8%). The main uncertainty is the ball-size scale.
