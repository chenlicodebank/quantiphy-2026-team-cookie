# q_439 — width of the box (simulation_0181)

Prior: acceleration of the box at t = 0.75 s (frame 18, 24 fps) = 2.338 m/s². No depth_info.
fps = question_fps = 24, so there's no re-timing issue.
Time base check: free fall measured at 2510 px/s². With the prior's scale that gives g = 9.70 m/s², so 24 fps is physically right.

## Scale from the prior (sliding acceleration)
- The scene/ record's centroid track gives ~700 px/s². That value is biased because the silhouette changes:
  the box is still settling between frames 12 and 20, and the ramp's front edge hides the box's lower part.
- Re-measured with frame-to-frame masked template matching (`track_pair.py`). Per-frame steps along the ramp
  are smooth (18.8 → 40.5 px/frame), and a linear fit of speed vs frame gives:
  602 (frames 13–32), 611 (14–28), 608 (15–30), 609 (20–30) and 599 (14–24) px/s².
  Adopted a_px = 605 ± 6 px/s².
- Scale = 2.338 / 605 = 0.003864 m/px. The template is mostly the front face, so this scale applies at the
  front-face depth.

## Box pixel width
- Free fall (`edges_fall.py`, frames 1–2): the silhouette (327 px, x 378–704) is the front face plus a right side
  face, plus a bottom strip. These extra faces show because the camera faces the wall square-on, with the principal
  point at the image centre, and the box sits up-left of centre.
  - Front-face left edge: x = 377.5.
  - Front/side edge: x = 655 (strongest vertical gradient).
  - Front face width: 277.5 px.
  - Side face runs from 655 to 704.
- While sliding, the box image was rotated back by 28.5° (`face_edges.py`). The face width settles at
  279, 276, 277 and 277 px (frames 20–26), matching the fall value.
- SIFT matching between fall and slide frames (`sift_scale*.py`) gives texture scale 0.99–1.02 with 28.5° rotation.
  So it's the same face at the same depth, and one scale holds throughout.
- W_px = 277.5 ± 1.5 px.

## Which dimension is "width"
- Depth: the side face (655 → 704, measured from the image centre at 960) and the bottom face (420 → 440, measured
  from 540) both give D/Z_front ≈ 0.19–0.20.
- Focal length: the floor bolt rings are ellipses with axis ratio ≈ 0.18–0.21 (`floor_rings.py`). The pinhole model
  for those ratios gives f ≈ 2000–2300 px.
  - That makes D ≈ 0.195 × f × 0.003864 ≈ 1.5–1.7 m, longer than the front face (D < W would need f < 1420 px).
- So the front face's horizontal extent is the shorter horizontal extent, i.e. the width.
  - Reading "image-horizontal extent of the visible face" gives the same value.
  - Reading "depth" would give ~1.6 m, which is the length.
- Height (front face 229 → 420 px) ≈ 191 px ≈ 0.74 m.

## Result
- Width = 277.5 px × 0.003864 m/px = **1.072 m**.
- Second route (gravity): the free-fall front-face texture accelerates at 2510 px/s² from rest at t = 0.
  With g = 9.81 the scale is 0.003908 m/px, so width = 1.085 m (1.2% from the prior route).

Confidence: about ±3% on the face-width value. The main residual risk is the width/length interpretation,
which rests on the focal-length estimate from the floor rings.
