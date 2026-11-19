# q3213 – height of the person (m); prior g = 9.8 m/s^2

Internet video, 30 fps (file = question_fps, no re-timing). The camera is almost static (drift < 1 px/frame).

## Scale from gravity (fit.py)
Quadratic fits of the ball centre y(t) (scene/tracks/ball.csv) over the free flights:
- flight 2, frames 116–143: 3531 px/s^2 raw, 3558 px/s^2 with drift removed (rms 0.3–0.45 px); 118–141: 3540 / 3565
- flight 1, frames 81–113: 3539 raw, 3546 with drift removed (rms ~2 px; the horizontal speed is not constant, so this fit is less clean)
- Adopted g_px ≈ 3548 px/s^2, which gives a scale of 9.8/3548 = 2.762e-3 m/px.
- Sanity check: the in-flight ball diameter of 85 px × scale = 0.235 m. A real basketball is about 0.24 m, so this agrees.

## Person pixel height (height.py, captop.py, sole.py), standing frames 10–50
- The record's height_px of 620 is too small. Its threshold-45 mask misses the low-contrast beige cap top.
- Column intensity profiles at frame 30 put the cap top at y ≈ 423 (wall 115,113,111 changes to cap at about 422–424). The sole/floor contact line is at y ≈ 1058–1061, with the floor starting at about 1062.
- A background difference against the warped frame 169 at threshold 30 gives 631–636 px over frames 10–50.
- Adopted height ≈ 636 px (cap top to shoe sole).

## Answer
636 × 9.8 / 3548 = 1.757 m, giving **1.76 m**.
Second route: using flight 2 alone (3531–3565) gives 1.75–1.77 m. Using the record's 620 px instead would give 1.71 m, but the profiles show that value cuts off the cap.
Confidence: moderate-high (about ±3%).
