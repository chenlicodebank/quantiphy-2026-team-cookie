# q_669 — lampshade diameter of the table lamp (simulation_0222)

Prior: robot vacuum diameter = 0.438 m. depth_info: none. fps = question_fps = 24, so no re-timing (the answer
does not depend on time anyway).

## Pixel measurements (frame 77, scripts measure.py / hole.py)
- Lamp shade: white pleated round shade on the right end of the TV console, centred at (1190.9, 224.9).
  Bright, low-saturation mask (threshold 130–150): bbox 150 x 150 px (x 1116–1266, y 150–300), enclosing circle
  150.7, 95th-percentile tip diameter 149.4, least-squares circle 146.4 (halfway between the tips and the valleys; the
  valleys are about 143). The AABB runs to the pleat tips, so I used about 149.5 px. Overlay: frames/lamp_mask.png.
- Robot: circle fit 117.8 px, mask bbox 119 px (scene record, checked). Ratio shade/robot = 1.26–1.27, mean 1.263.
- With a single floor-plane scale (0.438/118.4 m/px) the shade comes out at 0.553 m.

## Perspective correction (the shade is elevated)
The view is a perspective top-down view: the wall faces are visible, the top-left wall corner line runs toward
the image centre, and the elevated objects show parallax.
- The shade's dark top opening sits 13.0 px radially outward from the bottom-rim circle, at rho = 391 px. That
  gives (shade height)/(H - z_bottom) ≈ 0.033. For a shade 0.25–0.35 m tall, the camera height is H ≈ 8.5–12 m.
- Vase on the console: the rim sits 8.9 px outward at rho = 368, so dz/H ≈ 0.024. A vase 0.1–0.2 m from belly to
  rim gives H ≈ 4–8 m.
- The robot's silhouette stretches radially by 0.0063 px per px of rho on the right side (robot_persp.py). For a
  robot about 0.1 m tall that gives H ≈ 15 m (noisy and asymmetric).
- The console's front-face band is only 2–3 px, which points to a large H, but the dark face may merge with the top.
Taking H ≈ 10 m, the shade's bottom rim at about 0.75–0.8 m (console plus lamp body) and the robot's silhouette rim
at about 0.09 m, the magnification correction is (H - z_shade)/(H - z_robot) ≈ 0.93. This gives 0.553 x 0.93 ≈
0.515 m. Range over H = 6–20 m: 0.49–0.535 m.

## Check
Two scale routes agree: bbox ratio 150/119 = 1.261 and tip-diameter/circle ratio 149.4/117.8 = 1.268. The
uncertainty is dominated by the camera height. 0.515 m is also a plausible size for a table-lamp shade.

Answer: 0.515 m. Confidence moderate (about ±6%).
