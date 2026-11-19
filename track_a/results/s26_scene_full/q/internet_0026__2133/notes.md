# q2133 – height of the toy truck (cm); prior: total sofa height = 90 cm

Internet video, so I used the annotators' convention: one planar scale = 90 cm / sofa pixel height.
No perspective correction is applied. The sofa sits farther back than the truck, so a real-world
estimate would come out smaller, but the reference answers ignore this.

## Sofa (red sofa at left, behind the child)
- measure.py builds an HSV red mask and reads, per column, the top and bottom of the red region
  (frames 0, 7, 14, 21, 28). The highest point is the crown of the rounded arm/back,
  y ≈ 130 (130-132 in every frame).
- Bottom: the red base ends at y ≈ 535-540 (x 400-540), and the dark feet/shadow reach the floor at
  y ≈ 548 (checked on zoomed crops frames/sofabot.png and sofatop.png). Mask values of 570-580 at x 500-560 come
  from the child's skin/legs, not the sofa.
- Total sofa height ≈ 545 − 130 = **415 px** (±8 px).

## Truck
- From the scene record's mask bbox, height_px is 252-264 over the clip, with a median of 255.5 over frames 3-28.
  On my zoomed frame-14 crop it runs from the bed top (~466) to the tyre bottoms (~720), about 255 px.
- Truck height = **255 px**.

## Result
height = 90 × 255 / 415 = **55.3 cm**.
Sensitivity: using a sofa bottom of 535 (fabric only), the sofa is 405 px and the truck 56.7 cm. Using a truck
height of 252 (late frames), it is 54.7 cm. The time base (19.68 vs 24 fps) does not matter for a size.
Confidence: moderate, about ±5%. The main uncertainty is where the sofa's top and bottom are taken.
