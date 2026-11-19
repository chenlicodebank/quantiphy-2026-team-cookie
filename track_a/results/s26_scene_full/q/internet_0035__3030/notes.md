# q3030: width of the thumbnail (cm)

Prior: toilet paper core size = 100 mm. I read this as the tube's length (its axis). If it were the diameter (260 px), the
nail would come out at about 3.6 cm, which is implausible. Under the length reading the core diameter is 4.7 cm, which is realistic.
This is a 2D internet clip, so I use one planar scale (annotator convention). Time base doesn't matter for a size.

## Scale
Tube length end to end, measured on frames where the open right end is visible:
- frame 0: 1720 → 2279 (bbox); the record gives 555 px at row 1300.
- frame 10: 1864 → about 2427.

I take **558 px** (555–563), so scale = 100 / 558 = 0.179 mm/px.

## Thumbnail
The thumb sits under the tube and points left, with the nail facing the camera. The nail width runs across the thumb axis,
which here is vertical in the image. I measured from the upper lateral nail edge to the lower lateral nail edge on
CLAHE-enhanced 4x crops (view.py, frames/v*.png):
- frame 0: y 1393 → 1485, about 91 px
- frame 10: y 1364 → 1457, about 93 px
- frame 17: y 1346 → 1442, about 95 px

I take a mean of **93 px**, so 93 × 0.179 = 16.7 mm = **1.67 cm**.

## Checks
- The three frames agree within ±2.5%.
- Tube diameter: 260 px × 0.179 = 4.7 cm, a realistic core size.
- A thumbnail of 1.4–1.8 cm is typical for an adult.

Confidence: moderate. The main uncertainty is where exactly the annotator placed the nail edges (±5 px) and whether
they used 555 or 560 px for the tube.
