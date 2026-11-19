# q_1620 — height of the dog (including its tail), metres

File fps = question_fps = 24, so the scene/ frame numbers are used directly.

## Focal length (focal.py)
- Cat origin approximated by the scene/ core centroid. Its positions were back-projected at t=0 (frame 0, d=4.199 m) and
  t=1 s (frame 24, d=4.481 m), with the principal point at the image centre.
- Solving |P24 − P0| = 0.94 m gives f ≈ 2150 px. Other choices of reference point and frame give 2099–2156 px (frame 23 or
  24; core, centroid or bbox centre). That is a horizontal FOV of about 48°.
- Check (height2.py): with f = 2150, the level-camera model gives a net cat speed of 0.954 m/s from frame 0 to frame 23.

## Camera and floor
- The camera is almost level (horizon near y = 540). Floor points satisfy Z·(v − 540) ≈ const:
  - mirror bottom centre (1500, 815) at 6.407 m → 1694
  - cat feet at frame 0 → 1686
  - camera height ≈ 0.79 m.
- Dog origin (core centroid) follows the same rule: Z·(v − 540) = 953 at t=0 and 961 at t=0.5. The two given dog depths
  agree to within 1%, so the dog's depth in every frame comes from its smoothed core_cy.

## Dog height per frame (height2.py)
H = bbox pixel height × Z_origin / f, using the scene/ bboxes. I checked them visually at frames 0, 24, 36 and 45.
- Back only (tail below the back line), e.g. frames 0–2 and 27–32: 0.56–0.62 m. Median of all frames: 0.604 m.
- Tail raised above the back, at frames 3, 14, 23–25, 36 and 46: 0.64–0.70 m. The maximum is at frame 24 (tail tip at
  y ≈ 585, lowest paw at y ≈ 922, 337 px → 0.70 m).
- Second route at frame 24: tail-tip height = camera height − (v_top − 540)·Z/f = 0.788 − 45·4.5/2150 ≈ 0.69 m.
  This barely depends on the tail's own depth.

## Reading and answer
"Including its tail" implies the tail sets the top of the bounding box. That happens when the tail is raised: 0.65–0.70 m.
With the tail down, the height is about 0.60 m. Answer: **0.67 m**, weighted toward the tail-up value.

Confidence: moderate. The focal length is ±3%. The main uncertainty is which frame or pose the reference uses:
- tail-up maximum ≈ 0.70
- frame 0, back height ≈ 0.61
