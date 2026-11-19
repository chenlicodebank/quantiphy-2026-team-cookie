# Q2022 – pizza diameter (cm); prior: Monopoly money width = 7.5 cm

The view is near top-down, so I used one planar scale (the internet convention): cm/px = 7.5 / (bill short-side px).
Time doesn't matter here (static sizes), so the 18.31 fps vs 24 fps difference is irrelevant.

## Pizza (from scene record, checked on frame 29)
Ellipse fit to the outer crust: horizontal 1015 px, vertical 964 px, mean ~990 px. A manual zoomed reading in the record
gives left 847 and right 1857, so about 1010 px. I used the horizontal diameter, 1015 px.

## Monopoly bill width (short side), frame 29
- "1" bill (isolated on the wood, right side, fully visible). Segmented in code (bill.py, low-saturation mask,
  approxPolyDP): corners (2459,689) (2623,738) (2557,1033) (2389,980). Short sides 171 and 176 px (mean ~174);
  long sides 299 and 302 px. minAreaRect gives 315 x 179. The overlay frames/bill1_mask_f29.png fits the bill edge.
- Top tilted "500" bill (on top of the stack, fully visible). Corners read on zoomed crops: (1922,530) (2220,464)
  (2275,602) (1967,675). Short sides 152 and 149 px (mean ~150); long sides 305 and 317 px.
- The 100 bill and the other 500 bills are partly covered by other bills, so they can't be used for width.
The two usable bills give different short sides (174 vs 150 px; aspect ratios 1.73 vs 2.07). The 500's short side
runs roughly vertically, so the ~5% vertical foreshortening seen on the pizza would explain only part of the gap.

## Result
- Scale from the "1" bill: 7.5/174 = 0.0431 cm/px, so the pizza is 1015 px = 43.8 cm (42.7 cm with the 990 px mean).
- Scale from the "500" bill: 7.5/150 = 0.050 cm/px, so the pizza is 50.8 cm (49.5 cm with the mean).
- I can't tell which bill the annotator used, so I answer 47.0 cm, about midway (each reading is about 7% from it).
  Sanity check: the pepperoni slices are ~90 px, i.e. 4–4.5 cm, which is plausible. A 44–50 cm pizza is large but
  plausible.

Confidence: moderate. The main uncertainty is which bill (and which side) was taken as the "width".
