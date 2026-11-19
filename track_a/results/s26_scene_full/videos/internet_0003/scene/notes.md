# internet_0003 – measurement notes

Video: 2732x1440, 37 frames (0–36), fps 18.313953, 2.02 s. Internet footage, 2D (near top-down) view of a
pepperoni pizza being cut with a pizza cutter. Everything is in full-resolution pixels and seconds; no metric scale.
Time convention: t = frame / fps.

## Files
- `scene.json` – inventory (all objects, what distinguishes them, static sizes/positions), events, camera summary.
- `tracks/pizza_cutter.csv` – per frame: `x,y` raw image position of the cutter reference point, `x_s0,y_s0`
  the same point stabilised into frame-0 image coordinates (camera drift removed), centroid and bbox of the visible
  black plastic part, its PCA length/width/axis angle, area, per-frame step (stabilised, px) and an occlusion flag.
- `tracks/cutting_hand.csv` – per frame: back-of-hand point (raw and stabilised), template match score, skin-mask
  centroid/bbox/area of the hand, step, flag.
- `camera.csv` – per-frame similarity transform (m00..m12) mapping frame-i pixels to frame-0 pixels, its scale,
  rotation, the displacement of the image centre, RANSAC inlier count. `camera_homography.json` – full homographies
  (same direction). `camera_raw.json` – early phase-correlation test (superseded; regions disagreed because of rotation).
- `scripts/` – all scripts (common.py decoder; camera2.py camera; pizza_edge.py pizza rim fit; track.py cutter+hand;
  hand_mask.py; write_record.py builds CSVs; overlay_check.py draws stabilised tracks; view/zooms/sheet/csheet viewers).

## Camera
Handheld, NOT static. SIFT + RANSAC similarity to frame 0 (800–3000 inliers per frame). Scene content shifts upward
by ~60 px over the clip (max -61 px at frame 21), dx -14..+5 px, rotation to -0.87°, scale +0.9% by the end.
Motion of the cutter/hand should be measured with `x_s0,y_s0` (background-referenced). Raw minus stabilised differs by
up to ~65 px, i.e. comparable to 2 frames of cutter motion, so it matters.

## Pizza (static; the likely size reference)
Ellipse fitted to the outer crust edge (radial strongest intensity drop, 80 inlier rim points, outliers at cardboard
edge / hand rejected; overlay checked and confirmed by zoomed manual reading).
Frame 29: centre (1352.0, 803.7); horizontal width 1015 px (x 844.5–1859.6), vertical height 964 px
(y 321.7–1285.7); manual: left 847, right 1857, top 322, bottom 1276. In frame-0 coords centre (1356.5, 851.2),
axes 969 x 1021. Diameter: horizontal ~1015 px, vertical ~964 px, mean ~990 px. The ~5 % difference is either slight
camera tilt or a non-round hand-made pizza – note which diameter you use (annotators typically measure along the
main motion direction or horizontally). The cut runs diagonally (direction ≈ 41° below horizontal, image right-down);
along that diagonal the pizza diameter is ≈ 990 px.

## Pizza cutter (moving)
Reference point = front (up-left) extreme of the black hub guard, which sits at the wheel axle. The steel wheel is
mostly hidden by the hand and seen edge-on, so the wheel centre/contact point could not be tracked directly; the hub
guard point moves rigidly with the wheel while cutting. Visible-black-part bbox/length grow from ~45–75 px (only the
guard, frames 0–13) to ~150–190 px (handle exposed, 28–32) and >300 px when lifted (34–36, merged with blur/shadow) –
these extents are NOT the cutter's true size. The whole cutter is never fully visible (hand covers the handle).
Stabilised path: (1081,540) at f0 → (1641,1032) at f28 (straight diagonal, ~745 px net, path a bit longer due to
per-frame jitter ±3 px). Steps ~30–40 px/frame in 0–14, ~15–22 px/frame in 15–27, 4–9 px/frame 28–32 (stopped/rocking),
then lifted: 33–36 steps 11→53 px. Frames 33–36 are blurred and the cutter is closer to the camera (looks larger), so
their positions are ±15 px and not in the table plane.

## Cutting hand (moving)
Template-tracked back-of-hand point (140x140 px patch, score 0.84–0.99 for frames 0–33). Path f0 (1250,600) →
f28 (1887,1075), then turns right/up (lift) and accelerates: steps 11 px (f29) → 92 px (f36). Skin mask bbox
~360–410 x 290–310 px (fingers to wrist) in 0–33; partial in 34–36 (blur, fingers only at 36).
Overlays were checked by eye (frames/c3.png-style sheets): both points stay on the same physical spot all clip.

## Events (frame, time)
- f0 (0.000 s): cutter already rolling – stroke began before the clip.
- f0–14: steady cut; f15–27 deceleration.
- f28 (1.529 s): cutter reaches end of cut near lower-right rim, essentially stops.
- f32 (1.747 s, ±1 frame): lift-off begins (hand speeds up, moves right/up); f33–36 cutter in the air, blurred.

## Static objects
See scene.json: wine glass (bowl rim ~320 px wide, foot ~218 px), Monopoly bills (500: ~307–319 x 133–150 px;
100: ~340 x 150; 1: ~309 x 133), brown paper board (top edge ~942 px, left ~818 px), helper's hands at bottom
centre, Monopoly board/cards/houses (partial). These are ±8–15 px manual readings at one frame (static except the
camera drift; convert with camera.csv if needed).

## Ambiguities
- "Cutter position" could mean wheel centre/contact point; our point is the hub guard at the axle (within ~20 px of
  the wheel centre, constant offset while cutting, so displacements/speeds are unaffected).
- Hand vs arm: hand point is on the back of the hand, not the forearm/sleeve.
- Pizza diameter horizontal vs vertical differs by ~50 px.
- No shadows of note; motion blur only in frames 33–36.
