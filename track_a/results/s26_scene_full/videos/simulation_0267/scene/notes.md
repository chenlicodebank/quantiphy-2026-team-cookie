# simulation_0267 – measurement record (pixels, seconds)

Video: 2560x1440, 24 fps, 72 frames (t = frame/24). Source: simulation, 2D scene.
Content: one futuristic **flying car** (dark grey/black upper shell, white/silver underside machinery, two small
roof antennas at the rear, nose pointing LEFT, seen side-on) flies right-to-left across a static sunset sky above a
sea. Nothing else moves. The camera is static: phase correlation of the sky against the empty last frame gives shifts
under 0.03 px in every frame.

## Files
- `scene.json`: inventory, size summaries, events, camera and horizon.
- `tracks/flying_car_final.csv`: **the main track**, one row per frame 0-71 (visible=0 from frame 68 on).
  - `ref_x, ref_y`: car reference point, used as a proxy for the origin. `ref_method` says how it was obtained:
    - frames 10-52 (car fully in frame): `bbox_centre`, the midpoint of the nose tip (x0) and tail tip (x1) of the mask.
    - frames 0-9 (tail cut off at the right edge): x0 + 515.0, the nose-to-centre offset measured at frame 10.
    - frames 53-67 (nose cut off at the left edge): x1 − 496.0, the tail-to-centre offset measured at frame 52.
    - ref_y is the frame-24 bbox centre row carried along by the template match. It is constant at about 887 (±0.5).
  - x0,y0,x1,y1 / bbox_w,bbox_h: mask bounding box (full-res px). bbox_h includes the roof antennas.
  - mask_len_axis / mask_wid_axis / axis_angle_deg: PCA main-axis extents of the mask.
  - mask_centroid_*: area centroid of the mask. It is biased when the car is clipped, so don't use it as a position there.
  - template_cx/cy: whole-car template match (frame-24 template). This is a cross-check only, see the caveats below.
  - clipped_by_frame_edge: 1 when part of the car is outside the image. occluded is always 0, because nothing occludes the car.
- `tracks/flying_car.csv`: raw mask track that the final track was built from. Its frames 68-69 are cloud noise, not the car.
- `tracks/flying_car_template.csv`, `tracks/flying_car_endpatch.csv`, `tracks/flying_car_darkshell.csv`: auxiliary trackers used to check the main track.
- `scripts/`: every script. `track.py` (background-difference mask against empty frame 71), `template.py`,
  `endpatch.py`, `spoiler.py`, `finalize.py` (builds the final track and draws the check image), `write_json.py`,
  plus `check_bg.py` and the `crops*.py` viewers.

## Results
- **Motion**: pure horizontal translation to the left (−x). The car does not move vertically (y within ±0.5 px) and
  does not rotate. Apparent scale stays constant to within about 1-2 %.
- Frames 0-1: car at rest (ref_x 2091). From frame 2 the per-frame displacement grows steadily: −2, −2, −4, −5, … −58
  px at frame 53, −72 px at frame 67. The second difference is about −1.1 px/frame² throughout, which looks like
  constant acceleration from rest starting at about frame 1. No direction changes, bounces or contacts.
- Path length of ref_x over frames 0-67: 2515 px (frames 53-67 use the extrapolated centre, since part of the car is off-screen).
- **Size of the car** (frames 10-52, fully visible):
  - Nose-to-tail bbox length: median 1009 px (range 982-1031). At frame 24 it is 1018 px (x 1252-2269, y 731-1044).
  - Height including antennas: median 314 px (299-318). Body height without antennas is about 266 px (roof about y 778 to underside y 1044).
  - Mask main-axis length: median 1018 px; width across the axis about 260 px. The axis is tilted about 8° (nose lower).
  - The apparent length shrinks slowly from about 1031 px (frame 10) to about 982 px (frame 47), then rises again to 993 px (frame 52).
    This is a perspective change in the car's visible outline as it crosses the view, not a real size change.
- **Static**: sea horizon at row about 1204 px, nearly horizontal. The rest is the cloud sky and the sea surface (the sea has very faint shimmer). There are no other objects, ground markings or furniture.

## Reliability and ambiguities
- Mask edges are accurate to about ±2 px. I checked this on zoomed crops: the nose tip and tail fin tip match x0/x1.
  The frame-57 x1 overshot the fin by about 9 px, so it was replaced by the dark spoiler tip + 2 px (742).
- Full-frame ref_x is good to about ±2 px. In clipped frames the offsets assume a constant nose/tail-to-centre distance, which adds roughly ±5-10 px.
- Origin choice: the true origin is not visible. The midpoint of nose and tail tips should be close to the projection of the car's centre.
  The whole-car template (template_cx) and a tail-patch tracker move about 2-8 % faster than the tips. They lock onto the near-side
  body panels, which are closer to the camera, and on perspective changes of the outline. I treat the tip-based ref_x as primary. If a
  question's answer seems about 2 % off, this choice is the reason.
- For a pixel→metre scale from a given car length, use bbox_w (nose-to-tail along x, about 1009-1018 px). bbox_h includes the antennas.
- Mild motion blur at high speed (frames >45, up to about 70 px/frame). Edges stay sharp enough.
