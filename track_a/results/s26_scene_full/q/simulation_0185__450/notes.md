# Q450 – height of the gift box (m)

Prior: the box's acceleration after 1 s is 3.18 m/s² (it is sliding down the ramp then). This is a 2D scene, the camera is static, and fps = question_fps = 24.

## Scale (acc.py)
- Box path length along the ramp (track ref point, frame 38 duplicate fixed), quadratic fit:
  frames 10–37 give 1.293 px/frame² = 745 px/s². Subwindows 10–24 give 749, 14–34 give 747, 24–37 give 692.
- Scale = 3.18 / 745 = 0.00427 m/px.
- Independent check: the free fall in frames 0–8 gives 2277 px/s², and 9.81 / 2277 = 0.00431 m/px (1 % apart).
  So the prior is consistent with g, and the motion is in one plane.

## Box size in pixels (size.py, zoomed frames 0 and 24)
- The record's "110 px cube face" was wrong. It included the perspective side face, which is visible at the
  right because the box sits left of the image centre.
- Front face corners at frame 0 are about TL(467,321), TR(549,366), BR(507,446) and BL(429,401). The edge along the
  ramp is about 92 px (frame 24, near the image centre, gives 93.5 px) and the edge along the box's up axis is about
  89 px. The box is tilted 28.6° (the bottom face is parallel to the ramp) and does not rotate.
- Side-face strip is about 16 px, which gives f ≈ 2300 px and Z ≈ 10 m. The front face is therefore about 2 % closer
  than the origin, so I scaled it down by 1.02.
- World AABB vertical extent of the tilted body: 92 sin28.6 + 89 cos28.6 ≈ 122 px. The image shows about 125 px
  (y 321 → 446). I used 123 px, which gives **≈ 0.515 m**.
- World AABB including the bow: bow top y ≈ 304 to bottom corner y ≈ 447, so 143 px, which gives **≈ 0.605 m**.
- Readings without the tilt: the body's own up-axis height is 89 px (≈ 0.37 m); with the bow it is about 125 px (≈ 0.53 m).

## Answer
I followed the world-space AABB convention. It is unclear whether the bow is part of the box object, so I answered
0.55 m, between the body-only (0.515 m) and with-bow (0.605 m) extents. Confidence: medium. The scale is solid (±2 %);
the size definition is the main risk.
