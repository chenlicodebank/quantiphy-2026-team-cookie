# q3102 – ball diameter (cm), prior g = 9.8 m/s^2

Time base: file fps = question_fps = 30, no re-timing issue.

Scale from gravity (fitg.py): quadratic fit of ball centre y vs t over free flight frames 36–60
(after release at 35, before bounce at 61), from scene/tracks/ball.csv (clean masks, ±1 px).
- raw y: 2a = 3729 px/s^2 (rms 0.6 px); camera-compensated y (bg0): 3713 px/s^2.
- sub-windows: 36–48 → 3813–3823, 48–60 → 3729–3749, 38–58 → 3694–3708.
- Adopted g_px ≈ 3715 px/s^2 → scale = 9.8/3715 = 2.638 mm/px.
  (Implied g with 30 fps gives a basketball ~24–25 cm: physically consistent.)

Ball pixel diameter (diam.py + record): at apex frames 42–50 (vertical velocity ≈ 0, blur is horizontal
only) the vertical extent is 92.5 px by half-level edge crossings, 93–94 px by mask bbox; ellipse minor
91–92.6. Visual 4x zoom of frame 45: top ≈ 258, bottom ≈ 352 → 94. Adopted 93.5 px.

Diameter = 93.5 × 0.2638 cm = 24.7 cm (range 24.0–25.1 over g-fit windows and 92.5–94 px).
Second route: sub-window g fits (3694–3823) give 24.0–24.8 cm; consistent. Real basketball 24 cm – sanity ok.
Confidence: good (±4 %).
