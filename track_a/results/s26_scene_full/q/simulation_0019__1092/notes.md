# Q1092: height of the pedestal (square base) of the central sculpture

**Answer: 0.635 m.** This is the dark square base box. The other reading is given below.

## Structure seen in the video
The image is rotated: world up points to image −x. The sculpture sits on two blocks:
- **Dark charcoal box** (the square base):
  - Front face spans image x 766.7 to 895.7 (129.0 px tall) and y 446.6 to 747.8 (301 px wide). Edges were found to subpixel precision by `edges.py`.
  - Its side edges are exactly parallel along x, so the camera pitch is about 0.
  - The receding left edge of its top face (a grey wedge at x 720–767) runs to a vanishing point at x ≈ 538, about the image centre. This confirms pitch ≈ 0, so the horizon is at x ≈ 538.
- **Tapered light-stone block** on top of the box:
  - Its front face is about flush with the box front and spans x 702 to 767.
  - Its sides lean inward by roughly 0.2 px per px.
  - Its lit top face is at x ≈ 670–700, and the sculpture stands on it.

## Scale (3D pinhole)
- **Focal length, route 1 (two person depths):** the person walks parallel to the image plane. Requiring the same camera-z for d = 6.84 m (frame 0, pelvis (655.5, 197.7)) and d = 6.49 m (frame 33, pelvis (657.5, 382.0)) gives f = 888 px and z = 6.336 m at both times.
- **Focal length, route 2 (person height):** 1.87 m corresponds to about 260 px (head top 521 to soles about 782–784, feet-together frames). This gives f = 881 px, which agrees with route 1 within 1%.
- **Camera height:** (784 − 538) × 6.336 / 888 = 1.75 m. The implied pelvis height is 0.92 m (0.49 × 1.87), which is plausible.
- **Pedestal front face depth:** z = 6.336 × 245.7 / 357.4 = 4.36 m, from where its bottom edge meets the floor.
- **Dark box height:** 129 × 4.36 / 888 = **0.632 m**. With route 2's focal length it is 0.638 m.
- **Width check:** 301 px corresponds to 1.48 m wide. The box is plausibly square in plan.

## Second route (no focal length)
On a level camera, ratios of floor-referenced pixel extents give the height directly:

H = 1.87 × (x_feet − x_hor) / h_person_px × (x_bot − x_top) / (x_bot − x_hor)

- Over h_px = 258–262 and x_hor = 528–548, this gives 0.625–0.651 m.
- The central value is 0.638 m.

## Ambiguity
- **Dark square base alone: 0.635 m.** This is the answer. "(square base)" points to the box: it is the square block, while the stone part is a tapered cap.
- **Whole plinth (dark box plus tapered stone block up to x ≈ 702): about 0.93–0.95 m.**

The pedestal and sculpture have the same given distance (5.085 m). This suggests they share one asset origin, so the given distance cannot tell the two readings apart. With an unknown origin height and plinth depth, the geometry is consistent with 5.085 m in both cases.

## Time base
No timing is needed. t = 1 s is frame 33 at both 33 fps and 33.26 fps.

## Confidence
- **Dark-box reading:** moderate to high. The measurement error is about ±3%.
- **Main risk:** which part the question means.
