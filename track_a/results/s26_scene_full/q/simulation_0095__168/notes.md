# Q168: height of the plane (m)

- This is a 2D simulation, so one metres-per-pixel scale comes from the prior: car acceleration = 10 m/s^2. The file fps and question_fps are both 24.
- **Car pixel acceleration:** a quadratic fit of x(t) over frames 2–71 (from scene/tracks/car.csv).
  - mask centroid: 292.15 px/s^2 (residual 0.17 px)
  - bbox centre: 290.8 px/s^2
  - frames 10–71 only: 292.1 / 290.3 px/s^2
  - Value used: 292.15 px/s^2, giving a scale of 10/292.15 = 0.03423 m/px.
- **Plane pixel height:** fin top to engine-nacelle bottom. I re-measured it with ph.py at thresholds 15 and 30 on frames 8, 10, 12 and 14: y 170–497, which is 328 px (327 at threshold 30). The value is stable across frames. A visual check on frames/f10.png confirms that the fin top and nacelle bottom are the extremes.
- **Answer:** 328 x 0.03423 = **11.23 m**.
- **Second route:** using the bbox-centre acceleration (290.8) gives 11.28 m, a 0.4% difference. The real A320 height is about 11.8 m, which is plausible.
- **Confidence:** high, about 2%.
