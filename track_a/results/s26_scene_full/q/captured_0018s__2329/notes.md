# q_2329: distance pineapple toy to soccer ball at 3.0 s (cm)

Video: 49 frames at 24 fps (0 to 2.0 s). question_fps 24, so 3.0 s is frame 72, which is **past the end of the clip**.
The answer therefore relies on extrapolating from frames 36–48. It cannot be checked directly.

Pineapple toy = scene "yellow_fruit", dropped by the near (right) person. Soccer ball is dropped by the far (left) person.
Camera: f = 763 px, (cx, cy) = (640, 360).

## Measurements (scripts: gfit.py, ballpost.py, dist.py, crops.py)
- A camera frame was dropped between file frames 35 and 36. Fitting gravity to the falls confirms it: the ball's rms drops
  from 6.8 to 1.3 px when the extra frame is counted.
- Depth from gravity (a_px = f·g/Z): soccer ball Z = 3.03 (D 3.05; the given value is 2.8), pineapple Z = 2.02 while
  falling, green ball Z = 2.56.
- Floor model with a level camera, using the people's feet and their given depths: camera height H = 0.843 / 0.847 m,
  which agree. The green ball's bounce row (616) matches the floor at its gravity depth.
- Pineapple: first bounce at f36 (bottom row 697, so floor Z ≈ 1.92). It then hops backwards: from f40 to f48 its
  bottom stays at rows 617–631 and its width drops from 30 to 25 px. That puts it on the floor at Z ≈ 2.44
  (centre ≈ (842, 612) px, P = (0.645, 0.804, 2.436) m). I assume it is nearly at rest there by 3.0 s.
- Ball after its bounce: a parabola fit gives the apex at camera frame ~49 and the next landing at ~57–59.
  With restitution e ≈ 0.7 (drop of 279 px, rebound of 139 px), the next landing is at ~70 and the next small hop
  (≈ 36 px high) comes after that. So at frame 72 the ball is near the floor: cy ≈ 535 (range 515–554).
  It drifts horizontally at 2.1 px/frame, which gives x ≈ 601 at frame 72.
  The given D = 2.8 m (which is probably the depth at 3.0 s) is used to back-project the centre:
  B = (-0.139, 0.625, 2.726) m.

## Result
|B − P| = 85.5 cm for the main reading. Sensitivity checks:
- ball row 515–554: 84–88 cm
- ball x drift stops (x = 551): 102 cm
- half the drift (x = 575): 93 cm
- pineapple at its fall depth Z = 2.02: 99 cm
- ball at its gravity depth instead of 2.8: 100 cm

Answer: **88 cm**. This is the main estimate, nudged up because most of the alternatives are larger.
Confidence is low to moderate (about ±15 %), because 3.0 s lies outside the clip.
