# simulation_0076: measurement record

**Scene.** This is a Blender render tagged 2D: 1920x1080, 24 fps, 72 frames, 3.0 s, with t = frame/24. The camera looks straight down on a flat, untextured grey floor. Two adult men walk side by side in straight lines from right to left (toward -x), and both are visible in every frame:
- **man_black_shirt**: black T-shirt, maroon trousers. He is the upper walker (head at y ≈ 405–415) and the slower one, at about 12.2 px/frame for the head.
- **man_white_shirt**: white T-shirt, blue jeans. He is the lower walker (head at y ≈ 600–612) and the faster one, at about 15.8 px/frame for the head.

Nothing else is in the scene: no props and no floor markings. Each walker has a faint soft circular shadow halo around them, which is excluded from the masks.

## Files
- `scene.json`: inventory, pixel sizes, events, camera notes and a pair-distance table.
- `tracks/man_black_shirt.csv` and `tracks/man_white_shirt.csv`: one row per frame (0–71). Columns:
  - `cx,cy`: mask centroid.
  - `x0,y0,x1,y1,bbox_w,bbox_h`: bounding box of the mask (inclusive pixels).
  - `area`: mask area in pixels.
  - `main_axis_len`, `cross_width`, `main_axis_deg`: PCA extents of the mask, with the axis angle in image degrees in [0,180).
  - `head_x,head_y,head_diam`: centroid of the brown hair blob and its equivalent diameter.
  - `pelvis_est_x,pelvis_est_y`: see below.
  - `occluded`: always 0, because the masks never merge.
- `scripts/`:
  - `bg.py`: per-pixel median background over every 4th frame (`bg.png`).
  - `track.py`: segmentation, tracking and overlays.
  - `feet.py`: a failed attempt to find planted feet; `feet_raw.csv` is not reliable.
  - `summary.py`: writes `summary_out.json` with path lengths and pair distances.

## Method and reliability
- **Masks.** A pixel belongs to a mask if it differs from the median background by more than 28 in any channel, after a 3x3 morphological open. Connected components are assigned to the nearest previous centre. Overlays on frames 0, 24, 48 and 71 confirm that each mask covers its whole person (head, arms, legs, shoes) and leaves out the shadow halo. Extents are good to about 2 px.
  - Along the walking direction, `bbox_w` / `main_axis_len` swing with the stride and arm swing (100–243 px).
  - Across the walking direction, `bbox_h` (≈140–154 px) is the shoulder/arm span and is nearly constant.
  - Body height cannot be measured in this top-down view.
- **Head track.** This is the cleanest point. The white-shirt man's head is precise to about 1 px. The black-shirt man's dark hair sits against a black shirt, so his head track has occasional 3–5 px jitter, for example at frames 19–20 and 23–25. Smooth over a few frames if needed.
- **Mask centroid.** It follows the body but oscillates with the gait: per-frame steps range from about 6 to 20 px over a cycle of roughly 12 frames.
- **Perspective / parallax (the main ambiguity).** The camera is a perspective camera over the floor, so points higher above the ground project farther from the image centre.
  - The head's horizontal offset from the body flips sign as each walker crosses x = 960, which places the principal point at about the image centre.
  - The head path is about 8.5% longer than the centroid path (black 853 vs 785 px net; white 1106 vs 1019 px net).
  - The pelvis (the benchmark origin) sits lower than the head, so its image displacement is smaller than the head's. I estimate `pelvis_est = centre + 0.94 × (head − centre)`, taking centre = (960,540). The factor 0.94 is rough, from the head/centroid parallax ratio. Expect about ±3% error in the absolute pelvis scale.
  - Ratios between the two men are almost the same whichever point is used, because they have similar heights and are at the same depth. If the given prior is a speed or distance of one man, the scale taken from the same kind of point cancels most of this effect. Use the same column for the prior and for the target.
- **Motion events.** Frames 0 and 1 are almost identical (step under 1 px), and walking starts from frame 1 to 2. After that both men move continuously to frame 71, with no stops, turns or contact. Their headings are almost exactly -x (head y drifts only ±6 px with the gait).
  - Net head displacement over frames 0–71: black 852.9 px, white 1106.2 px.
  - Mean head step over frames 2–71: black 12.25 px/frame, white 15.83 px/frame.
  - Distance between the men grows from about 199 px (heads, frame 0) to 328 px (frame 71). The table is in `scene.json` and the per-frame values can be computed from the CSVs.
- **Camera.** It is assumed static. The floor has no texture, so a pan cannot be measured, but nothing suggests one.
