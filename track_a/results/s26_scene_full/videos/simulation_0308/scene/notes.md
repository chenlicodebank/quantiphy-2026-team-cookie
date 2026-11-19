# simulation_0308 – measurement record (pixels, seconds)

Video: 2560x1440, 24 fps, 72 frames (t = frame/24, 0 … 2.958 s). Blender render, 3D scene.
Content: one blue whale swimming slowly above a flat sandy sea floor with animated caustics, casting a
dark shadow on the floor. Small seabed props (seaweed, coral, a spotted rock) lie under the whale.
Camera is static (elevated, oblique, looking down). No horizon is visible.

## Files
- `scene.json` – inventory, camera, static props, manual fluke-tip points, events, file index.
- `tracks/whale.csv` – every frame 0-71: centroid of the colour mask (cx_px, cy_px), bbox (x0,y0,x1,y1,w,h),
  PCA major-axis length / minor width of the mask, axis angle, mask area, `occluded_or_cut` (1 = mask touches the
  image border: tail cut by the bottom edge in frames 8-39), bbox centre, `head_top` (topmost mask pixel row, mean x
  of that row), `far_pt` (mask pixel farthest from head_top) and their distance.
- `tracks/whale_shadow.csv` – the same mask measures for the floor shadow (flag = 1 when cut by the bottom edge or
  touching the whale in the image).
- `tracks/camera_shift.csv` – phase-correlation shift of the top 300 rows vs frame 0.
- `scripts/` – `track.py` (all tracks + overlays), `tailcrops.py` (grid crops for manual fluke-tip reading),
  `probe.py`/`probe2.py` (colour sampling), `show_cols.py`.

## Method
- Whale mask: (B−G>36 & B−R>85) | saturation>0.62 | (R<62 & B−R>40), open 7, close 41, keep large components,
  fill holes. Background sand never exceeds sat 0.58. Overlays (frames 0,10,…,70,71) were inspected: the mask covers
  the blue back, navy underside and left pectoral fin well.
- Shadow mask: B−R<35 & mean<125, minus the whale mask.
- Camera: phase correlation shift ≤0.16 px in every frame ⇒ static. (Mean abs difference ~50 is caustic animation
  and render noise.)

## Reliability / caveats
- **Origin**: the whale's world origin is not visible. `head_top` gives the cleanest translation signal: a smooth,
  nearly uniform path from (1180,390) at f0 to (1000,298) at f71 (≈205 px, ~2.9 px/frame, up-left = forward and
  slightly away from camera). Its x is a row mean (±3 px jitter). The mask centroid/bbox centre are contaminated
  by tail beats, the tail being cut (f8-39) and the missed pale fluke (late frames) – use them with care.
- **Missed pale parts**: pale/white fluke undersides (frames ~44-71) and part of the right pectoral fin are
  background-coloured and are partly missing from the mask; bbox x1 and far_pt underestimate the tail in frames
  ≥60 (e.g. f71 mask x1 = 1834 vs true fluke tip ≈1992). Use `manual_fluke_tip_px` in scene.json (f0, 52, 58, 64,
  68, 71; ±8 px). In frames 8-39 far_pt is the bottom-edge cut, not the tail tip.
- In frames ~50-71 the mask also picks up the dark red coral/seaweed under the whale (small blob near
  x 1210-1360, y 720-780) – slightly biases bbox_y1/centroid.
- **Length**: head-top to fluke tip = 1440 px at f0 (whole whale visible, tail swept down-right); 995 px at f71
  (tail raised). Both are foreshortened by the oblique 3D view; pixel length depends on pose.
- Shadow: tail of the shadow leaves the bottom edge in frames 0-66; pectoral-fin portion partly lost in 9-33
  (bbox jumps at f34). Shadow is on the floor plane, light from upper left.
- Seabed props: tiny (≈35-170 px), static, only uncovered from ~f48-60; bboxes at f71 in scene.json.
- Perspective: floor recedes toward the top of the image (caustic pattern compresses upward); no lines or vanishing
  points available. Focal length unknown – derive from depth_info + a known size if given.

## Events
Whale swims continuously all clip (no start/stop). Tail down-stroke: fluke leaves bottom edge f8, back in view f40;
up-stroke f40-71 (fluke tip y 1130→381). From ~f50 the whale rolls, showing its pale belly and right pectoral fin.
