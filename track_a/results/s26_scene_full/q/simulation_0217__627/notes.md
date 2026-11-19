# q_627 — width of the TV stand (m)

**Object.** The TV stand is the long, dark wooden console along the top wall, at x ≈ 711–1265 and y ≈ 168–293 px. The
vase sits on it at the left end and the lamp at the right end. Width means the front-to-back depth, which is the image
y extent in this top-down view. Both fps values are 24, so there is no time-base issue.

**Scale (2D, from the prior).** The black cat walks at a steady speed in +x along y ≈ 360 (`scene/tracks/black_animal.csv`, checked in `measure.py`):
- front edge: 10.98 px/frame (net change over 49 frames)
- centroid: 10.92 px/frame
- body: 11.01 px/frame
- linear fits: 10.94–10.98 px/frame
- the first and second halves agree to within 2 %.

I use 10.95 px/frame = 262.8 px/s. Setting 0.94 m/s equal to that gives 0.003577 m/px at the cat's height.

**Stand edges** (`measure.py`, column profiles every 20 px from x = 820 to 1080, frames 0, 24 and 49, all identical):
- back edge of the top surface: y = 168.5
- front edge of the top surface: y = 282.5, so the top surface is **114 px** deep
- a lighter band from 282.5 to 292.5 (10 px) is the stand's front vertical face. It shows because of perspective: the
  stand is above the image centre, so its face toward the centre is visible. The full visible footprint is 124 px.

**Perspective correction.** Assume the principal point is at y = 540. The face band gives Zf/(Zf−H) = 257.5/247.5 = 1.040,
so H/Zf ≈ 0.039. The top surface is therefore magnified by about 4 % compared with the floor. The cat's origin is at
roughly 0.15 m, which magnifies it by about 1 %. The net correction is about 0.973.
- The leaning A-frame shelf, whose top projects beyond the wall line, gives a similar camera distance (roughly 15–25 m), so the model is consistent.

**Result.**
- corrected: 114 × 0.973 × 0.003577 = **0.397 m**
- no correction, top surface only: 0.408 m
- full footprint including the face band (an overestimate): 0.443 m

Second route: I also took the scale from the cat's centroid speed instead of its front edge (10.92 px/frame), which
gives 0.398 m. The plausibility check also holds: the console length of about 553 px comes to about 1.9 m. That is a
normal TV-stand size.

**Answer: 0.40 m.** Confidence is moderate. The main uncertainty is whether the reference depth matches the top surface
(about 0.40) or a slightly deeper base, which would raise it by at most 0.44.
