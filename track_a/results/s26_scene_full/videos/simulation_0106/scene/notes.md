# simulation_0106 — measurement record

Simulation (Blender render), declared 2D, 24 fps, 72 frames (t = frame/24), 1920x1080.
All values in pixels (x right, y down) and frames/seconds. No metric scale is assumed.

## Scene
Two spiky virus particles (coronavirus-like: dark blue-teal spherical body, ~40 thin spikes with
dark-red knob tips) on a flat uniform grey background (RGB 206). Nothing else: no ground, no
static objects, no markings. Camera static (background identical in every frame).

- **virus_left_small** — left one, slightly smaller (body radius 123.8 px at f0). Moves straight
  UP (dx ≈ -0.4 px/frame, dy ≈ -11.5 px/frame at start rising to ≈ -12.9 later), exits the top.
- **virus_right_large** — right one, slightly larger (body radius 139.1 px at f0). Moves straight
  DOWN (dx ≈ -0.4, dy ≈ +11.5 px/frame at start falling to ≈ +10.3 later), exits the bottom.
- Both slowly rotate (spike pattern changes), so whole-object extents fluctuate by a few px.

## Files
- `scene.json` — inventory, frame-0 positions/sizes, events, camera notes.
- `tracks/<name>.csv` — one row per frame the object is visible (left 0–54, right 0–50; after
  that only spike tips remain, which are not tracked). Columns:
  `ref_x, ref_y` = centre of the spherical body (object origin); `body_radius` = fitted body
  radius (body diameter = 2x); `body_fit_resid` = median circle-fit residual; `bbox_*` = box of
  the whole object including spikes (clipped at the image edge); `mask_len_main / mask_w_across`
  = extents of the whole mask along / across its principal axis; `mask_height` = bbox height;
  `mask_area`, `mask_cx, mask_cy` = mask centroid (biased once cut by the edge);
  `body_truncated` = body circle touches the image edge; `occluded_or_cut` = whole mask touches
  the edge (extents then are not full sizes); `ref_reliable` = 0 when the circle fit fails.
- `scripts/track.py` (tracking), `overlay.py` (check images), `stats.py` (step/size summary),
  `probe.py`, `view.py`.

## Method
Mask = RGB L1 distance from background > 40. Body = morphological opening of the mask with a
91-px disc (removes spikes); centre and radius = least-squares circle fit to the body contour
points not on the image border (refit after dropping the worst 20 % residuals), so the centre is
still measured when the body is partly out of frame. Whole-object pixels are assigned to the
nearest body (distance minus radius). Overlays at frames 0/20/40/48 confirmed the circles sit on
the bodies and the boxes enclose all spikes.

## Reliability
- Centres: ~±0.5–1 px per frame while the body is fully visible (left 0–36, right 0–27);
  per-frame steps then scatter ±1 px (single-frame speed noise ~±10 %; use multi-frame fits).
  While truncated the arc fit gets noisier (right frames 38–45 steps 7–12 px; left 37–50 ±1.5 px).
  Flagged unreliable: left 51–54, right 46–50 — do not use.
- Frame 10 (left) has a 13.4 px step followed by normal steps: fit jitter.
- Full sizes (incl. spikes) only valid with occluded_or_cut = 0: left frames 0–27, right 0–13.
  Body radius valid with body_truncated = 0: left 0–36, right 0–27.
- The two objects' spike tips interleave around x≈970–986 at frames 0–1 (boxes overlap slightly);
  assignment there is by nearest body and may misplace a few tip pixels.

## Ambiguities / caveats
- **Apparent size changes despite "2D"**: left body radius grows ≈ +0.22 px/frame (123.8 → 133.5
  at f48), right shrinks ≈ -0.16 px/frame (139.1 → ~131 at f41–44); whole-object boxes follow
  (left 519 → 534 px wide by f27, right 567 → 559 by f13). Pixel speed changes in the same sense
  (left 11.5 → ~12.9 px/frame, right 11.5 → ~10.3). So the left one likely drifts toward the
  camera and the right one away (or there's real acceleration as well); a single m/px scale is
  only approximate: about ±4 % over the clip. If a question gives a size prior, its pixel size at
  the relevant frame (or frame 0) is in the CSV.
- Motion starts at frame 1 (frames 0 and 1 are identical); already ~11.5 px/frame on the first
  step (no visible ramp).
- Frames 61–68: the remaining spike tips at the edges render pale grey (shading); frames 69–71
  empty.
- Spikes give an extent ~2.1x the body diameter; "size" questions most likely mean the whole
  object's bounding box (spikes included), which is bbox_w/bbox_h at uncut frames.
