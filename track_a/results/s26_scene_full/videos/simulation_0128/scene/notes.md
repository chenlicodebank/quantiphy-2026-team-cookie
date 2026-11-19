# simulation_0128 — measurement record (pixels, seconds)

Video: Blender render, 2D scene, 1920x1080, 24 fps, 38 frames (t = frame/24, 0 … 1.5417 s).
Camera: **static** (static-region frame differences < 0.3 grey levels). Fronto-parallel view of a hall back wall
with a large gridded window; floor recedes in perspective, but both moving objects move in image planes
(ball purely vertical, forklift purely horizontal, neither changes apparent size), so a single px scale per object
plane applies (2D convention: one metres-per-pixel scale from the prior's object).

## Objects
- **red_ball** (moving): small red sphere, x ≈ 962.5 (in front of the central window mullion). Diameter
  22.5 px (area-equivalent; 21.7–23.1 per frame, bbox width always 22 px). At rest frames 0–1 at (962.5, 253.1),
  then falls straight down (x constant ±0.2 px), speeding up the whole clip; at frame 37 centre y = 977.2
  (724 px below start). No bounce, impact or floor contact inside the clip.
- **forklift** (moving): orange/black Toyota counterbalance forklift, bottom-left foreground, forks pointing +x.
  Rigid horizontal translation only (y shift 0, tyre-bottom and guard-top rows identical in frames 0 and 37).
  Frame-0 bbox x 125.5–538.0, y 814.0–1055.5 → length rear-to-fork-tip 412.5 px (±4; fork-tip edge is
  thin/anti-aliased: 538 at f0, ~653 at f37 − 120.5 = 533 → length 408–413), height tyre-bottom-to-
  overhead-guard-top 241.5 px (±2). Rear to mast/carriage front ≈ 295 px. Wheels (visual, ±4 px): rear tyre
  ⌀≈66 centred (166,1023), front tyre ⌀≈78 centred (352,1019), wheelbase ≈186 px. At rest frames 0–1, then drives
  right with increasing speed until the end; total shift 120.5 px by frame 37.
- Static: back-wall window x 686–1233 (547 px), y 326–870 (544 px), vertical mullions at x 717.5, 798, 879,
  959.5, 1040, 1121, 1201.5 (spacing ≈80.7 px), horizontal bars at y 418.5, 511.5, 604.5, thick transom 697–713,
  743.5 (row spacing ≈93 px). Floor/back-wall junction y≈873. White double floor stripes converging toward the
  back wall (perspective), side steel galleries with light strips, big grey pillars at x<70 and x>1850, dark roof
  trusses with ridge at x≈960.

## Events
- Frames 0 and 1 identical: both objects at rest. Both start moving at frame 2 (t = 0.0833; release ≈ frame 1,
  t = 0.0417): ball dy = 1.9 px, forklift dx = 0.3 px in frame 2.
- No other events (no impact, bounce, stop or direction change) before the clip ends at frame 37.

## Files
- `scene.json`: inventory, extents, events, camera.
- `tracks/red_ball.csv`: per frame: centre (cx, cy) = centroid of the convex-hull-filled red mask (the sphere centre
  = origin), bbox, width/height px, diam_area_px (2·sqrt(area/π)), diam_circle_px (min enclosing circle), occluded=0.
  Precision ≈ ±0.3 px on the centre; width/height values jump by 2 px (frames look 2-px quantised in places).
- `tracks/forklift.csv`: per frame: shift_x_px (primary: masked template match of the rear half of the forklift —
  counterweight, seat, guard posts — taken from frame 0 with the background pixels masked out, sub-pixel parabola),
  ref_x/ref_y = bbox centre (frame-0 bbox moved by shift), ground_y, bbox, length/height, plus two cross-checks:
  rear_edge_x_measured (orange counterweight edge, rows 965–995; 2-px quantised) and template_shift_x_check (unmasked
  template, biased toward 0 for small shifts in frames 2–5). Primary vs rear-edge agree within ~1 px; final shift
  120.54 vs 120.0 (edge) vs 120.21 (template). Per-frame increments are noisy at ~±0.3 px, so fit a smooth motion
  rather than single-frame differences if needed. Forklift root position is not visible; for a rigid translation
  any point's displacement equals the root's.
- `scripts/`: measure.py (ball + raw forklift template), forklift.py (edges), forklift_shift.py (primary masked
  shift), forklift_extent.py / profiles.py (extents), static.py (window grid), wheels.py (failed dark-run attempt;
  wheel numbers come from visual crop), build_record.py (CSV assembly + overlays checked visually in frames/).

## Ambiguities / reliability
- Ball: clean, unoccluded, no motion blur problem; its shadow is not visible. High reliability.
- Forklift: fork tip low contrast against the light floor (±3–4 px); rear wheel rotates (excluded from the
  template mask). Rear-edge orange mask also catches a static orange-ish strip near x≈70 (excluded by x>100).
- Depth: the ball and forklift lie in different planes (forklift in the near foreground, ball in front of the back
  wall); the 2D convention uses one scale, but a size prior on one object may not transfer exactly to the other.
- The ball's apparent diameter is constant (no depth change); the forklift's apparent size is constant.
