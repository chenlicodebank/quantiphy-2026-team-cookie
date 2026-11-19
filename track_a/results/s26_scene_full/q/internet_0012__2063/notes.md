# Q2063: average velocity of the white car in the second lane from the left (m/s)

**Which car:** The left carriageway has 3 lanes. Lane lines at frame 54 sit at x ≈ 753 (solid edge), 852, 948 and 1046 (median line), measured near y = 1350. The car is the scene record's `white_car_upper`: a sedan centred at x ≈ 868–870, with its body spanning x ≈ 845–895. It sits mostly in the lane between 852 and 948, which is the second lane from the left. The other white car (x ≈ 829) is in the leftmost lane. A crop of frame 107 confirms the track box is on the car (centre y ≈ 2128).

**Scale (prior: lane width 3.66 m):** `lanes.py` finds the line centres from column brightness profiles at 4 dash rows (y ≈ 1400–2600). The spacing between adjacent lines is 96–99 px, and the 3-lane span divided by 3 gives 97.7 px (97.6–98.0 across the rows). Scale = 3.66 / 97.7 = 0.03746 m/px. If the annotator used only the car's own lane (≈96 px), the answer would be about 1.7% higher.

**Motion:** The camera is static (record: lamp drift ≤ 2 px). The video repeats 3 frames in every 7, so I used the net displacement and fits rather than one-frame differences.
- Net displacement from frame 0 to frame 107 is 665.6 px, or 6.221 px/frame. Both end frames are distinct frames, not repeats.
- A linear fit over the non-repeated frames gives 6.229 px/frame.
- The independent edge-based centre gives 6.216 px/frame.

| route | fps 59.35 | fps 60 |
|---|---|---|
| net displacement | 13.83 m/s | 13.98 m/s |
| fit on template track | 13.85 m/s | 14.00 m/s |
| fit on edge track | 13.82 m/s | 13.97 m/s |

**Time base:** The file runs at 59.35 fps and the question states 60 fps. That 1.1% difference can't be told apart physically (about 50 km/h is plausible either way). I answer 13.9 m/s, which is within 0.6% of both.

**Confidence:** Good. The main uncertainty is which lane width the annotator measured (about ±2%).
