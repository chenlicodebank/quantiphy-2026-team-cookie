# internet_0002_segmented — measurement record (pixels, seconds)

Video: 1280x720, 24 fps, 44 frames (t = frame/24, frame 0 at t = 0). Source "segmentation": SAM2-segmented
internet footage, background blacked out; only vehicles, lane dashes, the top guardrail and a watermark remain.
Scene: top-down (nadir) aerial view of a multi-lane road; all vehicles drive left -> right (+x). Road axis ≈ image x
axis (dash rows tilt down to the right by only 0.004-0.008 px/px). 2D: one planar pixel scale applies.

## Files
- `scene.json` — inventory, per-object summary (visible frames, median pixel length/width), static objects (guardrail,
  every lane dash with position/length), camera, duplicate frames, events.
- `tracks/<object>.csv` — one row per visible frame: `cx,cy` = mask centroid (the "visible centre");
  `bbox_cx,bbox_cy`, `x_left,x_right,y_top,y_bottom` = robust bounding box; `length_px` = x extent (bumper to bumper,
  along the motion direction), `width_px` = y extent (across); `area_px`; `occluded` = 1 when cut by the image edge
  (`cut_left`/`cut_right`); `duplicate_of_prev` = 1 when the frame repeats the previous one.
- `camera_markings.json` — the 19 lane dashes at frame 0 and their per-frame shift (camera check).
- `scripts/` — explore.py, camera_markings.py, track.py (seed tracks -> _raw_tracks.json), track2.py (final tracks,
  CSVs, overlays), summarize.py (scene.json), dump.py.

## Objects (all moving, left -> right)
| name | what | visible | full-view length_px (median, range) | width_px |
|---|---|---|---|---|
| red_pickup_mid_lane | red/orange pickup/SUV, grey-blue trailing section; lane between dash rows y≈330 and y≈437; main subject | f0–f42 (right-edge cut from f37) | 184 (179–190) | 70 |
| white_car_top_lane | white/silver sedan, top lane under guardrail | f9–f43 (left-edge cut f9–f12) | 158 (156–162) | 70 |
| dark_car_top_lane | dark grey car, top lane, ahead of the white car | f0–f15 (right-edge cut f12–f15) | 154 (151–157) | 66 |
| dark_car2_top_lane | second dark grey car, top lane, behind white car | f33–f43 (left-edge cut f33–f37) | 166.5 (163–175), only 6 frames | 57 |
| gray_car_low_lane | dark grey car/van, lane below the red pickup (y≈437–539) | f24–f43 (left-edge cut f24–f28) | 176 (170–179) | 62 |

Pixel-motion examples (not models): red pickup centroid cx 150.7 (f0) -> 1171.4 (f35); ≈35 px per non-duplicate
frame. White car ≈42 px/frame, gray low-lane car ≈39-41 px/frame, dark top car ≈42-44 px/frame.
Red pickup's centroid also drifts down: cy 382.4 (f0) -> 426.6 (f35) (≈+44 px), more than the dash rows tilt — it is
slowly drifting across its lane. For "pixel length along the motion" use `length_px` (x extent); for position use
`cx` (or `bbox_cx`; both agree within ~1-2 px when the car is fully in view). Do not use cx when occluded=1.

## Static objects
- Guardrail: grey band across the full width, y 0–24.
- Lane dashes: 6 rows at y ≈ 118, 221, 330, 437, 539, 648 (lane width ≈ 105 px row to row). Dashes 98–107 px long,
  9–12 px thick, centre spacing ≈ 380–388 px along a row (positions in scene.json). Real dash length / gap are a
  possible scale reference if a question gives them.
- Watermark "Modified with Segment Anything 2 Demo", bottom right (y > 695), ignore.

## Camera
Static. All 19 dashes tracked every frame: median shift vs f0 stays within |dx| < 0.45 px, |dy| < 0.37 px (tiny
drift; per-frame values in camera_markings.json). No background compensation needed.

## Duplicate frames (important for per-frame velocities)
Frames 3, 8, 14, 19, 25, 30, 36, 41 repeat the previous frame (mean grey difference < 0.6 vs ~2–3.7 normally):
the footage was converted from ~20 fps to 24 fps. Vehicles show 0 displacement into these frames and the normal
step out of them. Forward differences across them are 0 / normal; averaging over several frames (or skipping the
duplicate) gives the true rate. Annotators may have used raw frame-to-frame values — keep both in mind.

## Events
dark_car_top_lane reaches right edge f12, last visible f15; white car enters left edge f9, fully in view f13;
gray_car_low_lane enters f24, fully in view f29; dark_car2 enters f33, fully in view f38; red pickup front reaches
the right edge f37, last sliver f42. No stops, contacts, bounces or direction reversals; all move steadily.

## Reliability / ambiguities
- Masks: background subtraction against the per-pixel median (static camera), morphological cleanup and a vertical
  opening to cut lane-dash slivers; extents use columns with >= 15 mask pixels. Overlays checked at f0, 12, 20, 30,
  36, 43 (boxes hug the cars). Length ±3 px, centroid ±1–2 px; SAM mask edges are soft (motion blur ~2 px).
- Top-lane cars touch the guardrail at y≈24: their width (and dark_car2's length, 163–175 px) is less reliable; the
  top edge may be slightly hidden.
- Two dark grey cars exist in the top lane (different times: f0–15 ahead, f33–43 behind the white car) plus a dark
  grey car in the low lane — distinguish by lane and time.
- Pixel scale differs slightly between objects only by measurement noise; nadir view, no notable perspective.
