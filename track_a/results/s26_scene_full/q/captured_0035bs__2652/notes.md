# q_2652 — soccer ball displacement 0.4 s → 0.9 s (cm)

File fps = question_fps = 24. t=0.4 → frame 10 (ball at rest at the kicker's foot), t=0.9 → frame 22 (in flight).
Lab card: f = 763 px, principal point (640, 360).

## Measurements (scene/ track, circle overlays checked on frames 10 and 22 — the fits match the ball outline)
- Frame 10: centre ≈ (437, 682) (mean of rest frames 6-10), radius 37.8 px (mean of rest frames 0-10).
- Frame 22: centre ≈ (615, 485) (mean of 21-23), radius 30.3 px (mean of 21-23); depth given 2.477 m.
- Depth at frame 10 is not given: from apparent size, d10 = 2.477 × 30.3/37.8 = 1.985 m
  (same as soccer diameter D = 2.477×60.6/763 = 19.7 cm → d10 = 763·D/75.7).
- Back-projection d·r/|r| at both frames → displacement 84.9 cm.

## Checks
- Using the 5-frame median radius at frame 10 (37.25 px): d10 = 2.016 m → 83.6 cm.
- Using the t=1.4 soccer depth 2.602 m with radius ~29.6 px at frame 34 → D ≈ 20.2 cm → d10 ≈ 2.02 m → ~83.6 cm.
- Basketball sanity: at frame 22 radius 30.8 px vs 23.2 cm at 2.778 m predicts 31.9 px (3% off) — focal consistent.
- depth_info's second t=1.4 line is labelled soccer too (2.373 m); likely the basketball, not used.

Answer: 84.5 cm (range 83.5-85). Confidence: moderate-good (depth at 0.4 s inferred from size, ±2%).
