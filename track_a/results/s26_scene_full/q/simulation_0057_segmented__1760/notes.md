# q1760 — distance between the two streetlights (m)

Prior: orange car acceleration = -2.86 m/s^2. fps = question_fps = 30 (no re-timing).

## Objects
The two dark "dumbbell" props in scene/ are the streetlights seen from almost directly above. The hexagonal blob
is the lamp head on top, the round knob is the pole base, and the thin shaft is the pole, foreshortened by
perspective. Check: the hex centre equals the knob centre scaled radially about the image centre (540,540) by
1.183 in both x and y for both lights (measure_props.py), which is what a vertical pole looks like under a
pinhole camera. Pole height h = 0.155 H, where H is the camera height.

## Measurements (scripts in this folder)
- measure_props.py (frame 90, distance-transform centres):
  - knob (base) upper (250.5,464.9), lower (250.7,910.3), giving a base-to-base distance of **445.4 px**
  - hex (top) upper (197.5,451.0), lower (197.9,978.5), giving 527.5 px (= 445.4 x 1.184, consistent)
- measure_car.py: quadratic fits of the car silhouette's y(t). Mid of front and rear edges, frames 16-90:
  -163.7 px/s^2 (frames 40-90: -163.6). Mask centroid, frames 20-90: -162.5. Front edge only: -158.8; rear edge
  only: -168.6. The front and rear edges change as the silhouette switches between surfaces, so I use the mid and
  centroid values: a = 163.2 px/s^2.
- Scale at the height of the car's outline: 2.86 / 163.2 = 0.01752 m/px (car length 288 px, which gives 5.0 m;
  plausible).

## Perspective correction
The car's outline sits about 0.5-0.7 m above the ground, and the pole bases are near the ground, so the base
points are slightly farther from the camera. roof_shift.py measures the parallax of the dark roof glass against
the outline: a slope of about 0.016 per pixel of image offset. That means dz/H ≈ 0.016, so H is roughly 30-40 m
(a pole height of about 5-6 m, which is plausible). The resulting ground-scale correction is +0.5 % to +2 %; I
used about 1.01.

Distance = 445.4 px x 0.01752 x 1.01 ≈ **7.85 m**. Without the correction it is 7.81 m. Using the tops instead
(527.5 px at height h, scale = ground scale / 1.183) gives the same value.

## Second route
Using the centroid acceleration (162.5) instead of the edge mid (163.7) changes the result by ±0.4 %. Using the
tops gives the same result as the bases (the radial ratio is consistent). Confidence: good, ±3 %. The main
uncertainty is the small perspective correction for the car's height.
