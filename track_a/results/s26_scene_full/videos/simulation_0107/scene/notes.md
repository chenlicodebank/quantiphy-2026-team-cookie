# simulation_0107 — measurement record

2D Blender render, 1920x1080, 24 fps, 72 frames (t = frame/24). Uniform grey background (RGB 206),
static camera, no ground, markings or other props. All values are in pixels and frames; there is no metric scale.

## Objects
Two spiky "virus" particles (dark-blue spherical body, dark-red club-tipped spikes):
- **virus_small_left**: the smaller one. It starts on the left (body centre (694.2, 582.7) at frame 0) and moves
  LEFT. Visible in frames 0–69.
- **virus_large_right**: the larger one (about 1.12–1.13x the small one). It starts on the right (body centre
  (1307.5, 615.4)) and moves RIGHT. Visible in frames 0–68.
They look the same apart from size and position. The two never touch: the gap between their masks is 82 px at frame 0 and grows.

## Files
- `scene.json`: inventory, sizes, motion summary, events, camera.
- `tracks/<object>.csv`: one row per frame (0–71). Columns:
  - `cx, cy`: the best estimate of the reference point (body-sphere centre, used as the object origin).
    `centre_source` says how each row was measured:
    - `body_fit`: least-squares circle fit to the body outline. The body is the mask opened with a 181 px disc,
      which strips the spikes.
    - `trailing_edge`: used once the body touches the image edge (small: frames ≥41; large: ≥36). x = the trailing
      mask edge (small: bbox_x1; large: bbox_x0) plus a centre-minus-edge offset. That offset was fitted linearly
      over the reliable frames and extrapolated, because it drifts slowly as the spikes rotate. y = linear
      extrapolation of the fitted y.
  - `cx_bodyfit, cy_bodyfit, body_radius_fit`: the raw circle fit. `bodyfit_reliable` = 0 marks rows where the fit
    is on a clipped arc and is biased. Do not use those rows.
  - `cx_trailedge`, `cx_template, cy_template`: independent cross-checks. The template columns come from colour
    template matching of the frame-0 appearance. Its `template_score` falls as the spikes rotate, so it is
    unreliable once the score is below ~0.5.
  - `bbox_*`, `mask_len_x`, `mask_h_y`, `mask_area`: the full mask including spike tips (|rgb−206| sum > 40).
    `clipped_by_frame_edge` = 1 means the bbox is cut off by the frame. `occluded` is always 0 (nothing occludes anything).
- `tracks/_raw.json, _body.json, _match.json`: intermediate outputs of the scripts.
- `scripts/`: `seg.py` (first look), `track.py` (masks), `body.py` (circle fit), `match.py` (template),
  `assemble.py` (CSV), `overlay.py` (visual check plus per-frame steps), `check.py`.

## Motion (measured, no model)
- Frames 0 and 1 are identical. Both objects start moving between frame 1 and frame 2, already at their full
  per-frame step (no visible ramp).
- Small: straight line, dx = −14.17 px/frame (sd 0.20), dy = +0.14 px/frame. Constant over the whole clip.
- Large: straight line, dx = +13.72 px/frame (sd 0.17), dy = −0.73 px/frame (drifts slightly upward). Constant.
- No bounce, collision, contact or direction change.
- Edge events (also in scene.json):
  - Large: spike tips reach the right edge at frame 24, the body at 36, the centre is outside from frame 46, last
    pixels at frame 68.
  - Small: spike tips reach the left edge at frame 32, the body at 41, the centre is outside from frame 51, last
    pixels at frame 69.
  - Frames 70–71 are empty.

## Sizes (pixels)
- Full extent including spikes, at frame 0:
  - Small: 513 (x) × 515 (y).
  - Large: 573 × 581.
  - While fully in frame the width ranges 513–529 (small) and 573–593 (large), because the spikes rotate slowly.
  - For a size prior that names the virus's world bounding box, these full-mask extents are the best match.
- Body-sphere diameter (circle fit):
  - Small: 243.8 at frame 0, rising to 251 by frame 40.
  - Large: 275.4, rising to 283.6 by frame 35.
  - The growth is probably spike roots joining the outline as the object rotates, not true scaling.

## Reliability
- Body-fit centres are good to about ±0.3 px per frame while the body is inside the frame. Template matching and
  the trailing edge agree on the step.
- Trailing-edge centres (exit phase) are good to about ±1 px. Spike rotation biases the edge, and the step jitters
  by ±1 px from integer edges.
- Ambiguity: a simulation origin could differ slightly from the visible sphere centre. The full-bbox centre differs
  from the body centre by up to ~12 px (large, x) because of asymmetric spikes. Motion steps are unaffected.
- No motion blur, shadows or occlusion. Spike tips are thin, so the mask threshold sets the extents to ±2 px.
