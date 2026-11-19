# q1314 — height of the traffic light (simulation_0064)

File fps = question_fps = 24, so no time-base conflict. The scene has four identical traffic signals, one on each corner.
I measured the two near ones (left: pole base about (435,571), sign apex y 65.5; right: base about (1887,566), sign apex y 64).
"Height" here means the full asset: from the pole base on the sidewalk to the top of the triangular sign on top.

## Camera model (calib.py, poles.py, vvp.py, final.py)
- Vertical vanishing point: I fitted the axes of both near poles with sub-pixel dark-ridge fits (rms 0.4 px). The lines
  meet at (1063, 7887). Its x is close to cx=1080, which fits a camera with no roll. Building edges found by Hough
  give 7700–8150, so I used yv ≈ 7950 ± 200.
- Horizon / street vanishing point: y ≈ -121, from the scene record's curb lines (uncertain between about -187 and -80).
- Focal length from orthogonality: f² = (cy - y_h)(yv - cy) gives f ≈ 2210 px (hFOV ≈ 52°). Pitch ≈ 16.7° down.
- Camera height from depth_info: the pedestrian at t=1.58 s (f38) has pelvis pixel (332,245), D = 38.722 m and feet row 298.
  I placed the pelvis in 3D and intersected the vertical line below it with the feet ray, which gives H = 6.64 m.
  The cyclist at f14 (D = 33.998 m, wheel bottom row 331) gives an independent H = 6.65 m, which agrees.
- Traffic light: I put the pole base on the ground plane and found the height on its vertical at which the apex row
  projects. Result: left 4.968 m, right 4.968 m.

## Checks
- The two traffic lights measured independently agree to 1 mm.
- The camera height from the pedestrian and from the cyclist agrees (6.64 vs 6.65 m).
- Prior (white van, a = 4 m/s²): its displacement from f14 to f38, reconstructed from the depths, is 4.12–4.14 m.
  Constant acceleration from rest predicts 4.17 m (start at frame 1) to 4.33 m (start at frame 0). This is consistent,
  but it hardly depends on f, so it does not constrain f.
- Sanity check: the pedestrian comes out about 1.8 m tall.
- Sensitivity: the vertical vanishing point over 7700–8100 gives 4.93–5.04 m. The horizon over -160 to -100 gives ±0.04 m.

Answer: **4.97 m**. Confidence: good, about ±3%.
