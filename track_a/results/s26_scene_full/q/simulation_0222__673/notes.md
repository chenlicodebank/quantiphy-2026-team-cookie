# q_673: length of the white sofa (m)

Prior: robot vacuum diameter = 0.438 m. No depth_info. The fixed camera looks straight down (top-down 2D-style
render). fps 24 = question_fps; time does not matter for a size question. Frame 77 was used (everything is static
except the robot).

## Pixel measurements (scripts in this folder)
- Robot diameter (`robot_diam.py`): circle fit to subpixel 50 % edge crossings on 180 rays, frames 30/48/60/72/77:
  120.5, 119.9, 120.1, 120.1, 120.1 px, so **120.1 px**. The scene record's 117.8 px came from a gray > 185 mask, which
  sits inside the edge, so I did not use it.
- Sofa x-extent (`edges.py`, `sofa_extent.py`, `sofa_sub.py`): right end at a sharp drop into the shadow,
  x ≈ 1452 (rows 790–810); left end against the fur rug, x ≈ 566 (rows 756–770). That gives **886 px**. A 50 %
  crossing that includes the shaded rounded ends gives 879 px. The sharp silhouette edge is the right one.
- Planar scale: 0.438 / 120.1 = 0.003647 m/px, so a planar length of 886 × 0.003647 = **3.23 m**.

## Perspective correction
The camera is not orthographic: the wall faces are visible, and the tops of tall objects shift outward from the
image centre.
- TV on the console (`tv.py`): the front face shows as a trapezoid band. Its top edge is at radius 319 px and its
  bottom edge at 298.5 px, a ratio of 1.069, so (H − h_bottom) = 15.6 × h_tv. The panel is 276 px wide. Assuming a
  16:9 TV (aspect about 1.75 with bezel), the camera is about 9.1 m above the robot top, so **H ≈ 9.2 m**
  (W ≈ 0.96 m, h ≈ 0.55 m).
- Second route, the leaning framed glass panel (top right): its top/bottom width ratio is 194/156 = 1.244, so
  h_top / H ≈ 0.20. For a floor mirror about 1.5–1.8 m tall, H ≈ 7.7–9.2 m, which agrees.
- The vase opening is offset 9.8 px radially from the body centre (Δh/(H−h) = 0.027). That fits a vase about
  0.4 m tall at H ≈ 9. The seat-seam creases on the sofa are not radial, so they are not vertical edges and I did
  not use them.
- The ends of the sofa (rounded arm rolls) are taken at h ≈ 0.55 m and the robot top at about 0.1 m. Magnification
  = (9.2 − 0.1)/(9.2 − 0.55) = 1.052.
- Corrected length = 3.23 / 1.052 ≈ **3.07 m**. Sensitivity: H 7.7–10 m and end height 0.45–0.7 m give 3.02–3.14 m.

## Answer
3.07 m. Confidence: moderate. The planar value is 3.23 m. The correction depends on the camera height, which I
inferred from the TV and mirror cues, not from a given depth.
