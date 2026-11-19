# q_2730 — diameter of the white ball (cm)

The video is a lab capture at 24 fps (file fps = question_fps = 24). Focal length f = 0.5959 × 1280 = 762.75 px, and the principal point is taken at the image centre.
Formula: diameter = depth × pixel diameter / f, using depth_info: t=1 s → frame 24, 1.014 m; t=1.5 s → frame 36, 0.737 m.

## Measurements
- `measure_ball.py` builds a threshold mask (difference from the empty frame 48, bright and unsaturated). This mask under-reads the shaded bottom (h < w even at rest), so it biases the diameter low:
  - circle fit: 26.76 px at frame 24 (3.56 cm) and 39.29 px at frame 36 (3.80 cm)
  - perpendicular-to-motion extent: 3.52 and 3.79 cm
- `radial.py` is the main route. It finds sub-pixel half-max edges along 47 radial rays over the left, top and right of the ball, skipping the shaded bottom that sits against the shadow, then fits a circle to them. Half-max edges are not shifted by box motion blur. The overlays in frames/rad_24.png and rad_36.png show the fit following the outline (rms 0.5–0.7 px).
  - frame 24: 28.54 px → **3.79 cm** (mean of frames 23–25: 28.76 px → 3.82 cm)
  - frame 36: 41.68 px → **4.03 cm** (mean of frames 35–37: 41.3 px → 3.99 cm). Frame 36 follows a probable dropped frame (35→36 jump). Frame 35 at the same depth gives 3.78 cm.
- Scale check with the credit card (the prior): at 0.6867 m, 85.6 mm should be 95.1 px. Measured on frame 48, the long edge is about 94 px on the far edge and 101 px on the near edge (mean ≈ 97). That is consistent within about 2–3%, so f and the depths agree.

## Answer
The mean of the two depth-time routes (half-max fit) is ≈ 3.9 cm. This is consistent with a table-tennis-sized ball (4.0 cm). The mask-based routes read 3.5–3.8 cm and are biased low by edge loss.
Confidence: moderate. The likely error is ±5%.
