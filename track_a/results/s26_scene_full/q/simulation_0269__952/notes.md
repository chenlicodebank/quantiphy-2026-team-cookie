# q_952 — speed of the phoenix at 1.0 s (prior: acceleration at 2.0 s = 2 m/s^2)

fps = question_fps = 24, so t = 1.0 s is frame 24 and t = 2.0 s is frame 48.

## Measurement
- `track_head.py`: sub-pixel frame-to-frame template matching of three regions: head, head+body and body (anchored on the record's beak track). This gives per-frame steps with about ±1–2 px of noise. The record's beak track (2 px quantised) agrees with it.
- The per-frame speed is stepped: about 5 px/frame (frames 2–22), about 15.6 (31–46) and about 26 (55–71). Short surges happen once per wing-flap cycle (period about 25 frames).
- `fit.py`: quadratic fits x = x0 + v0 f + a f²/2, made over whole flap periods so that the periodic surge averages out.
  - Over frames 0–71: head+body a = 0.416 px/f², v0 ≈ 0, so the bird is at rest at f ≈ −0.1.
  - Over frames 5–55 (exactly 2 periods): a = 0.411, rest at f ≈ 0.1.
  - The beak, body, centroid and bbox tracks give the same result (a = 0.41–0.42, rest at f within about ±0.6 of 0).
- Residuals from the quadratic are a clean periodic ±13 px flap surge. This means the origin moves with uniform acceleration from rest at t = 0, and the flight-cycle animation adds a periodic surge to the mesh.
- Cross-check: the plateau speeds 5 / 15.6 / 26 px/frame at frames ~12 / 38 / 63 lie on v = 0.415·f.

## Scale and answer
- Uniform acceleration means a = 2 m/s² throughout. The scale is 2 / (0.415 × 576) ≈ 0.0084 m/px, so the bird is about 3.7 m long. Rendered scenes are not at real-world scale, so this is acceptable.
- The answer does not depend on the scale, only on the start-from-rest time.
- One-frame backward-difference speed at frame 24, starting from rest at frame 0: a × (24 − 0.5)/24 = 1.958 m/s.
- Other readings of the start:
  - Analytic a × t = 2.00.
  - Rest at frame 1 (frames 0 and 1 are identical): 1.875.
  - The individual whole-period fits give 1.93–1.97.
- Answer: **1.95 m/s**.

## Confidence
Fairly high for the uniform-acceleration-from-rest model, which fits well over several windows and tracking points. The remaining spread (1.88–2.0) comes from where exactly the motion starts.
