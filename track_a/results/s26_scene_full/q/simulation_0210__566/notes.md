# Q566 – lampshade diameter (simulation_0210)

Prior: black cat speed = 0.94 m/s. No depth_info. fps 24 = question_fps.

## Scale from the cat
From scene/tracks/cat.csv (mask centroid; I checked it against the record): the mean per-frame speed is 432 px/s,
the net displacement over the frames gives 429.7 px/s, and linear fits give 427.7 px/s (centroid), 427.2 (torso) and
426.4 (nose). I used 429.7 px/s, so the scale is 0.94/429.7 = 2.188e-3 m/px at the cat's depth.

## Lampshade pixel width (measure.py, shade.py, shade_edge.py)
- The shade's widest extent is at its bottom rim, y≈614–615. I placed the edges at half-max between the wall and the
  shade: x 1409 → 1623.5, so the width is 214.5 px (scene record: 215).
- The bottom rim sags about 4 px in the middle, so the camera sits only slightly above the rim. The rim is close to
  edge-on, and its width equals the diameter.
- Without a depth correction: 214.5 × 2.188e-3 = 0.469 m.

## Depth correction (perspective)
- The cat walks in front, with its paws at y≈1025–1030. The lamp stands on a table against the wall: the table's
  front feet are at y≈1000, the wall base at y≈955, and the lamp base is near the back of the visible table top
  (y≈800, while the top spans 795–818).
- The horizon is estimated at y≈470–560, from the nearly edge-on rim.
- The floor point under the lamp is at y≈965–975, so Z_lamp/Z_cat = (y_cat − y_h)/(y_lamp − y_h) ≈ 1.10–1.15.
  The bounds are 1.06 (table front) and 1.17 (wall).
- I applied a factor of ≈1.11, giving a diameter of ≈0.52 m.

## Check / confidence
- The pixel width agrees between the threshold run, the half-max run and the record (213–215 px).
- The speed scale agrees across five reference points to within ±1%.
- The main uncertainty is the depth ratio, which is estimated rather than measured (±5%). Overall confidence is
  about ±8%.
- Answer: 0.52 m. The uncorrected planar value is 0.47 m.
