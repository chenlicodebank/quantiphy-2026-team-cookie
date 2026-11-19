# q_2754 – diameter of the tape (cm)

Lab clip, 1280x720, 24 fps (file fps = question_fps = 24). Camera static; tape roll static, lying flat on the table
right of the glass jar (scene record bbox frame 0: x 551–629, 78 px wide – checked).

Method (lab method card): f = 0.5959 x 1280 = 763 px, depth to tape = 0.973 m (depth_info).
- Diameter = horizontal image extent of the roll (lying flat, so its horizontal width is the diameter).
- Measured in code (`overlay.py`): grayscale column profile averaged over rows 452–476 (tape body), half-max edges:
  left ≈ 551.5 px (jar/table 136 → tape 160), right ≈ 628.2 px (tape 171 → table 130). Extent ≈ 76.7 px
  (gradient maxima at several rows in `measure.py` give 76–77 px). Overlay `frames/overlay.png` confirms the edges.
- D = 0.973 x 76.7 / 763 = 0.0978 m ≈ 9.8 cm. Off-axis angle (~3.7°) and cylinder-silhouette corrections < 0.2 %.

Check (prior): credit card (dark card with yellow note, depth 0.690 m) – long edges ≈ 90 px (back) and ≈ 95 px
(front), mean ≈ 92–93 px; prediction 85.6 mm x 763 / 690 mm = 94.7 px → agrees within ~2 % (card slightly rotated),
so f = 763 px is consistent.

Answer: 9.8 cm. Confidence: good (±3 %).
