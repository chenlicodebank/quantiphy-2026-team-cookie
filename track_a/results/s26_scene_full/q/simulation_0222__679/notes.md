# q_679 — speed of the vacuum cleaner at t = 2 s

- 2D top-down render, fps 24 (file and question agree). t = 2 s -> frame 48; speed = |p48 - p47| x 24.
- Object: the white robot-vacuum disc, the only moving object (checked on a zoomed frame-48 crop: disc spans x≈888–1007, y≈328–446, centre ≈ (947, 387), matching the record).
- Pixel step 47->48: record circle-fit centres give 22.16 px; independent phase correlation of the disc patch gives 22.19 px. Neighbouring steps (21.7, 22.6) show a smooth speed-up, with no event near frame 48.
- Scale: the prior diameter is 0.438 m. The record's circle fit on a strict threshold mask (g>185) gives 117.5 px, which is slightly inside the anti-aliased rim. Half-max edge profiles along 12 directions through the centre (`measure.py`) give 119.6–119.9 px, so I used about 119.6 px. Scale = 0.438/119.6 = 3.66e-3 m/px.
- Speed = 22.17 px x 24 /s x 3.66e-3 = 1.95 m/s. Using the 117.5 px diameter instead gives 1.98 m/s, a 1.7% difference.
- Confidence: high, within about 2%.
