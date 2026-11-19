# q_639 – long side of the marked parking space

**Prior:** the big robot moves at 5.924 m/s. **fps:** 24 (the file and the question give the same rate). The camera is static.

## Geometry
- The floor box is made of two white horizontal lines (back line at row 844, front line at row 909) and two thick
  depth lines. The depth lines meet at a vanishing point of (958, 552), so they run perpendicular to the wall. The
  box's horizontal span (about 1000–1200 px, which is 5.8 m) is much larger than its depth (estimated at about 4 m,
  see below). So the long side is the edge along the wall, i.e. the distance between the two depth lines.
- Although the clip is labelled 2D, perspective is clear: parts of the robot at different depths move at 45.8 to
  54.5 px/frame. A single image scale would be wrong, so I used ground-plane geometry. Every rigid part moves at the
  same world speed, 5.924/24 = 0.2468 m/frame.
- The near-side outer face of the track (near-side rear corner silhouette 50.90 px/frame, chassis plate 50.75) gives
  50.9/0.2468 = **206.2 px/m**. That holds at the ground row where this face touches the floor. The track bottom,
  measured as the lowest row that differs from the empty frame 49, is **row 894** (x 640–740).
- Depth-line centres (`measure.py`, linear fits over rows 850–899 of frame 49, residuals ≤ 2.5 px): the centre
  spacing at row 894 is **1191.9 px** (inner edges 1119.7, outer edges 1264.2; the lines are about 68 px wide, i.e.
  0.35 m).
- Long side = 1191.9 / 206.2 = **5.78 m** centre to centre (inner edges 5.43 m, outer edges 6.13 m).

## Check
- Spacing is proportional to (row − 552) at every row: 1024.7 px at row 846 and 1223.3 px at row 903 give the same
  constant, 3.485 px per row. The scale is also proportional: 206.2/342 = 0.603 px/m per row. Taking any row gives
  W = 3.485/0.603 = 5.78 m.
- The 2D rule of thumb (origin_est rate 52.46 px/frame with the back-line spacing) would give 4.8 m, but that mixes
  depths. I reject it.
- Which side is long: from the widths of the horizontal lines (taking them equal to the 0.35 m depth lines) I get
  f ≈ 3400–4600 px. That puts the box depth at about 4 m and the robot's track gauge at about 2.2 m, a plausible
  value for a 3 m long, 2.9 m tall robot. The horizontal edge (5.8 m) is therefore the long side.

## Confidence
Medium-high for the centre-to-centre value, ±3%. The main uncertainty is whether the reference counts line centres,
inner edges or outer edges (±6%). Answer: 5.78 m.
