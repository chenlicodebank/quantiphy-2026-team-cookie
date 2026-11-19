# q_3000 — ball distance from desk at 0.40 s (prior: g = 9.8 m/s^2)

Script: `measure.py`. It uses the ball track from scene/tracks/ball.csv (centroid, checked) and measures the desk edge itself.

- Time: fps = question_fps = 50, so t = 0.40 s is frame 20. The camera is static (scene record).
- Desk (grey box) top edge: the strongest vertical gradient at x = 450–600 in frame 20 is at **y = 970.5 px** (a visual read gives about 972).
- Ball at frame 20: centre y = **606.1 px**. Radius 38 px (unblurred diameter 76), so the bottom is at about 644.
  - Centre to desk: 364.4 px. Gap from ball bottom to desk: 326.5 px.
- Scale from gravity:
  - The clip drops one source frame every 5th output frame (steps double at frames 7, 12, 17, 22, 24), so it is a 60 fps source shown at 50 fps.
  - A quadratic fit on the corrected 60 fps time base gives a = 8887 px/s^2 for frames 8–23 (rms 0.56 px), and 8961 for frames 7–23.
    - Within-segment fits (no missing frames) at 60 fps give 8871 and 8789. These agree.
  - This gives a scale of 9.8/8887 = 1.103e-3 m/px. The ball diameter then comes to 8.4 cm, which is plausible.
  - Second route: a naive fit with the frames taken as-is at 50 fps gives 9473 px/s^2, so the scale is 1.035e-3 m/px (6.5% smaller).
- Candidates:
  - Physical scale: centre 0.402 m, gap 0.360 m.
  - As-is 50 fps scale: centre 0.377 m, gap 0.338 m.
- Answer: **0.375 m**. It is a compromise between the centre-to-desk and gap readings and between the two scale conventions, within about 7% of the three most likely readings.
- Confidence: moderate. The pixel measurements are good to about 1%; the uncertainty is in the convention used.
