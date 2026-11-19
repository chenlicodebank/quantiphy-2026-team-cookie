# simulation_0166 – measurement record

Simulation (Blender) clip, 1920x1080, 24 fps, 80 frames (t = frame/24, 0 … 3.2917 s). inputs.json labels it **2D**.
The render is a perspective night-time street view (a main street recedes to a vanishing point at about (990, 598)),
but both moving objects travel **left to right, parallel to the image plane, along one horizontal cross street**
at almost the same depth. So the 2D convention (one metres-per-pixel scale from the prior object) applies.
**Camera is static** (phase-correlation shift < 0.08 px over all frames).

## Files
- `scene.json` – inventory (moving + static objects), rigid pixel sizes, events, camera/perspective cues.
- `tracks/van.csv`, `tracks/cyclist.csv` – one row per frame the object is visible:
  `ref_x, ref_y` = centre of the rigid side-view box (reference point / origin proxy);
  `midaxle_ground_x, ground_y` = point midway between the wheel centres, at tyre-contact height;
  `bbox_*` = rigid side-view box placed at the tracked position (can extend off-image);
  `length_px, height_px` = that box's size (constant);
  `vis_*`, `vis_len_px, vis_h_px` = what the foreground mask actually shows (body rows only), shrinks when occluded/off-image;
  `occluded` flag + `occlusion` text (frame edge, poles, foreground fences, van/cyclist overlap);
  `match_ssd` = template-match residual (lower = better; 0 at the template frame); `note`.
- `scripts/` – all code: `bg.py` (camera check), `seg.py` (colour median background -> ../frames/bgc.png, needed by the others),
  `groups.py` (foreground column groups), `track.py` (masked template tracking), `build.py` (CSV), `check.py`, `overlay.py`/`view.py`/`gridbg.py` (visual checks),
  `masks*.py` (segmentation experiments). `work/` holds intermediate json.

## How measured
- Foreground = |frame − temporal median background| > 22 (max over RGB), blue siren glow removed for tracking.
- Positions: masked SSD template matching (gray), horizontal sub-pixel (parabola), vertical ±4 px search. Van template = frame 66
  (van at image centre, pure side view, siren light bar excluded); cyclist template = frame 45 (near centre). Result dy = 0 in every
  frame for both (purely horizontal motion). Visual overlays at frames 3, 12, 21–28, 32, 40, 45, 74, 77, 79 confirmed boxes on the
  right object and full extent.
- Rigid sizes (pixels, side view, measured at the centre frames with a 20-px grid, ±2 px):
  - **Van**: length 438 (x 748–1185 at f66), height ground→roof 188 (y 556–743), ground→top of light bar 200 (y 544), wheel Ø ≈ 68,
    wheelbase 275 (wheel centres x 840 / 1115, y 710). Width (depth) not observable.
  - **Cyclist (person + bike)**: length 163 (x 820–982 at f45, rear tyre to front tyre/basket), height ground→helmet top 163 (y 576–738),
    wheel Ø ≈ 66, wheelbase (hub to hub) 95 (hubs x 854 / 949, y 706). Hip/saddle ≈ (ref_x − 11, 657).
- Pixel motion (for orientation only; answer sessions should refit): van +27.00 px/frame (std 0.15), cyclist +21.03 px/frame (std 0.35);
  both constant over the whole clip, no start/stop, no acceleration visible.

## Events
- f0 (0 s): cyclist already riding, entering at the left edge; fully in frame from f6 (0.25 s).
- f21 (0.875 s): van front appears at left edge, already at full speed; whole van inside the frame from f39 (1.625 s).
- Van closes on the cyclist by ≈6 px/frame; template-box gap van front → cyclist rear: 111.9 px at f60, 29.1 at f74, 4.6 at f78, −1.3 at f79
  (image overlap at the last frame). Centre-to-centre horizontal distance 411.4 px (f60) → 298.2 px (f79), see CSVs for every frame.
  The cyclist's tyres are 5 px higher (farther), so f79 is image overlap, no visible collision reaction.
- f79: clip ends with both still moving; neither leaves the frame.

## Reliability / ambiguities
- Van ref_x: ±0.5 px for f24–79. **f21–23 are extrapolated** (only a sliver of bumper visible; constant 27.02 px/frame step) – flagged in `note`.
- Cyclist ref_x: ±1 px (pedalling legs perturb the match slightly; worst steps 19.5/22.6 px at f24–26 where pole + fence occlude).
- Perspective: when the van is left of image centre, its front face is also visible, so the raw mask (`vis_len_px`) reads up to ~460 px
  instead of 438; the rigid side box (`length_px`) is the correct side-view length. Use frames near the image centre (f60–72 van,
  f40–55 cyclist) for clean pixel sizes.
- Depth: van tyres at y 743, cyclist at y 738 (horizon ≈ 598) → cyclist ≈ 3–4 % farther; same pixel scale is a good approximation
  but not exact.
- Origins: simulation origins (van root, cyclist pelvis/root) are not visible; ref_x/ref_y are box centres. Since motion is rigid
  translation, speeds/displacements are identical for any body point; for distances between the objects, the choice of point
  (box centre vs mid-axle vs hip) matters by up to ~10 px horizontally – mid-axle and hip columns are provided.
- Occlusions: left lamp pole x 205–232 (cyclist f8–17, van f30–47), pole x 538–557 (cyclist f24–32, van f42–58), left foreground fence
  hides the lower bodies while x < ~600, right traffic-light pole x 1652–1673 (cyclist f77–79), right fence x > 1695 (cyclist f79).
- Blue flashing siren light on the van roof and grille changes from frame to frame (glow halo up to ~y 470); excluded from sizes.
- Shadows: soft contact shadows under both vehicles on the road (below y ≈ 738/743) – excluded from heights.
- Bunting, buildings, lamps are static; no other moving objects (no pedestrians/animals).
