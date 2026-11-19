# q_272 – length of the grey/red (silver, red-striped) car

Prior: black car speed = 26.085 m/s. 2D top-down render, static camera, 24 fps (file fps = question_fps, no re-timing).

## Scale (speed.py)
- Dark car per-frame centre steps from scene/tracks/dark_car.csv (frames 3–45, excluding low-reliability edge frames):
  mean 27.01, median 26.97 px/frame, std 0.33 → speed nearly constant ≈ 26.97 px/frame = 647.3 px/s.
- Scale = 26.085 / 647.3 = 0.04030 m/px.

## Silver car length
- Record: 122 px (averaged aligned crops), clean per-frame masks median ~123 px (120–131, some shadow inflation).
- Own check (prof.py): frame 18, car heading straight down (89.8°); difference vs empty frame 70 along the car
  axis: rear edge at y ≈ 244.5, front edge ≈ 365 (shadow beyond) → ≈ 120.5–122 px. Visual zoom (frames/f18.png)
  agrees: ~243 to ~365.
- Using 122 px: length = 122 × 0.04030 = 4.92 m (121 px → 4.88 m).

## Answer
4.92 m. Sanity: realistic car length. Confidence: good (~2–3 % uncertainty from edge and speed).
