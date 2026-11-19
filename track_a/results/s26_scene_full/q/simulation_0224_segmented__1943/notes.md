# q_1943 - length of the chinese chess board (m)

Prior: chess piece diameter = 0.097 m. No depth_info. fps 24 = question_fps; the question asks for a static size, so
re-timing does not matter.

Scene: the "ramp" in scene/ is the chess board. It is seen almost edge-on and tilted 26 deg in the image. The "block"
is the chess piece: a disc lying flat, seen at a grazing angle, so its silhouette is diameter x thickness. The piece
slides along the board's long axis, so I measured the piece diameter and the board length along the same image axis,
u = (-0.899, 0.438).

Measurements (scripts measure.py, piece.py, profile.py):
- Board: silhouette at frame 44 (piece gone), pixels counted where the difference from white is > 40. Extent along u
  = 1059.6 px. The extreme points are the two rounded tips of the near top rim, (1380,495) and (425,954). The lower
  mouldings and feet stop 38-45 px short of these tips, so tip-to-tip along the rim is the board's length. This
  matches the scene record (1060 px).
- Piece diameter along u: mask taken against the empty-board frame, frames 0-36. Medians: threshold 15 -> 81.8 px,
  threshold 25 -> 79.2 px, threshold 40 -> 77.0 px. Half-contrast chord profiles in the clean frames 16-36 give
  74-77 px. The scene record gives 81.3 px, which includes the shaded side and anti-aliasing.
  Adopted D = 77 px (+-3).
- The piece's apparent size stays the same along the whole board, so there is no depth change along the length.
  The piece's base sits in the near part of the visible top strip, so I treated the depth difference between the near
  rim and the piece as negligible and applied no perspective correction.

Answer = 1059.6 / 77 x 0.097 = 1.335 m.
Sensitivity: D 75 -> 1.37 m, D 79 -> 1.30 m, D 81.3 (record) -> 1.26 m.

Second route: the record's own numbers (1060 / 81.3 px) give 1.26 m. A board/piece ratio of about 13.5-14 is
plausible for a xiangqi board (a real board is about 0.5 m with pieces about 3.5 cm across).
Confidence: moderate, about +-5%. The main uncertainties are where the piece's edge lies and possible perspective
between the near rim and the piece.
