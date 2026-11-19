# q_1692 — width of the rock (m)

File rate 25 fps, question_fps 24. The rock does not move, so time does not matter here.

## Measurements (rock_measure.py, mask = min(RGB) < 240)
- Human: its apparent height is about 58–60 px over the whole clip (scene track median 58.4, smoothed value flat;
  frame 25 mask gives y 352–411 = 60 px). The head is pale, so the top may be a little under-segmented. Its depth is
  given as 100.56 / 100.60 m, and its apparent size does not change, so the body really stays at about 100.6 m.
- Focal length f = 59.5 px × 100.58 m / 1.75 m ≈ 3420 px (horizontal FOV ≈ 16°). If 58.4 px is used instead,
  f ≈ 3360 px, a 2 % difference.
- Rock: static. Bbox x 328–957/959 and y 25–310, so it is about 630 px across and 285 px tall. Its right tip just
  reaches the frame edge (only 1–4 px in column 959), so it is essentially not cut off.

## Scale and the main uncertainty
- No depth is given for the rock, and the scene has no ground or occlusion cues: the background was removed and the
  human appears to walk downhill at constant depth, so the terrain is not flat. I therefore placed the rock at the
  human's depth (about 100.6 m).
- At that depth, the rock's left-right extent in the image is 630 × 100.58 / 3420 ≈ 18.5 m (18.9 m with f = 3360).
  Its vertical extent in the image is about 8.4 m, and the top surface is partly visible.
- "Width" means the shorter horizontal extent. Its front-to-back depth cannot be seen. If the image left-right extent
  is the long side, a typical boulder ratio (about 0.6–0.7) gives a width of about 11–13 m. If width means the
  left-right extent in the image, it is about 18.5 m.
- I answered 15 m, between the two readings (about 18.5 m and about 12 m).

## Confidence
Low. The rock's depth is assumed, not measured, and its front-to-back extent cannot be seen. The focal length from
the human is solid (about ±3 %).
