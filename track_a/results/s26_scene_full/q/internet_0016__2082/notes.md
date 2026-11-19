# Q2082: distance between the ball and the player in black at t = 0.5 s

- Time: frame round(0.5 x 29.9) = round(0.5 x 30) = 15. Both rates give the same frame.
- Scale (2D, internet convention): prior "inner court width" = 4.88 m = lane (paint) width. The bottom lane,
  where the play happens, is 639.5 px between line centres (scene.json). That gives 0.007631 m/px. Using the
  inner or outer line edges (±11 px) would change this by about 1.7%.
- Ball at frame 15: NCC track (1142.3, 3434.0) px. Checked on a zoomed crop (frames/f15.png).
- Player B (black shirt) at frame 15: the record's mask centroid (1049.5, 3262.5) is pulled up-left by the two
  raised white arms. I re-measured it with body15.py: non-shadow dark pixels (gray 7-44) make up the shirt, with
  a centroid of (1058, 3274). The head and upper body are darker and extend to y ≈ 3325, so the body centre is
  about (1060, 3280) ± 8 px.
- Distance: about 174.6 px (dx 82, dy 154), so 174.6 x 0.007631 ≈ 1.33 m.
- Other centre choices: the shirt-only centroid gives 181 px (1.38 m), the torso+head box centre (1061, 3288)
  gives 167 px (1.28 m), and the full mask centroid including the arms gives 195 px (1.49 m).
- Confidence: moderate. The main uncertainty is which point counts as the player's centre (about ±5%).
