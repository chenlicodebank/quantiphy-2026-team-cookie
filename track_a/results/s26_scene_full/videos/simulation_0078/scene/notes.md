# simulation_0078 – measurement record

Overhead (top-down) Blender render, 1920x1080, 24 fps, 72 frames (t = frame/24). Labelled 2D: the uniform grey floor
is the motion plane and faces the camera. Two men walk towards each other along one image row; nothing else is in
the scene (no props, furniture or floor markings). Camera static (fixed render camera; the floor has no texture
so a shift could not be measured directly, but nothing indicates any motion).

## Objects
- **person_A_dark_shirt** – black T-shirt, blue jeans, brown hair. Walks left→right along y≈550, frames 0–71
  (cut by the left edge in frames 0–5). Never stops.
- **person_B_white_shirt** – white/light-grey T-shirt, blue jeans, shoes with white stripes, brown hair. Enters at
  the right edge (first foot pixels frame 2, fully inside from frame 17), walks right→left along y≈558–563 (≈10 px
  below A). Never stops. Faster in the image than A (pelvis ≈14.7 vs ≈11.1 px/frame).
- **floor** – uniform RGB≈136 grey; soft faint shadows under each walker (excluded from the masks).

## Files
- `scene.json` – inventory, camera, key positions, events.
- `tracks/<name>.csv` – one row per frame the person is visible:
  `pelvis_est_x/y` (recommended reference point = pelvis, see below), `head_x/y` (centroid of the brown hair
  blob = top of head), `mask_cx/cy` (centroid of the whole silhouette, jittery because of swinging limbs),
  `shirt_cx/cy` (centroid of the shirt colour), bbox `x0,y0,x1,y1,w,h,cx,cy`, `mask_len_main` / `mask_wid_across`
  (silhouette extent along / across its principal axis, ≈ along / across the walking direction), `main_axis_deg`,
  `mask_area`, `occluded` (never: they never overlap), `cut_by_frame_edge`.
- `tracks/<name>_raw.csv` – raw segmentation output (also jeans centroid, hair pixel count).
- `scripts/` – `bg.py` (floor level), `track.py` (segmentation + tracks), `finalize.py` (pelvis estimate,
  foot plants), `overlay.py` (drawn checks), `plants.json`.

## How measured
Mask = pixels deviating > 28 grey levels from the floor (136) in any channel, opened/closed; pieces assigned to the
person whose shirt colour (black vs white) is nearest; when the two blobs would touch they are split at the
emptiest column between the shirts (not needed in practice – they stay ≥16 px apart). Overlays at frames 6, 9,
17, 30, 36, 46, 71 confirm full silhouettes incl. arms, legs and shoes, and correct identity.

### Pelvis estimate and perspective
The camera is close enough that heights matter: points higher above the floor are pushed away from the image
centre. Each head is displaced outward from its feet (A's head left of its body, B's right), the offset shrinking
as they approach the centre. Measured: the head-top image speed is 1.13–1.14 × the progression speed of the planted
feet (A: head 11.83 vs feet 10.34 px/frame; B: 15.36 vs 13.53), i.e. camera height ≈ 8–9 × head height.
The pelvis is not visible from above, so `pelvis_est = c + (head − c) × 0.942` with c = (960,540) (pelvis at ≈0.53
of head-top height ⇒ factor 1.065/1.13). This is a modelled point: absolute position uncertainty ≈ ±20–40 px along
x (head may not be exactly above the pelvis, lean/bob; principal point assumed), but its frame-to-frame motion is
smooth (head bob ±2–3 px). Valid from frame 6 (A) and 17 (B); before that the head is cut by the frame edge
(use bbox/mask columns there, flagged `cut_by_frame_edge=1`).
Image speeds therefore depend on which height you track: feet (ground) ≈ 0.885 ×, pelvis ≈ 0.942 ×, head-top 1 ×
the head speed. If the prior and the question concern the same kind of point on the two walkers, the factor
cancels; both walk on almost the same row, so the factor is the same for both.

### Gait
Leading-foot plants (frame where the leading edge of the silhouette stops advancing): A ≈ 9, 26, 42, 59 at
x1 ≈ 290, 474, 644, 828 (step ≈178 px, period ≈16.7 frames); B ≈ 10 (cut), 26, 42, 60 at x0 ≈ 1734?, 1522, 1303,
1062 (step ≈225 px). `mask_len_main` oscillates with the stride (A 140–250 px, B 140–255 px; minima when the legs
pass, e.g. A frames 33–35, 49–53, 65–70); this is the only "height-like" extent visible from above – standing
height cannot be measured directly in this overhead view (only via the perspective head offset).
Width across (shoulders+arms) ≈ 115–160 px; bbox height ≈ 140–150 px for both.

## Events
Both walk at roughly steady pace throughout (no start, stop, turn, contact). B enters frame 2 (fully in frame 17);
A fully in frame from 6. At the last frame (71) they are face to face: bbox gap 16 px, pelvis_est gap 216 px in x,
7 px in y; still closing (no contact within the clip).

## Reliability
- head_x/y: ±2 px; bbox and mask extents: ±3 px (limbs with fingertips may lose a few pixels at the threshold).
- pelvis_est: smooth, but absolute offset model-based (see above). mask_cx is identity-correct but jitters
  ±10 px with limb swing.
- B's shirt centroid before frame 11 is invalid (blanked); B's early track (2–16) is partial body only.
