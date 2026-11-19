# q_2304 — tennis ball velocity at 3.4 s (cm/s)

## Time problem
Clip has 49 frames (0–2.0 s at 24 fps; file fps = question fps = 24). t = 3.4 s -> frame 82, which does not exist.
Assumption: the clip is a 2.0 s cut [1.4 s, 3.4 s] of the original recording (49 frames inclusive), so 3.4 s = clip
frame 48 (last frame). At that moment the tennis ball is falling again after its first rebound (apex at frame 45.0).
This mapping is a guess -> low confidence.

## Measurements (scene/tracks/tennis_ball.csv, checked with fit.py)
- Rebound flight frames 39–48: parabola fit, apex 44.97, a = 4.4 px/frame^2, residual 0.7 px.
  Instantaneous vertical speed at frame 48 = 13.3–14.0 px/frame (fits over 37–48 / 39–48 / 41–48); backward diff
  47->48 = 10 px/frame; forward diff 48->48.5 (extrapolated) ≈ 15.5 px/frame. x is constant (750 px) -> speed is vertical.
- Depth: tennis ball diameter 24–25 px near the apex -> 0.067 m * 763 / 24.5 ≈ 2.09 m; near person (who dropped it)
  depth_info 2.002 m. Used 2.05 m -> 2.69 mm/px.
- Free fall frames 28–35: a = 5.6 px/fr^2 -> g gives 3.0 mm/px (depth ≈2.3 m), roughly consistent; rebound a = 4.4
  px/fr^2 would imply 3.9 mm/px (not explained; possibly timing irregularity — a dropped frame is suspected at 35->36).

## Answer
v ≈ 14 px/frame * 24 * 2.05 / 763 ≈ 0.90 m/s = 90 cm/s.
Second route (scale from gravity on the rebound parabola): 13.5/4.4 * 9.8/24 ≈ 1.25 m/s; pinhole with backward diff only: 0.66 m/s.
Confidence: low (time mapping assumed; scale routes differ by ~±30%).
