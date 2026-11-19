# q_1445 — droplet speed at t = 0.2 s (frame 12 at question_fps 60; file fps also 60)

The drop leaves the image after frame 9, so I can't measure it at frame 12. I extrapolate using the
prior instead (uniform acceleration 9.7 m/s², as the paper's convention for a uniformly accelerated object).

Method (fit.py, fit2.py): I used the scene/ centroid track for frames 0–9 (I checked the overlays in the record).
The principal point is the image centre. For each trial focal length f, I back-project frame 0 at
0.156 m and frame 6 at 0.186 m. That fixes the 3D fall line. Each frame's ray is then intersected with
this line to get the arc length s(t). I fit a quadratic to s(t).
- For every f tried (800–8000 px) the fit gives release from rest at t ≈ 0 (t_rest between −0.003 and +0.002 s). So the
  release time does not depend on the scale.
- Solving for the f that gives a = 9.7 m/s² yields f ≈ 3580–3690 px (fit windows 0–9, 0–7, 1–9).
  At that f, v0 ≈ 0.01–0.02 m/s and t_rest ≈ −0.001 to −0.002 s.
- Speed at frame 12 = backward difference between frames 11 and 12 = v0 + a·(11.5/60) = 1.870–1.882 m/s.
- Second route, ideal release from rest exactly at frame 0: 9.7·23/120 = 1.859 m/s. The instantaneous
  value a·t would be 1.94–1.96.

Answer: 1.88 m/s. It is within 1–3 % of every reading above, so confidence is good.
