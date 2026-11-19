# q_237: width of the football (m)

The scene is a 2D Blender render. The football falls straight down in front of a flat wall. The prior is gravity = 9.8 m/s². The video file runs at 24.006 fps; every time and frame conversion here uses question_fps = 24.

## Scale (fit.py)
- I fitted a quadratic to the ball's vertical centroid y(t), with t = frame/24, over frames 0–31 (frame 17 left out).
- The fitted acceleration is 1799 px/s², with a residual RMS of 0.4 px. Using `bbox_cy`, or starting the fit at frame 3, gives values within 0.1 %.
- Scale: 9.8 / 1799 = **0.005447 m/px**.
- Sanity check: the doors (155 × 342 px) come out at 0.84 × 1.86 m, which is plausible.

## Pixel width of the ball
- The ball's long axis is roughly vertical and tilted toward the camera, so we see an end cap. Its horizontal extent therefore equals the ball's diameter, which is the asked width.
- The scene record's mask width (39 px) and the background-difference edge profile (41–42 px) both include a dark, blue-tinted shadow on the wall. The shadow runs along the ball's left side and below it, and is clearly visible in `frames/crop_6.png`. That widens the measurement by about 4–6 px.
- Measurements that exclude the shadow:
  - Visual reading of a 10× crop of frame 6: brown ball from x ≈ 1020.5 to 1055.5, about 35 px.
  - Blue-chromaticity edges, B/(R+G+B) at thresholds 0.40 / 0.42 / 0.44 (width4.py): medians 32.4 / 34.1 / 35.7 px over all frames.
  - Linear colour unmixing at both edges, which preserves area under the chroma blur (width5.py): median 34.1 px, mean 34.2 px, spread ±1.9 px across frames.
- Adopted width: **34.5–35 px**, uncertain by about ±1.5 px.

## Answer
- 35 × 0.005447 = 0.191 m, and 34.5 px gives 0.188 m. **Answer: 0.19 m.**
- Cross-check: the apparent length (61–63 px, foreshortened) is ≥ 0.34 m, so this model ball is about 1.2× a regulation ball (0.28 × 0.17 m). A width of 0.19 m fits that.
- Confidence: moderate, about ±6 %. The main uncertainty is where the ball's left edge is against its own shadow.
