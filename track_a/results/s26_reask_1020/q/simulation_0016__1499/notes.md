# q_1499 – width of the bench seat (simulation_0016)

The file runs at 33.004 fps and the question at 33.0 fps. All timing uses frame numbers × 1/33.

## Geometry
- The camera looks straight down (nadir). Floor tiles are evenly spaced over the whole image, so one m/px scale
  holds at floor level. A point at height h has scale s_floor·(1 − h/H).
- **Scale from the prior (person 1.3 m/s).** The footprints from scene/ show the floor point under the walker moving
  3.952 px/frame. That is 130.4 px/s at 33 fps, so s_floor = 1.3/130.4 = 0.00997 m/px.
- **Check against depth_info.** The plinth of the central sculpture is at the image centre, directly below the camera,
  so H − h_plinth = 9.967 m, i.e. H ≈ 10 m. With H/f = 0.00997, f ≈ 1000 px (hFOV ≈ 57°). With these values the
  benches (centres 389 px and 374 px from the centre) give camera-to-origin vertical distances of 9.91 m (left) and
  9.92 m (right) from their given distances of 10.63 m and 10.59 m. Both benches agree, and their origins come out
  about 5 cm above the plinth origin, which makes sense. The speed scale and the static depths are consistent.
- The given human depths (9.24 → 9.14 m) change much less than the visible walk would produce, so the character's
  origin lags the body. I did not use them.
- Side note: with H ≈ 10 m, the head magnification (1.256) puts the head at about 2.0 m, so the person model is
  tall. This does not affect the bench answer.

## Measuring the bench (bench.py, frame 50, intensity profiles across x at 5 rows that avoid the cushion seams)
- Left bench: cushion top runs from x ≈ 532 (thin dark outline) to x ≈ 605.5, i.e. 73.5 px. A dark band at
  606–615 is the inner side face seen in perspective (its lean means it is about 0.2–0.25 m tall), not top surface.
- Right bench: cushion top runs from x ≈ 1300 to x ≈ 1372.5, i.e. 72.5–73 px. Its inner side face is at 1290–1297.
- I used 73 px. The length is 234 px along y, so 73 px is the shorter horizontal extent (the front-to-back depth).
- Converting at the seat-top height (h ≈ 0.25–0.5 m, factor 0.955–0.975):
  73 × 0.00997 × 0.96 ≈ 0.70 m. Range 0.69–0.71 m.

## Second route
Using the depths alone and assuming the plinth and bench origins are at the same height: f ≈ 1041–1048 px, giving
s_floor ≈ 0.0095 and a width of ≈ 0.665 m, about 5 % lower. The combined solution (speed plus depths) is
self-consistent, so I kept 0.70 m.

Answer: **0.70 m**. Confidence: moderate-to-good (±5 %).
