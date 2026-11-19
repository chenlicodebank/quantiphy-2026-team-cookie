# Q1355 – diameter of the bicycle wheel (simulation_0067, 3D)

File fps = question_fps = 24. Bike depths given: 14.1413 m (frame 14) and 17.8223 m (frame 38). Between those frames the
bike is only fully visible in frames ~16-35, so I interpolated the depth linearly in time.

## Focal length
- Vertical vanishing point from 8 vertical poles (5 street lamps, 3 traffic-light poles). Each pole axis was fitted in
  code to sub-pixel accuracy (`poles.py`, line rms 0.1-0.2 px). The VP is at (1076, 2628), and leave-one-out changes it
  by only ±7 px. With the horizon / east-west road VP at y ≈ -45 and a principal point at the image centre, this gives
  f = 1103-1106 px. The VP x of 1076 matches the image centre column (1080), which supports a centred principal point.
- Check 1, cyclist pelvis height: back-projecting the pelvis at frames 14 and 38 with the given depths at f = 1105
  gives heights of -6.27 and -6.21 m relative to the camera. They stay constant, as they should for a bike on flat
  ground (`hubdepth.py`).
- Check 2, the prior (white van acceleration = 4 m/s²): with f = 1105, the van tracked on a constant-height plane gives
  an acceleration of 4.3-4.4 m/s² from a quadratic fit over frames 15-60 (`vancheck.py`). That agrees within ~10 %. The
  van check is not very sensitive to f, and the error mainly comes from the van's origin pixel.

## Wheel measurement
- A projected wheel is an ellipse. Its major axis is the diameter seen at right angles to the line of sight, so
  D = major_px × (camera distance of the hub) / f.
- I picked points on the outer tyre edge on 9× crops (`picked.json`, crops made with `crop3.py` / `wcrops.py`) and fitted
  an ellipse centred on the dark hub spot (`fit2.py`). Overlays are in `frames/*_fit.png`.
- Hub distances come from the bike's 3D motion direction. The front hub is about +0.88 m along the track from the
  pelvis and the rear hub about -0.18 m, so the wheelbase is about 1.06 m (plausible). The front hub is therefore ~0.8 m
  farther from the camera than the pelvis.

| wheel / frame | major px (picked) | hub dist m | D (picked) | D (auto-refined edge) |
|---|---|---|---|---|
| front 20 | 46.25 | 15.89 | 0.665 | 0.635 |
| rear 20  | 48.42 | 15.19 | 0.666 | 0.652 |
| front 26 | 43.96 | 16.86 | 0.671 | 0.643 |
| rear 26  | 45.96 | 16.10 | 0.670 | 0.669 |
| rear 32  | 43.46 | 17.00 | 0.669 | 0.722 (refinement jumped onto fender/leg) |

- The picked-point fits are consistent across two wheels and three frames: 0.665-0.671 m.
- The automatic radial edge refinement is noisier. On the front wheels it cuts inside the top highlight, and at rear 32
  it snaps onto the fender.
- Answer: 0.66 m (outer tyre diameter). This is also plausible for a real 26" wheel.

## Confidence
- Moderate-high, about ±4 %.
- Main error sources: tyre edge blur (±0.5 px on ~45 px) and f (±1-2 %).
