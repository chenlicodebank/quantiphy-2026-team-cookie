# internet_0059 – measurement record (pixels, seconds; t = frame/30, 123 frames, 1920x1080, 2D)

## Scene
A plain greyish wall with three dark-framed posters (left tall, middle wide, right small) and a white outlet near the
bottom centre. A dark red-brown basketball is thrown in from the left edge (thrower never visible). It flies in an arc
past the top of the frame, falls, and leaves through the bottom edge. It bounces on the floor out of view and comes back
up at the bottom right, then leaves through the right edge. The ball is the only moving object. A faint grey shadow of
the ball shows on the wall.

## Files
- `scene.json`: inventory (ball, 3 posters, outlet, wall), pixel extents, events and camera summary.
- `tracks/ball.csv`: one row per frame (0-122). `visible`=0 when the ball is not in frame.
  - `cx,cy`: bbox centre in image coordinates (the reference point, the visible centre).
  - `mask_cx,mask_cy`: mask centroid.
  - `bbox_*`: bounding box.
  - `area_px`, `length_major`/`width_minor`: min-area rectangle of the mask.
  - `encl_circle_diam`.
  - `cam_dx,cam_dy`: camera shift.
  - `cx_bg,cy_bg`: centre in frame-0 background coordinates, i.e. cx - cam_dx. **Use these for motion.**
  - `truncated_by_frame_edge`: ball cut by the image border, so its centre and size are biased.
  - `over_poster_colour_mask_only`: frames 91-94, where only the red-colour mask was usable. Its extents are about 5 px small, but the centre is fine.
- `tracks/camera_shift.csv`: per-frame image shift of the wall/poster region against frame 0 (phase correlation).
- `scripts/`:
  - `track.py`: ball and camera tracking.
  - `static.py`: poster boxes in several frames.
  - `finalize.py`: writes scene.json.
  - `probe.py`: grid frames.

## Method and reliability
- **Ball mask:** red-dominant pixels (R-G>14, R-B>12), refined with a darkness mask (gray<72) around the blob to
  capture the dark rim. I checked the overlays (frames 68, 80, 88, 96, 108) and the outline sits on the ball edge.
  The centre is good to about ±1-2 px in clean frames.
- **Ball diameter:** best 121-122 px, from frames 88-90 where the ball is nearly round (122x122). The minor-axis median over
  clean frames is 122 px; the overall range is 119-127 px. Horizontal motion blur stretches `bbox_w`/`length_major` to 130-139 px:
  - in frames 66-75 (about 50 px/frame horizontally);
  - also in frames 105-109 (139 px wide, even though horizontal motion there is only about 19 px/frame). The cause is unclear (blur, spin, or the rim mask); the height there is still about 120 px.

  For "ball size" use about 121 px. If a question's convention is length along the motion direction, note that the blurred
  extent is larger.
- **Truncation:**
  - Frames 63-65: entering at the left edge.
  - Frames 77-80: top cut off near the apex, so cy there is slightly biased downwards (by a few px).
  - Frames 98 and 103-104: bottom edge.
  - Frames 109-115: right edge.

  For the cut frames, use the uncut edge plus a radius of about 61 px if a precise centre is needed.
- **Camera:** handheld with slow drift, no zoom (poster sizes constant within about 1%). The drift is about 22 px in x and 37 px in y over
  the clip. During the flight dx goes from +2 to -20 px and dy from +7 to +26 (frame 90) and back to +9. Phase-correlation
  shifts agree with poster box positions within about 3 px (a slight rotation or roll is possible).
- **Posters (frame 0 boxes, outer dark frame):**
  - left: 433-702 x 260-653 (270 w x 394 h);
  - middle: 745-1127 x 399-652 (383 x 254);
  - right: 1163-1415 x 478-650 (253 x 173).

  ±2 px.
- **Outlet:** approximate (about 878-912 x 1018-1075 at frame 81).

## Events (frame / time s)
| Event | Frame | Time (s) |
|---|---|---|
| Ball enters at the left edge | 63 | 2.100 |
| Ball fully in view | 66 | 2.200 |
| Apex (min cy; top clipped) | about 79 | 2.633 |
| Last visible before leaving at the bottom | 98 | 3.267 |
| Not visible (floor bounce out of view, about 3.35 s) | 99-102 | |
| Re-enters from the bottom, moving up-right | 103 | 3.433 |
| Last visible at the right edge | 115 | 3.833 |

Horizontal image motion is about +44 to +50 px/frame before the bounce and about +19 px/frame after it. No release or
impact is visible in frame.

## Ambiguities
- The thrower, the floor and the bounce are out of view.
- The ball's faint wall shadow is not part of the mask.
- Perspective: 2D treatment (the wall is roughly fronto-parallel). The ball may not be in the wall plane, so its
  scale relative to the posters is unknown.
