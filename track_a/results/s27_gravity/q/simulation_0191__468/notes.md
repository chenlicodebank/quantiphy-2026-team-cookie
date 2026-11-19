# q_468 — truck length (simulation_0191)

File fps = question_fps = 120.

Scale from prior (box free fall g = 9.8 m/s^2 before 0.6 s):
- fit.py: quadratic fit of the box front-face centre cy (scene/tracks/box.csv, template match on the logo) vs t = frame/120.
  Frames 0-60: a = 1975.9 px/s^2 (rms 0.06 px); 5-58: 1975.4; 0-40: 1984.6; 20-60: 1966.4.
  -> 9.8 / 1975.9 = 0.004960 m/px (spread about ±0.5 %).
- The tracked point is on the box's front face, so the scale applies to the front-face depth. When the box rests,
  its front bottom edge (y≈407.5) lines up with the truck's roof edge (y≈410). So the box front face lies in the
  truck's side plane to within about 2 %, and the same scale holds for the truck side.

Truck pixel extent (frames 0 and 180, grid crops): rear bracket/lamp x≈122. Cab front body x≈1812, top railing
x≈1828, mirrors x≈1838. The mirrors stick out toward the camera, so their projected x is inflated by about 1-2 %.
I took the overall front at x≈1825, giving 1703 px.
Length = 1703 x 0.00496 = 8.45 m. Body only (1690 px) = 8.38 m; mirrors as seen (1718 px) = 8.52 m.

Check: 8.4-8.5 m is a plausible size for a catering truck on a rigid chassis. Wheel diameter 165 px = 0.82 m and
the box length of 408 px = 2.0 m are also plausible.
Confidence: about ±3 %.
