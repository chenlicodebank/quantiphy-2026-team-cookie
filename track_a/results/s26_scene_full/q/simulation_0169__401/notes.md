# Q401 — speed of the astronaut at t = 0.5 s (m/s)

- 2D render, static camera, fps = question_fps = 24 → t = 0.5 s is frame 12. The step that counts is frame 11 → 12.
- Scale from the prior (height 2.2 m): I measured the astronaut's vertical mask extent in code (measure2.py, crop that leaves out the moon
  and stars) on frames 0, 6 and 12. It is 91 px at thresholds 15–40 (89–90 px at stricter thresholds). This
  matches the scene record (bbox height 91, body length along its axis ≈91). The figure is upright here (tilt ≈95–96°).
  Scale = 2.2 / 91 = 0.02418 m/px.
- Pixel speed around frame 12 (ease-in phase, so the speed is increasing smoothly):
  * Route 1: intensity-weighted mask centroid, quadratic/cubic fit over frames 4–20, 6–18 and 8–16, then the fitted step 11→12:
    2.61–2.73 px/frame.
  * Route 2: masked phase correlation between consecutive frames. The raw step at 11→12 is 2.77 px; a quadratic fit
    of the cumulative positions gives 2.69–2.70 px/frame.
  * Scene record centroid raw steps: 2.47 (11) and 2.63 (12); the bbox and centroid steps are noisy, about ±0.5 px.
  * Adopted value: 2.69 px/frame.
- Speed = 2.69 × 24 × 0.02418 ≈ 1.56 m/s.
- Confidence: good (about ±4%). The main uncertainties are the ±1 px height definition and the per-frame noise in the steps.
