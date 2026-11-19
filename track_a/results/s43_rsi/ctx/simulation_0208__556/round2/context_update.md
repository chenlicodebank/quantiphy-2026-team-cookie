# Round 2 addendum: Q556 (typewriter height)

## Established (independently re-measured with new code: edges3.py, fit3.py)
- Round 1's switch is verified. The timing route (horizon row 539.5, bottom crossing at frame 5.95, top crossing at
  frame 7.465, vertex at frame −0.2) gives h = 0.1763-0.1795 m (median 0.1776) over 20 fit windows × 3 choices of t0.
  The pixel-gap route gives 0.1765-0.1795 m.
- Accelerations: top (paper-rest plate edge) 6730-6795 px/s²; bottom-back 6880-7020; bottom-front 7415 px/s².
  All fits have rms ≤ 0.15 px. The top parabola predicts frame 8 within 1 px, so the top is a single thin edge.
- In-flight roll reaches about 3° at the crossings and 3.8° by frame 9. Its effect on the centre-column extent is
  0.1 %, which is negligible.
- Consistency: at 757 px/m (front-face scale) the parabola puts the bottom at row ≈ 982 in frame 10 (the scene record
  says 975-982) and contact at frame 10.4, which matches what the clip shows.
- Answer 0.177 m (switch, follows C2). Confidence: high.

## Ruled out
- 0.231 (C3, C5) is the flat rest silhouette (173 px), which includes the top deck. The front-face height is ≈ 134 px.
- The submitted blend, 0.193, is ≈ 9 % high because it carries 30 % weight on 0.231.

## Open
- Nothing material. The top-edge detector needs a threshold relative to the plateau because the plate's contrast is
  only ≈ 23 levels; a fixed threshold mis-tracks it.
