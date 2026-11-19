# simulation_0261 – measurement record

Scene: a 2D simulation (Blender) render, 1080x1920, 24 fps, 50 frames (t = frame/24). There is one object: a beige ceramic
mug with its handle on the right. It falls straight down from the top of the image (y≈78 px at frame 0) onto a plain beige
floor, gives a small rebound/rock and then rests (y≈1626.6 px). The backdrop has no other objects. The camera is static.

## Files
- `scene.json`: inventory, extents, camera, events.
- `tracks/mug.csv`: one row per frame (0-49). Columns:
  - `frame`, `time`
  - `cx,cy`: centroid of the mask, handle included
  - `bbox_cx,bbox_cy`, `x0,y0,x1,y1,w,h`: the bounding box, inclusive pixels
  - `area`
  - `occluded`: always 0
  - `body_x0,body_x1,body_w,body_cx`: the cylinder without the handle. `body_cy` is the same as `bbox_cy`.
- `scripts/track.py`: makes the mask from the difference to a clean background. The background is the last frame for rows
  above 1100 and frame 0 for rows below; the threshold is 14 on the max over channels, followed by an open/close.
  Largest component.
- `scripts/body_and_floor.py`: body width (first mask run in the middle rows) and the wall/floor boundary row.
- `scripts/overlay.py`: draws the box and centroid on crops (`frames/overlay.png`). I checked frames 0, 10, 14, 18-21, 23
  and 40: the box hugs the full mug and handle.

## Reliability and caveats
- The object's origin is probably the mug centre. x stays the same within about 1 px. The vertical position of the
  centroid / bbox centre is good to about 1 px.
  - Body centre x ≈ 568.5; bbox centre x = 583.5, pulled right by the handle.
  - Vertical differences are the same for all three reference points.
- Per-frame centroid y steps during the fall: 5.0, 13.8, 22.6, 31.8, 40.6, 49.6, 58.4, 67.0, 76.4, 84.8, 93.6, 102.5,
  111.3, 120.3, 129.0, 137.8, 146.4, 154.9 (frames 1-18).
  - The steps grow by a near-constant ~8.8 px/frame², so this is uniform acceleration from rest at about frame 0.
  - Motion blur is small. The mask does not lengthen at speed.
- Size scale: use the width, not the height.
  - The mug's apparent height changes with perspective: 112 px at the top of the image, 89 px near the image centre
    (frames 13-14), and 102-103 px at rest. This is because the rim/bottom ellipses show when the mug is far above or
    below eye level. Since the scene is 2D and the width is constant, this is not a depth change.
  - Total width with handle = 112 px (constant). Body diameter = 81-82 px.
  - The best side-view height of the cylinder is about 89 px.
  - If a prior gives the mug "height", be aware that the world AABB height probably corresponds to about 89 px, whereas
    the width prior (with handle) corresponds to 112 px.
- Impact: between frames 18 and 19. Frames 20-22 show a small rebound/tilt: the bbox top rises about 15 px while the
  bottom stays at about 1677, and the centroid rises 5-8 px. The mug is at rest from frame 23/24.
  - The exact contact time within the frame interval is not resolved.
  - The rest-state bbox x0 = 519 includes a faint contact shadow (body starts at 529).
- Drop height: centroid moves from 78.1 to 1626.6 (1548.5 px). The bottom edge moves from 133 (frame 0) to 1676
  (1543 px).
- Wall/floor boundary at image row ≈1535. This is a soft brightness step, not a sharp line.
