# Q1176 — height of the telephone booth (m) → **2.85**

The question's rate (33 fps) and the file's rate (33 fps) are the same. Static camera. The principal point is assumed to be the image centre (960, 383).

## Pixel measurements
- Booth (static, right sidewalk): the white front face runs from y ≈ 114 (roof edge against the sky) to y ≈ 400 (base on the
  sidewalk), measured from column intensity profiles at x = 830–905 on frames 90/96/98 (`booth_px.py`). That gives **286 px**
  (the record's bbox, 114–402, gave 288). The face spans x ≈ 805–913, with the shaded left side face at x ≈ 795–805.
- Bike path (`fit3d.py`): rigid constant-velocity straight-line model fitted to the rear-wheel contact, pelvis and head tracks
  (frames 5–98). The shared vanishing point is (568.1, 197.8) and the rms is 2.4 px. So the bike moves on a straight, uphill
  road line.

## Focal length (independent of the bike-origin question)
- The bike's depths plus 4.87 m/s do not fix f, because the result depends on the bike origin's height (pelvis → ~1300,
  ground → ~1850). So f comes from the road plane instead.
- Road plane = street direction D (bike VP) + horizontal cross direction (no roll or cross-slope assumed).
- Exact perspective fit of the near manhole's inner dark disc (contour, `manhole_fit.py`): **f = 1983–2027**, with a clear rms
  minimum (f = 1340 gives rms 5.8 px against 1.5 px at f = 2000).
- Check: at f = 2000 the same disc on the same plane predicts the far manhole at 85.8 × 8.6 px; observed ≈ 86 × 8.6 px
  (`manhole_check.py`). A joint shared-radius fit gives f = 1992. **f = 2000 is used** (HFOV 51°).

## Scale and depth
- Camera-to-road distance H = 2.044 m. It comes from the rear-wheel contact line scaled by the prior speed of 4.87 m/s.
- Check against depth_info: the contact point's distances are 11.585 / 16.378 m at t = 1 / 2 s. The given bike distances
  (12.1238 / 16.9027) are reproduced by an origin a constant 0.55 / 0.53 m further along the path, which fits a bike root
  between the wheels. So the speed and the bike depths agree.
- Curb (the sidewalk's height above the road) is 0.088 m, from the curb face's edges at row 700.
- The ray to the booth base (860, 400), intersected with the sidewalk plane, gives Z = 19.93 m (distance 19.96 m). That is
  just closer than the bike at t ≈ 2.9 s (its contact y is 391, against 400 for the booth base), which is consistent.
- **Height = 286 × 19.93 / 2000 = 2.85 m.** Without the curb correction it would be 2.98 m.
  Sensitivity: f = 1983 → 2.87 m; f = 2027 → 2.81 m.

## Sanity checks
- At f = 2000 the rider plus bike is 1.6 m (head to wheel), the pelvis is about 1.07 m above the road, and the manhole disc
  is about 0.83 m across. All are realistic.
- The pedestrian's feet on the sidewalk give a stature of 1.70 m at about 10.9 m. But the pedestrian's depth_info says
  17.17 / 18.38 m, which cannot be right: their feet sit lower in the image than the bike's contact point, which is at 12 m.
  So I did not use the pedestrian depth_info; that object's origin seems to be offset from the person.

## Confidence
About ±5%. The main uncertainties are f (±2%), the curb/sidewalk offset (±2%), and the booth's top edge (±1 px). If the
world bounding box also includes a roof cap or base not visible on the front face, the true value would be a little higher.
