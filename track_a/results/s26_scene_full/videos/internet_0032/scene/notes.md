# internet_0032 – measurement record

Internet video, 2D, 1920x1080, 220 frames, 29.851282 fps (t = frame/fps). Static camera: a calm lake at dusk.
The only moving object is a small rowing boat with two seated people (dark silhouettes). It moves right to left
across mid-frame (bow on the left) and slowly comes closer to the camera.

## Files
- `scene.json`: inventory, static object extents, events, camera, summary numbers.
- `tracks/boat.csv`: one row per frame (0-219), never occluded. Columns:
  - `bow_left_x`, `stern_right_x`: hull tips. `hull_top_y` is the highest hull row that is >60 px wide (gunwale/bow top). `hull_bottom_y` is the waterline (539).
  - `hull_length_px`: bow tip to stern tip, measured along x. The boat is side-on, so this is its main axis. `hull_height_px` is gunwale to waterline.
  - `cx_hull`, `cy_hull`: centre of the hull box. **Use this as the reference point.**
  - `bbox_*`: box around the whole silhouette above the waterline, people included. `bbox_h_incl_people` is waterline to the highest head.
  - `centroid_x/y`, `area_px`: mask centroid and area.
  - `cam_dx/dy`: background shift.
- `tracks/person_left_rower.csv`, `tracks/person_right_stern.csv`: the part of each person above the gunwale. Columns are x0/x1, head_top_y, cx, head_x, width, height above the waterline (y=540) and height above the hull top.
- `tracks/camera_shift.csv`: phase correlation of the horizon/treeline band (rows 300-470) against frame 0.
- `scripts/`: `track_boat.py` (segmentation and camera check), `track_people.py`, `motion_summary.py`, `inspect_len.py`, `probe.py`.

## Method
- The silhouette is nearly black (grey 0-30) against water (grey 50-140). I thresholded at grey < 35 in rows 470-575, cleaned the mask with open/close, and kept the largest component.
- The reflection merges with the hull below the waterline, so I cut the mask at row 540. I checked this on zoomed frames: the hull bottom is at ~538-539 in every frame, and the overlays in `frames/ov/` show the red mask covering the hull exactly.
- Spot checks of the hull tips against zoomed frames:
  - frame 0: bow ≈ 758-761, stern ≈ 972
  - frame 120: bow ≈ 578, stern ≈ 811
  - frame 219: bow ≈ 415-419, stern ≈ 660-666
- The people are the two blobs above the hull top.

## Key numbers (px)
- **Hull length (bow to stern):** 212 (f0) → 232 (f110) → 247 (f219), growing smoothly.
- **Hull height:** 34 → 40.
- **Boat centre x:** 866.5 (f0) → 538.0 (f219), a net -328.5 px. Bow -347, stern -310.
- **Pixel rate:** grows from about -1.36 px/frame (frames 0-55) to -1.62 px/frame (frames 165-219). The boat is probably not speeding up; it gets nearer, so the scale grows. The pixel speed over 10 frames varies between -1.1 and -1.8 px/frame, which may be oar strokes or mask noise.
- **Vertical position:** steady (cy 519.5-522.5).
- **Camera shift:** under 0.2 px throughout, so the camera is static.
- **Events:** the boat moves the whole clip. It has no start, stop, turn, contact or bounce.

## Reliability and ambiguity
- Hull tips are about ±2 px. The bow tip is thin and pointed and the stern edge is softened by splash/wake, so the length is about ±3 px. The centre x is about ±1.5 px.
- **Perspective:** the boat's apparent size grows 16.5% over the clip because it approaches the camera. Under the annotators' single-scale convention, the result depends on which frame the prior's pixel length is taken from. The median length is 232 px (≈ frame 110, mid-clip). Frame 0 is 212 px and the last frame is 247 px.
- The bow-to-stern centre differs from the mask centroid, which is shifted by the people. Both are recorded.
- Oars are thin, partly in the water, and not segmented. Dark reflections below y=540 are excluded.
- The people are seated and seen as silhouettes: only head and torso show above the gunwale, so their heights are partial. The left person is the rower.
- Static extents (treelines, reeds, horizon) are visual estimates from a gridded frame 0, accurate to about ±10 px.
