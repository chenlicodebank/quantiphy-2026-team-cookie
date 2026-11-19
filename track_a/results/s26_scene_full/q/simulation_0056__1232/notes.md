# q1232: distance between the two streetlights (simulation_0056)

The file runs at 29.9936 fps and question_fps is 30. That makes no difference here because both lamps are static.

## Which lamp is which
Both lamps stand on the left sidewalk.
- The image-left lamp is the near one: tall, behind the hydrant, pole at x≈795. Its depth is 5.201 m.
- The image-right lamp is the far one: pole at x≈850. Its depth is 13.174 m.

The answer is |P_far − P_near|, with P = d · normalize(u − cx, v − cy, f) and the principal point at (1024, 1024).

## Pixel measurements (frames 0 and 60; the lamps are static)
- Far lamp: top of the finial at y≈706. The base bottom is at y≈1265, x≈862, and the base is about 45 px wide. The base-footprint centre is at about (862, 1263).
- Near lamp: top of the finial at y≈239. The base is mostly hidden by the hydrant; its right side is visible at x 856–884 and its bottom at y≈1678 (`lamps.py`, crops in frames/). The centre is at about (828, 1662) after removing the projected base radius.
- Pixel height ratio: 1439 / 559 = 2.57. This is close to the depth ratio 13.174 / 5.201 = 2.53, so it is the same lamp model.

## Horizon and focal length
- `vp2.py` (LSD line segments): 19 segments converge to a vanishing point at (885, 1009) with a median residual of about 1 px. The road-edge line and the building ledges give the same point. The horizon is therefore y≈1009. The scene record's value of (923, 1050) relied on the noisy dashed centre line.
- `ground.py`: both lamp bases must lie on one ground plane. With the horizon at 1009–1014 this gives f≈2500–3450 px and a camera height of about 1.0–1.3 m.
- Independent check on f: the two lamps must have the same physical height, H = H_px · d / |r|.
  - At f = 2400 this gives 2.97 vs 3.04 m; at f = 3450, 2.10 vs 2.12 m. Both agree.
  - At f = 1500 they disagree by 6%. So f is large, about 2400–3500 px.
- The hydrant base gives a camera height about 5% above the lamps' value. Its origin is probably slightly above the ground; this is not used.

## Result
- With the origin at the base, the distance is 8.03–8.09 m for f = 2400–3450. It would be 8.21 m even at f = 1544 (horizon 1030).
- With the origin at the lamp's mid-height, the distance is 7.97–7.99 m for any f (`geom.py`).
- **Answer: 8.05 m.**

Confidence: good, about ±3%. The two routes (ground plane plus horizon, and equal lamp heights) agree on f, and the answer depends only weakly on f.
