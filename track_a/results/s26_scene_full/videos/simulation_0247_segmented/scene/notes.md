# simulation_0247_segmented — measurement record

Video: 1920x1080, 30 fps, 75 frames (t = frame/30, 0 … 2.467 s). Source: segmentation of a Blender render
(3D scene), background replaced by plain white.

## Content
- **creature**: one large fantasy quadruped (orange-brown body, long striped horns sweeping back, white muzzle,
  tufted tail). Walks steadily left→right across the whole clip.
- **rabbit**: one small brown rabbit just in front of the creature's front feet, hopping left→right at the same pace.
- No static objects, ground markings or background: nothing else to measure.

## Files
- `scene.json`: inventory, pixel sizes (min/max/mean, frame 0), image motion summary, events, camera notes.
- `tracks/creature.csv`, `tracks/rabbit.csv`: one row per frame (0–74, visible in all). Columns: frame, t,
  ref_x/ref_y (bbox centre), centroid_x/y (mask centroid), bbox_x0/y0/x1/y1, bbox_w/h, bottom_y, mask_area,
  main_axis_len / main_axis_width / main_axis_angle_deg (PCA of mask pixels; for the creature the "main axis" is
  diagonal because of the horns, so prefer bbox_w/bbox_h for length/height), occluded (always 0), n_components.
- `scripts/track.py`: segmentation + tracks (+ overlays written to ../frames/ov_*.png);
  `scripts/summarize.py`: statistics quoted below.

## Method
Foreground = pixels whose minimum RGB channel is < 225 (i.e. >30 below white), 3x3 opening; a 15x15 dilation is used
only to group pixels into components; the largest component is the creature, the second the rabbit (exactly 2
components in every frame). Overlays at frames 0, 37, 74 checked visually: masks cover each animal fully incl. the
pale muzzle, horns and tail; no leakage between the two.

## Key numbers (pixels)
- Creature: bbox height 428–439 (mean 434; horn top y≈363 to hooves y≈799), bbox width 542–617 (mean 580; tail tip to
  muzzle, oscillates with the ~40-frame gait). Centroid moves +586.8 px in x over 74 frames, dy ≈ 0; mean step
  7.96 px/frame (sd 0.77); linear fit 7.87 px/frame, no acceleration. bbox centre: +567 px, 7.71 px/frame (noisier,
  sd 1.68, because the tail swings).
- Rabbit: bbox 77–99 w x 57–75 h (mean 84 x 67; frame 0: 81 x 73). Centroid +572.1 px, mean step 7.74 px/frame,
  fit 7.69 px/frame; steps pulse 4.4–11.6 px with each hop (period ~13 frames, feet lift only ~8 px).
- Rabbit centroid is 239–265 px ahead (to the right) of the creature centroid throughout.

## Events
Both animals move for the whole clip (no start/stop). Rabbit take-offs ≈ frames 3, 16, 29, 42, 55, 68; landings ≈ 9,
22, 34, 48, 61, 73. Creature gait: lowest hoof lifted (bbox bottom 790–795) frames 18–31 and 58–71.

## Camera / 3D
Camera static (no background to check against, but both animals keep constant foot row y≈800, constant top row and
constant apparent size: bbox height varies <3 % for the creature, only pose-driven for the rabbit). So motion is
parallel to the image plane at an essentially constant depth; one px scale per animal applies over the whole clip.
Both feet lines at the same image row suggests similar depth for both, but this is not certain (a nearer rabbit
would sit lower only if the camera looks down; no horizon visible to tell). With depth_info the focal length can be
estimated as f = (pixel size × depth)/(world size) using a given size prior.

## Reliability / ambiguities
- Simulation origins (creature root/pelvis, rabbit origin) are not visible; the mask centroid is the best proxy for
  horizontal motion (the creature's root likely moves at constant speed ≈ 7.9 px/frame). Vertical origin position
  unknown (centroid y ≈ 570 creature, ≈ 768.5 rabbit).
- Creature "length" depends on definition: bbox width includes the tail and backward horns; body length alone
  (rump to chest) is not separately measured. Height includes horns.
- Pale muzzle tip is near-white; threshold may clip a few pixels there (±3 px on bbox_x1).
- No occlusion; masks of the two animals overlap in x-range but never touch. No motion blur of note.
