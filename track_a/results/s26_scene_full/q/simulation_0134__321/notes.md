# q_321 — toaster length (m)

Prior: toaster height = 0.166 m. No depth_info. fps 24 = question_fps; the toaster is static, so time doesn't matter.

The toaster is seen from the front. Its long (left-right) axis runs along the slots and is parallel to the image,
so length = horizontal pixel extent. One m/px scale comes from the toaster's own pixel height (2D ratio).

Measurements (frame 0 for the sides and bottom; frame 43 for the top, where the toast is out of the slot and the rim is clear):
- measure.py, measure2.py: grey-level row and column profiles.
  - Widest extent is the cream base/feet near y ≈ 1390: left edge x ≈ 277.5, right edge x ≈ 738.5, so **461 px**.
    The red body alone is 294-723 (430 px). The base flares out wider than the body, so the base sets the bounding box.
  - Bottom of the feet: y ≈ 1398.5. The edge is at 1397-1399 in columns x = 290, 310, 700 and 725.
- measure3.py (frame 43): the top rim is flat at y = 1115 from x 410 to 610 (the edge crossing is ≈ 1114.5).
  - Height = 1398.5 - 1114.5 = **284 px**.
- Scale: 0.166 / 284 = 5.85e-4 m/px. Length = 461 × 0.166 / 284 = **0.2695 m**.

Second-route check: the record's independent numbers (cream base 278-740 = 462 px, overall height ≈ 276 px measured from
the lip to y ≈ 1390) give 0.278 m. That route stopped at y = 1390 and missed the bottom of the feet at 1398, so it
under-measured the height. With corrected heights the result stays at 0.27 m. The length/height ratio of 1.62 is
plausible for a two-slot toaster.

Confidence: ±3 % from the edge reading (±2 px on each extent) plus some perspective, because the feet are slightly in
front of the rim.
