# Q556: typewriter height (m). Round 2 investigation

Prior: free fall at g = 9.8 m/s² before 0.45 s (frames 0-10). No depth_info. File fps = question_fps = 24.
Submitted: 0.193 (0.7/0.3 blend of C2 0.179 and DeepSeek 0.231). Round 1 proposed a switch to 0.176 (follows C2).

## Crux
The flat rest-silhouette height (173 px, which includes the top deck seen from above) × the fall scale gives 0.231 (C3, C5).
A perspective-corrected world height gives 0.172-0.179 (C1, C2, round 1).

## My verification (own code: edges3.py, fit3.py, overlay3.py)
- Edges: per-column 50 %-of-plateau crossings of |frame − background| at columns 900-1076, frames 0-9. The top is the
  thin top edge of the paper-rest plate. It has low contrast (≈23 levels), which is why a fixed threshold failed in my
  first try (edges2.py). The bottom is the base. Overlay: frames/overlay3.png, checked by eye.
- The camera is level, with the horizon at row 539.5 (round 1 and C2 found this from the mat edges).
- Top track, frames 0-7: a = 6730-6795 px/s², rms 0.08-0.15 px, vertex at frame −0.2. The parabola predicts frame 8
  within 1 px, so the top is one thin edge. Bottom-back track, frames 0-5: a = 6880-7020 px/s², rms ≤ 0.13 px.
  Bottom-front branch, frames 6-9: a = 7415 px/s².
- Roll: the bottom-edge slope grows steadily from 0 to 3.8° by frame 9 (≈2.9° at the crossings). For the centre
  columns this changes the extent only by a factor 1/cos ≈ 1.001, so it has no effect.
- **Route A (focal-length-free timing):** the bottom reaches eye level at frame 5.95 and the top at frame 7.465.
  h = g/2·[(t_t−t0)² − (t_b−t0)²] = 0.1763-0.1795 over 20 fit-window combinations × 3 choices of t0. **Median 0.1776 m.**
- **Route B (pixel scale at the top's depth):** the gap horizon − top at the bottom crossing, divided by a_top/g,
  gives 0.1765-0.1795 m.
- Answer: **0.177 m**.

## Rechecks
- a. Closure: the scale comes from the prior. The fall is a clean constant-acceleration parabola (rms ≈ 0.1 px). The
  front-face scale from the prior (7415/9.8 = 757 px/m) puts the mat at 0.639 m below eye level, from the rest contact
  row 1023. The extrapolated parabola then puts the bottom-front at row ≈ 982 in frame 10, and the scene record
  measured 975-982. It predicts contact at frame 10.4, and the record shows contact between frames 10 and 11. There is
  no depth_info, so g cannot be recovered independently: closure ≈ 0 % by construction, and the geometry is consistent.
- b. Plausibility: width 292 px / 757 px/m = 0.39 m, depth ≈ 0.3-0.37 m, height 0.18 m. This is a realistic portable
  typewriter. The camera sits about 0.64 m above the mat.
- c. Units: metres. All times are frames at 24 fps (question_fps = file fps).
- d. Fault proof:
  - C3/C5 (0.231): they used the 173 px rest silhouette with one flat scale. At rest the object is 300-480 px below eye
    level, so that extent includes the foreshortened top deck. The front-face height is 0.177 × 757 ≈ 134 px. The
    timing route, which needs no focal length, shows this directly.
  - C4 (0.20): its own corrected routes gave 0.188-0.194, and it then hedged toward the flat 0.234 with no measurement.
  - The submitted 0.193 is 30 % weighted on the faulty 0.231, so it is about 9 % high.
  - C1 0.172 and C2 0.179 are within 3 % of my value. No fault is needed.

## Decision
I verified round 1's switch: I reproduced the fault, and my own value, 0.1776, is within 1 % of round 1's 0.176.
The decision is a switch, following C2. Answer 0.177 m. Confidence: high.
