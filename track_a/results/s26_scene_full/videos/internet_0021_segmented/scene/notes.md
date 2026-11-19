# internet_0021_segmented — measurement record

Video: 850x478, 29.970629 fps, 107 frames (t = frame/fps). Segmentation version of internet footage: sky replaced by
flat white; buildings along the bottom (y > ~286). Scene declared 2D.

## Content
- **airplane** (only moving object): dark twin-engine jet airliner (737-like) seen side-on, nose RIGHT, flying
  left -> right across the upper half (y ~ 183-201 at f0), slight climb in the image (centre y 192 -> 186).
  Fully visible frames 0-89; nose touches the right edge from frame 90 (t=3.003 s); partially cut frames 90-104;
  last visible (tail fin only) frame 104; gone in frames 105-106.
- Static: left tall apartment blocks (x 0-432, roof median y 310, min 286), middle low pitched-roof houses
  (x 433-600, top median y 378), right apartment block (x 601-849, top median y 330) with a lit roof mast
  (x~730, top y~293) and a red vertical sign (x~735, y~365-390). Skyline per column at f0 in tracks/skyline_frame0.csv.

## Files
- scene.json: inventory, events, camera summary, key airplane sizes.
- tracks/airplane.csv (frames 0-104): cx,cy = bbox centre (visible centre); centroid_x/y = mask centroid;
  nose_x = bbox_x1 (front, valid only while nose_visible=1, i.e. frames 0-89); tail_x = bbox_x0 (rear tip of tail /
  stabiliser, valid all frames); bbox; bbox_w = nose-to-tail length (main axis ~horizontal, angle ~-178 deg);
  bbox_h = fin-top to belly/engine height; axis_len/axis_width = PCA extents; area_px; occluded=1 when cut by
  the image edge (frames 90+); bg_shift_x/y = camera-induced background shift at the plane's height relative to f0;
  *_bgcomp = coordinates minus that shift (position relative to the buildings).
- tracks/camera_affine.csv: per-frame similarity transform of the building band vs frame 0 (ORB+RANSAC).
- tracks/camera_shift.csv: phase-correlation shift of the building band (cross-check).
- scripts/: track.py (segmentation: gray<170 above y=270, largest component + nearby pieces), camera_affine.py,
  finalize.py (bg-compensation, skyline, scene.json), overlay.py (visual check -> frames/overlay.png).

## Key numbers (pixels)
- Airplane length nose-to-tail: 70 px at f0, 72 (f20), 78 (f45), 80 (f60), 84 (f70), 88 (f85); mean over frames
  0-89 = 78.3 px. Height (fin top to belly) 19-23 px. The apparent size grows ~26% over the clip (plane getting
  closer / perspective), so a single length -> scale is ambiguous; annotators most likely measured it at one frame
  (often the first, 70 px) — pick the frame the question names; mention the spread.
- Motion: image x of the plane centre 390.5 (f0) -> 782.5 (f85), ~4.6 px/frame raw; relative to background
  (tail_x_bgcomp) ~4.2 px/frame early, ~5.5 px/frame late (apparent speed rises as it approaches, as size does).
- Camera: not static — slow pan; background drifts ~-15 px in x and +4..6 px in y over the clip, scale 1.000+-0.002
  (no zoom), rotation <0.25 deg. Small vs. plane motion (~0.15 px/frame vs ~4.6 px/frame) but correct for it if
  measuring against the background.

## Events
- f0 (t=0): plane already in steady flight; no start/stop in clip.
- f90 (t=3.003 s): nose reaches right edge. f104 (t=3.470 s): last frame with tail visible; f105: plane gone.

## Reliability
- Mask edges ±1 px (slight compression blur, thin wing tips/antenna fuzz); length ±1-2 px. Centre ±0.5 px.
  Frames 90-104 centres are of the visible part only (biased left) — use tail_x there.
- Undercarriage/engines below the fuselage are included in bbox_h. Overlay check (frames/overlay.png) confirmed the
  mask covers the whole aircraft and nothing else.
