# q172 — length of the plane (m)

2D simulation, 24 fps (file fps = question_fps = 24). Prior: car acceleration = 10 m/s^2 → scale from the car's pixel acceleration.

## Method (measure.py)
- Background = frame 40 with the car region patched from frame 0. Mask = |frame - bg| > 18, then a 3x3 opening.
  (My first run patched the wrong region; I fixed it. The scene/ record is consistent with the corrected run.)
- Car x position per frame (bbox x0, x1, bbox mid, mask centroid, intensity-weighted centroid) fitted with a quadratic:
  a = 0.3494 – 0.3527 px/frame^2 for every reference point and every start frame (1, 2 or 4). Centroid fits:
  0.3502–0.3506, rms 0.1 px. A rest-start model gives 0.3507–0.3512. Adopted value: a = 0.3505 px/frame^2
  = 201.9 px/s^2.
- Scale = 10 / 201.9 = 0.04953 m/px.
- Plane length (tail-plane tip to nose, bbox width in frames 0–10 while fully visible): 750 px (749–753; frames 2–10
  are all 750–751, and frames 0/1 read 753). Using 750.5 px gives **37.2 m**.

## Checks
- Car length: 113.5 px × 0.04953 = 5.62 m, which matches a Cybertruck-style pickup (about 5.7 m), so the scale is realistic.
- Plane: 37.2 m matches an A320-class airliner (37.6 m). Plane height: 227 px → 11.2 m (A320 is about 11.8 m).
- The plane's own speed of 50.5 px/frame works out to 60 m/s. That speed is plausible for a takeoff or landing roll.

Confidence: high. The scale is uncertain by about ±0.5 % and the pixel length by about ±0.3 %.
