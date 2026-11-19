# q_1007 – height of the plane (m)

Prior: plane speed = 22.16 m/s. 2D video, no depth_info -> one metres-per-pixel scale from the jet's pixel speed.

## Measurements (measure.py, using scene/tracks/jet.csv; checked on a zoomed, gridded frame 32 crop)
- Pixel speed: frame-to-frame rigid matching steps, frames 2-71: mean 42.08 px/frame (centre frames 25-45: 42.34).
  Vertical motion is negligible.
- Height: bbox vertical extent from the fin top (y≈312) to the lowest store tip (y≈525-526) = 214 px (median over
  the fully visible frames 12-55, range 213-217 apart from one mask dropout). Confirmed on the frame 32 crop.

## Time base
The file is 24 fps and the question states 25 fps. I used **25 fps** (question_fps). The speed prior was presumably
computed at the question's rate. As a weak plausibility check, the side-on length (≈680 px) comes out at 14.3 m at
25 fps, close to a real Harrier's 14.1 m, versus 14.9 m at 24 fps.

## Result
scale = 22.16 / (42.08 x 25) = 0.02106 m/px -> height = 214 x 0.02106 = **4.51 m**
(the centre-frame speed gives 4.48 m; at 24 fps it would be 4.70 m).
Second route: with the centre-window speed instead of the full mean, the result differs by less than 1%.
Answer: 4.5 m. Confidence: moderate. The main uncertainty is the 24/25 fps choice (4%). A smaller one is that the
silhouette height may include a little depth extent because the camera views the jet slightly from below.
