# simulation_0104 – measurement record (pixels, seconds)

2D simulation, 24 fps, 31 frames (t = frame/24), 1920x1080. Static camera, plain blue-grey backdrop.
Scene: a smartphone lying flat (seen edge-on) on top of a telescoping pedestal/lift. The phone and the lift head
rise straight up together; a column shaft extends out of the static base underneath.

## Files
- `scene.json` – inventory, extents, events, camera.
- `tracks/phone.csv` – per frame: centre (cx, cy), sub-pixel top_y / bottom_y of the phone body, bbox, bump_bottom_y
  (lowest pixel of camera bump), length_px (horizontal), thickness_px, occluded.
- `tracks/lift_head.csv` – per frame: band-centre reference (ref_x, ref_y_band_centre), top disc and dark band
  rows/columns, bbox, occluded (1 in frames 0-2: lower part of the band hidden behind the base flange).
- `tracks/column_shaft.csv` – visible shaft rows (top_y moves with head, bottom fixed at 1015) and width (157 px).
- `scripts/` – probe.py (background/camera check, row profiles), track.py (tracking), fix_head.py (head cleanup),
  static_and_overlay.py (row-by-row extents, overlay PNGs in ../frames/).

## Method
Mask = sum |RGB - background mean| > 40. Phone = mask pixels outside the disc x-range; top edge sub-pixel from
the mask fraction of the strip x 700-790 (only phone there). Head band = dark rows (grey < 110) at x 940-980.
Overlays (frames 0, 2, 15, 30) checked visually: boxes sit on the phone and the dark band.

## Key results
- Phone: length 568 px (x 689-1256), body thickness 22.9 px (±0.5, compression), 27 px including camera bump
  (x 1100-1222). Centre x = 973 throughout (no horizontal motion).
- Motion: frames 0-1 at rest; from frame 1 to 27 the phone/head rise by 23.9-24.1 px every frame (mean 23.96
  px/frame; 622.9 px total, top_y 954.98 -> 332.07); frames 27-30 at rest. Start and stop are abrupt (constant
  velocity, no visible ramp). Phone and head move identically (head band top 1011 -> 389).
- Head: disc 318 px wide x 33 px tall, dark band 281 x 42 px. Column shaft 157 px wide, visible length grows from
  0 (frames 0-2) to 587 px (frames 27-30).
- Base (static): flange 345 px wide (y 1020-1037), sleeve 279 px (y 1038-1062), lower post 165 px wide cut by the
  image bottom.

## Reliability / ambiguity
- Phone positions are reliable to ~0.2 px; phone cy is from the body only (bump excluded). The phone is the
  likely "object" of questions (its length or thickness would be the size prior; 2D scene -> one px scale).
- "Height" of the lift/pedestal is ambiguous: the base continues below the image bottom, so the full pedestal
  height is not measurable; only visible parts are recorded.
- Head band rows in frames 0-2 are partly occluded by the base flange (band bottom inferred from 42 px height).
- Origin of the phone in Blender is presumably its geometric centre; its vertical displacement equals that of
  any rigid point on it, so speeds are unaffected by the reference choice.
