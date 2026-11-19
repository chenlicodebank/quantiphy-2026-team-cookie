# simulation_0199 – measurement record

The video is a 2D Blender render, 60 fps, 14 frames (t = 0 to 0.2167 s), 2560x2560 px. It is a product shot: an amber serum
bottle ("SKYNOVA … VITAMIN B 30ml") stands on a light-grey pedestal. A glass dropper with a white bulb lies tilted across the
open neck, and **one amber teardrop droplet** falls from the dropper tip. The camera is static, with a mean frame-0 to frame-13
difference of 0.14 grey levels and no shift. All values are in full-resolution pixels (x to the right, y down) and seconds.
No metric scale was assumed.

## Files
- `scene.json`: the object inventory (descriptions, pixel sizes and positions of static objects), events, camera and
  perspective notes, and the per-frame centroid steps of the droplet.
- `tracks/droplet.csv`: one row per frame from 0 to 10. Columns:
  - `cx, cy`: the mask centroid. This is the reference point for the drop's origin.
  - `bbox_cx, bbox_cy`: the bounding-box centre.
  - `x0..y1, bbox_w, bbox_h`: the bounding box.
  - `area`: the mask area.
  - `len_major, width_minor, axis_deg`: PCA extents of the mask.
  - `occluded`: frames 0–1 are flagged because the drop still touches the glass tip.
- `scripts/`:
  - `diff.py`: coarse detection at half resolution against the median background.
  - `track_drop.py`: full-resolution mask, using frame 13 (no drop in view) as the background, a threshold of 25 and a column window of x 1300–1560.
  - `overlay.py`: draws the boxes and centroids for checking (written to `frames/overlay.png`, which I inspected: every box covers the whole drop).
  - `static_edges.py`: edge profiles for the bottle and pedestal.
  - `write_record.py`: writes the CSV and the JSON.

## Key measurements
- **Droplet size:** about 89 px tall and 57 px wide. It is a rigid, constant shape (point up) at a constant depth. In frames
  8–10 the box height drops to 83–86 because motion blur and low contrast soften the tip. Use frames 0–7 (89–90 px) for its size.
- **Droplet path:** the centroid goes from (1449.3, 747.8) at frame 0 to (1428.2, 2341.0) at frame 10.
  - Vertical steps per frame: 17.1, 48.3, 81.0, 111.5, 145.2, 176.0, 206.9, 236.5, 269.8, 301.0 px.
  - Each step is about 31–33 px larger than the last, i.e. a constant downward acceleration in pixels.
  - It also drifts slowly left, 21 px in total.
- **Events:**
  - The fall starts at frame 0 (t = 0). The drop is detaching from the tip and is effectively at rest at about frame 0.
  - The drop is clear of the dropper by frame 2.
  - Frame 10 (0.1667 s) is the last frame where it is visible.
  - It leaves the bottom of the frame by frame 11.
  - There is no impact or bounce in view.
- **Static objects** (from frame 13):
  - **Bottle:** body x 1704–2131 (427 px wide), shoulder at y about 675, bottom at about 1246, neck top at about 495, liquid level at about 778.
  - **Pedestal:** top edge at y = 1232, left edge at x about 1666 at y = 1500 and 1649 at y = 2500. It runs off the frame to the right and bottom.
  - **Dropper:** tip at about (1440, 700), bulb end at about (2262, 170), so it is about 980 px long at roughly 33° above horizontal. The tube is about 40–45 px wide and the bulb about 110–120 px.

## Reliability and ambiguities
- **Droplet centroid:** accurate to about ±1 px. The mask is clean, the drop is the only moving thing, and there are no similar objects.
  - The origin of the rendered drop mesh is unknown. The centroid sits about 5 px below the bbox centre, so both are recorded.
  - Frame differences of either point give the same motion to within about 1 px.
  - In frames 0–1 the top of the mask overlaps the transparent dropper tip slightly. The centroid is still reliable.
- **Static extents:** about ±3 px for sharp edges (bottle sides, pedestal edges) and ±10–15 px for soft or translucent parts (bottle shoulder, dropper bulb).
- **Shadows:** none on the drop. The pedestal has a light-shaft gradient that does not affect the edges.
