# q3179 – average ball speed 1.40–2.00 s (frames 42–60, 30 fps)

Time base: file fps = question_fps = 30. Frames 42 (apex) to 60 are free fall (release 22, catch 64); no contact in window.

Scale from prior (g = 9.8 m/s^2): parabola fit to ball centre y (scene/tracks/ball.csv, checked centres are on ball per record) over free flight.
- frames 23–63: g_px = 2001 (stab) / 2000 (raw) px/s^2; 25–61: 2006; 28–58: 2016.
- rise only 24–45: 2012–2019; fall only 40–62: 1942–1949 (asymmetry consistent with air drag, ~±4 %); whole-flight fit averages it out.
- scale = 9.8/2001 = 0.004898 m/px.

Speed: mean of per-frame (forward-difference) speeds frames 42→60:
- stabilised coords 2.866 m/s; raw coords 2.789 m/s.
- second route: derivative of fitted parabola (linear x) averaged over window: 2.873 (stab) / 2.799 (raw); displacement/time 2.86 / 2.78 (motion is near-straight down).
- With fall-only g (1942) the value would be ~2.95; backward-difference convention gives ~3.1–3.2 (window shifted by one frame during acceleration).

Answer: 2.83 m/s (midpoint of raw and stabilised, forward difference, whole-flight g). Confidence: moderate (±5 %).
