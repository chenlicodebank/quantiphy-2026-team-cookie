# q1858: speed of the astronaut at t = 0.5 s (m/s)

Prior: astronaut height = 2.2 m. 2D video, 24 fps (file fps = question_fps = 24), so t = 0.5 s is frame 12, and the speed is |p(12) - p(11)| x 24.

## Scale
- Vertical extent of the figure, measured in code (`height.py`: darkest pixel per row, 30/60/100 thresholds plus a sub-pixel edge crossing). It is 90-93 px over f0-f16 with a mean of about 91.0 px; it is 90.5 px at f11-f12. The figure is nearly upright here (main axis 94-95°), so the vertical extent is its height.
- SAM 3 masks ("astronaut", box-prompted): f11 is 91 rows tall, which agrees with mine. f12 is 93 rows tall: about 2-3 px more than mine (a 3% difference). On the overlay and the zoomed crop (`frames/f12.png`) the figure has sharp edges at rows 460-549. The extra SAM rows are a halo at the helmet, so my extent is the right one. (A first SAM call with a misplaced box gave a bad 116 px mask; I discarded it.)
- I used H = 91.0 px, so the scale is 2.2 / 91.0 = 0.02418 m/px.

## Motion
- Centroid track (`measure.py`, binary and soft-weighted centroids; it matches scene/tracks/person.csv). The figure rises almost vertically and accelerates smoothly from rest at about f3. The pose is rigid, so the centroid stands in for the pelvis origin.
- Speed at frame 12 as a backward difference on fitted curves (`fit.py`): quadratic fits over windows 4-22, 5-19 and 6-18 give 2.64-2.68 px/frame; cubic fits give 2.69. The raw p12 - p11 step is 2.73 px (binary) or 2.77 px (soft), and the raw centred average (p14 - p9)/5 is 2.66 px/frame.
- The SAM centroid step from f11 to f12 is about 2.2 px. That is noisy (the f12 mask has the halo), so I did not use it.
- Adopted speed: 2.67 px/frame = 64.1 px/s, giving 64.1 x 0.02418 = **1.55 m/s**.

## Second route
- The raw 5-frame average (2.66 px/frame) gives 1.54 m/s.
- The raw one-frame step (2.73 px/frame) gives 1.58 m/s.
- The routes agree within about 2%.

Confidence: good, within about ±4% (height ±1 px, speed ±0.05 px/frame).
