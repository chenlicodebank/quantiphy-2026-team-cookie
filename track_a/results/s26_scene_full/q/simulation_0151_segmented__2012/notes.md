# q_2012: speed of the yellow car at t = 1 s (m/s)

The question fps (24) is the same as the file fps (24), so t = 1 s is frame 24. Speed = |p(24) - p(23)| x 24.

## Approach
The car is a rigid body translating parallel to the image plane. Its apparent size and image row stay constant.
Every point of the car therefore has the same world speed. A point at depth Z moves V·f/Z px per frame. So if
the pixel motion of a near-side feature is divided by the pixel size of the near-side tyre (same depth), the
result is in tyre diameters. That ratio gives the metric speed directly from the prior (tyre = 0.764 m), and
needs neither f nor the depth.

The car's silhouette ends (nose and tail) move only ~90–92 px/frame (scene/ track). This is because they are
near the car's centre plane, ~7.5 % farther than the near side. Mixing their pixel speed with the near-tyre scale
would be inconsistent, so I used near-side features only.

## Measurements (scripts in this folder)
- `rim_fit.py`: sub-pixel circle fit to the light rim edge of both near-side wheels in frames 15–32 (~320 edge
  points each, very stable).
  - Front hub x: f22 824.97, f23 728.19, f24 629.91, f25 530.28.
  - Rear hub x: f22 1534.6, f23 1437.78, f24 1339.46, f25 1239.83.
  - **Step 23→24: front 98.28 px, rear 98.32 px.** Neighbouring steps: 96.8 (22→23) and 99.6 (24→25), so the
    speed is smoothly increasing.
- `hub_track.py`: door template matching (near-side body panel) in a second, independent route gives a 23→24
  shift of 97.9 px. This agrees within 0.4 %.
- `tyre_radius.py`: radial sub-pixel edge from the rim centre to the tyre/white boundary over 20–160° below the
  hub, frames 15–32.
  - Front tyre: d = 182.3 (bottom) / 183.4 (median) px.
  - Rear tyre: d = 183.7 / 184.0 px.
  - Adopted value: **183.3 px**, with about ±0.7 %.
  - The cruder fits in `wheels_fit.py` / `tyre_lower.py` gave 181–198 px. They were biased by the wheel-well
    shadow and by the cy/r degeneracy on a partial arc, so I did not use them.

## Result
- Scale at the near side: 0.764 / 183.3 = 0.004168 m/px.
- V = 98.3 px/frame x 0.004168 x 24 = **9.83 m/s**.

## Checks
- Wheelbase: 700 px x 0.004168 = 2.92 m. The car's centre-plane length is 1153.5 px x 0.004168 x 1.075 ≈ 5.2 m.
  That is a large car, but consistent with its large 0.764 m tyres.
- depth_info (11.38 m to the left front tyre at t = 0.5 s) is not needed by this ratio method. The left tyre is
  on the far side, since the car drives to screen-left. It is consistent with a near-side depth of ≈ 9.8 m and
  f ≈ 2350 px (HFOV ≈ 44°). The ratio of near-side to silhouette speed (≈ 1.075) is also consistent with a car
  half-width of ~0.8 m at that depth.

Confidence: high (≈ ±2 %).
