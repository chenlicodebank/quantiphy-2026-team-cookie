# Q269 — length of the largest towel (bottom of the 3-towel stack), metres

**Scene:** 2D, static top-down camera, 24 fps (file fps = question_fps, so no re-timing).

**Prior object:** "the cup" is the only moving object. It is the teal item the scene record calls `teal_box`, which slides along +x at constant speed. The round teal toothbrush cup is static, so the speed prior cannot refer to it.

## Scale (`speed.py`)
- I re-tracked the cup with a teal HSV mask over frames 2–71. The mean step is 14.535 px/frame (sd 0.22) and the linear-fit slope is 14.537 px/frame, which matches the scene record.
- Speed = 14.537 × 24 = 348.9 px/s.
- Scale = 0.338 / 348.9 = **9.688e-4 m/px**.

## Towel (`edges.py`, frame 0; overlay in `frames/edges.png`)
- I sampled gradient profiles along each of the 4 edges of the bottom (largest) towel (40 per edge) and fitted a line to each edge (residual sd 0.3–0.9 px). The corners are the intersections of these lines.
  - Edge angles: −24.8°, 65.3°, −25.4° and 64.0°. The towel is rotated about 25° from the counter/image axes.
  - Side lengths: 374.6 and 370.3 px (long), 181.9 and 185.7 px (short).
  - Long side = **372.5 px**, short side = 183.8 px.
- The axis-aligned bounding box of the fitted quad is 416.0 × 324.2 px.

## Readings
- Towel's own long side: 372.5 px × 9.688e-4 = **0.361 m** (short side 0.178 m).
- World-space axis-aligned extent along the counter (the towel is rotated ~25°): 416 px → **0.403 m**.
- The stated size convention (world AABB) points to 0.403. The natural meaning of "towel length" (and Blender's object dimensions) points to 0.361.
- **Answer: 0.38 m.** This sits between the two readings and is about 5% from each.

## Checks
- The scene record's rough corner estimate (365 px, ±10) agrees with the edge fit (372.5 px).
- Plausibility at this scale:
  - The towel at 0.36 × 0.18 m is a plausible folded bath towel.
  - The basin, 482 px wide, comes out at 0.47 m.
  - The drain, 35.5 px across, comes out at 3.4 cm.
- The two long sides differ by 1% (slight perspective, and the shaded side face is visible on the upper-left edge).

## Confidence
- Pixel measurements: about ±1.5%.
- The main uncertainty is the length convention (own length vs world AABB), about ±5% around the answer.
