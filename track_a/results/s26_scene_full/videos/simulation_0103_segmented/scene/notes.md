# simulation_0103_segmented – measurement record

2D scene, segmentation video (Blender render, background replaced by white), 1920x1080, 24 fps, 54 frames (t = frame/24).
All values in pixels (x right, y down) and seconds; no metric scale assumed.

## Files
- `scene.json` – inventory, sizes, reference-point definitions, events, camera.
- `tracks/boat.csv`, `tracks/shark.csv` – one row per frame (0-53). Columns: frame, t, cx_bbox/cy_bbox (mask bbox centre),
  cx_mask/cy_mask (mask centroid), x_min/x_max/y_min/y_max, bbox_w/bbox_h, pca_len/pca_wid/pca_angle_deg (mask extents
  along/across main axis), area, touches_* edge flags, occluded_or_clipped, **ref_x/ref_y (recommended origin)**, ref_x_source.
  Boat extras: hull_x_min/max, hull_y_min/max (coloured red/purple pixels only, excludes white mast), bow_tip_x/y,
  stern_visible, hull_len_px. Shark extras: nose_x/y (left-most px), tail_x/y (right-most px).
- `scripts/measure.py` (segmentation + tracks), `scripts/inspect_series.py` (step printout), `scripts/finalize.py`
  (reference points, overlay check image frames/overlay.png).

## Method
Foreground = pixels whose darkest channel is >30 below white, 3x3 opening, components >=150 px. Boat = everything above
y=740, shark = below. Overlays at frames 0,1,10,21,35,53 confirmed boxes cover each object fully.

## Objects
- **boat** (red fishing boat "AH805", white cabin, mast; bow points right). Moves right. Rest frame 0->1, then steady
  ~17.8 px/frame (bow tip steps 16-20 px, integer-pixel noise; 522 at f1 -> 1451 at f53, i.e. 929 px in 52 frames).
  No vertical motion or rotation. Length stern->bow tip 856 px (range 853-857, frames 20-53). Keel y=644, cabin roof y=237,
  bow tip y=368; keel-to-cabin-roof 407 px. Cabin ~175 px wide. Mast always runs off the top edge, so total height is not
  measurable. Stern off the left edge for frames 0-19: ref_x there = bow_tip_x - 427.5 (rigid offset; reliable since the
  shape does not change). ref_y = 440.5 (cabin roof/keel midpoint) – the true Blender origin height is unknown, but y is constant
  so it does not affect motion. In 2D, horizontal speed from bow tip or ref_x are equivalent.
- **shark** (small grey-blue shark, white belly, nose left; y 853-955). Moves left, starts at rest (f0->f1 ~0 px),
  then accelerates: bbox-centre steps ~7.5 px/frame at f2 rising roughly linearly to ~14.5-15.5 px/frame by f50-53
  (nose 1526 at f1 -> 944 at f53). y constant (~904). Length nose->tail tip 275 px (bbox_w 272-278; tail fin flexes
  slightly), height incl. fins 103 px. Never clipped or occluded. Centroid (cx_mask) lies ~24 px left of bbox centre
  (heavy head); ref_x uses bbox centre.

## Static objects / camera
No static objects, ground or markings (plain white). Camera static (no background to verify directly, but both
objects keep fixed y and fixed pixel size). No perspective: side view, motion parallel to image plane.

## Events
- f0-f1: both at rest; motion begins between f1 and f2 for both.
- f20/21: boat stern enters frame.
- ~f41.5: boat bow tip passes shark centre x. Boat ref_x and shark centre do not cross before the end (gap 57.5 px at f53).
  No contact (vertical gap ~210 px between keel and shark top).

## Reliability / ambiguities
- Edge positions +-1 px; per-frame steps carry +-1-2 px jitter (integer edges, segmentation). Use bbox centres or fits.
- Segmentation artefacts on the boat: a small dark-red blob near the stern below the hull (rudder/propeller, ~x stern+30,
  y 570-635), white stern deck cage only partly segmented (appears from ~f30), a few stray white specks near the mast.
  They do not change the stern/bow extents. The boat's top (mast) is clipped in all frames -> boat bbox_h/cy_bbox are
  NOT the true height/centre; use hull_* values.
- Relative scale: the boat is drawn much larger than the shark (856 vs 275 px) – this is a rendered scene, not real scale;
  in a 2D question use one m/px scale from the given prior.
