# Q1273: height of the turning yellow car (taxi)

Answer: **1.58 m**

The file runs at 24 fps and question_fps is also 24. t = 0.58 s is frame 14 and t = 1.58 s is frame 38.

## Focal length (from the prior: the white van accelerates at 4 m/s²)
- The van's 3D positions at f14 and f38 come from the given depths (45.52 m and 43.95 m) back-projected along the pixel rays. This gives a straight 3D line. Every other frame's ray is intersected with that line to get the path distance s(t). A quadratic in t is fitted, and f is solved so that a = 4 m/s².
- Pixel tracks used:
  - `win_track.py` / `win_fit.py`: sub-pixel edges of the van's three tan side windows.
  - `van_track2.py` / `focal_van3-5.py`: a roof/window template.
  - `focal_van.py` / `focal_van6.py`: the record's bbox centre.
- Results with v0 free (the fit is clearly better than forcing v0 = 0; v0 comes out at about 0.12 m/s):
  - window edges: 2200, 2210, 2163, 2234 and 2148 px
  - record cx: 2164 px
  - template: 2237 px
  - Forcing v0 = 0 gives about 2240–2290 px.
- **Chosen f = 2200 px (±2–3 %).**

## Ground plane / horizon (`ground.py`)
- Pedestrian feet and cyclist wheel bottoms at f14/f38, with their given depths, give a horizon at v_h ≈ 475 and f·h ≈ 6220 px·m. So the camera points slightly down: the record's horizon of 535 is wrong.
- The taxi's own wheel contacts at f14 agree: the near-side mean of 635.5 px, corrected from the near side (about 0.8 m closer) to the centre depth, gives about 632, against the model's 631.7.

## Taxi pixel height
- **f14:** the roof-sign top is at y ≈ 545.0, from the saturation and value edge in `sign_edges.py`. The ground row at the origin's depth is ≈ 632.0. That gives 87.0 px. The depth along the optical axis is Z = 40.10 × cos factor = 39.83 m.
  - H = 87.0 × 39.83 / 2200 = **1.575 m**
- **Second route, f38 (front view):** the sign top is at 550.5 and the ground row at the centre depth is 646.6, giving 96.1 px at Z = 36.35.
  - H = 96.1 × 36.35 / 2200 = **1.588 m**
- The ground-model form gives the same result: H = (f·h − (v_top − v_h)·Z) / f, which is 1.566 m at f = 2205.

## Result
- Mean ≈ 1.58 m.
- Uncertainty: about ±3 % from f and about ±1.5 % from the pixel edges.
- Sanity check: a Crown Victoria taxi with its roof sign is about 1.5–1.7 m tall.
- The record's taxi bbox height (100 px at f14) includes shadow and the van/sign confusion, so it was not used.
