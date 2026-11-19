# Q617 — height of the floor mirror (prior: black cat speed 0.94 m/s)

fps 24 = question_fps, so no retiming.

## Measurements
- Cat speed: 17.73 px/frame (scene record matched track; nose by eye 529→1399 over 49 frames = 17.76). Steady walk,
  constant depth. Scale at the cat: s_cat = 0.94 / (17.73·24) = 0.002209 m/px.
- Camera is level and faces the wall squarely: the TV screen edges are exactly vertical (x 815/1211 at every row) and
  horizontal (y 530/756 at every column) (`edges.py`). So the horizon is at the image centre, y = 540.
- The cat's paws meet the floor at y ≈ 1012–1019, giving y ≈ 1016 for the mid-plane. Camera height:
  h = (1016−540)·s_cat = 1.052 m.
- Mirror (`edges.py`, `mirror_w.py`): top of frame y = 388, bottom on the floor y = 967 (579 px). It leans on the
  wall: outer width is 236 px at the top and 249 px at the bottom, and the centre-offset ratio is 1.031. So
  Z_top/Z_bottom ≈ 1.04.
- At the mirror base, m/px = h/(967−540). Height = h + (540−388)·(h/427)·1.04 = **1.44 m** (1.426–1.446 m over the
  lean range).

## Checks
- At this geometry the TV is ≈1.0 m wide and the stand top is ≈0.49 m high, both plausible.
- A naive single 2D scale would give 579·s_cat = 1.28 m. That ignores the fact that the mirror stands against the
  wall, ~12% farther away than the cat (clear floor perspective: the floor line is at 967 for the wall and 1016 for
  the cat). I rejected it.

Confidence: moderate-high (±3–4%). The main uncertainties are the cat's ground line and the assumption that the
horizon sits at the image centre.
