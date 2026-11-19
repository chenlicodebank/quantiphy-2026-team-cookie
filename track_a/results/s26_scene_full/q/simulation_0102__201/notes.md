# q_201 — distance shark–boat at t = 0.5 s (frame 12, fps 24 = question_fps)

2D scene: the boat is on the surface (upper part), the shark is underwater (lower part), and there is one static camera.
I used a single metres-per-pixel scale.

## Scale (prior: shark acceleration = 1 m/s^2), script fit.py
I fitted a quadratic to the shark's x track (frames 1–60):
- centroid: −0.1502 px/f² = 86.5 px/s²
- frames 1–30: 83.4 px/s²; frames 30–60: 85.8 px/s²
- nose edge: 87.3–88.4 px/s²

→ 86.3 px/m (0.01159 m/px).
Check: at this scale the boat's constant 17.95 px/frame = 431 px/s = 4.99 m/s, and the shark's initial speed of
7.33 px/f = 2.04 m/s. Both are round numbers, so the scale is consistent.

## Positions at frame 12
- boat bbox-centre x = 856.0 (stern edge + 413 px offset; the boat is rigid)
- shark x: centroid 705.2, nose/tail midpoint 731.1 → dx ≈ 125–151 px; I used 138
- vertical: shark centre y ≈ 905. The boat origin's y is the main uncertainty because the mast is clipped at the
  top of the frame:
  * hull+cabin bbox centre y ≈ 415 → dist 510 px = 5.9 m
  * full bbox including mast (top guessed at ≈ −30) y ≈ 307 → 615 px = 7.1 m
  * waterline/bottom origin y ≈ 640 → 300 px = 3.5 m

## Answer
I took the origin to be the object centre (the convention). The boat centre is somewhere between y 307 and 415, so
I used y ≈ 380: dy = 526 px, dx = 138 px → 544 px → **6.3 m**.
Confidence: moderate-low. The scale is solid (to within 2%), but the boat origin's vertical position cannot be seen.
