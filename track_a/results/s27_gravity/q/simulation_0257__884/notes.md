# q 884 – width (diameter) of the plant, simulation_0257 (2D)

Prior: acceleration of the plant before 0.5 s = 9.8 m/s^2. depth_info: none. File is 24 fps, question_fps = 30 —
all time conversions use 30 fps, as the instructions say (one frame = 1/30 s).

## Method (measure.py)
- Free fall during frames 0–14 (impact at frame 15). Fitted a quadratic in frame number to four vertical tracks:
  the subpixel bottom edge (re-measured here), the integer bottom edge, the mask centroid and the bbox centre from scene/,
  over several frame windows (0–14, 1–14, 0–11, 3–14). a = 6.93–7.08 px/frame^2; the values cluster around
  **6.98 px/frame^2** (fit rms 0.3–0.9 px).
- At 30 fps: a = 6.98 x 900 = 6283 px/s^2 -> scale = 9.8 / 6283 = 1.560e-3 m/px.
- Width: horizontal extent of the whole pot+plant (the rim and the leaf rosette are about equally wide), half-threshold
  subpixel edges on frames 0–5 give 46.6–47.4 px, so I use **46.8 px** (scene record: 47 px bbox, pot body 46 px).
- Width = 46.8 x 1.560e-3 = **0.073 m**.

## Checks
- Agreement between routes: the centroid-based and edge-based accelerations differ by about 1 pct, and the width
  readings by about 1 pct.
- If the clip were timed at the file's 24 fps instead, the result would be 0.114 m. I followed question_fps (30), as
  instructed. 7 cm is small but plausible for a small succulent pot. 2D scene, so one px scale applies.

Confidence: good (about ±3 pct) under the 30 fps convention.
