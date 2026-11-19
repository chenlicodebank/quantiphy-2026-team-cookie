# q_3063 – width of the road (m)

Prior: white car length = 4.572 m. Top-down drone view of a bridge deck; road = asphalt between the white kerb/barrier strips.
No timing involved (fps 28.7 vs question_fps 30 doesn't matter here).

- White car length: 457 px bumper to bumper, frames 11-17 (scene record, checked on a zoomed frame 13: rows ~73-529).
  Scale = 4.572/457 = 0.01000 m/px.
- Road width measured in code (kerb.py, frame 13, half-way threshold between asphalt and white kerb in row profiles):
  1312-1328 px at the car's rows (y 30-530), mean ~1320 px; it grows down the frame because of perspective
  (1343 at y=1030, 1369 at y=1830; the record gives 1474 at y=3700).
- Same-depth result (car rows): 1320 x 0.01 = 13.2 m. Measured at mid-frame (1373 px): 13.7 m.
- Second check: four lanes about 375-400 px wide at the top -> 3.75-4.0 m each, which fits a real 4-lane road of ~13-14 m.
- Answer: 13.3 m, mostly from the measurement at the car's own rows, nudged a little toward the mid-frame value.
  Confidence: about ±4 %.
