# q_960 — speed of the phoenix at 1.0 s (m/s)

Prior: acceleration of the phoenix at 2.0 s = 2 m/s². 2D video, 24 fps (file fps = question_fps, no re-timing).

## Method
- Used the scene record's beak-tip track `ref_x` (frames 0-69, the beak is visible there; the record says the body
  template moves rigidly with the beak). Single object, static camera.
- Per-frame dx goes up in steps (≈8 → 25 → 41 px/frame), with plateaus tied to the 25-frame wing-beat. Model:
  x(f) = c + v0·f + ½·a·f² + periodic surge (period 25 frames, Fourier terms) — that is, the origin accelerates
  uniformly and the mesh surges back and forth with the flap. Fit (fit2.py): rms residual 1.2 px (vs 20 px for a
  quadratic alone; periods of 24 or 26 frames give 3.8 px), a = 0.657 px/frame², v0 ≈ 0.01 px/frame, so the bird
  starts from rest.
- So the origin accelerates uniformly. That makes the prior's 2 m/s² the constant acceleration:
  scale = 2 / (0.657·24²) = 0.00528 m/px.
- Speed at t = 1.0 s (frame 24), one-frame backward difference of the fitted origin: |x24 − x23|·24·scale = 1.957 m/s.

## Checks
- Analytic: uniform 2 m/s² from rest at frame 0 gives speed(24) = ½·2·(24² − 23²)/24² · 24 = 47/24 = 1.958 m/s.
- The body-template cumulative track (the second route) gives a = 0.640 px/f², speed 2.06 m/s. Its rms is worse
  because the template drift adds up.
- The other reading (local acceleration near frame 48 ≈ 1.7 px/f² from the step) gives ≈ 0.7 m/s. I rejected it:
  the uniform-accel-plus-periodic model fits to 1.2 px, and the 2 m/s² prior is a round, designed constant.

Answer: 1.96 m/s. Confidence: fairly high (about ±3%) if the uniform-acceleration reading is right.
