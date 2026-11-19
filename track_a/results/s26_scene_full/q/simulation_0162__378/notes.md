# Q378: acceleration of the ball at t = 1 s (frame 24)

The video is a 2D sim at 24 fps. The file fps and question_fps agree, so t = 1 s is frame 24. The camera is static and the ball rolls horizontally.

**Scale.** The prior gives a ball diameter of 0.21 m. The ball measures 81.5 px across: the record's median circle fit is 81.6, and the vertical mask extent is 607–688. That gives 0.002577 m/px.
Unit conversion: a in m/s² = a in px/frame² × 576 × 0.002577 = a × 1.484.

**Tracks.**
- The record's `cx`. I checked it on the frame-24 crop: the ball spans x ≈ 109–192, centre ≈ 150, and the record has 150.3.
- My own sub-pixel edge tracker (`edge.py`). It takes the median midpoint of the left and right edges of the background difference in rows 652–683. It agrees with the record to within about 0.5 px.

**Kinematics.**
- The per-frame speed rises steadily, about 16.5 px/frame at frame 24 and 28 near the end, so the acceleration falls over time.
- The per-frame steps also wobble with a period of about 10–15 frames. That matches the ball's rotation period (circumference ≈ 256 px) and the chord-width wobble, so it is a texture artifact. The underlying acceleration has to be smoothed over at least one rotation.

**Estimates of the acceleration at frame ≈ 23.5** (the convention's speed(24) − speed(23)):

| Method | Script | px/frame² |
|---|---|---|
| Central-difference speeds (k = 5–7), quadratic trend in speed over frames 23–42/50 | `smooth2.py` | 0.42–0.46 |
| Linear trend in speed, which underestimates because the acceleration is falling | `smooth2.py` | 0.30–0.38 |
| Global model with an exponential approach to terminal speed (τ ≈ 24–45 frames), fitted over several windows | `fit2.py` | 0.42–0.49 |
| Local quadratic position fits over frames 17–31 | `fit.py` | 0.36–0.39 (window affected by edge-cut frames and the wobble) |

**Adopted value.** 0.43 px/frame² × 1.484 ≈ **0.64 m/s²**. The plausible range is 0.56–0.69, so confidence is moderate (about ±10 %).
