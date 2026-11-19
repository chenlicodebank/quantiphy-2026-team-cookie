# simulation_0016 – measurement record (pixels, seconds)

Video: 3D Blender render, 1920x1080, 33.004425 fps, 97 frames (t = frame/fps). Only x 420–1499 is rendered
(1080x1080 square); the sides are black bars. Scene: top-down view of a gallery floor with a white abstract
sculpture on a square plinth at the exact image centre, a 4-cushion bench left and right of it, a dark pedestal
with a bronze sculpture at the top-left (cut by the top edge), a grey pedestal with a small silver sculpture at the
bottom, marble floor tiles, and sunlight window-shadow bands. **One moving object: a walking man** (white t-shirt,
jeans, black shoes, face blurred) who comes in from the top edge next to the bronze pedestal and walks straight
down the image (+y, x ≈ 812–836) on the left of the central sculpture. He walks the whole clip (no start, stop or turn).

## Files
- `scene.json` – inventory (all objects, extents, positions), camera, events, file index.
- `tracks/person.csv` – one row per frame 0–96:
  - `pelvis_x, pelvis_y` – **primary pelvis (origin) estimate**, ground-based (see below). Negative y in frames 0–6 =
    pelvis still above the image (extrapolated); `pelvis_in_image` flag.
  - `pelvis_head_x, pelvis_head_y` – alternative per-frame pelvis estimate from the head point (frames 22–96).
    Agrees with the primary to mean (1.3, 1.7) px, sd ~2 px. Has real gait wobble plus ~1–2 px measurement noise.
  - `ground_x, ground_y` – the floor point under the body (pelvis foot-point), from the footprints.
  - `head_x, head_y, head_top_y` – head point = centroid of the top 20 px of the person mask (frames 20–96).
  - `front_foot_x/y` – lowest (front) toe point of the mask. It sits still during each stance, so it shows the footprints.
  - `mask_cx/cy, bbox_*, mask_len_px, mask_wid_px, area_px` – person silhouette (minAreaRect length/width).
    `mask_shadow_merged=1` (frames 84–95): bbox/length include part of the cast shadow, so treat those extents
    as too big. `cut_by_top_edge=1` frames 0–19. `occluded` is always 0 (nothing occludes him).
  - `head_to_front_foot_px` – image length of the person, head point to front toe.
- `tracks/person_geometry.json` – footprints, perspective fit (k, V, toe offset, residuals).
- `tracks/person_raw.csv, person_kp_raw.csv, person_head_raw.csv` – raw per-frame outputs of the scripts.
- `scripts/` – bg.py (median background, camera-motion check), track_person.py (mask), keypoints.py (feet),
  head_track.py, build_tracks.py (perspective fit + final csv), tiles.py (floor grid), crops.py and
  check_overlay.py (visual checks), probe.py (pixel colour probe).

## Camera and perspective
- Static: phase-correlation shift of the background is < 0.03 px.
- **Nadir (straight-down) view.** The floor-tile grout lines are evenly spaced over the whole image: 131 px in y
  (lines at y = 48…966) and 140 px in x (lines at x = 539…1379), identical at both image edges. So the floor is parallel to
  the image plane, there is no horizon, and **one floor-level px→m scale holds everywhere**. Tiles look 140×131 px.
- Vertical lines point radially away from the image centre (960,540). That point is the vertical vanishing
  point, i.e. the image of the point straight below the camera. A point at height h over floor point G images at
  V + K(h)(G − V), K(h) = H/(H − h), where H = camera height. A free fit from the person gives V ≈ (951, 594). The
  floor grid shows no tilt, so V = (960, 540) is used; both fits give identical residuals (≤ 2.2 px).
- Head magnification k = K(head point) = 1.256 ⇒ H = 4.91 × (height of head point). The head point is about the
  head centre, ~stature − 0.10 m. With ~1.65 m that gives H ≈ 8.1 m. **This is an estimate, not given.**
- For depth_info questions: the camera-to-pelvis distance is d = sqrt((H − h_p)² + r²), where r = horizontal offset
  from the point below the camera = (pixel distance of the pelvis from (960,540)) × (H − h_p)/f. Focal length f is unknown. Get it
  from the given depths, a known size, or the tile/footstep scale.

## How the pelvis was located (the main uncertainty)
In this top-down view the pelvis is hidden under the torso, so it is computed, not seen:
1. Footprints: the front-toe track has 6 stationary plateaus (stance). Positions (x, y), first–last frame:
   (836.0, 99.4) 3–13; (820.9, 168.3) 22–30; (835.3, 235.3) 40–47; (820.7, 301.5) 56–64; (835.6, 368.3) 72–81;
   (820.8, 436.4) 90–96. Each plateau ends when the other foot swings past, i.e. at mid-stance, when the pelvis is
   over the stance foot. The mid-stance y values lie on a straight line in frame number to within 0.9 px
   (y = 3.952·frame + 48.86), so the walk is uniform and straight. Lateral midline x = 828.2.
2. Fitting head = V + k(G − V) at the mid-stance frames, with G = footprint + a constant toe→ankle offset, gives
   k = 1.256 and offset (1.9, −11.0) px (the ankle/body is 11 px behind the toe tip, which makes sense).
3. Pelvis = V + k_p(G − V), with k_p = 1/(1 − ρ(1 − 1/k)) = 1.134. ρ = pelvis height / head-point height = 0.58
   is **assumed** (≈ 0.95–1.0 m / 1.65 m). If ρ changes by ±0.05, k_p changes by ±0.01 and pelvis_y by about ±3 px.
   The primary pelvis track is therefore a straight uniform line (x = 812.6). It does not contain the pelvis's real
   in-stride speed wobble or ±~5 px side sway. Use pelvis_head_* if a question needs frame-level detail. Both
   estimates were drawn on frames (frames/check_sheet.png, not kept in the record) and sit on the waist/shirt-hem
   area of the torso.
- Ground (floor) displacement per frame is 3.95 px. Pelvis-level image displacement is k_p times that (the pelvis
  is closer to the camera). Convert pelvis motion with the scale at pelvis height, or convert the floor point with
  the floor scale.

## Person size cues
- The apparent length (head_to_front_foot 142 px at frame 20 down to ~75 px at frame 96, mask_len 160 down to 90) is
  mostly perspective lean, which shrinks as he nears the image centre. **It is not his height** and not a depth change;
  he stays at the same depth from the camera plane. True height needs H: h_head = H(1 − 1/k).
- Width across the body (shoulders/arms) is ~58–74 px, depending on arm swing.
- Step length on the floor is ~67.4 px between successive plants (stride = 2 steps ≈ 135 px), and the step period
  is ~17 frames (0.51 s).

## Static objects (pixel extents from the median background; ±2 px)
See scene.json. Central plinth 156×156 px centred (960, 539). Benches 235 (left) / 224–258 (right) px long in
y and 76 px wide; their centres are 763 px apart in x. Bottom pedestal top face 80×83 px. The top-left pedestal is
cut by the image edge. Heights of the static objects cannot be measured in this view: only their side faces show,
as 37–42 px lean bands for the pedestals.

## Reliability and ambiguities
- Footprints, timing and floor positions: good (±1 px). Camera static: certain. Nadir view: strong evidence.
- Pelvis absolute position: ±3–5 px (depends on ρ and on the head-point definition). Head point: ±2 px; it is biased
  in frames 20–30 when the head is sunlit and low-contrast.
- Mask extents: fair. The soft cast shadow (to the upper right) was removed with an edge-based criterion, but parts
  of the shadow merge in frames 84–95 (flagged), and the white shirt sometimes has holes. Bboxes ±5 px.
- Sunlit/shadow bands on the floor change the person's brightness. There is no motion blur to speak of.
- There is only one person and one moving object, so there is no identity ambiguity.
