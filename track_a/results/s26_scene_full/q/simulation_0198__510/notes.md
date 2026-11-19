# Q510: vertical height of the "SKYNOVA" lettering

- 2D scene with a static camera. fps = question_fps = 60.
- Scale comes from the prior: the drop accelerates at 9.7 m/s².
  - I fitted a quadratic to the drop centroid y (scene/tracks/drop.csv) using the render-index mapping from scene/notes.md (frame 7 is a duplicate, render step 8 is missing).
  - Frames 0–6 give a = 31.67 px/frame², and frames 0–10 give 31.69 px/frame². Both agree with the record's per-frame step growth of about 31.6 px.
  - a ≈ 31.68 × 3600 = 114,050 px/s², so the scale is 9.7 / 114,050 = 8.51e-5 m/px.
- Lettering (measure.py, frame 12):
  - "SKYNOVA" is printed vertically in white on the orange label.
  - I masked it with b > 150 and r − b < 60 inside x 1760–1850 (checked visually in frames/mask.png).
  - The letters run from row 814 (top of the "A") to row 1141 (bottom of the "S"), which is about 328 px.
- Height = 328 × 8.51e-5 ≈ 0.0279 m.
- Sanity check: the bottle is about 750 px tall (neck to base), which comes to about 6.4 cm. That is plausible for a 30 ml dropper bottle.
- Confidence: moderate to high. Lettering edges are good to about ±2 px. The main risk is that the reference does not put the drop and the bottle in the same plane.
