# simulation_0261_segmented — measurement notes

**Scene:** 2D segmentation video, 1080x1920 portrait, 24 fps, 50 frames (0–49, t = frame/24, 0–2.042 s).
Pure white background. The **only object is one beige ceramic mug with a brown handle on its right**. It falls
straight down from near the top of the frame, lands on an invisible floor at image row y≈1670, rocks briefly and
rests. The camera is static (no background features, and the object's x and its rest position are constant).
No metric scale is given here. The answering session uses its prior (for example the mug height, or the drop's
acceleration) to make one m/px scale (2D video, single plane).

## Files
- `scene.json`: inventory, extents, key positions, events, camera.
- `tracks/mug.csv`: one row per frame (0–49). Columns:
  `frame, t, visible, cx_bbox, cy_bbox` (full-mask bbox centre = reference point / origin proxy),
  `cx_mask, cy_mask` (mask-pixel centroid), `body_cx` (centre of the body without the handle),
  `x0,y0,x1,y1` (inclusive bbox), `w_px,h_px` (bbox width with handle, height),
  `body_x0, body_x1, body_w_px` (body columns without the handle), `area_px`, `n_components` (number of
  non-white blobs, extra ones are tiny compression specks), `occluded` (always 0).
- `scripts/track.py`: segmentation (pixel is "object" if any channel is more than 40 below 255; keep the largest
  connected component; body columns = columns whose mask height exceeds 80% of the maximum).
  `scripts/crops.py`: 3x crops with the bbox drawn. I checked frames 0, 8, 14, 18, 19, 20, 21 and 30: the box
  hugs the whole mug, handle included, with no shadow or halo.

## Key numbers (px)
- Width with handle **111** (x 529–639) in every frame; body only **77** (x 530–606); body centre x = 568; bbox centre x = 584.
- Height: **110 at frame 0**, **96 at rest** (f24–49). During the fall it changes smoothly 110→87 (f14)→102 (f18),
  then 92 (f19), 106, 111, 108 (f20–22), 97 (f23), 96. The crops show the mug really changes apparent shape
  (it rotates/tilts slightly about a horizontal axis, so the rim and base curves change). It is not a
  segmentation artefact. If a question gives the mug's height as the prior, the rest height of 96 px
  (or frame 0's 110 px) is the cleanest. The width (111 px with handle, 77 px body) is constant and the most
  reliable size reference.
- Positions: frame 0 bbox centre (584.0, 78.5), bbox top 24, bottom 133. Rest centre (584.0, 1622.5), bbox 1575–1670.
  Total vertical drop of the centre from f0 to rest is ≈1544 px. The bottom edge goes 133→1670 (1537 px).
- x stays at 584 ±1 px, so the motion is purely vertical.

## Events
- f0 (t=0): already falling slowly (bottom edge moves 6, 13, 21, 34, 39, 48 px in successive frames). The
  per-frame steps grow about linearly (≈8.7 px/frame² on the bottom edge), which looks like free fall
  starting at or just before f0.
- Impact between f18 and f19. The bottom first reaches the floor (y1=1671) at **f19 (t=0.792 s)**, and the
  centre is lowest there (1625.5).
- f20–22: the bottom stays on the floor while the top edge rises and falls back (rock / squash or a small
  bounce). The centre's direction changes at f19 (down→up) and f21 (up→down).
- Rest from **f24 (t=1.0 s)** to the end.

## Reliability / ambiguities
- Edges are sharp. There is no visible motion blur, even at ≈150 px/frame just before impact. Edge positions
  are good to about ±1 px.
- The bbox centre includes the handle. The true 3D origin of the mug is unknown (could be the body centre,
  x=568, or the bbox centre, x=584; vertically it could be the geometric centre or the base). The vertical
  displacement is the same for any rigid point, apart from the ±10 px apparent height wobble, which moves cy_bbox
  by up to about ±7 px relative to the bottom edge. For fall kinematics before impact, the bottom edge y1 and
  the top edge y0 are also tabulated. Their average is cy_bbox.
- There is no floor, shadow or other object. Nothing is occluded.
