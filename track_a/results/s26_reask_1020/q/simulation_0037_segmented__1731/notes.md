# q1731 — length of the rock (m)

File fps = question fps = 24.

## Scale (from the prior)
- I tracked the person in `measure.py` (mask = RGB deficit > 15, hip x = mean mask x in the 40–60 % height band). A linear fit gives 41.34 px/s, walking right in side view.
- Assuming the walk is purely lateral: 1.3 m/s / 41.34 px/s = 0.03145 m/px at the person's depth of 122.86 m. That gives f ≈ 3907 px (horizontal FOV ≈ 15.8°).
- Check: the person's median mask height is 62 px, which gives 1.95 m. That is plausible, though tall.
- The given distances are constant (122.857 / 122.859 m). This matches a static character origin, so the person's depth is taken as about 122.9 m.

## Rock
- The rock's mask bbox at frame 0 is x 13–715 (702 px) and y 594–735.
- Its bottom (ground) edge runs from y≈707 at the left end to y≈733 at the right tip. The person's feet are at y≈750, so the left end is farther away than the right tip.
- I computed ground depths with a pinhole model and a camera pitch θ, fixing the camera height H with the person's feet at 122.9 m:
  - θ = 5° (H ≈ 17 m): left end D ≈ 133 m, right tip D ≈ 126.5 m. Lateral X runs from −17.9 to +5.7 m, so the extent is about 23.6 m; the depth extent is about 6.5 m.
  - θ = 10°: about 23.0 m. θ = 0° (horizontal camera, extreme case): about 26.6 m.
  - With no depth correction (a single scale): 702 px × 0.03145 = 22.1 m.
- Answer: **23.5 m**, taking the lateral (long) horizontal extent.

## Confidence
Moderate. The camera pitch and height are unknown, and the rock's depth comes only from its ground-edge rows. If the person-height scale (1.8 m) were used instead, the answer would be about 8 % smaller.
