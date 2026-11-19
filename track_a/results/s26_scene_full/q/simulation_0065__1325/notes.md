# Q1325 – diameter of the bicycle wheel (simulation_0065)

Answer: **0.68 m**

The file and the question both run at 24 fps, so frame = round(t*24). t=0.58 s is frame 14 and t=1.58 s is frame 38.

## Focal length (3D clip, unknown f)
- Road vanishing point, from my own fit of the two far-road curbs in the median background (`vp.py`): (807, -194.5).
- Cross-street vanishing point, from lines fitted to the far-right curb (slope -0.02646) and the near-right curb
  (slope -0.03921) (`curbs.py`): they meet at (20059, -187.6). That y matches the road VP's y, so roll is about 0.
- The two road directions are orthogonal, which gives f^2 = -(v1-c)·(v2-c), so **f ≈ 2156-2190 px** (`focal.py`).
  The short far-left curb gives 1995 and is treated as an outlier. I used f = 2170.
- Check with the depths: the pedestrian's 3D displacement between f14 and f38 (from depth_info) is perpendicular to the
  road only at f ≈ 2200, which fits a walk along the cross street (`calib.py`). The pedestrian's height comes out
  constant at f ≈ 2000-2200 (`horizon.py`).
- The van-acceleration prior (4 m/s²) is only weakly sensitive to f with the bbox-centre proxy: it gives 4.0 at f ≈ 1500
  and 3.8 at f ≈ 2170 (`vanacc.py`, `vanground.py`). I treat it as a loose consistency check only.

## Wheel measurement
- The bike is seen from directly behind, so the rear wheel appears edge-on as a thin vertical line. For a disc whose
  plane contains the line of sight, the projected vertical extent is the full diameter.
- Bottom: the end of the thin tyre line on the road. Top: the first non-background row below the saddle, where the
  background gap between the seat stays/legs closes (`colprof.py`, `wheelscan.py`, `bottom.py`; crops in `frames/`).
- I got usable measurements in 25 frames (0-8 and 19-37). Pixel height × depth stays constant at 1.50±0.04 ×10³ px·m,
  so it is a rigid feature that scales with the given depth.
- 3D conversion (`diameter.py`): the bike origin is placed by back-projecting the f14 and f38 refs with the given depths
  and assuming constant velocity. The rear-wheel centre is set 0-0.5 m behind the origin along the road. A unit circle
  in the vertical plane along the road is projected, and D = 2·h_px / (pixel extent of the unit circle).
  - f = 2170: median D = 0.675 (wheel 0.5 m behind origin) to 0.689 (wheel at origin), sd 0.016 across frames.
  - f = 2000 → 0.73-0.75; f = 2300 → 0.64-0.65.
- The depths at f0-8 and f19-37 are interpolated or extrapolated linearly between the two given depths. The bike moves
  at an almost constant speed (fitted acceleration ≈ -0.1 m/s²).

## Second route and confidence
- The frames in two separate windows agree: 0-8 give a mean of 0.67, 19-37 give 0.68.
- A real-world sanity check also fits: a 0.68 m wheel is a normal adult bicycle wheel (about 26-28 inch), and the
  pedestrian comes out about 1.85 m tall at the same f.
- Main uncertainties:
  - f, about ±5%.
  - Whether the top edge is the tyre or a fender/brake just above it. That would make the answer up to about 3% too
    large.
  - Where the rear wheel sits relative to the bike origin, about ±1%.
- Confidence: moderate, roughly ±7%.
