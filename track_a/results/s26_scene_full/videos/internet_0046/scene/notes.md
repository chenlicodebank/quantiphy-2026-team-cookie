# internet_0046 — measurement record

Real footage, 2D (side view), 1920x1080, 30 fps, 51 frames (t = frame/30, 0 … 1.667 s).
**Scene:** the camera sits low at floor level and looks at a plain grey wall, with a light wooden floor in the lower half.
A ceramic **mug** (dark body that has been privacy-blurred, white handle on its right side) is pulled to the RIGHT by a tan **string**
tied to the handle. It slides across the floor from the left image edge to the right image edge. It speeds up the
whole time: body-centre steps are about 94 px/frame at frames 27→28 and about 132 px/frame at frames 38→39. No metric scale is assumed anywhere.

## Files
- `scene.json`: inventory (objects, visible frames, pixel sizes), events, camera, and a summary of the centre x per frame.
- `tracks/mug.csv`: one row per frame (0-50). Columns:
  - `ref_x, ref_y`: centre of the **visible mug body** (handle excluded). This is the reference point to use.
    In edge-cut frames (`cut_left`/`cut_right` = 1) this is only the centre of the visible part.
  - `centre_x_est_full_body`: for cut frames, the visible edge ± (median full body width 483 px)/2. It equals `ref_x` when the body is not cut.
  - `body_left_x, body_right_x, body_width_px`: horizontal body edges, taken as the 50 % crossing of the background-difference profile
    in the wall band (rows 330-470).
  - `top_y, bottom_y, height_px`: rim and base of the body.
  - `handle_right_x`: outer edge of the handle. It is `measured` only in frames 27-31. Elsewhere it is `body_right+offset`, using the
    rigid offset of 179.6 px (median of frames 27-31, which ranged 173-184).
  - `length_incl_handle_px` (body left edge to handle outer edge), `bbox_*` (body + handle), `cut_left`, `cut_right`, `occluded_or_cut`, `note`.
- `tracks/mug_auto.csv`: raw output of the automatic tracker. This is intermediate: its handle and knot columns are unreliable, so use `mug.csv`.
- `tracks/string_knot.csv`: automatic trace of the string's left end. It is **unreliable** (the trace breaks along the thin
  string). The values are plausible only in frames 27-38, where the knot sits about 0-30 px left of `handle_right_x`. Do not use it for motion.
- `scripts/`: `track_mug.py` (body edges), `handle.py` (handle edge), `camera_caps.py` and `camera_static.py` (camera check),
  `edge_strip.py` (entry and exit frames, checked by eye), `finalize.py` (builds mug.csv and scene.json), plus probe scripts.
  The JSON files hold intermediate results.

## Key pixel numbers (body fully in frame, frames 27-39)
- Body width (the length along the motion direction, without the handle): median **483 px**, range 465-499. The variation comes from motion blur
  and the blurred, low-contrast right edge. The handle sticks out **≈180 px** beyond the body's right side, so the full mug length
  including the handle is **≈ 660 px** (measured 651-683 in frames 27-31).
- Body height (rim to base): median **570 px**, range 568-582. It grows slightly late in the clip.
- The mug moves almost horizontally. `ref_y` drifts from 578 to 601 px and the height grows by about 2 %, so the mug comes slightly
  toward the camera. Its x motion dominates (about 1350 px across frames 27-39).
- Body-centre x in the full frames: 27: 251.3, 28: 345.6, 29: 440.2, 30: 540.3, 31: 643.0, 32: 751.0, 33: 862.6, 34: 977.7,
  35: 1097.2, 36: 1220.8, 37: 1347.6, 38: 1476.6, 39: 1608.2.
  The left edge, right edge and centre each give consistent steps. You can also difference the left edge (`body_left_x`, not cut in frames 27-42) or the right edge
  (frames 21-39) to extend the series to entry and exit.

## Events
- Frames 0-17: no mug. The taut string crosses the frame at y≈310-360 and shifts slightly.
- Frame 18: the knot enters at the left edge.
- Frame 19: the handle tip enters.
- Frame 21: the body enters (a sliver at x 0-30).
- Frames 27-39: the body is fully in frame.
- Frame 39: the handle starts leaving at the right edge.
- Frames 40-43: the body is cut at the right edge. Frame 43 shows only a sliver at x≈1862-1919.
- Frame 44: the mug is gone. Its floor shadow is still visible at the right edge until about frame 46.
- There is no bounce, no stop and no change of direction while the mug is visible. It is pulled and accelerating the whole time.

## Camera
Static. The black end caps of the baseboard tube move ≤3 px over the whole clip (left cap x 446.7-452.4, right cap x 1718.6-1726.0),
and in opposite directions. That points to slight shake or focus breathing, not a pan. It is negligible next to motion of ~100 px/frame, so no background correction was applied.

## Static objects (frame 50, empty scene)
- Light-grey baseboard tube/cable cover along the wall-floor junction: black caps at x≈452 and x≈1722 (cap to cap ≈1270 px), y≈497-552.
- A bluish-white strip to its left (x 0-430, y≈485-540) with a black cap at the left image edge.
- The wall (y < ~495) and the wooden floor (y > ~555, horizontal grain). The floor/wall line is close to horizontal; there is no other ground marking.

## Reliability / ambiguities
- Motion blur is strong: about 30-50 px smear per frame. Edges are taken at the 50 % contrast crossing, so the centre is the most reliable
  quantity (±3 px). Single edges are ±8 px. Widths are ±15 px.
- The body's right edge has a blurred, low-contrast band next to the handle. In a zoomed look at frame 35 the dark edge was at ≈1310 px, while the
  table says 1332. A ~20 px systematic uncertainty on the right edge is possible, which makes the 483 px width uncertain by about the same amount.
- The handle is white against a light wall, so it is hard to segment. It was measured directly only in frames 27-31 (checked by eye); in other frames it is extrapolated.
- The privacy blur on the mug body changes appearance across frames (for example, sharper and darker in frames 21-22). This does not affect the edges.
- The mug's shadow on the floor (to its lower-left) is excluded from all extents. The base is measured in the body's central columns.
- Frames 21 and 43 are manual readings (±10 px). Frames 18-20 have no body measurement.
