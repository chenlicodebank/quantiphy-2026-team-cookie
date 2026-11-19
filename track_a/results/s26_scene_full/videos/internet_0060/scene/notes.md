# internet_0060 — measurement record

Video: 1920x1080, 110 frames, 30.013643 fps (t = frame/fps). Internet footage, 2D. All values in pixels / seconds.

## Scene
A hand at the left image edge holds a small square pink foil packet (white Japanese text) still for frames 0-51,
lets it go at frame ~52, the packet travels right (+x) with steadily growing per-frame steps (dx 21, 34, 47, 59, 74,
84, 96, 108, 118, 126, 139, 149, 162 px for frames 52->65), hits the black vertical strip at frame 65, rebounds
(x max at 66, x min ~69-70), lands again (~73-74), slides along the strip toward +y and rests from frame ~78
at about (1383, 969). The uniform acceleration along +x suggests the clip is rotated 90 deg: image +x is probably
physical "down" (a drop onto the floor), black strip + wood = floor side. Image y is then horizontal. Treat this as
an interpretation; a question's prior decides the scale.

## Files
- `scene.json` — inventory, static object extents, events, camera summary.
- `tracks/packet.csv` — per frame 0-109: `cx,cy` mask centroid; `bbox_x0..y1,bbox_w,bbox_h` (inclusive pixel bbox);
  `bbox_cx,bbox_cy` bbox centre; `mask_len,mask_wid,rect_angle` (cv2.minAreaRect of the mask); `area_px`;
  `cam_dx,cam_dy` background shift vs frame 0 (strip phase correlation); `cx_bg,cy_bg` = centroid minus camera
  shift (background-fixed coordinates); `occlusion`.
- `tracks/hand.csv` — coarse skin-mask bbox of the hand per frame.
- `tracks/camera.csv` — background shift vs frame 0 from three regions (strip+wood rows 0-420; high-passed wall
  x200-1300,y0-450; wood — wood only valid to frame 37).
- `scripts/` — `common.py` (decoder), `probe.py`, `colors.py`, `track.py` (first pass + camera shift -> `_raw.json`),
  `track2.py` (final packet track + overlay), `hand_static.py` (hand, strip edges, bbox centres), `camcheck.py`,
  `look.py` (crop viewer).

## Method and reliability
- Packet frames 0-51: magenta hue mask (h>=160, s>40, v>45) limited to x<300. The fingers cover the left part of
  the packet and the packet touches the left image edge (bbox_x0=0), so centroid/bbox here are biased and NOT a
  size reference (occlusion flag set). Position is static to a few px — fine for "start position".
- Frames 52-109: |frame - camera-shifted background| > 30 AND pink hue, inside a window around the previous position;
  background = frame 75 for frames 52-62, frame 40 for 63+. Overlays (checked visually at 21 frames) show the bbox
  enclosing the whole packet in every checked frame; the contour sometimes has notches (white text / black strip),
  so prefer `bbox_cx,bbox_cy` or centroid — they differ by a few px. Centre accuracy ~±3 px in flight, ±5 px during
  the tumbling 66-73 (blur, rotation), ±1-2 px at rest.
- Packet size: best = rest frames 79-99, ~99-100 px square (bbox 100x100, minAreaRect 99x98). In flight the bbox
  is ~110x100 because motion blur stretches it along x by ~10 px. Packet length along main motion direction (x) ≈
  100 px (blur-free).
- Camera: slow smooth drift, about -0.25 px/frame in x, ~-0.1 px/frame in y, total ≈ (-26..-28, -12..-14) px at
  frame 109. Negligible relative to flight motion (100+ px/frame) but matters for the rest phase (the apparent drift
  of the resting packet is camera drift). Strip and wall estimates agree within ~2-3 px; a slight rotation/zoom
  exists (strip edge moved -26 px at top, -30 px at bottom).
- Hand bbox (hand.csv) is coarse: frames 52-58 its x1 is inflated by the packet's pink/skin-coloured motion-blur
  smear; true hand stays within x<~160 until it leaves; re-enters lower left from frame ~97 (arm sweeping toward
  bottom centre). Hand shadows on the grey wall are not tracked.
- Static: black strip ~135-137 px wide, full height, slightly tilted (left edge x 1326 at y=0 to 1341 at y=1079,
  frame 0). Wood region from strip right edge to x=1919 (~450 px visible).
- Ambiguities: only one packet, no similar objects. Strip is dark so packet contrast over it is lower but the
  pink still segments well. No timestamps of a second throw.
