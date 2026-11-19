# q_2373: displacement of the white jar, 0.60 s to 0.80 s (cm)

- The "white jar" is the small white cylinder that scene/ calls `white_ball`. The near person throws it underarm.
- question_fps = file fps = 24, so the times map to frames 14 (0.60 s → 14.4) and 19 (0.80 s → 19.2).
  - f14: last frame in the hand (blurred, release at f15). f19: in flight, partly overlapping the yellow fruit.
- Crops (frames/crops.png) confirm that the record's centroids sit on the jar centre.
  - f14: (405.4, 238.1). f19: (480.1, 65.1).
- Camera: f = 0.5959 × 1280 = 763 px, principal point (640, 360).
- Depth: given only at f14 (1.9735 m). The f19 depth has to be estimated.

## Method (fit2.py, fit3.py)
- Fitted a 3D ballistic trajectory to the flight centroids, f15–25 and f15–22.
  - Gravity direction was fixed from the vertical vanishing point of the two people (the near person's slanted
    body axis meets the far person's legs at about (852, 1623); I also tried (800, 1400), (735, 1280) and (852, 2200)).
  - Metric scale comes from D14: the trajectory extrapolated to f14 must have |P| = 1.9735 m.
  - Fit quality: rms about 1.2 px.
- Model depth at f19 is 2.06–2.16 m. The ratio d19/d14 is about 1.08.
- Reference convention: P = unit ray(centroid) × depth, displacement = |P19 − P14| with D14 and the model d19.
  - Result: 46.7–50.4 cm (49.7 cm for the best vanishing point).

## Checks / inconsistencies
- Gravity magnitude:
  - With D14 as the scale, the fitted gravity is 8.0–8.4 m/s².
  - With g fixed at 9.8 and no D14, the depth at f14 would be 2.40 m instead of 1.97.
  - So the two scale cues disagree by about 20%. Possible causes: the f14 hand-held point is not a free-flight
    point, or the focal length is off.
- Sensitivity to that disagreement (fit3.py): I modelled with f = 600–763 px, so that g ≈ 9.8 holds together with
  D14, and then computed the displacement the reference way.
  - d19 stays at 2.07–2.19 m and the displacement at 47–52 cm. The answer is robust to this.
- Combining g = 9.8, D14 and a fixed gravity direction fits worse (rms 2–3.5 px) but still gives 47–58 cm.
- Apparent jar width hardly changes between f15 and f19 (it is inflated by blur), which agrees with a small depth
  change of about 8%.

## Answer
49.5 cm. Confidence: moderate. The main uncertainty is the depth at f19 (±0.07 m → ±3 cm).
