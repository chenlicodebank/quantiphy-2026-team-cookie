# q1102: height of the boat (m)

The file is 25 fps and question_fps is 24. Times are converted at 24 fps, so t=1 s is frame 24 and t=2 s is frame 48.
Cx = cy = 480.

## Focal length from the eagle (focal.py)
- I used the eagle centroid track from scene/tracks/bird.csv: (470.9, 372.2) at frame 24 and (741.9, 369.8) at frame 48.
  The depths are 116.05 and 108.28 m.
- With speed 11.84 m/s held for 1 s (24 frames), the 3D displacement is 11.84 m.
  - Back-projecting both points and solving for f gives the chord solution, **f ≈ 3380-3392 px** across the
    raw, smoothed, centroid and bbox variants.
  - Making the per-frame path length over frames 24-48 (smooth cubic track, depth interpolated) equal 11.84 m gives
    **f ≈ 3413 px**. The per-frame speeds then run 11.7-11.95 m/s, which is consistent.
- I used f ≈ 3400 px, so the horizontal field of view is about 16°.
- Sanity check: an eagle wingspan of about 50 px at 116 m comes to about 1.7 m, which is plausible.

## Boat pixel height (boatpx.py, frame 24)
- The mast top is at y ≈ 303. The gray profile shows the white mast column starting at y≈306, with a dark cap above it
  at 302-305.
- The hull keel (dark band) ends at y ≈ 618-620, and the rudder/skeg bottom is at y ≈ 628-630. The rudder was also
  noted in the scene record, 16 px below the hull.
- The world AABB includes the rudder, so I took 303 to 628, giving **≈ 325 px**. Taking the hull bottom only gives
  about 315 px.
- The boat is at x≈320, near the image centre, so the off-axis correction is under 0.1 %.

## Result
H = 325 × 103.157 / 3400 ≈ **9.86 m**. The range of f gives 9.82-9.90 m.

## Second route (frame 48, depth 106.09 m)
- The record's rigid-mapped values give about 320 px from mast top to rudder bottom at frame 48 (my mast-top offset
  applied), so H ≈ 320 × 106.09 / 3400 ≈ 9.99 m.
- Height × depth agrees between frames 24 and 48 to within 1 % (31638 vs 31901 px·m).

## Answer and confidence
**Answer: 9.9 m.**

Uncertainties:
- Any hull below the waterline cannot be seen. I assumed the hull is essentially fully visible, since the rendered keel
  curve sits on the water.
- Without the rudder the height is about 9.55 m.
- Mast-top pixel reading: about ±3 px.

Confidence is moderate, about ±5 %.
