# Q801 — height of the house (m)

Prior: speed of the horse at the back = 0.874 m/s. The horse at the back is the chestnut horse: it trails on the left, and its hooves sit higher in the image (y≈1048 against ≈1056 for the pale horse), so it is also slightly farther from the camera. fps = question_fps = 24, so no retiming.

## Scale (2D, one m/px)
- Chestnut mask-centroid x over frames 0-48 (from scene/tracks, checked; frame 49 is a loop reset and is excluded).
  A linear fit gives 3.24 px/frame; the net (x48-x0)/48 gives 3.15 px/frame. I use ≈3.20 px/frame = 76.8 px/s.
- Scale = 0.874 / 76.8 = 0.01138 m/px. Sanity check: horse hoof-to-ear height of 166 px comes out at 1.89 m, which is plausible.

## House height (measure.py)
- Roof gable apex: first non-sky row at x=538-542 is y=256.
- Wall base: the brick-to-grass transition is at y≈1038-1040 in several columns.
- Height ≈ 783 px, which gives 8.91 m at the horse's scale.

## Perspective check (persp.py)
- The house's vertical edges are parallel within noise, so the camera is level and the true horizon is near the image centre (y=960). The lawn edge at y≈986 is a finite ground edge.
- The wall base (1039) is slightly higher in the image than the chestnut hooves (1048). That points to the house standing a little behind the horse: depth ratio ≤ (1048-960)/(1039-960) ≈ 1.11. Both contact lines are partly hidden by grass, so this is uncertain. On the frames the horse looks as if it walks right against the wall.
- Answer: 9.2 m. This is the single-scale value (8.9 m) with a small allowance for the house being a little farther away than the horse. The full correction would give ≈9.9 m.

Confidence: moderate (±8%).
