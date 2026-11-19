# Q406 — acceleration of the astronaut at t = 2 s (frame 48)

fps = question_fps = 24, so t = 2 s is frame 48. This is a 2D render with a static camera, and the body length stays constant (~91 px), so there is no depth change.

Scale: astronaut height is 2.2 m. The upright figure at frame 0 measures 91 px tall at mask threshold 15/25, 90 px at 40 and 89 px at 60. I used 90.5 px, which gives 0.0243 m/px.

Motion (measure.py, using the centroid track from scene/tracks/astronaut.csv, which I re-checked):
- The path is a straight line (~3° right of vertical). I projected the centroid onto that line.
- Route 1: I fitted a Blender-style ease-in/ease-out cubic (3u²−2u³) between two keyframes. The fit gives f0 = −0.3, f1 = 78.2, D = 274.8 px, with an RMS of 0.27 px, so the model matches very well. From the fit, speed at frames 47 and 48 is 5.056 and 5.001 px/frame, so a = −0.055 px/frame².
- Route 2: local cubic polynomial fits around frame 48 (half-widths 6–12 frames) give −0.058 to −0.067 px/frame².
- The raw one-frame difference is −0.59 px/frame². That is centroid noise (±0.3 px per step), so I did not use it.

Result: a ≈ −0.056 px/frame² × 576 × 0.0243 m/px ≈ −0.78 m/s². The astronaut is slowing down, and the answer is the magnitude: **0.78 m/s²**.
Confidence: moderate. The smoothstep fit is excellent, and the two routes differ by ~5%.
