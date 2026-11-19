# q 2071: distance from the player closest to the goal to the goal at t = 0

- The camera looks straight down at the pitch, so this is a 2D scene. Frame 0 is t = 0, so the 30 vs 29.76 fps question does not matter here.
- Scale: I re-fitted the centre circle in code (`measure.py`, 71 ray samples of the white line, algebraic circle fit):
  centre (941.4, 521.6), R = 116.94 px, residual sd 0.26 px. This matches the record's 116.9 px.
  Scale = 9.15 / 116.94 = 0.07825 m/px.
- Players at frame 0 (from the scene tracks, checked on a 4x zoomed crop, frames/f0.png): A (light) at (1406.6, 520.4),
  B (dark) at (1462.0, 530.2). B is the player closer to the right goal.
- Goal: the goal line is at x ≈ 1595 (seen on the crop) and the posts span y 470-570, so the centre of the goal mouth is (1595.3, 520).
- B to the centre of the goal mouth = 133.7 px → **10.46 m**.
- Other reading: measured to the middle of the goal frame/net (x ≈ 1609.5) it is 147.9 px = 11.57 m. I answer with the goal-mouth reading, which is the standard one.
- Check: the penalty spot comes out 143.9 px × 0.07825 = 11.26 m from the goal line (the real value is 11 m, a 2% difference), so the scale is consistent.
  B stands about 10 px goal-side of the spot, which fits a distance of about 10.5 m.
- Confidence: good. The scale is accurate to about 0.3%. The main uncertainty is which point counts as "the goal" (about ±1 m).
