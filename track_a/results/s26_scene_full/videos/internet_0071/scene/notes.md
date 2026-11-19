# internet_0071 – measurement record

**Scene:** a real internet clip. It is a close-up of a white tiled bathroom wall with a white toilet-roll holder: a suction cup, a short bracket and a horizontal arm pointing right with a small upturned end tab. A right hand brings a white toilet-paper roll in from the bottom-right corner, lifts it up-left, slides it left over the holder arm, lowers it onto the arm and stops at the suction cup. The hand still holds the roll when the clip ends. 60 frames at 24.097768 fps, 3840x2160. All values are full-resolution pixels; x points right, y points down. t = frame / fps.

**Camera:** static. Phase correlation of the top band (y < 600, never covered by anything) against frame 0 gives |shift| ≤ 0.03 px in every frame (`scripts/camera_shift.json`). No background correction is needed.

## Files
- `scene.json`: inventory, static object geometry, camera, events.
- `tracks/toilet_roll.csv`: one row per frame (0–59) with these columns:
  - `cx, cy`: visible centre = centre of the bounding box. This is the reference point.
  - `bbox_x0, y0, x1, y1`: x0 is the left edge, x1 the right edge, y0 the top edge and y1 the bottom edge of the roll.
  - `length_axis_px = x1 - x0`: the roll's length along its axis. The axis is horizontal, the same as the main motion direction.
  - `diameter_px = y1 - y0`: the vertical extent.
  - `top_slope` (dy/dx of the top edge) and `left_edge_slope_dxdy`: how tilted the roll is.
  - `bottom_source`, `method`, `reliability`, `out_of_frame`, `note`.
- `tracks/hand.csv`: for frames 1–59, the bbox of the hand plus forearm, the leftmost point (thumb or fingertip) and the mask area. The hand always runs off the right and bottom edges, so it has no meaningful centre.
- `scripts/`:
  - `bg_and_camera.py`: camera check.
  - `segment.py`: rough roll and hand masks; the hand mask comes from skin saturation.
  - `roll_edges.py`: the main roll measurement.
  - `early_mask.py`, `early_zoom.py`, `early_sheet.py`: the entry phase.
  - `static_measure.py`: grout lines and the holder.
  - `build_record.py`: assembles the csv files.
  - `check_right.py`, `final_overlay.py`: visual checks.
  - The small JSONs are intermediate outputs.

## How the roll was measured
- **Frames 10–59 (`method = edges`):**
  - A translation-only template match (half resolution, template from frame 30) gives a rough position.
  - The edges are then found at full resolution on Gaussian-smoothed gray-level gradients:
    - **Top:** per-column maximum of +dy, fitted with a line; the value is taken at mid-roll.
    - **Left:** per-row maximum of +dx. The shadow to the left of the roll is dark, so this edge is crisp. Fitted with a line; value taken at mid-height.
    - **Right:** median over rows of the maximum of −dx, using only rows between the roll's top and the top of the hand.
    - **Bottom:** maximum |dy|.
  - The bottom edge has low contrast and often snaps to the lower grout line (y ≈ 1760). In frames 10–11, 25–30 and 42–49 the bottom is therefore set to top + 698.6 px, the median diameter from 24 frames with a clean bottom edge (`bottom_source = top+median_diameter`). In frames 50–59 the roll's bottom really does sit on the grout line, and the measured diameter there is 694–699.
  - In frame 36 the right edge snapped to the vertical grout line at x ≈ 2604, so it was read by eye as 2572.
  - Accuracy:
    - Left and top edges: about ±2 px.
    - Right edge: ±4 px.
    - Bottom edge: ±5 px, or about ±8 px where it was substituted.
    - Centre: about ±3 px from frame 14 on. Frames 10–13 are rated medium because the roll is still tilted.
- **Frames 0–9 (`method = manual+mask`, reliability low):**
  - The roll is tilted in 3D, so its left end face and dark core hole show. It is motion-blurred.
  - Top and right edges come from a brightness mask (`early_mask.py`).
  - The left extent (the end face) and the bottom were read by eye from 50-px-grid zooms of frames 2, 4, 6 and 8 (`early_zoom.py`). Frames 3, 5, 7 and 9 were interpolated.
  - Frame 0 is a rough box around the small blurred corner of the roll at the bottom-right.
  - In frames 0–5 the roll is cut off by the bottom edge, and in frames 0–1 also by the right edge (`out_of_frame = 1`). There the box centre is biased toward the inside of the image; do not use those centres for speed.
  - Error: ±15–30 px.
- Every track was drawn on frames and checked (`frames/roll_edges_overlay.png`, `frames/check_right.png`, `frames/final_overlay.png`). The boxes hug the visible roll.

## Roll size (for a size prior)
- Length along the axis (horizontal, the motion direction, end to end) is **≈585 px** at rest (frames 56–59: 583.5–585.2).
  - While the roll moves face-on it measures 588–606 px (frames 20–35).
  - In frames 36–48 it measures 607–620 px, because the roll turns slightly and a thin sliver of its end face adds to the right extent.
- Diameter (vertical) is **≈698–699 px**, nearly constant over the whole clip (697–712 while tilted in frames 12–16).
- Apparent size barely changes: the roll stays at about the same distance from the wall, which is nearly fronto-parallel.

## Motion summary (raw positions are in the csv; no speeds were computed)
- Frames 0–17: the roll moves up and left. The highest point is at frame 17 (top y 969.6, cy 1321.5).
- Frame 18: the left edge passes the arm tip (x ≈ 2334).
- Frames 18–41: the roll moves left at roughly −20 to −22 px/frame on the left edge, and cy slowly drifts from 1324 to 1368 to 1358.
- Frames 42–50: the roll is lowered about 47 px onto the arm (cy 1363 → 1414) while it overlaps the suction cup.
- Frames 50–56: the roll slows down.
- From frame 56: the roll is at rest (cx ≈ 1908.5, cy ≈ 1411, left edge 1616 ± 1).
- For horizontal motion, the left-edge x (`bbox_x0`) is the cleanest single coordinate. It is never occluded from frame 10 on.

## Static objects (frame 0)
- **Holder:**
  - Suction cup: x 1445–1742, y 900–1200; diameter about 297 px.
  - Knob: x 1536–1622, y 950–1133.
  - Arm: from the bracket at x 1517 to the tip tab at x 2334 (about 817 px); top y 1292, bottom y 1410 (118 px thick).
  - End tab: x 2324–2344, y 1235–1430.
- **Tiles:**
  - Horizontal grout lines run from y 688 to 681 (upper) and from y 1728 to 1772 (lower), going left to right.
  - Vertical grout lines are at x 264, 1812, 3441 (top row), 998, 2606 (middle row) and 252, 1800, 3433 (bottom row).
  - Tile pitch is 1548–1630 px wide and 1040–1091 px tall.
  - These are a little uneven because the wall is slightly turned (right side nearer, about a 5% scale gradient). The tiles' real size is unknown; do not assume one.

## Ambiguities and caveats
- Everything is white-on-white. The roll is separated from the wall by its warmer tint and by its edges and shadow. Shadows lie to the left of and below the roll, and are not included in any box.
- The hand's fingers always cover the roll's lower-right part. The roll's right edge is measured above the hand.
- In frames 43–49 the roll overlaps the suction cup and turns slightly (top-edge slope up to −0.09). The top-edge values there are good to about ±4 px.
- The hand mask (skin saturation) includes a little warm reflected glow on the wall. Treat the hand boxes as ±20 px.
- No metric scale was assumed anywhere.
