# q3230 – ball velocity at 1.80 s

- The clip is a top-down view of a gym floor. A basketball rolls (or travels very low) from right to left over frames 49–72. The file and question_fps are both 30, so t = 1.80 s is frame 54.
- The prior is gravity, 9.8 m/s². The clip shows no vertical fall: the motion lies in the floor plane and the ball's pixel acceleration is about 0. So the prior gives no usable scale.
- **Scale:** taken from a regulation basketball, size 7, diameter 0.239 m. Its blur-free vertical diameter is 256 px, the median over frames 53–69 (range 250–261) from scene/tracks/ball.csv. That gives 0.239/256 = 9.34e-4 m/px.
- **Pixel velocity** (cx_stab, camera drift removed; y motion about 1 px/frame, negligible):
  - Per-frame differences around frame 54: 96.5 (53→54), 101 (54→55), 97, 82.5, 89 px/frame. They are noisy, about ±5 px.
  - Quadratic fit over frames 53–69, slope at frame 54: 93.0 px/frame.
  - Local linear fits: 51–58 gives 91.9 px/frame and 52–57 gives 93.2 px/frame.
  - Value used: about 92 px/frame = 2760 px/s.
- **Answer:** 2760 × 9.34e-4 ≈ **2.58 m/s**.
- **Second route:** the global linear fit over 53–69 gives 90.4 px/frame, i.e. 2.53 m/s. The raw forward difference at frame 54 (101 px) would give 2.83 m/s, but it is noise-dominated.
- **Confidence:** moderate. The scale depends on assuming a size-7 ball; a size 6 (0.232 m) would give a value 3% lower.
