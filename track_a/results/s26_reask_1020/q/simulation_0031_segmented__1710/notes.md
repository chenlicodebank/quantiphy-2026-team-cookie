# Q1710 — eagle wingspan (m)

File is 25 fps, question_fps = 24: frame = round(t*24) (t=1 -> f24, t=2 -> f48). Scripts: measure.py, measure2.py,
solve.py, crops*.py (frames/ holds the check images).

## Focal length (from the human)
- The human faces the camera at about 3/4 front and walks toward the camera and to our left. Its given distances are
  almost constant (139.95 -> 139.98 m), so the origin stays put while the body moves. The speed prior
  (1.3 m/s) therefore cannot be applied to the image motion alone: lateral-only would need f = 3470 px, which would make
  the person about 2.9 m tall (implausible).
- Scale taken from the human's standing height instead: walking bbox height upper envelope = 78 px (85th percentile,
  threshold min(RGB)<250 so the pale head is included; max 80), at body distance ~139 m. With H = 1.75 m,
  f = 78*139/1.75 = 6195 px (HFOV ~8.9 deg).
- Check against the speed prior: at f = 6195 the lateral speed = 0.65 m/s, so 1.3 m/s needs ~1.13 m/s toward the camera
  -> a heading 30 deg off the line of sight, which matches the visible 3/4-front walking pose and the ~2 px size growth
  (within noise). Boat: 9.2 m from keel to mast top (plausible).

## Eagle
- Wingspan seen at full straight spread at f5 and f32 (one per flap cycle, V/wings-up at f0, 24, 48). Tip-to-tip
  (convex-hull diameter) 65.2 px at f5 and 69-72.7 px at f32 (thresholds 225/240).
- Eagle depth, linear in time from depth_info: 147.3 m at f5, 136.6 m at f32. Check: span*depth = 9600-9930 px*m in
  both cycles (the growth from f5 to f32 matches the depth ratio of 1.078), so the given eagle depths agree with its
  apparent size.
- Projected span = 1.52-1.60 m. 3D velocity from the t=1 / t=2 positions = (5.9, 2.2, -9.7) m/s (mostly toward the
  camera). I assumed the wings are horizontal and perpendicular to that velocity, which gives a foreshortening
  factor of 0.84-0.86. True span = 1.79 (f5), 1.81 / 1.91 (f32 at 225 / 240), 1.81 (f33).
- Answer 1.82 m. Sensitivity: human height 1.70 / 1.80 m -> 1.75 / 1.88 m; without the foreshortening correction
  it would be 1.55 m.

Confidence: moderate. The scale depends on the assumed human height (1.75 m) and on the wing-orientation correction.
