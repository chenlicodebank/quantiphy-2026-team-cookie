# q_462 — width of the truck (prior: box width = 1.33 m)

Video: 2D simulation, 120 fps (file and question rates are the same), static level camera looking at the rear of a box truck.
There is no depth_info, so the scale is metres per pixel from the cardboard box's width, treated as being in the same plane as the truck's rear face.

## Measurements (widths.py: sub-pixel gradient edges, many rows, frames 0/200/400)
- Box horizontal extent (edge of the saturation/brown region), rows across the visible face: 282.0, 282.0, 280.0 px. The scene record says 281.5.
- Cargo body rear face (the widest part of the truck; no mirrors or other parts stick out beyond it), outer left/right edges: 566.9 (some frame-0 rows catch the rounded corner), 569.3, 569.4 px. The scene record says 570.
- Truck width = 1.33 × ratio: 2.674, 2.685, 2.705 m. Using the record values (570 / 281.5): 2.693 m.
- Answer: **2.69 m**.

## Checks and caveats
- Second route: the record values (570 / 281.5) give 2.693, the same as my own edge measurements on three frames (2.67–2.70).
- Width reading: the truck's width is its horizontal extent across the rear face (side to side), which is what was measured.
- Depth caveat: the box sits on or above the roof, so it is somewhat behind the rear face. Its image motion is not rigidly tied to the body: it lags at the start and stops at frame 397 while the body keeps accelerating. So the motion ratio cannot give the depth ratio.
  - No usable perspective cue was found. The truck's sides are not visible, and the stabiliser feet and floor line only give quantities that do not depend on focal length.
  - If the box were 5–10 % deeper than the rear face, the true width would be about 2.45–2.55 m.
  - Following the 2D convention (one scale, no clear perspective), the answer is 2.69 m.
- Confidence: moderate. The pixel ratio is good to about 1 %; the main risk is the depth offset of the box.
