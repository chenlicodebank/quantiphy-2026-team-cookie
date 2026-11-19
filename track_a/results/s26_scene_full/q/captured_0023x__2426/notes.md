# q_2426 — velocity of the book at t = 1.4 s (cm/s)

Lab video, 24 fps (the file rate and question_fps are the same). t = 1.4 s → frame round(33.6) = 34. f = 0.5959·1280 = 763 px, principal point (640, 360).

## What happens around frame 34 (checked on 3x zoom crops: frames/zoom.png, frames/sheet28_39.png)
- Frames 21–30: the book slides down the board. Board model: a line through the board top (588,356) at 1.201 m and the bottom (584,481) at 0.9555 m.
  It gives d = 1.029 m at frame 29; the given value at t = 1.2 s is 1.02 m, so the model checks out. Speed on the slope is about 0.75–0.78 m/s at frames 29–30.
- Frames 31–32: the book tips off the bottom of the board. Frame 33: it is on the table.
- Frames 33–36: it slides toward the camera at an almost constant 2.3–2.5 cm per frame (about 60 cm/s), then stops at frame 36. Frames 36–48: at rest, d = 0.851 m.
- Depth on the table was measured from the book's front-bottom contact line (dark line; column profile prof.py: v = 496, 500, 504, 508.5, 508.7 for
  frames 33–37) using the table-plane ratio, anchored at rest (d = 0.851). Book geometry at rest: W ≈ 10.7 cm front to back, L ≈ 19.5 cm.
  Cross-check with the book's apparent length (167 / 170 / 175 px at frames 34 / 35 / 37): it gives the same depths within 1 cm.
  Image-based depth: frame 33 ≈ 0.922 m, frame 34 ≈ 0.899 m, frame 35 ≈ 0.876 m, frame 36 ≈ 0.852 m.
  The given 0.857 m at t = 1.4 s is about 4 % below the image value at frame 34; it matches frame ~36 better.

## Velocity (reference convention: forward differences of 3D centres, smoothed over 5 frames)
- A 5-frame centred mean of the forward-difference velocity at frame 34 is (p37 − p32)/5 · 24. It depends only on p32 (tipping off the board, d ≈ 0.945 ± 0.01)
  and p37 (at rest, d = 0.851). The intermediate depths, including the disputed 0.857 at frame 34, drop out.
- |p37 − p32| ≈ 0.098–0.101 m → v(34) ≈ 47–48 cm/s.
- Check against the prior: the same convention gives a(34) = 24·(v35 − v34) ≈ −115·(|p37−p32| − |p37−p33|) ≈ −2.8 to −3.1 m/s².
  That matches the given 2.8 m/s² in magnitude. Requiring exactly 2.8 gives v34 = (0.0733 + 0.0243)·4.8 ≈ 47 cm/s.
- Other conventions, for comparison:
  - raw forward difference at frame 34: 56 cm/s
  - raw backward difference: 60 cm/s
  - 7-frame window: about 44 cm/s
  - mean of scalar step speeds over frames 32–36: about 48–50 cm/s

## Answer
48 cm/s. Confidence is moderate: the result depends on the smoothing convention (±10 %) and on the depth at frame 32.

Scripts: view.py, view2.py (crops), edges.py, bottom.py, prof.py (edge and profile measurements), vel.py, model3d.py (3D positions and velocities).
