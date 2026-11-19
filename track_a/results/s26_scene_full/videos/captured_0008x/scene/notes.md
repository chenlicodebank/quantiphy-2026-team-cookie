# captured_0008x — measurement record

Lab video (Orbbec, 24 fps, 1280x720, 49 frames, t = frame/24), segmented: background replaced by white
(SAM2 watermark bottom-right). 3D scene. Lab intrinsics: f = 763 px, principal point ~(640, 360).

## Scene
A hand holds an orange basketball still above a small square wooden table (single grey pole leg), releases it
around frame 21, the ball falls down and slightly right in the image, bounces on the tabletop (frame 30), rises to an
apex (frame 36), bounces again (frame 41), rises to a second apex (frame 46) and is coming down again at the end (frame 48).
Camera is high, looking down obliquely at the table; it is **static** (tabletop mask bbox constant to ±1 px in all frames).

## Files
- `scene.json`: inventory, table geometry, events, camera.
- `tracks/ball.csv`: per frame (0-48): `cx, cy` = centre of circle fitted to the ball outline (reference point = visible
  ball centre), `radius_fit`, `diameter_fit` (= 2r, best apparent-size measure), mask bbox, fitted-ellipse major/minor
  axes of the mask, mask area and area-equivalent diameter, mask centroid, `occluded` flag and note.
- `scripts/track_ball.py` (HSV orange mask → largest component → hole fill → robust circle fit with outlier rejection;
  writes overlays), `scripts/table.py` (tabletop hull, leg, camera stability), `scripts/write_record.py` (run after track_ball.py; consumes and deletes its ball_raw.csv), `scripts/probe.py`.

## Ball (only moving object)
- Apparent diameter: ~114 px while held (frames 4-21, r 56.7-57.2; frames 0-3 fit ~117 because fingertips touch the
  outline); ~100-108 px near the table (frames 31-48, r 49-54) since the ball is then farther from the camera. Around
  the bounces (frames 28-31, 40-42) r dips to 47.5-51 — partly real squash/blur, partly mask trimming; use
  diameters from frames 33-38 / 44-47 (~103-108 px) as the clean near-table size.
- Events: held still frames 0-20 (cy ≈ 96-100); release between frames 20 and 21 (cy 96.0 → 99.6 → 111.7 at f22);
  first impact frame 30 (t 1.25 s, cy 421.0, lowest point); apex frame 36 (t 1.5 s, cy 306.2); second impact frame 41
  (t 1.708 s, cy 421.4); second apex frame 46 (t 1.917 s, cy 374.5); end frame 48 descending.
  Impact frames are the sampled lowest points; true contact may lie between frames (±0.5 frame).
- Image x: 518 at release → 579 at first impact → 549 at apex 1 → 569 at impact 2 → 549-550 at apex 2.

## Table (static)
Tabletop corners at frame 0 (px): far-left (479,416), far-right (689,381), near-right (753,549), near-left (434,607);
edge lengths far 213, right 180, near 324, left 196 px (strong perspective: near edge looks ~1.5x the far edge).
Tabletop bbox x 432-755, y 378-624; front edge thickness ~10-12 px. Leg: dark grey pole, x ~615-668, from y 575 to the
frame bottom (cut off), ~27-30 px wide. The ball lands on the far/middle part of the tabletop (image y ~421 is the ball
centre; the contact point is ~50 px below it).

## Reliability / ambiguities
- Centre accuracy: ~±1 px in clean frames; ±2-3 px while held (hand occludes lower-right; dark hand shadow under ball)
  and at impact frames 30, 41 (glossy table reflection merges with the mask bottom; flagged occluded=1).
- Falling frames 22-29: strong motion blur (up to ~55 px/frame); segmentation keeps a pale/brown blur ghost above the
  ball, so the mask bbox/area are inflated upward — use the circle fit (cx, cy, radius_fit), not bbox.
- Hand: mostly erased by segmentation; fingertips visible at the ball's right side frames 0-3, residue until ~21. No
  person otherwise visible.
- No metric scale is assumed; depth_info and the ball's real size (from the question) set the scale. With f = 763 px,
  Z ≈ 763·D/diameter_px gives a sanity check of depth from the ball's apparent diameter.
