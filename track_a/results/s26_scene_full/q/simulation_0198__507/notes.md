# Q507: diameter of the bottle's neck (m)

Prior: the droplet's acceleration is 9.7 m/s². The video is 60 fps and question_fps is also 60, so no re-timing is needed. The scene is a static-camera 2D setup, so one m/px scale comes from the drop's pixel acceleration.

## Scale (fit_acc.py)
- Drop centroids come from scene/tracks/drop.csv. They use the record's render-index mapping: video frame 7 duplicates frame 6, and render step 8 is missing. With that mapping one quadratic fits frames 0–10 with a residual under 0.4 px.
- Quadratic fit over render steps 0–10: a = 31.69 px/frame² (vertical 31.69, horizontal −0.47), which is 114,100 px/s².
  - Fit over steps 1–6 only: 31.66. Fit over steps 0–8: 31.71.
- Second route: mean one-frame change in scalar speed over the clean frames 0–6 is 31.79 px/frame². This differs from the fit by 0.3%.
- Scale = 9.7 / 114,100 = 8.50e-5 m/px.

## Neck width (neck_profile.py, neck.png)
- I averaged frames 11–13 (drop gone) to cut the grain, then took column profiles of the horizontal gradient over the threaded neck, rows 545–655.
- The outermost strong edges are at x ≈ 1776 (left) and x ≈ 2066 (right). Reading the grid crop by eye gives 1773 and 2067.
- Neck width: 292 ± 5 px, measured as the outer thread extent, which I take as the neck's bounding-box width. The record's 295 px agrees.
- For reference, the body edges are at 1704 and 2129, so the body is 425 px wide.

## Answer
292 px × 8.50e-5 m/px = 0.0248 m.

Sanity check: the body comes out 3.6 cm wide and the bottle about 6.4 cm tall. That is plausible for a 30 ml serum bottle, and the label says 30 ml.

Confidence: moderate-high. The main uncertainties are:
- whether "neck" means the outer thread extent (used here) or the bare cylinder (about 255 px, which would give 0.0217 m);
- a possible depth difference between the drop (at the pipette tip) and the bottle.
