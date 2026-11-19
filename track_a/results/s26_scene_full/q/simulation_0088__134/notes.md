# Q134 – body length of the small bird (crow)

2D video (birds fly horizontally in one plane), fps 24 = question_fps.

- measure.py: background-difference mask (sum|RGB-bg|>40), connected components per frame.
- Big bird (eagle) right edge (tail end) 1643 px at f2 → 206 px at f14: 119.75 px/frame = 2874 px/s
  (each step is 119–120 px, steady). This agrees with the scene record (119.69).
- Scale = 17.98 / 2874 = 0.006256 m/px.
- Crow horizontal extent (beak to tail, body axis horizontal) over fully visible frames f2–f24: 85–88 px,
  mean ≈ 86.6 px. Checked on a zoomed crop at f12: the mask spans beak tip to tail end.
- Length = 86.6 × 0.006256 = 0.542 m.

Check: the eagle's length of 138.7 px works out to 0.87 m, which is plausible for an eagle, and the
eagle-to-crow ratio is consistent. The ±1 px edge uncertainty is about ±1.2 %. Confidence: high.
