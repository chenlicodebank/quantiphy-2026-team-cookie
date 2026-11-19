# simulation_0281 – measurement record

Video: 3840x2160, 24 fps, 72 frames (t = frame/24, 0 … 2.958 s). Simulation (Blender), 2D scene.
Top-down view of a single whale swimming leftward over a sandy seabed with animated caustics.
All values in original-resolution pixels; no metric scale is assumed.

## Files
- `scene.json` – inventory, camera, static-object positions/sizes, whale size summary, events.
- `tracks/whale.csv` – one row per frame 0-71:
  `cx,cy` mask centroid; `bbox_cx,bbox_cy`, `x0,y0,x1,y1,bbox_w,bbox_h` mask bounding box;
  `nose_x,nose_y` snout tip (leftmost mask column, y = mean of the leftmost 40 px of mask);
  `tailtip_x,tailtip_y` rightmost fluke point; `axis_angle_deg` body axis (PCA of eroded trunk, 0 = head pointing -x);
  `length_axis` mask extent along the body axis (nose to fluke tip); `span_across` extent across it (fin tip to fin tip);
  `trunk_width` body width just behind the head (fins excluded); `area` mask pixels; `occluded` (always 0).
- `scripts/` – `probe.py` (colour stats), `mask_test.py`, `track_whale.py` (segmentation + track + overlays), `summarize.py`.

## Method
Whale mask = colour threshold (HSV hue >= 100 or Lab a >= 120 after 3 px blur; the seabed is hue 97-99),
open/close, largest component plus fin pieces within 40 px, 61 px elliptical closing, hole fill. Overlays for frames
0, 24, 48, 66, 71 were checked by eye: outline follows snout, pectoral fins and flukes; the pale dorsal edge of the
back is sometimes cut by up to ~40 px (affects trunk_width, not length or bbox_w).

## Key findings
- Camera static (seabed prop at the same pixels in frames 0 and 70); no background shift.
- Whale: at rest frames 0-2 (nose x 1117), then swims straight in -x at nearly constant speed:
  nose x ≈ 1127.5 - 8.567·frame for frames 3-71 (≈ 8.6 px/frame ≈ 206 px/s; quadratic term ≈ 0, i.e. no measurable
  acceleration); per-frame nose steps are integer-quantised (5-13 px, mean 8.6). Vertical drift of the nose < 5 px
  (y ≈ 1115). Nose ends at x = 517 in frame 71 (net ≈ 600 px).
- **Use the nose (rigid snout) for position/speed**; the Blender origin should translate like it. The mask centroid and
  bbox centre are NOT reliable for speed: the flukes beat up/down (top view → tail foreshortened), so the tail tip
  stays near x≈3010-3050 during frames 28-56 while the nose advances, making the centroid speed swing 0-26 px/frame.
- Whale size: length (nose to fluke tip) 2126-2403 px (mean 2274; 2352 at rest in frame 0; varies with tail
  stroke, min frame 26, max frame 63). Fin-to-fin span (bbox height) 958-1225 px (mean 1101). Trunk width
  466-605 px (mean 531; probably underestimated, true ≈ 560-620). For a "length" prior, the rest/frame-0 value 2352 px
  or the max 2403 px are the best candidates for the model's full length (bbox of the rig).
- Static seabed prop upper-left (blue rounded object + pale slab + 5 green weed tufts), centre ≈ (1165, 730);
  extent incl. plants ≈ 490 x 260 px; blue object ≈ 130 px across (eyeballed, ±10 px).
- Whale shadow: faint dark blur on the seabed lower-left of the whale, moves with it; not tracked.

## Reliability / ambiguity
- Nose x: ±3 px per frame (quantised), very good over longer intervals. Lengths: ±10 px at each end.
- Fins and flukes deform (animated swim cycle) – any size based on fins/tail changes over time; frames 64-71 show the
  dark underside of the fluke as it twists.
- Motion-start frame ±1 (frame 2→3 is the first nose step; frame 3→4 is 15 px, so motion likely begins ~frame 1-2).
- Only one moving object; no contacts, bounces or direction changes.
