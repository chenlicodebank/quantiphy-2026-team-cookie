# q_473 — height of the box (simulation_0192)

Prior: the box falls with a = 9.8 m/s² before 0.6 s. No depth_info. question_fps = 120, which is the same as the file fps.

## Scale from the fall (2D: one m/px scale in the box's front-face plane)
- Camera is static and level. The front-face width stays at 281.6 ± 1 px through the whole fall (width.py), so the
  depth does not change and the vertical projection is linear.
- Box track: cy_ref (front-face texture, NCC template) from scene/. I checked it with high-pass texture matching
  (hpmatch.py). Five sub-patches all give a shift of 226.4 px at frame 57 and 264.5 px at rest, with no scale change.
  The track is good. The face-top silhouette edge moves 5 px less because of a thin flap band that only shows at rest.
- The video frames show sim states k or k+1 (duplicate frames followed by double steps). I gave each frame its
  sim-step index and fitted a parabola (assign.py). Result: a = 2066–2070 px/s², rms 0.10 px.
  Single-step-difference slope (fit3.py): 2046–2074 px/s². I use **a = 2066 px/s²**, so the scale is
  9.8/2066 = **0.004743 m/px**.

## Box height in pixels
- Front-face (body) height: front-top 61.7 to front-bottom ≈261.5 at frame 0, where the underside trapezoid starts.
  At rest, mapped to texture coordinates, the bottom is at 260. Body height ≈ **199.5 px**, or 204.5 px with the
  thin band seen at rest.
- The open lid flap (dark, top-right, free edge near the centre seam) rises to y = 43.5 at frame 0 and 307.5 at rest.
  It moves rigidly with the box (264 px). Top of the AABB is at the flap tip: about 217.5 px from the flap tip to the
  box bottom.
- Heights in metres:
  - body only: 199.5 × 0.004743 = **0.946 m**
  - world AABB including the raised flap: 217.5 × 0.004743 = **1.032 m**
  - Cross-check: width 281.6 px = 1.336 m, which is a plausible large carton.

## Answer
The convention is the world-space AABB, so I favour 1.03 m, but the flap may not be meant to count. I answer
**1.00 m**: 3 % from the AABB reading and 5.5 % from the body-only reading.

Confidence: the scale is good to about ±1.5 %. The main uncertainty is whether the raised flap counts (±4 %).
