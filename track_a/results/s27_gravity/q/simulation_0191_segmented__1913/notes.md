# q_1913: width of the box (m)

2D simulation (segmentation) clip, 120 fps (the file rate and question_fps are the same). The box falls straight down from rest at t≈0 and lands on the truck roof at frame 60–61 (t≈0.50 s).

**Scale from the prior (a = 9.8 m/s² before 0.6 s).** fit.py fits a quadratic to the vertical position over the free fall, on two tracks from scene/tracks/box.csv:
- face bottom edge: frames 0–60 → 1951 px/s²; 5–58 → 1962; 10–58 → 1967; 30–59 → 1960. Residuals have an RMS of about 0.7 px.
- face centre: frames 5–58 → 1962; 10–58 → 1963.
- Adopted value: a ≈ 1961 px/s², so the scale is 9.8 / 1961 = 0.00500 m/px. Across the windows the scale varies by ±2%.

**Box width.** width.py re-measured the front face's horizontal extent with a colour mask at frames 40, 120 and 190. Edge to edge it covers x = 530–937 (columns 529–938 with the partial edge pixels), so it is about 409–410 px in every frame. The box does not rotate.

Width = 409.5 px × 0.00500 m/px = **2.05 m**. The face height is 190 px, which is 0.95 m.

**Check.** At this scale the truck is 1717 px × 0.005 = 8.6 m long, with a wheelbase of 4.4 m and wheels 0.9 m in diameter. These are realistic for a catering truck, so the scale is consistent.

**Ambiguity.** "Width" is read as the visible horizontal extent across the box face (the in-plane extent in a 2D video). The box's depth front to back cannot be measured from this view; only a thin top/underside strip is visible.

Confidence: good (about ±3%).
