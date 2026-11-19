# simulation_0024_segmented — measurement record

Video: 960x960 px, 25 fps, 75 frames (t = frame/25, 0 … 2.96 s). Source: segmentation of a Blender render, 3D scene.
Background replaced by pure white (255): there is no ground, water, horizon or vanishing point to use.
Units are pixels (x right, y down, origin top-left) and seconds. No metric scale is assumed.

## Files
- `scene.json` – inventory, camera, static-object extents, apparent-size summary, events.
- `tracks/boat.csv` – one row per frame (0–74) for the boat. Columns:
  `ref_x, ref_y` = centre of the bbox of the full boat mask (mast included); this is the default stand-in for the rig origin.
  `centroid_x/y` = mask centroid. `bbox_x0,y0,x1,y1,w,h` = mask bounding box (h includes the mast).
  `length_px/width_px` = min-area-rectangle sides (the mast makes this rectangle skewed, so prefer bbox/hull values).
  `hull_x0/x1/hull_len_px/hull_cx` = horizontal extent of the hull (bottom 30 % of the bbox), i.e. bow-to-stern length.
  `keel_y` = lowest mask row (bottom of the hull). `mast_top_x/y` = top of the mast. `area_px`.
  `occluded` = 1 when clipped by the image edge (frames 0–2, stern at x = 959). `mast_near_rock` = 1 when the mast tip is within 8 px of the rock's bottom edge (frames 0–29), so `bbox_y0`/`bbox_h` may be off by about 5 px there.
- `scripts/` – `probe*.py` (exploration), `track.py` (segmentation and tracking, writes boat.csv, rock_mask.png and rock_stats.json), `finalize.py` (derived columns, checks, scene.json).

## Objects
1. **boat** (the only moving object): a red-and-white fishing boat with a white wheelhouse, red roof, tall mast and the lettering "AH805" on the hull. The bow points left. It is visible in all frames. It moves right to left the whole clip. Bbox centre x goes 763.5 → 292.5; a linear fit of hull_cx gives about −6.44 px/frame, and the per-frame steps are 4–8.5 px (pixel noise of about ±1.5 px, nearly constant pace). It drifts slightly up in the image (keel_y 673 → 656, about −0.29 px/frame).
   Apparent size: hull length about 396 px in frames 1–10 and 387 px in frames 65–74 (−2.3 %). Bbox height including the mast is about 363 ± 3 px. Overall bbox width is about 397 px. The small shrink plus the upward drift suggest the boat recedes slightly from the camera, but it moves nearly parallel to the image plane.
2. **rock** (static): a large pale cream/brown boulder or cliff with dark shadowed facets on its right side. It fills the upper part of the frame above the boat. Image bbox is x 326–959, y 24–313 (634 × 290 px). Mask centroid is (636.6, 167.3) and area is 128,675 px². Its right tip touches the image edge, so its width may be truncated by a few px. It does not move: per-frame bbox and centroid stay within 1–2 px.

## Camera
The camera is static: the rock's mask is constant across all frames. There are no perspective cues in the background. Depth must come from the question's depth_info, with a focal length estimated from depth plus the known size.

## Events
- The boat is already moving at frame 0 and still moving at frame 74. There is no start, stop, bounce or direction change.
- The boat never touches the rock. In frames 0–29 the mast tip passes just below the rock's bottom edge (a gap of a few px). It is pale and nearly white, so its exact top row is uncertain there.

## Method and reliability
Foreground is min(RGB) < 250. The rock mask is the union of the filled rock component over frames 60–74, when the boat is clear of it. Boat mask: foreground minus the rock mask dilated by 5 px, keeping the largest component plus fragments within 20 px, then a 7×7 closing and hole fill. I checked overlays (frames 0, 20, 40, 60, 74): the masks cover the full boat (hull, cabin, railings, mast) and the full rock.
Reliability: horizontal positions and hull length are ±2 px. The bbox centre jitters by about 1–2 px per frame because the thin white railings and mast tip go in and out of the mask, so use fits or multi-frame differences rather than single-frame steps. Frames 0–2 are clipped at the right edge, which biases their x-centre and length; extrapolate from frames ≥ 3. The boat's true origin (rig root) is unknown. Its bbox centre in the image is the best proxy; hull_cx/keel_y give an alternative at the waterline.
