# Q1323 – height of the turning yellow car (taxi)

Answer: **1.69 m**. This is the vertical extent of the world-space AABB, from the tyre contact with the ground (z = 0) to the top of the TAXI roof sign.
File fps = question fps = 24. Frames 14 / 38 are the depth_info times (0.58 s / 1.58 s).

## Camera calibration (static camera, principal point at the image centre)
- Horizon: the forward-road curbs (`curbs.py`) meet at VP1 = (809.6, -195.2). The far-right and near-right curbs are one line.
- Vertical vanishing point (`poles.py`): I fitted 5 poles (lamps and traffic lights). The nadir is at (1074, 6908); all 5 lines pass within ±12 px of it, so roll is about 0 and cx is about 1080.
- f = sqrt((540+195)(6908-540)) = **2164 px**. Pitch is 18.8°.
- Cross-check from the cross-street curbs' vanishing point (`crosscurb.py`), assuming the streets are orthogonal: f = 2090–2155. This depends on which part of the curb is used.
- Cross-check from depth_info (`headings.py`): the pedestrian's displacement between f14 and f38 is parallel to the cross street when f is about 2240. The cyclist's path follows the road direction at every f, so it does not constrain f.
- Camera height from the pedestrian's depths (`camh.py`, `combined.py`): I put the pelvis at its depth and dropped a vertical to the feet ray. This gives h = 8.09 and 8.11 m (f14, f38) at f = 2164. The cyclist gives 7.91 m, but its wheel-bottom pixel is noisy.

## Measurement (`taxi_side.py`, `tyre_bot.py`, `height_side.py`)
- Frames 58–63: the taxi is side-on and unoccluded. Later frames are not used because the trash can corrupts the front tyre.
- Tyre bottoms come from the transition from dark tyre to lighter shadow: rear tyre y ≈ 477–479, front tyre y ≈ 468–470. The sign top comes from a background-difference mask (y = 328–330).
- I intersected the tyre bottoms with the ground plane, which gives the near-side line. The heading comes out at 8°, which matches the cross-street direction (6.8°). The wheelbase is 2.95 m and the length about 5.4 m, so the car is at real-world scale (it looks like a Crown Victoria).
- The sign sits on the car's centreline, 0.9 m (±0.1) behind the outer tyre line. The top-of-sign ray meets that vertical plane at **H = 1.700 ± 0.006 m** over the six frames (f = 2164). A ±0.1 m change in the offset moves H by ±0.025 m.

## Second route: the taxi's own depth_info (`taxi_origin_check.py`, `combined.py`)
- I placed the origin at the car centre: at height H/2 and 0.3 m ahead of the sign, below the sign-top ray at f14 and f38.
- The predicted camera distances come out 1.3 % (f14) and 1.1 % (f38) larger than the given 23.744 m and 27.006 m. Rescaling by the taxi depths gives H = 1.68 m. With the origin directly below the sign the predictions match to 0.3 %, which gives 1.70 m.
- The van's acceleration is only loosely consistent. With a = 4 and v0 ≈ 0, the path from f14 to f38 should be about 4.33 m, but depth_info plus image motion gives 4.15 m at f = 2164. The van's origin image point is uncertain, so I did not use the van to set f.

## Sensitivity and confidence
H is roughly proportional to 1/f:

| f (px) | H (m) |
|---|---|
| 2080 | 1.76 |
| 2164 | 1.70 |
| 2240 | 1.65 |

Combining the routes (pole/horizon f, pedestrian camera height, taxi-depth rescaling) gives H = 1.68–1.70. I answer **1.69 m**. My confidence is about ±4 %, and the main uncertainty is the focal length.
