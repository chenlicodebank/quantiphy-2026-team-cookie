# simulation_0232 – measurement record

Video: Blender render, 2D scene, 1920x1080, 24 fps, 50 frames (t = frame/24, 0 … 2.0417 s).
Units: pixels (x right, y **down**, origin top-left) and seconds. No metric scale was assumed.

## Scene
Classroom, frontal view of a grey wall. Static camera (no pan/shake: median-background differencing leaves no
residue on static objects in any frame). Two moving objects:

1. **cat** – black cat with white paws and light face, the only animal. Walks left→right along the top of the long
   wooden teacher desk during the whole clip (frames 0–49, already moving at frame 0, still moving at 49).
2. **arrow** – thin light-grey arrow (fletching at the rear, pale separate-looking arrowhead), flies left→right on an
   arc across the wall, high above the cat. Visible frames 7–41 (enters left edge at 7, fully in frame 10–37/38,
   leaves right edge, last visible 41, gone at 42). Apex (highest point) at frame 23 (ref ≈ (1030, 340.5)); vertical
   direction reverses between frames 23 and 24. Passes ~150 px above the cat around frames 14–16; no contact.

Static: teacher desk, wall clock, two dark-red chairs (foreground, backs to camera), orange chair against the
right wall, small student desks at left/right edges, four ceiling light panels, wall/floor junction (y≈950).
Pixel positions/extents are in scene.json → static_objects (read from grid views of frames, ±3 px).

## Files
- `scene.json` – inventory, reference-point definitions, size summaries, static object extents, events, camera.
- `tracks/cat.csv` – every frame 0–49: `cx,cy` = centroid of the torso mask (tail and legs removed by a 15 px
  morphological opening) – used as the cat's root/reference point; `mask_cx,mask_cy` = centroid of full mask;
  full-mask bbox (`bbox_*`, includes the raised tail, so the top y≈596–606 is the tail tip); `torso_*` box;
  `body_len` = nose to rump (tail excluded); `head_top_y`, `height_no_tail` = ears to paws; `area`; `occluded` (0).
- `tracks/arrow.csv` – frames 7–41: `ref_x,ref_y` = **recommended reference point** = arrow midpoint computed as
  fletching end + L/2 along the shaft with constant L = 132 px (`ref_method`; frames 7–9 use tip − L/2 since the
  tail is still outside the image; frame 7 tip read by eye); `cx,cy` = midpoint of the visible mask ends;
  `tail_*`, `tip_*` = detected end points; bbox; `length` = visible length along the shaft; `length_full`=1 where the
  whole arrow was segmented; `width`; `angle_deg` (CCW from +x, image-up positive: +13° rising → 0 at apex → −18°);
  `cut_by_frame_edge`/`occluded` = 1 for frames 7–9 and 38–41.
- `scripts/` – `bg.py` (median background, writes frames/bg.png), `track.py` (segmentation + tracking, overlays
  frames/ov_XX.png), `arrow_ref.py` (robust arrow midpoint), `arrow_crops.py` (amplified-diff check crops),
  `probe.py` (diff dump), `make_scene.py` (scene.json). Run in that order.

## Sizes (pixels)
- Cat: bbox incl. tail median 199.5 w × 145 h; nose–rump length median 186 (160–199, varies with gait and mask);
  ears-to-paws height median 106 (98–112); torso height ~85. Light face/nose blends into the wall, so the front
  extent may be under-measured by ~5 px.
- Arrow: length 132 px (median 132.5, 127–135 in well-segmented frames 17–38); in frames 10–16 and 28–31 the pale
  arrowhead is partly invisible, so visible length is 108–126 there. Thickness ~4 px shaft, 8–13 px with fletching
  and blur. Arrow pixel length stays constant over the flight → it moves in a plane parallel to the image (no depth
  change visible).
- Teacher desk top: x 75–795 (720 px long), back edge y≈738, front edge y≈767; legs reach the floor at y≈1025
  (top-to-floor ≈258 px). Clock: centre (1762, 293), diameter ≈113 px.

## Motion observations (no fitting done)
- Cat: x of torso centroid 255.9 → 702.1 over frames 0–49 (~9 px/frame, step size oscillates 5–12 px with the
  gait); y constant within ±3 px. Cat nose reaches the desk's right end (x≈795) at frame 49.
- Arrow: per-frame displacement of ref grows from ~69 (frame 10) to ~76 (frame 18) then decreases steadily to ~50
  (frame 35) and ~40 (frames 38–41); horizontal step falls from ~73 to ~31 px/frame and the vertical step changes
  from −33 (up) to +25 (down) – not a constant-gravity parabola, so the answering session should fit what its
  question needs directly from the per-frame points.

## Reliability / ambiguities
- Cat reference: torso centroid ≈ the Blender root; ±3 px jitter from leg/tail motion. Tail swings change bbox_x0.
- Arrow: very low contrast (diff 15–90 grey levels); ends ±3 px in frames 17–38, ±8 px in 10–16 and 28–31.
  Frames 7–9 (entry) are least reliable: the arrowhead is faint and a bright vertical wall band at x≈60–100 adds
  noise; refs there are extrapolated off-screen/near the edge (frame 7 ref x≈−26). Exit frames 39–41 use the
  well-visible fletching end and are good. The Blender origin of the arrow may not be its geometric midpoint –
  if a question implies otherwise, tail_/tip_ columns allow other points.
- Desk-top flicker: small difference blobs on the desk top (y≈730–743) are the cat's paws/contact shadows, not
  separate objects.
- 2D assumption: cat (on the desk by the wall) and arrow may be at somewhat different depths; nothing in the
  image measures that.
