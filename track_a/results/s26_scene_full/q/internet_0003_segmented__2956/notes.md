# q_2956 — pepperoni diameter (cm), prior "money width = 7.5cm"

Internet video (segmented), top-down static-ish shot, size question -> one planar scale from the prior; no timing
involved (fps 24 vs question_fps 30 irrelevant).

## Reference (prior): Monopoly 500 note, frame 0 (note.py, note2.py)
- Top 500 note lies horizontally: x 874 -> 1022/1023 (white-background edge on the left, edge seen in 5x zoom on the
  right) = 149 px long side; y 195 -> 265 = ~70 px short side. Rotated 500 note ~146-148 x 71 px (scene record).
- Used long side = 148.5 px as "width" (horizontal extent in the image / banknote width x height convention).
  Scale = 7.5 / 148.5 = 0.0505 cm/px.

## Pepperoni (rays.py)
- Radial rays from manual centres, outer edge = largest drop of (R-G) redness, robust circle fit; overlays checked
  in frames/rays_0.png. Clean fits frame 0: 58.8, 64.9, 62.9, 56.3, 60.5, 64.1, 61.0, 58.5 px (median 60.75).
  Bad fits (hand, overlap, under-fit) discarded.
- Second route: frame 47 (camera shifted -26.6 px): 64.6, 60.6, 60.1, 58.4 px — same population. Manual gridded
  reading in frame 0: ~54-63 px.
- Pepperoni = 60.75 px x 0.0505 = 3.07 cm. (Pizza ~456 px -> 23 cm, ratio pizza/pepperoni 7.5.)

## Main risk
If the annotator meant the note's short side (~70 px) as "width", the scale is 0.107 cm/px and the answer would be
~6.5 cm. I chose the long (horizontal) side: it gives a more plausible pizza (23 cm vs 49 cm) and pepperoni
(3.1 cm vs 6.5 cm). Confidence: moderate (measurement +-5 %, interpretation uncertain).
