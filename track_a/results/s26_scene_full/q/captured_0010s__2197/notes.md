# q_2197 — length of the pendulum string (cm)

The file and the question are both at 24 fps, so frame = round(t*24). The ball track comes from scene/tracks/ball.csv; I checked it on frames 17 and 32 (overlay crops are in frames/). The pivot is at about (638.5, 229) px.

## Route 1: period (uses the prior g = 9.8)
- Period from the turning points (f3 to f32.5, f17 to f46.5) is 29.5 frames = 1.229 s. Damped-sinusoid fits to depth, 1/diam, cx and X give 1.240 to 1.248 s. I used T = 1.235 ± 0.01 s.
- The amplitude is large. Using size-based depth (k = depth*diam_px = 51.3 from the depth_info frames, so the ball diameter ≈ 6.7 cm), the 3D chord between the far turning point (f32) and the near one (f17) is 0.53 m, which makes the full swing about 95° (θ0 ≈ 47–50°).
- Solving self-consistently with T = 2π√(L/g)·2K(sin(θ0/2))/π and sinθ0 = chord/(2L) gives θ0 ≈ 50° and L(pivot to ball centre) ≈ 0.343 m. The physical-pendulum correction is about 0.1 cm.

## Route 2: 3D geometry (depth_info plus f = 763 px)
- I back-projected the ball centres at the 6 depth_info times. The pivot was taken on the ray through (638.5, 229), and I fitted it to be equidistant from those points. Result: pivot distance 1.49 m, L = 0.327 m, residuals ±2 cm (the depth_info values are noisy: f7 and f29 sit at similar phases but differ by 8 cm).
- Using size-based depth for all frames instead gives L = 0.311 m (rms 2.8 cm).

## Answer
- Pivot to ball centre: ≈ 0.33–0.34 m. String only (pivot to ball top, i.e. minus r ≈ 3.4 cm): ≈ 0.30–0.31 m.
- The name "length of the string" is ambiguous between these two readings (string only, or pendulum length to the centre). I answered 31.5 cm, between the two, which is within about 5–7 % of either.
- Confidence: moderate. The main uncertainty is that ambiguity; the measurement itself is good to about ±4 %.
