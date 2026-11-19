# q_1825 – width of the football (m)

2D simulation clip (segmented), 24 fps file = question_fps 24, 32 frames. Prior: g = 9.8 m/s^2, depth_info none.

## Scale (measure.py)
Football falls straight down from rest (x constant ±2 px). Re-measured the mask centroid (min RGB < 240,
largest component at x >= 880) every frame and fitted y = a/2 f^2 + v0 f + c:
- frames 0-31: a = 3.1216 px/frame^2 (rms 0.55 px); 0-25: 3.1209; 2-25: 3.1231; 0-15: 3.1122; 16-31: 3.1259.
- a = 3.121 px/frame^2 × 24^2 = 1797.7 px/s^2 → 9.8 / 1797.7 = 0.005452 m/px.
The windows agree to within 0.4 %, so the scale is solid.

## Ball width in pixels (measure.py, width_axis.py)
The long axis is roughly vertical (88-99°), so the horizontal (AABB) width = short diameter.
- Bbox width and the extent across the principal axis: frames 0-15 ≈ 44-47 px (bluish segmentation fringe on the
  left edge, odd foreshortened look), frames 16-25 ≈ 39-41 px (cleanest side view, e.g. frame 24),
  frames 26-31 ≈ 44 px (grey silhouette with a dark rim). Median over all frames is 43-44 px; on the clean frames it is 40.4 px.
- I used about 42 px (between the clean-frame value and the overall median; the <240 threshold
  also takes in about 1 px of antialiased edge) → 42 × 0.005452 = 0.229 m.
  Range: 0.220 m (clean frames) to 0.242 m (all frames).

## Check
Length on the same scale is 0.33-0.35 m (61-65 px). Width/length = 0.66, close to a real football's ~0.61.
The ball is about 1.2-1.3× a regulation football (0.28 × 0.17 m). That is within the plausible range, so I kept
the prior's scale (2D convention: a single m/px value from the prior).

Answer: 0.229 m. Confidence: moderate, about ±5 %. Most of the uncertainty is the pixel width (mask edge and
segmentation artefacts), not the scale.
