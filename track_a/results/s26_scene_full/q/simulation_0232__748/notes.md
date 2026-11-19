# q_748 – width of the chair next to the blackboard

**Answer: 0.50 m**

## Which chair
I couldn't see a separate blackboard anywhere in the frame (checked the full frame and a crop of the left edge). The
large grey front wall is the only board-like surface. The chair "next to" it is the orange/wood chair standing against
the wall at the far right (x ≈ 1598–1795, back top y ≈ 738, seat ≈ 885, feet ≈ 1015–1023). The two dark-red chairs
are foreground student chairs, away from the wall. Confidence in this identification: moderate.

## Scale (2D scene, prior = cat speed 0.714 m/s, fps 24 = question_fps)
- `measure.py`: cat root speed from scene/tracks/cat.csv (torso centroid). Mean of the per-frame speeds is 220.6 px/s.
  Net displacement / time is 218.5 px/s, and a linear fit gives 215.0 px/s. The per-frame mean is pushed up by
  centroid jitter, so I used about 219 px/s, giving **3.26e-3 m/px** (the range across the three estimates is 3.24–3.32e-3).
- Depth: the chair's feet (y ≈ 1017–1023) are at about the same floor row as the teacher-desk legs (≈1025). The cat
  walks on that desk, so the chair and the cat are at about the same depth, and one scale fits both.

## Chair pixel width (`measure.py`, `legs.py`, frame 24)
- I masked orange pixels (R−B>25). The back panel spans x 1598–1753 (rows 760–800), about **153 px** side to side.
  The seat's front edge is 1648–1791 (143 px). The legs are at 1653 and 1792 (front) and ~1610 (hidden) and 1752
  (back), inset from the edges. The front of the seat is shifted about 42 px to the right because of perspective
  (front-to-back depth), so the overall image bbox (≈197 px) does not give the width.
- Width = 153 × 3.26e-3 = **0.499 m**.

## Checks
- Sanity check with the same scale: the back's top to the floor is ~280 px, or 0.91 m (chair height). The seat height
  is ~135 px, or 0.44 m. Cat nose to rump is 186 px, or 0.61 m. All of these are plausible, so the scale is consistent.
- Ambiguity: width here means the side-to-side extent (≈0.50 m). This view cannot measure the front-to-back depth
  without a focal length. A typical stacking chair's depth (~0.5 m) is about the same, so either reading gives ≈0.5 m.
- Uncertainty is about ±5% (scale ±2%, pixel extent ±2 px, plus the risk of choosing the wrong chair).
