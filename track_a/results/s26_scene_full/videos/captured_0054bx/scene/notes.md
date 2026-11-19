# captured_0054bx: measurement record

Lab video (Orbbec, 24 fps, 49 frames, 1280x720, 3D scene). It has been **segmented with SAM2**: everything except
four balls is pure black. There is no floor, wall, person or furniture, and the hands holding the balls were removed
too, which leaves straight cut edges on balls that are still held. A watermark "Modified with Segment Anything 2 Demo"
sits at the bottom right (x 1035-1272, y 698-712). It is not an object.
Units: pixels and seconds. Image x points right, y points down, origin at the top left. t = frame/24.

## Files
- `scene.json`: inventory, per-object summary, apparent diameters at key frames, events, camera.
- `tracks/basketball.csv`, `soccer_ball.csv`, `yellow_ball.csv`, `white_ball.csv`: one row per frame where the ball is visible.
  - `ref_x, ref_y`: **the recommended visible-centre point**. `ref_quality` is good, fair or rough (see below).
  - `diam_px`: recommended apparent ball diameter.
  - `cx, cy`: mask centroid. `x0,y0,x1,y1`: mask bounding box (inclusive). `area`: mask pixels.
  - `len_major, wid_minor, axis_deg`: full mask extent along and across its principal axis, and the axis angle (deg, image coords).
  - `encl_*`: minimum enclosing circle. `fit_*`: least-squares circle fitted to the outer contour.
    `rs_*`: RANSAC circle fit to the contour, which ignores straight cut edges. `rs_inl` is its inlier fraction.
  - `occluded`: 1 means part of the ball is hidden (removed hand or arm, the image edge, or the cut at y=584).
- `scripts/`: `track.py` (segmentation and tracking), `finalize.py` (adds the ref/diam columns), `events.py`
  (per-frame displacements used to find events), `view.py` and `overlay.py` (check images), `explore.py`.
  Rerun in this order: track.py, then finalize.py. track.py also writes label masks to `../frames/masks/` (scratch).

## How it was measured
Each pixel is classified by HSV colour: orange is the basketball, yellow (S>=65) is the yellow ball, and neutral
(S<70) is either the soccer ball or the white ball. A pixel is assigned to an object if it falls inside a search circle
around that object's predicted position. After a morphological close and hole fill, the component nearest the
prediction is kept. Pixels next to balls that were already assigned are excluded, so the yellow ball's desaturated rim
is not counted as the white ball. In f8-10 the basketball is split in two by the removed arm, so its mask is the
convex hull of the pieces. Every frame's mask outline was drawn on the image and checked by eye (frames 0-13, 17,
20-26, 30, 35-39, 44, 47, 48): the masks sit on the correct ball and cover the whole visible ball.

## Objects (all four move; nothing static is visible)
- **basketball**: orange Wilson ball, the largest object. Visible f0-48.
  - f0-4: held still at about (873,666). Occluded (fair) f0-10: a hand hides the right part, the mask is cut
    at y=584, and the bottom touches the image edge. In those frames ref = mean of the LSQ and RANSAC circle centres
    (uncertain by about ±5 px), and diam = RANSAC diameter (about 85-92 px, uncertain by about ±5 px).
  - Thrown up-left and away from the camera from f5. Its apparent diameter shrinks from 77 px (f12) to 53 px (f38-39).
  - f39: it reverses at its leftmost/highest image point (400.5, 264.8). It then moves right and down while its
    apparent size grows to about 56-57 px, so it is coming back toward the camera (probably hit a wall).
  - From f43 its image motion drops sharply, from about 6-7 px/frame to about 3 px/frame (probably a second contact).
- **soccer_ball**: white with black pentagons. Visible f0-48.
  - From f32 on, the segmented video shows it as a uniform **dark-grey disc**. The position and size continue
    smoothly, so it is the same ball.
  - Held f0-24 near (912-918, 595-619), with its right side hidden by a hand (cut at x≈933) and its top cut at y=584.
    In those frames ref = centroid of the visible part (rough: the true centre is probably about 5-15 px further right,
    since the RANSAC circle in f18-22 gives a centre near x 925 and d≈64-72). The apparent 20 px up-down wobble in
    f9-17 is mostly the hand changing which part is hidden.
  - Released about f23-24. It then rises up and slightly left, away from the camera, slowing down in the image.
    Its diameter goes from 70 px (f26) to 47 px (f48). Fully visible (good) from f25.
- **yellow_ball**: small yellow ball. Visible f17-48; f17-18 are partial at the left image edge.
- **white_ball**: off-white ball, the same size class as the yellow one. Visible f20-47. It is gone at f48: the
  segmentation lost it, and the cause is unknown.
- The two small balls were thrown together from the left, flying right, up and away from the camera.
  - At speed they are motion-blurred into elongated blobs, so their diameter = `wid_minor`, the width across the blur
    (about 47 px at f20 down to about 23-25 px at f37-48). `len_major` includes the blur streak.
  - Image apex: yellow f27, white f28. Bounces (lowest image point): yellow f37 (y 491.7), white f38 (y 470.0).
    Both then rise again; the yellow ball is close to a second apex at f48.
  - They touch or overlap in the image in f22-26 and f38-40. The split there is by colour, which is reliable.

## Events (frame / t)
- f5 / 0.208 s: basketball starts moving.
- f17: yellow ball enters. f20: white ball enters.
- f23-24 / 0.96-1.0 s: soccer ball released.
- f27 and f28: apexes of the yellow and white balls.
- **f35→f36: every object moves about 2x its normal per-frame step, so a recording frame is very likely missing
  here.** f11→f12 shows a similar 1.6x step for the basketball, but that is less certain because its occlusion ends
  there. Frame-to-frame differences across these steps are therefore inflated. Times still follow t = frame/24 by
  convention.
- f37: yellow ball bounces. f38: white ball bounces.
- f39 / 1.625 s: basketball reverses direction. f43: basketball slows abruptly.
- f47: white ball last seen.

## Camera / 3D
- The camera is assumed static (fixed lab camera). It cannot be verified because no background is left.
- Benchmark intrinsics: f = 0.5959 × 1280 ≈ 763 px, principal point ≈ (640, 360).
- There are no perspective cues (ground, horizon). Distance from the camera is ∝ 1/diam_px for each ball.
  Combine a given depth with diam_px and f to get metric size, or back-project (ref_x, ref_y) with the given depth.

## Reliability
- Unoccluded centres: about ±1 px.
- Unoccluded basketball and soccer diameters: about ±2 px. The mask includes about 1 px of soft edge;
  `fit_d` runs about 2-3 px smaller than mean(len, wid).
- Small-ball widths: about ±2-3 px, because of blur and soft edges.
- Occluded frames are noted per object above.
