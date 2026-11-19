# q_1921 — width of the truck (m)

The prior says the box falls at 9.8 m/s² before 0.6 s. This is a 2D clip, and the camera looks straight at the rear of the truck. The file rate and question_fps are both 120.

## Scale (fit.py, steps.py)
- I used the box front-face top edge from scene/tracks/box.csv. The box is free-falling from about frame 5 until it lands at about frame 61.
- The per-frame steps are uneven because the simulation baked the motion in irregular steps, so I fit a quadratic over the whole fall rather than differencing frames.
  - Piecewise fit (box held still, then constant acceleration) over frames 0–60: a = 2047.5 px/s².
  - Polynomial fits over different windows gave 2012 to 2070 px/s² (5–58, 5–60, 10–60, 4–55, 15–60). The 5–40 window gave 2160.
  - Endpoint check: the box drops 253 px in about 0.495 s, which gives a ≈ 2065 px/s².
- Scale = 9.8 / 2047.5 = 0.004786 m/px.

## Truck width
- The truck's rear body spans x 661–1227, which is 566 px. I confirmed this on frame 120 with a grid; no mirrors are visible.
- Width = 566 × 0.004786 = 2.71 m. This is plausible for a box truck (typically about 2.5 m wide).
- Check: the box face is 281 px wide, which works out to 1.34 m.

## Caveat
The box rests on the roof a little behind the truck's rear face. That depth difference could make the truck slightly narrower than this estimate, by a few percent. I could not measure it, so no correction was applied.

Confidence: moderate, about ±5%.
