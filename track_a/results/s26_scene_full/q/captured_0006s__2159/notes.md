# q2159 – displacement of the toy (yellow fruit) between t=1.0 s and t=1.2 s

- question_fps = file fps = 24 -> frames 24 and round(28.8) = 29.
- Pixel centres (mask centroid from scene/tracks/fruit.csv, checked on zoomed frames frames/f_10.png, f_12.png):
  f24 (606.2, 139.8), f29 (581.1, 222.9) (f29 is motion-blurred vertically; centroid = blur centre; bbox centre
  (582.5, 223.5) agrees).
- Lab method card: f = 0.5959*1280 = 762.8 px, principal point (640, 360); P = ((u-cx)/f, (v-cy)/f, 1) x depth
  with depth 1.402 m (t=1.0) and 1.065 m (t=1.2).
- Displacement |P29 - P24| = 39.9 cm (centroid), 40.0 cm (bbox centre). Mostly toward the camera (dZ = 33.7 cm).
- Alternative reading (depth as Euclidean range, ray normalised): 36.2 cm. I answer with the card's convention (39.9).
- Check: the object size from depth matches at both times (f24 eq_diam 58.6 px -> 10.8 cm; f29 minor 72.6 px -> 10.1 cm),
  so the given depths fit the apparent sizes. The acceleration prior (g) is not needed for this displacement.
- Confidence: moderate-high. The main uncertainty is the depth convention (~10%).
