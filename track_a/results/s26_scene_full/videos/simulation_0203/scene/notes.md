# simulation_0203 – measurement record

2D simulation (Blender) clip, 2124x1080, 24 fps, 30 frames (1.25 s), t = frame/24. Static camera. A desk scene
against a teal wall; the only moving object is a **magnifying glass** (silver ring + clear lens, white ferrule, tan
handle with dark end cap pointing right). It falls straight down from the top-centre (x~1060), hits the desk top at
frame 11, tips its handle up (frames 13-16, highest at 15), falls back (second contact frame 18), rocks and is at
rest from frame 24. All values are pixels / seconds; no metric scale is assumed.

## Files
- `scene.json` – inventory (moving + static objects with pixel boxes), events, camera, pixel sizes of the glass.
- `tracks/magnifying_glass.csv` – one row per frame 0-29: `ref_x, ref_y` (bounding-box centre = reference point),
  bbox (x0,y0,x1,y1,w,h), `mask_centroid_*`, `length_major`/`width_minor`/`major_axis_angle_deg` (min-area rectangle
  of the mask; frames 0-10 only), `lens_centre_*` (approx. = ring left edge + 52 px, frames 0-10 and 18-29), occlusion flag (never occluded),
  `source` (auto_mask / manual_bbox) and a pose note.
- `scripts/` – `diff_explore.py` (frame differences, static-camera check), `track.py` (difference-mask
  segmentation + overlays), `montage.py` (zoomed gridded crops for manual reading), `build_record.py` (writes the CSV).

## How measured / reliability
- Frames 0-10 (in the air, plain wall behind): mask = |frame - clean background| > 30 (background = last frame with
  the landing area patched from frame 0), largest blob; overlays checked: the mask covers ring + handle + cap.
  Bbox edges +-1 px. Vertical positions are very reliable (motion blur small). Centroid of the mask is biased by the
  see-through lens; prefer bbox centre (`ref_x/ref_y`).
- Bbox centre y during the fall: 200.5, 208.5, 228, 261, 308, 367.5, 440, 524.5, 621, 732.5, 857.5 (frames 0-10);
  ring left edge stays at x 979-980 (pure vertical drop; bbox-centre x jitters 1056-1060 only because the
  handle tip foreshortens).
- Frames 11-29 (on the desk): automatic masks were polluted by the contact shadow and the transparent lens, so
  bboxes were read by eye from 3x zoomed gridded crops: +-2 px. Frames 25-29 equal frame 24 (no change).
- Object size: overall length (ring edge to handle tip) **~162 px** when close to horizontal (frames 0-3, 6-10;
  bbox_w 161-164); frames 4-5 look shorter (152-153) because the glass is slightly rotated. Ring diameter ~104 px,
  edge-on thickness 19-22 px (frames 6-8), handle+ferrule ~60 px. At rest it appears 154 px long (lying on the
  receding desk top, slightly rotated) – use the in-air 162 px for a length prior.
- Static objects: boxes read from frame 29 on 50-px grids, +-5 px; the two chairs are blurred (+-10 px).

## Ambiguities
- The Blender origin of the glass is not visible: it could be the lens centre or the overall centre. For vertical
  motion (frames 0-10) both give the same displacement because the glass barely rotates in the air (it does slowly
  tilt from ~4 deg to edge-on and back, changing the bbox height 19-41 px: ~+-10 px uncertainty on bbox-centre y).
  If a question needs the bottom or top edge instead, bbox_y1/y0 are given.
- Impact occurs between frames 10 and 11 (bbox bottom 877 -> 1018; desk-contact height of the bottom ~1018); the
  extrapolated free-fall step (~138 px) lands almost exactly at frame 11, so contact ~ frame 11 (t = 0.458 s).
- Contact shadow under the glass on the desk (not part of object). Faint render noise near the alarm clock and
  phone is not motion.
