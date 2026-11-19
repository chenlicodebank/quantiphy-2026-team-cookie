# q_151 — length of the plane (simulation_0092, 2D)

fps 24 = question_fps (no re-timing). 2D side-view render, static camera; plane (Air China narrow-body) and car
(Cybertruck-like) both move right->left. Prior: car length = 5.67 m -> one metres-per-pixel scale (2D convention).

Measurement (`measure_len.py`): median background, |RGB diff| > 12 (captures the faint grey nose; >25 misses ~13 px of
it), 3x3 opening, components >= 30 px, plane = rows < 590, car = rows >= 590; bbox width = length.
* Plane fully in frame 12-30: 876 (frame 12, right edge, perspective) -> 857 px constant at frames 21-30 (centre x 436-949).
* Car: 128 px minimum (frames 33-36, image centre), 128-130 px at x ~ 780-1000 (same region as plane frames 21-30).
Reproduces scene/ record exactly.

Scale = 5.67 / 128 = 0.04430 m/px -> plane = 857 x 0.04430 = 37.96 m.
Second route: car measured at the same image x as the plane (frames 40/45, 128-130 px) -> 37.4-38.0 m.
Sanity: A320 / C919-class airliners are 37.6-38.9 m long — consistent.
Confidence: high (~±2%).
