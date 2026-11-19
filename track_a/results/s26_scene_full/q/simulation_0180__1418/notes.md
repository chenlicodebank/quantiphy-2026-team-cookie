# q_1418 – length of the trolley (shopping cart), simulation_0180

The prior: the cart accelerates at 1.507 m/s² from rest at frame 0 (confirmed: x steps of 0, 1 and 2 px in frames 1–3).
depth_info: 12.589 m at t=0 and 12.513 m at t=0.5 s (frame 12). File fps = question fps = 24.

## Focal length and motion (fit_f.py, triang2.py)
- Model: origin P(t) = P0 + (a t²/2)·D. P0 is the frame-0 ray scaled to 12.589 m, D is a free unit vector, f is free.
  I fit the scene-record bbox-centre track (60 frames) with the frame-12 depth as a constraint.
  -> f = 2697 px, rms 0.52 px, |P(12)| = 12.509 m (given 12.513).
  Using the bottom-centre track gives f = 2678 instead.
- Independent check from the floor tiles (vp_hough.py, tiles.py): vanishing points of the tile rows
  (-11136, 223) and of the receding seams (1558, 224). Orthogonality gives f = 2670 (2603 if the cart's own
  vanishing point is used). The fitted D lies within 0.6° of the tile-row direction, and D·up = 0.0008, so the
  cart moves horizontally along a world (tile) axis. That means the cart's own length is the world AABB length.
  Forcing f = 2603 makes the motion fit fail (rms 6.8 px), so f ≈ 2690 ± 1 %.

## Length (extremes.py, triang2.py)
- Cart mask from a median background (rows 640–1060). For each frame I took the leftmost mask point (the end of
  the red handle = rear extreme) and the rightmost point (rim of the far front wheel = front extreme). I checked
  both on the overlays frames/ov_*.png.
- Each track was triangulated as a rigid point, using the known metric translation (a t²/2)·D: the parallax gives
  the depth.
  - handle end: X = −0.531 m along D from the origin (lateral −0.23, +0.55 up), rms 1.1 px
  - front wheel rim: X = +0.550 m (lateral +0.23, −0.51 up), rms 1.6 px
  - The two points' camera distances (12.52 m and 12.69 m) average 12.60 m, about d0, so the origin is near the
    cart centre.
- The rear wheel rim is at X = −0.36, so the handle is the rear extreme. The basket's front-top corner sits about
  12 px behind the vertical through the wheel rim (≈0.05 m further back), so the wheel is the front extreme. The
  automatic basket-corner track was unreliable (rms 20 px) and was not used.
- **L = 0.550 + 0.531 = 1.081 m.** Frames 4–39 give 1.087 m, frames 25–59 give 1.081 m, and the bottom-centre
  motion reference gives 1.084 m.
- Sanity check: the cart is about 0.5 m wide and about 1.1 m tall, which fits a real cart. From frame 0 alone,
  273 px of bbox width ≈ 203 px/m·L + 86 px/m·W, which gives about 1.07 m if W ≈ 0.6 L.

Answer: 1.08 m. Confidence: good (about ±4 %). The main risks are the exact front extreme (wheel or basket) and
f accurate only to about 1 %.
