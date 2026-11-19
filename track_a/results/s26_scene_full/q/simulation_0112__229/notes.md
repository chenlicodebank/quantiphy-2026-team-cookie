# q_229 – wheel diameter (m); prior: car speed 6.66 m/s

## Time base
File fps 24.007, question fps 24.0 — they differ by 0.03 %, so it makes no practical difference. The car moves uniformly
(no acceleration), so the per-frame speed is simply 6.66 / 24.007 = 0.2774 m/frame.

## Scale (from the prior)
- I checked the near-side hub track in scene/tracks/car.csv: x = -148.14 + 28.227·frame px, rms 0.65 px. A spot check
  from the raw front hub gives 334.5 → 644.5 over frames 13-24 = 28.18 px/frame.
- The tyre and the hub are both in the near-side wheel plane, so the depth cancels. The far-side wheels sit at about
  1.09× the depth, but that does not affect this measurement.
- Scale = 0.2774 / 28.227 = 0.009828 m/px at the near-side wheel plane.

## Tyre pixel diameter
- **Hub-aligned stack (wheel2.py, wheel4.py):** I averaged frames 14-34 aligned on each hub. The bottom edge is at
  r ≈ 33.5 px, which matches the deck top at y 539.5 against hub y 505.5. The diagonal edges are at r ≈ 34-35 px.
- **Per-frame columns (wheel5.py):** the rear tyre runs from y ≈ 471.5 (top) to about 539 (bottom), which gives
  about 67.5 px.
- **Overlay check (zoom.py, frames/zoom_*.png):**
  - Rear tyre: a circle of radius 33.5 px fits the outline closely, and radius 35 is slightly too big. Its horizontal
    extent is about 68 px.
  - Front tyre: horizontal extent is about 67 px. Its vertical extent is 64-67 px, but the top is partly hidden in the
    dark wheel-arch shadow.
- **Adopted value:** D = 67.5 ± 1 px.

## Answer
D = 67.5 × 0.009828 = 0.663 m.

## Second-route check
The wheelbase is 232 px, which gives 232 × 0.009828 = 2.28 m. The real Porsche 930 wheelbase is 2.27 m, so the scale is
consistent. The car's length is about 4.2-4.3 m, also plausible. The real tyre of this car is about 0.63 m. The model's
tyre/wheelbase ratio of 0.29 is slightly larger than the real car's, so I kept the measured value.

## Confidence
The pixel diameter is uncertain by about ±1.5 %, and the scale by under 1 %. I expect the error to be within about 3 %.
