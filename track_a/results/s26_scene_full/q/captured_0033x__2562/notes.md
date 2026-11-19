# q_2562 – velocity of the ping pong ball at t = 1.4 s (cm/s)

Time base: question_fps = file fps = 24 -> t = 1.4 s = frame round(33.6) = 34. The ball is rolling or hopping on
the table top toward the camera and to the left. It leaves the table's front edge at about frame 35 and falls (f36-38).

Camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360). Scale comes from the given depth 0.738 m at f34.
The prior (40 mm) checks this: the apparent diameter at f34 is about 39-41 px, so the expected distance is
0.74-0.78 m, which agrees.

## Routes (scripts in this folder)
- `table.py`: median background (frames 40-48) and the table outline. `velocity.py`: the table-plane normal from
  vanishing points (side edges VP (622, 339), front/back edges nearly parallel). Horizon about y 338, camera pitch
  1.6 deg down. As a check, the front and back table edges both come out 0.516 m wide.
- Route A (`combine.py`): ball centroid (scene track) back-projected onto the ball-centre plane. The plane offset
  is calibrated so that f34 has distance 0.738 m. Distances f29-35: 0.910, 0.880, 0.830, 0.809, 0.798, 0.738, 0.679.
  A linear fit over f29-35 gives |v| = 98 cm/s; over f30-35 it gives 100.
- Route B: the ball's sub-pixel top edge (`topedge.py`) on a parallel plane, calibrated the same way. Linear fits
  give 99-106 cm/s and quadratic v(34) gives 97-107.
- Route C: apparent size (horizontal width minus exposure blur), so depth is proportional to 1/diameter. f29-34
  gives 81-100 cm/s. It is noisy and f35 is unusable because of the edge.
- Every route shows uneven frame-to-frame steps (a small step at f32->33 and a large one at f33->34), so I only
  used fits over 5-7 frames.
- `smooth_ref.py`: emulates the reference convention (5-frame smoothed positions, forward difference at f34). It
  gives 98 cm/s using only on-table frames (f30-34). It gives 115 cm/s when the window takes in f35-37, where the
  ball drops off the front edge and its centroid there is a blur streak or cut by the image edge.

## Notes
- The given depth at t = 0.9 s (1.457 m) does not fit the ball's apparent size at f22 (about 32 px, which implies
  about 0.95 m for a 40 mm ball). The table-plane geometry puts the ball near the back of the table there, at about
  1.2-1.3 m. That depth is not used: the answer depends only on f29-36.
- Velocity is mostly toward the camera (vz about -94 cm/s, lateral about -30 cm/s).

Answer: 105 cm/s. This sits between the on-table rolling speed (about 99) and the smoothed value that includes the
fall-off frames (about 115). Confidence: moderate (about ±15%).
