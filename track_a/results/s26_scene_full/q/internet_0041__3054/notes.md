# q_3054 – displacement of the middle duck (cm)

Prior: middle duck size = 66 cm, taken as its bill-to-tail length (the long axis, which is also the direction it swims).
Internet video, 2D planar convention, one scale. The camera is nearly static (background shift < 1 px in x, -6 px in y
by frame 51). The clip runs frame 0 to 51; question_fps 24 ≈ file fps 23.98, and the time base does not matter for a displacement.

## Pixel length of the duck (scale)
- Scene mask bbox_w: median 127 px. The mask cuts off the pale tail-tip feathers on several frames.
- Read by eye from zoomed grids (bill to tail tip): frame 0 ≈ 131 px, frame 25 ≈ 139 px, frame 51 ≈ 136 px.
- Value used: L ≈ 133 px (between the mask value and the full tip-to-tip reading), so 0.496 cm/px.

## Displacement, frame 0 to 51 (disp.py)
- Mask centroid: dx -174.0, dy +9.8 → 174.3 px.
- Template matching of the duck body, frame 0 ↔ 51, run forward and backward: (-171, +11) → 171.4 px.
- Bill (bbox_x0): -177 px.
- Value used: 173.5 px.

Answer = 173.5 × 66 / 133 ≈ 86 cm. With L = 127 it would be 90 cm; with L = 137 it would be 84 cm.
Confidence: moderate. The main uncertainty is the pixel length the annotator used for the prior (about ±4%).
