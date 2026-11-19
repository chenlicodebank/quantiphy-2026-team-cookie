# q1662 — height of the central sculpture (excluding pedestal)

File fps = question_fps = 33. Pinhole camera, principal point assumed at image centre (540,540), camera untilted
(consistent with floor geometry: painting base y 686 at ~11 m, man's feet y 786 at ~6.4 m give the same camera height ~1.73 m).

## Sculpture pixel height (measure.py, frame 0, static)
Top tip row 391; bottom of the bowl / contact shadow on the pedestal top at row ~693 (darkest point of the column at x=489).
Height = 302 px (±2), matches scene/ record (bbox 376,391-602,693).

## Focal length (two routes)
- Route A (depths only): man's pelvis (882.9,648.3) at t=0 with d=6.84 m and (688.6,649.8) at t=1 s (frame 33) with
  d=6.49 m; his apparent height is the same at both (259 vs 258 px, same gait phase), so equal camera-Z -> f = 908 px, Z = 6.36 m.
- Route B (prior 1.87 m): walking bbox height 258-266 px (max 266 with legs together, frame 7; frames 19-26 are
  contaminated by the painting top edge). With hp=266 -> f = 904; hp=262 -> 889. Walking max height is slightly below
  rest height, so f ~ 905-913. Agrees with route A.
- Adopted f = 907 px (HFOV ~ 61 deg).

## Answer
Sculpture origin assumed at its bbox centre (489,542): Z = 5.085/|r| = 5.077 m.
Height = 5.077 * 302 / 907 = 1.69 m.
Alternative: origin at sculpture base (489,693) -> Z = 5.006 -> 1.667 m (1.4% lower). f range 889-913 gives 1.68-1.72.
Answer 1.69 m. Confidence: moderate-high (~3% uncertainty).
