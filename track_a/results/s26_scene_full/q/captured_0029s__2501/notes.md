# Q2501: velocity of the tennis ball at 1.6 s (cm/s)

- The file and question_fps are both 24 fps, so t = 1.6 s is frame round(38.4) = 38.
- Camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360). The camera is static.
- `measure.py`: HSV mask of the ball, then an algebraic circle fit to its contour, for frames 26 to 48. This gives the centre (u, v) and the diameter d. At frame 38 the centre is (616.6, 448.0) and d = 47.5 px.
- Depth: the size-based depth Z = f x 0.067 / d is scaled so that Z(38) = 1.027 m (depth_info). The scale factor is 0.955, because the mask runs slightly small. Check: the scaled value at frame 30 (t = 1.24 s) is 1.149 m, against the given 1.144 m. So the given depths and the ball size agree within 0.5 %.
- `velocity.py`: a linear fit over a window of about 5 frames around frame 38 gives du = -10.5 px/frame, dv = +0.55 px/frame and dZ = -1.08 cm/frame. The ball is rolling left and toward the camera. The 3D centre is back-projected as ((u-cx)/f, (v-cy)/f, 1) x Z.
  - v = (-33.2, -1.3, -26.2) cm/s, so |v| = 42.3 cm/s.
- Second route: other windows (36-40, 36-44, 37-43, 38-42, with Z fits over 36-48) give 41.5 to 42.3 cm/s, mean 41.9. Raw per-frame 3D speeds for frames 37 to 41 are 44, 41, 43, 40 and 42 cm/s.
- Caveats:
  - A capture frame was probably dropped between frames 35 and 36. That step (73 cm/s) is excluded from every window.
  - Interpolating the two depth anchors linearly (1.144 m at frame 30, 1.027 m at frame 38) would give a larger Z rate of about 1.46 cm/frame and |v| of about 48 cm/s. That window spans the rebound and the dropped frame, so I used the local size trend instead.
- Answer: **41.9 cm/s**. Confidence: moderate to good (about ±10 %).
