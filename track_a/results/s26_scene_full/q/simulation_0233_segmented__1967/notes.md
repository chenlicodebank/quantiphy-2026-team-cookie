# Q1967 — horizontal width of the chair (next to the blackboard)

2D segmentation clip, top-down-looking view, 1920x1080, 24 fps (file fps = question_fps = 24, no re-timing issue).
Objects: a black cat walking right along y≈531 and a static brown chair on the right (x 1538-1835). The blackboard
has been removed by the segmentation; the only chair is the one the question asks about.

## Scale (from prior: cat speed 0.714 m/s)
`measure.py` segments every frame (non-white pixels; cat = left of x=1500), tracks the cat in frames 22-49
(fully visible), output in `cat_track.csv`:
- mask centroid: 13.36 px/frame (linear fit and mean step agree; mean 2D step 13.37)
- tail-removed body centroid: 13.10 px/frame; nose front x1 (frames 0-49): 13.08-13.14; body front 13.30
- adopted 13.2 ± 0.15 px/frame = 316.8 px/s → 0.714 / 316.8 = 0.002254 m/px

## Chair
Mask bbox constant over all frames: x 1538-1834/1835 → 297-298 px horizontal (the same for thresholds 150-250),
y 496-715 (220 px). Horizontal extent includes the thin dark leg/rail tips on the left; per the AABB convention these count.

## Answer
297.5 px × 0.002254 = 0.671 m → **0.67 m**.
Second route: using the centroid speed only (13.36) gives 0.660 m; using the nose/body (13.08-13.10) gives 0.674-0.675 m.
The spread is ±1.5 %. Caveat: the chair top may be closer to the camera than the cat (perspective). That cannot be
quantified from this clip, so I used one planar scale as the 2D convention says. Confidence: moderate-high.
