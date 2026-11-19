# q_907: height of the red cup (m)

Prior: the mug falls with 9.8 m/s^2 before 0.5 s (frames < 15). question_fps = file fps = 30. The "red cup" is the static red/white takeaway cup on the table (x ~838-878 px). There is no depth_info, so the scale comes from the mug's free fall alone.

## Camera
The camera is static and frontal with no pitch: the window and AC-unit vertical edges keep a constant x from y=50 to y=1060 (verticals.py). A fall at constant depth therefore maps linearly to pixels, with one px/m scale for the fall plane and the mug's rest spot.

## Pixel acceleration (fit2.py, subpix.py)
- The mug rim (top silhouette edge) was measured to sub-pixel accuracy on frames 7-15. A quadratic fit gives a = 6.95 px/frame^2 with rms 0.02 px. Frames 5-6 are polluted by a dark halo (shadow) above the mug.
- The scene record's bottom edge gives 6.87 px/frame^2. The midpoint of my top and the scene bottom gives 6.91 px/frame^2 (rms 0.25).
- Perspective: the silhouette shrinks as the mug falls (seen from below). From that, horizon ~ y 743 and f ~ 2570 px. The top-edge acceleration is inflated by about 1+R/f and the bottom's deflated by 1-R/f, so the centre is about 6.90 px/frame^2.
- Scale: 6.90 x 900 / 9.8 = **634 px/m** in the mug's plane.

## Cup height in pixels (cupwidth.py, bottoms.py, frame 39)
- Lid top edge: y = 807.6. Base: y ~ 871.5 (the red band ends there; the dark contact line and glossy reflection start below it). The silhouette is 64 px, which matches the scene record (bbox 808-872).
- The cup is seen slightly from above. Removing the lid far-edge and base near-edge bulges (about 1.7 px) gives an axial height of about 62.4 px.
- Depth: the cup's base sits ~3.5 px lower than the mug's resting base (868.5, which is 124 px below the horizon). The cup is therefore about 2.8 % closer to the camera, so the scale at the cup is 634 x 1.028 = 651 px/m.

## Answer
62.4 / 651 = **0.096 m**.

Alternatives:
- Uncorrected: 64 px / 634 px/m = 0.101 m.
- Constant-scale fit of the scene ref_y: 623 px/m, giving 0.098-0.103 m.

Sanity check: at this scale the mug is about 8.2 cm tall and 7.5 cm wide, and the takeaway cup about 9.6 cm. Both are realistic sizes.

Confidence: moderate-high, about ±4 %.
