# simulation_0043_segmented — measurement record

Video: 1080x1080, 24 fps, 72 frames (3.0 s), segmentation video (Blender render, background replaced by white), 3D scene.
Time t = frame/24.

## Content
- **boat** (moving): small fishing boat, white hull with red bottom stripe, red-roofed cabin with thin mast, bow pointing
  left. Visible, unoccluded and fully inside the frame in all frames 0-71. Moves at a nearly constant image velocity
  up-left along its own long axis (bow first): centroid (441.8, 949.1) at frame 0 -> (193.9, 877.8) at frame 71;
  ~3.53 px/frame left and ~1.02 px/frame up, |step| mean 3.67 px/frame (88 px/s). First and second half are the same
  within noise. No start, stop, turn or other event during the clip.
- **rock** (static): large tan boulder/rocky islet in the upper centre, bbox x 391-883, y 12-451 (493 x 440 px),
  centroid (624.8, 204.8), main-axis length 548.6 px, width across 404.6 px (main axis at -37 deg in image).
- Nothing else is visible: no water, ground, horizon or markings.

## Files
- `scene.json`: inventory, pixel sizes, motion summary, camera notes, events.
- `tracks/boat.csv`, `tracks/rock.csv`: one row per frame. Columns: frame, time; cx, cy = mask centroid (proxy for the
  object origin); bbox_cx/bbox_cy = bbox centre; left_pt/right_pt = leftmost (bow tip) / rightmost (stern) mask pixel;
  bottom_y = lowest mask pixel (hull bottom); bbox_x0..y1, bbox_w/h (mask threshold: 255 - min(RGB) > 40, 3x3 opening);
  loose_x0..y1 = bbox with a looser threshold (>15) that keeps the thin mast tip; area_px; mask_length / mask_width =
  extent along / across the mask's principal axis; main_axis_deg (image angle, y down); occluded (always 0);
  touches_border (always 0).
- `scripts/track.py` (mask + tracks + overlays), `scripts/check.py` (linearity, size change, frame-0 check).

## Camera / 3D
- Camera static (rock centroid constant within 0.05 px over frames 1-71).
- High oblique view looking down on the boat (deck and roof visible). No ground plane or vanishing points.
- The boat's apparent size shrinks only ~1.2% over the clip (bbox_w 208.1 -> 205.6 px, mask_length 224.3 -> 221.7 px,
  first/last 10-frame means), so it moves slightly away from the camera, mostly sideways in the image.
  Because the depth change is so small, one px-to-metre scale per depth is nearly the same for the whole clip.
  Combine it with the given depth_info and a known size to get the focal length.

## Reliability and ambiguities
- Boat centroid: per-frame jitter ~0.5 px (rms residual from a linear fit), caused by the thin mast/antennas
  dropping in and out of the mask (e.g. frame 42: bbox top 834 instead of ~826, mask_width 103 instead of ~117).
  Use the hull-based columns (bottom_y, left_pt_x) or the bbox width/length for size; the loose bbox is the fullest
  extent (~212-213 x 144-145 px). For speeds, use differences over several frames, or the linear-fit slope, rather
  than single-frame steps.
- The mask centroid is the centre of the visible silhouette. The boat's Blender root may be at the hull bottom or
  waterline instead, but with a nearly constant velocity this does not change speed or displacement.
- Rock: frame 0 has slightly different texture/compression from the later frames; its geometry is unchanged. Its far
  side is in dark shadow but stands out clearly from the white background, so the mask covers its full extent
  (checked on overlays).
- Boat bbox_w (~207 px) is the horizontal image extent; the boat lies at ~22 deg in the image, so mask_length (~223 px)
  is its length along the hull axis in the image. The true 3D length is foreshortened by an unknown amount.
