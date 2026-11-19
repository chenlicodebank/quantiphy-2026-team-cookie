# q_2760 — diameter of the white ball (cm)

File fps = question_fps = 24, so t=1.5 s -> frame 36 and t=2.0 s -> frame 48. Lab camera: f = 0.5959*1280 = 763 px, centre (640,360).

## What the object is
scene/ calls it an oblong toy. That is wrong. In the slow in-hand frames (crop frames/c2_8_*) it is a **sphere** (the hand
cutout bites into it). Its oblong look in flight is motion blur along the motion direction. Check: (length along motion - width)
≈ 0.8 x per-frame displacement in frames 29, 36, 45 and 48 (exposure ≈ 0.8 frame). So the diameter = the half-max width
**perpendicular to the motion** (perpw.py, edge36.py).

## Measurements (half-max edges)
- Frame 36 (t=1.5, d=0.7045 m, almost on the optical axis, cos a = 0.99): motion is horizontal, so the vertical extent is the diameter.
  The top edge is at y=337.6. The bottom is hidden where the ball overlaps the cup rim. Against the black background the bottom is
  already at y≥379.6 at x=738 and still dropping, so the diameter is 42-44 px or a little more.
  D = 0.7045*42..44/763 = 3.9-4.1 cm (Z-based: 3.84-4.02 cm).
- Frame 48 (t=2.0, d=0.627 m, far off axis, cos a = 0.81, diagonal blur): perpendicular width 54.8 px.
  Method card (d*px/f): 4.50 cm. Off-axis pinhole correction (Z = d cos a, ellipse factor 1.11): 3.27 cm.
- Card check of the depth convention: the navy credit card (d=0.69) is ~105 px long. Z-based prediction 103 px; d-based 95 px.
- Perpendicular widths in other frames: f29 35.8, f45 45.0, f43-47 47-54 px. The width depends somewhat on the blur direction.

## Second route
I fitted 3D ballistic arcs (known g, f=763) to the pixel track (ballistic.py; rms 0.9 px). It gives distance 0.677 m at
frame 36 (given 0.7045) but 0.83 m at frame 48 (given 0.627). Diameters from those depths: arcs 1 and 3 give 4.4-5.0 cm,
arc 2 gives ~3.6 cm. The depth along the line of sight is weakly constrained, so this check is only loose.

## Answer
The two given ball depths do not agree with a constant ball size (they differ by ~10-25% depending on the convention).
Frame 36 is the cleanest: on-axis, so both depth conventions agree, and the blur does not affect the vertical width.
It gives 3.9-4.0 cm. The other routes scatter from 3.3 to 4.6 cm around it. Answer: **4.0 cm** (a ping-pong-ball size is a sanity check).
Confidence: moderate (±10%).
