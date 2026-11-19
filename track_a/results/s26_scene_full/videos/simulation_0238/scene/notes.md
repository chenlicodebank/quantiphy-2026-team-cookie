# simulation_0238 – measurement record

2D simulation (Blender) clip, 1080x1920 portrait, 24 fps, 50 frames (t = frame/24, 0 … 2.0417 s).
All values are pixels / seconds in the full-resolution image (x right, y down). No metric scale is assumed.

## Scene
A static camera looks straight at the facade of a two-storey half-timbered house (brick ground floor with three
arched windows, timber upper storey, brown roof) standing on a grass meadow under a cloudy blue sky. Two horses walk
from left to right (+x) along the foot of the brick wall, side-on to the camera:

* **horse_tan** – light tan/cream horse, darker tail; the right-hand, larger and faster horse (median ~6.4 px/frame).
* **horse_brown** – chestnut horse with white socks, the left-hand, smaller and slower horse (median ~3.0 px/frame);
  its head renders as a dull grey-brown patch. **Between frame 48 and frame 49 it jumps back ~148 px to almost its
  frame-0 position** (animation loop reset). Frame 49 is a discontinuity, not real motion; use frames 0-48 for its motion.

Both horses' hooves are on the same ground line (y ≈ 1041-1050), right in front of the wall, so they are at
practically the same depth: one px-to-world scale applies to both (2D convention). Neither horse is occluded, and they
never touch or overlap. No other objects move. Static extras: three windows, an upper-storey door, shutters, and two
small red flowers in the grass (see scene.json).

## Files
* `scene.json` – inventory (all objects, distinguishing features, static pixel extents), camera, events, summary sizes.
* `tracks/horse_tan.csv`, `tracks/horse_brown.csv` – one row per frame (0-49):
  * `ref_x, ref_y` – **reference point** = centroid of the torso blob (the horse mask opened with a 31 px disc, which
    removes legs, tail and most of the head). Use it as the body-centre / rig-root proxy for positions, displacements
    and per-frame speeds.
  * `torso_x0/x1/y0/y1` – extents of that torso blob (x1 often includes part of the neck).
  * `mask_cx, mask_cy` – centroid of the full mask (moves with leg/head swing; noisier).
  * `bbox_x0, bbox_y0, bbox_x1, bbox_y1`, `bbox_cx, bbox_cy` – full mask bounding box (tail tip/rump … nose; head top …
    lowest hoof).
  * `length_px` (= bbox width, along the motion/main axis; nose-to-tail), `height_px` (bbox height, head/ear top to
    hoof). Width across the body is not observable (pure side view).
  * `area_px`, `occluded` (always 0).
* `scripts/` – `bg.py` (strip extraction + median background), `track.py` (segmentation + tracks), `overlay.py`
  (visual check), `static.py` (camera shift, house/window/flower measurements), `summary.py` (size statistics),
  `view.py`/`probe*.py` (inspection helpers), `finalize.py` (checks + scratch cleanup). Run order: bg.py → track.py
  → overlay.py/summary.py (bg.py recreates the scratch `frames/strips.npz` that was deleted to save space).

## Method
1. Camera: phase correlation of the upper house (never crossed by a horse) against frame 0 → |shift| ≤ 0.01 px. Static.
2. Background: per-pixel median of the strip y 780-1100 over all frames, then refined twice as the median over frames in
   which the pixel is not near a horse mask. The patch at x 222-376, y 933-990 is always covered by the brown horse and
   was filled with brick/window copied from the same rows elsewhere; inside it the horse is found by colour
   (saturated chestnut) instead of difference.
3. Mask: |frame − background| > 24, minus cast shadows on the window glass and the grass (darker, same chroma), then
   GrabCut seeded by that mask. Window glass pixels are kept only if coat-coloured (R − B > 25), because horse shadows
   and reflections change the glass. Heads (low contrast against brick) are grown with a weak threshold (>12) inside a
   box at the front-top of each horse. Blobs are assigned to a horse by nearest previous centroid.
4. Masks/boxes/reference points were overlaid on frames 0, 4, 8, 13, 18, 29, 30, 35, 40, 44, 48 and 49 and inspected.

## Reliability
* Reference point (`ref_x`): good to about ±3-5 px per frame. It jitters with the gait (the torso blob sometimes takes
  in part of the neck or a thigh). Single-frame differences can be off by up to ~±8 px (e.g. brown 28→29 +17 px,
  tan 0→1 +18 px). Smooth over several frames or use longer baselines for speeds. The rear edge `torso_x0` (rump) is
  another fairly smooth body marker. Vertical `ref_y` changes (±8 px) are gait bob plus noise; the motion is horizontal.
* Net displacement: tan ref_x 475.0 → 783.8 (frames 0-49, +308.8 px); brown ref_x 233.3 → 384.7 (frames 0-48, +151.4 px).
* Sizes: bbox length is ±10 px. The mask sometimes clips part of the nose (brown head, e.g. frames 40-48), misses a thin
  lower leg/hoof, or takes in a few pixels of wall shadow between the legs. Length also really changes with gait and
  head carriage. Medians: tan length 228.5 px (p10-p90 218-237), height 169 px (164-172); brown length 183.5 px
  (168-196), height 159.5 px (154-164). Manual check on frame 0: tan tail-to-nose ≈ 394-620 (226 px), brown ≈ 153-339
  (186 px). For a size prior, prefer the median over a single frame.
* Static extents (house, windows) come from intensity edges and are ±3 px. Roof apex and ridge are ±8 px. The upper-door
  and shutter boxes are read off the grid (±5 px).
* Ambiguities: the horse heads are rendered as flat, semi-transparent-looking patches (dull grey-brown on the brown
  horse), which makes the nose-tip position the least certain part. The horses cast shadows on the wall and the window
  glass behind them, which are not part of the horse. Some tiny red specks at the lower right (x 1014-1070,
  y 1708-1747) are grass tips, not objects.
