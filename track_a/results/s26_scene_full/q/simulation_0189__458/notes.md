# q_458 — length of the truck (m)

2D side-view Blender render, 120 fps (file fps = question_fps, so no re-timing). Prior: box speed 0.094 m/s.

## Scale
- Box rises at constant speed. Linear fit of the scene/ track cy(frame) gives 19.194 px/s (frames 0–400), with
  19.194 / 19.201 / 19.191 px/s on sub-windows and a fit residual of 0.05 px. The motion is uniform
  (quadratic term ~0) (speed.py).
- Independent check (check_box.py): my own template match of the box interior at frames 0/100/200/300/400 gives
  −63.93 px over 400 frames, i.e. 19.18 px/s. The two routes agree.
- Scale = 0.094 / 19.19 = 4.899e-3 m/px.

## Truck length (horizontal bounding-box extent, frame 0; the truck does not move horizontally)
- Left: rear lamp/step bracket x ≈ 123 (cargo body edge 128). Right: cab side mirror x ≈ 1840 (the railing
  reaches ≈1828 and the bumper ≈1812). Row-gradient scan in measure.py, confirmed on zoomed crops frames/lc.png
  and frames/rc.png.
- Full bbox including the mirror: 1717 px → **8.41 m**. Without the mirror/step (body 128 to bumper 1812,
  1684 px) the length is 8.25 m, about 2% less. I answered with the bounding-box reading.
- Sanity check: an 8.4 m catering truck is realistic.

Confidence: high on the scale (<0.5%). The main uncertainty is which features count toward the length (~2%).
