# Q2056: truck length (m), prior lane width = 3.66 m

Method: this is a 2D top-down drone clip with a static camera. I used a single scale, prior divided by lane-width pixels, as the annotators did. Script: `measure.py`.

- **Lane width:** I measured the subpixel x-centres of the lane lines (max-projection column profiles) on the truck's carriageway, frames 0, 54 and 106, at several y bands.
  - Left edge line to right edge line spans 3 lanes, for example 1077.9 → 1370.9 and 1083 → 1375.
  - That gives 97.4–98.6 px per lane, mean ≈ 97.7 px (record said 96–98).
  - Scale = 3.66 / 97.7 = 0.03746 m/px.
- **Truck length:** cab front to trailer rear, from the brightness profile along the truck's centre columns (5 columns agree within ±1 px).
  - Frame 106 (truck near the image centre, y 2435–2892): 458 px. This matches the record's 457.
  - Frame 54: 468 px.
  - Frame 0 (bottom of the image, y 3083–3561): 479 px. I confirmed this visually. The record's constant 457 understates it there; image-edge distortion and lean of the 4 m tall trailer are stronger at the bottom of the frame.
- **Lengths in lanes:** 4.69 (f106), 4.79 (f54) and 4.87 (f0), mean 4.78. In metres: 17.2, 17.5 and 17.9.
- **Answer:** 17.5 m, the mid-clip value and the mean across positions. It is plausible for a tractor plus semi-trailer.
- **Confidence:** about ±3%. The main uncertainty is which frame the annotator measured on.
