# q1199 — height of the telephone booth (simulation_0049)

The file and the question both use 33 fps. The camera is static and level: the road vanishing point is (960, 537), where the curb lines meet,
and the cyclist's tyre-contact asymptote is at y = 537.5. Principal point (960, 537).

## Geometry used
For a level camera, a point on a plane a height Y below the camera, at depth Z, appears at v - h = f*Y/Z (h = 537).
The booth's front face is upright and stands on the sidewalk, so
height = (v_bottom - v_top) * (H - c) / (v_bottom - h),
where H is the camera height above the road and c is the sidewalk (curb) height.

## Measurements (scripts in this folder)
- Booth (`booth.py`, mean of frames 0-10, half-level edges along 6 columns): top 404.5 and bottom 663.8, so 259.3 px tall.
  The bottom is 126.8 px below the horizon. The scene record's box (409-659, 250 px) was too tight, so I corrected it.
- f*H (`tyrefit.py`): I fitted the cyclist's tyre contact as y = h + A/(frame+b): h = 537.5, A = 19973, b = 57.4, rms 0.8 px. Depth grows
  linearly at 4.87 m/s (the prior). The bike moves almost exactly along the optical axis (its image x converges to 960 and its lateral
  X ≈ -0.43 m at t = 1 and t = 2), so f*H = A*4.87/33 = 2948-2961.
- Focal length (`manhole.py`, `manhole2.py`): the manhole cover is a circle on the road, averaged over frames 70-98. Outer ring: width 208.2,
  height 33.9 (rows 823.0-856.9). Inner disc: width 174.5, height 27.15 (rows 826.1-853.2). For a level camera, f = width * (v_mid - h) / height.
  This gives 1861 from the outer edge and 1945 from the inner one. The difference comes from the rim's relief. A rim-plane model that uses only
  the unbiased edges (outer far edge, inner near edge, both widths) gives f = 1899, and the centre-line estimate is 1900. I took
  f = 1900 ± 45 (horizontal field of view 54°). So H = 2961/1899 = 1.56 m.
- Check against depth_info: with f = 1900, the bike origin at about ground level and about 0.66 m ahead of the rear tyre contact
  reproduces d = 14.11 / 18.95 m if the speed is 4.864 m/s, which is within the rounding of 4.87.
  Taken alone, depth_info gives Yo = 1.74 ± 0.16 m (that is, f = 1700 ± 150), which is consistent but much less precise.
- Curb height (`curb.py`, `lcurb.py`, crops): on the left curb, the block joints on the shaded vertical face span 25 px with the foot at
  row 854, and 22 px with the foot at row 822, so c/H ≈ 0.078. On the right curb, the lit (tan) face strip, after removing blur, gives
  c/(H-c) ≈ 0.065-0.07. I took c/H ≈ 0.065 (c ≈ 0.10 m).

## Answer
H - c = 1.559 * 0.935 = 1.458 m, so the height is 259.3 * 1.458 / 126.8 = **2.98 m**. The booth's depth is about 22 m.

## Second route (independent of the curb)
The pedestrian walks on the same sidewalk. I fitted their lowest-shoe track with v = h + A'/(frame+b'), giving b' = 307,
and the bbox-height fit agrees (b' = 305). The pedestrian's speed comes from Δd = 1.230 m/s in depth_info.
This gives f*(H-c) ≈ 2960 ± 110, so a booth height of 3.19 ± 0.12 m (that route implies c ≈ 0).
The absolute pedestrian depths (19.0 / 20.3 m) do not match the ground plane: the body is at Z ≈ 12.7 m,
so the human origin is offset about 6 m from the body. Only the difference between the two depths was used.
The two routes differ by 7%. I put more weight on the curb measurement, which I could see directly on both curbs.

## Sensitivity and confidence
f ±2.5% and c ±0.04H give about ±5%. If c = 0, the answer would be 3.18 m. My overall confidence is moderate: I expect the answer to be within about 6%.
