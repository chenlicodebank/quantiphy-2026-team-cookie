# Q974: width of the raccoon (m)

- The prior gives the raccoon's length, tail included, as 1.51 m. The clip is 2D: a top-down camera, static, and fps = question_fps = 24.
- **Scale:** the median nose-to-tail-tip length over all 72 frames is 295 px (scene/tracks/animal.csv bbox_w; p10–p90 is 285–300). It matched what I saw on a zoomed frame at t = 1.5 s. Scale = 1.51 / 295 = 0.005119 m/px.
- **Width:** the shorter horizontal extent runs across the body, which is the image y extent because the raccoon walks along +x.
  - Record mask, which excludes the shadow: median bbox_h is 66.5 px (p10–p90 62–75, including leg swing). The body alone is about 62 px.
  - Zoomed frame at t = 1.5 s: the body runs from about y = 698 to 760, so roughly 62–66 px. The top edge is about y = 697 in every frame, which matches my own threshold run (measure.py).
  - measure.py's plain colour-difference threshold also picks up the raccoon's shadow at the lower-left. Its lower edge is therefore biased, and I used it only to check the top edge.
- **Answer:** 66.5 px × 0.005119 = **0.34 m**. This is the bounding box including the legs, which is the AABB convention. The body-only reading is 62 px, or 0.317 m.
- **Confidence:** moderate, about ±7%. The main uncertainty is whether the legs count and the ±5 px error in the length.
