# q2896: velocity of the green ball at t = 1.0 s (frame 24)

- The "green ball" is the yellow-green (tennis-type) ball, `yellow_ball` in scene/. Frames 19-30 were checked on a montage
  (frames/montage.png). The ball is motion-blurred into a streak. The track centroid is the centre of the streak, and it
  overlaps the white ball in f22-26 (split by colour). The x/y steps around f24 are smooth (about 45 px/frame in x) and no
  frame is dropped near f24. The f35->36 drop does not matter here.
- question_fps = file fps = 24. f = 0.5959*1280 = 762.8 px, principal point (640, 360). Depth of the green ball at t=1.0 = 1.331 m.
- Only one depth is given for the ball, so the depth rate came from the trajectory:
  - **Route 1 (fit3d.py):** I fitted a ballistic 3D model (constant acceleration) to the projected track, with Z(f24) pinned at 1.331 m.
    Over windows 19-35, 20-33, 22-30, 19-30 and 23-35, |V(t=1)| = 2.02-2.07 m/s (Vz about 0.3-0.7 m/s away from the camera).
    The fitted |g| was 8.2-9.8, which is physically reasonable. The fitted Z gives a ball diameter of about 0.07 m from the
    unblurred widths (f27+), consistent with a tennis-type ball.
  - **Route 2 (route2.py):** I back-projected the measured centres with Z(t) tracks spanning Vz = 0 to 1.26 m/s and took
    3D forward differences. The 5-frame mean (f22-26) is 2.00-2.12 m/s, the forward difference at f24 is 2.01-2.17, and the
    chord f22->f26 is 2.02-2.13. The result is insensitive to the depth rate.
- Prior check (prior_check.py): for the basketball at t=0.5, lateral motion at Z=2.24 smoothed over f10-f14 gives 2.26 m/s,
  against a prior of 2.21. The depth-constrained fit gives about 1.9 m/s, but that window includes the suspected dropped frame
  at f11->12, and the given orange-ball depths (2.24 -> 1.81 m) contradict its shrinking apparent size. So the prior is only
  roughly reproduced, and only with the convention that includes the inflated step.
- Answer: **2.05 m/s**. Confidence moderate (about ±6%). The main unknown is the depth rate the reference's depth sensor recorded.
