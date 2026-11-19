# q_1690 — length of the rock (m)

Prior: person height 1.75 m. depth_info: human origin at 100.56 m (t=1 s) and 100.60 m (t=2 s). File fps 25, question_fps 24
(only frame 24 vs 25 matters here; the rock is static, so timing does not affect the answer).

## Measurements (rockmask.py)
- Human, top of head to sole, mask min(RGB)<240 (stable for thresholds 230–250): 60 px at frames 0, 24, 48, 74 (59–61).
  Apparent size stays constant over the clip, so the distance to the body stays ≈100.6 m.
- Scale at the human's depth: 1.75 m / 60 px = 0.0292 m/px, so f ≈ 60·100.58/1.75 ≈ 3450 px (HFOV ≈ 15.9°).
- Rock: static. Mask bbox x 328–959 → 632 px wide, plus ~1–2 px cut off at the right edge, where the tip narrows to a 1 px
  column at x=959. Total ≈ 633 px. Its height in the image is 285 px.

## Scale for the rock
- If the rock is at the same depth as the human: 633 × 0.0292 ≈ 18.5 m.
- The rock's bottom edge (y≈309) is above the human's feet (y≈410), and the camera looks down a little (the rock's top
  surface is visible). So the rock's origin is probably somewhat behind the human. With plausible tilts of 20–45°, the
  ground-plane argument puts it about 5–12 % farther, giving 19.4–20.6 m.
- No ground, horizon or other cues exist to fix the tilt. The depth factor is therefore the main uncertainty (±10 %).

Answer: ≈19.5 m (same-depth scale × ~1.05 depth factor). Same-depth reading: 18.5 m.
Confidence: moderate. The scale from the person is solid; the rock's depth is an assumption.
