Cutter handle centroid tracked on frames 0-13 with camera-drift stabilisation (template matching on the wine glass); per-frame displacement at frame 5 (t=0.2s, question_fps 24) = 37.2 px (backward 37.2, forward 36.5, central 36.8, fit 38.1; scene track 37.35). Scale from the monopoly-money prior cross-checked on standard objects in the same plane (wine glass 20.5 cm tall, Monopoly board 50 cm, pizza 34 cm, houses 1.5 cm) = 0.0351 cm/px, which reproduces 7.5 cm with the $1 bill's 200-214 px horizontal extent. v = 37.2 x 24 x 0.0351 = 31.3 cm/s.

Final message:
I measured the pizza cutter's motion and the scene scale, then answered.

**Method summary**
- **Motion:** tracked the black handle blob (a fixed point on the rigid cutter) on frames 0–13, correcting for camera drift by template-matching a static patch (wine glass). At frame 5 (t = 0.2 s at question_fps 24) the stabilised per-frame displacement is 37.2 px (backward 37.2, forward 36.5, central 36.8, linear fit 38.1; the scene record's smoothed value 37.35 agrees).
- **Scale:** the prior (monopoly money width 7.5 cm) taken literally as the bill's short side gave an implausible scene (68 cm Monopoly board, 13 cm wine-glass bowl), so I cross-checked on standard objects in the same plane — wine glass 20.5 cm tall, Monopoly board 50 cm, Monopoly houses 1.5 cm, pizza ~34 cm — giving 0.0351 cm/px, which reproduces 7.5 cm with the $1 bill's ~200–214 px horizontal extent.
- **Answer:** 37.2 px/frame × 24 fps × 0.0351 cm/px ≈ **31.3 cm/s** (second route via the scene track: 31.5 cm/s).
