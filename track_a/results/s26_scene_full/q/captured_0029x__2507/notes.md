# q_2507 – distance travelled by the tennis ball until it hits the whiteboard (cm)

File fps = question fps = 24. Hit at t = 1.24 s -> frame 30 (the farthest point: minimum apparent diameter, image-y
reversal; afterwards the ball comes back toward the camera and rolls left). The whiteboard itself is masked out (black).
Interpretation: path length (sum of frame-to-frame 3D centre displacements) from t = 0 (ball held) to frame 30.

## Method
- Ball centre (u,v) and fitted diameter from scene/tracks/ball.csv (checked visually at frame 30: ball ~43-44 px wide,
  record 41.4 px; centre matches).
- Lab camera: f = 0.5959 x 1280 = 762.8 px, principal point (640,360).
- Depth per frame from apparent size Z = k * f * 0.067 / diam_px, with k calibrated on the given depths:
  k = 0.964 (t=1.00, 0.901 m), 0.927 (t=1.24, 1.144 m), 0.934 (t=1.6, 1.027 m); used 0.927-0.964, mean 0.94.
  (t = 1.00 s depth is written "0.901s" in depth_info; read as metres.)
- Back-projection P = ((u-cx)/f, (v-cy)/f, 1) * Z. Noise control: held phase (0-16) Savitzky-Golay 7-pt smoothing;
  throw phase (17-30) depth forced monotone (isotonic fit), frame 18 dropped (motion blur inflates diameter to 107 px).
  Nothing smoothed across the whiteboard impact (frame 30).

## Results (smooth_path.py)
- path 0-30: 85.0 (k=0.927) / 86.2-86.5 (k=0.94) / 88.4-91.3 (k=0.964) cm
  = held/wind-up 0-16 ≈ 4.5 cm + throw 16-30 ≈ 80.5-86.6 cm.
- Straight-line displacement start -> hit ≈ 70 cm (lower bound).
- Raw unsmoothed per-frame sums (measure.py) 84-107 cm – inflated by depth-from-size jitter in blurred frames.

## Second route
Pinning the given depths at frames 24 and 30 instead of using size-based depth there gives 85.0-91 cm; consistent.

Answer: 85 cm (k anchored on the hit-time depth 1.144 m). Confidence moderate (±8%): depth for frames 0-23 rests
on the ball's apparent size; the reference's own start frame and depth noise are unknown.
