# internet_0008_segmented: measurement record (pixels, seconds)

Video: 960x540, 24 fps, 240 frames (t = frame/24). The source is "segmentation": a SAM2 cut-out on a pure white background. Treated as 2D.
There is no metric scale here. Each question's prior sets the scale. Convention: one scale = prior world value / prior pixel value.

## Files
- `scene.json`: inventory, summary extents, events and camera notes.
- `tracks/sailboat.csv`: frames 0-239, one row per frame. Columns:
  - `cx,cy`: bbox centre (the visible centre).
  - `centroid_x/y`: mask centroid.
  - `bbox_x0..y1`, `length_px` (horizontal extent), `height_px` (mast top to hull bottom), `area_px`.
  - `hull_x0/hull_x1/hull_len_px`: hull ends taken from the bottom 13 mask rows, so the hull length without the sails.
  - `mast_top_x`: x of the main mast top.
  - `cut_by_frame_edge`.
- `tracks/bottom_object.csv`: frames 179-239, same columns minus the hull columns.
- `scripts/measure.py` (segmentation and tracks, plus overlays in `frames/ov_*.png`), `scripts/summarize.py`, `scripts/build_scene.py`.

## How it was measured
- The mask is every pixel with min(RGB) < 200. The watermark box (x≥705, y≥508) is excluded.
- Connected components: the largest is the sailboat. Any component away from it is `bottom_object`.
- I checked the overlays at frames 0, 120, 200 and 239. The masks cover each object fully: sails, masts and hull for the sailboat, and the whole blob for the bottom object.

## Objects
- **sailboat**: a dark maroon two-masted (ketch) sailboat. The tall main sail is on the right and the smaller mizzen on the left.
  - Visible in all frames and never cut by the frame edge. It moves right (+x) and stays horizontal (cy ≈ 454 ± 1 px).
  - cx goes from 289.5 (frame 0) to 627.5 (frame 239). A linear fit gives about 1.417 px/frame, rms residual about 1.2 px, so the motion is very steady. Speeds are left for each question to fit.
  - Overall length (bbox) is about 98-100 px, median 100, range 95-105 because of mask jitter. Hull length is about 96-98 px, median 98.
  - Height from waterline to mast top is about 122 px (117-126).
  - Apparent size does not change, so there is no depth change.
  - For a "boat length" prior, use `length_px` or `hull_len_px` (median about 98-100 px). Their difference (~2 px) is within the jitter.
- **bottom_object**: a small dark brown/black blob near the bottom edge (y ≈ 510-536).
  - It is probably a small boat, dinghy or flotsam in the foreground. What it is cannot be identified.
  - It enters at the left edge at frame 179 (t = 7.458 s), is fully inside from frame 184 (t = 7.667 s), and is still visible at frame 239.
  - Its full size is about 41 px long and 19 px high.
  - It moves right much faster than the sailboat, about 9 px/frame on average. It is not constant: about 8.3 px/frame over frames 185-209 and about 9.6 px/frame over 209-239, so it seems to be speeding up.
  - It drifts down about 6 px over the clip. Its mask is small and blurry, so its position has about ±2 px jitter.
- **watermark**: the grey "Modified with Segment Anything 2 Demo" box at the bottom right. It is not a scene object.
- There is no water, horizon or ground: the background was removed.

## Events
- The sailboat moves steadily for the whole clip. No start, stop or turn is seen.
- bottom_object enters at frame 179 and is fully in from frame 184.
- The two objects never touch or overlap.

## Camera and reliability
- The background is pure white, so camera pan or shake **cannot be measured**.
- The sailboat's constant vertical position and constant x speed fit a static camera, or a smooth pan. If the original video panned, all speeds here are relative to the frame.
- Sailboat positions are good to about ±1-2 px.
- The bottom object is less reliable: its mask is small and blurry, and its first 5 frames are cut by the left edge.
