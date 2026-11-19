# internet_0017_segmented — measurement notes

Clip: 34 frames, 30.0003 fps (1.133 s), 1280x674. A segmented, top-down view of a desk on a pure-white background:
two forearms/hands, a white keyboard, a pen and a round tin. 2D scene. Only the right hand moves: it slides up-left
across the keyboard and comes back (typing / reaching gesture). Units are pixels and seconds; no metric scale was assumed.

## Files
- `scene.json`: inventory, static extents, camera info, events.
- `tracks/<object>.csv` (right_hand, left_hand, keyboard, pen, tin), one row per frame 0-33: frame, time (=frame/fps),
  cx, cy (mask centroid = visible centre), bbox x0,y0,x1,y1, bbox_w, bbox_h, len_main_axis / width_across (PCA extents
  of the mask), main_axis_deg, area_px. The hand files also have tip_x, tip_y (topmost fingertip pixel), hand_cx,
  hand_cy (centroid of the mask within 200 px of the tip, i.e. hand without forearm), truncated_by_frame_edge (always 1),
  occluded (0; nothing covers the hands).
- `scripts/`: measure.py (segmentation + tracks), keyboard.py (keyboard footprint), overlay.py (mask check images),
  explore.py (frame differencing), colors.py, show_tracks.py.

## Method
Non-white = min(RGB) < 235. Skin = non-white with R-B > 8 and R >= G (keyboard grey has R-B < 0), cleaned with
open/close; split into left/right hand by connected component. Pen = non-white x<400, tin = non-white top-right,
keyboard = remaining non-white in its region. Overlays at frames 0, 12, 18 checked: masks cover the full hands/arms,
pen, tin, keyboard.

## Reliability / ambiguities
- Camera static (static objects' centroids std < 1 px). No background texture exists (segmented), so nothing else to check.
- Frames 3, 9, 15, 21, 27, 33 are near-duplicates of the previous frame (25->30 fps pulldown), so per-frame
  displacement is ~0 there and larger on neighbouring frames; smooth or skip these when differencing.
- Right hand: the forearm is cut by the bottom edge, so the whole-mask centroid (cx,cy) and main-axis length depend on
  how much arm is in frame; hand_cx/hand_cy or tip_x/tip_y are better reference points for hand motion. Tip is the
  topmost pixel, ±2 px, and can switch between fingers. Hand reaches farthest at frames 14-19 (tip ~(924-930, 292)),
  returns by frame 29. Net hand-centroid excursion ~56 px left, ~84 px up.
- Keyboard: the raw keyboard.csv mask is partly hidden by the right hand, and a few non-skin pixels of the hand get
  included, so use the footprint in scene.json: 363 x 167 px (long x short), centre (997.8, 332.1). The lower-right
  corner is hidden under the hand; the rectangle is fitted to the three visible sides. ±4 px.
- Pen: 181 x 19 px, static, ±2 px. Tin: 133 px wide x 125 px tall (slightly oblique, side wall visible), static.
- Left hand: static apart from small finger movement (≤4 px).
- Segmentation edges have a thin white halo around the right fingers where they overlap the keyboard; fingers that are
  pressed down are slightly foreshortened. These affect mask extents by a few px.
