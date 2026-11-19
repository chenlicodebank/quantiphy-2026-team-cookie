# captured_0016x – measurement record

Lab recording (24 fps, 49 frames, 1280x720, 3D). The background has been replaced by flat green (SAM2 watermark at
the bottom right), so this behaves like a segmentation video. Content: a near person at the left (grey T-shirt,
the **thrower**) holds a **white/black soccer ball** at waist height, swings it, and throws it underhand to a far
person at the right (dark shirt, black trousers, the **catcher**). The catcher catches it in front of her chest/waist.
There are no other objects, no floor markings and no furniture.

## Files
- `scene.json` – inventory, camera, events, summary of sizes.
- `tracks/ball.csv` – one row per frame (0-48). `x,y` = the reference point (visible ball centre). `ref_source` says how
  it was measured: `circle_fit` = RANSAC circle fitted to the ball/green boundary (hand edges excluded);
  `blob_centroid` (frames 27-36, heavy motion blur) = centroid of the blurred ball blob. `circle_*` = fitted circle
  (centre, radius, diameter) for every frame. `bbox_*`, `blob_c*`, `mask_len/mask_wid` (min-area rectangle of the ball
  mask, long/short side), `mask_h` = ball mask. `occluded_by_hand` = 1 when hands cover part of the ball. `state` =
  held_by_thrower / throw_in_hand / release / flight / catch_contact / caught_by_catcher.
- `tracks/thrower.csv`, `tracks/catcher.csv` – visible-mask centroid, bbox, area and edge-truncation flags per frame
  (the ball disk is removed from the masks).
- `scripts/` – `ball_fit.py` (seeds + RANSAC circle fit), `build_tracks.py` (final tracks + overlays), probes/sheets.
  Run them from the scene_ws folder.

## How the ball was measured, and how reliable it is
- Frames 0-26 and 37-48: the circle fit lies on the ball outline (checked on overlays). Centre is good to ~1-2 px;
  radius to ~1-2 px (r = 62-65 px in frames 0-18, dropping to ~54-56 at 22-26 as the ball swings back/down).
  Frame 21 and frame 48 needed a narrower radius window (set in `build_tracks.py`).
- Frames 27-36: the ball is smeared along its motion (blob ~125-145 x 100-130 px). The reference point is the blob
  centroid, roughly the ball centre at mid-exposure (good to ~3-5 px). The circle radius in these frames is not a
  reliable size (r 49-59). Frame 31's blob also includes some of the blurred hand (mask_len 183), so it is less accurate.
  For the ball's true size use the sharp frames: diameter ~128 px at frames 0-15 (closest to camera), ~94 px at 38,
  ~81 px at 42, ~63-73 px at 44-48 (farthest away).
- The apparent size shrinks steadily during flight, so the ball moves **away from the camera** (in depth) as well as
  to the right. Under the lab pinhole model (f = 763 px), depth ∝ 1/radius: Z(f48)/Z(f0) ≈ 64/32 ≈ 2.
  A question's depth_info or the ball's real diameter sets the metric scale: Z = f·D_real/d_px.
  Back-project with X = (x-640)·Z/763, Y = (y-360)·Z/763.
- Image path: start (316.6, 545.6) at f0; lowest point of the wind-up y=604 at f24; release ~(535, 320) at f31;
  image-space top y≈70.6 at f37-38 (x 837-871); catch contact (927, 108) at f41; end (965, 232) at f48.

## Events (frame / time)
held and swaying 0-24 (rises to y 518 at f13-15, dips to y 604 at f24) · swing forward begins f25 (1.042 s) ·
last hand contact f31 (1.292 s), free from f32 (1.333 s) · flight f32-40 · catcher's arms rise from ~f36 ·
catch contact f41 (1.708 s) · ball held and lowered f42-48.

## People
- Catcher: stands still; feet fixed (shoe bottoms y≈437, left shoe x≈925). Top of head is cut off by the frame top, so
  the visible height of 438 px (y 0-437) is a lower bound. bbox at f0 = [924,0,1237,437]. Arm motion changes the bbox
  and centroid from f36 on (the centroid moves from x≈1091 to ≈1068).
- Thrower: always cut by the left and bottom edges (only part of the torso, arms and half the head are visible), so
  the mask centroid/bbox follows the arms and is **not** a body/pelvis position. The body barely moves; the arms swing
  out to x≈490 at f30.

## Camera
Static (feet and catcher silhouette stay fixed to the pixel). No ground plane, horizon or vanishing points are visible
because of the green background. Depth comes only from apparent size or from depth_info.

## Ambiguities
- The thrower's shirt is about the same colour as the ball's white; the ball masks in held frames are limited to the
  fitted circle so the shirt is not included.
- No shadows are visible (background replaced). The ball is fully visible in flight (32-40); hands cover part of it
  in 0-31 and 41-48.
- "Release" can be taken as f31 (last contact) or f32 (first free frame).
