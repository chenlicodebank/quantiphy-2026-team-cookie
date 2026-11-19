# simulation_0101_segmented — measurement record

2D segmentation clip, 1920x1080, 24 fps, 73 frames (t = frame/24, 0 … 3.0 s). The background is pure white
(RGB 255, so the masks are exact up to compression edges). There are two objects and no static scenery.

## Files
- `scene.json`: inventory, sizes, reference-point definitions, events, camera.
- `tracks/boat.csv`: one row per frame (0–72). `ref_x` = bow_x + 429 (horizontal bbox centre from the full length
  859 px), `bow_x/bow_y` = leftmost mask pixel, `stern_x_or_edge` = right bbox edge (it is the image edge, 1919, in frames 0–25),
  `keel_bottom_y`, bbox, `length_px` (blank while cut), visible height, mask centroid (biased while cut), area, cut flags.
- `tracks/shark.csv`: one row per frame. `ref_x/ref_y` = bbox centre, snout (leftmost) and tail tip (rightmost) x, bbox,
  length/height, mask centroid, area. Never occluded or cut.
- `scripts/track.py`: segmentation (non-white threshold 12, components ≥40 px, split at y=740: boat above, shark
  below) → `_raw.json` plus overlays `../frames/ov_*.png`. `scripts/write_record.py`: CSVs plus diagnostics. `thr_check.py`: threshold test.

## Objects
- **boat**: a red fishing boat ("AH805" in yellow on the hull) with a white wheelhouse, a mast and grey stern rails. Its bow points left. Full length
  859 px (856–862) from bow tip to stern/antenna. Hull alone (rows 450–560) is 831 px. Keel bottom y≈643, bow tip y≈370, cabin roof y≈237.
  The mast runs off the top edge in every frame, so the **true height and vertical centre cannot be measured**: the visible
  height is about 646 px and the hull from bow top to keel is about 290 px. It moves left at a steady ~17.9 px/frame (linear-fit residual 1 px). The bow x steps alternate
  16/18/20 px because of pixel quantisation. Frames 0–25: the stern is off the right edge, so ref_x comes from the bow (reliable, ±1–2 px).
- **shark**: a grey-blue shark with a white belly, lower in the frame (y 852–958), swimming left. Its length is 279 px (277–283, varies with tail
  flap) and its height including fins is 105 px. It **speeds up** from ~7.5 px/frame (frames 2–5) to ~18 px/frame (frames 68–72), quite
  smoothly (a quadratic fit of the centroid has 0.5 px rms). Its y is constant. The bbox centre jitters by ±1 px because of the tail flap. The mask centroid is
  smoother, but it sits ~25 px left of the bbox centre (the head is more massive).

## Events
- Frames 0 and 1 are identical for both objects. Motion of both starts at frame 1 (the first displacement is between frames 1 and 2).
- Frame 26 (1.083 s): the boat is fully inside the frame horizontally.
- About frame 32 (1.33 s): boat and shark reference x values coincide. After that the boat is further left.
- There is no contact, bounce or direction change. Both are still moving left at the end of the clip.

## Camera and reliability
The camera is presumed static. There is no background to check against, but the objects keep a constant y and size. It is a 2D scene with a single
px scale for both objects. Pixel extents are good to ±2 px. There are thin rigging lines and a stern antenna (faint, partly
dropped by the threshold). The maximum boat length could vary by a few px depending on whether the antenna counts. Ambiguity: the boat's true origin
height is unknown (cut mast). For horizontal motion use ref_x or bow_x (same displacement).
