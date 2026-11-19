# q_651: length of the TV stand (m). Prior: vacuum diameter = 0.438 m

Time base: fps = question_fps = 24, so there is nothing to re-time. The stand is static, so I measured it on frame 77.

**Object.** The TV stand is the long dark low console at the top centre, with the vase on its left end. Its right end is
hidden under the white pleated lamp. Right of the lamp, the pixels are floor (sunlit 178,154,110 and shaded ~100,90,80),
not stand wood (~53,42,37). So the stand ends under the lamp, at x < ~1233 px.

**Pixel length** (`profile.py`, `inner.py`, `inner2.py`):
- Left end edge: x = 710.5 px.
- Right end: found by symmetry from the stand's internal structure. Legs/brackets at 834/1066, 843/1065 and 842/1062,
  plus the inner shelf at 810/1095, put the centre at x = 952 ± 1.5. That puts the right end at x ≈ 1193.5.
  This matches the lamp centre (1192), so the lamp sits on the stand's end.
- Top-face length is 483 ± 4 px. The scene record's "~450 px" stopped at the lamp's edge, which is wrong.

**Perspective** (`persp.py`): the camera is a perspective camera looking down, not orthographic.
- The stand's front face shows as a ~10 px strip, from y = 282.5 to 292 (image centre y = 539.5). The ratio
  257 / 247.5 = 1.038 gives h_stand / D ≈ 0.037, so the stand's top is magnified 1.038x compared with the floor.
- The fitted vacuum diameter grows with distance from the image centre: diam = 119.75 + 0.0043 r px (residual 0.25 px).
  This is the side wall showing. The top disc is 119.75 px, with h/D ≈ 0.009.
- The left end face is not visible, as expected because it faces away from the centre. So the silhouette edge is
  the top edge.

**Scale and answer.** Both objects were brought to the floor plane:
length = 483 × (1 − 0.037) / (119.75 × (1 − 0.009)) × 0.438 = **1.71 m**.

**Check.**
- The naive single-scale route (482 px / 121 px mean vacuum diameter × 0.438) gives 1.745 m, about 2% higher.
- Taking the end at the lamp edge (the scene record, ~450 px) would give ~1.6 m. The symmetry analysis rules this out.

**Confidence.** About ±4%. The main uncertainty is the hidden right end, which comes from the symmetry assumption.
