# q1317 — average speed of the bicycle over the whole clip (m/s)

File fps = question fps = 24; frames 0–71; t=0.58 s -> f14, t=1.58 s -> f38.
Prior: white car (the van) has acceleration 4 m/s^2. depth_info gives the bike's distance to the camera: 33.9976 m (f14) and
28.6807 m (f38).

## Measurements (my own; zoom.py / strip.py crops at 2–4x with row ticks)
- Cyclist head top / front-wheel bottom (px): f2 ≈202–204 / 294; f14 225.5 / 326; f26 256 / 365; f38 288.5 / 406;
  f50 330 / 454; f56 352.5 / 490; f62 380 / 525; f66 398 / 550; f71 425 / 582. Body x is 1055 at f14 and 1045.5 at f38.
- Correction to the record: in the van-shadow section its `*_best` columns are wrong. At f38 it gives wheel 431 and
  height 145, but the crop shows 406 and 117.5. Its height grows by 1.47x from f14 to f38, while the depth ratio is only 1.185.
- Constant speed: for any point at a fixed height on a flat ground, 1/(y − y_horizon) is linear in the distance along the
  street, whatever f is. With horizon y = −121 (street vanishing point), the head-top step per frame
  is −1.78…−1.93e-5 in every segment from f2 to f71. The f14→f38 rate predicts wheel row 294.5 at f2 (observed 294) and
  head row 425 at f71 (observed 425). So the bike rides straight at constant speed. Frames 0 and 1 are duplicates, so motion starts
  at about f1–f2.

## Scale / speed
- Pinhole camera with principal point (1080,540) and pitch from the horizon (tanθ = 661/f). The bike origin is back-projected at the
  given depths for f14 and f38, and v = |P38 − P14| / 1 s (bikev.py).
- The origin height is constant (dh ≈ 0) for f = 1500–3000 with horizon −121, which supports the geometry. v = 5.57 (f=1500), 5.46 (1800),
  5.41 (2200), 5.38 (2600), 5.36 (3000). Where the origin sits on the bike (wheel bottom to head top) changes v by only ±0.5%.
- f from sizes (sanity only): at f≈2200 the pedestrian (103 px at 38.5 m) is 1.80 m tall, the van body width (120 px at about 35.5 m to its
  front) is 1.94 m, and rider plus bike is 1.55 m. f=1500 or 3000 would give a 2.6 m or 1.3 m person, so f≈2000–2400 and
  v ≈ 5.41–5.44 m/s.
- The van prior is consistent with this. If it starts from rest, it covers 4.17–4.33 m between f14 and f38, which matches its 3D displacement of
  4.13–4.25 m (f-insensitive, so it gives only weak support).
- Second route: the radial depth change alone is 5.317 m in 1 s (a lower bound). Adding the transverse part from the image motion
  (about 80 px vertically at f≈2200) gives 5.41.

## Answer
The speed is constant at v ≈ 5.41 m/s. The mean of the per-frame speeds over frames 1–71 is 5.41 if motion starts at f0, or 5.34 (70/71) if the
duplicated f0/f1 counts as a zero-speed step. Answer: 5.38 m/s (both readings are within 1.5%; uncertainty about ±3%, mainly f).
