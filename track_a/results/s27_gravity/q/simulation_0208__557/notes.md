# Q557: length of the letter under the gun

The "scissors" in scene/ are really a revolver lying on a cream paper letter on the desk mat. The scene record's
paper bbox [1191..1305] is wrong: the letter goes on to the right of the dark block (the revolver grip) and ends at x≈1387.

## Letter pixel length (letter.py, frame 0)
Cream mask (R>120, R-B>15). The paper is a flat rectangle, seen as a parallelogram because of perspective.
Row 996: x 1195..1385, and the bbox is 1192..1387. Length along the edge ≈ 191 px (±2).
Overlay check: frames/letter_mask.png.

## Scale from the prior (2D convention: one m/px from the typewriter's fall acceleration of 9.8 m/s²)
- Quadratic fits to the bbox-centre track (fit.py, frames 0-10 before the 0.45 s impact): 7190 px/s²
  (frames 0-8: 7214; 0-6: 6981). Mask centroid gives 6926-7360.
- Second route (tm.py): chained template matching of the typewriter, frames 0-9, gives 7324-7367 px/s², rms 0.15 px.
- Value used: a ≈ 7250 px/s², so 9.8/7250 = 1.352 mm/px. Sanity check: the airborne typewriter, 292 px wide,
  comes out at 0.39 m, which is a plausible size for a typewriter.
- The letter sits on the mat at about the same depth as the typewriter's landing spot (rows ~990-1000).
  From the mat's perspective, the depth difference changes the scale by ≲2-3 %.

## Answer
191 px × 1.352 mm/px = 0.258 m, so the answer is ≈ 0.26 m. The spread from the choice of acceleration is 0.254-0.268 m.
Confidence: moderate-good (±5 %).
