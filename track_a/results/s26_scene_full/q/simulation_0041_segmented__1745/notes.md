# q_1745 — length of the boat (m); prior: person height 1.75 m; no depth_info

Video: 1080x1080, 24 fps (file fps = question_fps = 24, so no re-timing). Segmented Blender render. The camera is fixed
and looks steeply down: the boat deck and the top of the person's head are clearly visible. So the plain 2D ratio
(46.5 px person, 360 px boat -> 13.5 m) is wrong, because the person's height is foreshortened and the boat's length lies
almost flat on the ground.

## Measurements (scripts in this folder)
- `mastfit3.py`, `mastlean_fit.py`: I tracked the white mast pole in frames 2–62. Its image lean changes linearly
  as the boat moves left: d(dx/dy)/dx = -2.13e-4 (bootstrap ±5 %). That puts the nadir 4700 px below the mast, so
  f·cot(theta) ≈ 5030 px. The person's mean lean (~2.5°, top-left, from `lean.py`) agrees roughly (~4000 px).
- `footslide.py`: the person's planted toe stays fixed in the image (rows 429, 454.5, 479, 506), so the feet do not
  slide. One step = 25.6 px in the image (17 frames). The minimum image extent at mid-stance is 38.6 px (soft-alpha edges).
- `person.py`: the person's width at the shoulders, arms included, is about 19–20 px.
- `boatscale2/3.py`, `boatvel.py`: the boat's area shrinks by about 1 % over 80 px of upward motion. This gives a
  horizon distance of roughly 4000–11000 px, depending on how much of the boat counts as deck versus vertical faces,
  so it constrains theta only weakly (about 49–55°).
- The boat's x-extent at frame 0 is 338 px (bow tip x = 347 to stern x = 683). The image motion direction
  (-396, -111) px gives the ground heading.

## Model (`solve.py`)
- Pinhole camera with pitch theta and f = 5030·tan(theta).
- Person extent: k_p·(1.64 cos + 0.105 + 0.17 sin) at the person's ray elevation, where 1.64 m is the head-centre
  height, 0.105 m the head radius and 0.17 m how far the toe sits ahead of the head.
- Scale ratio from the person to the boat: sin(ray elevation at boat) / sin(ray elevation at person), about 1.04.
- L = x-extent / (k_b·cos psi).

| theta | 52° | 56° | 58° | 60° | 63° |
|---|---|---|---|---|---|
| L (m) | 11.0 | 10.4 | 10.0 | 9.65 | 9.1 |

The evidence for theta conflicts:
- Boat perspective and the stated FOV range (≥ about 8°, so f ≤ 7720 and theta ≤ 57°) favour 52–57°.
- The person's anatomy favours a steeper view. A natural step of 0.75–0.8 m and a width of about 0.5 m give 61–63°;
  at 52° the step would be 1.08 m and the width 0.62 m.

I chose theta ≈ 58° (FOV about 7.7°, step 0.89 m, width 0.56 m), which gives **L ≈ 10.0 m**.

## Check
- The full range of plausible theta gives 9.1–11.0 m (±10 %).
- Boat speed comes out at about 4.5 m/s and the boat at about 10 m long, both plausible for a fishing boat.

Confidence: moderate (±10 %). The main uncertainty is the camera pitch.
