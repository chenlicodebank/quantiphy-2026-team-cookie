# q 2278 — height of the toy (teddy bear), cm

Prior: g = 9.8 m/s^2; no depth_info. File fps = question_fps = 24.

## Method
- measure.py: re-segmented the bear myself as its own connected non-white component in the free-flight frames
  17-22 and 53-58 (thresholds s>30|v<225 and s>50|v<205 give the same boxes). Results match scene/ tracks.
- fit.py: quadratic fit y(t) per toss, t = frame/24. The pixel centroid is the physical reference (the bear tumbles a
  little, so top and bottom edges give 2780-3085 px/s^2, biased by rotation).
  - Toss 1 centroid: a = 2721 px/s^2 (rms 0.26 px; leave-one-out 2654-2775). Bear bbox height 93 px (side view).
    -> 93 / 2721 * 9.8 m = 33.5 cm
  - Toss 2 centroid: a = 2906 px/s^2 (rms 0.36 px; leave-one-out 2789-3042). Bear bbox height 98-99 px (front view,
    upright, frame 54-55). -> 33.05-33.4 cm
- The two tosses agree within 1.5 % on height/acceleration ratio (independent second route).

## Answer
33.3 cm (range of routes 33.0-33.5; edges-based fits 29.7-34.6 are rotation-biased and not used).
Confidence: moderate-high (~5 %), limited by the short 6-frame parabolas.
