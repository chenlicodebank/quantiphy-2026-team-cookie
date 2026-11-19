# q3049 – acceleration of the swimmer, 0–2.33 s

- Time base: question_fps = 25, so 2.33 s = frame 58. The file runs at 18.54 fps and has exact duplicate frames 1, 11, 20, 30, …
- Scale: prior 1.68 m over the swimmer's cap-top-to-feet length. That is 1007 px at frame 0 and 1041 px as the median; I used 1020 px, giving 1.647e-3 m/px. This gives a swim speed of about 0.75 m/s, which is plausible. The camera is static (scene record).
- Measurement (est.py, scene head/hip tracks, frames 0–58; positive means speeding up):
  - head: quadratic fit −0.030; windowed endpoint velocities −0.017 to −0.043; three-point second difference (0, 29, 58) −0.035; one-frame forward difference that skips the duplicate frame −0.051 m/s²
  - hip: about 0 (−0.03 to +0.01)
  - mask centroid: noisy (−0.10 to 0)
- Where the candidates part ways: both scale the same way, but they read the near-zero mean acceleration differently. C1 reports +0.1 from a median of endpoint estimates. My head track shows a slight slow-down, not a speed-up. C2's 0.037 comes from a quadratic fit and matches my head result.
- Artefact reading: if the forward difference at t = 0 uses duplicate frame 1, then v0 = 0 and a ≈ 0.3–0.36 m/s². I rejected this because the duplicate frame is a frame-rate artefact and the swimmer is plainly moving at frame 0.
- Answer: |a| ≈ 0.035 m/s² (the swimmer slows slightly; the head track is the most consistent route). I agree with C2. Confidence is low because the true value is close to zero and depends on convention.
