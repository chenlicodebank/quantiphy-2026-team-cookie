# internet_0022 — measurement record

Internet footage, 2D, 3840x2160, 16.666667 fps, 36 frames (0–35, t = frame/fps, 0–2.10 s).
Static overhead (top-down) camera looking at an office desk. A seated man in a dark suit reaches to the left,
picks up a **navy clipboard/folder carrying an A4 chart sheet** (world map plus a blue/purple bar table with red cells),
and brings it to the centre in front of him, above the keyboard. Everything else is static.
All values are in full-resolution pixels and seconds. No metric scale has been assumed.

## Files
- `scene.json`: inventory (moving and static objects with pixel sizes and positions), camera, events, folder
  net displacement, path length and per-frame centre steps.
- `tracks/folder.csv`: one row per frame (0–35). `cx,cy` is the primary reference point (visible centre of the board).
  `bx0..by1` is the bounding box, `long_axis_px/short_axis_px` are the board edge lengths, `c0x..c3y` are the board corners
  where SIFT tracking gives them, and the `mask_*` columns come from the change/colour mask (centroid, minAreaRect length, width and angle).
  The table also has `alt_back_sift_*` (frames 29–31), plus `occluded`, `motion_blur` and `reliability` flags.
  `source` says which method gave `cx,cy`:
  - frames 0–16: `sift_fwd_similarity`. SIFT matched to the frame-0 template (rotation, scale and translation). Corners are
    top, right, bottom, left. Reliable to about 5 px, but frames 15–16 are blurred (77 and 29 inliers).
  - frames 17–31: `mask_centroid`. Centroid of the pixels that changed against a composite background (frame 35 for x<1600,
    frame 0 for x≥1600), are bright (V>105) and are not skin, taking the largest blob with holes filled. The folder is heavily
    motion-blurred here, so the centre is good to about ±20–30 px. The mask's length and width are inflated by blur and by the hands
    (not usable as sizes). At both hand-off points it agrees with SIFT within about 10–15 px (frames 14–16 and 32).
  - frames 32–35: `sift_back_homography`. SIFT matched to the frame-35 template with a homography (67–116 inliers).
    Corners are TL, TR, BR, BL. Reliable to about 5 px.
- `tracks/man.csv`: the head box and centre come from NCC template matching (`head_cx, head_cy, head_ncc`; box 420x440 px; verified
  on frames 0/7/14/21/28/35). The `body_*` columns come from a rough suit/hair colour mask (bbox, centroid, area). It misses the
  lit right shoulder in some frames (around 21–28), so body extents are approximate only.
- `scripts/`: every script (`explore.py` camera check; `track_folder_sift.py`, `track_folder_back.py`, `track_all.py`,
  `seg*.py`, `track_head.py`, `finalize_folder.py`, `static_objects.py`, `write_scene.py`; `montage.py` and `check_overlay.py`
  for visual checks). Order to rebuild: track_folder_sift → track_folder_back → track_all → track_head → finalize_folder →
  static_objects → write_scene.

## Key numbers (pixels)
- Folder board at frame 0, lying flat: 559 x 417 (long x short edge). The A4 chart sheet on it is about 535 x 368.
  Centre (1087.5, 1494.0).
- Folder at frame 35 (held up and tilted, top tilted away from the camera): quad edges TL-TR/TR-BR/BR-BL/BL-TL = 391/426/457/437. The long axis
  (map→bars direction, now roughly vertical) is foreshortened to about 430. Centre (2069.5, 1197.2).
- SIFT similarity scale grows about 9% (frames 0→16) as the folder is lifted toward the camera.
- Net folder displacement from frame 0 to 35: dx = +982, dy = −297, 1026 px, direction −16.8° (right and slightly up in the image).
  Path length is 1110 px.
- Board extent projected on that motion direction: 692 px at frame 0 (close to the diagonal, because the board is rotated about 37°
  to the motion), 454 px at frame 35.
- Per-frame centre steps: <6 px for frames 0–12 (the hand adjusts the folder in place). The steps then grow: 8, 14, 20 … up to about 129 px
  (frame 20→21), stay at about 95–120 for frames 21–25, fall through 21–31 and are ≤8 px for frames 32–35. The step from 16→17
  (15→40) crosses a change of method.
- Static objects (frame 0 unless noted; minAreaRect length x width): keyboard 502x211, centre (1990,1273);
  mouse 198x103; Business Goals sheet 534x382, centre (1755,1755); saucer with teacup diameter about 250, centre (1291,1123)
  (it is partly under the sleeve at frame 0); CONTRACT clipboard 574x408 at −36°, centre (927,1403), measured at frame 35 where it is
  uncovered; dark tablet top right 410x253; pencil about 306 long (hand-read). Desk far edge at y≈780.
- Man: head centre moves (2010,550) → (2018,580) at frame 6 → (2000,458) at frames 25–27 → (2020,502) at frame 35.
  Horizontal motion <25 px, vertical range about 120 px. His position on the chair barely changes.

## Events
- Frame 0: hand already on the folder.
- Frame 13 (0.78 s): lift and transport start.
- Frame 20→21 (1.2–1.26 s): peak speed.
- Frames 15–28: heavy motion blur.
- Frame 28 (1.68 s): decelerating.
- Frames 32–35 (1.92–2.10 s): folder held essentially at rest in front of the man.

## Caveats
- Camera: static. Phase-correlation shift is below 0.1 px in every frame, so no background compensation is needed.
- The folder is never fully unoccluded until frame 34: the hands or sleeve always cover part of it. Its top corner at frame 0 is
  under the sleeve, so it was completed as a rectangle.
- The folder leaves the desk plane: it is lifted and tilted toward the man. The planar 2D assumption is only approximate for it,
  and its apparent size changes (about 9% growth while lifting; strong foreshortening at the end).
- Possible confusion: the CONTRACT clipboard (also navy with a white page and a silver clip) stays at the left and is NOT the
  moving object; the chart papers at the right are static.
- Shadows are negligible (diffuse lighting). The man's face is blurred in the source video.
