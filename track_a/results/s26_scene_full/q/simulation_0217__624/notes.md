# q_624 — length of the TV (m)

Prior: black cat speed = 0.94 m/s. No depth_info. fps 24 = question_fps, so no re-timing.

## Objects
- The TV is not in the scene/ inventory. It is the dark flat-screen slab standing on the console table (between the
  vase and the lamp), seen from above. Its front face shows as a trapezoid at y ≈ 220–242 px and x ≈ 806–1099 px. Two
  thin feet run down to y ≈ 266 at x ≈ 843 and 1066 (crops: frames/tvzoom_0.png, frames/tv_eq.png).
- Black cat: I re-segmented it in catcheck.py (max(BGR) < 60, largest component). The front edge moves 10.98 px/frame
  and the centroid 10.94 px/frame, with essentially zero acceleration. This matches scene/tracks.
  Speed = 10.96 px/frame = 263.0 px/s, so the scale at cat height is k = 0.94/263.0 = 3.574 mm/px.

## TV pixel length (tvedges.py, 6 frames averaged, sub-pixel half-level edges per row)
- Rows 223–241: the width shrinks steadily from 290.0 to 274.5 px. Extrapolated to the top edge (row ≈ 220) it is
  ≈ 292.5 px; at the bottom edge (row ≈ 242) it is ≈ 275.2 px.
- The left and right edge lines converge at about (971, 611), near the image centre. So this is a vertical face seen
  in perspective: the top is closer to the camera.
- The top-to-bottom ratio is r = 1.063. The y offsets give a similar ratio (1.057–1.07), so the readings are consistent.

## Scale with perspective correction
The camera looks straight down, so a scale taken from the cat (about 0.2–0.25 m above the floor) does not apply
exactly at the TV's height.
- With a 16:9 TV, H/L ≈ 0.58. Then D − z_top = H/(r−1), and f = 292.5·0.58/0.063 ≈ 2.7–2.8k px (HFOV ≈ 38°, close to
  Blender's default 50 mm lens at f = 2667 px).
- L = 292.5·k − 292.5·Δ/f, where Δ = TV-top height − cat feature height.
- Heights: the console is about 0.3 m (its front face is foreshortened by ~8.5 px), the TV is about 0.56 m tall, and
  the cat is about 0.22 m. That gives Δ ≈ 0.68 m.
- Result: L = 1.045 − 0.074 ≈ 0.97 m.

## Checks
- Route via the bottom edge (275.2 px at z_bottom): L = 275.2·k·(D−z_b)/(D−z_c) ≈ 0.973 m.
- Route with f fixed to the Blender default of 2667 px: L ≈ 0.969 m.
- Without any perspective correction the result would be 290·k ≈ 1.04 m (upper bound).
- Sensitivity: Δ from 0.5 to 0.9 m gives L from 0.99 to 0.95 m.

Answer 0.97 m. Confidence: moderate-good (±4%); the main uncertainty is the height of the TV above the cat.
