# q_1933: floor mirror height (m)

Prior: black cat speed = 0.94 m/s. 2D side-on render, static camera, 24 fps (file fps = question_fps; no re-timing).

- Cat pixel speed: steady walk, no start/stop. Record: cx 17.64 px/frame, dark_cx 17.83 px/frame. My own
  check (measure.py, centroid of black non-static pixels) gives 17.34 px/frame; it is biased low where the cat
  crosses the console's black base. Adopted 17.6 px/frame = 422 px/s.
- Scale: 0.94 / 422 = 2.225e-3 m/px (one 2D scale, as the convention says).
- Mirror: non-white extent rows 390–967, so 578 px tall. This is the same in frames 0, 25 and 48 and matches the
  record. It is the vertical image extent, which equals the AABB height for a side view (the mirror leans, but that
  does not change the vertical extent).
- Height = 578 × 2.225e-3 = 1.286 m, so the answer is **1.29 m**. Using the different cat-speed measures gives
  1.27–1.30 m.
- Sanity check: cat body length about 260 px = 0.58 m, and TV width 399 px = 0.89 m. Both are plausible.
- Caveat: the mirror's foot (y 967) sits higher than the cat's paws (y 1021), so the mirror may be further from the
  camera. If so, it would be taller than the single-scale figure, perhaps by up to about 10%. The camera's horizon
  is unknown, so this was not corrected, following the 2D single-scale convention.

Confidence: moderate-high under the single-scale convention.
