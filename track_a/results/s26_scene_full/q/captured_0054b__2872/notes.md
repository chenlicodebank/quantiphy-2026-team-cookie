# q_2872 – velocity of the green ball at 1.0 s (frame 24)

The green ball is the yellow-green tennis ball, called `yellow_ball` in scene/. The orange ball is the basketball.
The file and the question both run at 24 fps, so t = 1.0 s is frame 24. f = 0.5959 x 1280 = 762.8 px, principal
point (640, 360).

## Prior check (orange ball, frame 12, depth 2.24 m)
I back-projected the basketball track and fitted a linear velocity over ±2 frames around frame 12:
- 2.29 m/s with depth from its apparent size;
- 2.19 m/s with constant depth;
- prior: 2.21 m/s.

The ±2-frame smoothing window includes the 11→12 skipped capture, and the prior was evidently computed that way
too. The convention (a ≥5-frame smoothed 3D velocity) is reproduced to within about 4 %.

Note: the depth_info distances for the orange ball (2.24 m at 0.5 s, then 1.81 m at 1.0 s) do not fit its
shrinking image (75 px, then 63 px). The given depths are noisy sensor values.

## Green ball
The pixel track (scene/tracks/yellow_ball.csv, frames 20–34) looks right on crops (`yellow_crops.png`). The ball
is heavily motion-blurred, so I used the minor-axis width as its diameter. Depth is 1.331 m at frame 24 (given).
The answer depends almost entirely on how fast the depth grows: the ball is thrown away from the camera.

| Route | Depth model | Speed at frame 24 |
|---|---|---|
| A (`vel.py`) | Constant 1.331 m | 1.82 m/s (lower bound: ignores the motion in depth) |
| B (`vel.py`, `vel2.py`) | Depth ∝ 1/diameter, anchored at 1.331 m, fitted over several windows | 2.33 – 2.81 m/s. Most fits are 2.4–2.6, with depth growing 0.065–0.09 m per frame. Blur inflates the early diameters, which probably biases this route high. |
| C (`projfit.py`) | Ballistic 3D fit: g = 9.81, camera tilt fitted, distance at frame 24 fixed to 1.331 m, fitted to the pixel track | 2.01 – 2.17 m/s (6 windows). Tilt 42–56°, rms 1.6–3.5 px, depth rate about 1.1–1.5 m/s. The fitted ball diameter is 0.067–0.071 m, which matches a real tennis ball, so this route is self-consistent. |

## Answer
**2.15 m/s.** This leans on route C (physically consistent), allowing a little for route B.

Confidence: moderate, about ±10 %. The main uncertainty is the depth rate of a blurred ball, and the reference's
own per-frame sensor depths are unknown.
