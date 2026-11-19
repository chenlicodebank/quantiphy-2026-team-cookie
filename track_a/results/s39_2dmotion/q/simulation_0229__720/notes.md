# Q720: paper airplane speed at t = 1 s (prior: chalkboard length = 5 m)

The video is 2D. The camera is static. The file rate and question_fps are both 24, so t = 1 s is frame 24.
Speed = |p(24) − p(23)| × 24 × (m/px).

## Scale
- Chalkboard length, outer wooden frame included (the board object's full extent): x = 320 → 1693, so **1373 px**.
  - Found from background-median gradient profiles at rows 330, 360 and 420 (`measure.py`).
  - The scene record says 1372.
- SAM 3 "chalkboard" mask on frame 24: box x 325–1690, 1365 px, 0.6% shorter.
  - The overlay shows the mask's left side eaten by the sunbeam, which explains the gap. It is within 3%.
- Scale = 5 / 1373 = 0.003642 m/px.
- Alternative reading (green writing surface only, 1328 px): it gives answers about 3.4% higher (~6.25 m/s). Not used.

## Plane position (origin proxy = bbox centre, i.e. nose–tail midpoint)
I segmented the plane myself against a background median (`measure.py`, frames 20–28).

| Route | f23 → f24 (px) |
|---|---|
| My bbox centres | 69.5 |
| Scene ref point (`tracks/paper_airplane.csv`) | 69.0 |
| SAM 3 box centres (f23 and f24 masks, length 133–139 px, consistent) | 69.4 |
| Quadratic fit of my centres, frames 20–28 | 68.9 |

- Mask centroids jump around (71.3 px) because of the rear-wing bias, so I did not use them.
- All the box-centre and midpoint routes agree within 1%.

## Answer
69.2 px/frame × 24 × 0.003642 = **6.05 m/s**. The routes give 6.02–6.08.

Confidence: high for the pixel speed. The main uncertainty is the board-length convention (outer frame vs green
surface, 3.4%).
