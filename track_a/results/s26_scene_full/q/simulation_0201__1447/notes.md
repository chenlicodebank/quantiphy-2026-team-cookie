# q1447 - droplet speed at t=0.1 s (frame 6, question_fps 60 = file fps)

Method (fit3d.py): drop centroid track from scene/tracks/drop.csv (overlays checked in the sheet; frame 0 centroid
biased by pinch-off so excluded from residuals but used as the anchor). 3D pinhole model, principal point at the
image centre: P(t) = P0 + D*s(t), P0 = 0.156 m * ray(frame-0 centroid), D = unknown unit direction, s = v0*t + a/2*t^2
with a = 9.7 (prior, exact). Unknowns f, D, v0; constraint |P(frame 6)| = 0.186 m (depth_info).
Result: f = 3823 px (hFOV ~37 deg), rms 0.65 px over frames 1-9, effective v0 at frame 0 = 0.008 m/s (released from
rest at t=0, matching the scene record). Per-frame speeds 0.089, 0.250, 0.412, 0.574, 0.735, 0.897 (frame 6), ...

Second route: analytic free fall from rest at t=0 with a=9.7: backward difference at frame 6
= 0.5*9.7*((6/60)^2-(5/60)^2)*60 = 0.889 m/s. Agrees with the fit within 1 pct.
Free-a fit (a also unknown) is ill-conditioned (f and a trade off): a=20.6 and f=1394 - rejected because the prior is exact.
The drop's apparent size is not a reliable depth cue here (the mask shrinks as the drop darkens).

Answer: 0.895 m/s (between 0.889 and 0.897). Confidence: high, given the prior.
