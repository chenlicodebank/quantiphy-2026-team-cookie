# q1438 — height of the gift box (simulation_0186)

The file rate and question_fps are both 24 fps. Prior: the slide acceleration is 3.18 m/s². Depths: 9.859 m at frame 0 and 9.741 m at frame 12.

## Focal length (cx, cy = image centre)
- **Route B (from the prior), `fit_focal.py`:** Frames 10–38 of the slide are fitted as a straight 3D line through P12, where P12 is back-projected using the 9.741 m depth, with constant acceleration along the line. The pixel rms is 0.27 px. The fitted acceleration varies as about 1/f, and it equals 3.18 m/s² at **f ≈ 2200 px**.
- **Route A (free fall, g = 9.81), `height.py`:** Frames 0–8 are fitted with a level camera, since the post, sign and box edges are vertical in the image and the fall path stays at x = 554 px. This gives f = 2158 px with rms 0.29 px, which is 2% from route B. A fit that also frees the camera pitch is degenerate and gives 2286.
- f = 2200 is used (it comes from the exact prior).

## Box height
- I segmented the box myself, by difference against frame 30 where this region is background. The mask overlay is in `frames/mask0.png`.
- The silhouette's vertical extent, including the bow (the top of the bow down to the lowest box corner), is 139–142 px in frames 0, 2, 4, 6 and 8. I use 139.5 px. The box does not rotate during the fall.
- Frame 0 camera depth: Z = 9.859 / |r| = 9.675 m.
- Height (world AABB vertical extent, bow included) = 139.5 × 9.675 / 2200 = **0.613 m**.
- Alternative readings:
  - Body without the bow: 121 px, which gives 0.53 m.
  - Using route A's f = 2158: 0.625 m.

Confidence: moderate. The main uncertainty is the convention, i.e. whether the bow is included and whether the tilted box's AABB or its own edge is meant. The scale itself is good to about 2%.
