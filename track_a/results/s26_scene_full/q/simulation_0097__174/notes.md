# q174 – plane speed at 0.3 s (prior: car acceleration = 10 m/s^2)

2D scene, fps 24 (= question_fps). t=0.3 s -> frame 7 (plane nose visible, partly cut by left edge).

Script: fit.py (uses scene/tracks, which were checked: plane = upper jet flying +x, car = lower pickup accelerating -x).

- Car pixel acceleration: quadratic fit of mask centroid x(frame), frames 1–40: a = 0.3706 px/frame^2
  (frames 0–40: 0.3713; 2–40: 0.3703; bbox centre: 0.369; mean 2nd difference 0.375). Use 0.370 px/f^2
  = 213.3 px/s^2. Scale = 10 / 213.3 = 0.04689 m/px.
- Plane pixel speed: constant; linear fit of nose x1 (frames 3–38) 53.41 px/frame, of tail x0 / full bbox centre
  (frames 18–38) 53.40 px/frame; frames 6–8 nose: 198, 251, 305 (Δ 53, 54). -> 1281.7 px/s.
- Speed = 1281.7 x 0.04689 = 60.1 m/s.

Second route: ratio form v = (53.40/0.370)/24 x 10 = 60.1 m/s; with the bbox-based acceleration 0.369 -> 60.3.
Plausibility: plane 800 px x 0.0469 = 37.5 m long (airliner ~37 m), car 121 px -> 5.7 m (Cybertruck 5.7 m). Consistent.
Confidence: high (~1–2 %).
