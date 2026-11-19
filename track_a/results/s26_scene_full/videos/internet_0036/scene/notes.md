# internet_0036: one-dollar bill handed from one hand to another (top-down, 2D)

2160x4096 portrait video, 69 frames at 24.0625 fps (t = frame/24.0625). All values are full-resolution pixels, with
x to the right and y downward. No metric scale is assumed anywhere.

## Scene
- **bill**: a US $1 note, face up. It is the only prop. Its long axis is tilted about 44° (rising to the right), and
  the angle drifts slowly to about 47° by the end.
- **hand_giver**: the top hand and arm, entering from the top/top-right. It holds the bill, lets go around
  frame 41, and pulls back out of the frame (last visible frame 55).
- **hand_receiver**: the bottom hand and arm, entering from the bottom-left. It reaches up (frames 0-20), grips the
  bill with its thumb on the portrait (about frames 17-28), then pulls the bill down-left out of the frame (frames
  41-67).
- **backdrop**: plain light grey-blue, with soft shadows that change with the hands. There are no markings,
  furniture or ground features. No other static objects.

## Files
- `scene.json`: inventory, frame-0 bill size, events, camera notes.
- `tracks/bill.csv`, one row per frame (0-68; columns are empty for 65-68):
  - `cx,cy`: centre of the full bill rectangle (the main reference point; extrapolated when partly outside the frame).
  - `vis_cx,vis_cy`: centroid of the part inside the frame.
  - Corners: `L` = left corner, `B` = bottom corner, `R` = right corner, `T` = top corner.
  - `bbox`: bounding box of the 4 corners (not clipped to the frame).
  - `len_long_px = |R-B|`, `len_short_px = |B-L|`, `angle_long_deg`.
  - `frac_in_frame`, `frac_hand_covered` (share of the bill covered by a skin mask), and `occluded`
    (covered > 2% or partly outside the frame; covered is true in nearly every frame because a thumb is always on the
    bill).
- `tracks/hand_giver.csv`, `tracks/hand_receiver.csv`:
  - `cx,cy`: skin-mask centroid.
  - `bbox`.
  - `tip_x,tip_y`: fingertip (giver = lowest skin pixel, receiver = highest skin pixel).
  - `area_px`, `truncated_by_border` (always 1, because the arms run off the frame edge), `visible`.
- `tracks/camera.csv`: phase-correlation shift of a background patch. **Unusable**: the backdrop has no texture
  (response < 0.1).
- `tracks/bill_raw.npz`: the raw corner quads.
- `scripts/`:
  - `track_bill.py`: bill tracking.
  - `make_tracks.py`: CSVs, hand masks, overlays.
  - `summarize.py`, `probe.py`, `crops.py`, `mysheet.py`, `overlay_bill.py`, `check_corners.py`, `check_quad.py`:
    inspection tools.

## Methods
- **Bill size**: I read the corners by eye on 3x zooms of frame 0: L (410,2028), B (822,2479), R (1839,1507).
  - Long edge (bottom, along the bill's main axis) = **1407 px**; short edge = **611 px**. The ratio 2.30 is close
    to a real note's 2.35.
  - The top corner T (1427,1056) is inferred as a parallelogram. Until the hand-over, the bill's top part is bent and
    partly under the giver's fingers, so the upper-right short edge looks only about 350 px long. Do not measure the
    bill there.
  - At frame 44 the receiver has flattened the bill, and the tracked L and R corners sit within about 2 px of the
    real corners.
- **Bill track**: SIFT features inside the current bill quad (half resolution), matched to the next frame. Each
  step fits a RANSAC similarity transform (shift + rotation + scale), and the steps are chained from the frame-0
  corners.
  - Inliers: 800-2000 per step in frames 1-46, falling to 10-60 in the blurred frames 54-64.
  - Overlays checked at frames 0, 20, 36, 44, 48, 52, 55-64: the quad stays on the bill. Under motion blur
    (frames 55+) it encloses the blurred bill.
  - The tracked long edge is 1397-1412 px up to frame 50, then 1365-1394 px. That 2-3% shrink may be real (the bill
    moving or tilting slightly away) or chaining scale drift.
  - Accuracy of the centre: about ±3 px in frames 0-50, about ±10-15 px in frames 55-64. For a pixel length that
    matches the annotator convention (bumper-to-bumper along the motion), use 1407 px.
- **Hands**: skin mask = LAB a* > 131.5 at half resolution. The two hands are split by a watershed on the mask's
  distance transform, seeded from the top border (giver) and the bottom/left border (receiver).
  - Checked on overlays at 10 frames: correct except for small gaps at sleeve-shaded arm edges.
  - The centroids depend on how much arm is in view (they are truncated by the frame), so they are poor reference
    points. The fingertip points are better but jump between fingers. Hands are non-rigid.

## Motion summary (pixels, for orientation only; no speeds fitted)
- **Frames 0-40**: the bill is nearly still; its centre wanders from (1124,1768) to (1109,1830), with steps of
  0.8-5.5 px/frame.
- **Frame 41 (t = 1.70 s)**: release. From here the bill moves down-left with the receiver, roughly along
  direction (-0.52, +0.86), i.e. about 59° below the -x axis.
- **Frames 42-58**: the per-frame step grows nearly linearly, from 7 to 157 px/frame.
- **Frames 59-64**: the step levels off at 167-200 px/frame.
- **Exit**: the bill starts leaving the frame at frame 58, its centre passes x < 0 at frame 64, and its last corner
  is visible at frame 67.
- **Giver's hand**: starts moving away at about frames 42-44 and leaves the frame after frame 55.

## Camera and ambiguities
- **Camera**: assumed static. It cannot be checked, because the backdrop is featureless and shows only soft
  shadows. Treat image motion as true motion.
- **Perspective**: top-down, roughly planar. Use a single scale.
- **Similar objects**: there is only one bill; the two hands are told apart by where they enter (top vs bottom-left).
- **Occlusion**: thumbs and fingers always cover part of the bill (20-38%), so the bill centre is taken from the
  rectangle, not from visible pixels.
