# simulation_0280 – measurement notes

Video: Blender render, 2D scene, 3840x2160, 24 fps, 72 frames (t = frame/24). Camera **static**
(seabed patch phase-correlation shift ≤ 0.03 px in all frames, `scripts/camcheck.py`).
Everything is in full-resolution pixels; no metric scale is assumed.

## Scene
An underwater side view: one large blue whale (humpback-like, long white-flecked pectoral flippers) swims
**right to left** (head on the left) across the frame, a little above a sandy seabed. Its shadow moves
along the seabed. The static props are a pale rock, a dark branching coral bush, and five thin seaweed stalks
in the lower left. Higher up are a darker mid-water band and the rippled surface. The whale is the only moving
object. Nothing bounces, hits anything or is released.

## Files
- `scene.json`: inventory, static object extents, summary pixel sizes, events, camera.
- `tracks/whale.csv`: one row per frame, 0–71. Columns:
  - `ref_x, ref_y`: centroid of the whale mask (proxy for the rig origin / body centre).
    **Biased in frames 0–46** because the tail is cut off by the right edge (`cut_by_right_edge = occluded = 1`).
    It is also moved by tail bending (ref_y rises from 885 to 943 at f27 and falls to 822 at f71, while the head stays level).
  - `snout_x, snout_y`: leftmost mask pixel. Integer values with ±5 px jitter: the snout tip is low-contrast,
    with a thin light rim and a dark mouth notch, so the mask sits about 10–20 px inside the true tip.
  - `jaw_front_x`: mean leftmost mask x over rows 880–979 (the front of the lower head). This is the **smoothest
    translation reference** (rms second difference about 3 px). Net motion is −838 px over 71 frames, about
    −11 to −15 px per frame. `front_x_780_880` is the same measure over rows 780–879.
  - `head_cy`: centroid y of the mask within 450 px behind the snout. The head height stays about level (842–847).
  - `right_x, right_y`: rightmost mask point. This is the image edge (3839) while the tail is cut off, and the fluke tip from frame 47.
  - `bbox_*`: mask bounding box. `axis_len / axis_width / axis_angle_deg`: extents along and across the mask's principal axis.
  - `trunk_top/bot_y_at_snout400`: vertical head depth 400 px behind the snout (about 365 px).
  - `area_px`, `cut_by_right_edge`, `occluded`.
- `tracks/whale_shadow.csv`: the shadow's dark region (Lab L < 105 in y 1450–1900): centroid, bbox, length, height. Lower
  reliability: the left end can merge with the coral and rock, the box is cut by the right edge in frames 0–30, and the
  caustics change the threshold.
- `scripts/`: `whalemask.py` (segmentation), `track.py` (writes both CSVs), `overlay.py` / `maskview.py` / `crop.py` /
  `view.py` (verification images), `camcheck.py`, `stats.py`, `colors.py`. Discarded attempts: `masktest.py`, `snouttest.py`, and
  `headtrack.py` (template matching on the head locked onto edges and background; its output was **not** used, and
  `track.py` was rerun afterwards).

## Method
Whale mask: Lab colour score s = a − b. On the whale s is about 24–27; on water and seabed it is about 0–7. Blur, threshold at 12,
open/close, keep the largest component, add very dark connected pixels (shaded jaw, fluke in silhouette),
and fill holes. Overlays at frames 0, 24, 40, 47 and 71 show the outline matches the body, both flippers and the fluke well.
The snout tip is the exception: the mask is about 10–20 px short there.

## Key pixel numbers
- Whale full length (snout to fluke tip, whole whale visible, frames 47–71): bbox_w is 3303–3454 px (median 3419), and
  along the principal axis 3358–3453 px. With the body nearly straight (frames 49–53) the length is about 3450 px. It shrinks to about 3300 (bbox_w) by
  frame 71 because the tail bends up. In frames 0–46 the length cannot be measured (tail cut off).
- Whale height (vertical bbox, flippers and fluke included), uncut frames: 762–1292 px. Head depth is about 365 px.
- Translation: snout moves from 947 to 95 (−852 px), jaw_front from 1058.5 to 220.1 (−838 px), centroid x from 2335 to 1530. The centroid change is
  not true displacement, because of the tail cut in the early frames. Vertical head motion is under 10 px.
- Rock: bbox (937,1471)–(1167,1579), 230 x 108 px. Coral: (812,1467)–(967,1579). Seaweed stalks: see scene.json.

## Ambiguities and reliability
- Origin: the Blender origin of the whale rig is unknown. For speeds, use the rigid head (`jaw_front_x`, or
  `snout_x` smoothed). The whole-body centroid is only valid from frame 47 on.
- Different head references disagree by about 15–30 px in net displacement over the clip, because of slight pitch and
  mask noise. The per-frame pixel speed is about 12 px/frame (about 290 px/s) and increases slightly over the clip. Fit it from
  the CSV yourself; nothing is modelled here.
- Frame 0→1: the snout moves 8 px but jaw_front does not move. Motion is effectively continuous from frame 0.
- Shadow, caustics and the pale streaks at top right are background, not objects. There is no motion blur problem.
