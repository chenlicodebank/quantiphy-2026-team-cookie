# q_322 — peak vertical displacement of the bread slice

Prior: toaster height = 0.166 m. 2D scene (frontal view, the toast moves only vertically in the toaster's slot,
so it is at the toaster's depth). One metres-per-pixel scale from the toaster's height. fps = question_fps = 24.

## Toaster pixel height (profile.py, base.py)
- Top: the slot cover top edge, sharp transition at y = 1115 (frame 43, toast out of the slot; x = 420-600).
- Bottom: the cream base's lower edge at its outer ends (x ≈ 280-320 and 700-740) ends at y ≈ 1398; below it there is
  a grey gradient band 1399-1411 = contact shadow on the counter (darkest next to the toaster, fades out); the black
  band 1390-1395 in the middle is the recess under the base, inside the outline.
- Height ≈ 1398 - 1115 = 283 px (±4) → scale = 0.166 / 283 = 5.866e-4 m/px.
  (The record's "276 px" used the bottom at 1390, the top of the black recess, which is not the toaster's lowest point.)

## Toast rise (toptoast.py, matches scene/tracks)
- Top edge (median over x 440-570): rest 1058 (frames 0-39), apex 843 at frame 43 (frames 42: 852, 44: 876).
  Min-based edge: 1055 → 839. Rise = 215-216 px; I use 215.5 px. Rigid, non-rotating toast, so the origin moves the same.
- Peak displacement = 215.5 × 5.866e-4 = 0.1264 m.

## Checks
- Toast size by the same scale: 232 × 196 px → 0.136 × 0.115 m, a plausible slice of bread relative to a 0.166 m toaster.
- Using the alternative toaster bottoms (1390 → 275 px, 1411 → 296 px) gives 0.130 / 0.121 m, so the result is within ±4 %.
- Frame-sampled maximum is used (frame 43); a parabola through the tops of frames 41-45 would put the true apex
  only ~1-2 px higher (<1 %).

Confidence: moderate-high; the main uncertainty is where the toaster's bounding box ends at the base (±1.5 %).
