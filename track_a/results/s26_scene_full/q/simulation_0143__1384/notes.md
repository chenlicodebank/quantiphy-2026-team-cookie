# Q1384 — speed of the man at t = 2 s (frame 48 at question_fps 24 = file fps)

## Scale
- depth_info: D(f0)=7.21 m, D(f12)=7.91 m. For a level camera (horizon ~row 538 in scene/notes), the pixel height is
  h_px = f*H/Z. That gives K = f*H_walk = Z*h_px: 3093 (f0, h=429) and 3156 (f12, h=399); 3096/3120 after smoothing h
  and correcting D to Z for the off-axis ray. I used K = 3108 and f = K/1.8 ≈ 1727 px (HFOV ≈ 58°).
- Depth: Z(t) = K / h_px(t). Lateral: X = (torso_x − 960)·Z/f.
- Checked the heights on crops: frame 0 is 415→843 (429 px) and frame 48 is 462→737 (~276 px), which matches scene/tracks.

## Speed
- The gait makes per-frame values unusable: height-based Z moves in steps of about ±1.5 m/s per frame. So I took the
  smooth (cycle-averaged) velocity of the origin at frame 48.
- Route 1 (height cue), fitting a polynomial plus a step-frequency sinusoid (period ~12 frames) over several windows
  (26–70, 30–66, 20–80, 34–62): speed 2.76–2.86 m/s, with vz ≈ 2.8 and vx ≈ 0.2–0.35.
- Route 2 (ground-contact cue): Z ∝ 1/(feet_y − 538), scaled to route 1. The same fits give 2.75–2.83 m/s.
- Plain linear fits over 23-frame windows near frame 48 give 2.5–3.1 (noisy). Polynomial fits without the harmonic give 2.77–3.1.
- He walks faster later in the clip (~1.75 m/s during frames 0–20, ~2.8 m/s from frame 35 on). The depth_info
  pair alone gives ~1.9 m/s over 0–0.5 s, which matches route 1 in that early window.

## Answer
2.81 m/s. Confidence: moderate. The answer is about ±5 % from the cycle averaging; the true per-frame origin speed
can vary within the gait cycle by an amount that cannot be measured here.
