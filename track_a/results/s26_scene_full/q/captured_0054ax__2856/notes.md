# q_2856 – soccer ball displacement 1.0 s → 1.4 s (captured_0054ax)

Answer: **0.545 m** (range of credible variants 0.515–0.56).

Time base: question_fps = file fps = 24. 1.0 s → frame 24, 1.4 s → round(33.6) = frame 34.
Camera: f = 0.5959·1280 = 762.8 px, principal point (640, 360). Positions P = z·((u−cx)/f, (v−cy)/f, 1)
(the lab method card treats the given depth as z).

## Which ball is which
depth_info gives depths for the orange ball (basketball), a "white" ball and a "green" ball at 3.04–3.07 m.
At t = 1.0 s the two small thrown balls (pale grey/white and yellow-green) are just leaving the standing
person's hands, about 3 m away. The soccer ball (white with black patches, ≈70 px) is near the crouching person
at about 2.4 m. So "white"/"green" are the small balls: **no depth is given for the soccer ball**, and it has to
come from geometry.

## Measurements (scripts in this folder)
- `spherefit.py`, `spherefit_bb.py`: fit a projected-sphere silhouette (a cone of angular radius β around the
  centre ray, plus a motion-blur segment) to the ball edge points that border the green background. Lower arc
  only while the hand covers the top of the ball. Median residuals are 0.4–0.9 px.
  `shapetest.py` confirms the image follows pinhole geometry: the soccer-ball silhouette is an ellipse with axis
  ratio 1.20–1.24 at rest (pinhole prediction 1.226) and 1.35 in motion (prediction 1.29–1.31 plus blur), with
  its long axis roughly radial.
  - Soccer-ball centre pixel: f24 (149.3, 609.1), f34 (67.7, 679.8). The silhouette centres (148.7, 609.5) and
    (66.7, 680.4) change the result by less than 1 mm.
- Basketball: R = 2.3557 / (z/R at f12 = 21.07) = 0.112 m. Its sizes agree with the given depths within
  about 1–2 % (f12–f22). Prior check: the basketball speed is about 1.9–2.0 m/s around 0.5 s; the prior says
  2.21 (the capture has frame-timing jitter, and the reference smooths clicked centres).
- Floor plane (`floorz.py`, `floor2.py`, `final.py`): fitted to the basketball's rolling centre line from the
  given depths (2.3557 m at f12, 1.81 m at f24, interpolated), offset down by R_b. The camera is about 0.90 m
  above the floor and nearly level (pitch about 0.6°). Checks: it puts the basketball's rest position at
  z = 2.72 m, against 2.69 m from its size; and the standing person comes out 1.64 m tall at 3.7 m.
- Soccer-ball radius from floor + size together: 0.085 m (rest frames) and 0.081 m (free-rolling frames),
  so D ≈ 0.165 m (a small ball). I used R = 0.084 m; the answer changes by only ±2 mm over 0.081–0.087.

## Result (primary route: floor plane + centre pixel)
z24 = 2.415 m, z34 = 1.895 m. P24 = (−1.554, 0.792, 2.415), P34 = (−1.422, 0.793, 1.895).
**Displacement = 0.537 m** with roll 0. Sensitivity to camera roll: −1° → 0.515, +1° → 0.560.
The standing person's silhouette leans 1–3.7° (top to image-right), which suggests roll ≥ 0, so I answer 0.545.
Using front-surface depth instead of centre depth adds about 2 mm. The per-frame floor path is smooth: steps of
about 0.05–0.06 m per frame, about 1.3 m/s while rolling freely.

## Second route (sizes only) and why it disagrees
z = R·(z/R) from each frame's fitted size gives z24 ≈ 2.33 and z34 ≈ 1.94, so the displacement is
0.38–0.40 m. This route is much noisier: per-frame steps jump 0.03–0.36 m, and the path length over 24→34 is
1.27 m against a net 0.39 m. The cause is a size bias of about 1.5 px between frame types. Frames where the hand
is on top or the ball sits on the floor imply R = 0.085–0.088 m, while the blurred free-rolling frames imply
0.079–0.083 m. Because the motion is mostly toward the camera, this bias swings Δz strongly. Making the two routes
agree would need a roll of about −4°, which is opposite to the person-tilt evidence. The floor route only uses the
centre pixel, and its floor plane was checked on the basketball, so I trust it more.

Confidence: moderate. The main uncertainty is the soccer ball's unknown depth (camera roll ±1° → ±4 %), plus
whatever the reference's sensor depth was at the image corner at 1.4 s.
