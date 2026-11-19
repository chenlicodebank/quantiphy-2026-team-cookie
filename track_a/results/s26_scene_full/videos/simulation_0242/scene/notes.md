# simulation_0242: measurement record (pixels and seconds only)

The video is a 3D Blender render, 1920x1080, 24 fps, 50 frames (t = frame/24, from 0 to 2.0417 s). The camera is
**static**. It looks down at a lawn in front of a brick building. Three animals walk or hop **left to right** for
the whole clip: a **brown horse** (farthest, near the wall), a **cream horse** (middle) and a **rabbit**
(nearest, low in the frame). No metric scale is recorded here.

## Files
- `scene.json`: inventory (moving and static objects, how to tell them apart), static pixel extents, camera and
  perspective cues, events, and a summary of apparent size over time.
- `tracks/brown_horse.csv`, `tracks/cream_horse.csv`, `tracks/rabbit.csv`: one row per frame (0..49), with these columns:
  - `mask_cx, mask_cy`: centroid of the whole segmentation mask (legs and head included).
  - `torso_cx, torso_cy`: centroid of the mask rows in the upper 55 % of the bbox, so the legs are left out. This is the
    best proxy for the body centre / pelvis-root height in the image, and it is less noisy than the bbox centre.
  - `bbox_cx, bbox_bottom_y`: bbox centre x and bottom y (hoof/foot line = ground contact).
  - `bbox_x0, y0, x1, y1, bbox_w, bbox_h`: axis-aligned image bbox (inclusive pixels). For a side-on animal moving in x,
    `bbox_w` is the nose-to-tail length plus leg spread and `bbox_h` is the hoof-to-ear height.
  - `axis_length, axis_width, axis_angle_deg`: extents along and across the mask's principal axis.
  - `mask_area` (px), `occluded` (always 0: no animal is hidden by another or by scenery; the horses never overlap).
- `camera_shift.json`: per-frame phase-correlation shift of four background patches relative to frame 0.
- `tracks_overview.jpg`: torso-centroid paths and the bboxes at frames 0/24/48, drawn on frame 24 (for checking).
- `background2_half.jpg`: preview of the reconstructed animal-free background.
- `scripts/`: `camera.py` (camera shift); `background.py` and `background2.py` (two-pass clean background; full-res
  output goes to ../frames/); `segment.py` (masks); `track.py` (writes the CSVs; run it after background2.py);
  `zoom_obj.py` and `zoom_head.py` (overlay checks); `static.py` (rough wall-edge fits, not used for final values);
  `summary.py` (dx / size statistics); `draw_tracks.py`; `probe_*.py` (colour probes).

## How it was measured
1. **Camera.** Phase correlation of the building, roof and two grass patches gives |shift| < 0.05 px in every frame,
   so the camera is static and no background compensation is needed.
2. **Background.** First a band-wise temporal median. Both horses barely translate (brown about 290 px, cream about
   530 px over 2 s), so their bodies contaminated the median. In a second pass the median is taken only over frames
   where the first-pass mask was absent. About 3.8 k pixels at the wall bottom behind the brown horse's neck were never
   uncovered; they are inpainted and only colour rules are used there.
3. **Masks.** A pixel is foreground when it differs from the background and is not grass-green. Two extra rules: a
   rule for the flat grey-brown head discs (local SD < 2.5 plus a greyish colour) and a rule for dark smooth legs,
   hooves and tails (smooth, changed, R ≥ G). Pixels are assigned to animals by colour seeds (brown/saturated,
   cream/low saturation, small object low in the frame) plus nearby components. Overlays were checked visually at
   frames 0, 5, 6, 12, 15, 20, 24, 30, 40, 42, 45, 48 and 49 (zoomed): the masks are on the right animal and cover
   the body, head, tail and most of the legs.
4. **Static extents** were read from 2x zoomed, gridded crops of frame 0 (±5 px).

## Key results (pixels)
- **brown_horse:** frames 0-48 move +x at a mean of 5.99 px/frame (torso_cx), 287.6 px in total. The image y is
  constant (torso_cy ≈ 388-392, hooves y ≈ 553-566). **Between frames 48 and 49 it jumps back to its frame-0
  position** (mask_cx 691.1 → 408.2; frame 0 is 411.6). This is a looped-animation reset, not motion: exclude the
  48→49 step from speeds and path lengths, and treat frame 49 as a repeat of about frame 0. Size: bbox_w 315-360
  (mean 330), bbox_h 240-273 (mean 257).
- **cream_horse:** moves +x at 10.88 px/frame (torso_cx), 533 px in total over frames 0-49, with constant image y
  (hooves y ≈ 671-702). Size: bbox_w 389-460 (mean 423), bbox_h 265-296 (mean 284).
- **rabbit:** moves +x at 11.26 px/frame on average, 552 px in total, with a periodic hop of about 10.3 frames
  (0.43 s). Per-frame steps range from about 7 to 18 px; the biggest steps arrive at frames 6, 16, 26, 37 and 47.
  The centroid y stays fixed at 766-769 with no visible airborne phase. Size: bbox_w 78-105 (mean 87), bbox_h 59-77
  (mean 68).
- **Building (static):** the brick wall spans x 440-1495 at its top (y ≈ 95) and x 462-1462 at its base
  (y ≈ 375; fit y = 0.0033x + 373), so it is about 280 px tall. The timber upper storey spans x 318-1600, y 0-95
  (cropped by the frame top). There are three arched windows, each about 115-127 px wide by 155 px tall: left
  [473, 95, 600, 250], middle [903, 95, 1018, 250], right [1325, 95, 1450, 250]. The rest of the frame is lawn, with
  the building's shadow on the left and a sunlit pale patch at the upper right.
- **Events:** all animals are already moving at frame 0 and still moving at frame 49, and nothing enters or leaves
  the frame. The only discontinuity is the brown horse's reset at frame 49. There are no impacts or contacts between
  objects.

## Perspective (3D)
- The camera is elevated and pitched down. The facade is parallel to the image x axis. The building's vertical
  edges converge downward, putting the vertical vanishing point roughly at (820, 5500) (uncertain by ±1500 px in y),
  so the horizon is above the image.
- Depth order follows the image y of the ground contact: rabbit (y ≈ 800) is nearest, then the cream horse
  (≈ 690), then the brown horse (≈ 560), then the wall (≈ 375). The pixel scale therefore differs per animal: never
  use one animal's px/m for another. With depth_info, use the pinhole relation size_px = f·size/depth, with f
  estimated from a known size and its given depth.
- All three animals move almost exactly along image x at constant image y, so their depth changes little during
  the clip. Apparent size is nearly constant: first-10 vs last-10 frame mean bbox_h is 262/248 for the brown horse
  (a gait effect), 282/288 for the cream horse and 67/69 for the rabbit.

## Reliability and ambiguities
- **Centroids:** torso and mask centroids are good to about ±2 px per frame. Gait and leg-swing jitter is 2-4 px per
  frame in x, so smooth over several frames for speeds. The bbox centre is noisier (±5-10 px) because legs, ear
  tips and tail swing.
- **The rig origin (root/pelvis) is not visible.** The torso centroid is the best body-centre proxy. The world
  origin of an animal rig may sit at ground level, so horizontal pixel displacement is the same either way.
- **Head discs:** both horses' heads render as flat grey discs, an untextured-material artifact. They are included
  in the masks. The brown horse's disc sits over brick of similar colour, so its right bbox edge is uncertain by
  about ±10 px; frames 0 and 49 may include a few grass specks.
- **Cream horse:** dark lower legs and tail in shade are sometimes partly missed, and belly-shadow pixels sometimes
  leak in. bbox_bottom_y is uncertain by about ±10 px.
- **Rabbit:** the tips of the trailing hind feet are sometimes missed (bbox_w about 5 px short).
- **Shadows:** cast shadows on the grass are excluded (greenish), apart from small leaks under the horses' bellies.
- **Mask extents** are image-plane only. They are not world-space AABB dimensions; convert with depth.
