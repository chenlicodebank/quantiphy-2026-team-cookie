# Q326: speed of the cup at t = 1 s (m/s). Prior: cup diameter = 0.087 m

The file rate and question_fps are both 24, so t = 1 s is frame 24 and speed = |p24 - p23| x 24.

## Object
The only moving object is the navy tapered cup (scene/ calls it `blue_cylinder`). It is held at a fixed tilt and
spins about a vertical axis while sliding left to right; its bbox height stays at ~168-172 px the whole time. Its
visible flat end is the narrow base (~95-100 px). The rim end (widest) is the diameter the prior gives. A camera that
does not move, a 2D video, and the cup at constant depth (y constant) mean one m/px scale is enough.

## Diameter in pixels (rim width across the symmetry axis)
- `diam.py`: for each mask, find the symmetry axis, then take the widest section across it.
  SAM 3 masks (`run_sam.py`, frames 7-46) give 132-137 px at every orientation, mean ~135 px (frame 24: 134.5).
  Since end-on and side-on frames agree, perspective changes along the cup are small.
- The colour mask (scene/ method) gives ~121-127 px around frames 18-26. **That is 9 pct less than SAM.** On the
  zoomed overlay `frames/outline_24.png`, SAM (red) follows the true silhouette. The colour mask (green) misses the
  dark shaded left side of the cup, so the colour widths and areas are too small. SAM is the right one.
- Edge check (`speed.py`): intensity half-crossings across the widest section give 133.2 px at frame 16 and
  131.8 px at frame 24. That is ~2 pct less than SAM (SAM is about 1 px loose per side). This failed at frames 8 and
  44, where the dark underside sits on a dark background.
- Value used: D = 133.5 px (± 1.5), so the scale is 0.087 / 133.5 = 6.52e-4 m/px.

## Pixel speed at frame 24 (`speed.py`)
| Series | Raw p24 - p23 (px/frame) | Cubic fit over frames 19-29 (px/frame) |
|---|---|---|
| SAM track centroid | 35.11 | 34.93 |
| SAM track bbox centre | 34.03 | 35.02 |
| SAM segment centroid | 35.01 | 34.90 |
| SAM axis midpoint (origin proxy) | 34.11 | 35.42 |
| Colour centroid | 35.91 | 35.49 |

Vertical motion is under 1 px. Value used: 35.1 px/frame, which is 842 px/s.

## Result
Speed = 842 x 6.52e-4 = **0.549 m/s**.
The range from the uncertainty in D (132-135 px) and the speed (34.9-35.5 px/frame) is 0.54-0.56 m/s.

## Second route / checks
- The rim width is the same in end-on (frames 20-26) and side-on (7-12, 40-46) views, so the scale does not depend
  on orientation.
- Five independent reference-point series agree within ±1.5 pct after smoothing.
- If the prior meant the narrow base (~97 px), the answer would be ~0.75 m/s. A cup's "diameter" is normally its
  rim or largest diameter (the extent of its bounding box), so I answered with the rim.

## Confidence
Good (about ±3 pct). The main residual risk is which diameter the prior means.
