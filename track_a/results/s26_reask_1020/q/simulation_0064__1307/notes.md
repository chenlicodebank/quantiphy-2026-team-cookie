# Q1307 — width of the lane (road surface the vehicles drive on, curb to curb)

The question rate and the file rate are both 24 fps, so t=0.58 s is frame 14 and t=1.58 s is frame 38.
The prior (the white van accelerates at 4 m/s²) is realistic, so the scene is at real scale. The scale comes from depth_info plus pinhole geometry.

## Focal length (poles.py, curbs2.py, farcurbs.py)
- Vertical vanishing point: the centre lines of the two near signal poles were fitted on frame 71.
  - Left pole: dx/dy = 0.0931.
  - Right pole: dx/dy = −0.1174; its upper segment gives −0.1185.
  - The two lines meet at (1077, 7464). The x value is about cx, so the roll is about 0.
- Street vanishing point (horizon):
  - Re-fitted near curbs (road edge = bottom of the curb face, found from cobble texture): VP (1084, −137).
  - Re-fitted far curbs (gradient): VP (1089, −123).
  - The record's far-right curb fit had an rms of 15 px; I replaced it.
- With orthogonal vanishing points and the principal point at the image centre, f² = (cy − v_h)(v_v − cy). This gives f = 2143–2165 px (horizontal FOV about 53°). I used 2154.

## Road width
- Image width of the carriageway:
  - Far street: 1.6773·y + 207.0 px.
  - Near street: 1.6533·y + 226.8 px.
  - Over the rows used, the two agree within about 1.5%.
- W = width_px(y_g) · Z_g / f, where:
  - y_g is the row where an object touches the ground.
  - Z_g = camera-axis depth of that point = d · f / sqrt(f² + du² + dv²), with a small correction for the offset between the origin and the contact point (cyclist 0.6 m, van 1.9 m to the front-wheel line).
- Results:

| Object and frame | W (m) |
|---|---|
| cyclist f14 | 11.7–12.0 |
| cyclist f38 | 12.1–12.2 |
| van f14 | 12.2–12.4 |
| van f38 | 11.9–12.1 |
| pedestrian f38 (on the sidewalk, +0.15 m curb correction) | 12.2–12.4 |

  - Mean: 12.05–12.17 m across the horizon choices, with spread sd 0.17.
  - The implied camera height is about 6.9 m and is consistent across the objects.

## Checks
- Pedestrian height: 103 px at Zc 36.3 m gives 1.73 m, which is plausible for an adult.
- Van front width: about 1.95 m, matching a real full-size van (about 2.0 m).
- So the f and the scale are consistent with standard objects.

## Answer
12.1 m. Confidence: good, about ±4%. The main uncertainties are f (about 1%), which ground row matches each origin's depth, and whether the far and near curbs are measured at the curb top or at the road edge.
