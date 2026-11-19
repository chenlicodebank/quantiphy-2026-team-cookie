# captured_0018x — measurement record (lab video, 3D, 24 fps, 49 frames, 1280x720)

## Scene
A lab recording processed with SAM2: the background is replaced by plain white, and a watermark sits at the bottom right.
Two women stand still with their arms out and each drops two objects:
- **person_left** (farther from camera, white tank top, dark cargo trousers). Holds a **white_box** (white rectangular carton with a printed label) in her left hand (image-left) and a **soccer_ball** (black/white) in her right hand.
- **person_right** (nearer, long dark hair, black shirt and trousers). Holds a **tennis_ball** (small, yellow-green) in her outstretched left hand (image-left) and a **yellow_plush** (yellow plush with dark-green leaves on top, corn/banana-like) in her right hand near her body.
- There are no other objects. The floor and background are not visible.

## Files
- `scene.json`: inventory, static pixel sizes, events (frame and time), camera and perspective cues.
- `tracks/<obj>.csv` for soccer_ball, white_box, tennis_ball, yellow_plush. One row per frame (0-48).
  Columns: frame, time, visible, method, cx/cy (mask centroid), bbox_cx/bbox_cy (bbox centre = recommended
  reference "visible centre"), bbox_x0..y1, bbox_w/h, mask_len_major/mask_wid_minor (PCA-axis extents of the mask),
  major_axis_deg (image angle of the long axis, 90 = vertical), mask_area, occluded.
- `tracks/person_left.csv`, `tracks/person_right.csv`: per-frame bbox, width and height of each person's silhouette.
- `scripts/`: `track2.py` (the final tracker, which writes the CSVs), `overlay.py` / `montage.py` (visual checks),
  `summarize.py` (event and size numbers), `components.py` and `track.py` (exploration and first version).

## Method and reliability
- `method` column:
  - `template(ncc=..)`: object still in the hand. Located by normalised cross-correlation against a frame-0 template, with sub-pixel precision. The box is the fixed template box, not a mask, so there are no mask extents. Position is good to about 0.5 px. White box and plush are flagged occluded=1 because fingers cover them.
  - `colour`: object touching a hand, arm or another object (release frames 27-32). Pixels are selected by colour inside a window. The mask may include a few hand pixels, especially for the box at frames 29-31, where the bbox is about 5 px too wide. Centres are good to about 2-3 px.
  - `comp`: the object is an isolated silhouette on the white background, so the mask is complete. This holds for all frames from 33 onward.
- All tracks were checked visually with overlays (frames 0-5 and 26-48) and hit the correct objects.
- **Motion blur** is strong during the fall (up to about 50 px/frame). The vertical bbox height and mask length are inflated by roughly the per-frame displacement. Use horizontal widths or low-speed frames for sizes; scene.json gives the recommended sizes.
- Pale ball and box pixels: in some frames the white panels of the soccer ball blend into the white background (for example frames 47-48: width 44, height 37). The diameter is best taken as about 45 px.
- **Timing anomaly**: from frame 35 to 36 every falling object moves about twice the expected distance. This is most likely a dropped capture frame. Speeds across 35→36 are unreliable, so fit around it.
- The bbox centre jitters by ±2-5 px frame to frame during the fall because of blur and segmentation edges. Smooth before differencing.

## Pixel sizes (unblurred)
- Soccer ball: diameter about 45 px (range 44-47), at about the left person's depth (it lands at y=577, the same row as her feet).
- Tennis ball: diameter about 20-21 px.
- White box: about 26 x 54 px held upright at frame 0 (top partly behind fingers). On the floor at frames 40-48: long axis about 56-63 px, short axis about 26-30 px.
- Yellow plush: length including leaves about 55-60 px, width about 27-31 px.
- Left person: 404 px from head to feet.
- Right person: about 615 px. Her feet reach the bottom edge of the image, so the height may be slightly cut.

## Events (frame / time in s)
| Object | Release | Floor impact | After impact |
|---|---|---|---|
| Tennis ball | 26 / 1.083 | 36 / 1.50 (lowest bottom y=616) | Rebound apex at 45 / 1.875 (cy 421.5), then falls again |
| Yellow plush | 28 / 1.167 | 36 / 1.50 (bottom y=697) | Rebounds and tumbles up to cy ≈595 (frames 41-42), then hovers between cy 596 and 612 to the end with no clear second contact (ambiguous, possibly moving in depth) |
| Soccer ball | 29 / 1.208 | 39 / 1.625 (bottom y=577) | Rising until the end; apex at or just after frame 48 |
| White box | 29 / 1.208 | 39 / 1.625 (bottom y=602) | Small hop, tips over toward image-left, slides or rolls left about 64 px, lies horizontal at frames 47-48 |

- Before release, the right person slowly raises her arms: the tennis ball moves from cy 256 to 249 and the plush from 248 to 242 over frames 0-25. The left person's arms are almost still (less than 3 px of movement).
- "Release" means the first frame with downward motion. The last held frame is the one before it.

## Camera and perspective
- The camera is static: person bboxes stay constant to within 1 px.
- Intrinsics (benchmark convention): f ≈ 763 px, principal point ≈ (640, 360). These give the back-projection X = (u-640)·Z/763 and Y = (v-360)·Z/763, with Z taken from depth_info.
- Depth order from floor-contact rows, farthest to nearest: left person and soccer ball (y 577) → box (y ≈602-609) → tennis ball (y 616) → plush (y 697) → right person (y 719).
- Each object moves mostly vertically in the image during the fall, and its apparent size stays roughly constant (ball width 44-47 px throughout). This suggests little depth change, except for the plush after its bounce.
