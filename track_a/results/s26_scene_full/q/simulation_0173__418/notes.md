# Q418 – height of the stone cliff (m)

Prior: airplane speed = 153.582 m/s. 2D clip, 24 fps (file fps = question_fps, no re-timing). Camera is static.

## Scale
- speed.py: median-background diff mask in the plane's band. Nose edge slope over frames 2–31 = −61.49 px/frame,
  over frames 8–31 = −61.34. Tail edge over 8–31 = −61.48. The scene record's template track gives −61.52.
  I used 61.5 px/frame = 1476 px/s, so the scale is 153.582 / 1476 = 0.1041 m/px.
- One 2D scale for the whole frame, following the benchmark's 2D convention.

## Cliff pixel height (frame 0; cliff.py plus zoomed crops)
- Base (where the rock meets the sand): rows 1008–1014 under the left and middle parts, 1026–1032 under the
  right block (x 1070–1170). I took the lowest point as about 1025–1030.
- Top of the bare rock: about 620–628, at the visible rock crest near x 850 (the record's "rock plateau" is 620).
- Treetops: about 522.
- Rock only: 1025 − 620 ≈ 405 px → **42.1 m** (answer).
- With the trees: about 507 px → 52.8 m (alternative reading).

I chose the rock-only reading because the question says "stone cliff". Also, in Blender the trees are separate
objects or particle instances, and neither counts in the mesh's bounding box.

## Check
The nose-based and tail-based speeds agree with the record's template track to within 0.3%, so the scale is
solid. The main uncertainty is which reading the question means (rock only or with trees), plus a top edge of
about ±15 px hidden under the trees.
Confidence: moderate.
