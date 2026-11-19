# internet_0069 – measurement record (pixels, seconds)

**Scene.** The camera sits at about table height and looks at a plain gray wall with a white rail and black clamps, over a
wooden table top. A coffee mug is pulled from left to right by a brown string tied to its handle. The mug has a
white rim and handle, a dark blurred print, and its handle on the right (leading) side. It accelerates the whole time
it is in view. There is only one moving object. 114 frames at 30.013158 fps; t = frame/fps.

## Files
- `scene.json`: inventory, pixel sizes, events, camera summary.
- `tracks/mug.csv`: one row per frame in which the mug body is detected (frames 54-84). Columns:
  - `body_x_left`, `body_x_right`: trailing and leading edges of the cylindrical body. These are 0 or 1919 when cut by the image edge.
  - `body_width`
  - `body_cx`: body centre. Only filled when the body is fully in view (frames 62-79).
  - `handle_x_right_est`: body_x_right + 170. This is the estimated outer edge of the handle and knot.
  - `mug_cx_incl_handle`: centre including the handle (frames 62-77).
  - `rim_top_y`, `base_bottom_y`, `cy`, `height`
  - `bbox_*`: includes the handle when it is in view.
  - `left_cut`, `right_cut`: flags for the image edge cutting the mug.
  - `cam_dx`, `cam_dy`: background shift.
- `tracks/camera.csv`: per-frame background offset compared with frame 0. It is the mean of the rail clamps matched with score > 0.95. `camera_check.csv` gives each clamp separately.
- `raw_body_cols.csv`: raw detector output.
- `scripts/`:
  - `track_mug.py` and `build_track.py`: tracking.
  - `vertical_handle.py` and `probe_handle.py`: vertical extents and handle.
  - `overlay.py`: drawing for visual checks.
  - `diffmask.py`: first mask check.

## Method
- **Body edges:** I compared each frame with the empty background (frame 100). A pixel counts as different when the
  summed absolute BGR difference is > 40, after a 5x5 blur. In the band y = 720-760, where the mug is in front of the
  wooden table, a column counts as mug if at least 60% of its pixels differ. The widest run of such columns is the
  body. I checked the overlays at frames 56, 62, 66, 70, 74, 77, 79, 82 and 84: the boxes fit the body edges to within a few px.
- **Height:**
  - The rim top is about y 505: the first row where the difference profile is > 25.
  - The base bottom is about y 1075: the strongest dark-to-light step.
  - The height is about 570 px and stays within about 1% over frames 62-79. Values in frames 54-56 and 84 are unreliable (sliver of the mug).
- **Handle:** The handle is semi-transparent from motion blur and close to the wall's colour, so it could not be
  segmented reliably. Its outer edge, which is also where the string knot sits, lies 155-178 px right of the body's
  right edge. I measured this from the difference-profile bump at frames 62, 66, 70 and 74, and by eye at frame 70.
  I used a constant 170 ± 10 px.
- **Camera:** I template-matched the two black rail clamps against frame 0. The background drifts by only a few px
  (|dx| ≤ 7 px, dy from +3 to −16 px over the clip). The two clamps differ by up to about 5 px around frames 67-80,
  which looks like a slight zoom or focus breathing. The mug moves 56-95 px/frame, so the camera can be treated as
  static. If you want to correct for it, subtract `cam_dx`. In frames 74-80 only one clamp was usable, so `cam_dx`
  jumps there; `camera_check.csv` has each clamp separately.

## Key numbers (px)
- **Body width along the motion direction:** about 420-425 near the image centre (419-421 at frames 69-72). It grows
  towards the edges: 452 at frame 62 and 459 at frame 79. This comes from the cylinder's perspective and/or motion
  blur. An annotator's "mug length" is probably either the body (~425) or body plus handle (~595).
- **Mug height:** about 570 (rim y ≈ 505 to base y ≈ 1075).
- **Motion:** purely horizontal. y is constant to within about 2 px. The body's left edge moves about 70 px/frame at
  frames 62-63, rising to about 90 px/frame at frames 77-80, so it accelerates throughout.

## Events
| Event | Frame | Time |
|---|---|---|
| Knot enters at the left edge | 51 | 1.699 s |
| Handle enters | 52 | |
| Body enters | 54 | 1.799 s |
| Body fully in view | 62-79 | 2.066-2.632 s |
| Body leading edge reaches the right edge | 80 | 2.666 s |
| Last sliver of the mug | 84 | 2.799 s |
| Mug gone | 85 | |

- The start and end of the motion are not in view.
- During frames 0-50 the string shifts and tautens slightly.
- After the mug leaves, its shadow remains visible at the bottom right (frames 85-113).

## Reliability and ambiguities
- **Body edges:** ±3 px.
  - The trailing (left) edge is the cleanest.
  - The leading edge is next to the white handle.
  - Motion blur (smear of about 10-20 px) softens both edges equally, so the centre is unaffected.
- **Shadow:** The soft shadow lies lower-left of the mug at y > 850. I excluded it by choosing the measurement band.
- **Handle edge:** ±10 px (estimate).
- **Rim:** The top is the far edge of the rim ellipse.
- **Mug print:** The mug's print is blurred in the source video (it looks like deliberate blurring), so there are no internal texture features.
- **Partial frames:** In frames 54-61 the left edge is cut (left_cut = 1), so only body_x_right is a true edge. In frames
  80-84 the right edge is cut, so only body_x_left is a true edge. Use edge-point tracks (body_x_left) to extend the
  time span across these frames.
