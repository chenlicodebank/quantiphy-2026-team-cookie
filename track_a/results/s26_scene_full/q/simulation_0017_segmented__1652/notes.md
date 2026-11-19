# q_1652: width of the pedestal (square base) of the central sculpture

The file's frame rate and question_fps are both 33. The camera is static and level: the dark block's vertical sides
are parallel in the image, with a constant 250 px width from row 608 to row 692.

## Focal length (focal.py)
- The person's pelvis x comes from scene/tracks/person.csv (pelvis_x_raw), fitted with a straight line, so that the
  extrapolated frame 0 (head cut off) is not used directly. The fit gives u ≈ 1-2 px at t=0 and u ≈ 252 px at t=1
  (frame 33). v ≈ 541, and the principal point is assumed at (540, 540).
- Route A (independent of the prior): assume the person walks parallel to the image plane, so Z is constant. Then
  5.424 at t=0 and 4.886 at t=1 give f = 898-906 px, with Z = 4.65 m.
- Route B (uses the prior): the 3D displacement over 1 s equals 1.3 m. This gives f = 894-918 px, depending on the
  fit window.
- With f from route A, the reproduced 1-s displacement is 1.297-1.309 m, against the 1.3 m/s prior. Adopted value:
  f ≈ 902 ± 8 px.
- Sanity check: the person is 364 px tall at Z = 4.65, which is 1.88 m. The camera height is about 0.99 m.

## Pedestal pixel width (measure_ped.py)
I measured the non-white run through x = 530, row by row, on frames 5, 10 and 15 (the person is far away).
- The dark square block spans x 405-654, which is **250 px** (stable over rows 616-692).
- The lighter part above it (rows 552-596, 189-223 px wide) is a narrower tapered tier. It does not set the
  bounding-box width.
- The bbox 395-664 in scene/static_extents.json is about 10 px too wide (halo or shadow). I corrected it to 405-654.

## Metric width
- The pedestal origin is at a distance of 5.963 m. It lies on the optical axis horizontally (u ≈ 529.5). Vertically
  it is about 60-120 px below the image centre (estimated pedestal centre height), so Z_c ≈ 5.91-5.95 (I use 5.94).
- The block is square, so its front face is at Z_c − w/2. Then w = 250·(Z_c − w/2)/f, which gives
  w = 250·Z_c/(f + 125).
- f = 900, Z_c = 5.94 gives w = 1.449 m. Over f = 895-915 and dv = 0-120 px the range is 1.42-1.46 m.
- Other reading: if the face were at the origin's depth (no square-depth correction), the width would be 1.64 m. I
  rejected this, because the question says "square base" and the origin is at the box centre.
- Consistency checks:
  - The front face is at Z ≈ 5.22 m, behind the person (Z 4.65), and the person does occlude the pedestal.
  - The floor at that depth projects to y ≈ 710, which is hidden behind the bench top (697). This is consistent.

Answer: **1.445 m**. Confidence: moderate-high, about ±3%. The main uncertainties are f and the vertical position of
the origin.
