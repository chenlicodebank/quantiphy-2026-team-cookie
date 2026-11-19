# q1954: black cat length including tail (m)

Prior: cat speed = 1.041 m/s. No depth_info. The clip is 2D-style (static camera, and the cat walks parallel to the
image plane at constant apparent size), so I used one metres-per-pixel scale from the cat's own pixel speed.
fps is 24 in both the file and the question, so no re-timing.

## Speed (px)
I fit linear x(t) over frames 0-49, leaving out frames 26-30 (chair-leg contact). The per-frame slopes were:
- record: nose x (bbox_x1) 5.456, centroid 5.462
- my own mask (measure.py, dark fur plus nearby low-saturation pixels, overlay checked in frames/mask_24.png):
  tail-end 5.404, dark-blob front 5.447, nose 5.415, dark-blob centroid 5.381
- I took the consensus, 5.43 px/frame = 130.3 px/s, so scale = 1.041 / 130.3 = 0.00799 m/px.
  All the routes agree to within about 1%.

## Length (px)
The horizontal extent runs from the tail tip or hind paw to the nose. The tail is held upright.
- Own mask: median 107 px, ranging from 103 px (legs under the body, tail tip rearmost) to 115 px (hind leg stretched).
- Record bbox_w: median 105 px.
- I used 107 px, which gives 107 x 0.00799 = 0.855 m.

## Confidence
Moderate. The scale is solid (to about 1%). The main uncertainty is how the reference AABB treats the walking pose:
from the 103-115 px range, the answer could be anywhere from 0.82 to 0.92 m.
