# q_2837 – velocity of the green ball at t = 1.0 s (frame 24, question_fps = file fps = 24)

Green ball = the yellow-green tennis ball (`scene/tracks/yellow_ball.csv`) thrown by the standing person. The "white ball" in
depth_info is the pale ball next to it (3.07 m). Released ~f23. At f24 it is just out of the hand, near (599.5, 291.8).
My own HSV re-track (`track_green.py`) matches the record to <0.5 px for f18-40.

## Dropped frames
The file has missing frames: basketball step f11->f12 = 31.7 px vs ~15-16 px around it; tennis ball step f35->f36 is about
2x the neighbouring steps (pale ball the same). So file frames >= 36 are one frame (1/24 s) later in real time. f24-f35 are uniform.

## Method (lab card: f = 763 px, c = (640, 360))
- P(f24) = 3.039 m along the ray of (599.5, 291.8).
- Floor geometry from the basketball (rolling, centre 0.12 m above floor) at f12 (R 2.3557) and f24 (R 1.81): camera ~0.9-1.0 m
  above floor, pitch 2-6 deg (horizon by eye y~285 gives 5.6). Bounce at file f37 (341, 656.5) -> floor point Z ~= 1.98-2.0 m,
  X -0.78, Y +0.77 (hardly depends on pitch).
- Projectile fit (`fit_constrained2.py`): P(f24) fixed, velocity free (g fixed 9.81 or free), image track f24-f33/35/36, plus the ball
  on the floor at the bounce (true time index 38 = file f37 + 1 dropped frame). The drop=1 timing fits (rms 0.6-1 px with g free,
  g ~8.4); assuming no drop or 2 drops fits much worse.
- Results: V ~ (-1.06, -0.55..-0.80, -1.9..-2.1) m/s; |V| = 2.14-2.42; forward difference at f24 2.10-2.37; 5-frame smoothed
  forward differences 2.06-2.35. Central value ~2.28 m/s. Radial (toward camera) is the largest component.
- Second route: endpoints only (f24 3D point and the floor bounce point, 14 frames apart, gravity): |V| 2.25-2.5 m/s.
- Fit with no floor constraint and free depth (`fit3d.py`) is poorly constrained in Z (not used).

## Prior check
Basketball at f12 with the given depths interpolated linearly: clean 3D speed ~1.60 m/s (1.72 if the smoothing window spans the
dropped frame) vs prior 2.21. Depth from the ball's apparent size (noisy) gives per-frame speeds averaging ~2.1, so the reference
seems inflated by per-frame depth noise; the given 1.81 m at f24 is also closer than the ball's size suggests (~1.96 m).
I could not reproduce the prior exactly, so the scale comes from the green ball's own depth.

## Answer
2.4 m/s: the physical estimate of ~2.28 nudged up by about 5 % toward the noise inflation seen in the prior check.
Confidence: moderate (about ±15 %). The main uncertainties are the radial velocity component and how the reference
smoothed its depths.
