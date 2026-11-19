# q_599 — length of the wooden bench (m)

Prior: speed of the black cat = 0.94 m/s. 2D top-down scene (the camera looks straight down), fps = question_fps = 24.
(The scene record calls the animal a "dog". It is the only moving object, a small black cat.)

## Scale from the prior
- Cat pixel speed (scene/tracks/dog.csv, checked in measure.py): linear fit slope 10.99–11.00 px/frame for
  nose_x, mask_cx and torso_cx. Mean per-frame dx is 11.02 (nose and mask). Motion is constant (no acceleration).
  This gives 11.0 px/frame × 24 = 264 px/s.
- Scale: 0.94 / 264 = 0.003561 m/px.

## Bench
- Orange-wood colour mask (r−b>50, r>110) at frames 10 and 40, measure.py. The x extent is 244–531/533, so the
  length is 288–290 px (scene.json says 290). I used 289 px. The y extent is 116 px (width).
- Length = 289 × 0.003561 = 1.029 m, rounded to 1.03 m.

## Checks
- Two frames agree within 2 px, and three tracking points on the cat give the same speed within 0.1%.
- Sanity check: the floor between the walls is about 1555 px, which is about 5.5 m. The cat is about 191 px with
  its tail, which is about 0.68 m. The bench is about 1.03 × 0.41 m. All of these are plausible.
- Possible error: the bench top sits higher than the cat's origin, so perspective could make it look a few
  percent larger. I applied no correction, following the 2D single-scale convention.

Confidence: good (±5%).
