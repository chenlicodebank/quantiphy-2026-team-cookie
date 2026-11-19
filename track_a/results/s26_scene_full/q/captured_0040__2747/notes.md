# q_2747 – height of the white cup (cm)

- Lab video, 1280x720, 24 fps (file fps = question_fps = 24). f = 0.5959 x 1280 = 762.8 px, pp (640,360).
- depth_info gives "distance_white_cup_camera = 8420m" – clearly a typo; read as 0.8420 m (consistent with the
  cup standing behind the card at 0.69 m and in front of the tape/poker tower at 0.91-0.97 m).
- Cup is static. measure.py (frame 12): vertical gradient profiles at x = 760..795 give top (silver rim) y = 376-380,
  bottom y = 501-503; white-mask bbox (S<40, V>170) 740..814 x 379..502 (123 px, excludes the grey rim). Rim top
  ~376, bottom ~503 -> pixel height ~127 px (overlay frames/cupmask.png).
- Method card: H = 0.842 x 127 / 762.8 = 14.0 cm. Using the true depth z (distance / 1.021 for the off-axis ray at
  (777,439)): 0.8245 x 127 / 762.8 = 13.7 cm. Answer 13.8 cm (between the two).
- Second route / check with prior: dark flat card (credit card?) at front of table spans 107 px horizontally at
  0.69 m -> 9.7 cm by distance (9.4 cm by z) vs 85.6 mm prior, i.e. the depth-based scale may be ~10% high; the
  card's identity/orientation is uncertain, so it is not used to rescale. Real-world sanity: a 14 cm tumbler is plausible.
- Confidence: moderate (±5-10%), dominated by depth-value interpretation and rim/bottom edge choice.
