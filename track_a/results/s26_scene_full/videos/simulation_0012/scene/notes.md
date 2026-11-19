# simulation_0012 — measurement record (pixels, seconds)

Video: 1920x1954 px, 61 frames, fps 22.925373 (t = frame / fps). Simulation, 2D scene. Straight top-down
(nadir) view of a garden yard. **Camera static** (sharp median background, static objects fixed). No metric
scale has been estimated: use the question's prior (e.g. bird wingspan / body length / speed) to get m/px.

## Files
- `scene.json` — inventory (moving + static objects with pixel boxes), camera, events, summary numbers.
- `tracks/bird.csv` — one row per frame 0-60:
  `x,y` body centre = midpoint of beak tip and tail tip on the body line (proxy for the rig origin);
  `body_x` = beak_x - 65 (beak tip minus half the median body length; use instead of `x` on frames flagged
  `tail_shadow_contaminated=1`); `cx,cy` mask centroid (wobbles ±5-15 px with the wing flapping);
  `bbox_*` axis-aligned mask box; `beak_x/y`, `tail_x/y`; `heading_deg` (fixed 0 = flying toward +x);
  `length_px` = beak-to-tail (bbox_w); `span_px` = extent across the body = wingspan seen from above
  (= bbox_h); `area_px`; `occluded` (always 0: nothing covers the bird).
- `tracks/bird_shadow.csv` — visible part of the bird's ground shadow: centroid, bbox, area (frames 2-50).
- `scripts/`: `bg.py` (median background), `seg2.py` (bird/shadow masks), `track.py` (tracks),
  `view.py` (overlay sheets used for checking), `steps.py` (per-frame steps), `check.py`, `probe.py` (colour stats).
  Masks are written to `../frames/masks/` (scratch, not part of the record).

## Method
Background = per-pixel median of 11 frames (bird never stays in place). Change = |frame - bg| > 25 (16 on
shaded grass). The bird's shadow on sunlit ground is a darkened, still-green copy of the ground (G-B ~ 33),
while feathers are grey/blue/black (G-B ~ 0) or the light grey tail (brighter than bg); shadow blobs are cut
out by that colour test, the remaining largest blob is the bird (closed, holes filled). All masks were
overlaid on frames and checked visually (frames 0,2,5,8,10,12,14,17,19,22,24,27,30,32,38,43,44,46,48,50,52,54,55,57,59,60).

## Objects
- **bird** (only moving object): large crow/raven-like bird, dark grey-black wings, light grey fan tail, flies
  straight toward image right along y ~ 1108-1114 from x ~ 748 (frame 0) to ~ 1716 (frame 60) — passes below the
  white flower bush at the start and just below / over the lilac bush at the end. Visible every frame.
  Body length (beak-to-tail) ~ 130 px (clean frames 123-138). Wingspan as seen from above (span_px) flaps between
  max ~ 255-258 px (frames 0-1, 17, 33, 49-50) and min ~ 125-127 px (frames 9, 25, 42, 58).
- **bird_shadow**: offset ~(-142, +30) px from the bird when fully on sunlit ground (frames 30-36); clipped by tree
  shade otherwise; invisible on shaded grass (from ~frame 50). The bird is clearly above the ground (not on it).
- Static (frame 0, ±10 px, from grid views): wooden shed (bbox 400-1375 x 0-690, cut by top edge), two barrels
  (centres (1072,705), (1153,712), diameter ~77), crate steps (825-980 x 695-790), white flower bush
  (705-780 x 868-945), lilac flower bush (1563-1780 x 945-1108), wooden hand cart (1365-1722 x 1245-1440 incl.
  handles; box body 1487-1720 x 1285-1425), wooden fence (top edge x~1560-1650 down to (1330,878)), tree canopy
  top-left (0-545 x 0-785), hedge left edge (0-380 x 940-1290), dappled tree shadows on the grass.

## Motion (descriptive only)
Beak-tip step per frame: ~7-8 px (frames 1-4), increasing steadily to ~18-20 px by frames 16-20, about constant
~19-20 px over frames 20-45, then decreasing to ~13 px (47-51) and ~7-9 px (52-60). So: accelerate, cruise,
decelerate; no stops, bounces or direction changes; vertical drift < 8 px over the clip.

## Reliability / ambiguities
- **Frame spacing**: steps 18->19 and 42->43 are double size (~37 px) for the beak, tail and centroid alike:
  the encoded video seems to skip a source frame there (61 frames at 22.93 fps ≈ 64 frames at 24 fps, so probably
  one more skip in frames 50-58 where steps are noisy). Per-frame speeds at frames 19 and 43 are therefore ~2x
  the neighbours; answering sessions should decide how to treat them (reference uses frame index as given).
- Beak tip x: ±2 px on sunlit ground; ±5 px in frames 46-60 where the dark bird is over dark shaded grass and
  the lilac bush (beak tip blends in; e.g. steps 3/18/5 px at frames 52-54).
- Tail tip / `x` / `length_px` / `bbox_x0`: inflated by the attached shadow on frames 11-18, 26-27 (flag
  `tail_shadow_contaminated`); use `body_x` there. Frames 47-49 length 137-141 (slightly inflated).
- span_px / bbox_h: ±3 px on sunlit ground; feather tips over shaded grass (frames 43-60) may be clipped by a few px;
  frames 16-18 bbox_y1 may include a few px of shadow fringe.
- Mask centroid includes the flapping wings (moves ±5-15 px relative to the body); the body centre is steadier.
- No other animals, people or vehicles move; foliage does not move noticeably.
