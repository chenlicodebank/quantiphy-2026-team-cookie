# Q2880 – soccer ball diameter (cm)

Lab clip: 24 fps (file and question_fps are the same), 1280x720, f = 0.5959*1280 = 763 px.
Scale: depth_info gives the soccer ball at t=2.0 s (frame 48) at 3.254 m. Diameter = 3.254 * D_px(48) / 763.

## Measurement
- From frame 27 on, the soccer ball shows only as a faint, untextured SAM2 disc. Method (`discfit.py`):
  - background = per-pixel median of frames more than 12 frames away;
  - |frame - bg| (max over channels), blurred with sigma 1;
  - fit a blurred-disc model (centre, radius, edge sigma, amplitude, offset) by robust least squares near the track position.
- The diameter is the half-maximum edge. Fitted D (px) by frame:
  - 29–35: 63.8, 61.9, 62.0, 61.2, 59.7, 57.8, 56.9
  - 36–41: 57.0, 54.7, 56.6, 53.8, 53.6, 52.5
  - 42–48: 51.6, 52.6, 53.6, 50.0, (46: bad fit), 53.0, 53.9
- The overlays (`overlay.py`, frames/overlay*.png) show that the fitted circles follow the disc edge in frames 41–48.
- Frame 48 estimate:
  - direct mean of frames 44–48 = 52.4 px;
  - 1/D quadratic trend over frames 29/33/37–48 = 52.4–53.3 px. This includes the dropped source frame between 35 and 36.
  - Only a linear-in-time trend fitted to frames 29–41 gives a lower value, about 48–50 px.
- Adopted D48 = 52.5 px, about ±1.5 px.
- Result: 3.254 * 52.5 / 763 = 0.224 m = **22.4 cm** (52–54 px gives 22.2–23.0 cm).

## Checks
- The record's circle_diam is noisy (49–63 px in late frames). It was re-measured here with a model fit.
- Sanity check: a size-5 soccer ball is about 22 cm, which agrees with this result.
- The orange-ball depths look inconsistent with its pixel size: at 0.5 s it is 75.8 px at 2.24 m, at 1.0 s 60.4 px at 1.81 m. The question does not use them, so the answer does not depend on this.

Confidence: moderate-high, within about 5%.
