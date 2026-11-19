# q_1835 cup diameter
- Side view 2D scene; the only moving object (teal, record's "teal_block") is the cup, seen from the side: 42-44 px wide x 78 px tall.
- Speed (prior object = same cup): centroid x linear fit frames 2-71 = 14.536 px/frame = 348.88 px/s (24 fps, question_fps same);
  mean per-frame speed 14.535 px/frame agrees. Scale = 0.338/348.88 = 9.688e-4 m/px.
- Diameter = horizontal width at rest (frames 0-1, measure.py): teal mask 42 px in upper rows, 42-44 px at bottom; faint grey
  fringe gives 44-46 px non-white in lower half (likely shading/segmentation edge). Took 43 px.
- Diameter = 43 x 9.688e-4 = 0.0417 m (range 0.0407-0.0426 for 42-44 px).
- Check: per-frame mean speed and linear fit agree (<0.01 pct); width consistent at frames 0,1 and moving frames (blur widens).
- Confidence: moderate-high (+-3 pct).
