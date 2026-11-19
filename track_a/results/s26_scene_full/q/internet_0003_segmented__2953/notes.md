# q_2953 — pizza diameter (cm), prior: money width = 7.5 cm

Static size question, so the time base (24 vs 30 fps) does not matter. Internet convention: one scale = 7.5 cm / pixel width of the note.

## Money (frame 0, prof.py intensity profiles + zoomed grids)
- Top 500 note (upside-down, axis-aligned): left edge x≈873.5; at x=878 the top edge is at y≈196-197 and the bottom edge at y≈265.5,
  so the short side is ≈69 px. The long side is ≈149 px (scene record).
- Rotated 500 note, corners from the record: short sides 65.5 / 71.2 px (mean ≈68), long side ≈146 px.
- I read "width" as the short side of the banknote, ≈69 px. 7.5 cm is a believable short side for a banknote, but not a long side.
  Scale = 7.5/69 = 0.1087 cm/px.

## Pizza (scene/tracks/pizza.csv, RANSAC rim ellipse; the pizza is static)
- Horizontal 471.8 px, vertical 440.9 px, mean 456 px.
- 471.8 x 0.1087 = 51.3 cm; 456 x 0.1087 = 49.6 cm. Answer: 50.5 cm, between the two (each is within 2 %).

## Checks / confidence
- Second route: the rotated note's short side (68 px) gives 50.0–52.0 cm, which agrees.
- Caveat: real-world cues (finger ≈27 px, glass, pepperoni ≈57 px) suggest the true scale is about 0.07 cm/px, i.e. a pizza of about 33 cm.
  The prior does not match reality under either reading. If the annotator used the long side (≈148 px), the answer would be ≈23 cm.
  Confidence is moderate and depends mainly on which side "width" means.
