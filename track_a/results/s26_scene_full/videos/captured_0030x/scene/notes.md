# captured_0030x – measurement record

Lab clip (real camera; 24 fps, 49 frames, 1280x720, t = frame/24). The background has been removed by SAM2:
everything except the table, the ball and its string is black, mask outlines are drawn as thin dark lines, and a
"Modified with Segment Anything 2 Demo" watermark sits at the bottom right. Benchmark intrinsics for this camera:
fx = fy ≈ 762.8 px, principal point ≈ (640, 360), horizontal FOV 80°. All values here are in pixels and frames; no metric scale.

## Scene
- **ball**: one reddish-brown sphere (it looks bright orange in the most blurred frames, 0-2). It moves the whole
  clip along a closed, roughly elliptical loop over the tabletop. Seen from above it goes clockwise: leftward along
  the front (near the camera), rightward along the back. It does about two laps (period ≈ 25 frames ≈ 1.04 s).
  It leaves an orange glow/reflection on the table just below it. There is no start, stop, release or bounce in the clip.
- **string**: a thin light-grey tether attached to the ball. Only pieces of it survive the segmentation. Its far
  visible end always lies around x 600-700, y 390-415 (above or behind the back-centre of the table), so the ball is
  probably tethered to a fixed point there (a conical-pendulum or tether loop). Use it only qualitatively.
- **table** (static): a square wooden top facing the camera squarely, on one dark pedestal leg. Image corners of the top:
  back-left (378,443), back-right (812,443), front-left (205,530), front-right (970,530). Back edge ≈ 434 px long,
  front edge ≈ 774 px (the full slab spans x 201-975), and the front edge band is ≈ 28 px thick (y 530-558).
- **table_leg** (static): x 573-620 (47 px wide), from y 559 to the bottom of the frame.
- **Camera**: static (the median background fits every frame). The side edges of the tabletop meet at a vanishing
  point ≈ (605, 329), so the horizon is at y ≈ 329 and the camera is pitched down about 2°.

## Files
- `scene.json`: inventory, static geometry, camera/perspective cues, events, size ranges.
- `tracks/ball.csv`: one row per frame (0-48). The ball is visible in every frame.
  - `ref_x, ref_y`: the ball centre (the reference point to use).
  - `diam_px`: apparent diameter. `diam_reliable` = 0 when the image step is ≥ 30 px/frame (heavy blur).
  - `ref_method`: how the centre and diameter were found.
  - `occluded`: frames 15-19, where the bottom of the ball is cut at the table's far edge.
  - `motion_blur`, `img_step_px` (largest step to a neighbouring frame), `est_blur_px` (≈ 0.37 × step).
  - Raw mask data: `circle_diam_px`, `fit_cx/fit_cy`, `mask_cx/cy`, `bbox_*`, PCA `length_px/width_px`, `height_px`,
    `area_px`, `equiv_diam_px`, ellipse axes and `axis_angle_deg`.
- `tracks/string.csv`: bounding box of the string pieces, the far tip (the string pixel farthest from the ball) and
  `visible_len_px` per frame. It is blank where no string was found (5 frames).
- `scripts/`:
  - `bg.py`: median background.
  - `track.py`: the masks, both tracks, and the overlays it writes to frames/ov*.png.
  - `static.py`: the table extents.
  - `summary.py`: the events and scene.json.
  - `probe*.py`, `check.py`: colour probes and checks.

## Method
The foreground is |frame − median background| > 50, keeping only saturated pixels for the ball. Low-saturation grey
pixels are the string. The ball's convex hull is the mask. The orange glow under the ball often merges into the mask,
which inflates bbox_h, ellipse and area by up to about 25 px vertically. Because of that, the centre and diameter come
from a least-squares circle fitted to the **upper arc** of the mask only (the top 55 %). In frames with strong
horizontal blur (bbox_w − bbox_h > 10: frames 0-2 and 25-29) the centre is the bbox centre and the diameter is the
vertical extent. I checked the overlays (circle, bbox, mask, string) for all 49 frames by eye: they sit on the ball.

## Reliability and ambiguities
- **Centre**: about ±2 px in sharp frames and ±3-4 px in blurred ones. Frames 3-5 and 29-31 move diagonally and fast,
  so their fitted circle is still a bit stretched (diameter 74-84 px is too big; the true front value is ≈ 63-69 px).
- **Apparent diameter, reliable frames**:
  - back of the loop: ≈ 41-50 px (frames 12-19 and 38-45)
  - left end: 55-61 px (frames 8 and 33)
  - right end: ≈ 60 px (frames 22-23)
  - front: ≈ 63-69 px (vertical extent in frames 0-2 and 26-28)
  - The size grows toward the front, which is consistent with depth (nearer = bigger). The far-side sizes may still
    include up to about 10 px of horizontal blur (the step there is about 30-40 px/frame).
- **Frames 15-19**: the ball's lower silhouette is flat at the table's far edge (y ≈ 442). Either the ball is partly
  hidden behind the edge or the mask is cut there; the bottom-based extents (bbox_h, area) are not usable.
- **Frame 11 → 12** jumps 50 px in x (other back-side steps are about 33 px), so frame 11 may be slightly off: its
  mask touches the string.
- **Glow**: the orange patch on the table under the ball is a reflection or lighting effect, not part of the ball.
- **Depth**: the ball's depth changes a lot around the loop (its apparent size is about 1.5× bigger at the front than
  at the back). A question's depth_info is needed to turn pixels into metres. Use pinhole back-projection:
  X = (u − 640)·Z/762.8, Y = (v − 360)·Z/762.8.
