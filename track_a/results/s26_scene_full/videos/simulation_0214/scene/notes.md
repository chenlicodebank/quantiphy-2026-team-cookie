# simulation_0214 — measurement record

2D simulation (Blender) clip, 1920x1080, 24 fps, 50 frames (t = frame/24, frame 0 = 0 s, frame 49 = 2.0417 s).
All values are in full-resolution pixels (x to the right, y down) and frames/seconds. No metric scale is assumed.

## Scene
A living room seen from directly above (top-down). On the beige carpet are two walking cats:
- **black_cat**: all black with small white hind paws. It is the upper cat (y ≈ 358) and walks **left to right** (+x) for the whole clip.
- **tabby_cat**: orange/brown with stripes. It is the lower cat (y ≈ 452) and walks **right to left** (−x). It starts almost at rest, speeds up, then slows almost to a stop by the last frame. Its tail swings and curls (white tip).

Static items (frame 0 extents are in scene.json → static_objects_frame0):
- wooden slat bench, top-left: 289 x 120 px
- dark TV console along the top wall
- white vase on the console: about 68 px across
- round pleated white lamp shade: 146 px across
- round fluffy white rug, left: about 476 px across, partly under the sofa
- curved cream sofa: about 885 x 470 px
- two grey cushions
- leaning picture frame, top-right
- carpet edges and walls

**Camera:** static. Phase correlation against frame 0 gives shifts under 0.03 px. The walls' inner faces show it is a perspective camera looking straight down, but both cats walk on the same floor plane. One px→m scale therefore fits both cats. Their apparent size has no trend: it changes only with gait and tail pose.

## Files
- `scene.json`: inventory, per-object summary (positions at frames 0/49, extent ranges), events, static objects, camera.
- `tracks/black_cat.csv`, `tracks/tabby_cat.csv`: one row per frame (0–49). Columns:
  - `cx,cy`: full-mask centroid, including the tail.
  - `body_cx,body_cy`: centroid after a morphological opening that removes the tail. This is the **recommended origin proxy**.
  - `bbox_*`, `bbox_w`, `bbox_h`: mask bounding box including the tail. x is the motion direction.
  - `body_bbox_*`: bounding box without the tail.
  - `mask_len_main`, `mask_wid_across`, `main_axis_deg`: PCA extents of the full mask.
  - `body_len`, `body_wid`: PCA extents without the tail.
  - `area_px`.
  - `gap_to_other_cat_px`: smallest mask-to-mask distance between the two cats.
  - `occluded`: always 0.
  - tabby only: `torso_x,torso_y,torso_ncc` (see below).
- `scripts/`:
  - `bg.py`: camera check.
  - `bg_clean.py`: clean background of the cat strip. It writes `_bg_crop.npy`, which is deleted afterwards; rerun it before `track.py`.
  - `track.py`: segmentation and tracks.
  - `torso_match.py`: tabby texture track.
  - `static_objects.py`, `build_scene.py`, `check_overlay.py`, `inspect_tracks.py`.
  - `seg_explore*.py`, `probe.py`: exploration only.

## How measured
- **Black cat:** largest blob of dark pixels (gray < 60), so its soft shadow is excluded. The small white hind paws are not added; they lie inside the extents.
- **Tabby:** pixels whose HSV saturation rises by more than 20 (or brightness by more than 45, for the white tail tip and paws) against a clean background. The background is a per-pixel median over frames where the pixel is clear of both cats. Shadows only darken the carpet and do not raise saturation, so they are excluded.
- **Mask check:** overlays on frames 0, 6, …, 48, 49 were checked by eye. The masks cover the full cats, including tails, with no shadow.
- **`torso_x/y` (tabby):** frame-to-frame NCC template tracking of a 110x60 px fur patch on the back, with sub-pixel peaks and NCC ≥ 0.94. It is very smooth and good for the speed profile. It may drift: over frames 0→49 it moves −452 px, while the body centroid moves −432 px and the body bbox edges move −422 to −429 px. For long displacements prefer the body centroid or bbox edges; for per-frame speed shape, torso_x is cleanest.
- **Tabby motion profile (torso):** steps in px/frame are 0.5 at frame 1, 2.5 at frame 2, ~5 at frame 5, ~8.4 at frame 10, ~11 at frame 17, ~13 at frames 20–23, 12.5 at frames 24–26, a peak of ~14.1 at frames 30–33, 11 at frame 36, ~9.5 at frame 40, ~5 at frame 45 and 0.9 at frame 49. The body centroid follows the same trend but is noisy (±4 px/frame) from leg and tail motion.
- **Black cat:** steady at ~11.0 px/frame along +x for the whole clip. The head front (bbox_x1) goes 647→1185 and the body centroid 570→1108. y stays within ±2 px. Per-frame centroid steps are 6–15 px (gait noise); use multi-frame differences or the bbox_x1 edge.

## Sizes (px; the ranges come from gait and tail pose)
- **Black cat:**
  - length including tail: 183–200 (median 191)
  - body without tail: about 146–176 (median 156)
  - width across: 39–50 (median ~41)
- **Tabby:**
  - length including tail and head patch: 254–338 (median 285)
  - body without tail: 237–283 (median 251)
  - body width: 98–110 (median 104); width including the curled tail: 102–154
- A top-down view shows no animal height.

## Events
- **Black cat:** already walking at frame 0 and keeps going through frame 49. It never starts or stops in the clip.
- **Tabby start:** begins moving at about frame 1 (t ≈ 0.04 s).
- **Tabby peak speed:** about frames 20–33 (0.83–1.38 s).
- **Tabby near stop:** at frame 49 (2.04 s).
- **Cats pass each other:** body-centre x values are equal at about frame 31.5 (t ≈ 1.31 s), with about 95 px of vertical separation.
- **Closest approach:** at frame 42 (t = 1.75 s) the tabby's white tail tip comes within about 4 px of the black cat's tail. Contact cannot be confirmed; there is no body contact.

## Ambiguities and reliability
- **Origin proxy:** the rig origin of each cat is not visible, so `body_cx/body_cy` stands in for the pelvis/root. Treat it as ±5–10 px along x.
- **Tabby head artefact:** a flat light-brown rectangle (~40x60 px) is drawn where the tabby's head is and moves with it. It is included in the tabby mask and extents. Without it the front edge would be ~10–30 px further back.
- **Cat extents:** reliable to ±3 px for the black cat and ±5 px for the tabby (soft fur edges, low contrast with the carpet).
- **Static extents:** automatic masks are reliable to ±3 px. The cushions, picture frame and sofa outline were read off a gridded frame, so ±10 px.
- **Image quality:** no motion blur of note. Soft shadows lie above and below each cat.
