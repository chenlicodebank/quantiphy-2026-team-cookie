# q_1062 — crow body length (m)

File fps = question fps = 24, so there is no time-base issue.

## Scale
- Prior: gravity of the falling "nest" (the black fuzzy object; depth 17.26 m). A parabola fit to its image fall
  (fit_fall.py, frames 28-49) gives about 1100-1250 px/s^2, so f = a_px*Z/g ≈ 2100 px.
- That f makes the standard objects about 2.7x too big: the door (195 px at ~60 m) would be 5.6 m, the barrels
  (90 px) 2.6 m, the cart wheel (172 px at 33 m) 2.7 m, the nest 1 m across, and the crow's wingspan 2.5-3 m. So the
  fall in the clip is slower than real gravity (it looks keyframed or damped) and gives no usable scale.
- Scale taken from standard objects instead: door 2.0 m / barrel 0.9 m at the house front (~60 m; house origin is
  63.6 m) gives f ≈ 5900. The cart wheel (~1.0-1.2 m) gives 4700-5700. I used f ≈ 5850 (HFOV ≈ 19 deg). At this f
  the nest is 0.37 m across and the camera height is about 0.7 m (ground-plane check: horizon near v≈1300).

## Bird
- Crow depth: 46.65 m at t=0 and 43.97 m at t=1. Its image x goes 1030→1220 px. That gives ΔX≈1.4 m against
  ΔZ≈-2.7 m in 1 s, so it flies about 60 deg out of the image plane toward the camera. Its body axis is strongly
  foreshortened and beak to tail cannot be measured directly. I checked the zoomed crops (crowcrops*.py, frames/).
- In wings-level frames (24, 41, 58: thin horizontal silhouette) the x-extent is 127/138/146 px at d≈44.0/42.1/40.5,
  which is 0.96/0.99/1.01 m projected. These agree across depths, which supports f and the depth trend. Correcting
  for the ~27 deg tilt of the wing axis gives a wingspan of ≈1.06-1.12 m, a real-sized large crow.
- Body length ≈ 0.45-0.5 x wingspan for crows/ravens, so about 0.50-0.56 m. Answer 0.52 m.

## Confidence
Low to moderate. The body length is inferred from the measured wingspan plus crow proportions, not measured beak to
tail, because of the viewing angle. The scale rests on standard objects, not on the gravity prior (with the gravity
scale the answer would be about 2.7x larger, ≈1.4 m).
