# Q749 – length of the teacher's table (m)

Prior: black cat speed = 0.714 m/s. No depth_info. fps 24 (file) = question_fps, so no re-timing.

## Scale from the cat (speed.py)
- Cat walks left→right on the desk top, y constant; the camera is static.
- Pixel speed over frames 0–49 (from scene/tracks/cat.csv; the cat's positions at frames 0, 24 and 48 were checked on the frames): torso centroid linear fit 8.96 px/frame,
  end-to-end / mean per-frame |dx| 9.106; nose-side torso edge 9.09–9.10; full-mask centroid 8.95–9.08.
  Adopted 9.05 px/frame = 217.2 px/s → 0.714 / 217.2 = 3.287e-3 m/px at the cat's depth.

## Desk length in pixels at the cat's depth (desk.py, desk2.py, desk3.py)
- I built a cat-free composite (frame 49 for x<500, frame 0 for x≥500). The wood/wall boundary was taken from the R−B chroma.
- In perspective the desk top is a trapezoid. Back edge y≈733, x 183–797 (≈614 px). Front top edge y≈764, x 70–776
  (≈706–712 px). The scene record's "720 px (75–795)" mixes the front-left and back-right corners, so it is wrong
  for this purpose.
- The cat's origin is at its body midline. Far paws touch at y≈735 and near paws at y≈741, so the midline row is ≈738.
  A linear fit of the desk width against image row (which is exact for a horizontal plane) gives 630 px at y=738;
  the raw row reading there is 636. Adopted 634 px.

## Result
634 px × 3.287e-3 m/px = 2.08 m.

Check: using the end-to-end speed (9.106) gives 2.07 m and the linear-fit speed (8.96) gives 2.11 m. A depth-row error of
±3 px changes the width by ±10 px (±1.6 %). If the front edge were used instead (≈710 px), the result would be 2.33 m.
That would be wrong because the front edge is closer to the camera than the cat. Sanity check: the cat is 186 px nose to
rump, which is ≈0.61 m, and a desk of ≈2.1 m is plausible. Confidence: moderate-high (±4 %).
