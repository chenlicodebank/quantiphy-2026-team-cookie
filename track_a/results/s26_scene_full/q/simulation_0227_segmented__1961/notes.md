# q_1961: acceleration of the "red general chess" at t = 0.5 s

Prior: the black cat's speed is 1.041 m/s. There is no depth_info. fps = question_fps = 24, so t = 0.5 s is frame 12.

## Object identity (main uncertainty)
No chess piece appears in the clip. scan.py found no red pixels and no connected component other than the chairs, the cat
and the flamingo float. The only moving object other than the prior's cat is the flamingo float, and it is the only
object that accelerates. I assumed the question's "red general chess" label refers to it.

## Scale (2D convention)
- Cat: a linear fit to the centroid x over frames 0–49 (scene/tracks/cat.csv) gives 5.465 px/frame. A fit to the nose
  edge gives the same, 5.463. The walk is steady: 5.59 px/frame in frames 0–24 and 5.34 in frames 24–49.
- Scale = 1.041 / (5.4646 × 24) = 0.007937 m/px. This is one scale for the whole clip, as the 2D convention requires. If
  the float is nearer the camera than the cat, the true value would be lower.

## Float acceleration at frame 12
- Tracks: the record's centroid track, plus my own track of the coloured pixels below y = 905 (measure.py), which
  avoids the chair legs. The two agree.
- The motion fits an ease-in/ease-out (smoothstep) curve with keyframes at frames about 0 and 49.1, D = 429.6 px, with an
  rms error of 0.42 px. On that curve, speed(12) − speed(11) = 0.590 px/frame², which gives 2.70 m/s².
- Polynomial fits to the per-frame speeds (vfit.py: degree 2–4 over frames 1–24, 1–30 and 0–48), evaluated at frame
  11.5, give 0.565–0.576 px/frame², which gives 2.58–2.63 m/s². Narrow local windows give 0.48–0.55 px/frame²
  (2.2–2.5 m/s²), but they are noisier.
- Answer: 0.57 px/frame² × 576 × 0.007937 = **2.60 m/s²**.

## Confidence
The pixel measurement is good to about ±5% across the methods. The main risks are that the asked object may be
misidentified, and that the cat and the float may be at different depths.
