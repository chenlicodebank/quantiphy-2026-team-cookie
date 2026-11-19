# q739 – ceiling height of the room (m); prior: black cat speed = 0.714 m/s

fps = question_fps = 24 (no re-timing issue).

## Measurements (scripts in this folder)
- `measure.py`: wall/ceiling junction y = 172.6 px, wall/floor junction y = 951.4 px (sub-pixel, 4 wall column
  bands x 960–1310, agree within ±0.4 px) -> wall (= room) height on the front wall = **778.8 px**.
- Cat pixel speed (scene/tracks/cat.csv, checked): linear fit of torso_cx 8.91 px/frame (cx_dark/cx_mask 8.99,
  end-to-end 8.85–9.02); steady walk -> 8.91 px/frame = 213.9 px/s.
  Cat-plane scale = 0.714 / 213.9 = 0.003339 m/px. Planar (no depth correction) answer: 778.8 x 0.003339 = 2.60 m.
- `vp.py`: vanishing point of the receding ceiling-tile seams (18 Hough lines, median residual 1 px) =
  (959, 540) = image centre -> camera optical axis is horizontal and perpendicular to the wall; horizon y = 540.
- Depth of the cat vs the wall (floor/desk-plane geometry, y - 540 ∝ height offset / Z):
  desk top front edge y 763.5, rear edge y 736, cat paw contact (midline between near/far paws) y ≈ 739.5,
  floor at the desk front (shadow edge under the desk) y ≈ 1028, wall floor line 951.4.
  Zc/Zd = 223.5/199.5 = 1.120; Zw/Zd = 488/411.4 = 1.187 (floor route); desk rear Zr/Zd = 1.140 (lower bound for Zw).
  -> Zw/Zc = 1.06 (floor route) or ≥ 1.018 (desk against wall). Used 1.054.
- Answer = 2.60 m x 1.054 ≈ **2.74 m**.

## Checks
- Self-consistency of desk geometry: desk rear (1.140 Zd) lies just in front of the wall (1.187 Zd): plausible.
- Range from the depth uncertainty: 2.65–2.76 m; planar-only 2.60 m. Plausible classroom ceiling.
## Confidence
Moderate: pixel measurements are tight (<0.5 %); main uncertainty is the cat-to-wall depth ratio (±2–3 %).
