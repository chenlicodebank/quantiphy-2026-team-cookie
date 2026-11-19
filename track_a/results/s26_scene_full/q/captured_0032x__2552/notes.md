# q 2552 — tennis-ball velocity at t = 1.5 s (cm/s)

- t = 1.5 s → frame 36 (question_fps = file fps = 24). The tennis ball is the yellow ball in scene/ (it rolls left and toward the camera, frames 22–42).
- Scale check: prior D = 6.7 cm at the given depth 1.183 m → 763·0.067/1.183 = 43.2 px. The measured diameter is 42–45 px at frame 36, so this is the right object and the right frame.
- measure.py: re-fits the yellow mask outline with a circle in frames 24–42 (only the upper 3/4 of the contour is used). Depth per frame comes from a linear fit of the diameter against the frame number, Z = f·D/d, scaled so that Z(36) = 1.183 m. Each centre is back-projected to 3D with f = 762.75 and (cx, cy) = (640, 360).
- Per-frame 3D speeds (forward differences, cm/s): 33→34: 76.1, 34→35: 74.0, **35→36: 126.2**, 36→37: 74.8, 37→38: 77.1, 38→39: 73.2, 39→40: 75.1.
  The 35→36 step is about twice the normal step. This is the probable dropped or duplicated recording frame flagged in scene/notes.md.
- Candidate answers:
  - single forward difference at 36, or a window that skips the jump: about 75 cm/s (the physical rolling speed);
  - centred 5-frame mean of the forward differences (34–38): 85 cm/s; 7-frame mean: 82 cm/s; Savitzky–Golay 5-point derivative: about 90 cm/s.
  The reference used clicked centres in the actual frames, smoothed over at least 5 frames, so it most likely includes the jump.
- Second route: the scene track ccx gives a 16.5 px step from 36 to 37 → 2.56 cm laterally, plus about 1.9 cm/frame in depth → 3.2 cm/frame ≈ 76 cm/s. This agrees with the clean value.
- Answer: 82 cm/s, a compromise between the clean value (75) and the smoothed values that include the jump (85–90). Confidence: moderate (±10%).
