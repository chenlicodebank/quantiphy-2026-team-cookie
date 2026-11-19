# q_2662 — displacement of basketball between 0.4 s and 0.9 s (cm)

Frames: 0.4 s -> frame 10 (ball at rest, before kick at frame 11); 0.9 s -> round(21.6) = frame 22. File fps = question fps = 24.
Camera: f = 0.5959*1280 = 762.8 px, principal point (640,360).

## Measurements (measure.py: HSV colour mask + ellipse fit; scene/ track checked and agrees)
- Frame 10 centre (828.2, 279.6) px (record circle centre 827.5, 278.4; colour ellipse 828.3, 280.1).
  Rest ellipse 54.0 x 52.4 px (colour-only mask; ratio 1.03 = 1/cos(15 deg) off-axis stretch). Rim-inclusive bbox 56x56.
- Frame 22 centre (667.0, 397.3) px (motion blurred; blur-free minor axis ~59-60 px; neighbours 21/23 agree).
- depth_info: basketball at 0.9 s = 2.7777 m. Check: prior 23.2 cm at 2.7777 m -> 63.7 px; rim-inclusive measured ~64-65 px. Consistent.

## Depth at 0.4 s (not given)
- Route A (prior size, method-card convention): 762.8*0.232/56 = 3.16 m -> displacement 84.6 cm.
- Route B (size ratio to the given 0.9 s depth, with the off-axis sphere correction cos(15deg)/cos(4deg)):
  2.7777 * (59.3/52.4) * 1.033 = 3.24 m -> 89 cm. Without the cos correction it gives 3.16 m (same as A).
- Positions = depth * unit ray; displacement = |P22 - P10|. d10 = 3.16 / 3.22 / 3.27 m gives 84.6 / 88.1 / 91.2 cm.

## Answer
89 cm (d10 ~ 3.24 m). Confidence moderate: the depth at 0.4 s is inferred, ±3 % depth -> ±4 cm.
