# captured_0009x – measurement record

Video: lab capture (Orbbec Femto Mega RGB, 1280x720, 24 fps, 49 frames, t = frame/24), shown as a **SAM2 segmentation**:
everything except the ball is replaced by white. A grey "Modified with Segment Anything 2 Demo" watermark sits bottom-right
(x 1030-1280, y 690-720); it is not a scene object. Camera: static tripod (no background visible to check, but nothing suggests motion).
Intrinsics per benchmark convention: f = 0.5959 x 1280 = 762.8 px, principal point ~ (640, 360).

## Files
- `scene.json` – inventory, events, camera, apparent-size summary.
- `tracks/basketball.csv` – one row per frame 0-48: `x,y` = centre of a circle least-squares fitted to the outer
  (convex-hull) silhouette points (the reference point = visible ball centre); `diam_circle` = that circle's diameter;
  bbox of the mask (`bbox_x0..y1`, `bbox_w`, `bbox_h`); `len_major`/`width_minor` = PCA extents of the mask;
  mask centroid; `area_px`; `occluded` (1 = hand cut-out / fragments); `motion_blur`; `note`.
- `scripts/track_ball.py` (mask = saturated or dark pixels, fragments of the ball merged, circle fit),
  `scripts/overlay.py` (draws circle/centre/bbox for visual checks – checked on frames 0, 26-38, 40, 43, 46, 48: all hit the ball
  and its full extent), `scripts/finalize.py` (writes the final CSV and scene.json).

## Scene / inventory
Only one object: an **orange basketball** with black seams. A person's hand holds it at the lower left in frames 0-27;
the hand was erased by segmentation, leaving a white notch in the ball (no person, floor or walls are visible).

## Motion and events
- f0-26 (t 0-1.083 s): held, nearly still (centre drifts up ~6 px: y 186.4 -> 179.7, x ~483).
- f27 (t 1.125 s): release / start of fall (y 182.7, then 195.4 at f28, 216.3 at f29).
- Falls nearly straight down with a small rightward drift (x 483 -> 547).
- Step f35->f36 is 114 px vs 57/59 px around it: very likely a **dropped frame** in the recording (frame indices are still
  what the reference uses; keep in mind if fitting a parabola).
- f37 (t 1.542 s): lowest centre (y 657.8, bottom of ball ~y 715, image bottom 720) = **bounce** on the floor (contact at or just before f37).
- f38-46: rebound upward, apex at f46 (t 1.917 s, y 481.5); f47-48 falling again.

## Apparent size (3D cue)
Diameter (px): held 136-137 (circle fit, frames 0-27; bbox_h of held frames is cut by the notch, use diam_circle / bbox_w);
f32 ~123, f33 ~119-128, f34 ~111, f35 ~107, f36 ~99, f37 ~93 (bbox_w; blurred frames), f38-39 ~100, f42 ~105, f46 ~110, f48 ~110.
The ball shrinks as it falls and grows again on the rebound, i.e. it moves **away from the camera as it drops** (camera is
above / looking down at the drop). Relative depth Z ∝ 1/diameter (Z = f·D/d with f = 762.8 px and true diameter D from a prior),
so the held position is ~1.37x closer than the bounce point. Pixel displacements therefore mix depth change; use depth_info
or the size ratio to back-project to 3D.

## Reliability
- Frames 0-27 and 38-48: centre ±1 px, diameter ±1-2 px.
- Frames 28-31: the erased hand splits the ball into fragments; centre from circle fit to their union, ±3 px, diameter ±4 px.
- Frames 32-37: strong vertical motion blur – bbox_h and diam_circle overestimate; bbox_w (horizontal) is the better diameter
  (±3 px); vertical centre ±3 px.
- Faint grey ghost pixels near the bottom (x~520-560, y~690-720) are segmentation residue, not objects.
