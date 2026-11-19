# q_629: diameter of the vase (m)

Prior: the black cat's speed is 0.94 m/s. fps is 24, the same as question_fps. The scene is a 2D top-down render
with a static camera, so I used one metres-per-pixel scale.

## Scale (measure.py)
- I made a black-cat mask (max channel < 60, largest component) for all 50 frames.
- The front edge moves from x 647 to 1185 over 49 frames. That is 10.98 px/frame, with steady steps of 10–12 px.
- Second route: the mask centroid's mean step is 10.93 px/frame, and its net displacement divided by 49 is 10.92 px/frame.
- I used 10.98 px/frame × 24 = 263.5 px/s, which gives 0.94 / 263.5 = 0.003567 m/px.

## Vase pixel diameter
- The vase is a white/blue round vase on the left end of the console, seen from above. It is static: frames 0, 24
  and 49 give the same result.
- Half-intensity edges on the brightness profiles:
  - Along the row through the centre: x 717.8 to 791, so 73.2 px.
  - Along the column: y 198.6 to 272.5, so 73.9 px.
- From the masks: the bbox at threshold 150 is 71 × 74 px, and the enclosing circle is 72–74 px. The overlay
  (frames/vase_mask_0.png) shows an outline of about 73 × 73.5 px.
- I used 73.5 ± 1 px, which agrees with the scene record's 72 px.

## Answer
73.5 px × 0.003567 m/px = **0.262 m**. Using the centroid speed instead gives 0.263 m.

## Caveat
The vase top is above the floor, so under perspective it may look slightly larger than at floor depth. Following the
2D convention, I applied no correction.

Confidence: good, about ±3%.
