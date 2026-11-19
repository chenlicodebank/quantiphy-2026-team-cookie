# Q291 — width of the red car (m)

Prior: bike speed = 24 m/s. No depth_info. Top-down, static camera, 2D treatment (one m/px scale). question_fps = file fps = 24.

## Scale from the prior
- Cyclist pixel speed: scene record gives 31.64 px/frame (chained NCC, frames 2–53). Independent check
  (`cyc_speed2.py`, RGB template from frame 36 matched in frames 16, 26, 46, 52): steps 31.68, 31.97, 31.77, 31.49;
  line fit 31.78 px/frame. Used 31.7 px/frame = 760.8 px/s.
- Scale = 24 / 760.8 = 0.03155 m/px.

## Red car width
- `measure_red.py`, frame 41: red-body mask spans y 716–801; column profiles at x=60 and 230 show the body
  edges at about y 715 and 801.5 → body width ≈ 86 px (95 px incl. mirrors per scene record).
- Width = 86 × 0.03155 = 2.71 m (incl. mirrors it would be 3.0 m; answered body width, wheel-to-wheel reading).

## Plausibility
24 m/s is unrealistic for a bicycle, so the scene is evidently scaled: the same scale gives bike length 85 px →
2.68 m and red car length 244 px → 7.7 m, all ~1.5–1.6x real sizes, consistent with each other. As the prior is
exact and unrealistic, the prior scale is kept. (With realistic scale the car width would be ~1.8 m.)

Confidence: moderate-high under the prior-scale convention (±3%).
