# q1249: height of the turning yellow car (taxi), in metres

File fps = question_fps = 24, so t=0.58 s is frame 14 and t=1.58 s is frame 38.

## Focal length (focal.py)
- The white van (prior: a = 4 m/s^2) is placed in 3D from the given depths at f14 (43.812 m) and f38 (43.003 m), using the
  bbox centre from scene/tracks/van.csv. Every frame's ray is intersected with the line through those two points, and
  the path coordinate s(t) is fitted with a quadratic. f is chosen so that the fitted a = 4.
  - bbox cx: f = 2165 (frame windows 2-71), 2252 (2-36), 2179 (36-71), 2146 (10-60)
  - panel template cx (patch_cx + 27.5): f = 2210 / 2206 / 2214
  - Check: per-frame speed rises from about 0 at f1 to about 11.6 m/s at f71, so a is about 4 and constant.
  - Adopted value: f = 2190 +- 25 px (horizontal FOV about 52 deg).
- Weak check (check_f.py): at this f the van and cyclist travel directions agree to within about 1.5 deg.

## Taxi pixel extents (profile.py, taxi_h.py, frames/th_14.png, th_38.png)
- f14 (side view): top of the roof sign y = 719.5; bottom of the near front tyre y = 815.5, so 96 px.
- f38 (oblique front view): top of the roof sign y = 719.5; bottom of the front-left tyre y = 829, so 109.5 px.

## Height (height.py)
- I used a level camera frame with the horizon at y = 702 (the main road's vanishing point), which gives the pitch.
- The horizontal distance of the taxi origin comes from its given depth. The sign top is taken at the origin's
  distance. The bottom tyre is taken that much closer to the camera: 1.0 m at f14 (half the car's width) and about 1.6 m
  at f38 (the front-left wheel).
- Results with f = 2190: H = 1.62 m (f14) and 1.655 m (f38). With f = 2165 or 2210 the range is 1.60-1.67.
- Second route: the plain value h_px x Z / f = 96 x 37.6 / 2190 = 1.65 m (f14).
- Camera height from objects on the ground: the cyclist gives 1.82, the van 1.85-1.87 and the taxi's own tyres 1.92.
  The pedestrian gives 1.55, probably because they stand on the raised sidewalk. These do not fully agree, so
  "camera height minus sign top" gives a lower 1.48-1.50 m. That route is less reliable.

## Answer
1.64 m: the world bounding box including the roof sign.
- The roof sign adds about 9 px (about 0.15 m). Without it the height would be about 1.49 m.
- Confidence: moderate. The main uncertainties are f (+-2%) and whether the roof sign is part of the box.
