# simulation_0240 — measurement record (pixels, seconds)

Video: 1080x1920 portrait, 24 fps, 50 frames (t = frame/24, frame 0 = 0 s, last frame 49 = 2.0417 s).
Source: simulation (Blender), declared **2D**. Camera **static** (no pan/zoom/shake; frame-to-frame
difference over sky/house < 0.05 grey levels), so image pixels = scene positions directly.

## Scene
Side view of a two-storey half-timbered house (brick ground floor with three arched windows, cream
timber-framed upper storey, gabled roof) on a lawn. Three animals walk/hop **left -> right** parallel to the
house front, all moving for the whole clip:
- **chestnut_horse** – reddish-brown horse with a grey-brown head and white socks, on the left (trailing).
- **pale_horse** – cream/beige horse with dark mane/tail, in the middle (leading horse).
- **rabbit** – small brown rabbit hopping on the grass just ahead of the pale horse's front hooves.
Static: house (with windows, shutters, roof), lawn, two small red flowers in the foreground grass, sky.

## Files
- `scene.json` – inventory (description, how to tell objects apart, moving or not, visible frames),
  static extents (house, windows, shutters, flowers, horizon), size statistics and mean x-step of each
  animal, events, camera info.
- `tracks/<object>.csv` – one row per frame (all 50 frames for all three animals):
  `frame, t, bbox_x0, bbox_x1, bbox_y0, bbox_y1` (inclusive pixel box), `bbox_cx, bbox_cy` (box centre),
  `mask_cx, mask_cy` (silhouette centroid = reference point), `len_px` (horizontal extent = nose-to-tail
  for horses, since they move horizontally), `height_px` (vertical extent = hoof to ear top),
  `axis_len_px, axis_wid_px, axis_deg` (extent along / across the mask's principal axis – for horses
  the silhouette is nearly square so this axis is diagonal; prefer len_px/height_px), `area_px`,
  `touch_other` (mask within 5 px of another animal's mask), `edge` (touches image border; always 0).
  Occlusion: no animal is occluded by another or by scenery except the hooves/rabbit feet partly sunk in
  grass blades.
- `check_ov2A.jpg`, `check_ov2B.jpg` – mask outlines, boxes and centroids drawn at frames
  0,6,12,18,24 and 30,36,42,49 (crop x 50-1000, y 820-1090, scaled 0.7) – visually checked.
- `scripts/` – bg.py (median background, camera check), track.py (pass 1 masks), track2.py (final masks
  and track CSVs; needs frames/pass1_masks.npy from track.py), static.py (house/flower edges),
  summarize.py, write_scene.py; probe*/dbg/segtest were exploration.

## Method
Pass 1: colour mask (saturated orange-brown) for the chestnut horse and rabbit, difference to composite
backgrounds (frames 0/36/49 stitched where the animals are absent) for the pale horse and the chestnut
head. Pass 2: a clean background averaged from all frames where each pixel is >12 px away from every
pass-1 mask (covers all but a small patch behind the chestnut horse's neck), then |frame - bg| > 40
(sum over BGR) split into objects by overlap with pass-1 masks, holes filled, stray specks and thin
hoof-shadow streaks on the grass removed. Rows below y = 1066 are cut (grass shadows).

## Key numbers (pixels)
| object | len_px (median, range) | height_px (median, range) | mean x-step px/frame | y of centroid |
|---|---|---|---|---|
| chestnut_horse (f0-48) | 187 (166-213) | 166 (159-169) | +3.15 (f0-48) | ~961 |
| pale_horse | 228 (215-244) | 177.5 (168-188) | +5.89 | ~960 |
| rabbit | 45 (38-54) | 34 (26-38) | +6.25 | ~1050 |

Lengths vary with the gait (legs stretch fore/aft; the chestnut head mask is the noisiest part, ±10 px).
A clean full-length frame for each horse: pale horse ~230 px nose-to-tail, ~180 px high; chestnut ~185-190
px long, ~166 px high. Vertical position is constant (no up/down motion apart from gait bob of 1-3 px).
Positions: chestnut mask_cx 234.1 (f0) -> 385.5 (f48); pale 496.3 (f0) -> 785.2 (f49);
rabbit 614.0 (f0) -> 920.1 (f49). Per-frame centroid steps are noisy (±2 px) because of leg motion;
fit over several frames for speeds.

## Events
- Frame 0: all three animals already moving right; nobody starts or stops inside the clip.
- **Frame 48 -> 49: the chestnut horse jumps back to its frame-0 position (mask_cx 385.5 -> 234.6,
  -151 px in one frame).** This is an animation-loop reset, not real motion; treat frames 0-48 as its
  continuous walk. A one-frame backward difference at frame 49 would give a spurious huge speed.
- No contacts/collisions; the rabbit stays 5-40 px ahead of the pale horse's front hoof.

## Static objects (frame 24, pixels)
House: roof peak y≈262, roof top edge y≈295, roof x 215-865 (at y 450); upper storey x 200-880
(680 px wide), y 625-833; gable eaves lowest at (180,625) and (905,625); brick ground floor x 250-830
(580 px wide), y 835-1038 (203 px high); total peak-to-wall-base ≈ 776 px. Windows (arched): left
x 272-335, centre 507-572, right 745-808, all y 848-950 (≈64 x 102 px). Big central upper shutter
x 466-615, y 628-792 (149 x 164 px). Horizon (far lawn edge at image sides) y≈988. Red flowers:
(326,1248) 22x14 px and (969,1658) 24x24 px.

## Reliability / ambiguity
- Horse boxes ±3-5 px (edges against brick of similar colour; chestnut head is grey-brown like the
  brick, recovered from the clean background – ±10 px at its muzzle in a few frames, e.g. frames 3-4, 8,
  22-24 show larger x1). Pale horse rear legs occasionally partly missed inside the box (box unaffected).
- Rabbit bottom often clipped at y = 1066 by the processing cut and hidden in grass; its height_px is a
  lower bound by a few px; x-extent and centroid x are reliable (±2 px).
- 2D scene: one metres-per-pixel scale. Ground-contact rows differ slightly (chestnut hooves y≈1048, pale
  horse ≈1055, rabbit ≈1062-1066), suggesting small depth differences (rabbit nearest); apparent sizes do
  not change over time.
- Reference point: mask centroid (body centre proxy, near a quadruped rig's root/pelvis in x). Using
  bbox centre instead changes x by a few px per frame (head/leg pose).
