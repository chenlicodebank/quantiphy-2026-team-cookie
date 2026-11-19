# Q781: width of each glass window (m)

Prior: speed of the horse = 0.874 m/s. The clip has only one horse (it walks in front of the house, "at the back" of
the scene). 24 fps for both the file and the question. The video is 2D-like: the horse walks side-on across the image
plane, close to the house facade (hooves at y≈1045, house base at y≈1040), so I used a single metres-per-pixel scale.

## Window width (win_profile.py)
The three arched ground-floor windows (frame 49, where the horse is clear of them) were measured with a B−R chroma
profile, which separates the bluish glass and frame from the reddish brick:
- left window: 271.5–337.5
- middle window: 507.5–573.5
- right window: 743.5–809.5

All three are **66 px** wide (±1 px), outer frame edge to outer frame edge.

## Horse pixel speed (horse_edges.py, horse_check2.py)
The record's chained torso track gives 3.15 px/frame. Its drift is visible: it falls about 6 px behind the real body
by frame 20. I re-measured the speed without chaining:
- Body band rows 935–975, horse mask R−B > 55:
  - rear (buttock) edge: slope 3.29 px/frame, end-to-end 3.26
  - breast edge: slope 3.19, end-to-end 3.20
  - mask centroid: slope 3.31, end-to-end 3.25
  - trunk midpoint: about 3.24
- Direct long-baseline template matches (0→49, 5→45, 24→48): 3.20–3.31 px/frame.

I used **3.24 px/frame = 77.8 px/s**, which gives a scale of 0.874 / 77.8 = **0.01124 m/px**.

## Answer
66 px × 0.01124 = **0.742 m**.

Second-route check: with the scale above, the horse measures 182 px ≈ 2.05 m long and 162 px ≈ 1.82 m tall (ear top
to hoof), which is plausible for a horse. With the record's 3.15 px/frame the answer would be 0.763 m (+3%).

Confidence: moderate-high. The main uncertainties are about 3% in the speed (gait wobble, rig-root convention) and a
small depth offset between the horse and the facade: the horse is slightly in front, which would make the true window
a little larger.
