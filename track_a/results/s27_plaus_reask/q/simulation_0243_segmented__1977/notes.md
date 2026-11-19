# q_1977 – height of the deer (m)

Prior: deer speed = 1.277 m/s. 2D scene with a static camera, 30 fps (the file and question_fps agree), no depth_info.
The "deer" is the only animal: a stylised dark quadruped with a large back-swept horn, walking right in side view.

## Scale (from the prior)
measure2.py: the belly-band (y 1380-1400) column profile is shifted between frames, with the tree columns x<120
masked out.
- Per-frame shift: mean 6.31 px/frame (noisy because of gait).
- Long lags (10/20/30/37/50 frames): 6.60/6.54/6.58/6.55/6.58 px/frame. The leg-band profile at lags 20-37 gives 6.44-6.56.
- The scene record also matches: torso_cx linear fit 6.55, muzzle tip 6.54 px/frame.
- Adopted speed: 6.56 px/frame = 196.8 px/s. Scale = 1.277 / 196.8 = 6.49e-3 m/px.

## Height
Height is measured from the horn top to the lowest hoof. The hoof line is at y = 1546 (range 1544-1550). The horn top
is at y 1128-1144: in frames ≥ 43 it is at 1128-1133 and clear of the tree; in mid frames it is near 1135-1143. The
height therefore ranges from 403 to 420 px. Median of all frames: 414 px (my measure) and 411 px (scene record).
Adopted: 413 px.
Height = 413 x 6.49e-3 = **2.68 m** (range 2.62-2.72 m).

## Checks
- At the same scale, the body length without the tail (344 px) is 2.23 m and the belly-to-hoof height (170 px) is 1.10 m.
  This is a large deer or elk with a big horn crest, which is plausible at real-world scale. The prior speed is a
  realistic walking speed, so I did not rescale.
- Second route: the record's independent track (torso_cx fit 6.55 px/frame, bbox height median 411 px) gives 2.67 m.

Confidence: moderate-high. The main uncertainty is the head bob of about ±2 % and which frame the reference bbox uses.
