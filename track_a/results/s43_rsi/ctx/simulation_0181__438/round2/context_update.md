# Round 2 addendum: q438 (speed of the box at 1.5 s = frame 36)

Answer: 3.68 m/s ("new"; verifies round 1's 3.6 within 2 %). Submitted was 3.839 (blend of C1 4.15 and DeepSeek median 3.2).

## Established (independent code: track.py, fit.py, fall.py)
- Free fall frames 0–7, from template tracking (rms 0.07 px): 2552 px/s². Taking this as g gives 3.844 mm/px.
- Slide acceleration over frames 20–29, where the silhouette length is constant at 281 ± 2 px: midpoint 633,
  trailing edge 618, leading edge 648 px/s². Trailing-edge fits over windows containing frame 18: 588–624.
  Adopted 620 → 3.77 mm/px. Closure with gravity: within 2–4 %.
- Early midpoint windows (14–22) give 730–810 px/s². These are biased by the side-face/yaw change in frames 12–20
  (length 312 → 281). At a 720 scale, g would come out at 8.3 m/s², so these windows are ruled out.
- From frame 30 the silhouette grows 6.5 px/frame (left side face, yaw). Trailing edge steps for frames 34/35/36 are
  35.5/36.2/36.9 px. Centre = trailing edge + half the length (extrapolated to 326 at frame 36). Centre step at
  frame 36 = 40.1–40.8 px → v36 = 970 ± 15 px/s (round 1: 960).
- Speed = 3.66 (prior scale) to 3.73 (gravity scale) m/s.

## Ruled out
- C1's v36 = 1056 px/s (constant-acceleration texture line).
- DeepSeek scales of 700–736 px/s².
- C2's constant v36 = 881 px/s.

## Open
- Whether a 2–3 % growth of the box height over frames 29–36 is approach to the camera (effect on the speed < 1 %).
- Residual ±3 % from the choice between prior scale and gravity scale.
